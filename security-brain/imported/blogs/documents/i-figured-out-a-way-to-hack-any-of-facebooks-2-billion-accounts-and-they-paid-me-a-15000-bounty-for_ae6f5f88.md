---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-09_i-figured-out-a-way-to-hack-any-of-facebooks-2-billion-accounts-and-they-paid-me.md
original_filename: 2018-02-09_i-figured-out-a-way-to-hack-any-of-facebooks-2-billion-accounts-and-they-paid-me.md
title: I figured out a way to hack any of Facebook’s 2 billion accounts, and they
  paid me a $15,000 bounty for it
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- api-security
language: en
raw_sha256: ae6f5f88311ce7082fd2229bfdbf5a71509d49fe5c496ddb2c5d4b92d65f3be7
text_sha256: 3679c2de6fd3860cdc8648ff1259fd0afc5fa46680a8549d2053198134610fb1
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# I figured out a way to hack any of Facebook’s 2 billion accounts, and they paid me a $15,000 bounty for it

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-09_i-figured-out-a-way-to-hack-any-of-facebooks-2-billion-accounts-and-they-paid-me.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `ae6f5f88311ce7082fd2229bfdbf5a71509d49fe5c496ddb2c5d4b92d65f3be7`
- Text SHA256: `3679c2de6fd3860cdc8648ff1259fd0afc5fa46680a8549d2053198134610fb1`


## Content

---
title: "I figured out a way to hack any of Facebook’s 2 billion accounts, and they paid me a $15,000 bounty for it"
page_title: "I figured out a way to hack any of Facebook’s 2 billion accounts, and they paid me a $15,000 bounty…"
url: "https://medium.freecodecamp.org/responsible-disclosure-how-i-could-have-hacked-all-facebook-accounts-f47c0252ae4d"
final_url: "https://www.freecodecamp.org/news/responsible-disclosure-how-i-could-have-hacked-all-facebook-accounts-f47c0252ae4d"
authors: ["Anand Prakash (@anandpraka_sh)"]
programs: ["Meta / Facebook"]
bugs: ["Bruteforce", "Account takeover"]
bounty: "15,000"
publication_date: "2018-02-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5980
---

February 9, 2018  / [ #Facebook ](/news/tag/facebook/)

# I figured out a way to hack any of Facebook’s 2 billion accounts, and they paid me a $15,000 bounty…

![I figured out a way to hack any of Facebook’s 2 billion accounts, and they paid me a $15,000 bounty…](https://cdn-media-1.freecodecamp.org/images/1*YxD3C1C9qLsIGG4pqLv7ig.jpeg)

By AppSecure

I am publishing this with the permission of Facebook under the responsible disclosure policy. They have fixed this vulnerability.

This post is about a simple vulnerability I discovered on Facebook which I could have used to hack into other users’ Facebook accounts easily and without any user interaction.

This gave me full access to other users account by setting a new password. I was able to view messages, their credit/debit cards stored under their payment section, personal photos, and other private information.

Facebook acknowledged the issue promptly, fixed it, and rewarded me with a US $15,000 bounty based on the severity and impact of this vulnerability.

### How the hack worked

Whenever a user Forgets their password on Facebook, they have an option to reset the password by entering their phone number and email address on [https://www.facebook.com/login/identify?ctx=recover&lwv=110](https://www.facebook.com/login/identify?ctx=recover&lwv=110&__mref=message).

Facebook will then send a 6 digit code to this phone number or email address which the user has to enter in order to set a new password.

I tried to brute force the 6 digit code on [www.facebook.com](http://www.facebook.com/?__mref=message) and was blocked after 10–12 invalid attempts.

Then I looked out for the same issue on beta.facebook.com and mbasic.beta.facebook.com. Interestingly, rate limiting was missing from forgot password endpoint.

I tried to take over my own account (as per Facebook’s policy, you should not do any harm any other users’ accounts) and was successful in setting a new password for my account. I could then use this same password to log into my own hacked account.

### A proof of concept video of the hack

As you can see in the video, I was able to set a new password for the user by brute forcing the code which was sent to their email address and phone number.

### **Vulnerable request**

`POST /recover/as/code/ HTTP/1.1`

`Host: beta.facebook.com`

`lsd=AVoywo13&n=XXXXX`

Brute forcing the “n” successfully allowed me to set new password for any Facebook user.

### **Disclosure Timeline**

Feb 22nd, 2016 : Report sent to Facebook team.

Feb 23rd, 2016 : Verified the fix from my end.

March 2nd, 2016 : Bounty of $15,000 awarded by Facebook

* * *

If you read this far, thank the author to show them you care. Say Thanks

Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. [Get started](https://www.freecodecamp.org/learn)

ADVERTISEMENT
