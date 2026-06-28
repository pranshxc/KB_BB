---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-21_disable-any-unconfirmed-account-in-facebook.md
original_filename: 2019-11-21_disable-any-unconfirmed-account-in-facebook.md
title: Disable Any Unconfirmed Account in Facebook
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 49f6b8ff71b36c746ec2862420a4dfedfa6ea562177cb93a3a3326076420c4cc
text_sha256: 2d815021619830cff98018509448fa2aa96c566577f7c8825761cb6469d86c5d
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Disable Any Unconfirmed Account in Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-21_disable-any-unconfirmed-account-in-facebook.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `49f6b8ff71b36c746ec2862420a4dfedfa6ea562177cb93a3a3326076420c4cc`
- Text SHA256: `2d815021619830cff98018509448fa2aa96c566577f7c8825761cb6469d86c5d`


## Content

---
title: "Disable Any Unconfirmed Account in Facebook"
url: "https://medium.com/@lokeshdlk77/disable-any-unconfirmed-account-in-facebook-123aeba19426"
authors: ["Lokesh Kumar (@lokeshdlk77)"]
programs: ["Meta / Facebook"]
bugs: ["Bruteforce"]
bounty: "1,000"
publication_date: "2019-11-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4924
scraped_via: "browseros"
---

# Disable Any Unconfirmed Account in Facebook

Disable Any Unconfirmed Account in Facebook
Lokesh Kumar
Follow
2 min read
·
Nov 21, 2019

312

1

This post is about an bug that I found on Facebook which used to Disable any new unconfirmed account in Facebook by using IP Rotation brute force attack. this post is bypass of this write-up → pagefault.me

Press enter or click to view image in full size

In Facebook if a user Sign-up a new account. 5 digit Verification code will be send to that corresponding email. but for security reasons victim has a option to disable that Verification code.because attacker can also try to create a new account on behalf victims email.

Vulnerable Endpoint:

https://m.facebook.com/confirmemail.php?e=victim@mail.com@&c=15579&report=1&message=1

But the Rate limit was implemented in this Endpoint. after some certain attempts of brute forcing the 5 digit verification code i got Temporary blocked

Press enter or click to view image in full size

In previous write-up pagefault.me the fix was made in 2014. so i guessed the fix would be in IP Based Blocking. so i change my IP address and made the request again . as expected no blocking occurred in new IP address.

But to make the attack easier i need to rotate my IP address for each request in brute force attack. so i search in google for a solution and came to know about IP Rotation Services to bypass IP Blocking. I have made separate write-up on How to Rotate IP ADDRESS in Brute Force Attack

Get Lokesh Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After configuring IP rotation Services. i can able to brute force the 5 digit Verification code without getting blocked.

Press enter or click to view image in full size

Video POC:

Impacts:

If the victims email got disabled he cannot create new Facebook account in future. because the email will get blacklisted on Facebook account creation.
If attacker know the unconfirmed email. he can brute force the code and disable that account without owners interaction.

Timeline:

30-June-2019 : Report Sent

03-July-2019 : Further investigation by Facebook

23-Aug-2019: Fixed confirmed by Facebook and me

23-Aug-2019 : $1000 bounty awarded by Facebook
