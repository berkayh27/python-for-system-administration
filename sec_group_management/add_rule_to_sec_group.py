import boto3 
import sys
 
 
 
ec2 = boto3.resource('ec2')
mysg = ec2.create_security_group(GroupName="sg-0757f399e2b559659", Description="DESCRIPTION")
mysg.authorize_ingress(IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=80,ToPort=80) 
