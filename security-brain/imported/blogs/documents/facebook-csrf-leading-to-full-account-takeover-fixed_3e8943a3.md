---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-10-18_facebook-csrf-leading-to-full-account-takeover-fixed.md
original_filename: 2013-10-18_facebook-csrf-leading-to-full-account-takeover-fixed.md
title: Facebook CSRF leading to full account takeover (fixed)
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
raw_sha256: 3e8943a3b4641edfac412567eb6014b6a4e40c09f185431ee47702aacedd91a3
text_sha256: 581200c02c2db0633a51ff8b230c138b0b764d4afc1f5cb25cfeb743af007952
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook CSRF leading to full account takeover (fixed)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-10-18_facebook-csrf-leading-to-full-account-takeover-fixed.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `3e8943a3b4641edfac412567eb6014b6a4e40c09f185431ee47702aacedd91a3`
- Text SHA256: `581200c02c2db0633a51ff8b230c138b0b764d4afc1f5cb25cfeb743af007952`


## Content

---
title: "Facebook CSRF leading to full account takeover (fixed)"
page_title: "Facebook CSRF leading to full account takeover (fixed) -  Josip Franjković"
url: "https://www.josipfranjkovic.com/blog/facebook-csrf-full-account-takeover"
final_url: "https://www.josipfranjkovic.com/blog/facebook-csrf-full-account-takeover"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF", "Account takeover"]
bounty: "8,450"
publication_date: "2013-10-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6395
---

#  [ Josip Franjković web security consultant ](/)

[Blog](/)

Bug bounties

##  Facebook CSRF leading to full account takeover (fixed) 

written on October 18th, 2013

Some cross site request forgeries are mere annoyance (like logout CSRF), some can be useful (example: changing name of user), and some - like the one I found - can be pretty devastating. 

This bug has some similarities to [Dan Melamed's findings](https://web.archive.org/web/20141111153957/http://www.dan-melamed.com/2013/06/hacking-any-facebook-account-exploit-poc.html) (archive.org link). 

To exploit this, you need a Facebook account, an Outlook.com (Hotmail) email, and a victim. The Outlook email must not be bound to your Facebook account. 

When you approve Facebook to access Outlook's contact book, a GET request to 
  
  
  https://m.facebook.com/contact-importer/login/?api_instance=1&api_ver=wave5&auth_token=TOKEN

is made, which adds the email to your account. This request has no checks; you can repeat it as many times as you want. 

**The problem is, it works for OTHER users too.**

#### So, the course of action to take over victim's account would be:

  1. Use "Find contacts on Facebook" from attacker account and log all requests 

  2. Find the /contact-importer/login request 

  3. Remove added email from your (attacker) account 

  4. Get the victim to somehow make the /contact-importer/login request (infinite possibilities here) 

  5. Email is now added to victim's account, silently 

  6. Use "Forgot your password" to take over the account 

[Click here](https://www.youtube.com/watch?v=EKvnM1oNpNw) for a video demonstrating the vulnerability. 

#### Timeline:

  * **August 13, 2013, 07:00:** Bug reported 

  * August 13, 2013, 19:40: Better PoC and video sent to Facebook team 

  * August 14, 2013, 01:00: Facebook team replies 

  * **August 14, 2013, 03:00:** Bug is fixed 

I would like to thank Facebook's security team for running their bug bounty program, and for quickly patching this issue - it took them only 2 hours to roll out working patch. 

##### Random blog post

Bug bounties 

####  Getting any Facebook user's friend list and partial payment card details 

written on March 9th, 2018

[ Read more ](/blog/facebook-friendlist-paymentcard-leak)

![Josip Franjković](/resources/img/josip-franjkovic.jpg)

##### Josip Franjković

###### web security consultant

I enjoy breaking websites and participating in various bug bounty programs. 

##### You can contact me using:

  * [@JosipFranjkovic](https://twitter.com/josipfranjkovic) (DM open to everyone) 
  * [[email protected]](/cdn-cgi/l/email-protection#365c59455f4618504457585c5d59405f5576515b575f5a1855595b)
  * [keybase.io/josipfranjkovic](https://keybase.io/josipfranjkovic)

All rights reserved © 2018.  
— Josip Franjković
