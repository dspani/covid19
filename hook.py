import sys
import boto3

def main():
    client = boto3.client(
        "sns",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-east-1"
    )

    topic = client.create_topic(Name="notifications")
    topic_arn = topic['TopicArn']



    ## sys.argv[0] file path
    ## sys.argv[1] name
    ## sys.argv[2] email
    ## sys.argv[3] phone number

    client.subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint=sys.argv[1]
    )

main()