---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-17_a-story-of-my-first-bug-bounty.md
original_filename: 2022-07-17_a-story-of-my-first-bug-bounty.md
title: A Story Of My First Bug Bounty
category: documents
detected_topics:
- command-injection
- information-disclosure
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- information-disclosure
- cloud-security
- supply-chain
language: en
raw_sha256: 427ba0d5264a92094450137509c9fe22f1dbe47f4faac58241633130f9c4b96e
text_sha256: 5afa62420c4bd2df378bffc3c0959a1f0d94a19bed2e71fcebd56eac3969105c
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# A Story Of My First Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-17_a-story-of-my-first-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `427ba0d5264a92094450137509c9fe22f1dbe47f4faac58241633130f9c4b96e`
- Text SHA256: `5afa62420c4bd2df378bffc3c0959a1f0d94a19bed2e71fcebd56eac3969105c`


## Content

---
title: "A Story Of My First Bug Bounty"
url: "https://medium.com/@rajqureshi07/a-story-of-my-first-bug-bounty-dda320db78d9"
authors: ["Raj Qureshi (@RajQureshi9)"]
bugs: ["Information disclosure"]
publication_date: "2022-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2439
scraped_via: "browseros"
---

# A Story Of My First Bug Bounty

A Story Of My First Bug Bounty
Raj Qureshi
2 min read
·
Jul 17, 2022

--

7

--

Hello everyone,

This is my first article. This article will talk about how I earned a first bounty. Let me introduce myself I am Raj Qureshi and I am a penetration tester.

After practicing on web application attacks, I started to try to check some websites related to bug bounty programs. I would like to share with you how I got my first bounty.

The company didn’t want me to publish their name. For this reason, I’ll call it “target.com”. Let’s begin! As everyone knows, there are a lot of testers on Hacker One and the Bug crowd platform.

So I would prefer to google for a responsible disclosure program. I have selected the site. Let’s call target.com. Performing testing for this, I checked all the functions and all the options there.

Unfortunately, I couldn’t find anything on the main website of the company’s website. So I think I have to check the vulnerability on target.com’s subdomain.

For that purpose. I have used the Sublist3r tool that helps me to find all subdomains related to target.com.After some research, I picked up the target called “backup.target.com”.

I noticed that this website is a little old and this website uses laravel framework. then I am researching about the laravel framework and looking for the directory structure of laravel.

Now i am checking for directory listening. And i got the .env file. This file contains some common configuration values that may differ based on whether your application is running locally or on a production web server.

In that file, I found the following information.

***REDACTED-AWS-KEY***_ID=Value

***REDACTED-AWS-KEY***_ACCESS_KEY=Value

AWS_DEFAULT_REGION=Value

AWS_BUCKET=Value

Now, this time to exploit first of all, I have installed the AWS CLI tool by using

Get Raj Qureshi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

pip3 install awscli command.

After that, I run aws configure command and put the value that found in .env file.

***REDACTED-AWS-KEY***_ID=Value

***REDACTED-AWS-KEY***_ACCESS_KEY=Value

AWS_DEFAULT_REGION=Value

AWS_BUCKET=Value

Then run following command

aws s3 ls s3://AWS_BUCKET_NAME

I got the list of directories available in that bucket.

Finally, I got my first bounty! After I reported to target.com.

I got a message from them that I earned a three digit $ bounty from this vulnerability and the happiest thing is that the company closed this vulnerability successfully!

That’s it for this article, I hope you enjoy reading it!

Follow me on Twitter.
