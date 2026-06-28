---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-01_httpsmediumcommahitman1i-own-your-customers-22e965761abd.md
original_filename: 2018-09-01_httpsmediumcommahitman1i-own-your-customers-22e965761abd.md
title: https://medium.com/@mahitman1/i-own-your-customers-22e965761abd
category: documents
detected_topics:
- cloud-security
- idor
- command-injection
- password-reset
- otp
- information-disclosure
tags:
- imported
- documents
- cloud-security
- idor
- command-injection
- password-reset
- otp
- information-disclosure
language: en
raw_sha256: 59da91f91394d84e23f6fba9bc1be57ccc5067cd78d01625340e5b1cad61b33c
text_sha256: 3dbe36653964dbc4005c690dee6f5e8604588ae1097256a97e032f81980983d2
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# https://medium.com/@mahitman1/i-own-your-customers-22e965761abd

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-01_httpsmediumcommahitman1i-own-your-customers-22e965761abd.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, command-injection, password-reset, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `59da91f91394d84e23f6fba9bc1be57ccc5067cd78d01625340e5b1cad61b33c`
- Text SHA256: `3dbe36653964dbc4005c690dee6f5e8604588ae1097256a97e032f81980983d2`


## Content

---
title: "https://medium.com/@mahitman1/i-own-your-customers-22e965761abd"
page_title: "I Own Your Customers !!!. Hi This is my second write-up related… | by Muhammad Abdullah | Medium"
url: "https://medium.com/@mahitman1/i-own-your-customers-22e965761abd"
authors: ["Muhammad Abdullah"]
bugs: ["Information disclosure", "Hardcoded credentials", "AWS misconfiguration"]
publication_date: "2018-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5727
scraped_via: "browseros"
---

# https://medium.com/@mahitman1/i-own-your-customers-22e965761abd

Top highlight

I Own Your Customers !!!
Muhammad Abdullah
Follow
4 min read
·
Sep 1, 2018

228

Hi
This is my second write-up related to cryptoExchange Hacks.Last time I hacked an Exchange using IDOR vulnerability in Password Reset Function(Writeup here). This time it was something very interesting which I found.This lead me to access all the KYC documents of Users.

Background Story:

So these days I am not doing hunting much ,rather I am learning DPDK(Data Plane Development Kit) which is a Development kit by Intel to do fast packet processing.As much tutorials are not available on this so one has to goto whole documentation to learn.Btw Intel has a very Good documentation on DPDK.So fed up with reading documentation ,I wanted to relax myself.Earning some bounties was the way :p

So Basically I got access to all the KYC documents of Users of two projects by accessing the s3 Buckets.I will not be disclosing the names of the project.But one is a CryptoExchange with a good volume.Other is a Blockchain project backed by some reputable names in Crypto community.

1.Blockchain Project

Every time I start testing a website.My first step is to do recon on it as everyone does.So I fired up my subdomain recon scripts and found the following.

Press enter or click to view image in full size
Enumerated Subdomain

The one which looked interesting to me was (120185.xyz.com). Turns out this was the admin panel of the website.So I started trying to bypass the admin panel with different tricks.I don’t have the screenshot of Admin panel right now as they have taken it down.So after trying for an hour hopelessly I turned to Burp to see the site’s spidered structure.I started reading the js files which were accessible on the panel.

https://120185.xyz.com/js/app-1eda861a990702514571.bundle.js

While reading the file I found this.

Press enter or click to view image in full size

This got my attention and I searched for keyword bucket.And what I found shocked me.Hardcoded AWS access keys.

Press enter or click to view image in full size

I used the credentials to access the S3 bucket.User Kyc docs were uploaded into the bucket.I had access to thousand of KYC Docs.

Press enter or click to view image in full size

I didn’t downloaded any Doc being Ethical.And reported it to organization ASAP.They quickly implemented the fix.

Get Muhammad Abdullah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Takeaways:
-Always read the Javascript files ,you might get lucky.

Timeline:
August 29.2018 12:57 PM -> Report Sent
August 29,2018 7:30 PM ->Checked and Bug is Fixed

2.CryptoExchange

I guess this is one of the easiest bug I found and was handsomely rewarded.I won’t be disclosing the exchange name ,lets call it vuln.com.

I had no intentions of hunting this exchange.I visited this exchange to see the exchange rate of a token in which I had invested.Out of now where I opened the source code of the exchange.And I found this.

Press enter or click to view image in full size

Upon viewing this my inside Hacker instinct got awaken.And I opened the s3 bucket.The bucket was readable.What I found next was astonishing.Whole KYC Documents here too.Plus support ticket documents too.

Press enter or click to view image in full size
Bucket Listing
Press enter or click to view image in full size
KYC Docs
Press enter or click to view image in full size

Take Away:
~Do look at the source code.
~Always Check the Buckets you never know what juicy info you can get.

Timeline:
August 30,2018 1:12 PM -> Report sent
August 30,2018 4:00 PM -> Bug Fixed
August 30,2018 5:07PM -> Bounty Rewarded (10 ETH)
