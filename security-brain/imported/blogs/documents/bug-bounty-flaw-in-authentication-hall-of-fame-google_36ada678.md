---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-21_bug-bounty-flaw-in-authentication-hall-of-fame-google-.md
original_filename: 2019-10-21_bug-bounty-flaw-in-authentication-hall-of-fame-google-.md
title: '[ BUG BOUNTY ] Flaw in Authentication ( Hall of Fame Google )'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 36ada678b14eb034bb7699bd878d456ca380ce179853d5ae62ed8f0c6160fd03
text_sha256: 7f93ea6f2d6098f0f0b341b8c9937a2eafd406730cc22943a73dde365403c74f
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# [ BUG BOUNTY ] Flaw in Authentication ( Hall of Fame Google )

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-21_bug-bounty-flaw-in-authentication-hall-of-fame-google-.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `36ada678b14eb034bb7699bd878d456ca380ce179853d5ae62ed8f0c6160fd03`
- Text SHA256: `7f93ea6f2d6098f0f0b341b8c9937a2eafd406730cc22943a73dde365403c74f`


## Content

---
title: "[ BUG BOUNTY ] Flaw in Authentication ( Hall of Fame Google )"
url: "https://medium.com/@danangtriatmaja/bug-bounty-flaw-in-authentication-get-hall-of-fame-google-6196726ee5b9"
authors: ["Danang Tri Atmaja (@danangtriatmj)"]
programs: ["Google"]
bugs: ["Broken authentication"]
publication_date: "2019-10-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4979
scraped_via: "browseros"
---

# [ BUG BOUNTY ] Flaw in Authentication ( Hall of Fame Google )

[ BUG BOUNTY ] Flaw in Authentication ( Hall of Fame Google )
Danang Tri Atmaja
Follow
3 min read
·
Oct 21, 2019

242

3

بسم الله الرحمن الرحيم

(This is a Simple POC).

Press enter or click to view image in full size

So the story is long. First I want to say Alhamdulillah until today. :)

I was begin intend to gather information … recon, recon and recon at the stage of searching for subdomains and their directory.

Tools:

Sub-domain search:

1. Knockpy — https://medium.com/hacker-toolbelt/knokpy-5c6745e53770
2. Sublist3r — https://github.com/aboul3la/Sublist3r

Directory search:

Dirsearch — https://github.com/maurosoria/dirsearch

A long story short is i found a subdomain from google subdomain.

I got a target : https://learndigital.withgoogle.com/digitalgarage

Press enter or click to view image in full size

From the look of this website you can see that there are two method for account registration forms to enter the system.

And then, I am reminded of a proof of concept that I made, which is :

https://medium.com/@danangtriatmaja/bug-bounty-allowing-register-with-official-domain-cfe605d83b63

Where when someone does the registration process, the system does not verify the registered email.

#Bugbountytips : Security Impact is Email addresses can be sign-in using main domain without verification, and this is can do an action with official email or other.

“sometimes you can try this method to registration with email officially or other and enter the system without verification”

And this is how to reproduce this issue :

Get Danang Tri Atmaja’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Summary: Insufficient Security Configurability | Flaw in Authentication

Steps to reproduce:

Case #1 on the Attacker-Side
1. Go http://learndigital.withgoogle.com/
2. Go registration page and choice signin with email officially
3. Input email official victim, example : gmail.com
4. And then input Name, Fill a password, Confirm password — Click Signup — Done
5. Input First Name & Last Name
6. Choose email preffence And complete — Finish

Note: At this stage you have successfully entered the system using the email that you registered without going through the verification process and you can do any activities using this email

In another Case #2 on the Victim-Side
1. Victim go http://learndigital.withgoogle.com/
2. Go registration page and choice sign in with Gmail
3. Input email & password through Gmail
4. And then the victim sees that his account has been entered by someone unknown

Browser/OS:
1. Firefox
2. Firefox Private

Version : 63.0.1

Video for PoC :

Attack scenario:

Sourced from : https://www.owasp.org/index.php/Top_10_2014-I8_Insufficient_Security_Configurability

Consider the impact of the business if data can be modified and control of the account assumed, other than that the impact of this is that attacker can fill in the data first before the original account owner enters the system

Timeline :

14 — June — 2019 : Report the issue
17 — June — 2019 : Not be severe enough for us to track it as a security bug
19 — June — 2019 : Explain about the security impact of this bug
27 — June — 2019 : Triaged
31 — July — 2019 : Valid issue
Press enter or click to view image in full size
Press enter or click to view image in full size
