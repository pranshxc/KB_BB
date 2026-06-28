---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-08_bugbounty-how-i-cracked-2fa-two-factor-authentication-with-simple-factor-brute-f.md
original_filename: 2019-11-08_bugbounty-how-i-cracked-2fa-two-factor-authentication-with-simple-factor-brute-f.md
title: 'BugBounty: How I Cracked 2FA (Two-Factor Authentication) with Simple Factor
  Brute-force !!! 😎'
category: documents
detected_topics:
- mfa
- rate-limit
- otp
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- mfa
- rate-limit
- otp
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: 9a3ab1809193ba9fd5a16d4ea42e07ff6f13fbc571fda12e42a9f035ee1e4be2
text_sha256: 153f1a7f3efccb21e94bff14309129128797a3d5d8c01190987979ab9db8e868
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# BugBounty: How I Cracked 2FA (Two-Factor Authentication) with Simple Factor Brute-force !!! 😎

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-08_bugbounty-how-i-cracked-2fa-two-factor-authentication-with-simple-factor-brute-f.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, otp, sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `9a3ab1809193ba9fd5a16d4ea42e07ff6f13fbc571fda12e42a9f035ee1e4be2`
- Text SHA256: `153f1a7f3efccb21e94bff14309129128797a3d5d8c01190987979ab9db8e868`


## Content

---
title: "BugBounty: How I Cracked 2FA (Two-Factor Authentication) with Simple Factor Brute-force !!! 😎"
url: "https://medium.com/clouddevops/bugbounty-how-i-cracked-2fa-two-factor-authentication-with-simple-factor-brute-force-a1c0f3a2f1b4"
authors: ["Akash Agrawal (@akashmagrawal)"]
bugs: ["2FA / MFA bypass", "Lack of rate limiting"]
publication_date: "2019-11-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4954
scraped_via: "browseros"
---

# BugBounty: How I Cracked 2FA (Two-Factor Authentication) with Simple Factor Brute-force !!! 😎

BugBounty: How I Cracked 2FA (Two-Factor Authentication) with Simple Factor Brute-force !!! 😎
Akash Agrawal
Follow
3 min read
·
Nov 9, 2019

251

2

Today I would like to share how I was able to bypass OTP (One Time Password) login with a simple brute force attack on India’s biggest travel service provider. OTP is treated as an additional measure for security termed as 2FA. For those who don't know about, what is 2FA?

Two-factor authentication (2FA), sometimes referred to as two-step verification or dual factor authentication, is a security process in which the user provides two different authentication factors to verify themselves to better protect both the user’s credentials and the resources the user can access.

Generally, OTP is a combination of 4 digits starting from 0000 to 9999. If we count there 10,000 combinations. In the age of powerful computer 10,000 combinations take only a few minutes to process. If OTP verification is not properly managed, anyone can bypass this with a simple brute force.

Why I was able to bypass the 2FA?

No rate limiting on an unsuccessful attempt
No new OTP policy on X unsuccessful attempt

Few prerequisites:

Web Browser
Burp Suite

Now let's see how I was able to bypass the 2FA with burp suite:-

Get Akash Agrawal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step 01: Logged into the website using the mobile number and entered the wrong OTP to intercept on burp suite

Press enter or click to view image in full size
Pannel to enter the OTP received on the Mobile Number
Press enter or click to view image in full size
Intercept the Verify OTP API call on Burp Suite

Step 02: Sending the verifyOTP API call to the intruder.

Press enter or click to view image in full size
Image showing the Dialogue box to send intruder.
Press enter or click to view image in full size
Intruder Screen Burp Suite

Step 03: Selecting the OTP placeholder and add it for simple brute force.

Press enter or click to view image in full size
Intruder screen with OTP placeholder selected for brute force

Step 04: Select the Payload tab, changed the payload type to Numbers and change the payload options as desired and clicked on the attack.

Press enter or click to view image in full size
Payload Screen: For setting payload desired options
Press enter or click to view image in full size
Brute Force In Progress

Step 05: As the brute force was in progress I could see length for one of the OTP value is changed from 617 to 2250. Lets check:

Press enter or click to view image in full size
OTP Response

Step 06: Boom !!! I was able to get the login token and was able to log in.

Press enter or click to view image in full size
Details of successful login

Hence, The simple brute force was successful.
