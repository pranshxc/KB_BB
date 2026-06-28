---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-17_hacking-a-nft-platform.md
original_filename: 2022-06-17_hacking-a-nft-platform.md
title: Hacking a NFT Platform
category: documents
detected_topics:
- ssrf
- cloud-security
- idor
- command-injection
tags:
- imported
- documents
- ssrf
- cloud-security
- idor
- command-injection
language: en
raw_sha256: 47f7f8280309888d3f4214997228fca8b77bfd707c5318f71045544823a28662
text_sha256: 568a6b8c938d180601ae48f137ac9bb694fdf9a8ddab3671303e50a01217c41c
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking a NFT Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-17_hacking-a-nft-platform.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, idor, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `47f7f8280309888d3f4214997228fca8b77bfd707c5318f71045544823a28662`
- Text SHA256: `568a6b8c938d180601ae48f137ac9bb694fdf9a8ddab3671303e50a01217c41c`


## Content

---
title: "Hacking a NFT Platform"
page_title: "Hacking a NFT Marketplace. Background: | by Muhammad Abdullah | Medium"
url: "https://medium.com/@mahitman1/hacking-a-nft-platform-56fc59479d3b"
authors: ["Muhammad Abdullah"]
bugs: ["SSRF"]
publication_date: "2022-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2538
scraped_via: "browseros"
---

# Hacking a NFT Platform

Hacking a NFT Marketplace
Muhammad Abdullah
Follow
2 min read
·
Jun 18, 2022

127

Background:

I will be doing a series of posts regarding my finding in Blockchain related platforms. These series of posts are inspired by the talk presented by https://twitter.com/samwcyo at Nahamcon. I have already posted 2 of my writeups regarding the subject. You can check them Below.

Hacking a Crypto Debit Card Service
Background:

medium.com

I Own Your Customers !!!
Hi This is my second write-up related to cryptoExchange Hacks.Last time I hacked an Exchange using IDOR vulnerability…

medium.com

Vulnerability:

The vulnerable platform was “cargo.build”. The Platform is now down as it has been acquired. I found a SSRF vulnerability which allowed me to gain access to the backend code moreover it was possible to escalate the issue to RCE.

Testing:

I found this issue during the hype of NFT craze , I was exploring the craze and came across the Platform. My habit is to run Burp in the background while surfing the internet , who knows what you come across. While surfing https://cargo.build I noticed a url which was being used to fetch the NFT images.

http://api2.cargo.build/v3/image?src=URL

Now my first guess was that it might be vuln to SSRF. So I fired up my Burp Collaborator and sent the request. And to my guess it was true and I got a ping from the server trying to fetch the image.

Get Muhammad Abdullah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next I tried

https://api2.cargo.build/v3/image?src=http://169.254.169.254/

And yes your guess is true I got the AWS metadata.

I retrieved the elasticbeanstalk cred via following

https://api2.cargo.build/v3/image?src=http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role

Next I listed the bucket via following

aws s3 ls s3:// elasticbeanstalk-us-west-2–ACCOUNTID/ — recursive

Press enter or click to view image in full size
Bucket Listing

This was enough to show the impact of the issue.

Result:

The team was super responsive and issue was fixed within an hour.

Bounty Awarded: 2 ETH
