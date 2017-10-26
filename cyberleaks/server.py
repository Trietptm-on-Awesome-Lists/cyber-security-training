# -*- coding: latin-1 -*-
import socket
import shutil


class listener:

    def __init__(self, host="localhost", port=1337):
        self.s = socket.socket()
        self.s.bind((host, port))
        self.s.listen(5)

    def listen(self):
        while True:
            client, addr = self.s.accept()
            file_name = str(client.recv(4096), "latin-1")
            print("Receiving file {} from {}:{}".format(file_name, addr[0], addr[1]))
            self.recv_file(file_name, client)

    def recv_file(self, file_name, client):
        with open("/var/www/cyberleaks/leaks/{}".format(file_name), "wb") as dest_file:
            src_file = client.makefile("rb")
            shutil.copyfileobj(src_file, dest_file)
        print("File {} received!".format(file_name))


if __name__ == "__main__":
    listener().listen()
