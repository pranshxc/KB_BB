---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-09_journey-from-low-to-critical-bug-.md
original_filename: 2020-07-09_journey-from-low-to-critical-bug-.md
title: Journey from low to critical bug $$$
category: documents
detected_topics:
- mobile-security
- idor
- command-injection
- password-reset
tags:
- imported
- documents
- mobile-security
- idor
- command-injection
- password-reset
language: en
raw_sha256: da1d9881b558b24fd5130241b307941863ae1751f1fe628bb22318e1007dc849
text_sha256: baa7c471d0aba90bc5583cf5262c0c34fae39f892a772451e4ae7759f133a358
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Journey from low to critical bug $$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-09_journey-from-low-to-critical-bug-.md
- Source Type: markdown
- Detected Topics: mobile-security, idor, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `da1d9881b558b24fd5130241b307941863ae1751f1fe628bb22318e1007dc849`
- Text SHA256: `baa7c471d0aba90bc5583cf5262c0c34fae39f892a772451e4ae7759f133a358`


## Content

---
title: "Journey from low to critical bug $$$"
url: "https://medium.com/@dheerajkmadhukar/journey-from-low-to-critical-bug-2ab98db2eec1"
authors: ["Dheeraj Madhukar (@Dheerajmadhukar)"]
bugs: ["IDOR"]
publication_date: "2020-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4426
scraped_via: "browseros"
---

# Journey from low to critical bug $$$

Journey from low to critical bug $$$
Dheeraj Madhukar
Follow
3 min read
·
Jul 9, 2020

206

Android insecure IPC leads to Full Account Takeover via IDOR

Press enter or click to view image in full size

Hello folks,

I’m Dheeraj Madhukar, a working professional. After been working for a long time for enormous government as well as private organizations in the field of Cyber Security, VAPT & Forensics.

I started around 7.5 years ago, during this phase i never tried any Bug Bounty platform, until now. So i decided to share my experience with you !

In this writeup I am sharing few of the scenarios which I reported to a private program. Let’s have two scenarios:

Scenario#1

L
et’s consider the org name as “example.com”. So i decided to start with Android App. First, i used apktool to decompile the app to analyse AndroidManifest.xml file and then searched for activities in which
‘ exported=”true” ’. I found one:

Press enter or click to view image in full size

As we can see this activity is called as “ForgetConfirmPassword” that means we can directly call this activity to bypass the forgot password process which will lead us to Insecure IPC [ Inter Process Communication ] bug in the Android App.

Insecure IPC [ Inter Process Communication ] : Android Mobile communication is possible by using internal communication mechanism and sending intents to each other. Intents can be sent by an invalid caller i.e. a malicious app, which can be abused to cause your application to perform sensitive actions without your control.

PoC

Get Dheeraj Madhukar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

adb shell am start -W -n com.exmaple.ForgetConfirmPassword

Press enter or click to view image in full size

Let’s dig more !!!

Scenario#2

N

ow… Let’s turn on the burp suite and intercept the mobiles’ traffic. So i just put random password and click on “Reset Password”. Here is the request in burp:

Press enter or click to view image in full size

As we can see there is only one JSON parameter called “password”, so i sent the request to repeater and put another JSON parameter “email” with my test email address and Sent. BOOM !!! It looks like this:

Press enter or click to view image in full size

Now i can reset any users’ password by using the same request, which will lead me to Full ATO [ Account takeover ].

I hope you get some motivation to do bug bounties and See you again in next writeup.

Twitter profile: @Dheerajmadhukar

Linkedin profile: @dheerajtechnolegends
