---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-24_dangling-dns-aws-ec2.md
original_filename: 2020-09-24_dangling-dns-aws-ec2.md
title: 'Dangling DNS: AWS EC2'
category: documents
detected_topics:
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: 754fe1e24c6af2aa53b181b05ea58564e9db1ac159a418045dca97b334892bc4
text_sha256: e5c1871c27e3121229be8d02be0ced329b15f5f11537e4fb333361bfccdb7209
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Dangling DNS: AWS EC2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-24_dangling-dns-aws-ec2.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, automation-abuse, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `754fe1e24c6af2aa53b181b05ea58564e9db1ac159a418045dca97b334892bc4`
- Text SHA256: `e5c1871c27e3121229be8d02be0ced329b15f5f11537e4fb333361bfccdb7209`


## Content

---
title: "Dangling DNS: AWS EC2"
url: "https://medium.com/@mohamed.elbadry/dangling-dns-aws-ec2-e2d801701e8"
authors: ["Mohamed Elbadry (@_melbadry9)"]
bugs: ["Dangling DNS records", "Subdomain takeover"]
bounty: "2,900"
publication_date: "2020-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4241
scraped_via: "browseros"
---

# Dangling DNS: AWS EC2

D
angling DNS: AWS EC2
Mohamed Elbadry
Follow
5 min read
·
Sep 24, 2020

145

1

Note

New write-up regrading automation of this issue was published here.

Slightly update version of this write-up was published here.

About Me

I’m Mohamed Elbadry aka “melbadry9” (Bounty Hunter @ HackerOne).

Timeline

Oct 3rd, 2019: First Clue (Amazon Web Service)
Nov 24th, 2019: Second Clue (Company has a serious issue)
Nov 26th, 2019: Third Clue (Check open ports)
Dec 26th, 2019: Make sure it’s a dangling record
Jun 16th, 2020: Payment day
Jul 10th, 2020: The underlying issue and other targets

Oct 3rd, 2019

Asset: Private Program #1 (*.example.com)
Report:
Press enter or click to view image in full size
Details:

I began with enumerating subdomains using Sublist3r when i stumbled upon interesting subdomain “fig.example.com”. (I have no idea why it was interesting but it was )

I opened “http;//fig.example.com/” on the browser it show nothing but a blank page with empty HTML code, So i decided to brute force directories using Dirsearch. when I found ‘http://fig.example.com/includes/’ directory with directory listing enabled.

I reported it and got the following respond.

Press enter or click to view image in full size

So I decided to look for similar issue with the reset of subdomains, Soon after i found two other subdomains “github.example.com” and “goose.example.com” with the same issue. How did i know it was? It’s simple it was redirecting to a totally different site.

Then checked the DNS records maybe it will help me identify other subdomains with same issue.

Press enter or click to view image in full size

When i realized what they have in common “Amazon Web Service”.

Then I decided to filter the subdomains based on there CNAMEs record, I used this tool which i have created. Now let’s check for similar issue, After spending 1h no luck. now we need to let go for now.

What i have missed? it’s simple check for open ports Dah!

Nov 24th, 2019

Asset: Private Program #1 (*.example.com)
Report:
Press enter or click to view image in full size
Respond:
Press enter or click to view image in full size

Now i know that this program has serious issue with dangling DNS records.

Nov 26th, 2019

Asset: Private Program #1 (*.example.com)
Report:
Press enter or click to view image in full size

Dec 26th, 2019

Now we have a list of possible subdomain with dangling DNS with no way to make sure it’s really is.

Get Mohamed Elbadry’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

what can we do?

Let’s check SSL Certificate.
Press enter or click to view image in full size
It’s definitely not our target :D
Let’s check Shodan for archived SSL Certificate
Press enter or click to view image in full size
Press enter or click to view image in full size
It’s a dangling DNS for sure.
Let’s use google dorks or Bing “ip: 54.161.231.55”
Maybe all you have to do is asking :D
Press enter or click to view image in full size
It’s great when you build trust with the security team :)

Jun 16th, 2020

Asset: Private Program #1 (*.example.com)
Report:
Press enter or click to view image in full size
Details:

After Monitor subdomains and confirming that every subdomain has a dangling DNS record before reporting, The program asked me to supply every possible Dangling record and they will confirm it all at once.

Turned out they all had a dangling DNS records!!

Jul 10th, 2020

It’s all started on Oct 7, 2015 when Matt Bryant blogged (Fishing the AWS IP Pool for Dangling Domains) about AWS IP pool.

“What happened to that IP tied to that EC2 instance that you just killed? Well, when you terminate an instance, that IP address isn’t put to waste. Instead, it’s reused by other AWS customers. There is a massive pool of IP addresses that are constantly being recycled and trusted by various organizations and people.”

The issue happens when company use EC2 instance without using elastic IP.

If the EC2 instance is killed or terminated and the DNS not updated this will lead to creating a dangling DNS record for the subdomain.

The EC2 IP will be released to AWS IPs pool, This mean it’s possible to assign the IP to new EC2 instance.

How to find this kind of issues?

Check for compute.amazonaws.com or compute-1.amazonaws.com in CNAME .
Confirm that it’s a dangling DNS before reporting to avoid (N/A), As mentioned before.

Case Studies

Asset: Transloadit
Press enter or click to view image in full size
Asset: Avast
Press enter or click to view image in full size
Asset: Amazon

As funny as it is Amazon itself had a similar issue.

Press enter or click to view image in full size
Asset: Private Programs
Press enter or click to view image in full size
Press enter or click to view image in full size

A piece of advice

Don’t ignore old researches, It might be old but not dead.
Building trust with security teams is great and it’s a two-way street.

Contacts

Facebook
Twitter
LinkedIn
