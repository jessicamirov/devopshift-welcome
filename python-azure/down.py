#!/usr/bin/env python

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.core.exceptions import ResourceNotFoundError

subscription_id = "3f79a68d-cf0d-4291-a31f-185897f7fda1"
resource_group_name = "jessica-resource-group"

credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

resource_ids = {
    "vm_id": "jessica-vm",
    "nic_id": "jessica-nic",
    "ip_id": "jessica-ip",
    "subnet_id": "jessica-subnet",
    "vnet_id": "jessica-vnet"
}


def safe_delete(callable, *args):
    """Helper function to safely delete a resource."""
    try:
        callable(*args).result()
        print(f"Deleted {args[1]} successfully.")
    except ResourceNotFoundError:
        print(f"{args[1]} does not exist, skipping.")


# Delete VM
print(f"Deleting VM '{resource_ids['vm_id']}'...")
safe_delete(compute_client.virtual_machines.begin_delete, resource_group_name, resource_ids["vm_id"])

# Delete Network Interface
print(f"Deleting Network Interface '{resource_ids['nic_id']}'...")
safe_delete(network_client.network_interfaces.begin_delete, resource_group_name, resource_ids["nic_id"])

# Delete Public IP
print(f"Deleting Public IP '{resource_ids['ip_id']}'...")
safe_delete(network_client.public_ip_addresses.begin_delete, resource_group_name, resource_ids["ip_id"])

# Delete Subnet
try:
    subnet = network_client.subnets.get(resource_group_name, resource_ids['vnet_id'], resource_ids["subnet_id"])
    print(f"Deleting Subnet '{resource_ids['subnet_id']}'...")
    safe_delete(network_client.subnets.begin_delete, resource_group_name, resource_ids['vnet_id'], resource_ids["subnet_id"])
except ResourceNotFoundError:
    print(f"Subnet '{resource_ids['subnet_id']}' does not exist, skipping.")

# Delete Virtual Network
try:
    vnet = network_client.virtual_networks.get(resource_group_name, resource_ids['vnet_id'])
    print(f"Deleting Virtual Network '{resource_ids['vnet_id']}'...")
    safe_delete(network_client.virtual_networks.begin_delete, resource_group_name, resource_ids['vnet_id'])
except ResourceNotFoundError:
    print(f"Virtual Network '{resource_ids['vnet_id']}' does not exist, skipping.")

# Delete Resource Group
try:
    resource_group = resource_client.resource_groups.get(resource_group_name)
    print(f"Deleting Resource Group '{resource_group_name}'...")
    safe_delete(resource_client.resource_groups.begin_delete, resource_group_name)
except ResourceNotFoundError:
    print(f"Resource Group '{resource_group_name}' does not exist, skipping.")

print("All resources processed successfully!")

