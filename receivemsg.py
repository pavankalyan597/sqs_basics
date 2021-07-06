import boto3
import time

queue = client.get_queue_url(
    QueueName='MyFirstQueue')

msg = client.receive_message(QueueUrl=queue['QueueUrl'])
print(msg)

time.sleep(45)

#deleting msg in queue
msg_delete = client.delete_message(QueueUrl=queue['QueueUrl'], 
        ReceiptHandle=msg['Messages'][0]['ReceiptHandle'])

print(msg_delete)
