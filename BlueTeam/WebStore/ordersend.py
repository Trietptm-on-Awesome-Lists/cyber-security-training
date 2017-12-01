import socket
import random
import time

host = ("127.0.0.1", 4444)
speed = 0.5                 # seconds

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
        send_random_order(s)
