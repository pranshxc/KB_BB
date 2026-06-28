---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-20_back-to-2019-disclosure-employers-pii-and-credentials.md
original_filename: 2020-10-20_back-to-2019-disclosure-employers-pii-and-credentials.md
title: 'Back to 2019: Disclosure Employers PII and Credentials'
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: c52d4e0786093684db31271202a6b2a3361d4464156f3da8ff14530bc8a599da
text_sha256: 63107fe41c9a24f540d04e3cd0992dd2db6295eeb89d8cc9a0245bdef6fda211
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Back to 2019: Disclosure Employers PII and Credentials

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-20_back-to-2019-disclosure-employers-pii-and-credentials.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c52d4e0786093684db31271202a6b2a3361d4464156f3da8ff14530bc8a599da`
- Text SHA256: `63107fe41c9a24f540d04e3cd0992dd2db6295eeb89d8cc9a0245bdef6fda211`


## Content

---
title: "Back to 2019: Disclosure Employers PII and Credentials"
url: "https://medium.com/@saneklarek22/back-to-2019-disclosure-employers-pii-and-credentials-bb7f344dcb08"
authors: ["Wh11teW0lf (@wh11tew0lf)"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2020-10-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4190
scraped_via: "browseros"
---

# Back to 2019: Disclosure Employers PII and Credentials

Back to 2019: Disclosure Employers PII and Credentials
Saneklarek
Follow
3 min read
·
Oct 20, 2020

61

1

Hi! I start my series of articles where i will show bugs founded by me on different Bug Bounty programs (mostly from HackerOne and Bugcrowd). It was announcement in my Twitter. The next article will be released in Friday and will cover some non-technical aspects of Bug Bounty.

Recon

The scope of target program was like:

*.example.com
*.anotherexample.com
somehost.fromdifferentproject.com
*.toomanyexamples.com

I like to do full recon on every target. This include ASN ranges, all company’s domains, opened ports, AWS IPs that belong to specific company, Github profiles etc. It can give to you internal paths, parameter names, filenames for “in scope” assets.

So i want to see a complete picture of the company. Time to use public data!

…

Get Saneklarek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This story will be about how to find many company’s domains using WHOIS information. Lets take Paypal as example.

Press enter or click to view image in full size

The most interesting part of a WHOIS response is specific entries that unique for company (it can be different for other domains of target). In this case is:

Registrant Organization: PayPal Inc.
Registrant Email:hostmaster@paypal.com

What we can do with this information? Maybe we can ask about that on Google? Lets try.

Press enter or click to view image in full size

As you see we found big amount of domains that registered for Paypal Inc. Easy!

…

With this i found domain that was registered for a target company which was called like exampleasia.com. Note that this domain is not marked as “in scope” so we cannot use big wordlists or actively scan hosts on this domain for vulnerabilities.On this case i always check Directory Indexing bugs. For this i use my wordlist with common directory names (1500 lines).

Scanning was completed and i start looking for results. From results i find that host bop.exampleasia.com have directory indexing on /webmaster/ filepath. On this folder was 2 another folders one of which called uploaded and located on /webmaster/uploaded/ filepath. This folder contained many PDF files which give to me username and password from the admin panel, personal information about employers (such as full name, personal telephone number and even address of living). Also, in this documents i was able to find usernames and passwords from other company’s assets (but not so critical). After my report company close this subdomain and reward me with 1000$ (as High).

Press enter or click to view image in full size
