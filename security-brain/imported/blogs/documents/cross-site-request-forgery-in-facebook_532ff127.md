---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-04_cross-site-request-forgery-in-facebook.md
original_filename: 2017-02-04_cross-site-request-forgery-in-facebook.md
title: Cross Site Request Forgery in Facebook
category: documents
detected_topics:
- command-injection
- password-reset
- csrf
tags:
- imported
- documents
- command-injection
- password-reset
- csrf
language: en
raw_sha256: 532ff127aa650f7844bf45a7f3fa91e8b75962e9958efe0874c2dd0c038c23e5
text_sha256: 323dbb0b56ffdb56cd26e533a61b2f5b37d36115a955de4473a855bf322ee656
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Cross Site Request Forgery in Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-04_cross-site-request-forgery-in-facebook.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, csrf
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `532ff127aa650f7844bf45a7f3fa91e8b75962e9958efe0874c2dd0c038c23e5`
- Text SHA256: `323dbb0b56ffdb56cd26e533a61b2f5b37d36115a955de4473a855bf322ee656`


## Content

---
title: "Cross Site Request Forgery in Facebook"
url: "https://medium.com/@zahidali_93675/cross-site-request-forgery-in-facebook-86087201d8c"
authors: ["Zahid Ali"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "1,000"
publication_date: "2017-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6230
scraped_via: "browseros"
---

# Cross Site Request Forgery in Facebook

Zahid Ali
Follow
2 min read
·
Feb 4, 2017

83

1

C
ross Site Request Forgery in Facebook

Victim having facebook account with number (+9233320xxxxx) — (Number
is confirmed on that account)

Attacker having facebook account with same number (+9233320xxxxx) — (
But number is unconfirmed on that id) Or Attacker can add that number
to any facebook account but (unconfirmed)

According to Facebook Policy User(s) can confirm that specific number
in each account. They can add that same number with multiple
account(s) but confirmed with only one account.

“In 2016 i reported facebook that i am able to add any number in my
facebook id(unconfirmed). But that number will display on my Facebook
so i can impersonate someone’s identify. They said “We are already
aware of the situation” and this is not a bug.”

In 2016 december i found out that i am able to reset password with
unconfirmed number(s) and email(s). So as an attacker i sent password
reset request to (+9233320xxxxx). But i was not able to get any code +
url to reset password because of being an attacker i did not have physical access
on that number.

But as a victim i got message from 32665 (FBOOK) that

“Your password reset code is 283923 and URL https://www.fb.com/h2hdj232”

Get Zahid Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As a victim i clicked on that encoded link
(https://www.fb.com/h2hdj232). After a single click on that encoded
link. The number (+9233320xxxxx) was deleted from victim’s account and
added into attacker’s facebook account.

Actualy when victim clicked on encoded link the number was deleted from
the victim’s id and added into attacker’s account because victim was
redirected to the attacker’s facebook account.

I submitted report and got reply from Neal
========================================
Hi Zahid,
Got it. The ability to reset the account via these methods is not the
problem: the problem is that we confirm the email or phone number when
someone simply clicks a link which isn’t clear that it will confirm
the account. I’ll follow up with the team about it.
Thanks,
Neal
Security
========================================

After a few hours i got another reply from Neal

========================================
Hi Zahid,
We’ve temporarily disabled the ability to perform password recovery
via unconfirmed phone numbers as a mitigation.
Thanks,
Neal
Security
========================================

I asked Neal, if this is a valid bug ?

========================================
Hi Zahid,
Yes, we’re going to change the circumstances in which we allow phone
confirmations to happen in this flow.
Thanks,
Neal
Security
========================================

I found multiple bugs in Facebook and i am in the hall of fame
2015/2016 and now 2017. I hope this POC was helpful.
