# print("php has executed hook.py  ..........")
import re
import sys

import boto3

### SUBJECT TO CHANGE ###
# sys.argv[0] file path
# sys.argv[1] name
# sys.argv[2] delivery option
# sys.argv[3] country
# sys.argv[4] email
# sys.argv[5] phone

# to get access_key and secret_key from server file
ini = open("/deploy/ini", "r", encoding="utf-8")
access_key = ini.readline().strip()
secret_key = ini.readline().strip()
ini.close()


def main():
    # delivery will either be 'text', 'email', or 'both'
    name = sys.argv[1]
    delivery = sys.argv[2]
    country = sys.argv[3]
    email = sys.argv[4]
    phone = sys.argv[5]

    # get all arns and stores them in dict format
    arns = get_arns()

    email_result = False
    phone_result = False

    if email != "na":
        if delivery == 'email' or delivery == 'both':
            email = check_email(email)
            email_result = add_email(email, arns, country)

    if phone != "na":
        if delivery == 'phone' or delivery == 'both':
            phone = check_phone(phone, country)
            phone_result = add_text(phone, arns, country, name)

    if (email_result or phone_result):
        print("Successfully subscribed to COVID-19 update")
    else:
        print("You are NOT subscribed to COVID-19 update. Please check your input.")


def check_phone(phone_number, country):
    # check if phone number is correct format
    # return properly formatted phone number
    # return empty string if number cannot be formatted
    length = len(phone_number)

    # correctly format phone number
    if length == 12:
        if phone_number[0] == '+' and phone_number[1] == '1':
            return phone_number
        # korean number without +
        if country == 'korea-south' and phone_number[0:2] == '82':
            new_phone = '+' + phone_number
            return new_phone
    # phone number without +1
    elif length == 10:
        new_phone = '+1' + phone_number
        return new_phone
    # number with 1 but no +
    elif length == 11 and country == 'korea-south' and phone_number[0:3] == '010':
        new_phone = '+82' + phone_number[1:]
        return new_phone
    elif length == 11 and phone_number[0] == '1':
        new_phone = '+' + phone_number
        return new_phone
    else:
        return ''


def add_text(phone_number, arns, country, name):
    # check sub status then opt-out status
    # publish welcome message and return true
    # returns false if phone number is opted-out
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    response = sns.check_if_phone_number_is_opted_out(
        phoneNumber=phone_number
    )
    if not response['isOptedOut']:
        if country == 'united-states':
            sns.subscribe(
                TopicArn=arns.get('us_text'),
                Protocol='sms',
                Endpoint=phone_number
            )
        else:
            sns.subscribe(
                TopicArn=arns.get('sk_text'),
                Protocol='sms',
                Endpoint=phone_number
            )
        sns.publish(
            PhoneNumber=phone_number,
            Message= name + ', Welcome to COVID-19 daily alerts!\nTo opt-out of daily updates reply STOP',
            # TopicArn=text_ARN,
            # Endpoint=phone_number,
            # Protocol='sms'
        )
        return True

    else:
        try:
            sns.opt_in_phone_number(
                phoneNumber=phone_number
            )
            return True
        except Exception as e:
            print('You have opted-out within 30 days\nPlease wait 30 days to opt back in.')
            return False


def check_email(email):
    # check email format
    # return true if proper format, false if wrong
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        return email
    else:
        return ''


def add_email(email, arns, country):
    # add email to server
    # will always return true
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")
    if country == 'united-states':
        sns.subscribe(
            TopicArn=arns.get('us_email'),
            Protocol='email',
            Endpoint=email
        )
        return True
    else:
        sns.subscribe(
            TopicArn=arns.get('sk_email'),
            Protocol='email',
            Endpoint=email
        )
        return True


def get_arns():
    # get all topic arns and put into dict
    # return dict
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
        if 'united-states_text' in arn.get("TopicArn"):
            arns['us_text'] = arn.get("TopicArn")
        elif 'united-states_email' in arn.get("TopicArn"):
            arns['us_email'] = arn.get("TopicArn")
        elif 'korea-south_text' in arn.get("TopicArn"):
            arns['sk_text'] = arn.get("TopicArn")
        elif 'korea-south_email' in arn.get("TopicArn"):
            arns['sk_email'] = arn.get("TopicArn")

    return arns


main()
