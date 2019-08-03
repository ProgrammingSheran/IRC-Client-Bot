import socket
from threading import Thread
import datetime

class Server:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 1337))
    sock.listen(1)
    connections = []

    def server_things(self, data, addr):

        time = datetime.datetime.now().strftime("%H:%M:%S - %d.%m.%y")

        '''FORMAT: SERVER [NUMBER] [TYPE/PURPOSE] :[CONTENT]'''
        data.send(b"SERVER 1 DATE :%s" % bytes(time, "utf-8"))

    def messaging(self, data, addr):
        string = b""
        while True:
            try:
                string = data.recv(1024)
            except BrokenPipeError:
                self.connections.remove(data)
            if not string:
                self.connections.remove(data)
                break

            msg = string.split(b" ")
            if len(msg) < 2 or msg[1] == b"":
                data.send(b"Empty message!")
            elif string.startswith(b"MESSAGE"):
                if msg[1] == b"MSG" and msg[2].startswith(b"#"):
                    for connection in self.connections:
                        connection.send(b"%s :%s" % (msg[2].replace(b"#", b""), b' '.join(msg[3:])))

                elif msg[1] == b"INFO":
                    data.send(b"You are: %s (PORT: %s)" % (str.encode(addr[0]), str.encode(str(addr[1]))))

                else:
                    data.send(b"Invalid message format!")
            else:
                data.send(b"An error occurred!")

            print(msg)

    def server(self):
        while True:
            data, addr = self.sock.accept()
            self.connections.append(data)
            print(len(self.connections))
            self.t = Thread(target=self.messaging, args=(data, addr))
            self.serve = Thread(target=self.server_things, args=(data, addr))
            self.t.start()
            self.serve.start()

s = Server()
s.server()