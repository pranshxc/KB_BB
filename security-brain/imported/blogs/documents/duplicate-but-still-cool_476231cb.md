---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-05_duplicate-but-still-cool.md
original_filename: 2018-11-05_duplicate-but-still-cool.md
title: Duplicate but still cool
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- rate-limit
- csrf
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- rate-limit
- csrf
language: en
raw_sha256: 476231cb67ff7a239530dbd2671128fa6a254ff256a8001bd373d25c7ac36023
text_sha256: d81d8f5ee002677ebcfd45a8148c14e02699f696e446951f6ffabd9693e12897
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Duplicate but still cool

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-05_duplicate-but-still-cool.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, rate-limit, csrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `476231cb67ff7a239530dbd2671128fa6a254ff256a8001bd373d25c7ac36023`
- Text SHA256: `d81d8f5ee002677ebcfd45a8148c14e02699f696e446951f6ffabd9693e12897`


## Content

---
title: "Duplicate but still cool"
page_title: "DUPLICATE BUT STILL COOL. TL;DR, From low impact to account… | by Plenum | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/duplicate-but-still-cool-236835685075"
authors: ["Plenum (@plenumlab)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2018-11-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5607
scraped_via: "browseros"
---

# Duplicate but still cool

DUPLICATE BUT STILL COOL
Plenum
Follow
2 min read
·
Nov 5, 2018

113

3

TL;DR, From low impact to account takeover to duplicate here is the story of a cool bug i found on a private program at 
HackerOne
.

Get Plenum’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The company redacted.com provided CRM services to users, a user can signup as an organization then invite team members with either admin role or basic user role. The invitation process seemed ok at first everything was being checked perfectly the invitation link had 32 bytes alphanumeric token (NO WAY OF BRUTEFORCING THAT), csrf token checked properly it was all good until i found the first bug

IDOR on resend invitation

An admin has the ability to view pending invitation and he could also resend invitations, it seems fine the post request was as follows

POST /invitations/363484/resend HTTP/1.1
Host: bugbounty.redacted.com
Authorization: Bearer base64 token

The JSON response contained the email {“status”:”success”,”email”:”email@example.com”}

The problem was if you change the invitation id you could actually see sent invitations by other companies registered to redacted.com. After creating multiple invites i noticed that the invitation id increments, this also confirmed that there no need to brute force simply use intruder and increment/decrement the id to disclose invited emails of other companies.
This by itself is not that important because we cant see any important information in the response except the email.

Chaining the first bug with a design flaw

Now The real fun started, i grabbed the email reflected in the response, then went on to register an account on redacted.com.
After sign up i got redirected to an html page where it said

Company X has invited you to join them, please use the link in the e-mail.
Click on resend invitation to receive the email again

Copied the resend invitation link on that page it looked something like

https://www.redacted.com/resend_invitation/TOKEN

Went over to check my email it had the same link except that instead of resend_invitation they used join so the link was like

https://www.redacted.com/join/TOKEN

So i went back to the tab replaced resend_invitation with join and boom! i got in. An attacker could takeover arbitrary accounts with this vulnerability simply by leveraging the first IDOR, and signup every email that gets reflected back in the json respone.

This was a duplicate report but it was a cool one.
To the original reporter if you are reading this then well done ;)

Till next time,
Happy hunting everyone,

Plenum
