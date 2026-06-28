---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-10_account-of-the-ceo-takeover-via-password-reset.md
original_filename: 2023-07-10_account-of-the-ceo-takeover-via-password-reset.md
title: Account (of the CEO) Takeover via Password Reset
category: documents
detected_topics:
- password-reset
- automation-abuse
- idor
- command-injection
- api-security
tags:
- imported
- documents
- password-reset
- automation-abuse
- idor
- command-injection
- api-security
language: en
raw_sha256: a4b855a5698237d43c4120284564269d1827875103f699b4c1d078eec74f3801
text_sha256: e3279adbf7df50848400b8b58b112ccf5dd6e311ba1e1b929f162ddd2765494b
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: true
---

# Account (of the CEO) Takeover via Password Reset

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-10_account-of-the-ceo-takeover-via-password-reset.md
- Source Type: markdown
- Detected Topics: password-reset, automation-abuse, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: True
- Raw SHA256: `a4b855a5698237d43c4120284564269d1827875103f699b4c1d078eec74f3801`
- Text SHA256: `e3279adbf7df50848400b8b58b112ccf5dd6e311ba1e1b929f162ddd2765494b`


## Content

---
title: "Account (of the CEO) Takeover via Password Reset"
url: "https://cristivlad.medium.com/account-of-the-ceo-takeover-via-password-reset-7e55c0175425"
authors: ["Cristi Vlad (@CristiVlad25)"]
bugs: ["Account takeover", "Password reset", "IDOR"]
publication_date: "2023-07-10"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 950
scraped_via: "browseros"
---

# Account (of the CEO) Takeover via Password Reset

Account (of the CEO) Takeover via Password Reset
Cristi Vlad
Follow
3 min read
·
Jul 10, 2023

703

1

Press enter or click to view image in full size

In a web app pentest for a client, I found this interesting account takeover and I thought of sharing my findings with the infosec community.

Usually, in apps involving authentication, I extensively test all the related functionalities. When I got to the “Forgot Password” feature, I wanted to observe how the entire flow goes.

You’ve probably seen this millions of times:

Click on “Forgot Password” ⇒ Enter Email ⇒ Submit ⇒ Check your email.

In this case, I immediately received an email with a password reset link, which looked something like this:

https://email.mail.redactedexample.com/c/verylongENCRYPTEDstring

And here’s what seemed interesting to me. After clicking on the link, I was redirected to:

https://redactedexample.com/someendpoint/confirm.php?u=551234911&t=<132bitUnknownHashType>&x=2913117

You probably already know what this meant. And in my mind:

No way, what if I….? It couldn’t be that simple, right? Probably not, but let me just try it and confirm that the entire process is safe…

The page looked like this:

Your email is <myemail>

Create new password=***REDACTED***
Confirm password=***REDACTED***
<Submit button>

The first thing I did was remove the “x” parameter and refresh the page to see if it made any difference. It didn’t!

Great! Now for the moment of truth, let me increment the value of “u” (+1) because it looks like a numerical ID. Great, hit enter.

Get Cristi Vlad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Lo’ and behold:

Your email is <anotheruser'semail>

Create new password=***REDACTED***
Confirm password=***REDACTED***
<Submit button>

Even at this point, I was still unsure if it would work, so I created another account (myaccount2) in a different browser session. The ID was exposed in the Account Settings section. I copied the exposed ID and pasted it into the URL:

https://redactedexample.com/someendpoint/confirm.php?u=myaccount2ID&t=<132bitUnknownHashType>

I created and confirmed a new password, hit Submit, and I was immediately logged into myaccount2’s account.

Afterthoughts

I’ve seen similar situations in the past, therefore this is not an extraordinary or uncommon case. It’s just another case of password reset gone wrong.

At the point of receiving the reset link in the email:

https://email.mail.redactedexample.com/c/verylongENCRYPTEDstring

They (devs) probably thought the link was safe. The string was not encoded, but encrypted.

But what’s the point of encryption if you’re handing over control of URL parameters to the end user at the next step?! Bad logic, in my opinion.

To take it a step even further, I played with the numerical ID and decremented it up to the point of finding the account of the CEO. If my account was (supposedly) 551234911, CEO’s account wasn’t 1 or 000000001, but somewhere at 551003010.

Also, I noticed that the point of the “x” parameter was to invalidate the reset link after some time. Removing it (“x”) also removed the entire logic, thus allowing me to use/abuse the reset URL days later.

The bottom line:

For the red guys and gals: always look closer and focus on manual testing. Tools and automation will never get you in front of this type of vulnerability.

As for the blue guys and gals: implement solid logic and don’t give more permissions than necessary to the end user.
