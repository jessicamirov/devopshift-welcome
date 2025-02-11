import logging

#create the logger
logger = logging.getLogger("mylog")
logger.setLevel(logging.ERROR)

log_format = "%(asctime)s:%(message)s"
logging.basicConfig(format=log_format)

def get_server():
    try:
        server_name = input("Enter a server name: ")
        if not server_name:
            raise ValueError("server name is empty")
        if not server_name.isalpha():
            raise ValueError("is not alpha chars")
    except ValueError:
        logger.error("your server name is invalid")
    finally:
        return server_name

def server_status(my_server_list):
    server_name = get_server()
    if server_name in my_server_list:
        logger.info(server_name + " is running")
    else:
        logger.error("Your server name not recognized")


while(True):
    server_list = ["nginx", "apache", "chrome"]
    server_status(server_list)
