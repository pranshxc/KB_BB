---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-22_password-reset-token-leak-via-referrer.md
original_filename: 2020-01-22_password-reset-token-leak-via-referrer.md
title: Password Reset Token Leak Via Referrer
category: documents
detected_topics:
- password-reset
- command-injection
- otp
- automation-abuse
- csrf
- information-disclosure
tags:
- imported
- documents
- password-reset
- command-injection
- otp
- automation-abuse
- csrf
- information-disclosure
language: en
raw_sha256: 480fc583b5c640d6a501f45999ff7aa57727572876e736dd844567c224229376
text_sha256: e9f2c5c3bd3e88bba30e628b9e6bb7159a6288b88bc48a2a81f3e74ba99b597a
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Password Reset Token Leak Via Referrer

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-22_password-reset-token-leak-via-referrer.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, otp, automation-abuse, csrf, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `480fc583b5c640d6a501f45999ff7aa57727572876e736dd844567c224229376`
- Text SHA256: `e9f2c5c3bd3e88bba30e628b9e6bb7159a6288b88bc48a2a81f3e74ba99b597a`


## Content

---
title: "Password Reset Token Leak Via Referrer"
url: "https://medium.com/@shahjerry33/password-reset-token-leak-via-referrer-2e622500c2c1"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["Password reset", "Information disclosure"]
publication_date: "2020-01-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4818
scraped_via: "browseros"
---

# Password Reset Token Leak Via Referrer

Password Reset Token Leak Via Referrer
Jerry Shah (Jerry)
Follow
2 min read
·
Jan 22, 2020

698

5

Summary :

I found this vulnerability in a responsible disclosure program and I was rewarded with Hall Of Fame.

What is referrer ?

The HTTP referrer is an optional HTTP header field that identifies the address of the webpage which is linked to the resource being requested. The Referer request header contains the address of the previous web page from which a link to the currently requested page was followed.

Why this is a vulnerability ?

It allows the person who has control of particular site to change the user’s password (CSRF attack), because this person knows reset password token of the user.

For example : There is a site name www.mydomain.com which has the password reset functionality. User A resets the password using that functionality. Now that request has the referrer header which contains a link of another webpage with the password reset token. Now that owner can use that token to compromise the victim’s account.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How to find this vulnerability ?

Go to any website that has password reset functionality
Press enter or click to view image in full size
Password reset page

2. Add your email and click on send. It will send the password reset link to your email

Press enter or click to view image in full size
Requested Password reset

3. Now open your email and click on that link to change the password

Press enter or click to view image in full size
Reset Password Email

4. You’ll find you’re password reset token in the URL and you can see the third party app on the bottom of the page.

Press enter or click to view image in full size
Password reset token and third party app

5. Now click on any of the app (twitter, facebook, linkedin) given on the webpage and intercept the request using burp suite

Press enter or click to view image in full size
Token leakage via referrer

6. You’ll see that your token is leaking via referrer to third party

Thank You :)

Instagram : jerry._.3
