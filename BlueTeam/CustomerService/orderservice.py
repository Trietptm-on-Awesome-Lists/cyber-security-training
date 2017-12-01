import socket
import time

host = ("46.228.143.102", 4444)
log_path = "/home/user/orderlog.txt"


def recv_order(conn):
    try:
        customer, product, price = str(conn.recv(4096), "latin-1").split("<split>")
        order_data = "Customer: {} ordered product: {} for {} euros\n".format(customer, product, price)
    except:
        order_data = "Warning: Can't receive orders!\nReboot WebStore server and your workstation!\n"
        time.sleep(0.5)
    print(order_data)
    with open(log_path, "a") as f:
        f.write(order_data)

if __name__ == "__main__":
    begin_time = time.time()
    s = socket.socket()
    s.bind(host)
    s.listen(5)

    conn, addr = s.accept()
    while True:
        recv_order(conn)
