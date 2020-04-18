import json
from datetime import date

import boto3

import parse_utility

URL = "https://api.covid19api.com/dayone/country/united-states/status/confirmed"
text_ARN = 'arn:aws:sns:us-west-2:737044771362:covid'
email_ARN = 'arn:aws:sns:us-west-2:737044771362:covid-email'
access_key = 'AKIAJJEGR2NACIGNQFMA'
secret_key = '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'


## Sends message
def send_text(parsed_data):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-west-2")

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
        region_name="us-west-2")

    ## Date format: DD/MM/YY
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

    ## Use JSON file
    fname = "Live-By-Country-All-Status.json"

    with open("./json/" + fname) as jfile:
        jdata = json.load(jfile)
        parsed_data = parse_utility.read_and_parse(jdata)
        string = parse_utility.output_to_string(parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z"))

    send_text(string)
    send_email(string)


main()
