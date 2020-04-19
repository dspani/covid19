#print("php has executed hook.py  ..........")
import sys
import boto3
import re

# sys.argv[0] file path
# sys.argv[1] name
# sys.argv[2] email
# sys.argv[3] phone number
# sys.argv[4] country
us_email = 'arn:aws:sns:us-east-1:737044771362:covid_united_states'
us_text = 'arn:aws:sns:us-east-1:737044771362:covid_united_states_text'
sk_arn = 'arn:aws:sns:us-east-1:737044771362:covid_south_korea'
access_key = 'AKIAJJEGR2NACIGNQFMA'
secret_key = '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'

def main():
    # out = open("/stuff/out","w",encoding="utf-8")
    # out.write(str(sys.argv[2])+"\n")
    # out.write(str(sys.argv[3])+"\n")
    check_email(sys.argv[2])
    if sys.argv[2] != '':
        add_email(sys.argv[2])

    sys.argv[3] = check_phone(sys.argv[3])
    if sys.argv[3] != '':
        add_text(sys.argv[3])

    print("Successfully subscribed to COVID-19 update")
    # out.write("code execution: successful")
    # out.close()


def check_phone(phone_number):
    # check if phone number is correct format
    length = len(phone_number)

    if length == 12:
        if phone_number[0] == '+' and phone_number[1] == '1':
            return phone_number
    # phone number without +1
    elif length == 10:
        new_phone = '+1' + phone_number
        return new_phone
    # number with 1 but no +
    elif length == 11 and phone_number[0] == '1':
        new_phone = '+' + phone_number
        return new_phone
    else:
        return ''
    # check if phone number is correct format


def add_text(phone_number):

    # to check sub status
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    response = sns.check_if_phone_number_is_opted_out(
        phoneNumber=phone_number
    )
    if not response['isOptedOut']:
        sns.subscribe(
            TopicArn=us_text,
            Protocol='sms',
            Endpoint=phone_number
            )
    else:
        try:
            sns.opt_in_phone_number(
                phoneNumber=phone_number
            )
        except Exception as e:
            print('You have opted-out within 30 days\nPlease wait 30 days to opt back in.')

    sns.publish(
        PhoneNumber=phone_number,
        Message=sys.argv[1] + ', Welcome to COVID-19 daily alerts!\nTo opt-out of daily updates reply STOP',
        #TopicArn=text_ARN,
        #Endpoint=phone_number,
        #Protocol='sms'
    )


def check_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        return email
    else:
        return ''


def add_email(email):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    sns.subscribe(
        TopicArn=us_email,
        Protocol='email',
        Endpoint=email
    )

main()
