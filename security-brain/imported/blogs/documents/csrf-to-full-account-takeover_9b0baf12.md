---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-29_csrf-to-full-account-takeover.md
original_filename: 2021-03-29_csrf-to-full-account-takeover.md
title: CSRF to Full Account Takeover
category: documents
detected_topics:
- command-injection
- otp
- csrf
tags:
- imported
- documents
- command-injection
- otp
- csrf
language: en
raw_sha256: 9b0baf1291f24996492472f4b97ba8bafc5d209dbac94d6f7f37291e14fdd581
text_sha256: e438e59f488ec053fbaa5723f425c5d343da89126bc4c5b235e98594861b9fcb
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF to Full Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-29_csrf-to-full-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `9b0baf1291f24996492472f4b97ba8bafc5d209dbac94d6f7f37291e14fdd581`
- Text SHA256: `e438e59f488ec053fbaa5723f425c5d343da89126bc4c5b235e98594861b9fcb`


## Content

---
title: "CSRF to Full Account Takeover"
url: "https://medium.com/@ashrafharb997/csrf-to-full-account-takeover-5196cef9d166"
authors: ["Ashraf Harb (@ashrafharb97)"]
bugs: ["CSRF", "Account takeover"]
publication_date: "2021-03-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3783
scraped_via: "browseros"
---

# CSRF to Full Account Takeover

ِAshraf Harb
 highlighted

Top highlight

CSRF to Full Account Takeover
ِAshraf Harb
Follow
3 min read
·
Mar 29, 2021

298

2

بسم الله الرحمن الرحيم

Hi everyone

I am Ashraf Harb and will be publishing my first Write-up about a CSRF issue that I was able to escalate To Account Takeover

I was testing a private site let’s call it target.com

when submitting any form through the site a parameter called `authenticity_token` is sent in the body as protection against CSRF Attack

Press enter or click to view image in full size

but popular misconfiguration regarding CSRF Tokens is that not being validated on the Server-Side

so let’s try to modify it or even completely delete it from the request

and my doubt was true no validation exist on the CSRF Token and no other measure is used as protection against CSRF and the Content-Type is application/x-www-form-urlencoded so nothing can stop us now from exploiting this as CSRF Attack

but when building CSRF POC let’s build it against function that would give us a Higher Impact for example changing email function as this would lead To Account Takeover

Change Email Function:

when testing CSRF against the change email Function I noticed some difficulties that may fail the attack

Press enter or click to view image in full size

1
User must Enter the Current Password in order to change the email linked to the account

I tried an invalid password in order to make sure parameter value is validated on the server-side and it was validated

another thing to try is to delete the parameter completely from the request and notice the server response and guess what request succeeded 😃

Now let’s move on

Get ِAshraf Harb’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2
Request Header exist as protection against CSRf Attack

Tried to delete it from the Request and it was accepted and email change took effect

Now We have Account Takeover we can change the email of any user once he visited an Html Page that contains the CSRF POC then reset the password using the reset password function
but can we do more?🤔

let’s see

taking a look at the change password function it was the same as change email it requires the user to enter the current password and even if we delete the current password parameter from the request it will succeed

Now We can create an HTML POC to change the Victim Account’s email and password with a single visit to the malicious page

last part

as site didn’t log the user out after changing the password why don’t we add final part in our code to log himout and terminate his active session 😎

HTML Exploit Code
ِAttack workflow:

1 - change the email of the victim account toqotoz+attacker@wearehackerone.com

2 - change the account password to Csrfattack-00

3 - log the user out

Impact:

Full Account Takeover 😃
