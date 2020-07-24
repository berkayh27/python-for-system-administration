import boto3 
# This script below takes a sec group ID in line 5 and takes a list of ports that has 0.0.0.0/0 ports open and removes the rules

# Tell which region to work on 
ec2 = boto3.resource('ec2', region_name='eu-central-1')

# Tell which sec group to work on 
security_group = ec2.SecurityGroup('sg-3a47b855')

# List of ports to check and remove
LIST_OF_PORTS = [22, 80, 3306]

for i in LIST_OF_PORTS:
    response = security_group.revoke_ingress(
        IpPermissions=[
            {
                'FromPort': i,
                'ToPort': i,
                'IpProtocol': 'TCP',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                    },
                ],
            },
        ],
    )