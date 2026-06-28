---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-21_how-i-turned-0000-into-600-phone-verification-bypass.md
original_filename: 2021-05-21_how-i-turned-0000-into-600-phone-verification-bypass.md
title: 'How I turned 0000 into $600: Phone Verification Bypass'
category: documents
detected_topics:
- otp
- command-injection
tags:
- imported
- documents
- otp
- command-injection
language: en
raw_sha256: 9a7280a343a01e5f7f99202c4d2daa050dfc7ae4fa92bdfe766681a19b4f3793
text_sha256: adeaa5094b61d86b3848919d7d84768bf41f6e06c229f7e9e5e9b640ebc2ae1a
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I turned 0000 into $600: Phone Verification Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-21_how-i-turned-0000-into-600-phone-verification-bypass.md
- Source Type: markdown
- Detected Topics: otp, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `9a7280a343a01e5f7f99202c4d2daa050dfc7ae4fa92bdfe766681a19b4f3793`
- Text SHA256: `adeaa5094b61d86b3848919d7d84768bf41f6e06c229f7e9e5e9b640ebc2ae1a`


## Content

---
title: "How I turned 0000 into $600: Phone Verification Bypass"
url: "https://shrirangdiwakar.medium.com/how-i-turned-0000-into-600-phone-verification-bypass-b1c0f6eb568e"
authors: ["Shrirang Diwakar"]
bugs: ["OTP bypass"]
bounty: "600"
publication_date: "2021-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3632
scraped_via: "browseros"
---

# How I turned 0000 into $600: Phone Verification Bypass

How I turned 0000 into $600: Phone Verification Bypass
Shrirang Diwakar
Follow
3 min read
·
May 21, 2021

247

2

Hello Hunters, This is a Tale of how I decoded the Verification flow of a well-known web application & bypassed the Phone Verification process because of the Initial code set at the Backend ❤

Damn Excited! Can’t wait to share this…😍

Press enter or click to view image in full size
Let’s Begin

The Web Application was a Server Hosting Management System with 24x7 support, Datacentre facilities, etc. After creating an account, a server of the user’s choice is hosted which means a Resource was being utilized. However, the Unnecessary creation of accounts could lead to excessive exploitation of available resources.

For which, a Phone verification mechanism was implemented where the user has to enter the 4 digit code which was told, on a call received on the entered mobile number. And only upon entering the correct code, the user had access to the functionalities offered.

The Phone Verification mechanism looked like this,

Phone Verification mechanism
Here is the catch,

While testing, I had to create multiple accounts & going through this process seemed hectic so I tried to bypass this. So I started forming test cases for the inputs (phone number, verification code). Out of many test cases formed, this was the one that had a strong logic :

T
est Case: As you can see, the “Verification code” input is already placed without entering the phone number. The normal flow should have been, asking for the phone number first & then the verification code. But here, things seem different 🤷‍♀️

So What if I enter any value in the “Verification Code” input box before entering the phone number and click on “Verify Code”?🤔

What if the developer had set a variable at the backend that held some initial value before the user clicks on “Call me Now”?😮

Get Shrirang Diwakar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Going with the test case, I tried 1234, 1111, 8421, etc. but none of them worked. However, for 0000 the account got verified successfully meaning that the Phone verification was bypassed.

Account Verified Successfully
Steps Followed :
Create an account
A Phone verification mechanism was implemented and also the Verification Code was asked at the same time making it vulnerable to the test case. So without entering the Phone number, enter 0000 in the “Verification Code” input box.
Your Account will be verified successfully.

So my What ifs were correct which means that a variable was set at the backend that held an initial value 0000 before the user clicks on “Call me Now”!

Hence, the title: “How I turned 0000 into $600” 💯😎

Press enter or click to view image in full size

The Submission was triaged and I got rewarded with a $600 bounty under the P3 category 😁

That’s all for this article, I hope you guys enjoyed this form of learning ❤

Stay Safe 🤗

Follow my Instagram Creator account for more Bug Bounty & Ethical Hacking related content: https://www.instagram.com/shrirangdiwakar/ 😇

My LinkedIn: www.linkedin.com/in/shrirangdiwakar 🥰

Shower your love with the claps & share this with your friends ❣
