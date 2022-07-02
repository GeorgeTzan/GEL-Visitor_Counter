import requests, threading
from functools import lru_cache

url = 'https://www.hitwebcounter.com/counter/counter.php?page=6221588&style=0003&nbdigits=5&type=page&initCount=0'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

@lru_cache(maxsize=None)
def do_request():
    while True:
        response = requests.post(url, headers=headers)
        
threads = []

for i in range(10400):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(10400):
    threads[i].start()

for i in range(10400):
    threads[i].join()
