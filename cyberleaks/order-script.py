import requests
import time

home_url = "http://www.webbikauppa.fi"
cart_url = "{}/index.php/ostoskori".format(home_url)

while 1:
    time.sleep(0.5)
    try:
        print("Ordering")
        requests.get(cart_url)
        requests.get(home_url)
        print("Done")
    except Exception as e:
        print(e)
        pass
