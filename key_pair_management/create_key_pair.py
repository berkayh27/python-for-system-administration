# Creates a key pair
# Run
#       python create_key_pair.py some

import boto3
import sys

KEY_PAIR_NAME = sys.argv[1]
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName=KEY_PAIR_NAME)
response['KeyMaterial']
print(response)