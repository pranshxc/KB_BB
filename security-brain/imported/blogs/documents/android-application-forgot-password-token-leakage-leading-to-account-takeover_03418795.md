---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-19_android-application-forgot-password-token-leakage-leading-to-account-takeover.md
original_filename: 2022-09-19_android-application-forgot-password-token-leakage-leading-to-account-takeover.md
title: Android Application Forgot Password Token Leakage Leading to Account Takeover
category: documents
detected_topics:
- password-reset
- mobile-security
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- password-reset
- mobile-security
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 0341879527e301e8a81364c2728caf9c8ec1d1183e41c45f208492dd02f5a9b0
text_sha256: dba16e57273b1b8149fc7acc52372a57fa403317fc880cb17ffd4b6855bbe237
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Android Application Forgot Password Token Leakage Leading to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-19_android-application-forgot-password-token-leakage-leading-to-account-takeover.md
- Source Type: markdown
- Detected Topics: password-reset, mobile-security, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `0341879527e301e8a81364c2728caf9c8ec1d1183e41c45f208492dd02f5a9b0`
- Text SHA256: `dba16e57273b1b8149fc7acc52372a57fa403317fc880cb17ffd4b6855bbe237`


## Content

---
title: "Android Application Forgot Password Token Leakage Leading to Account Takeover"
url: "https://medium.com/@cyberali/android-application-forgot-password-token-leakage-leading-to-account-takeover-8a0b28296531"
authors: ["Cyberali"]
bugs: ["Information disclosure", "Password reset", "Account takeover", "Android"]
publication_date: "2022-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2153
scraped_via: "browseros"
---

# Android Application Forgot Password Token Leakage Leading to Account Takeover

Android Application Forgot Password Token Leakage Leading to Account Takeover
Cyberali
Follow
2 min read
·
Sep 19, 2022

89

Hello Hunter,

I hope you all are doing well. I am back to put one of my finding’s in words. It was my first android bug hunting target. I was really excited and motivated as my first report was rejected due to low severity. I was just understanding the flow of this application and going through recon process. After capturing and analyzing some functionalities, I came across the forgot password endpoint of the target.

Authentication process protects from unauthorized access of the resources. Unfortunately the developer forgot to utilize and implement the features behind the authentication layer. Normally the reset password token is handled on the backend by making an API call to the backend to create a token, saving it in the database, assigning it to the user and sending via email.

In the target app, the application is showing abnormal behavior. After entering the email and Clicking on reset password the token of reset password can be easily seen disclosed in response. It means that the application is handling the reset token on frontend which is leading to leak in response and complete compromise of account.

Get Cyberali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to Reproduce:

Register on the target application and Log Out.
Navigate to forgot password form.
Enter the Registered Email, Turn on the burp suite proxy and click on submit.
Capture the request and Right Click and send the request to repeater.
Click on Send. BOOOOM! You will see the token in the response.

No effort just send the request to repeater.

Impact:

Attackers can easily take over any user’s account by just knowing his Email which is available to the public easily. It is a critical vulnerability because the goal of every attacker is to take over the user’s account. After utilizing the leaked reset token, he can change the password of any user and enjoy the Purchases Plans. The attacker can also get unauthorized access to the web application after changing the password from the mobile application. This Vulnerability is affecting users’ accounts on mobile and web. There are options to connect to a Facebook, apple or google account, an attacker can misuse it or attach his own account. Complete compromise of victims account making this vulnerability very critical because account takeover is one of the main goal of every attacker.

Bounty:

Press enter or click to view image in full size

Just Chill….Don’t forget the coffee cup…

Thank you!
