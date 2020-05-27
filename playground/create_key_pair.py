# Creates a key pair and attaches a public key to a specific region and outputs private key to a screen. I have to save it.
# Run
#       python create_key_pair.py some

import boto3
import sys

ec2 = boto3.client('ec2')

# gets an input from the user and creates a keypair
def create_key(key_name_from_user):
    response = ec2.create_key_pair(
        KeyName=key_name_from_user,
        DryRun=False,
        TagSpecifications = [
            {
                'ResourceType': 'key-pair',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Boto3'
                    },
                ]
            },
        ],
    )
    print(response)


#create_key(sys.argv[1])
# This works itself but if moved to another file it will work as a function
# from create_key_pair import create_key
# import sys
# create_key(sys.argv[1])