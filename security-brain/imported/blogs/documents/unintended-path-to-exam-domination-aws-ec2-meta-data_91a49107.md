---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-24_unintended-path-to-exam-domination-aws-ec2-meta-data.md
original_filename: 2023-05-24_unintended-path-to-exam-domination-aws-ec2-meta-data.md
title: Unintended Path to Exam Domination - AWS EC2 Meta-Data
category: documents
detected_topics:
- cloud-security
- access-control
- ssrf
- command-injection
- otp
- api-security
tags:
- imported
- documents
- cloud-security
- access-control
- ssrf
- command-injection
- otp
- api-security
language: en
raw_sha256: 91a49107d18a3e452cea4033b31bb76a45d2e320f4613474a2ff394ba5df2916
text_sha256: 0b7cc40774bd6b6fb8480eddf28577c5e39b91872ef2671ba63447ac8c646ec7
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Unintended Path to Exam Domination - AWS EC2 Meta-Data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-24_unintended-path-to-exam-domination-aws-ec2-meta-data.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, ssrf, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `91a49107d18a3e452cea4033b31bb76a45d2e320f4613474a2ff394ba5df2916`
- Text SHA256: `0b7cc40774bd6b6fb8480eddf28577c5e39b91872ef2671ba63447ac8c646ec7`


## Content

---
title: "Unintended Path to Exam Domination - AWS EC2 Meta-Data"
page_title: "Unintended Path to Exam Domination - AWS EC2 Meta-Data :: Rootcat"
url: "https://www.rootcat.de/blog/ec2-meta_may23/"
final_url: "https://rootcat.de/blog/ec2-meta_may23/"
authors: ["Dr. Michael Gschwender (@rootcathacking)"]
bugs: ["Cloud", "Privilege escalation"]
publication_date: "2023-05-24"
added_date: "2023-05-29"
source: "pentester.land/writeups.json"
original_index: 1120
---

## [Unintended Path to Exam Domination - AWS EC2 Meta-Data](https://rootcat.de/blog/ec2-meta_may23/)

This is directed to everyone using aws EC2 for CTF’s, labs or offensive security exams.

What prompted me to write this, is that the last three times in a row, whenever I found myself in an exam environment for pentesting/redteaming (and yes even one cloud exam), _meta-data_ and _user-data_ basically allowed to circumvent the exam or just strait up break out of the environment. I will not name any names here, instead I want to explain what the problem in this specific case is and provide resources and thoughts at the end in order to provide some help on this issue.

I will however say that this is just the most prevalent issue stemming from even some well-known industry exams having very unsecure aws environments. It is sadly obvious that for a lot of certification providers cloud security seems to be not even on the radar, as long as the lab deploys, and the cost is low.

## Notice and Update November 2023

This was initially written for the Metadata Service Version 1 (IMDSv1) – a request/response method, which was the de facto default at the time. Now, the Instance Metadata Service Version 2 (IMDSv2), is a session-oriented method and is currently the default for an out of the box windows “install” on aws, hence the short update on this post.

Everything in this post is still valid and for IMDSv1 remains unchanged, for IMDSv2 I put the updated commands on the end of this post.

## The issue

To explain this somewhat generally, I will reduce some complexity and limit this to the issues of meta- and user-data only.

Imagine you are in a hacking exam, your goal is to own the DC, get flags etc. Let’s say you have RDP to a Windows VM and on the Desktop, you see something like this:

