!/usr/bin/python3

import requests
import re

username = 'guest'
password = 'guest'

url = 'http://10.10.10.195/submitmessage'

session = requests.Session()
response = session.post(url, data={"message": '1=1'})

content = response.text

print('[-] RESPONE: ' + content)
