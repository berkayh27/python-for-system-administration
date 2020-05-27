from create_key_pair import create_key
from instance import create_instance


create_key("some_key_name")
create_instance(
    "ami-0323c3dd2da7fb37d", 
    "some_key_name", 
    "t2.medium",
    1,      # Min
    1,      # Max
    "subnet-c74d1e8d",
    )
