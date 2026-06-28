---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-24_how-i-acquired-xxx-bounty-by-investing-99-cents.md
original_filename: 2019-05-24_how-i-acquired-xxx-bounty-by-investing-99-cents.md
title: How I acquired $XXX bounty by investing 99 cents
category: documents
detected_topics:
- command-injection
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- business-logic
- mobile-security
language: en
raw_sha256: 23fe4ee5cfff027613bda3618b14befb0860564afa78bfe4feb89bd9b7a22c1f
text_sha256: e186827de7128bd6aa09b34c29670db7342d31b2c490010ece80a774c46eab2c
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I acquired $XXX bounty by investing 99 cents

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-24_how-i-acquired-xxx-bounty-by-investing-99-cents.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `23fe4ee5cfff027613bda3618b14befb0860564afa78bfe4feb89bd9b7a22c1f`
- Text SHA256: `e186827de7128bd6aa09b34c29670db7342d31b2c490010ece80a774c46eab2c`


## Content

---
title: "How I acquired $XXX bounty by investing 99 cents"
page_title: "How I acquired $XXX bounty by investing 99 cents – Smaran Chand"
url: "https://smaranchand.com.np/2019/05/how-i-acquired-xxx-bounty-by-investing-99-cents/"
final_url: "https://smaranchand.com.np/2019/05/how-i-acquired-xxx-bounty-by-investing-99-cents/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["Logic flaw"]
publication_date: "2019-05-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5248
---

[May 24, 2019](https://smaranchand.com.np/2019/05/how-i-acquired-xxx-bounty-by-investing-99-cents/)

# How I acquired $XXX bounty by investing 99 cents

I still remember that exhausting day full of failures which are common for bug bounty hunters whenever you don’t find issues in the application.

It was one of the public programs in bugcrowd with the mobile app, API and some domains in the scope. I had P1 duplicate on the same program. 🙁 I spent around 6 hrs to look for the issues in the web scope of a program and then I got to know that I am not being able to find any issues.

I decided to look for a parameter pollution issue at purchase endpoint because it was only missing thing. Hopefully i ended with disappointment. 😂

The scope program had the functionality to purchase digital stuff, So I planned to spend $0.99 USD on purchasing it.

And later on, I got to know that the payment receipt/invoice was sent to the old email address or the email address used to signup for the first time.

I already had changed my email address after signup while trying for account takeover/verification bypass issue.

I reported this issue with a good explanation, although they took long to verify and triage the issue.

![](https://smaranchand.com.np/wp-content/uploads/2019/05/reply-700x129.png)Let’s talk about $$$

Although they made me wait for more than 2 weeks but rewarded me satisfactory bounty amount for this issue. 🙂

![](https://smaranchand.com.np/wp-content/uploads/2019/05/bounty.png)This was beautiful

Yes, of course, it was a low hanging fruit which didn’t require any special method for exploitation but was little out of the common reach.

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/)
