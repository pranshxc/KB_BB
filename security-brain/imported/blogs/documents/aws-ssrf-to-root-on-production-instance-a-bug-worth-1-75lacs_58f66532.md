---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-27_aws-ssrf-to-root-on-production-instance-a-bug-worth-175lacs.md
original_filename: 2022-10-27_aws-ssrf-to-root-on-production-instance-a-bug-worth-175lacs.md
title: AWS SSRF to Root on production instance — A bug worth 1.75Lacs
category: documents
detected_topics:
- ssrf
- command-injection
- cloud-security
- sso
- password-reset
- otp
tags:
- imported
- documents
- ssrf
- command-injection
- cloud-security
- sso
- password-reset
- otp
language: en
raw_sha256: 58f66532b8f12dadd236f46f01b1e948cda59726548cc7f80f83dd7c1a973799
text_sha256: 7338c4148228d9145c537860a723137a1be846570bbe5d364fe42a723fbcd28d
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# AWS SSRF to Root on production instance — A bug worth 1.75Lacs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-27_aws-ssrf-to-root-on-production-instance-a-bug-worth-175lacs.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cloud-security, sso, password-reset, otp
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `58f66532b8f12dadd236f46f01b1e948cda59726548cc7f80f83dd7c1a973799`
- Text SHA256: `7338c4148228d9145c537860a723137a1be846570bbe5d364fe42a723fbcd28d`


## Content

---
title: "AWS SSRF to Root on production instance — A bug worth 1.75Lacs"
url: "https://logicbomb.medium.com/a-bug-worth-1-75lacs-aws-ssrf-to-rce-8d43d5fda899"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["SSRF", "RCE", "Password reset"]
publication_date: "2022-10-27"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1978
scraped_via: "browseros"
---

# AWS SSRF to Root on production instance — A bug worth 1.75Lacs

AWS SSRF to Root on production instance — A bug worth 1.75Lacs
Avinash Jain (@logicbomb)
Follow
3 min read
·
Oct 27, 2022

602

4

I
t’s been some time since I blogged mainly because there was not something new I could find in the last 6–7 months of bug bounty. Fortunately, this month started with a nice bug that I discovered in a Trading Platform. Let’s get straight away to the vulnerability writeup, would try to keep it short and crisp so here you go. This is about —

How I escalated well-known AWS SSRF to perform Remote Code Execution (RCE) in one of India’s growing Trading startups.
Press enter or click to view image in full size

I was manually traversing to different sections of the app to look for some sensitive API endpoints and parallelly I added the target scope to “Crawl and Audit” in Burpsuite. In the app, there was a usual “Password Reset” functionality. Looking closely at the endpoint, there was a parameter “return_url”. Such parameters always have the potential of carrying some easy-find bugs. And my expectations proved right when Burpsuite discovered an “External service interaction (DNS)” vulnerability in the same endpoint. While checking different HTTP request headers, it was clear that the application was over AWS since I could see the Response Header as X-Amz-Cf-Id and there was also an S3 bucket interaction for fetching profile photos.

The next move was clear to check if there is any SSRF possible or not. I tried accessing the AWS metadata URL (http://169.254.169.254/latest/meta-data/)and below was the response to the CURL request —

Press enter or click to view image in full size

Fetching security credentials from instance metadata —

Press enter or click to view image in full size

and that confirmed the SSRF for me.

Now it’s time to extend it further and this is what one should always try to do —

Escalate the vulnerability by trying out every possibility associated with it. That will increase the impact of the bug and also fetch much better rewards.

AWS provides a service called AWS System manager to manage applications and infrastructure running in the AWS Cloud which can be used by command-line tools as well. Ref — https://docs.aws.amazon.com/cli/latest/reference/ssm/index.html

The one thing that ran in my favor here was in order to run remote commands in the instance via SSM, it should have a relevant role attached to the instance.

Install and configure AWS CLI by using the above security credentials.
$ export ***REDACTED-AWS-KEY***_ID=
$ export ***REDACTED-AWS-KEY***_ACCESS_KEY=
$ export AWS_DEFAULT_REGION=
$ export AWS_SESSION_TOKEN=

2. Below command can be used to find the region used in the 1st step- http://169.254.169.254/latest/meta-data/placement/availability-zone

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Use send-command to execute the command, the query looks like this-

$ aws ssm send-command --document-name "AWS-RunShellScript" --comment "AnyComment" --instance-ids="[Instance-id]" --parameters "commands=whoami"

The output of this command provides a CommandId

Press enter or click to view image in full size

4. To get the instance ID used in the 3rd step- http://169.254.169.254/latest/meta-data/instance-id

5. Final step to see the output of the command executed (as used in step 3 “whoami”)-

$ aws ssm list-command-invocations --command-id="[Command_Id]" --details
Press enter or click to view image in full size

Pheww and finally I was able to get the command executed. One can see the output as “root”! And this is how I was able to escalate AWS SSRF to RCE. That’s it from this short writeup.

Report details-

8-Oct-2022 — Bug reported to the concerned company.

12-Oct-2022 — Bug was marked fixed.

15-Oct-2022 — Re-tested and confirmed the fix.

23-Oct-2022 — Rewarded.

Thanks for reading!

Twitter ~ logicbomb_1

Site ~ https://logicbomb.in/
