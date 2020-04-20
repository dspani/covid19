import datetime
import sys
from datetime import date
import boto3
import requests
import parse_utility

access_key = sys.argv[1]
secret_key = sys.argv[2]
base_URL = "https://api.covid19api.com/total/country/"


## Sends message
def send_text(arn, parsed_data):
    # send text to all subbed & opted-in subs at arn
    # message contains parsed data
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    # Message contains info in plain text
    message = parse_utility.output_to_string(parsed_data)
    # Send to subscribers
    sns.publish(
        Message=message,
        TopicArn=arn
    )
    # sns.publish(PhoneNumber="+", Message=temp())


## Sends email
def send_email(arn, parsed_data):
    # uses arn to send email containing parsed data to all subs
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
    html_message = parse_utility.output_to_string(parsed_data)
    ## Push to subscribers
    sns.publish(
        TopicArn=arn,
        Message=html_message,
        Subject=subject
    )


def united_states(arns):
    ## Use API
    # pings api for latest data
    # formats data for text and email
    # passes data and specific arn to text and email funcs
    today = date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    url = base_URL + 'united-states'
    request = requests.get(url)
    jdata = request.json()
    parsed_data = parse_utility.read_and_parse(jdata)
    string = parsed_data.get("-").get(yesterday + "T00:00:00Z")  ## Use JSON file

    ''''
    fname = "Live-By-Country-All-Status.json"
    with open("./json/" + fname) as jfile:
        jdata = json.load(jfile)
        parsed_data = parse_utility.read_and_parse(jdata)
        string = parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z")
    '''

    #send_text(arns.get('us_text'), string)
    send_email(arns.get('us_email'), string)


def south_korea(arns):
    ## Use API
    # pings api for latest data
    # formats data for text and email
    # passes data and specific arn to text and email funcs
    today = date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")

    url = base_URL + 'korea-south'
    request = requests.get(url)
    jdata = request.json()
    parsed_data = parse_utility.read_and_parse(jdata)
    string = parsed_data.get("-").get(yesterday + "T00:00:00Z")  ## Use JSON file

    send_text(arns.get('sk_text'), string)
    send_email(arns.get('sk_email'), string)




def get_arns():
    # gets all arns from sns account
    # formats and returns in dict
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1"
    )

    response = sns.list_topics()
    topics = response.get('Topics')
    # since us has arn for text and email
    print(topics)
    arns = {}
    for arn in list(topics):
        if 'united_states_text' in arn.get("TopicArn"):
            arns['us_text'] = arn.get("TopicArn")
        elif 'united_states_email' in arn.get("TopicArn"):
            arns['us_email'] = arn.get("TopicArn")
        elif 'south_korea_text' in arn.get("TopicArn"):
            arns['sk_text'] = arn.get("TopicArn")
        elif 'south_korea_email' in arn.get("TopicArn"):
            arns['sk_email'] = arn.get("TopicArn")

    return arns


def main():
    # driver code to split arns by country
    # starts country speific notif funcs
    arns = get_arns()
    # slipt arns into us and sk
    us_arns = {}
    sk_arns = {}
    # split arns
    for arn in arns:
        sk_arns['sk_email'] = arns.get('sk_email')
        sk_arns['sk_text'] = arns.get('sk_text')
        us_arns['us_email'] = arns.get('us_email')
        us_arns['us_text'] = arns.get('us_text')

    united_states(us_arns)
    #south_korea(sk_arns)


main()
