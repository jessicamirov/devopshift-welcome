def get_server():
    try:
        server_name = input("Enter a server name: ")
        if not server_name:
            raise ValueError("server name is empty")
        if not server_name.isalpha():
            raise ValueError("is not alpha chars")
    except ValueError:
        print("Error: Invalid server name")
    finally:
        return server_name

def server_status(my_server_list):
    server_name = get_server()
    if server_name in my_server_list:
        print(server_name + " is running")
    else:
        print(server_name + "not recognized")


def main():
    server_list = ["nginx", "apache", "chrome"]
    server_status(server_list)

if __name__ == "__main__":
    main()
