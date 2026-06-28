---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-05_stored-xss-on-bizwazecom.md
original_filename: 2020-05-05_stored-xss-on-bizwazecom.md
title: Stored XSS on biz.waze.com
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 3b0443e4b6486d7e5460067cd6dd1a3ac638bb5c930834f67904c357f45acc84
text_sha256: 07775c39353055943129a2bd8e2d3225550a89498ddae94bee1fd3261476e03b
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on biz.waze.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-05_stored-xss-on-bizwazecom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `3b0443e4b6486d7e5460067cd6dd1a3ac638bb5c930834f67904c357f45acc84`
- Text SHA256: `07775c39353055943129a2bd8e2d3225550a89498ddae94bee1fd3261476e03b`


## Content

---
title: "Stored XSS on biz.waze.com"
page_title: "Sign in - Google Accounts"
url: "https://sites.google.com/securifyinc.com/vrp-writeups/waze/waze-xss"
final_url: "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fsites.google.com%2Fsecurifyinc.com%2Fvrp-writeups%2Fwaze%2Fwaze-xss&dsh=S-1459248330%3A1782624287449235&followup=https%3A%2F%2Fsites.google.com%2Fsecurifyinc.com%2Fvrp-writeups%2Fwaze%2Fwaze-xss&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AcDsRvxGNGMMpTjAWqyaTRI03sjOwc-KzmWoKN6-PWo8UcRMFR9rB0AykN-AFE_LRpg22oADFrhs5w"
authors: ["Rojan Rijal (@uraniumhacker)"]
programs: ["Google (Waze)"]
bugs: ["XSS"]
publication_date: "2020-05-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4606
---

Loading

# Sign in

Use your Google Account

Email or phone

Forgot email?

Type the text you hear or see

Not your computer? Use Guest mode to sign in privately. [Learn more about using Guest mode](https://support.google.com/chrome/answer/6130773?hl=en-US)

Next

Create account
