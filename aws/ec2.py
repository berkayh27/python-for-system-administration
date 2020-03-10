import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)


ec2.monitor_instances('i-0fb4cc9d4978c6e57')