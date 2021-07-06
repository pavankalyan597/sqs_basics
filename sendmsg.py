import boto3

queue = client.get_queue_url(
    QueueName='MyFirstQueue')

response = client.send_message(QueueUrl=queue['QueueUrl'],
                                MessageBody="hii this is from boto3")
#print(response)
