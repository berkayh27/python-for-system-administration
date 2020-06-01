##################
# Deletes the keys
# Run: 
#       python delete_key_pair.py  NAME_OF_KEY_PAIR
import boto3
import sys
def delete_key_pair(KEY_PAIR):
    '''This function deletes a key pair'''
    ec2 = boto3.client('ec2')
    response = ec2.delete_key_pair(KeyName=KEY_PAIR)
    print(response)
    print("Key pair  has been deleted")

