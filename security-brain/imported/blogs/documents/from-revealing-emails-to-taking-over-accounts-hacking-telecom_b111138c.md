---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-13_from-revealing-emails-to-taking-over-accounts-hacking-telecom.md
original_filename: 2023-08-13_from-revealing-emails-to-taking-over-accounts-hacking-telecom.md
title: From Revealing Emails to Taking Over Accounts (Hacking Telecom)
category: documents
detected_topics:
- password-reset
- access-control
- command-injection
- otp
- rate-limit
- supply-chain
tags:
- imported
- documents
- password-reset
- access-control
- command-injection
- otp
- rate-limit
- supply-chain
language: en
raw_sha256: b111138c65d9708a3a20674b5a97696fa5da65fa7b3cca139e091dd9f9834bf3
text_sha256: 75b5bb79ead46a4046023350f19e95c0c48545d830f7e180046c1653c3e68163
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# From Revealing Emails to Taking Over Accounts (Hacking Telecom)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-13_from-revealing-emails-to-taking-over-accounts-hacking-telecom.md
- Source Type: markdown
- Detected Topics: password-reset, access-control, command-injection, otp, rate-limit, supply-chain
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `b111138c65d9708a3a20674b5a97696fa5da65fa7b3cca139e091dd9f9834bf3`
- Text SHA256: `75b5bb79ead46a4046023350f19e95c0c48545d830f7e180046c1653c3e68163`


## Content

---
title: "From Revealing Emails to Taking Over Accounts (Hacking Telecom)"
url: "https://ahmdhalabi.medium.com/from-revealing-emails-to-taking-over-accounts-hacking-telecom-ead1fcbffc32"
authors: ["Ahmad Halabi (@Ahmad_Halabi_)"]
bugs: ["OTP bypass", "Password reset", "HTTP response manipulation", "Account takeover"]
publication_date: "2023-08-13"
added_date: "2023-08-14"
source: "pentester.land/writeups.json"
original_index: 858
scraped_via: "browseros"
---

# From Revealing Emails to Taking Over Accounts (Hacking Telecom)

Top highlight

From Revealing Emails to Taking Over Accounts (Hacking Telecom)
Ahmad Halabi
Follow
4 min read
·
Aug 12, 2023

426

4

Press enter or click to view image in full size

بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

Hello,

My name is Ahmad Halabi.

Working at Resecurity — A Cyber Security Intelligence Company protecting Fortune 500 against threats of all types.

Part of what we do via our Hunter Unit Operations is investigate and identify new zero days, attacks and techniques that allow threat actors to cause massive data breaches and infections.

In this article, I will explain how I found a bug that allowed me to disclose all emails related to users of a Huge Telecom company and take over all their accounts too.

Exploiting “Forget Password” Feature ::

Usually if you forgot your password, you can recover it by sending a recovery code to your Email or Phone Number.

First, the application forces you to add your phone number in the “Forgot Login Details” section. So I added Victim Phone Number.

Press enter or click to view image in full size
Adding victim Phone Number in Forgot password page

Then the application gives you two choices to send the PIN code either to the email or the Phone Number.

Press enter or click to view image in full size
Send the PIN code to the victim number or email

We notice that the Phone Number is hidden as well as the Email.

In our case, we already have victim phone number and we want to reveal his email.

We don’t care where the code will be sent because we will bypass it later, so we can send it to the number or email.

Press enter or click to view image in full size
Verification PIN Code sent

After clicking on Send PIN button, we notice that the code is sent. We will not use the code.

Exploiting the Verification PIN Process ::

By using Response Manipulation technique to manipulate the wrong response of the code request and replace it with a Correct response.

Press enter or click to view image in full size
Adding random PIN Code

I added random PIN Code 1111 and intercepted the request via burp.

Press enter or click to view image in full size
Verify PIN Code Request

We notice in the above request that they are splitting the 4 digits code into 4 pin inputs (pin1, pin2, pin3, pin4) and into 3 normal pin inputs. They did the splitting technique to protect against Brute forcing the PIN Code.

Get Ahmad Halabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I didn’t do any brute force when I saw the above request. Instead, I intercepted the response as shown in the picture below.

Press enter or click to view image in full size
Intercept the Response of the PIN Code Request

After sending the request, I monitored its Response and found the below response showing the status code “700” and operation “verify OTP” meaning that the verification request failed as the OTP was wrong.

Press enter or click to view image in full size
Wrong OTP Code

I simply manipulated the response by replacing {"code":"700","operation":"VERIFYOTP"} with {"code":"200"} and forwarded the request.

Changing the wrong response with a true one

After forwarding the request, I got redirected to the Change Password Page revealing the Email address and confirming the PIN Code verification.

Press enter or click to view image in full size
Your username is (Email Disclosed)

After I tried to add new password, I got an Account Takeover.

Press enter or click to view image in full size

Impact ::

I was able to reveal the user emails found in the Database of the Telecom Company. Threat Actors can easily:
Collect all the Phone Numbers related to this Telecom.
Automate this Vulnerability to exploit it on all the Collected Phone Numbers.
Sell all the disclosed private emails on the Dark Web.
Use them in Massive Phishing Campaigns.

2. I was able to change the password of the accounts in the Telecom Company. This means obtaining Full Account Takeover that could have easily lead to:

Financial Loss (of users).
Huge Packages Loss.

Conclusion ::

In this case, the response manipulation technique allowed me not only to reveal the Emails but it also redirected me to the Change Password page allowing me to take over any account that I target.

Remediation ::

Fixing the Response manipulation bug was not enough, Authorization problem on changing password had to be fixed too so it won’t get bypassed.

Hope you enjoyed reading!

I created private bug bounty course to help struggled hunters find valid bugs and earn bounties.

If you are struggling in finding valid bugs or earning enough bounties, you just need to enroll and your mindset about approaching bug bounty hunting will improve.

Check Student bounties and feedbacks and enroll now: https://ahmadhalabi.net/course

Press enter or click to view image in full size

You can follow me on: LinkedIn / Twitter / Instagram / My Website

Press enter or click to view image in full size
Press enter or click to view image in full size

Kind Regards.
