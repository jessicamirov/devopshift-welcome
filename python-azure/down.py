#!/usr/bin/env python

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient

subscription_id = "3f79a68d-cf0d-4291-a31f-185897f7fda1"
resource_group_name = "jessica-resource-group"

credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

# Resource IDs from up.py (these are saved for down.py)
resource_ids = {
    "vm_id": "jessica-vm",
    "nic_id": "jessica-nic",
    "ip_id": "jessica-ip",
    "subnet_id": "jessica-subnet",
    "vnet_id": "jessica-vnet"
}

# Delete VM
print(f"Deleting VM '{resource_ids['vm_id']}'...")
compute_client.virtual_machines.begin_delete(resource_group_name, resource_ids["vm_id"]).result()

# Delete Network Interface
print(f"Deleting Network Interface '{resource_ids['nic_id']}'...")
network_client.network_interfaces.begin_delete(resource_group_name, resource_ids["nic_id"]).result()

# Delete Public IP
print(f"Deleting Public IP '{resource_ids['ip_id']}'...")
network_client.public_ip_addresses.begin_delete(resource_group_name, resource_ids["ip_id"]).result()

# Delete Subnet
print(f"Deleting Subnet '{resource_ids['subnet_id']}'...")
network_client.subnets.begin_delete(resource_group_name, resource_ids['vnet_id'], resource_ids["subnet_id"]).result()

# Delete Virtual Network
print(f"Deleting Virtual Network '{resource_ids['vnet_id']}'...")
network_client.virtual_networks.begin_delete(resource_group_name, resource_ids['vnet_id']).result()

# Delete Resource Group
print(f"Deleting Resource Group '{resource_group_name}'...")
resource_client.resource_groups.begin_delete(resource_group_name).result()

print("All resources deleted successfully!")
