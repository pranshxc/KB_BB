---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-20_internshala-bug-in-internshala-student-partner.md
original_filename: 2018-01-20_internshala-bug-in-internshala-student-partner.md
title: Internshala Bug in Internshala Student Partner
category: documents
detected_topics:
- rate-limit
- command-injection
tags:
- imported
- documents
- rate-limit
- command-injection
language: en
raw_sha256: c20ad7681c91811fab2cde2199cde699a7c2418f827b7cb69b5124e02e7532af
text_sha256: 1d49b72f225930b8244bb321af90161ecb2be9e6ef00b52ac566323eaae86167
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Internshala Bug in Internshala Student Partner

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-20_internshala-bug-in-internshala-student-partner.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `c20ad7681c91811fab2cde2199cde699a7c2418f827b7cb69b5124e02e7532af`
- Text SHA256: `1d49b72f225930b8244bb321af90161ecb2be9e6ef00b52ac566323eaae86167`


## Content

---
title: "Internshala Bug in Internshala Student Partner"
url: "https://medium.com/@circleninja/internshala-bug-in-internshala-student-partner-33d7b66c1bd5"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Internshala"]
bugs: ["Bruteforce"]
publication_date: "2018-01-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6003
scraped_via: "browseros"
---

# Internshala Bug in Internshala Student Partner

Internshala Bug in Internshala Student Partner
Ronnie Joseph
Follow
2 min read
·
Jan 20, 2018

135

1

Hi I am back again.

This is a quick writeup while my video is being uploaded to youtube.

I found that that there is no proper rate limiting set during isp login from herehttps://trainings.internshala.com/isp/login.

Hackers can run automated bruteforce tool like burp suite intruder to find the passwords. The isp login can be easily found when a student partner shares his referral link . The correct password can be found out through by seeing the length of the response which will be the least. (The passwords consist of small alphabets and numbers.)

The best fix was to atleast introduce a captcha and then also throttle out the IP account having multiple failed logins.

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Unfortunately they said that they are already aware of the issue and closed my report .

PS- I found out that Internshala responsible disclosure is a pain in ass to work with and they are replying after a long delay. I also reported bugs like they had old wordpress version running on their blog. Unfortunately the bug got rejected but they silently fixed the endpoint from where I reached it.

Like- https://example/wp-admin was available when i started my pentest. After my report where I said it is visible and then reported a chained bug; it got closed but the url link got removed . So sad :(

I hope for good luck with them in future.

I will be writing my Google and MS HOF sometime soon ! BYE!

UPDATE- THEY ARE NOW WILLING TO GIVE A T-SHIRT AND TAKE THIS AS AN EXCEPTIONAL CASE FOR ANOTHER OF MY REPORTS.

MY REPLY-

Press enter or click to view image in full size
