---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-26_an-effective-5-min-recon-leads-to-a-hall-of-fame.md
original_filename: 2021-10-26_an-effective-5-min-recon-leads-to-a-hall-of-fame.md
title: An Effective 5 min recon leads to a Hall of Fame
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
raw_sha256: c8dfdd0d3f888d86aeec7dba19a97f2661fc516d2d10053320f7ef7b04aa4b7b
text_sha256: 7b5b0baecc203edb8e5a9fee05b6a4f0ea3eba1261893cf58c242f1b2de14364
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# An Effective 5 min recon leads to a Hall of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-26_an-effective-5-min-recon-leads-to-a-hall-of-fame.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `c8dfdd0d3f888d86aeec7dba19a97f2661fc516d2d10053320f7ef7b04aa4b7b`
- Text SHA256: `7b5b0baecc203edb8e5a9fee05b6a4f0ea3eba1261893cf58c242f1b2de14364`


## Content

---
title: "An Effective 5 min recon leads to a Hall of Fame"
url: "https://renganathanofficial.medium.com/an-effective-5-min-recon-leads-to-a-hall-of-fame-ae7f20e5cf1a"
authors: ["Renganathan (@IamRenganathan)"]
bugs: ["Information disclosure"]
publication_date: "2021-10-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3215
scraped_via: "browseros"
---

# An Effective 5 min recon leads to a Hall of Fame

An Effective 5 min recon leads to a Hall of Fame
Renganathan
Follow
2 min read
·
Oct 26, 2021

442

2

Hi There,

Renganathan Here, I’m an Ethical Hacker & a Security researcher.

I’ve been acknowledged by LinkedIn, United Nations, BYJU’s, Nike, Lenovo, Upstox for reporting security vulnerabilities in their web applications.

So I came back to bug bounties after almost 2 months. I had exams after the IRCTC bug.

Let’s call it target.com, They offer a Hall of fame based on criticality.

I started with a shodan dork. I have a premium account of shodan.io that they gave free to their users for one day last year :P

ssl:target “200 ok”

I found some FortiClient VPN login pages

Get Renganathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So without wasting any time I went to GitHub and used the below dork

“target” “username” “password”

Soon on top of the result, I found a repo containing the below data ^_^

Press enter or click to view image in full size

Then I googled the name of the repo owner and came to know that it was a Software developer working at Target.com

I logged in using those FortiClient Credentials

Press enter or click to view image in full size

And yeah, the rest is history :D

I reported this to them and It was patched soon and got listed in their hall of fame.

Thanks for reading :)
Stay Safe.

https://www.instagram.com/renganathanofficial

https://twitter.com/IamRenganathan
