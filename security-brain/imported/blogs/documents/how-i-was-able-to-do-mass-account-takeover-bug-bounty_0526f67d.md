---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-05_how-i-was-able-to-do-mass-account-takeoverbug-bounty.md
original_filename: 2020-08-05_how-i-was-able-to-do-mass-account-takeoverbug-bounty.md
title: How I was able to do Mass Account Takeover[Bug Bounty]
category: documents
detected_topics:
- command-injection
- password-reset
- mfa
- otp
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- mfa
- otp
- api-security
language: en
raw_sha256: 0526f67d4d7fea0d4e666831c2add3cc788232eb04fbc57981e79913a04190dc
text_sha256: 576a682c9c9c46bd54b48db5610480a0cd909672bfaf7159ae66ffbfb126ac85
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to do Mass Account Takeover[Bug Bounty]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-05_how-i-was-able-to-do-mass-account-takeoverbug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, mfa, otp, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `0526f67d4d7fea0d4e666831c2add3cc788232eb04fbc57981e79913a04190dc`
- Text SHA256: `576a682c9c9c46bd54b48db5610480a0cd909672bfaf7159ae66ffbfb126ac85`


## Content

---
title: "How I was able to do Mass Account Takeover[Bug Bounty]"
url: "https://medium.com/@rikeshbaniyaaa/how-i-was-able-to-do-mass-account-takeover-bug-bounty-b279af1ce62b"
authors: ["Not Rickyy (@RickyyNot)"]
bugs: ["Account takeover", "Password reset"]
publication_date: "2020-08-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4353
scraped_via: "browseros"
---

# How I was able to do Mass Account Takeover[Bug Bounty]

How I was able to do Mass Account Takeover[Bug Bounty]
Rikesh Baniya
Follow
2 min read
·
Aug 5, 2020

192

1

This was one of the interesting bug that i found on a target.

Press enter or click to view image in full size
Photo by Nahel Abdul Hadi on Unsplash

The vulnerability lied in the website’s password reset page.
In order to reset the password an user required two things.(his username and his email)
It was a OTP based password reset mechanism.

There were 3 steps to it.
1.Enter your username and email address
2.Enter the OTP you received
3.Enter the New password

At first i tried to perform response manipulation in Step 2.I entered victims username and email,entered 123456 as the OTP and changed the response from {“success”:”false”} to {“success”:”true”}

The website redirected me to step 3 and i was allowed to enter a new password for victims account.

I entered a new password and pressed Enter.And Guess what???It gave an error message saying ”OTP invalid”.

The website was validating the OTP at the 3rd step also :(

Get Rikesh Baniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I wanted to see what would happen if i entered a valid OTP of attacker.
So I entered it and the password was successfully reset.

Excited with it,i rushed to login with victims email and the new password,but i was not able to login.WHYYY ???Turns out,since i entered attackers otp attackers password got reset instead of victim’s.I was like “WHATTT”.

The request was like this:
{“username”:”victim123" “email”:”victimemail@gmail.com”,”newpass”:”Pass@443",”mfa”:”432521"}

Eventhough the request body had email and username parameter of victim,it was totally useless.So i re-sent the request and it still worked.

So it means there was another bug also.
The OTP was not getting invalidated until a new OTP is requested.Which means i can re-use the same OTP again and again if I donot request a new one

Now,comes the interesting part,Since i realized that an attacker will now not need victims username and email,he can enter his own username and email.All he need to do is enter victims OTP in the 3rd step.

How will attacker get victim’s OTP?
There was no Rate-limit implemented which means he can easily bruteforce it and he will be able to change the password of every-user whose OTP got entered during the bruteforcing process.

Downsides:
-The OTP was expiring in 1 hour.Which means an attacker will only be able to change the password of the victim’s who have requested any OTP during this 1 hour period.
But,He can still change victims password if he has their username and email by requesting a new OTP and bruteforcing it.

Follow me on:
https://twitter.com/RickyyNot
