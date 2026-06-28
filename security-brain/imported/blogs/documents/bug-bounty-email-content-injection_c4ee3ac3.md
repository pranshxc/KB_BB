---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-12_bug-bounty-email-content-injection.md
original_filename: 2020-03-12_bug-bounty-email-content-injection.md
title: '[Bug Bounty] Email Content Injection'
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: c4ee3ac3a60f1bf772ae14e6ad7818a087c77a30b92eaf9c8ec9d14de0c0c328
text_sha256: 4ea6be2dab3dafd0300e604f60c95951df53d2c9635b01decfef1f4d29468546
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# [Bug Bounty] Email Content Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-12_bug-bounty-email-content-injection.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c4ee3ac3a60f1bf772ae14e6ad7818a087c77a30b92eaf9c8ec9d14de0c0c328`
- Text SHA256: `4ea6be2dab3dafd0300e604f60c95951df53d2c9635b01decfef1f4d29468546`


## Content

---
title: "[Bug Bounty] Email Content Injection"
url: "https://medium.com/@navne3t/bug-bounty-email-content-injection-544196d59e91"
authors: ["Navneet (@na5n33t)"]
bugs: ["Email content injection"]
bounty: "25"
publication_date: "2020-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4717
scraped_via: "browseros"
---

# [Bug Bounty] Email Content Injection

[Bug Bounty] Email Content Injection
Navneet
Follow
2 min read
·
Mar 12, 2020

246

1

This post is about a security bug i have found in a private program. As name suggest it is the injection of content including the link into the email which target website is sending to the user. Read this post to know where and how i found it.

A Picture just for story preview 😅
Functionality/Flow

This website have the shop section where they sell their product. You can visit to the product page and then add that product to your cart or can buy it (as usual in e-commerce websites) but if the product is out-of-stock then there is the button available which says "Notify Me". So , when user click on this button an auto generated email will be sent to his/her email that you have subscribed about this out-of-stock product and you will be notified once it comes back in the stock.

Problem with above functionality

This above mentioned button also have two input fields above it which contains username and email respectively. So when this button clicked it generates POST HTTP Request which have body parameters 'username’,’email' and others. First i try to change this 'email' value to some other email address to check whether there is restriction or not. And successfully able to receive email on different email address. Now , the best part , when the value of username parameter made changed to some content which also contains link , the corresponded email starts with Dear "INJECTED CONTENT.....and also the link" instead of Dear "USERNAME" .

Get Navneet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, I injected the content like "customer, this is important email. blah!blah! do this and Here is the link ...." for the PoC.

Thus, Effective phishing can be done using this security bug/issue.
Reward/Bounty

This was reported to security team and they removed the username parameter to mitigate this.

I was expecting good amount for the bug but they paid/reward with $25 only.

Take Away

if you are doing penetration testing then look at the each HTTP request which generates/send email to the user ,whether it contains some parameter or not which can be used to inject the content in the email.

Thanks! for reading this. Comments and feedback are welcome.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
