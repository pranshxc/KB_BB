---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-30_how-i-bypassed-the-registration-validation-and-logged-in-with-the-company-email.md
original_filename: 2023-01-30_how-i-bypassed-the-registration-validation-and-logged-in-with-the-company-email.md
title: How I bypassed the registration validation and logged-in with the company email
category: documents
detected_topics:
- api-security
- command-injection
- password-reset
- mfa
- otp
- mobile-security
tags:
- imported
- documents
- api-security
- command-injection
- password-reset
- mfa
- otp
- mobile-security
language: en
raw_sha256: 1325ab4a032edbf9f0bcbd95e68378239f5e550f5a6872bb880823119fa1fa8e
text_sha256: a93758a2763710abc680b7bc87078f4404a8c5f5a21e0d3bb328fd2eabd36b37
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed the registration validation and logged-in with the company email

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-30_how-i-bypassed-the-registration-validation-and-logged-in-with-the-company-email.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, password-reset, mfa, otp, mobile-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `1325ab4a032edbf9f0bcbd95e68378239f5e550f5a6872bb880823119fa1fa8e`
- Text SHA256: `a93758a2763710abc680b7bc87078f4404a8c5f5a21e0d3bb328fd2eabd36b37`


## Content

---
title: "How I bypassed the registration validation and logged-in with the company email"
url: "https://khaledyassen.medium.com/how-i-bypassed-the-registration-validation-and-logged-in-with-the-company-email-14eb12c45fb5"
authors: ["Khaledyassen"]
bugs: ["Email verification bypass"]
publication_date: "2023-01-30"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1604
scraped_via: "browseros"
---

# How I bypassed the registration validation and logged-in with the company email

Top highlight

How I bypassed the registration validation and logged-in with the company email
Khaledyassen
Follow
3 min read
·
Jan 30, 2023

410

5

Hello everyone, I hope all is okay with you.

Introduction:

Many websites feature sign-up pages that are only accessible to employees, but sometimes you may bypass the security and log in as an anonymous user. In this article, I’ll discuss different techniques that may be useful to you and a real-life scenario.

Firstly:

I began with wur.nl, a public program for Wageningen University, after gathering subdomains and taking screenshots with the Aquatone tool.

I discovered a target that I was interested in, so let’s go to work on it.

Usually, when I begin working on a target, the first thing I do is sign up for a fake account and browse the target to understand the functionalities to can work on it.

Unfortunately, the register allowed only for WUR-email address.

Press enter or click to view image in full size
What about trying to bypass it :)
Multiple scenarios came to my mind :

1] If you register with Target email, there might not be an activation code sent, try doing the following:

email=user@target.com

2] Response manipulation during the registration process

Response manipulation: technique that is used to make the target display some UI elements it shouldn’t. It can be used to find new endpoints, buttons, and also to trigger some new requests. Sometimes you can also bypass Password restrictions or OTPs

For example if I found thing like

status:false change it to status:true and so on

3] parameter pollution technique, for example

Try doing the following:

Get Khaledyassen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

a] Adding parameters with the same key: value like

email=victim@target.com&email=attacker@gmail.com

b] Adding parameter with incremental key: value pairs like

email=victim@target.com&email2=attacker@gmail.com

4] Sometimes, a list of values for the email parameter can be added to bypass the security, like this

email=[‘attacker@target.com’, ‘atatcker@gmail.com’]

HTTP Parameter Pollution (HPP) : is a Web attack evasion technique that allows an attacker to craft a HTTP request in order to manipulate or retrieve hidden information, You can try this technique on many places like password change, 2FA, comments, profile photo upload, on a parameter where API key is passed, OTP etc.

When you manipulate any parameter, its manipulation depends on how each web technology is parsing their parameters, For further details about parsing, go to this website: https://book.hacktricks.xyz/pentesting-web/parameter-pollution.

5] Playing with the value itself, Sometimes, developers write code with weak regex that can be bypassed in a variety of ways, like the following.

Regex: is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for “find” or “find and replace” operations on strings, or for input validation For example email validation, For further details about regex, go to this website: https://regexr.com/

email=victim@target.com@attacker.com

OR

email=victim@attacker.com@target.com

Other techniques:

email=attacker@target.com.atatcker.com

OR

email=attacker@atatcker.com.target.com

## I started with this

email=attacker@wur.nl.atatcker.com

Press enter or click to view image in full size

It’s working, and I was able to log in :)

Press enter or click to view image in full size
Lastly:

After logging in, I saw that I needed to activate my account in order to use all the features. The website offers a button to do this, so I used the burp collaborator payload to check if I would receive interaction or not, which is why I’m writing this in the registration process.

victim@wur.nl.burpcollaboratorpayload

And I got this

Press enter or click to view image in full size

The POC video https://youtu.be/q3I4ERKDD0U

I hope you found this useful.

Follow me on Twitter and LinkedIn.
