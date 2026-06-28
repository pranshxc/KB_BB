---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-23_how-i-bypassed-2fa-while-resetting-password.md
original_filename: 2022-04-23_how-i-bypassed-2fa-while-resetting-password.md
title: How I Bypassed 2FA while Resetting Password
category: documents
detected_topics:
- mfa
- command-injection
- password-reset
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- mfa
- command-injection
- password-reset
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 2c77f2aac1c9f80cace0e7f934984d1e3be707d68241a45d2c031ad9716d9545
text_sha256: 0b57d409ed86864bdef83426302089a085adbf55eb09b504b615b70421619580
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# How I Bypassed 2FA while Resetting Password

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-23_how-i-bypassed-2fa-while-resetting-password.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, password-reset, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `2c77f2aac1c9f80cace0e7f934984d1e3be707d68241a45d2c031ad9716d9545`
- Text SHA256: `0b57d409ed86864bdef83426302089a085adbf55eb09b504b615b70421619580`


## Content

---
title: "How I Bypassed 2FA while Resetting Password"
page_title: "Two factor Authentication bypass by abusing website function | by Sufiyan Gouri | InfoSec Write-ups"
url: "https://infosecwriteups.com/how-i-bypass-2fa-while-resetting-password-3f73bf665728"
authors: ["Sufiyan Gouri (@gouri_sufyan)"]
bugs: ["2FA / MFA bypass", "Password reset"]
publication_date: "2022-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2689
scraped_via: "browseros"
---

# How I Bypassed 2FA while Resetting Password

Sufiyan Gouri
 highlighted

Member-only story

How I Bypassed 2FA while Resetting Password
Sufiyan Gouri
Follow
2 min read
·
Apr 22, 2022

90

2

It was a private program on “Hackerone” , I had set target in my mind that I have to bypass 2fa, so I checked every method to bypass “Two Factor Authentication”

For Better understanding, I have divided this blog into two parts

1:Understanding the Functionality of Web Application.

2: Bypassing Two Factor Authentication.

Let’s Start

I can’t disclose the name of the Website, so let’s consider it “Target.com”

After checking all possible methods, I came to reset password functionality and I send a password reset link and opened it in my browser.

“https://abc.target.com/reset/<token>”

Press enter or click to view image in full size
Entered new password

I entered the new password and clicked on next button and captured the request in burp.

Request:

POST /reset2fa HTTP/1.1

Host: abc.target.com

..

_csrf=<token>&reset_key=<key>&password=***REDACTED***

After forwarding this request it redirected to 2fa page😓

Now I disabled 2fa from my account to check what is difference between both requests when 2fa is enabled&disabled.
