---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-12_account-takeover-via-reset-password-worth-2000.md
original_filename: 2021-03-12_account-takeover-via-reset-password-worth-2000.md
title: Account Takeover Via Reset Password Worth 2000$
category: documents
detected_topics:
- password-reset
- oauth
- ssrf
- command-injection
- otp
- csrf
tags:
- imported
- documents
- password-reset
- oauth
- ssrf
- command-injection
- otp
- csrf
language: en
raw_sha256: 06c625bf8f0c54e9cbe9b36b3ac488458c62a7a5e92a12b3b596ee6b3d7828e4
text_sha256: 0e5e1380fd3b345cfb097ba8b8b5685825037828a42f6a02266d37409eb5b460
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover Via Reset Password Worth 2000$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-12_account-takeover-via-reset-password-worth-2000.md
- Source Type: markdown
- Detected Topics: password-reset, oauth, ssrf, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `06c625bf8f0c54e9cbe9b36b3ac488458c62a7a5e92a12b3b596ee6b3d7828e4`
- Text SHA256: `0e5e1380fd3b345cfb097ba8b8b5685825037828a42f6a02266d37409eb5b460`


## Content

---
title: "Account Takeover Via Reset Password Worth 2000$"
url: "https://ashutoshmishra00x0.medium.com/account-takeover-via-reset-password-worth-2000-de085851d81d"
authors: ["Ashutosh mishra (@ashutoshmish_ra)"]
bugs: ["Password reset", "Account takeover"]
bounty: "2,000"
publication_date: "2021-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3822
scraped_via: "browseros"
---

# Account Takeover Via Reset Password Worth 2000$

Ashutosh mishra
 highlighted

Account Takeover Via Reset Password Worth 2000$
Ashutosh mishra
Follow
4 min read
·
Mar 12, 2021

2.3K

5

To People who don’t know me , I Ashutosh Mishra , 3rd Year Btech Computer Science Student, A cybersecurity Researcher by day and bug hunter by night,Mainly love to find Business logic bugs(Account Takeover and SSRF).

Press enter or click to view image in full size
Account Takeover by #ashutoshmishra

Hello everyone this is my second account takeover write up , hope all you have read the first one, if not you can read here. This account takeover was done Three months before on december 2020 , but the response and award came on Feb 2021

Lets Begin , I was searching for a financial websites to hunt , after searching for good time on google , I got a website which was running the bug bounty program . for security purposes lets take the website name redacted.com

This time before starting the burp suite , I started to understand the application flow as the normal user, then I started to spider the website using burp suite , I was searching for some endpoints to find SSRF , but after hunting 3 Hours I could not find any endpoints for successful ssrf.

The next thing which come to my mind is going for the registration and the login page of the website, I tried to put the collaborator link in every request for blind ssrf ,but no success.

As, I am a guy who always look for the ssrf and account takeover , spending around 3 days on the target , got some little hanging fruits, but i was not happy to report , then I started to hunt on login page ,there was two option to login , normal email and password and other was through the oauth , I tried to find oauth misconfiguration , but developers were quite good in implementing the oauth, now next try was to login through email and password with response manipulation , but no success.

It was the time where I was tired and was going to sleep at 2 am , but my eyes went on reset password, so i thought to give a last try on this mechanism,

The reset password was implemented by sending the email instructions to reset password, while requesting the reset password I intercepted the request to response hoping to get the reset token in response but got nothing.

Get Ashutosh mishra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so after I went to my mail , and opened up the reset link and tried to intercept the request while changing the password , i saw the following request

Press enter or click to view image in full size

After observing the following request two things came to my mind , one no csrf protection was implemented in the request, but I thought the authenticity_token might be chained with email address(so there will be no use of csrf) so to checked whether the token and email are linked or not , I changed the mail from ando@yopmail.com to victim@email.com and suddenly something happens , which made me shocked.

account takeover by #ashutoshmishra

There was a notification on right corner , claiming that password has been reseted . To actually confirm it I tried to enter the victim email address and my password and Boom Boom we are inside the victim account , so there was no chaining of authentication token with email address which lead me to account takeover of anyone

Timeline:
Bug Reported: 8 December 2020
Bug Triaged: 11 February 2021
Bounty Rewarded: $2000

Tip: Try to checked token whether it is chained to accounts or not by changing the parameter value

Feel Free to message on Instagram any queries related to bug bounty

PROOF:

Press enter or click to view image in full size
account takeover by ashutosh mishra

Well if you love this writeup drop a clap 👏(50X), let’s connect then:

Twitter: https://twitter.com/ashutoshmish_ra

Instagram: https://www.instagram.com/i.m.ashutoshmishra/

LinkedIn: https://www.linkedin.com/in/ashutosh-mishra-148864172/