![](https://rootcat.de/blog/ec2-meta/desktop.png) This is meta-data from the EC2 Instance, containing things like IP, availability zones, hostname and a bunch of other information. When you see this, you know you can probably access the aws meta-data service endpoint, from the EC2 via:
  
  
  curl http://169.254.169.254/latest/meta-data
  

This will contain all sorts of information, including the connected resources like security-groups, subnets and so on (maybe open-ports and the like). This alone might be stuff you should not be seeing, from the standpoint of the cert provider. And yes of course this is not operating system dependent:

![](https://rootcat.de/blog/ec2-meta/from_ec2.png)

Sidenote: You can also get the aws keys/token from this via:
  
  
  curl http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance
  

or directly in the browser  ![](https://rootcat.de/blog/ec2-meta/windows_meta_data.png)

But lab breakout is not my focus here, so I will not get into it too much here, but let me just say the following:  
In the screenshot above you see temporary creds for the EC2 (which I used in this example), which is good, read about it [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html), however, which keys you find here (or on other services…) depends on the lab setup. It is not uncommon that without too much hassle you get to the CloudFormation stack from here, or if it’s really bad basically take the whole aws account. In short protect your keys, make sure to limit the capabilities of the access keys, please don’t give everything just poweruser or admin permission. Yes, I know aws permission and roles makes one mad in the brain, believe me I know dis, but at least try to limit it somewhat, doesn’t have to be purrfect.

Back on topic.

So meta-data might be something (besides the aws key issue) that should not be seen from inside the lab, but there is another thing to watch out for - user-data. So, when setting up an exam environment you have to configure some stuff, like AD-accounts and the lot. Let’s consider the following example:

A Windows VM runs a script at startup to add an admin user (yes it wouldn’t work like this but it’s easier to understand for this example; the commands would be in a script but otherwise same principle)  ![](https://rootcat.de/blog/ec2-meta/ec2_win_build.png) This is what user-data is for. On the screenshot you also see the selection for the access to the discussed meta-data, typically it is on by default.

So where this user-data ends up depends, on a lot of factors, in this specific case though, it ends up in a log-file on the VM itself. In this case located in
  
  
  C:\ProgramData\Amazon\EC2Launch\log\agent.log
  

but have a look [here](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch.html), for more details.

![](https://rootcat.de/blog/ec2-meta/user-data.png)

So, to make this clear, if this is done like this, one can just access the EC2 launch log agent and get the credentials directly. Jap, this means the whole idea going through multiple windows clients, doing fancy ad magic, proxy-chaining some stuff can be entirely sidestepped, by accessing the user-data scripts. (Even though I call this hacking, this might not be what the exam provider had in mind.)

Of course, this is a general issue, not just in the case of my Windows example here. Typically, no matter how you deploy (CloudFormation, yaml, terraforms, etc.) you will give it something that aws puts in user-data, the question is more like, where exactly it ends up and how can it be accessed. To give another example, imagine a deployment of an Ubuntu VM via yaml and CloudFormation stack, at some point you give it something to run at startup, which might look like this:  ![](https://rootcat.de/blog/ec2-meta/user-data-input-yaml.png) This can then be accessed similar to meta-data from inside (if it is stored inside the VM). However, its tricky where what ends up, but in case of Ubuntu, it’s worth to try locking into:
  
  
  /var/log/cloud-init.log
  /var/log/cloud-init-output.log
  /var/lib/cloud/instances/instance-id/
  

Or it can be accessed, with dumped keys, from outside, like so:
  
  
  aws ec2 describe-instance-attribute --instance-id i-.... --attribute userData --output text --query "UserData.Value" | base64 --decode
  

![](https://rootcat.de/blog/ec2-meta/user-data-outside.png)

## Some thoughts on securing

So, there are two things to watch out for, _meta-data_ and _user-data_. In the case of meta-data the best would be to just outright disable the endpoint, either directly in the deploy or via aws cli:
  
  
  aws ec2 modify-instance-metadata-options --instance-id i-.... --http-endpoint disabled
  

However, it might be that your lab/exam needs it to function because it gets the IP from it, then it gets complicated but doable. This -> [document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) from aws will help.

Unfortunately for user-data this is a little more complex. All of it is really heavily dependent on your deployment, setup and what you actually run in the scripts. In principle you can have a look at aws docs first -> [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html).

Then maybe read up, if your using terraform on the SSM Parameters Store and the secure strings, check out blogs like [this one](https://advancedweb.hu/how-to-use-ssm-parameter-store-for-sensitive-inputs-in-terraform/). Another path might be to use the aws secret vault and all the multitude of options with these things, check one out -> [here](https://developer.hashicorp.com/vault/docs/secrets/aws).

But I got to be honest here, not only is all of this hilariously complex, but it also introduces a whole new bunch of attack surface, with new roles, permissions and tokens.

My best advice would therefore be the following:

Have a look at your lab/exam. Find all the ways in there to access meta-data and user-data, understand where (and if) it is stored. Identify the risk to your lab/exam in terms of sidestepping your exam path and in terms of escalating outside of your environment with the used keys. Then try to circumvent those in the frame of your deployment and understanding, so you do not introduce new vulnerabilities by misconfiguring your key vault etc. If you know a cloud hacker, maybe let them have a look. It doesn’t have to be completely bulletproof and it probably never will, but at least make sure it’s not possible to immediately drop juicy aws keys, or read out the domain-admin password, via user-data in log file.

## IMDSv2

Because the IMDSv2 of the meta-data service, is now session based, you need a token if you want to access meta or user-data. The structure of the data itself remains the same.  
If you try to access meta-data on IMDSv2, with a simple curl or directly in the browser you will get an access denied.

So one strait up way to do this, is to start powershell and ask for a token, like this:
  
  
  [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token
  

Then use this token to access meta-data and drop the keys as above, like so:
  
  
  Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance
  

You are not limited to powershell of course, but you must ask for a token first and send said token in order to access IMDSv2.
