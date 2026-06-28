---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-20_race-condition-bypassing-team-limit.md
original_filename: 2017-07-20_race-condition-bypassing-team-limit.md
title: Race Condition bypassing team limit
category: documents
detected_topics:
- command-injection
- otp
- race-condition
tags:
- imported
- documents
- command-injection
- otp
- race-condition
language: en
raw_sha256: 9df620c51fa8684338dabcf7c38d9285718ab6d55e1e115e7f84d691ea03f2ad
text_sha256: 0842c097dc4f9deeb0b7a01013f07510f46093bd2f88fd98af94fa940dda9cc5
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Race Condition bypassing team limit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-20_race-condition-bypassing-team-limit.md
- Source Type: markdown
- Detected Topics: command-injection, otp, race-condition
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9df620c51fa8684338dabcf7c38d9285718ab6d55e1e115e7f84d691ea03f2ad`
- Text SHA256: `0842c097dc4f9deeb0b7a01013f07510f46093bd2f88fd98af94fa940dda9cc5`


## Content

---
title: "Race Condition bypassing team limit"
url: "https://medium.com/@arbazhussain/race-condition-bypassing-team-limit-b162e777ca3b"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["Race condition"]
publication_date: "2017-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6146
scraped_via: "browseros"
---

# Race Condition bypassing team limit

Race Condition bypassing team limit
Arbaz Hussain
Follow
1 min read
·
Jul 20, 2017

159

1

Severity: Medium

Complexity: Easy

Weakness: Race condition

While testing one of the application, they have functionality to create team and invite user’s to team .
they have free limit of inviting 5 user’s to team.If you want to invite more user’s , they will ask you to upgrade you’r plan to pro.
Request while adding member to our team.
Request:

POST /account/work/team/ HTTP/1.1
Host: www.site.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: application/json, text/javascript, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Referer: https://www.site.com/home/work/team/manage
Content-Length: 108
Cookie: <REDACTED>
Connection: close

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

emails=xxxxxxx@gmail.com&team=name&authenticity_token=<>

Sending the Request to Burp Intruder By Adding Email List to emails= Parameter.
Setting Minimum Thread Speed(10–15) and Start Attack.
Result:
Press enter or click to view image in full size
Bypassed the limit to 22
Increasing Threading to ~10 will send 10 request’s at the same time. this will generate a type confusion which bypassed their team limit.
