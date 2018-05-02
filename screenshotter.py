import time
from mss import mss
import os
import boto3

# Initialize variables\
s3 = boto3.resource('s3')
client = boto3.client(
    's3',
    #aws_access_key_id= the id of your secret access key,
    #aws_secret_access_key= your secret access key to aws
)
sct = mss()
increment = 0
username = 'test_pc'
running = True
bucket_name = 'peterscreenshotbucket'

# Continually run script to save screenshots 5 over 5 minutes and save to S3
while running:
    if(increment == 5):
        running = False
        exit()

    increment += 1
    filename = str(increment) + '.png'
    file = sct.shot(output=filename)
    client.upload_file(filename, bucket_name, username + '/' + filename)
    print(file)
    time.sleep(60)
