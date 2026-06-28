---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-05_facebook-oauth-bypass.md
original_filename: 2022-02-05_facebook-oauth-bypass.md
title: Facebook Oauth bypass
category: documents
detected_topics:
- oauth
- access-control
- command-injection
- mfa
- otp
tags:
- imported
- documents
- oauth
- access-control
- command-injection
- mfa
- otp
language: en
raw_sha256: 2d6ac0f62a0c0300f145358b7c8dbf8c07c56841afc0f797bd1f46d060d15b76
text_sha256: b08580b7849f7f80d72533cd72504e72a6000307618ce4a0c14ddf3c31d32c87
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Oauth bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-05_facebook-oauth-bypass.md
- Source Type: markdown
- Detected Topics: oauth, access-control, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `2d6ac0f62a0c0300f145358b7c8dbf8c07c56841afc0f797bd1f46d060d15b76`
- Text SHA256: `b08580b7849f7f80d72533cd72504e72a6000307618ce4a0c14ddf3c31d32c87`


## Content

---
title: "Facebook Oauth bypass"
url: "https://medium.com/@yaala/facebook-oauth-bypass-446a073e687d"
authors: ["abdellah yaala (@yaalaab)"]
programs: ["Meta / Facebook"]
bugs: ["OAuth"]
bounty: "7,500"
publication_date: "2022-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2936
scraped_via: "browseros"
---

# Facebook Oauth bypass

Facebook Oauth bypass
abdellah yaala
Follow
Feb 6, 2022

137

A malicious user can steal access token for some facebook canvas applications

before 3 year this bug is N/A , because we can’t do anything with authorization code not like access token . but in 2021 meta rewarded me 7500$.

before 3 years during my testing in Oauth facebook applications, I discovered that oauth can bypassed for any canvas application have username, by adding app_id=attacker_app_id as parameter in redirect_uri :

https://www.facebook.com/dialog/oauth?client_id=appid&scope=email&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fapplicationsusername%2F?app_id=attacker_app_id

oauth redirected to attacker application instead to real application

Get abdellah yaala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

in 2021 I see Facebook add nonce as response type in oauth . I discovered endpoint to convert nonce code to access token

Timeline :

January 3, 2021 : Report Sent

February 16, 2021: bounty rewarded (7500$)

Thanks
