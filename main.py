from source.server.instance import Server


server = Server()
app = server.app

server.run()
