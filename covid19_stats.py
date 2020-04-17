import requests
import json


# request = requests.get("https://api.covid19api.com/live/country/united-states/status/confirmed")
# print(request.text)
# jdata = json.dumps(request.text)

fname = "by_country_example.json"

with open("./json/"+fname) as jfile:
    jdata = json.load(jfile)
    for jobject in jdata:
        print(str(jobject))
