---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-11_pre-denial-of-service-set-up-2fa-on-unverified-account.md
original_filename: 2021-07-11_pre-denial-of-service-set-up-2fa-on-unverified-account.md
title: Pre-Denial Of Service (set-up 2FA on unverified account)
category: documents
detected_topics:
- mfa
- command-injection
- api-security
tags:
- imported
- documents
- mfa
- command-injection
- api-security
language: en
raw_sha256: 8314b9b72fbd45e5673a3ffe225e0acbc604f88374f690ed23565fb1948a7639
text_sha256: 8c4ae4aee56226d2670a4d646bc788025ea105dd614c40f10765da3a45d25c59
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Pre-Denial Of Service (set-up 2FA on unverified account)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-11_pre-denial-of-service-set-up-2fa-on-unverified-account.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `8314b9b72fbd45e5673a3ffe225e0acbc604f88374f690ed23565fb1948a7639`
- Text SHA256: `8c4ae4aee56226d2670a4d646bc788025ea105dd614c40f10765da3a45d25c59`


## Content

---
title: "Pre-Denial Of Service (set-up 2FA on unverified account)"
url: "https://medium.com/@kalvik/pre-denial-of-service-set-up-2fa-on-unverified-account-8399af52ea2d"
authors: ["Vikash Maurya"]
bugs: ["Application-level DoS"]
publication_date: "2021-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3515
scraped_via: "browseros"
---

# Pre-Denial Of Service (set-up 2FA on unverified account)

Press enter or click to view image in full size
Pre-Denial Of Service (set-up 2FA on unverified account)
Vikash Maurya
Follow
2 min read
·
Jul 11, 2021

118

Here I will explain how I was able to setup 2FA on a unverified account which results denial of service for real user of that email. (Assuming victim has not registered his account yet). I’ll try to keep it short and simple for better understanding.

The setup flow was:

Sign-up account.
Verify email.
Setup 2FA.

Without verifying email, you cant setup 2FA as per security standards. I successfully bypassed this restriction and was able to setup 2FA without verifying email.

The website was using websocket. On setting up 2FA on a verified account, the first websocket request looked like this:

[“{\”msg\”:\”method\”,\”method\”:\”2fa/generateMFA\”,\”params\”:[],\”id\”:\”XXXX\”}”]

Then,

[“{\”msg\”:\”method\”,\”method\”:\”2fa/getSecretKey\”,\”params\”: [],\”id\”:\”XXXX\”}”]

This in response returned a secret key which is used in authenticator app to setup 2FA, So I thought to try sending above request from an unverified account.

Get Vikash Maurya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I logged in to victim’s account , sent this request

[“{\”msg\”:\”method\”,\”method\”:\”mfa/getSecretKey\”,\”params\”:[],\”id\”:\”24\”}”]

Unfortunately I got “The account is not verified” in response. Then after some hit and trial, I noticed that the first request of setting up 2FA was this one i.e. [“{\”msg\”:\”method\”,\”method\”:\”mfa/generateMFA\”,\”params\”:[],\”id\”:\”XXXX\”}”]

So again the sent this request from victim’s account, and got a blank response.

Again I tried sending [“{\”msg\”:\”method\”,\”method\”:\”mfa/getSecretKey\”,\”params\”:[],\”id\”:\”24\”}”]

This time I successfully got secret key in response. It was like 10–12 character long.

I opened Google Authenticator and quickly setup 2FA using that secret code and it was successful.

This way I was able to setup 2FA on a unverified account which blocks the real user of that email from accessing the website in future.

Timeline:

28 June 2021 : Reported
29 June 2021 : Acknowledged
2 July 2021 : Fixed and $$$ bounty.

Thanks for reading.
