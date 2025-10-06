from datetime import datetime
from time import sleep
import requests

while True:
    requests.get('https://github.com/eugene-okulik/Grafeeeee')
    print(datetime.now())
    sleep(2)
