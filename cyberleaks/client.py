# -*- coding: latin-1 -*-
import socket
import shutil
import sys


host = "localhost"
port = 1337


if __name__ == "__main__":
    file_path = sys.argv[1]
    file_name = file_path.split("/")[-1]

    s = socket.socket()
    s.connect((host, port))
    s.sendall(bytes(file_name, "latin-1"))

    with open(file_path, "rb") as src_file:
        dest_file = s.makefile("wb")
        shutil.copyfileobj(src_file, dest_file)
