from create_key_pair import create_key
from instance import create_instance
from create_sec_group import create_sec_group

# Creates a key pair
create_key("some_key_name")


# Creates an instance
create_instance(
    "ami-0323c3dd2da7fb37d", 
    "some_key_name", 
    "t2.medium",
    1,      # Min
    1,      # Max
    "subnet-c74d1e8d"
    )


# Creates a sec group
create_sec_group(
    SECURITY_GROUP_NAME="SECURITY_GROUP_NAME2",
    DESCRIPTION="This is create by python",
    CIDR_IP_1="0.0.0.0/0",
    VPC_ID="vpc-1471ad6e",
    IP_PROTOCOL_1="tcp",
    FROM_PORT_1=0,
    TO_PORT_1=22,
    )

