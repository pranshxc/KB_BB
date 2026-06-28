---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-12_cracking-the-2fa.md
original_filename: 2020-08-12_cracking-the-2fa.md
title: Cracking the 2FA
category: documents
detected_topics:
- mfa
- access-control
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- mfa
- access-control
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 08e770a5a7124b01c670f0d70bb3c4dfff538bb5b402065990a8850377fafd0f
text_sha256: dfe7426b15adef1e7f79cc39cba88d42159f9906bb07b287ffac7d5578d9b43b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Cracking the 2FA

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-12_cracking-the-2fa.md
- Source Type: markdown
- Detected Topics: mfa, access-control, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `08e770a5a7124b01c670f0d70bb3c4dfff538bb5b402065990a8850377fafd0f`
- Text SHA256: `dfe7426b15adef1e7f79cc39cba88d42159f9906bb07b287ffac7d5578d9b43b`


## Content

---
title: "Cracking the 2FA"
page_title: "Cracking The 2FA! Response Manipulation | Medium"
url: "https://medium.com/@rushikesh12gaikwad/cracking-the-2fa-215d24ccb29b"
authors: ["Rushikesh Gaikwad (@rsg_1212)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2020-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4330
scraped_via: "browseros"
---

# Cracking the 2FA

Cracking the 2FA
Rushikesh Gaikwad
Follow
4 min read
·
Aug 12, 2020

81

https://twitter.com/rushi_s_g

Alert First write up and also a beginner in the field accept some errors.

Testing a 2FA system is so much fun because we are breaching the stuff that was meant for additional security. And breaking them is so fun. You can skip to the part wherein the end I have explained the bug. Below are basics of response manipulation

What is Two-Factor Authorization?

Two-factor authentication (2FA) is the second layer of security to protect an account or system. Users must go through two layers of security before being granted access to an account or system.
What is Response Manipulation?

So normally what we do in burp suite is we browse through multiple requests and wherever we wanna tamper or change anything we do it and forward the request.

In Response Manipulation, we need to look for the appropriate request click on the “Action” button next to the “Intercept” button and select “Do Intercept” > “Response to Request”.

Press enter or click to view image in full size
How to get a response to the request

In Response manipulation, we tamper with the data that comes from the server.

Press enter or click to view image in full size
Response Manipulation

So let’s move on to see the bug,

It is a private program so let’s continue by saying it example.com and it had 2FA for account protection and it was well implemented no brute-force or whatever other methods, this also had a “use recovery codes option” and decided to test that and then I remembered reading some blogs which told that with burp suite we cannot just manipulate requests going to browser but also the incoming responses. So me being a noob still decided to try for this thing I read of response manipulation.

Get Rushikesh Gaikwad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps:-

1) Enable the 2FA for Attacker and Victims account, I used Google Authenticator and Microsoft Authenticator respectively just to keep no ties between them you know how the private programs are many questions and doubts from the teams.

2) Then Go to attackers’ account and log in and you’ll see “Please enter your 2FA code “ And also an option just below it “Use Recovery Code” (Codes provide as backups when you don’t have access to your authentication application or lost the device).

3)Select the “Use Recovery Code” Option and Now Enter a correct backup code for the Attacker’s account and intercept the request and get the response of that request. The Response has a session token for security purposes called _example_session=somenos. and string message showing correct code message.

The Response you get On Entering a correct recovery Code

4)Copy This response and keep it on a notepad.

4)Now, this is where the criticality of this bug is; Drop the Response what it does is stops the _example_session token going to websites server and the web application does not invalidate that token.

5)Now go to the victim’s account follow the same steps for that of attackers (Step 1,2,). But while performing Step 3 enter a wrong recovery code any number you want. Capture the Request and get its response. You’ll see that no session token provided to the error response that means we need a session token and there was an error string.

The response you get on entering the wrong recovery code

6)Now We had our attacker’s account response from server replace that response to the error response here for victim's account and …………

What Went Wrong?

1)Session token called _example_session= is not invalidated on the server-side when assigned someone and not got back.

2)Security is totally left on a string error message response I mean there was a security measure but due to invalidation of tokens, the security could be bypassed.

Conclusion

Always make sure Session tokens are properly validated and when sending a response back make sure it has some identity tokens attached to it.
