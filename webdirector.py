import urllib3
import colorama
from colorama import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
colorama.init()

# http = urllib3.PoolManager()
http = urllib3.ProxyManager('http://localhost:8080/')

url = input("Enter url: ")
wordlist = open("rockyou.txt", "r+")
for i in wordlist:
    r = http.request('HEAD', url+"/"+i.rstrip())
    if r.status != 404:
        print(url+"/"+i.rstrip(), r.status)