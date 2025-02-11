from dataclasses import dataclass
from fastapi import FastAPI

app = FastAPI()
servers = {"nginx":True, "chrome": False}

@dataclass
class Server:
    name: str
    status: bool | str

@app.get("/server")
def get_server(name: str) -> Server:
    status = servers.get(name, "Does not exist")
    return Server(name, status)

@app.post("/server")
def create_server(new_name: str) -> Server:
    if servers.get(new_name):
        return Server(new_name, "already exist")
    else:
        servers[new_name] = True
        return Server(new_name, "Created")
    


