import socket, json

class Proxy:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def main(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(1)
            conn, addr = s.accept()
            data = conn.recv(4096)
            if data:
                # print(json.dumps(data.decode()).split(' ')[1].split("://")[1][:-1])
                # exit()
                try:
                    print(json.dumps(data.decode()).split(' ')[1].split("://")[1][:-1])
                    new_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    new_connection.connect((json.dumps(data.decode()).split(' ')[1].split("://")[1][:-1], 80))
                    new_connection.send(data)
                    received = new_connection.recv(4086)
                    print(received)
                except Exception as e:
                    print(json.dumps(data.decode()))
                # print(json.dumps(data.decode()))
                #
                # received = server.recv(4096)
                # print(received)

network1 = Proxy('', 8080)
network1.main()