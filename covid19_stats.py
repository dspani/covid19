
import requests
import sys
from datetime import date
import boto3
import parse_utility
import datetime


access_key = ''
secret_key = ''
base_URL = "https://api.covid19api.com/total/country/"


## Sends message
def send_text(arn, parsed_data):
    print('text function: ' + arn)
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    ## Message contains info in plain text
    message = parse_utility.output_to_string(parsed_data)
    ## Send to subscribers
    sns.publish(
        Message=message,
        TopicArn=arn
    )
    # sns.publish(PhoneNumber="+", Message=temp())


## Sends email
def send_email(arn, parsed_data):
    print('email function ' + arn)
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
        TopicArn=arn,
        Message=html_message,
        Subject=subject
    )

def united_states(arns):
    ## Use API
    # request = requests.get(URL)
    # jdata = request.json()
    ## Use API
    today = date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    url = base_URL + 'united-states'
    request = requests.get(url)
    jdata = request.json()
    parsed_data = parse_utility.read_and_parse(jdata)
    string = parsed_data.get("-").get(yesterday + "T00:00:00Z")  ## Use JSON file

    fname = "Live-By-Country-All-Status.json"

    ''''
    with open("./json/" + fname) as jfile:
        jdata = json.load(jfile)
        parsed_data = parse_utility.read_and_parse(jdata)
        string = parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z")
    '''
    print("email arn: " + arns.get('email'))
    print("text arn: " + arns.get('text'))
    send_text(arns.get('text'), string)
    send_email(arns.get('email'), string)


def south_korea(arns):
    ## Use API
    # request = requests.get(URL)
    # jdata = request.json()
    ## Use API
    today = date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    print(today)
    url = base_URL + 'korea-south'
    request = requests.get(url)
    jdata = request.json()
    parsed_data = parse_utility.read_and_parse(jdata)
    string = parsed_data.get("-").get(yesterday + "T00:00:00Z")  ## Use JSON file


    send_text(arns.get('text'), string)
    send_email(arns.get('email'), string)


def main():
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


    print(sk_arns)
    print(us_arns)

    united_states(us_arns)
    south_korea(sk_arns)

def get_arns(): # FIXXXXX
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1"
    )

    response = sns.list_topics()
    topics = response.get('Topics')
    # since us has arn for text and email
    arns = {}
    for arn in list(topics):
        if 'united_states_text' in arn.get("TopicArn"):
            arns['us_text'] = arn.get("TopicArn")
        elif 'united_states' in arn.get("TopicArn"):
            arns['us_email'] = arn.get("TopicArn")
        elif 'south_korea_text' in arn.get("TopicArn"):
            arns['sk_text'] = arn.get("TopicArn")
        elif 'south_korea' in arn.get("TopicArn"):
            arns['sk_email'] = arn.get("TopicArn")

    return arns


try:
    access_key = sys.argv[1]
    secret_key = sys.argv[2]

    # TODO:remove ln159 & ln160 after testing
    print(access_key)
    print(secret_key)
    if sys.argv[1] and sys.argv[2]:
        main()
except Exception as e:
    print("No Access Keys")


