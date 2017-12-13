import socket
import random
import time
import os

host = ("46.228.143.102", 4444)
speed = 0.001

global log_lines
log_lines = 0
access_log_path = "/var/log/apache2/access.log"
match_string = "ostoskori"


customers = [   "Eetu Luukkanen",
                "Onni Hakkari",
                "Pasi Puumalainen",
                "Aleksi Ahola",
                "Teemu Tikkanen",
                ]


products = [("Keisari 1000-pack", 999.99),
            ("Karjala 100-pack", 99.99),
            ("Ultimaattinen MasterRace PC", 4999.99),
            ("Ultimaattinen 4K näyttö ultimaattiselle PC:lle", 1999.99),
            ("Ultimaattinen USB-muistitikku 512GB (Malli: Ananas)", 99.99),
            ]

def send_random_order(s):
    customer = random.choice(customers)
    product, price = random.choice(products)
    order_data = "{}<split>{}<split>{}".format(customer, product, price)
    s.sendall(bytes(order_data, "latin-1"))
    print("Sending: {}".format(order_data))


def is_order():
    global log_lines
    with open(access_log_path, "r") as f:
        for line in f.readlines():
            log_lines += 1
        last_line = line

        if match_string in last_line:
            return True

        return False


def erase_log():
    with open(access_log_path, "w") as f:
        f.write("")


if __name__ == "__main__":
    connected = False
    s = socket.socket()
    while not connected:
        try:
            s.connect(host)
            connected = True
        except:
            print("Failed to connect")
            time.sleep(1)

    while True:
        time.sleep(speed)
        if is_order():
            send_random_order(s)

        if log_lines > 1000:
            log_lines = 0
            erase_log()
