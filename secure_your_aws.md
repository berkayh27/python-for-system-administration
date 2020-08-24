# README

![](.gitbook/assets/secure.jpg)

## This repo is used for securing AWS

### It deals with:

1. AWS Password Policy
2. Enables CloudTrail
3. Enables Lambda Function to Secure AWS Security Groups. 1. It removes rules if rule allows 0.0.0.0/0 for multiple ports unless defined otherwise
4. It creates Config Rule for 1. S3 1. Tags compliance 2. encryption
   1. IAM
      1. Access Key Rotation
5. Creates CloudWatch Event Rule to Notify about SecGroups that is created
   1. Sends an email to a specific email address when new sec group created. 
6. Creates CloudWatch Event Rule when someone logs in thru console
   1. Sends an email to a specific email address when new sec group created. 

