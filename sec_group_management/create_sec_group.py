#!/usr/bin/env python
# These codes below creates a security group on AWS
import sys
import boto3
from botocore.exceptions import ClientError
region = "us-east-1"

# Takes input from user for VPC_ID
# VPC_ID=sys.argv[1]
VPC_ID="vpc-1471ad6e"

# Gets a name for a sec group name
# SECURITY_GROUP_NAME=sys.argv[2]
SECURITY_GROUP_NAME="Name_for_sec_group"

# Gets a description
# DESCRIPTION=sys.argv[3]
DESCRIPTION="This is create by python"

# Protocol
# IP_PROTOCOL_1=sys.argv[4]
IP_PROTOCOL_1="tcp"

# Ports
# FROM_PORT_1=sys.argv[5]
FROM_PORT_1=0
TO_PORT_1=22
# TO_PORT_1=sys.argv[6]

# IP address list
# CIDR_IP_1=sys.argv[7]
CIDR_IP_1="0.0.0.0/0"


ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = VPC_ID
try:
    response = ec2.create_security_group(GroupName=SECURITY_GROUP_NAME,Description=DESCRIPTION,VpcId=VPC_ID)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
    print("")
    
    # Sets Ingress Rule
    ingress_rule = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': IP_PROTOCOL_1,
             'FromPort': int(FROM_PORT_1),
             'ToPort': int(TO_PORT_1),
             'IpRanges': [{'CidrIp': CIDR_IP_1}]
            }
        ]
    )
    print('Ingress Successfully Set %s' % ingress_rule)
    print("")

    # Sets Egress Rule
    egress_rule = ec2.authorize_security_group_egress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': IP_PROTOCOL_1,
             'FromPort': int(FROM_PORT_1),
             'ToPort': int(TO_PORT_1),
             'IpRanges': [{'CidrIp': CIDR_IP_1}]}
        ]
    )
    print('Egress Successfully Set %s' % egress_rule)
    print("")
except ClientError as e:
    print(e)

