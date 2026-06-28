---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-03_account-takeover-in-cupsmailru.md
original_filename: 2020-08-03_account-takeover-in-cupsmailru.md
title: Account takeover in cups.mail.ru
category: documents
detected_topics:
- sso
- access-control
- command-injection
- password-reset
- business-logic
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- password-reset
- business-logic
- api-security
language: en
raw_sha256: 01709f8369b91363125d52af62d0d312f810d427aaf8d34500168885d4d74586
text_sha256: 1d31ce86e757d34042f7f036d4e0870609085180f13b9d2659a3e32ace2c4fa6
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover in cups.mail.ru

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-03_account-takeover-in-cupsmailru.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, password-reset, business-logic, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `01709f8369b91363125d52af62d0d312f810d427aaf8d34500168885d4d74586`
- Text SHA256: `1d31ce86e757d34042f7f036d4e0870609085180f13b9d2659a3e32ace2c4fa6`


## Content

---
title: "Account takeover in cups.mail.ru"
url: "https://medium.com/kminthein/account-takeover-in-cups-mail-ru-bdab1483f92c"
authors: ["kminthein / weev3 (@kyawminthein99)"]
programs: ["Mail.ru"]
bugs: ["Logic flaw", "Password reset", "Account takeover"]
bounty: "1,500"
publication_date: "2020-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4356
scraped_via: "browseros"
---

# Account takeover in cups.mail.ru

Account takeover in cups.mail.ru
kminthein
Follow
3 min read
·
Aug 3, 2020

363

In this year April 1, I quit my job due to some reason and so I can spend some times in Hackerone. I stopped finding bugs in 2018 because I have insecurity for my skills and I feels I don’t have enough skill set to deep dive into full-time bug hunting and so I tried to learn infra pentest, binary exploitation, source code analysis and some lesser know web attack ..etc. In April 8th, I started digging into Mailru program on Hackerone and I found account takeover bug in one of their subdomain. The bug is a little bit strange and so I want to share other hunters. Some ppls (who know me) think that I spend most of my time in bug hunting but actually I am not, I only spend less than 10hrs a week for hunting bugs. My goal is to be a security engineer who can model the threats, identify and can fix security bugs.

Normal application flow

When a user need to reset their password, he need to click restore access and need to put their associate email.

https://cups.mail.ru/faq/restore-password/restore?step=1

Press enter or click to view image in full size

After entering user email into password reset functionality, one time password reset code is sent to their email and it redirected to

https://cups.mail.ru/faq/restore-password/restore?step=3

Press enter or click to view image in full size

User then put their one time password and if password is correct, it redirects to https://cups.mail.ru/faq/restore-password/restore?step=4.

Press enter or click to view image in full size

Then he can reset their password and the requests contains

Get kminthein’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

{“password”:”password”,”email”:”user@gmail.com”,”code”:”onetimepassword”} .

Abusing password reset functionality

Due to lack of access control in their password reset functionality, I can reset every user’s password. I visit https://cups.mail.ru/faq/restore-password/restore?step=4 and then I changed original request which is {“password”:”password”,”email”:”user@gmail.com”,”code”:”onetimepassword”} to {“password”:”reset”, “email”: “victim@gmail.com”} as shown in below.

Press enter or click to view image in full size

After removing code parameter and forward the requests and then it redirected to

https://cups.mail.ru/faq/restore-password/restore?step=5

Press enter or click to view image in full size

I just shocked and tried to login with victim email but failed xD. I asked myself why?. The response said password is reset successfully.

So, I retest their password reset functionality and this time I clicked to come in link(see in above screenshot?) and surprisingly, victim’s password is reset successfully and I can login to victim account.

Conclusion

Honestly, I still don’t know how they implement password reset functionality in their back-end. In general, the vulnerable web application should reset successfully and it doesn’t matter clicking to come in link or not, but in this scenario they checked something in their back-end(may be Referer?). So if you don’t to click to come in link, the password reset functionality will fail.

I quickly reported to Mail.ru bb program and they rewarded $1500 for this bug.

Press enter or click to view image in full size
