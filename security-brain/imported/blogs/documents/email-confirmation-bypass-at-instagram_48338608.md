---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-10_email-confirmation-bypass-at-instagram.md
original_filename: 2022-08-10_email-confirmation-bypass-at-instagram.md
title: Email Confirmation bypass at Instagram
category: documents
detected_topics:
- password-reset
- command-injection
- business-logic
tags:
- imported
- documents
- password-reset
- command-injection
- business-logic
language: en
raw_sha256: 48338608f97f8120cf8cd587b8719882dc11f4d02697fe42e416c4f2e68399e0
text_sha256: ac680e7332e02eab3fb960ae7b1644e842751c5321e27844cdc5aa2df39ad93b
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Email Confirmation bypass at Instagram

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-10_email-confirmation-bypass-at-instagram.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `48338608f97f8120cf8cd587b8719882dc11f4d02697fe42e416c4f2e68399e0`
- Text SHA256: `ac680e7332e02eab3fb960ae7b1644e842751c5321e27844cdc5aa2df39ad93b`


## Content

---
title: "Email Confirmation bypass at Instagram"
url: "https://medium.com/@avinash_/email-confirmation-bypass-at-instagram-cc968f9a126"
authors: ["Avinash Kumar (@itsavinash_)"]
programs: ["Meta / Facebook"]
bugs: ["Email verification bypass", "Logic flaw"]
bounty: "3,000"
publication_date: "2022-08-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2341
scraped_via: "browseros"
---

# Email Confirmation bypass at Instagram

Email Confirmation bypass at Instagram
Avinash Kumar
Follow
2 min read
·
Aug 11, 2022

520

4

Press enter or click to view image in full size

This story is all about a logical vulnerability which helped me in Bypassing the email confirmation process and adding any arbitrary non-confirmed email to Instagram account.

This starts from when I was testing Instagram’s password reset option. Instagram sends us a magic link for resetting the password or literally login to account. This link provides an open gate by which we can directly enter to our Instagram account.

This Hack revolves around this magic link, Let’s see how?

Attacker added his own email attacker@email.com at his Instagram account but not confirmed it.
From Password reset option attacker requests a Password reset link(magic link).

3. Attacker go his Instagram account’s settings and changed the email to victim email victim@email.com.

4. In same browser attacker opened the magic link and magic happened!

5. The victim’s email victim@email.com has been confirmed automatically in Attacker’s Instagram account.

Get Avinash Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6. Victim’s Identity(email) has been stolen at Instagram.

Proof of Concept:-

https://www.youtube.com/watch?v=3opxcFLprBw

Responsible Disclosure Timeline:-

7 February 2021: Report Sent

10 February 2021: Report Triaged

4 March 2021: Facebook confirmed the fix has been deployed

14 March 2021: $3000 Bounty Rewarded

Facebook Security Team’s Explanation:-

Press enter or click to view image in full size

Thanks!
