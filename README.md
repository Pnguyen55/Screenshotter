# Screenshotter
 
 Mainly a test with AWS to try and run python scripts on their cloud systems, sends 5 screenshots over 5 minutes and saves it to a S3 bucket on AWS. 
 
Instance in AWS
EC2 t2.micro 

Steps taken: 
First make AWS account and instantiation 
Setup a S3 bucket for screenshots to be sent and saved to. 
Then, create key and connect to instance using key and the decrypyed password based on the key
Install the following dependences onto the newly created instance: Boto3, Python version 3.6+, Python MSS, git
Using boto3, setup your s3 access with AWS access key, this will have to be created if you haven't already
Use that key in your client setup for permissions to upload files to your S3 bucket on AWS.
Clone the github repository onto the instance 

To run the code remotely from AWS console 
After, create and add an administrative role or equivalent to your instance. 
Then go to Run Command in your EC2 management console and choose Run a command 
If Windows, select AWS-RunPowerShellScript from the command document
Select the instances you want the python script to run on 
Input the commands in the Commands section and find the file directory on the instance where the python script is located
Set execution timeout and timeout 
Run 

Commands sent through AWS console
[Environment]::SetEnvironmentVariable("Path","$env:Path;C:\Users\Administrator\AppData\Local\Programs\Python\Python36\")
python screenshotter.py
