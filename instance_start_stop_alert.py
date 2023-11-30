import json
import boto3
client = boto3.client('sns')
def lambda_handler(event, context):
    topic_arn = 'arn:aws:sns:us-east-1:112901932178:instance-start-and-stop-alert'

    instance_id = event['detail']['instance-id']
    instance_state = event['detail']['state']

    # Send SNS notifications based on instance state
    if instance_state == 'running':
        message = 'EC2 again running!!!!'
        client.publish(
            TopicArn=topic_arn,
            Message=message
            )
    elif instance_state == 'stopped':
        message = 'EC2 stopped . Please take a look into the situation as quick as possible!!!!'
        client.publish(
            TopicArn=topic_arn,
            Message=message
            )
