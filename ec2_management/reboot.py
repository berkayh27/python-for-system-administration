# Instructions
# Run:

#       python reboot.py "i-009adb89402f1dc2c"


import boto3
from botocore.exceptions import ClientError
import sys 
INSTANCE_ID = sys.argv[1]
print(INSTANCE_ID)
ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise
try:
    response = ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=False)
    print('Success', response)
    print("Instance %s is being restarted"   % INSTANCE_ID )
except ClientError as e:
    print('Error', e)