# Instructions
# Run:
#           python delete_sec_group.py sg-011d08ab2d2088074

import boto3, sys
from botocore.exceptions import ClientError


# Create EC2 client
ec2 = boto3.client('ec2')

# Delete security group
def delete_sec_group(SECURITY_GROUP_NAME2):
    try:
        response = ec2.delete_security_group(GroupName=SECURITY_GROUP_NAME2)
        print('Security Group Deleted')
    except ClientError as e:
        print(e)