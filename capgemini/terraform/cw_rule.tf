resource "aws_cloudwatch_event_rule" "console" {
  name        = "capture-sec-groups"
  description = "Capture each Security Groups More Granular"

  event_pattern = <<EOF
{
  "source": [
    "aws.ec2"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "ec2.amazonaws.com"
    ],
    "eventName": [
      "CreateSecurityGroup",
      "AuthorizeSecurityGroupIngress",
      "AuthorizeSecurityGroupEgress",
      "RevokeSecurityGroupIngress",
      "RevokeSecurityGroupEgress"
    ]
  }
}
EOF
}

resource "aws_cloudwatch_event_target" "sns" {
  rule      = "${aws_cloudwatch_event_rule.console.name}"
  target_id = "SendToSNS"
  arn       = "arn:aws:sns:us-east-1:607546651489:email_from_security_groups"
  input_transformer = {
    input_paths = { "name"="$.detail.requestParameters.groupId","source"="$.detail.eventName","time"="$.time","value"="$.detail" }
    input_template = "\"A <source> API call was made against the security group <name> on <time> with the below details\" \n \" <value> \""
  }

}


resource "aws_sns_topic" "aws_logins" {
  name = "aws-console-logins"
}