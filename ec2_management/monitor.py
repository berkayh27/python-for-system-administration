# Instructions

# Enables and disables monitoring on the instances

# Run:

#       python monitor.py "i-009adb89402f1dc2c" "ON" 
#       python monitor.py "i-009adb89402f1dc2c" "OFF"   


import sys
import boto3
import sys 
INSTANCE_ID = sys.argv[1]

ec2 = boto3.client('ec2')
if sys.argv[2] == 'ON':
    response = ec2.monitor_instances(InstanceIds=[INSTANCE_ID])
else:
    response = ec2.unmonitor_instances(InstanceIds=[INSTANCE_ID])
print(response)