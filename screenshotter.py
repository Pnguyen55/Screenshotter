import time
from mss import mss
import os
import boto3

# Initialize variables\
s3 = boto3.resource('s3')
client = boto3.client(
    's3',
    aws_access_key_id='AKIAJUCUVC3KJ2OZRIEQ',
    aws_secret_access_key='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'
)
sct = mss()
increment = 0
username = 'test_pc'
running = True

# Continually run script to save screenshots 30 and save to S3
while running:
    if(increment == 5):
        running = False
        exit()

    increment += 1
    filename = str(increment) + '.png'
    file = sct.shot(output=filename)
    client.upload_file(filename, 'peterscreenshotbucket', username + '/' + filename)
    print(file)
    time.sleep(10)
