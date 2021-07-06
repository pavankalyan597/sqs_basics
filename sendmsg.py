import boto3

client = boto3.client('sqs',region_name='us-east-2',aws_access_key_id='AKIA2DRAHDISQGOABUUC',aws_secret_access_key="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")

queue = client.get_queue_url(
    QueueName='MyFirstQueue')

response = client.send_message(QueueUrl=queue['QueueUrl'],
                                MessageBody="hii this is from boto3")
#print(response)
