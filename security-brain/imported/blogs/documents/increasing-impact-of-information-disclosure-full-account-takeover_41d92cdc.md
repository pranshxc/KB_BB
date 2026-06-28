---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-26_increasing-impact-of-information-disclosure-full-account-takeover-.md
original_filename: 2021-03-26_increasing-impact-of-information-disclosure-full-account-takeover-.md
title: Increasing impact of Information Disclosure — Full Account Takeover !
category: documents
detected_topics:
- password-reset
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- password-reset
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 41d92cdc7b7a5be25db9cfc489f481c3d74ab8c46b82b66ef23d0cb75c037c9c
text_sha256: 1d69600b82a4a1103570f7efc53d5cd90c9e1a0d98d00361568cba13bd246939
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Increasing impact of Information Disclosure — Full Account Takeover !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-26_increasing-impact-of-information-disclosure-full-account-takeover-.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `41d92cdc7b7a5be25db9cfc489f481c3d74ab8c46b82b66ef23d0cb75c037c9c`
- Text SHA256: `1d69600b82a4a1103570f7efc53d5cd90c9e1a0d98d00361568cba13bd246939`


## Content

---
title: "Increasing impact of Information Disclosure — Full Account Takeover !"
url: "https://abhisek3122.medium.com/increasing-impact-of-information-disclosure-full-account-takeover-2f12d8963d5c"
authors: ["Abhisek R (@abh1sek_r)"]
bugs: ["Information disclosure", "Password reset"]
publication_date: "2021-03-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3788
scraped_via: "browseros"
---

# Increasing impact of Information Disclosure — Full Account Takeover !

Increasing impact of Information Disclosure — Full Account Takeover !
Abhisek R
Follow
3 min read
·
Mar 26, 2021

91

1

Press enter or click to view image in full size

Hey, I’m Abhisek. Back with another write up. This write up is based upon my bug hunting tactics of increasing impact of information disclosure. With no further delay, Let’s start *_*

Working on Computer

As usual, I took a program and started checking it. Generally I like looking for authentication related bugs.

Now, Look these concepts. Information Disclosure vulnerabilities allows attacker to take advantage with the leaked piece of information. If the site is using GET method requests with sensitive information in its parameters, Then the site is vulnerable for information disclosure. It is because those information could get leaked through Web logs, Referer header, and More.

Okay, Learnt a lot? Nope actually. We haven’t learnt yet, we just read it. How we practically exploit this scenario?

Press enter or click to view image in full size

So now, Let’s get back to the target. I requested for a password reset on redacted.com, It sent me a reset link to my email. Copied, Turned on proxy(Ex.Burpsuite) and Opened.

Get Abhisek R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Wait, before changing password look the http history. Guess what, Password reset token is leaked to 3rd party !

But wait, Even if the attacker gets the reset token. He/She will be only able to reset password and will not be knowing “email id (or) username” to login again.

Press enter or click to view image in full size

Just kidding, Back to content. Again checking the HTTP requests, You know one of the request was leaking the user_id. Unless you find the email or username related to user_id its complete waste.

Then just went on browsing the site, There was a information disclosure again. And now it leaked user_id, email, username.

Now, You must get what I’m gonna say !

Yes, If attacker gets those two requests. He would be able to take over the account. Woah ?! But SHIT HAPPENS

Wrote a 2 page long report with all proof of concept and Company staff comes in contact, “Although the behavior described in your submission appears to be valid. They are our trusted 3rd parties”

Okay, End your excitement here. I’m Done on this write up !

In this field consistency is important, Stay Active. Bye bye *_*

Reach me out on Instagram, Twitter and LinkedIn
