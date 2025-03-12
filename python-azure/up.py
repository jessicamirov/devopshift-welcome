#!/usr/bin/env python

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.core.exceptions import ResourceNotFoundError

subscription_id = "3f79a68d-cf0d-4291-a31f-185897f7fda1"
resource_group_name = "jessica-resource-group"
location = "eastus"
vnet_name = "jessica-vnet"
subnet_name = "jessica-subnet"
ip_name = "jessica-ip"
nic_name = "jessica-nic"
vm_name = "jessica-vm"
admin_username = "ubuntu"
ssh_key_path = "/home/ubuntu/.ssh/id_rsa.pub"

credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

# ✅ Check if Resource Group exists
try:
    resource_client.resource_groups.get(resource_group_name)
    print(f"Resource Group '{resource_group_name}' already exists.")
except ResourceNotFoundError:
    print(f"Creating Resource Group '{resource_group_name}'...")
    resource_client.resource_groups.create_or_update(resource_group_name, {"location": location})

# ✅ Check if Virtual Network exists
try:
    network_client.virtual_networks.get(resource_group_name, vnet_name)
    print(f"Virtual Network '{vnet_name}' already exists.")
except ResourceNotFoundError:
    print(f"Creating Virtual Network '{vnet_name}'...")
    vnet_params = {"location": location, "address_space": {"address_prefixes": ["10.0.0.0/16"]}}
    network_client.virtual_networks.begin_create_or_update(resource_group_name, vnet_name, vnet_params).result()

# ✅ Check if Subnet exists
try:
    subnet = network_client.subnets.get(resource_group_name, vnet_name, subnet_name)
    print(f"Subnet '{subnet_name}' already exists.")
except ResourceNotFoundError:
    print(f"Creating Subnet '{subnet_name}'...")
    subnet_params = {"address_prefixes": ["10.0.1.0/24"]}
    subnet = network_client.subnets.begin_create_or_update(resource_group_name, vnet_name, subnet_name, subnet_params).result()

# ✅ Check if Public IP exists
try:
    ip_address = network_client.public_ip_addresses.get(resource_group_name, ip_name)
    print(f"Public IP '{ip_name}' already exists.")
except ResourceNotFoundError:
    print(f"Creating Public IP '{ip_name}'...")
    ip_params = {"location": location, "sku": {"name": "Standard"}, "public_ip_allocation_method": "Static"}
    ip_address = network_client.public_ip_addresses.begin_create_or_update(resource_group_name, ip_name, ip_params).result()

# ✅ Check if Network Interface exists
try:
    nic = network_client.network_interfaces.get(resource_group_name, nic_name)
    print(f"Network Interface '{nic_name}' already exists.")
except ResourceNotFoundError:
    print(f"Creating Network Interface '{nic_name}'...")
    nic_params = {
        "location": location,
        "ip_configurations": [{
            "name": "jessica-ipconfig",
            "subnet": {"id": subnet.id},
            "public_ip_address": {"id": ip_address.id},
            "private_ip_allocation_method": "Dynamic"
        }]
    }
    nic = network_client.network_interfaces.begin_create_or_update(resource_group_name, nic_name, nic_params).result()

# ✅ Check if VM exists
try:
    compute_client.virtual_machines.get(resource_group_name, vm_name)
    print(f"VM '{vm_name}' already exists.")
except ResourceNotFoundError:
    print(f"Creating VM '{vm_name}'...")
    with open(ssh_key_path, "r") as f:
        ssh_key = f.read()

    vm_params = {
        "location": location,
        "hardware_profile": {"vm_size": "Standard_B1s"},
        "os_profile": {
            "computer_name": vm_name,
            "admin_username": admin_username,
            "linux_configuration": {
                "disable_password_authentication": True,
                "ssh": {"public_keys": [{"path": f"/home/{admin_username}/.ssh/authorized_keys", "key_data": ssh_key}]}
            }
        },
        "storage_profile": {
            "image_reference": {
                "publisher": "Canonical",
                "offer": "UbuntuServer",
                "sku": "18.04-LTS",
                "version": "latest"
            },
            "os_disk": {
                "caching": "ReadWrite",
                "create_option": "FromImage",
                "managed_disk": {"storage_account_type": "Standard_LRS"}
            }
        },
        "network_profile": {
            "network_interfaces": [{"id": nic.id}]
        }
    }
    compute_client.virtual_machines.begin_create_or_update(resource_group_name, vm_name, vm_params).result()
    print(f"VM '{vm_name}' created successfully.")

print("All resources are ready!")
