# Instructions
# Run: 
#       python sec_group.py  "name_here" "vpc_id"

import boto3
from botocore.exceptions import ClientError
import sys

#   Takes an input from user
SECURITY_GROUP_NAME     = sys.argv[1]
vpc_id                  = sys.argv[2]

ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
try:
    response = ec2.create_security_group(GroupName=SECURITY_GROUP_NAME,
                                         Description='DESCRIPTION',
                                         VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
             {'IpProtocol': 'tcp',
             'FromPort': 53,
             'ToPort': 53,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)
 