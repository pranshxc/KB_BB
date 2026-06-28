---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-17_facebook-sms-captcha-was-vulnerable-to-csrf-attack.md
original_filename: 2022-10-17_facebook-sms-captcha-was-vulnerable-to-csrf-attack.md
title: Facebook SMS Captcha Was Vulnerable to CSRF Attack
category: documents
detected_topics:
- otp
- command-injection
- graphql
- csrf
tags:
- imported
- documents
- otp
- command-injection
- graphql
- csrf
language: en
raw_sha256: d1f6c7a6a89220e655781e84e9ab86035d0222fab4ad8990c7cac14bc1132d2f
text_sha256: f96a2ef7e2e7eb027d044324b916c6601c6edce3b070989fa1a258a555424ac0
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook SMS Captcha Was Vulnerable to CSRF Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-17_facebook-sms-captcha-was-vulnerable-to-csrf-attack.md
- Source Type: markdown
- Detected Topics: otp, command-injection, graphql, csrf
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `d1f6c7a6a89220e655781e84e9ab86035d0222fab4ad8990c7cac14bc1132d2f`
- Text SHA256: `f96a2ef7e2e7eb027d044324b916c6601c6edce3b070989fa1a258a555424ac0`


## Content

---
title: "Facebook SMS Captcha Was Vulnerable to CSRF Attack"
url: "https://lokeshdlk77.medium.com/facebook-sms-captcha-was-vulnerable-to-csrf-attack-8db537b1e980"
authors: ["Lokesh Kumar (@lokeshdlk77)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "18,750"
publication_date: "2022-10-17"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2034
scraped_via: "browseros"
---

# Facebook SMS Captcha Was Vulnerable to CSRF Attack

Facebook SMS Captcha Was Vulnerable to CSRF Attack
Lokesh Kumar
Follow
2 min read
·
Oct 17, 2022

646

1

This post is about an bug that I found on Meta (aka Facebook) which allows to make any Endpoint as POST request in SMS Captcha flow which leads to CSRF attack.

After reporting Contact Point Deanonymization Bug I started to find any way to bypass it in Account recover flow. but when sending multiple OTP code request I got hit with SMS captcha flow.

Vulnerable Endpoint:

https://m.facebook.com/sms/captcha/?next=/path

when digging deeper in captcha page I found that next= parameter is vulnerable to CSRF attack. because the Endpoint doesn't have any CSRF protection and the give action URL is sending as post request with fb_dtsg CSRF token

Press enter or click to view image in full size

So attacker can append any sensitive graphql endpoint.

Example:

Create | Update |Deleting ( Feeds, Stories)
Adding or Removing (Email address , Mobile number)
modifying any sensitive changes in /setting , etc…

If victim click the Continue button the POST request will be send with CSRF Token. So the action URL will get executed successfully.

Get Lokesh Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Fix:

Meta fixed this Vulnerability by adding next_mac=**** CSRF Protection and allows only OTP Code sending Endpoint in SMS Captcha form Action URL

Video POC:

https://youtu.be/JcCPjL4aycI

Timeline:

16-jan-2022: Report Sent

17-Jan-2022: Further investigation by Meta

16-Feb-2022: Fixed confirmed by Meta and me

11-Mar-2022: $18750 bounty awarded by Facebook (With Hacker plus & Timing Bonus)

Thank you Meta Team for quick Triaging and fixing this Vulnerability

Press enter or click to view image in full size
