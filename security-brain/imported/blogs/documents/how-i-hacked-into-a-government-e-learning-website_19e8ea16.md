---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-26_how-i-hacked-into-a-government-e-learning-website.md
original_filename: 2022-11-26_how-i-hacked-into-a-government-e-learning-website.md
title: How I hacked into a government e-learning website
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: 19e8ea16738cf31893982a3eeb1646cf32d63b01d75afe63fe728005d1210509
text_sha256: 5865c2bb78ade496062e167abcca687e300465842d6a4b1025d5a7777ea57a74
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked into a government e-learning website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-26_how-i-hacked-into-a-government-e-learning-website.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `19e8ea16738cf31893982a3eeb1646cf32d63b01d75afe63fe728005d1210509`
- Text SHA256: `5865c2bb78ade496062e167abcca687e300465842d6a4b1025d5a7777ea57a74`


## Content

---
title: "How I hacked into a government e-learning website"
url: "https://iamgk808.medium.com/how-i-hacked-into-a-government-e-learning-website-ce8da8fb4ccc"
authors: ["iamgk808 (@iamgk808)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2022-11-26"
added_date: "2022-11-26"
source: "pentester.land/writeups.json"
original_index: 1859
scraped_via: "browseros"
---

# How I hacked into a government e-learning website

How I hacked into a government e-learning website
DATE: 07/11/2022
iamgk808
Follow
4 min read
·
Nov 26, 2022

245

1

WHOAMI

My name is Ganesh Kumar AKA iamgk808, a cybersecurity enthusiast and bug hunter. Handles — Twitter, Linkedin

LET THE STORY BEGINS

One Day my father asked me to log in to a government e-learning website to finish some tasks, that all teachers are required to complete within two days, so I log into my father's account & finished the tasks.

Later my father's friend also wants to finish the task so he gave me the e-mail ID and the password I tried to log in with the credential but it showed “enter the correct credential” then I asked him if the credential is correct or not and he told me that he did not create the account someone else has created the account for him with the wrong information.

So I have to find a way to log in to the account !!!

GOAL: Log into the government e-learning website and finish the task

father’s friend given details :
email id - ######@gmail.com
password - ###### (wrong)
mobile no- ######## (wrong)
UDISE Code- #########

Attempt -1
Login

With the given email id and password tried to log in, and the UI shows “enter the correct credential”

Press enter or click to view image in full size

The burp suite response shows “user not found”, I thought both the email id & password is incorrect, so this attempt is failed

Attempt -2
Password reset

So I tried to reset the password but it asks a mobile number, not an email id, then I entered the mobile number and the UI shows “oops something went wrong”.

Press enter or click to view image in full size

The burp suite response shows “user not found”, Thus the mobile number is also incorrect, so this attempt also failed

Attempt -3
REGISTER

Asks for a UDISE Code (a code given to schools to register an account), entered the code and the UI shows “Another Teacher is already registered in the given School”.

Fortunately, they have given the correct code. The burp suite response shows the full details like email, user id, mobile number, etc...

Press enter or click to view image in full size

From this attempt 3, we got useful information like email, mobile number, and user id.

Get iamgk808’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With this mobile number, I tried Attempt -2 (password reset), and the OTP has sent successfully, I asked my father’s friend whether he got the OTP, and he said he did not get the OTP so I asked does the mobile number belongs to you he said it is someone else number and not his number.

so the only way here is to call the unknown number and ask for the OTP but it is not practically possible.

Attempt -4

An idea struck my mind, so I log in with my father's valid credentials and check for any functionality or request to change a password.

Luckily I found a password reset request that only requires a valid user id and does not check the old password, From Attempt -3 I already got the user id so I changed the password successfully.

NOTE: If anyone knows what encryption is used to encode the password comment below.

Press enter or click to view image in full size
Goal reached :)

Finally, I logged into the account and finished the task.

Bugs found during this process:
IDOR — able to change anyone's password (Critical)
IDOR — able to see other teacher's P1 information by simply changing the id value (Critical)
IDOR — able to see other student's P1 information by simply changing the id value (Critical)
From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
