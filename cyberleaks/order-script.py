import requests
import time

url = "www.webbikauppa.fi/index.php/ostoskori"

while 1:
    time.sleep(0.5)
    try:
        requests.get(url)
    except:
        pass
