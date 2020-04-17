
import json
import requests

# request = requests.get("https://api.covid19api.com/live/country/united-states")
# print(request.text)

'''

Search by parsed_data.get("CountryCode-Province").get("Date") to get list of data.
Example:    parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z")

If you don't know the date, use list() to list all dates available.
Example:    list(parsed_data.get("US-Washington"))

If the province was not provided, use an empty string for the province.
Example:    parsed_data.get("ZA-").get("2020-04-14T00:00:00Z")

The list contains various data. You can simply refer them by specifying the index.
Example:    parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z")[0]
            returns "United States of America"

index       data
0           Country
1           CountryCode
2           Province
3           City
4           CityCode
5           Lat
6           Lon
7           Confirmed
8           Deaths
9           Recovered
10          Active
11          Date
'''

def read_and_parse(jdata):
    data_dict = {}
    for jobject in jdata:
        parsed_object = []
        curr_prov = jobject["Province"]
        curr_cont_code = jobject["CountryCode"]
        curr_date = jobject["Date"]
        parsed_object.append(jobject["Country"])
        parsed_object.append(curr_cont_code)
        parsed_object.append(curr_prov)
        parsed_object.append(jobject["City"])
        parsed_object.append(jobject["CityCode"])
        parsed_object.append(jobject["Lat"])
        parsed_object.append(jobject["Lon"])
        parsed_object.append(jobject["Confirmed"])
        parsed_object.append(jobject["Deaths"])
        parsed_object.append(jobject["Recovered"])
        parsed_object.append(jobject["Active"])
        parsed_object.append(curr_date)

        name = curr_cont_code+"-"+curr_prov
        data_dict.setdefault(name, {})
        data_dict[name][curr_date] = parsed_object
    return data_dict



## Use API
# request = requests.get("https://api.covid19api.com/live/country/south-africa/status/confirmed")
# jdata = request.json()

## Use JSON file
fname = "Live-By-Country-All-Status.json"

with open("./json/"+fname) as jfile:
    jdata = json.load(jfile)
    parsed_data = read_and_parse(jdata)
    print(parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z"))


