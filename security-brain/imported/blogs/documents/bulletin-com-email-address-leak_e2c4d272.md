---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-02_bulletincom-email-address-leak.md
original_filename: 2021-07-02_bulletincom-email-address-leak.md
title: Bulletin.com email address leak
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- graphql
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- graphql
- information-disclosure
language: en
raw_sha256: e2c4d27234b5ec2d4b0b75773ed58879a1bc79f16c17ee3509946764c8a8b5c6
text_sha256: 5a8480aa46e980b0d584c56ab74b2c7724f24f911c80f0f77c7929b2b4444143
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Bulletin.com email address leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-02_bulletincom-email-address-leak.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `e2c4d27234b5ec2d4b0b75773ed58879a1bc79f16c17ee3509946764c8a8b5c6`
- Text SHA256: `5a8480aa46e980b0d584c56ab74b2c7724f24f911c80f0f77c7929b2b4444143`


## Content

---
title: "Bulletin.com email address leak"
page_title: "Bulletin.com email address leak - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/bulletin-com-email-address-leak/"
final_url: "https://philippeharewood.com/bulletin-com-email-address-leak/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "GraphQL"]
bounty: "3,750"
publication_date: "2021-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3530
---

Posted on [July 2, 2021September 22, 2021](https://philippeharewood.com/bulletin-com-email-address-leak/)

# Bulletin.com email address leak

Bulletin.com is Facebook’s new publication service.  
  
The VoiceCreator object in GraphQL has no apparent permissions, this means I can list the subscribers of a podcast/publication by email address.  
`  
query a {bulletin_browse_publications(){__typename,publications{creator{id,name,email_settings{nodes{__typename,...on VoicesEmailSettings{confirmed_email{email_address}}}}}}}}`

**Timeline**

Jul 2, 2021 – Report sent  
Jul 7, 2021 – Fixed by Facebook

Facebook incorrectly penalised me for “exploiting” which was just me retesting the endpoint to see when it was fixed and checking for paid and hidden publications. Retesting bugs is something I’ve done for all my reports. I’ve placed their message below. The warning mentioned was given in another report weeks **after** the “exploit”. I spoke on a Whatsapp call with a security manager at Facebook and we both agreed that they were wrong about the warning date (I asked him for an example) but they still somehow needed to issue the penalty to prove a point and I guess Facebook legal wants to make me _learn_. No one at Facebook ever approached me in the past eight years and said this was a problem. One year ago, I was the keynote speaker for Facebook’s bounty conference and I listed in my slides how I hunt but somehow no one at Facebook can find my contact to discuss this. I haven’t reported any bugs to Facebook since this incident.  
  
**Facebook’s reply**

_Thanks for reporting this issue to us. We would normally issue a $7,500 bounty for your report that described the ability to disclose email addresses of bulletin blog subscribers. That said, we expect our whitehat researchers to adhere to our bug bounty terms of service and to not exploit the issue against other people.~~Because you’ve violated these terms, even though we recently flagged to you these concerns, we’re forced to adjust the bounty as a penalty and call your attention once more to this issue~~._1 _~~  
~~  
In your report, you first demonstrated the issue in your initial PoC. At that time, we notified you the report had been sent to the product team on July 2nd at 2PM GMT. After such a notification, we don’t expect our whitehat researchers to further exploit a vulnerability, unless they have received written consent from Facebook (for example, to demonstrate further impact). However, you sent us two additional correspondences (12 hours after we started investigating your report and 10 hours afterwards) where you further tested the reported issue against additional assets without our consent.  
  
We understand that researchers may inadvertently interact with other user’s data in some situations when doing bug bounty hunting. For example, when other user’s data is accessed by accident. We expect researchers to act in good faith; when a researcher interacts with other user’s data, they should immediately report the vulnerability to us and stop exploiting it further (unless they asked for, and received, written consent from Facebook to continue testing).  
  
Since we had already confirmed the report, exploiting against assets that you don’t own or have consent to test against goes against our bug bounty Terms of Service. As such, we cannot condone such behavior.  
  
We have therefore decided on the following:  
  
1\. We have decided to issue a penalty and halve the bounty amount, thus, and awarding you with a bounty of $3,750. Please consider this decision as our effort to explain to you in good faith what is expected from our researchers. Please note that your future reports that would demonstrate exploiting a vulnerability once the report has already been accepted by Facebook would result in a $0 payout.  
  
2\. We hope this penalty resulting from your policy violation and halving the bounty will be a one-off and that you will continue raising valuable security issues to our bug bounty program, while engaging in good-faith research.  
  
3\. We ask that you please delete all data owned by other users you have gathered in the course of your research including data you have saved in github._

1 The security manager at Facebook told me to ignore this line, so I’ve placed strikethrough for emphasis.
