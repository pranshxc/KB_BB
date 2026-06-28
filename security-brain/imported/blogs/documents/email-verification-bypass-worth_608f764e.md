---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-03_email-verification-bypass-worth-.md
original_filename: 2023-03-03_email-verification-bypass-worth-.md
title: Email Verification Bypass Worth $$$
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- otp
- rate-limit
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- otp
- rate-limit
language: en
raw_sha256: 608f764e5cbcfb3a5c3768a157fe0d391ea50e1963be4716548bcae3f0449b98
text_sha256: 007e806ef0e3ce4e30f596ffe6598a05e9ab354dd86e1f4cdc5978f5c7f5199f
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Email Verification Bypass Worth $$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-03_email-verification-bypass-worth-.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, otp, rate-limit
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `608f764e5cbcfb3a5c3768a157fe0d391ea50e1963be4716548bcae3f0449b98`
- Text SHA256: `007e806ef0e3ce4e30f596ffe6598a05e9ab354dd86e1f4cdc5978f5c7f5199f`


## Content

---
title: "Email Verification Bypass Worth $$$"
url: "https://vijetareigns.medium.com/email-verification-bypass-worth-cbb65a68a34f"
authors: ["the_unluck_guy (@7he_unlucky_guy)"]
bugs: ["Email verification bypass"]
publication_date: "2023-03-03"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1441
scraped_via: "browseros"
---

# Email Verification Bypass Worth $$$

Email Verification Bypass Worth $$$
the_unlucky_guy
Follow
2 min read
·
Mar 3, 2023

550

3

Hello Geeks, Hope you guys are hacking well. In this blog i am going to share a small story of bypassing email verification. I am not allowed to share the organization name so I will be using redacted.com as the main domain.

*.redacted.com is in scope. As usual, I started with subdomain enumeration, for subdomain enumeration I mostly use combination of subfinder +findomain+amass. After enumerating domains i only found 3 live domains in which one is the main application and other two is having static pages. I picked init.redacted.com and used crt.sh to find more subdomains and found a subdomain swf-apps.init.redacted.com.

There is a registration page at swf-apps.init.redacted.com where you can create account.

Press enter or click to view image in full size

After creating an account, the user will receive an email with a verification link. Users have to verify their email to login into their accounts. The verification link looks like https://swf-apps.init.redacted.com/capabilities/Account/emailverification.aspx?e=token&n=1x0

Press enter or click to view image in full size

I decode the value of e and found that the token is base64 encoded of email. https://swf-apps.init.redacted.com/capabilities/Account/emailverification.aspx?e=user_email_base64_encode&n=1x0
I was like.

So I registered a new account using a random email like admin@redacted.com as I don’t have access to admin@redacted.com email. To get logged in successfully I have to verify my email. So, I crafted an email verification link and used it to verify it. That was it.

Get the_unlucky_guy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To show the impact I used company email address.

Timeline:

March 22, 2021— Reported

March 22, 2021 — Triaged and $$$ Bounty awarded

September 28, 2021 — Fixed.

Thanks for reading, hope you learned something new. Do clap and share if you like. I will write more of my findings soon so, stay tuned for my next write-up.

Twitter: 7he_unlucky_guy
Linkedin: Vijeta
