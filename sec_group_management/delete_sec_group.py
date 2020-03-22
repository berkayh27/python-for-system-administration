# Instructions
# Run:
#           python delete_sec_group.py sg-011d08ab2d2088074

import boto3, sys
from botocore.exceptions import ClientError

# Get sec group ID from user
SECURITY_GROUP_ID = sys.argv[1]


# Create EC2 client
ec2 = boto3.client('ec2')

# Delete security group
try:
    response = ec2.delete_security_group(GroupId=SECURITY_GROUP_ID)
    print('Security Group Deleted')
except ClientError as e:
    print(e)