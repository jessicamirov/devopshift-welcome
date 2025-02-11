from dataclasses import dataclass
from fastapi import FastAPI

app = FastAPI()
server_list = ["nginx", "apache", "chrome"]

@app.get("/")
def get_server():
    "This is our main function"
    return "main"

@app.get("/servers")
def status_server(server_name: str):
    return server_list[server_name]
