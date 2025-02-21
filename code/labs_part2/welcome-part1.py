servers = []
for i in range(1,4):
    servers.append(input(f"Enter the name of server {i}: "))
print(servers) 
    
servers_dict = {}
for i in range(3):
    servers_dict[servers[i]] = input(f"Enter the IP address for {servers[i]}:")
print(f"\nServer configuration: {servers_dict}")

server_name = input("Enter a server name to view details:")
if servers_dict.get(server_name):
    print(f"\n{server_name} has IP address {servers_dict.get(server_name)}")
else:
    print(f"\nERROR: {server_name} server doesn't exist! ")

update_ip = input("\nDo you want to update any server's IP address? (yes/no): ")
if update_ip == "yes":
    server_name = input("\nEnter the server name: ")
    if servers_dict.get(server_name):        
        new_ip = input("\nEnter the new IP address: ")
        servers_dict[server_name] = new_ip
        print(f"\nServer configuration: {servers_dict}")
    else:
        print(f"\n{server_name} not found! ")
else:
    print("\nanything to change")
