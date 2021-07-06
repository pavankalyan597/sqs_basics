import boto3
import time

client = boto3.client('sqs',region_name='us-east-2',aws_access_key_id='AKIA2DRAHDISQGOABUUC',aws_secret_access_key="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")

queue = client.get_queue_url(
    QueueName='MyFirstQueue')

msg = client.receive_message(QueueUrl=queue['QueueUrl'])
print(msg)

time.sleep(45)

#deleting msg in queue
msg_delete = client.delete_message(QueueUrl=queue['QueueUrl'], 
        ReceiptHandle=msg['Messages'][0]['ReceiptHandle'])

print(msg_delete)
