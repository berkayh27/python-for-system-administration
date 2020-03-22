# Instructions
# Run:
#           python describe_sec_group.py sg-011d08ab2d2088074

import boto3, sys
 
from botocore.exceptions import ClientError
SECURITY_GROUP_ID = sys.argv[1]


ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=[SECURITY_GROUP_ID])
    print(response)
except ClientError as e:
    print(e)