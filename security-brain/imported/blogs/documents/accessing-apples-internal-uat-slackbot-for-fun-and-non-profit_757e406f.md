---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-07_accessing-apples-internal-uat-slackbot-for-fun-and-non-profit.md
original_filename: 2021-10-07_accessing-apples-internal-uat-slackbot-for-fun-and-non-profit.md
title: Accessing Apple’s internal UAT Slackbot for fun and non-profit
category: documents
detected_topics:
- oauth
- access-control
- xss
- sqli
- command-injection
- automation-abuse
tags:
- imported
- documents
- oauth
- access-control
- xss
- sqli
- command-injection
- automation-abuse
language: en
raw_sha256: 757e406fb261620c790526a8c137f3c8dd911f3e2be2e42f09f8d3ea014b8e22
text_sha256: ba72589122a3abc153cc9361eadd2338e7858bc053ba0b3c9cb9383f68197eeb
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Accessing Apple’s internal UAT Slackbot for fun and non-profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-07_accessing-apples-internal-uat-slackbot-for-fun-and-non-profit.md
- Source Type: markdown
- Detected Topics: oauth, access-control, xss, sqli, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `757e406fb261620c790526a8c137f3c8dd911f3e2be2e42f09f8d3ea014b8e22`
- Text SHA256: `ba72589122a3abc153cc9361eadd2338e7858bc053ba0b3c9cb9383f68197eeb`


## Content

---
title: "Accessing Apple’s internal UAT Slackbot for fun and non-profit"
url: "https://shail-official.medium.com/accessing-apples-internal-uat-slackbot-for-fun-and-non-profit-25b167605f38"
authors: ["Shail Patel (@shail_official)", "Ashish Kunwar (@D0rkerDevil)"]
programs: ["Apple"]
bugs: ["Broken authorization"]
publication_date: "2021-10-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3256
scraped_via: "browseros"
---

# Accessing Apple’s internal UAT Slackbot for fun and non-profit

Accessing Apple’s internal UAT Slackbot for fun and non-profit
Shail Patel
Follow
2 min read
·
Oct 7, 2021

67

Press enter or click to view image in full size

In December 2020, 
Ashish Kunwar
 and I went on a hunting spree against multiple Apple targets. To begin with, as usual, we started by collecting all of their subdomains first.

One interesting target that we stumbled upon was

https://uat-gsdcb.apple.com/

Tried exploiting for XSS, SQLi, and authentication vulnerabilities, but to no avail.

Then we thought of files and directory brute-forcing; maybe we missed something? A quick dirsearch lead us to https://uat-gsdcb.apple.com/INSTALL which in turn then redirected us to the following page upon allowing the bot to be installed:

Get Shail Patel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://uat-gsdcb.apple.com/oauth?code=1540913643671.1564171726854.0d5ecd2aab831447498227d1185fc376228752b769d8dd97f228919dad09b742&state=botkit

Press enter or click to view image in full size

Upon successful installation, we encountered this page:-

Press enter or click to view image in full size
Slackbot installed in our slack workspace
Press enter or click to view image in full size

This would have permitted an adversary to essentially send any slack communication messages, make potential alterations in their SDLC process, or interrupt their CI/CD pipeline, possibly disclose some sensitive information.

At this point, after gathering enough evidence, we stopped testing and brought this to Apple’s attention

Press enter or click to view image in full size
Apple’s usual automated reply

Now this was patched in less than two days, but as of today (October 6, 2021), we never received any hall of fame acknowledgment or bounty rewards despite of repeated follow-ups.

Date reported and triaged: Dec 13, 2020

Remediation timeline: Dec 15, 2020

Bounty awarded: $00

So, this was our terrible experience with Apple’s security program for the first vulnerability that we reported!!

Thanks for taking your time to read!
