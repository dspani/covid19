import json
import requests
from datetime import date
import boto3
import parse_utility
import datetime

base_URL = "https://api.covid19api.com/total/country/united-states"
text_ARN = 'arn:aws:sns:us-east-1:737044771362:covid_text'
email_ARN = 'arn:aws:sns:us-east-1:737044771362:covid_email'
sk_arn = 'arn:aws:sns:us-east-1:737044771362:covid_south_korea'
access_key = 'AKIAJJEGR2NACIGNQFMA'
secret_key = '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'


## Sends message
def send_text(parsed_data):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    ## Message contains info in plain text
    message = parse_utility.output_to_string(parsed_data)
    ## Send to subscribers
    sns.publish(Message=message, TopicArn=text_ARN)
    # sns.publish(PhoneNumber="+", Message=temp())


## Sends email
def send_email(parsed_data):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    ## Date format: MM/DD/YY
    today = date.today()
    today = today.strftime("%m/%d/%Y")

    ## Email subject
    subject = 'Coronavirus stats for ' + today

    ## Email take plain text
    # html_message = parse_utility.output_to_html(parsed_data)
    ## html_message contains info in plain text
    html_message = parse_utility.output_to_string(parsed_data)
    ## Push to subscribers
    sns.publish(
        TopicArn=email_ARN,
        Message=html_message,
        Subject=subject
    )


def main():
    ## Use API
    # request = requests.get(URL)
    # jdata = request.json()
    ## Use API
    today = date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    print(today)
    url = base_URL
    request = requests.get(url)
    jdata = request.json()
    parsed_data = parse_utility.read_and_parse(jdata)
    string = parsed_data.get("-").get(yesterday + "T00:00:00Z")    ## Use JSON file

    fname = "Live-By-Country-All-Status.json"
    today = date.today()
    ''''
    with open("./json/" + fname) as jfile:
        jdata = json.load(jfile)
        parsed_data = parse_utility.read_and_parse(jdata)
        string = parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z")
    '''
    # send_text(string)
    send_email(string)


main()


