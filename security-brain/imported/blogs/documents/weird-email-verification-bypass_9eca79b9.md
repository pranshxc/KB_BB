---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-28_weird-email-verification-bypass.md
original_filename: 2022-05-28_weird-email-verification-bypass.md
title: Weird Email Verification Bypass
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: 9eca79b9baaa131a7c6627fb3080866e5cebbafc51a877807d6c3f687886c0c1
text_sha256: 5a9fff3ac9cb4aa2296cdc7549648b1a824c133d90ca596d5fad2285c1656f08
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Weird Email Verification Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-28_weird-email-verification-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `9eca79b9baaa131a7c6627fb3080866e5cebbafc51a877807d6c3f687886c0c1`
- Text SHA256: `5a9fff3ac9cb4aa2296cdc7549648b1a824c133d90ca596d5fad2285c1656f08`


## Content

---
title: "Weird Email Verification Bypass"
url: "https://medium.com/@vaibhavatkale/weird-email-verification-bypass-96c793c36d7e"
authors: ["Vaibhav Atkale"]
bugs: ["Email verification bypass"]
publication_date: "2022-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2601
scraped_via: "browseros"
---

# Weird Email Verification Bypass

Weird Email Verification Bypass
Vaibhav Atkale
Follow
3 min read
·
May 28, 2022

180

4

Hello you all OP hacker’s…!!!

Press enter or click to view image in full size

I’m Vaibhav Atkale, sharing the writeup explaining how i managed to bypass the email verification implementation. So here we go..!!!

By obvious reason i cannot reveal the target. Lets assume our target as target.com

So basically target.com is kinda eCommerce website. Where user can sign up using his email address however in order to access the account, it is must for user to verify his email using the link sent to their email address.

Whenever i start hunting on the program, i initially check authentication issues. I followed the below steps:

I created 2 accounts lets say test1@gmail.com and test2@gmail.com
Observed the email verification link sent to Email address: For Eg. for user test1@gmail.com -> https://target.com/o/blah/blah?user_id=1028356&confirm_key=Token1
test2@gmail.com -> https://target.com/o/blah/blah?user_id=1028357&confirm_key=Token2
If we observed the above email verification link, it can be seen that to crack the email verification link we need 2 parameter user_id and confirm_key.
By analyzing the response to user creation request carefully i found that the user_id was getting leaked in response header.
Our next task is to crack the confirm_key parameter, i followed different approaches to see if the key is crackable if its md5 encrypted or somehow if it guessable or if it has to do something with timestamp , tried comparing Token1 and Token2, initially i thought there will be chance that only some part of the token is different as i created account with almost similar email address i.e. test1@gmail.com & test2@gmail.com but both were completely different, no chance of guessing.

Took a break and came back later night

This time i created multiple(5–6) accounts observed all the email verification links by copying all of them in the notepad to my surprise those were as follows

https://target.com/o/blah/blah?user_id=1028361&confirm_key=Token1
https://target.com/o/blah/blah?user_id=1028362&confirm_key=Token2
https://target.com/o/blah/blah?user_id=1028363&confirm_key=Token1
https://target.com/o/blah/blah?user_id=1028364&confirm_key=Token2
https://target.com/o/blah/blah?user_id=1028365&confirm_key=Token1
https://target.com/o/blah/blah?user_id=1028366&confirm_key=Token2

If you see the above email verification links one can see that the application is generating only two confirm_key values either Token1 and Token2. And we already got the user_id value in user creation request’s response.

Get Vaibhav Atkale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So that means we have everything for crack the email verification link. I quickly created an account with programs domain name (i.e. user@target.com) to check if i can bypass the email verification and maybe i will be able to access additional internal tabs.

So final steps to reproduce vulnerability as below:

Create an account with email address user@target.com
Note down the user_id parameter from the response for eg. lets say it is 102838
Now try hitting below URL’s https://target.com/o/blah/blah?user_id=102838&confirm_key=Token1
If the above doesn’t work try the other one https://target.com/o/blah/blah?user_id=102838&confirm_key=Token2
So either of the above two will surely work as a result email verification will be done and we logged into the application using the email address user@target.com even though we don’t have access to that email address.
However there were no additional functionalities accessible to users who logged in with program domain email id i.e. user@target.com

Any way i reported the issue as email verification bypass . Team was good enough to categorize it as Account Takeover and triaged it as high severity.

As i always say observation is the key. Make sure to have a look on all the responses and try creating multiple accounts(atleast 6–7) whenever testing for email verification bugs, we never know the implementation..

Disclosure Timelines

14th November 2020: Vulnerability Reported

16th November 2020: Triaged and marked it as high

16th November 2020: Retested and Fixed

I hope you enjoyed the writeup and please feel free to share your feedback , criticism etc. Stay tuned for next writeup.

You can connect me on linkedin
