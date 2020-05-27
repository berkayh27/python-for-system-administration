import boto3
def create_instance(image_id, key_name, instance_type, min_count, max_count, subnet_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId = image_id,
        MinCount = min_count,
        MaxCount = max_count,
        InstanceType = instance_type,
        KeyName = key_name,
        SubnetId = subnet_id
        )
    print(instance[0].id)
# Following options can be set
# Unknown parameter in input: "s", must be one of: BlockDeviceMappings, ImageId, InstanceType, Ipv6AddressCount, Ipv6Addresses, KernelId, KeyName, MaxCount, MinCount, Monitoring, Placement, RamdiskId, SecurityGroupIds, SecurityGroups, SubnetId, UserData, AdditionalInfo, ClientToken, DisableApiTermination, DryRun, EbsOptimized, IamInstanceProfile, InstanceInitiatedShutdownBehavior, NetworkInterfaces, PrivateIpAddress, ElasticGpuSpecification, ElasticInferenceAccelerators, TagSpecifications, LaunchTemplate, InstanceMarketOptions, CreditSpecification, CpuOptions, CapacityReservationSpecification, HibernationOptions, LicenseSpecifications, MetadataOptions