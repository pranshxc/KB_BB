---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-19_broken-session-management-leads-to-bypass-2fa-and-permanent-access-to-facebook-u.md
original_filename: 2019-11-19_broken-session-management-leads-to-bypass-2fa-and-permanent-access-to-facebook-u.md
title: Broken session management leads to bypass 2FA and Permanent access to Facebook
  user’s
category: documents
detected_topics:
- command-injection
- mfa
- mobile-security
tags:
- imported
- documents
- command-injection
- mfa
- mobile-security
language: en
raw_sha256: 211e1955ffdb8f1c76028e87e41857cb3075b0cc58f043b753c58aed17249161
text_sha256: f15483e8ddd72d1cc564d51c3e366dfd3ab6a58b93f8a7e6e5e4b26e033211e0
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Broken session management leads to bypass 2FA and Permanent access to Facebook user’s

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-19_broken-session-management-leads-to-bypass-2fa-and-permanent-access-to-facebook-u.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `211e1955ffdb8f1c76028e87e41857cb3075b0cc58f043b753c58aed17249161`
- Text SHA256: `f15483e8ddd72d1cc564d51c3e366dfd3ab6a58b93f8a7e6e5e4b26e033211e0`


## Content

---
title: "Broken session management leads to bypass 2FA and Permanent access to Facebook user’s"
url: "https://medium.com/@0xBarakat/broken-session-permanent-access-to-facebook-users-cfed68684113"
authors: ["Mahmoud Barakat (@0xBarakat)"]
programs: ["Meta / Facebook"]
bugs: ["Authentication bypass"]
publication_date: "2019-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4931
scraped_via: "browseros"
---

# Broken session management leads to bypass 2FA and Permanent access to Facebook user’s

Broken session management leads to bypass 2FA and Permanent access to Facebook user’s
Mahmoud Barakat
Follow
2 min read
·
Nov 20, 2019

379

Press enter or click to view image in full size
Zuck

The story began when i received a notification from a friend about a donation campaign for his birthday. while using Facebook-App (IOS) when i tried to click donate button it redirected me to Web-browser version to make a donation using Creditcard or Paypal, throw this endpoint {/donation/login/?nonce=xxxxx&uid=xxxxxx}

Donation Feature

https://m.facebook.com/donation/login/?nonce=xxxxxx&uid={USER_ID}

I noticed that when go to Facebook.com in your Web Browser even if you didn’t signed in with your Facebook account the Facebook will automatically redirect you to your Facebook-Account without any password or any authentication !!

So I did the same scenario again but I copied the link https://m.facebook.com/donation/login/?nonce=xxxxxx&uid={USER_ID} and sent it to a friend i noticed that he got access to my Facebook account without any authentication (2FA — Password) and if you tried to change your password he’ll still has access to your Facebook !!

Steps :
Go to donate to any organization from Facebook App(IOS)
EX: https://www.facebook.com/donate/xxx/xxx/

2. Try to make a donation
3. You will be redirected to endpoint “https://m.facebook.com/donation/login/?nonce=xxxxxx&uid=xxxxxx “
4. Copy this link and try to use it from another device which you didn’t signed-in with your Account before.
5. Go to Facebook.com then you will be redirected automatically to the victim account.
6. Getting access into the Facebook account without Password or 2FA (even if the victim changed the password or remove all session you will still getting access to Facebook account.)

Impact :
Permanent access to Facebook user’s.
Bypassing any authentication.
Timeline

June. 18, 2019 — Initial Report
June. 19, 2019 — Report Triaged
June. 21, 2019 — Fixed By Facebook
June. 21, 2019 — Fixed Confirmed
June. 27, 2019 — Bounty awarded

Bounty awarded

Happy Hacking!!

Get Mahmoud Barakat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

@0xBarakat
