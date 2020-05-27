import boto3
ec2 = boto3.resource('ec2')

# create VPC
def create_vpc(CidrBlock):    
    response = ec2.create_vpc(
        CidrBlock=CidrBlock,
        DryRun=False,
        InstanceTenancy='default',
    )
    print(response)



def create_subnet(CidrBlock, VpcId):
    response = ec2.create_subnet(
        CidrBlock=CidrBlock,
        VpcId=VpcId,
        DryRun=False,
    )
    print(response)
