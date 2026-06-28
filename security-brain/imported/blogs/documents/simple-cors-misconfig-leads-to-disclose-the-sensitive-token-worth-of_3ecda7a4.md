---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-16_simple-cors-misconfig-leads-to-disclose-the-sensitive-token-worth-of-.md
original_filename: 2022-12-16_simple-cors-misconfig-leads-to-disclose-the-sensitive-token-worth-of-.md
title: Simple CORS misconfig leads to disclose the sensitive token worth of $$$
category: documents
detected_topics:
- cors
- command-injection
- otp
- api-security
tags:
- imported
- documents
- cors
- command-injection
- otp
- api-security
language: en
raw_sha256: 3ecda7a49487e587dc9883dbfee39141e7763ac60c476b537caacc397a34cdcb
text_sha256: 6625710eca29171a7ff95accc0709840e1872f338699dda880ea6716376b2a5b
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Simple CORS misconfig leads to disclose the sensitive token worth of $$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-16_simple-cors-misconfig-leads-to-disclose-the-sensitive-token-worth-of-.md
- Source Type: markdown
- Detected Topics: cors, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `3ecda7a49487e587dc9883dbfee39141e7763ac60c476b537caacc397a34cdcb`
- Text SHA256: `6625710eca29171a7ff95accc0709840e1872f338699dda880ea6716376b2a5b`


## Content

---
title: "Simple CORS misconfig leads to disclose the sensitive token worth of $$$"
url: "https://0xraminfosec.medium.com/simple-cors-misconfig-leads-to-disclose-the-sensitive-token-worth-of-91433763f4d6"
authors: ["Ramalingasamy"]
programs: ["Linear"]
bugs: ["CORS misconfiguration", "Token leak"]
publication_date: "2022-12-16"
added_date: "2022-12-20"
source: "pentester.land/writeups.json"
original_index: 1769
scraped_via: "browseros"
---

# Simple CORS misconfig leads to disclose the sensitive token worth of $$$

Simple CORS misconfig leads to disclose the sensitive token worth of $$$
Ramalingasamy
Follow
2 min read
·
Dec 17, 2022

213

1

Hey fellow hacker’s and Bug hunters , Recently i found some weird CORS misconfiguration in one of my targets.

If you don’t know what is CORS then learn from here.

Let’s assume the target as target.com . I started to extract the subdomains of target and saved it as target_subdomains.txt and extracted waybackurls for all the subdomains.

cat target_subdomains.txt | waybackurls >> target_waybackurls.txt

The waybackurls file has huge number of urls count of 10 lakh+ lines.

I started to search for sensitive words like token,password,amount etc… After 1–2 hours of searching , I’ve found one api endpoint which looks like

https://www-api.target.com/api/user/info/email

This api endpoint leaks the token which is used to authenticate a user for many api endpoints.this api response has two headers as

Access-Control-Allow-Origin: https://target.com
Access-Control-Allow-Credentials: true

I changed the Origin header in request as http://mysite.com but the response didn’t allowed that mysite.com and again i gave the origin as mysite.target.com now the target allowed this origin.

Get Ramalingasamy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, After this i simply gave the Origin as mysitetarget.com .Surprisingly it allowed this origin . i was like WTH!!!!

Now i can able to steal any user’s token from mysitetarget.com origin .I only need to buy the mysitetarget.com .

— — — — — — — — — — — — — — — — — — END — — — — — — — — — — — — — — — — —

Follow me for more bug hunting writeup’s

Follow me on Instagram : https://www.instagram.com/ram_0x_infosec/

Follow me on Twitter : https://twitter.com/Ram00733925

Connect with me on Linkedin : https://www.linkedin.com/in/ram0xinfosec/
