---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-22_tale-of-account-takeovers-part-1.md
original_filename: 2020-02-22_tale-of-account-takeovers-part-1.md
title: Tale of Account Takeovers (Part-1)
category: documents
detected_topics:
- password-reset
- otp
- command-injection
- automation-abuse
- csrf
- cloud-security
tags:
- imported
- documents
- password-reset
- otp
- command-injection
- automation-abuse
- csrf
- cloud-security
language: en
raw_sha256: ce1fc06201810cc2716a337f614f3a92b205e632e2f2da98c2139be2dce8f02e
text_sha256: b286343861a23cc50d49b0a68f901e88f9c6f708aeace51dc97688177c77e703
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of Account Takeovers (Part-1)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-22_tale-of-account-takeovers-part-1.md
- Source Type: markdown
- Detected Topics: password-reset, otp, command-injection, automation-abuse, csrf, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `ce1fc06201810cc2716a337f614f3a92b205e632e2f2da98c2139be2dce8f02e`
- Text SHA256: `b286343861a23cc50d49b0a68f901e88f9c6f708aeace51dc97688177c77e703`


## Content

---
title: "Tale of Account Takeovers (Part-1)"
url: "https://medium.com/@bathinivijaysimhareddy/tale-of-account-takeovers-part-1-b24e1f3c3187"
authors: ["Vijaysimha Reddy Bathini (@fatratfatrat)"]
bugs: ["Account takeover", "HTTP parameter pollution", "Password reset", "OTP bypass"]
bounty: "5,000"
publication_date: "2020-02-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4759
scraped_via: "browseros"
---

# Tale of Account Takeovers (Part-1)

Top highlight

Tale of Account Takeovers (Part-1)
Vijaysimha Reddy Bathini
Follow
4 min read
·
Feb 22, 2020

601

6

Hello guys, I’m here with a new blog post on account takeover vulnerabilities that have been reported by me. I’ve started bug bounty in the month of Jan-2019 where I have reported quite of few low hanging fruits which ended up in duplicates. After getting released from my college I got a lot of time to spend on bug hunting and learning recon process and building my own recon methodology and understanding the functionality and application flow. I would like to thank Nahamsec and Jhaddix for their recon streams. November has been the best month for me till now with a few account takeovers reported and got paid high. In this blog post, I would like to explain all the ACCOUNT TAKEOVER scenarios which I have reported. So Let’s get started…

What is Account Takeover Vulnerability?

This is a type of vulnerability that allows hackers to take full control of the user's account without any need for a password by finding the flaws in the application.

How it can be done?

There can be many ways to find the account takeover bugs like brute-forcing the OTP, account takeover through csrf, etc. I have found 6 account takeover bugs till now and still counting. In this blog post, I will explain how I achieved account takeover through HTTP Parameter pollution and account takeover through improper server-side validation of mobile numbers. I’ll be making a few more account takeovers in the next blogs as content might get heavy.

Account Takeover Scenario 1:

There was a forgot password implementation that will send an email with a password reset link to the provided email. First thing I have done is capture the request when clicked on forgot password there was a JSON data passing like this:

{“email”:”victim@gmail.com”,“token”:”some random token”}

When I forward this request reset link will be sent to this mail.

I have added a one more email address like this:

{“email”:[“victim@gmail.com”,”attacker@gmail.com”],”token”:”some random token”}

When I click on forward mail with the same password reset link was sent to both emails leading to account takeover.

Exploit Scenario:

Attacker issues a forgot password request of the victim account and capture the request.
The attacker then adds his email account along with the victim’s email in the request and forwards the request.
A mail will be sent to both victim and attacker email and attacker resets the account password with the link he got which leads to account takeover.

Timeline:
Bug Reported: 3rd November 2019
Bug Triaged: 4th November 2019
Bounty Awarded: 3000$ 🤑🤑

Press enter or click to view image in full size

Account Takeover Scenario #2:

So this was my second account takeover reported immediately after the first one got awarded with a bounty. This bug category became my favorite and i started to look for account takeovers hereafter.

Get Vijaysimha Reddy Bathini’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So this scenario was like this,
The website had a forgot password functionality. So, whenever the user tries to reset his password. The user is asked to input the email address for the reset function. After giving the valid email id it gives us two options:

Reset via OTP sent on email and Reset via OTP sent on mobile.
So I tried with the first option and it was secure. I didn't find anything suspicious.
So next I tried with the second option i.e Reset via OTP sent on the mobile. I fired up my burp suite and captured the request, and there i found the data has been sent to the server in JSON format with two parameters mobile and token.

To my surprise, the token value was unique to the account. I tried changing the token parameter but I have been given an error. So I tried tampering the mobile number. As there was only token validation at the back-end. Then, I changed the mobile number from victim to attacker mobile number. To my surprise, the OTP got delivered to the attacker’s mobile number and the victim’s password got successfully changed thus leading to account takeover.

Exploit Scenario:

Attacker issues a forgot password request on the victim’s email and he has been given the two options whether to reset via email or mobile number.
The attacker selects the reset via the mobile option and captures the request.
The attacker changes the mobile number from victims to his mobile number and forwards the request.
The attacker will get the OTP of the victim and use that to reset the password of the victim leading to account takeover.

Timeline:
Bug Reported: 7th November 2019
Bug Triaged: 7th November 2019
Bounty Awarded: 2000$

Press enter or click to view image in full size

I have submitted quite a few account takeover write-ups. As the content might get large I will be writing in the next blog.

I hope you like it. I request you to like this which encourages me to write more and more write-ups like this.

Bug Bounty Tip:

Thanks to Bhavesh Thakur for sharing the below scenario:

Intercept the request and put email:victim mail%0d%0acc:hacker mail id. The server sends an email with CC attacker email.

LinkedIn URL: https://www.linkedin.com/in/bhavesh-thakur-73b62723

Thank You!
~Vijaysimha(a.k.a FATRAT)

Follow me on Twitter and LinkedIn:

https://twitter.com/fatrat_v2

Buy me a Coffee: https://www.buymeacoffee.com/fatrat

vijaysimha reddy - Engineer - Vasavi College of Engg | LinkedIn
View vijaysimha reddy's profile on LinkedIn, the world's largest professional community. vijaysimha has 1 job listed on…

www.linkedin.com
