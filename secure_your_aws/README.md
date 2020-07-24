<img src="./images/secure.jpg" width="1200" />

# This repo is used for securing AWS
## It deals with:
1. AWS Password Policy
2. Enables CloudTrail
3. Enables Lambda Function to Secure AWS Security Groups.
   1. It removes rules if rule allows 0.0.0.0/0 for multiple ports unless defined otherwise

4. It creates Config Rule for 
   1. S3
      1. Tags compliance
      2. encryption

    2. IAM
       1.  Access Key Rotation


5. Creates CloudWatch Event Rule to Notify about SecGroups that is created
   1. Sends an email to a specific email address when new sec group created. 


6. Creates CloudWatch Event Rule when someone logs in thru console
   1. Sends an email to a specific email address when new sec group created. 


[![asciicast](https://asciinema.org/a/dtXcoxgpPhXSRW60s7cluMRro.png)](https://asciinema.org/a/dtXcoxgpPhXSRW60s7cluMRro)

<a href="https://asciinema.org/a/dtXcoxgpPhXSRW60s7cluMRro?autoplay=1"><img src="https://asciinema.org/a/dtXcoxgpPhXSRW60s7cluMRro.png" width="836"/></a>
