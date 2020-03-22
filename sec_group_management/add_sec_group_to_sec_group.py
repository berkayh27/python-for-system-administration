# Instructions
# Run: 
#       python add_sec_group_to_sec_group.py "sg-0757f399e2b559659"  "launch-wizard-2"
#   NOTE:   1st input takes ID
#           2nd input takes name of sec group

import logging
import boto3
from botocore.exceptions import ClientError
import sys

MODIFIED_SECURITY_GROUP_ID = sys.argv[1]
ADDED_SECURITY_GROUP_NAME = sys.argv[2]


def add_security_group_to_security_group(security_group_id,
                                         source_security_group_name,
                                         source_security_group_owner_id=''):
    # Add the security group
    ec2_client = boto3.client('ec2')
    try:
        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            SourceSecurityGroupName=source_security_group_name,
            SourceSecurityGroupOwnerId=source_security_group_owner_id)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise add_security_group_to_security_group()"""

    # Assign these values before running the program
    security_group_id = MODIFIED_SECURITY_GROUP_ID    # Note: Group ID
    security_group_name = ADDED_SECURITY_GROUP_NAME   # Note: Group Name
    added_security_group_owner_id = ''                  # AWS account ID

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Add the security group to the other security group
    if add_security_group_to_security_group(security_group_id,
                                            security_group_name,
                                            added_security_group_owner_id):
        logging.info(f'Added security group {security_group_name} '
                     f'to security group {security_group_id}')


if __name__ == '__main__':
    main()