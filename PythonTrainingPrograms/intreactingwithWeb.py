#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url="https://www.yum.oracle.com"
payload=''
headers={}

r= requests.get(url)

print(r.text)