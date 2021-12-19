from controllers.serverController import ServerController

server_v1 = {
    "server": "/favicon.ico",
    "server_controller": ServerController.as_view("server_conf"),
    # ----------------------------------------------------------------
}