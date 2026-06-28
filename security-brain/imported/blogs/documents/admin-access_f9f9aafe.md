---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-19_admin-access-.md
original_filename: 2021-09-19_admin-access-.md
title: Admin access !!
category: documents
detected_topics:
- access-control
- jwt
- idor
- xss
- command-injection
- password-reset
tags:
- imported
- documents
- access-control
- jwt
- idor
- xss
- command-injection
- password-reset
language: en
raw_sha256: f9f9aafe3d659f9fe4ccbe74d4ab39c358cc10a97d568db4a4095d348a6880b6
text_sha256: 8855e4248f87248552f662587410256f08df435821b6bad5b987a09fa3abab9e
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Admin access !!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-19_admin-access-.md
- Source Type: markdown
- Detected Topics: access-control, jwt, idor, xss, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `f9f9aafe3d659f9fe4ccbe74d4ab39c358cc10a97d568db4a4095d348a6880b6`
- Text SHA256: `8855e4248f87248552f662587410256f08df435821b6bad5b987a09fa3abab9e`


## Content

---
title: "Admin access !!"
url: "https://dewangpanchal98.medium.com/admin-access-799b50694965"
authors: ["th3.d1p4k (@DipakPanchal05)"]
bugs: ["Privilege escalation", "Broken Access Control"]
publication_date: "2021-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3303
scraped_via: "browseros"
---

# Admin access !!

Admin access !!
th3.d1p4k
Follow
3 min read
·
Sep 18, 2021

300

1

Hellow folks! I hope you’re well! In this writeup I’ll tell you how I become low privilege user to an Admin. So without further delay let’s get started.

I was hunting on private program of Bugcrowd. That company was providing Cloud Security, Network Security, etc. (Related to Cyber Security). I started doing recon and I tested 2–3 domains and I found nothing. I moved on another subdomain. That subdomain was type of ecommerce. We can purchase Softwares and so on. I was testing on sign in page functionality. There was validation while creating an account.

Press enter or click to view image in full size
JS Validation

So I typed something@example.com and intercept request while click on submit button. I changed example.com to gmail.com and forwarded the request. And I logged In, there was no email verification too.

Get th3.d1p4k’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I started playing with Burp History. I got sub.redacted.com/api/users. I send it to repeater click on go and got 401 Unauthorized. I checked other requests and I got that Authorization header is missing.

Press enter or click to view image in full size
Something is missing…

I copied Authorization header with value(JWT). And I got All users and bug hunter’s information who is also testing same website even admins too. Now I can see their Name, Email, ID, Is admin or not(JSON format). Interesting…

Press enter or click to view image in full size

I again login to website intercept request in check it’s response. In response admin param caught my attention. The param was like IsAdmin:false. I changed it to true and forward the request and turn off intercept. Now I’m admin. I tried finding another bugs which can perform by as admin. But there was nothing too test. No IDOR, XSS, CSRF, etc.

Press enter or click to view image in full size

I tried to play with JWT. I decode it. There were some values like email, ID, and IsAdmin? As you know I got All user’s Information I picked first admin’s details and replaced with my values and create JWT. Now again I logged In with another email and intercept request and check response and I replaced my JWT which created and paste it and forward the request. It works! So, I can perform admin access response manipulation and JWT attack. That’s it. Keep hunting. Keep sharing !!

Press enter or click to view image in full size
I have Admin power

Instagram: th3.d1p4k

Twitter: Dipak Panchal
