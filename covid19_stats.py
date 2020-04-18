
import json
import requests

import boto3
from datetime import date
from botocore.exceptions import ClientError


# request = requests.get("https://api.covid19api.com/live/country/united-states")
# print(request.text)


URL = "https://api.covid19api.com/dayone/country/united-states/status/confirmed"
text_ARN = 'arn:aws:sns:us-west-2:737044771362:covid'
email_ARN = 'arn:aws:sns:us-west-2:737044771362:covid-email'
access_key = 'AKIAJJEGR2NACIGNQFMA'
secret_key = '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'
from_email = 'coronavirusapi@gmail.com'

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


def output_to_string(parsed_data):
    string = ""
    string += "Country: "+str(parsed_data[0])
    string += "\nConfirmed cases: "+str(parsed_data[7])
    string += "\nTotal death: "+str(parsed_data[8])
    string += "\nTotal recovered: "+str(parsed_data[9])
    string += "\nTotal active: "+str(parsed_data[10])
    string += "\n\nData date: +"+str(parsed_data[11])[:10]
    return string


def output_to_html(parsed_data):
    string = "<p><strong>COVID-19: Daily case report</strong></p>"
    string += "\n<p>Country:</p>" + str(parsed_data[0])
    if str(parsed_data[2]) != "":
        string += "\n<p>Province:</p>" + str(parsed_data[2])
    string += "\n<p>Date:</p>" + str(parsed_data[11])[:10]
    string += "\n<p>Confirmed cases:</p>" + str(parsed_data[7])
    string += "\n<p>Deaths:</p>" + str(parsed_data[8])
    string += "\n<p>Recovered:</p>" + str(parsed_data[9])
    string += "\n<p>Active:</p>" + str(parsed_data[10])
    string += "\n<p>Data retrieved by <a href=\"https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#7934d316-f751-4914-9909-39f1901caeb8\">Postman</a></p>\n"
    return string


def temp():
    fname = "Live-By-Country-All-Status.json"

    with open("./json/" + fname) as jfile:
        jdata = json.load(jfile)
        parsed_data = read_and_parse(jdata)
        print(parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z"))
    return output_to_string(parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z"))


def send_text(data):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-west-2")

    topic_arn = text_ARN
    message = output_to_string
    sns.publish(Message=message, TopicArn=topic_arn)
    # sns.publish(PhoneNumber="+", Message=temp())


def add_sub():
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-west-2")
    print("Got here")
    response = sns.subscribe(
        TopicArn=text_ARN,
        Protocol='sms',
        Endpoint='+14253270404',
        Attributes={
            'string': 'string'
        },
        ReturnSubscriptionArn=True | False
    )
    print(response)
    print("What")


def send_email(data):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-west-2")

    topic_arn = email_ARN
    html_message = output_to_html(data)
    sns.publish(Message=html_message, TopicArn=topic_arn)


def main():
    ## Use API
    # request = requests.get("https://api.covid19api.com/live/country/south-africa/status/confirmed")
    # jdata = request.json()

    ## Use JSON file
    send_text()

    fname = "Live-By-Country-All-Status.json"

    headers = {}
    payload = {}

    response = requests.request("GET", URL, headers=headers, data=payload)

    with open("./json/" + fname) as jfile:
        jdata = json.load(jfile)
        parsed_data = read_and_parse(jdata)
        print(parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z"))

    # send_text(parsed_data)
    # send_email(parsed_data)
    add_sub()





