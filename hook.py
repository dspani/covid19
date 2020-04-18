import sys
import boto3

# sys.argv[0] file path
# sys.argv[1] name
# sys.argv[2] email
# sys.argv[3] phone number

text_ARN = 'arn:aws:sns:us-west-2:737044771362:covid'
email_ARN = 'arn:aws:sns:us-west-2:737044771362:covid-email'
access_key = 'AKIAJJEGR2NACIGNQFMA'
secret_key = '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'

def main():
    if sys.argv[2] != '':
        add_email(sys.argv[2])
    if sys.argv[3] != '':
        add_text(sys.argv[3])



def add_text(phone_number):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-west-2")

    sns.subscribe(
        TopicArn=text_ARN,
        Protocol='sms',
        Endpoint=phone_number
    )


def add_email(email):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-west-2")

    sns.subscribe(
        TopicArn=email_ARN,
        Protocol='email',
        Endpoint=email
    )


main()