import requests
import json


request = requests.get('https://api.covid19api.com/countries')
print(request.text)
