import logging
import json
import sys

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



class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        log = {"time": record.created, "module":record.module}
        return json.dumps(log)

#create the logger
logger = logging.getLogger("server")
logger.setLevel(logging.DEBUG)

#print to stdout
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)

# get_log_level = input("Get a LOG_LEVEL: ")

while(True):
    server_list = ["nginx", "apache", "chrome"]
    server_status(server_list)




