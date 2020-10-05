#!/bin/python 
import boto3 
import time
# Below code goes thru all the sec groups in AWS and checks if the sec groups are idle or attached. 
# If it is idle gives you a list 

ec2 = boto3.client("ec2")
elb = boto3.client('elb')
redis = boto3.client("elasticache")

print("Pulling Instance information")
all_instances = ec2.describe_instances() 

print("Pulling Sec Group information")
all_sg = ec2.describe_security_groups()

print("Pulling ELB information")
all_elb = elb.describe_load_balancers()

print("Pulling Redis information")
all_redis = redis.describe_cache_clusters()


# Creates empty sets
instance_sg_set = set()
sg_set = set()
elb_set = set()
redis_set = set()


# Gest a list of security groups on AWS
for security_group in all_sg["SecurityGroups"] :
  sg_set.add(security_group ["GroupId"])


# Gets  a list of security groups from Instances
for reservation in all_instances["Reservations"] :
  for instance in reservation["Instances"]: 
    for sg in instance["SecurityGroups"]:
      instance_sg_set.add(sg["GroupId"]) 


# Gets all the security groups  attached to ELBs
for sg_elbs in all_elb["LoadBalancerDescriptions"]:
    for sg in sg_elbs["SecurityGroups"]:
        elb_set.add(sg)
        


try:
  # Gets all the security groups attached to Redis
  for redis in all_redis["CacheClusters"]:  
      for thing in redis["SecurityGroups"]:
            redis_set.add(thing.get("SecurityGroupId"))
except:
  pass
finally:
  print("Good to go")




# Finalizes by substracting sec groups
idle_sg = sg_set - instance_sg_set - elb_set - redis_set
print("These are idle sec groups" + "=" + str(idle_sg))
print("Above is the %d idle sec groups" % len(idle_sg))

idle_sg_list = list(idle_sg)
response = ec2.describe_security_groups(GroupIds = idle_sg_list)
response = response.get("SecurityGroups")




#---------------------------------#---------------------------------#---------------------------------
# Below function finds sec groups that starts with a string
sec_group_by_name = []
def find_sec_groups(NAME):
  for i in response:
    GroupName = i.get("GroupName")
    GroupId = i.get("GroupId")
    NEWLIST = i.get("IpPermissions")
    for i in NEWLIST:
      IP_RANGE = i.get("IpRanges")
      #print(GroupName, GroupId, IP_RANGE)
      if GroupName.startswith(NAME):
        #print(GroupName, GroupId, IP_RANGE)
        sec_group_by_name.append(GroupId)

find_sec_groups("terraform")      
print(sec_group_by_name)
#---------------------------------#---------------------------------#---------------------------------









# ---------------------------------#---------------------------------#---------------------------------
#Delete security group
# # This will keep track of deleted sec groups. It can not be in for loop it should be outside of for loop to keep track of each
deleted_sg_set = set() 
for i in sec_group_by_name:
    #input("Should I proceed?")
    try:
        # This can be removed if not used with 6379
        # This line below removes rules that allow port 6379 for 0.0.0.0
        client = boto3.client('ec2')
        response = client.revoke_security_group_ingress(
            DryRun=False,
            GroupId=i,
            IpPermissions=[
                {
                    'FromPort': 6379,
                    'IpProtocol': 'TCP',
                    'IpRanges': [
                        {
                            'CidrIp': '0.0.0.0/0'
                        },
                    ],
                    'ToPort': 6379
                },
            ],
        )
        # This line below removes rules that allow port 6379 for 0.0.0.0
        response = ec2.delete_security_group(GroupId=i)
        deleted_sg_set.add(i)
        print('Security Group Deleted',  i)
        print(deleted_sg_set)

    except Exception as e:
        print(e)
# ----------@-----------------------#---------------------------------#---------------------------------



