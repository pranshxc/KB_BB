---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-01_bypass-2fa-in-a-website.md
original_filename: 2020-01-01_bypass-2fa-in-a-website.md
title: Bypass 2FA in a website
category: documents
detected_topics:
- mfa
- command-injection
- password-reset
- otp
- csrf
tags:
- imported
- documents
- mfa
- command-injection
- password-reset
- otp
- csrf
language: en
raw_sha256: 331204ccd94a356a39371c215f04b90308a95aa8fe164c1e8f10bf80ab7bcbf4
text_sha256: 4eff7c7c737301e6f86e889b97965aed98d7de864cb895c103ee137a4a5221bc
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass 2FA in a website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-01_bypass-2fa-in-a-website.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, password-reset, otp, csrf
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `331204ccd94a356a39371c215f04b90308a95aa8fe164c1e8f10bf80ab7bcbf4`
- Text SHA256: `4eff7c7c737301e6f86e889b97965aed98d7de864cb895c103ee137a4a5221bc`


## Content

---
title: "Bypass 2FA in a website"
url: "https://medium.com/sourav-sahana/bypass-2fa-in-a-website-d616eaead1e3"
authors: ["Sourav Sahana (@kernel_rider)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2020-01-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4848
scraped_via: "browseros"
---

# Bypass 2FA in a website

Bypass 2FA in a website
Sourav Sahana
Follow
1 min read
·
Jan 9, 2020

247

4

01.01.2020

Hii hunters ! I’m again with another story. I love 2FA, not because it provide extra security. Because of satisfaction to bypass them. Stay tuned with me because I’ll post more story on 2FA bypass. Enjoy the story !!

It was first day of 2020. I found a way to bypass 2fa in a website. I was randomly searching bug bounty program with GHDB. And found a domain that is allowing users to enable 2fa with google authentication app. Challenge accepted…

First I tried in login page. Tries every possible way but didn’t get any success. Then I thought lets look at the forget password page, I Entered my email ID and and clicked on ‘forgot password’ . After few seconds I got an email that looks like this: https://app.domain .io/reset/645hNr78tr5410HgG6yvYZtk2Y45lki7/

Get Sourav Sahana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I visited the url and entered a new password. After clicking submit, a new window opened that asking me 2FA code. So I first tried with response manipulation. But didn’t work.

Then I looked at the request to see what was going on with my 2fa code. That was a POST request and in the body I found ‘reset_key’, ‘_csrf’, ‘email’, ‘password’ and ‘token’ parameters. ‘token’ is my 2FA code.

I deleted token parameter and it’s value. Then I forwarded the request. And BOOM… I was redirected in my account with a notification : “Password successfully changed” . I was like…

Thank you for your time. Hope you enjoyed this story. Happy Hunting.!!
