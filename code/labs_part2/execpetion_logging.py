from dataclasses import dataclass
import logging 
import sys

# Create and configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # Log all levels to stdout
    ]
)

# Creating an object
logger = logging.getLogger()


@dataclass
class InvalidServerNameError(Exception):
    "Raised when the server name is invalid."

def check_service_status(server_name):
    servers = ["nginx", "docker", "k8s"]
    if server_name in servers:
        logging.info(f"Server {server_name} is running.")
        return "Running"
    else: 
        logging.error(f"{server_name} is not a recognized server.")
        raise ValueError(f"{server_name} is not a recognized server.")

# Main logic
try:
    server_name = input("Enter server name: ").strip()
    if server_name == " " or server_name == None or not server_name.isalpha():
        raise InvalidServerNameError("Invalid server name")
    print(f"{server_name} status: {check_service_status(server_name)}")

except InvalidServerNameError as e:
    logging.error(e)
    print(f"ERROR: {e}")    

except ValueError as e:
    logging.error(e)
    print(f"Error: {e}")