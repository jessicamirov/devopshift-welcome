from fastapi import FastAPI
from models import ServerStatusResponse, Server, add_new_server, read_server_list

app = FastAPI()


@app.get("/server")
def get_server(server_name: str) -> ServerStatusResponse:
    servers = read_server_list()
    for server in servers:
        if server.name == server_name:
            server_status = server.online
            return ServerStatusResponse(
                server_name=server_name, server_status=server_status
            )
    return ServerStatusResponse(
        server_name=server_name, server_status="Did not find server"
    )


@app.post("/server")
def create_server(server_name: str) -> ServerStatusResponse:
    new_server = Server(name=server_name, online=True, cpus=10, ram=20)
    add_new_server(new_server)
    return ServerStatusResponse(server_name=server_name, server_status="Created")