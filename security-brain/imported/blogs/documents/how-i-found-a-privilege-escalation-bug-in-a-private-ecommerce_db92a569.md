---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-06_how-i-found-a-privilege-escalation-bug-in-a-private-ecommerce.md
original_filename: 2020-01-06_how-i-found-a-privilege-escalation-bug-in-a-private-ecommerce.md
title: How I found a Privilege Escalation Bug in a private Ecommerce?
category: documents
detected_topics:
- csrf
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- csrf
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: db92a569b7ba665b5ba00dc7c8f5d0196fbd9282aa036e152fe56c2214854d28
text_sha256: 20bb2f31eec4c29680bfe4052adbbb80d868e4594033f1e8930e4d0be2966ee4
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I found a Privilege Escalation Bug in a private Ecommerce?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-06_how-i-found-a-privilege-escalation-bug-in-a-private-ecommerce.md
- Source Type: markdown
- Detected Topics: csrf, access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `db92a569b7ba665b5ba00dc7c8f5d0196fbd9282aa036e152fe56c2214854d28`
- Text SHA256: `20bb2f31eec4c29680bfe4052adbbb80d868e4594033f1e8930e4d0be2966ee4`


## Content

---
title: "How I found a Privilege Escalation Bug in a private Ecommerce?"
url: "https://medium.com/nassec-cybersecurity-writeups/an-interesting-story-of-privilege-escalation-1da021e7fd0"
authors: ["Baibhav Anand (@SpongeBhav)"]
bugs: ["Privilege escalation"]
publication_date: "2020-01-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4842
scraped_via: "browseros"
---

# How I found a Privilege Escalation Bug in a private Ecommerce?

How I found a Privilege Escalation Bug in a private Ecommerce?
Baibhav Anand
Follow
2 min read
·
Jan 6, 2020

334

Press enter or click to view image in full size
Image source: https://www.netsparker.com/blog/web-security/privilege-escalation/

This article is based on how I found a Privilege Escalation Bug on an Ecommerce website which allowed me to get full administrator access to the shop.

Let’s assume this Ecommerce site is redacted.com. In redacted.com, an administrator had the authority to add other users as an Admin, or also assign other roles. This article will take you through how I found a privilege escalation bug in redacted.com and was able to get full administrator access to the shop.

First of all, I would like to start with a brief introduction to what a privilege escalation vulnerability is.

Privilege Escalation is a vulnerability where a normal user is able to get an elevated resource which is normally prevented from normal users.

In redacted.com, when the admin added a user in his shop with a non-admin permission, the request appeared as below:

POST /seller/submitEditUser.json HTTP/1.1

Host: vulnerable.vulnerable.com

Connection: close

Content-Length: 63

Accept: application/json, text/javascript

Origin: https://vulnerable.vulnerable.com

X-XSRF-TOKEN:

User-Agent:

Get Baibhav Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Content-Type: application/x-www-form-urlencoded

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Cookie: XXXX

JSID=JSID value; CSRFT=335131365a3ee; JSESSIONID=value; isg=ISGVALUE

role=4&language=670&active=true&userName=xxxx &userId=1010799

Here, the ISG parameter disclosed which shop was on the website, the userID parameter disclosed which user to upgrade, and the role parameter disclosed what role should the user be assigned on the shop. Similarly, the JSID parameter checked if we are part of the shop or not.

I made 3 accounts on the website.

User A — who is the shop administrator.

UserB — who has a non-admin role in the shop.

UserC- Admin of a random shop. (A random account)

Now from user C, I sent the same request but changed the few parameters in the request. I changed the JSID parameter to that of USER B which informed the website that I was a part of that shop. I changed the user-role parameter to 1 which informed the website to upgrade my role to admin. I changed the ISG parameter to match the shop I was upgrading my privilege of. Lastly, I changed the userid parameter to that of User B and sent the request from account C.

Upon doing that User B’s role was upgraded to admin without any admin interaction. And, in this way, I was able to get full administrator access to the shop.

Thank you for reading till the end. If you have any questions DM on twitter at- @SpongeBhav

Editor’s Note — We are publishing write-ups related to cyber security every week. We are looking to grow our community. If you are interested in writing about cyber security, please email at blog@nassec.io.
