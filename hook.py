print("php has executed hook.py  ..........")
import sys
import boto3

# sys.argv[0] file path
# sys.argv[1] name
# sys.argv[2] email
# sys.argv[3] phone number

text_ARN = 'arn:aws:sns:us-east-1:737044771362:covid_text'
email_ARN = 'arn:aws:sns:us-east-1:737044771362:covid_email'
access_key = 'AKIAJJEGR2NACIGNQFMA'
secret_key = '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'

def main():
    #out = open("/stuff/out","w",encoding="utf-8")
    #out.write(str(sys.argv[2])+"\n")
    #out.write(str(sys.argv[3])+"\n")
    
    if sys.argv[2] != '':
        add_email(sys.argv[2])
    if sys.argv[3] != '':
        add_text(sys.argv[3])

    print("code execution: successful")
    #out.write("code execution: successful")
    #out.close()


def check_phone(phone_number):
    length = len(phone_number)


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
    if not response:
        sns.subscribe(
            TopicArn=text_ARN,
            Protocol='sms',
            Endpoint=phone_number
        )
    else:
        sns.opt_in_phone_number(
            phoneNumber=phone_number
        )

    sns.publish(
        PhoneNumber=phone_number,
        # TODO: Let user know about opt-in, opt-out as well
        Message='Welcome to COVID-19 daily alerts!\n To opt-out of daily messages reply STOP',
        #TopicArn=text_ARN,
        #Endpoint=phone_number,
        #Protocol='sms'
    )


def add_email(email):
    sns = boto3.client(
        'sns',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1")

    sns.subscribe(
        TopicArn=email_ARN,
        Protocol='email',
        Endpoint=email
    )

main()
