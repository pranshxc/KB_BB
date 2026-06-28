---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-05_an-unexpected-bounty-email-bounce-issues.md
original_filename: 2020-02-05_an-unexpected-bounty-email-bounce-issues.md
title: An Unexpected Bounty — Email Bounce Issues
category: documents
detected_topics:
- command-injection
- cloud-security
tags:
- imported
- documents
- command-injection
- cloud-security
language: en
raw_sha256: f1e1fec43aa35d648a7df25c6e16dab5508b72855cdb172e2c481c4a0c821a3d
text_sha256: f00b76397b8c6c40abf2348797bfb0d51e47693c91ca39a41f5c6ffb6315e072
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# An Unexpected Bounty — Email Bounce Issues

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-05_an-unexpected-bounty-email-bounce-issues.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `f1e1fec43aa35d648a7df25c6e16dab5508b72855cdb172e2c481c4a0c821a3d`
- Text SHA256: `f00b76397b8c6c40abf2348797bfb0d51e47693c91ca39a41f5c6ffb6315e072`


## Content

---
title: "An Unexpected Bounty — Email Bounce Issues"
url: "https://medium.com/@keshavaarav22/an-unexpected-bounty-email-bounce-issues-b9f24a35eb68"
authors: ["Keshav Malik (@g0t_rOoT_)"]
bugs: ["DoS", "Email Bounce Issue"]
publication_date: "2020-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4789
scraped_via: "browseros"
---

# An Unexpected Bounty — Email Bounce Issues

An Unexpected Bounty — Email Bounce Issues
Keshav Malik
Follow
2 min read
·
Feb 5, 2020

260

2

Hello Everyone ! Here’s is my write-up regarding a bug that you would have never heard before.

Meanwhile recon, I found that there was a functionality in the Application I was testing on to send invites for family members to use the application. I thought of exploiting this functionality by entering some Invalid Emails !

Okay, So I was successful in sending Email to the Invalid Emails xD Yeah, Sounds crazy right ?

Press enter or click to view image in full size
Photo by Sebastian Herrmann on Unsplash

Afterwards I checked how different companies treat the bounce emails. The biggest marketplace of cloud (Amazon Web Services) with a Email Service known as AWS SES was having a hard bounce rate of 10% (A hard bounce is an email that couldn’t be delivered for some permanent reasons. Maybe the email’s a fake address, maybe the email domain isn’t a real domain, or maybe the email recipient’s server won’t accept emails or simply a mistyped Email) , that means from total of 1000 Emails if 100 of them were fake or were invalid that caused all of them to bounce, AWS SES will block your service.

Get Keshav Malik’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Seems good ? I checked policies of AWS SES (Simple Email Service) related to bounce rates, how this all works. Here’s how AWS SES works whenever a Email is bounced.

Photo by AWS SES

The complete process that was going in a nutshell was, I was able to invite as many family members to use the Web App, but even if I enter a invalid email , invite was sent.

Reported this issue and as it was a bug, The team took some to understand what all was going on, but within a week the bug was Triaged and rewarded with a bounty $$$

Thanks for reading !

Happy Hunting :)
