import requests
import time

home_url = "www.webbikauppa.fi"
cart_url = "{}/index.php/ostoskori".format(home_url)

while 1:
    time.sleep(0.5)
    try:
        requests.get(cart_url)
        requests.get(home_url)
    except:
        pass
