regions = [
    "us-east-1",
    "us-east-2"
    ]
for region in regions:
    client = boto3.client('ec2', region_name=region)
    try:
        response = client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print("Instance: " + instance['InstanceId'])
                for securityGroup in instance['SecurityGroups']:
                    print("SG ID: {}, Name: {}".format(securityGroup['GroupId'], securityGroup['GroupName']))

    except Exception as E:
        print(region, E)
        continue