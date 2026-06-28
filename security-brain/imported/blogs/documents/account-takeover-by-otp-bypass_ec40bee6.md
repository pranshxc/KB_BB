---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-19_account-takeover-by-otp-bypass.md
original_filename: 2022-06-19_account-takeover-by-otp-bypass.md
title: Account Takeover by OTP bypass
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: ec40bee6be6eaa9d7041b1c8414fae2749ecdce4352e89dcbc8295516b78a7d0
text_sha256: 148a67ecb07273189c512840d635bd9bbfe000900f8958f19c71fdf53bddce3d
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover by OTP bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-19_account-takeover-by-otp-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `ec40bee6be6eaa9d7041b1c8414fae2749ecdce4352e89dcbc8295516b78a7d0`
- Text SHA256: `148a67ecb07273189c512840d635bd9bbfe000900f8958f19c71fdf53bddce3d`


## Content

---
title: "Account Takeover by OTP bypass"
url: "https://codewithvamp.medium.com/account-takeover-by-otp-bypass-ec0cff67f516"
authors: ["Vaibhav Kumar Srivastava"]
bugs: ["Information disclosure", "Client-side enforcement of server-side security", "OTP bypass", "Account takeover"]
publication_date: "2022-06-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2535
scraped_via: "browseros"
---

# Account Takeover by OTP bypass

Account Takeover by OTP bypass
Vaibhav Kumar Srivastava
Follow
3 min read
·
Jun 19, 2022

453

3

Hey everyone! This bypass is little bit interesting and you will get to learn a lot hopefully.

Press enter or click to view image in full size

So I was going through this website which actually deals with teacher’s login and education stuff (Government website). Let’s call this website “example.com”.

Press enter or click to view image in full size

In-order to login as a teacher you need to give the registered mobile number and then the example.com will verify it. I have members in my family who are in education sector so I tried with their number and I was able to login after complete verification.

Get Vaibhav Kumar Srivastava’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I thought let’s try to bypass this verification process. Fortunately, I got a contact number in the script of the web application (another Flaw!==> hidden treasure).

Press enter or click to view image in full size

I clicked on teacher’s login and entered the contact number that I found in the script(say Victim’s number).

Press enter or click to view image in full size

The moment I clicked on “verify” button, a new screen to send the OTP popped on screen (If I enter my mobile number and click verify then it will not allow me to proceed because I’m not registered as a teacher in this portal) Now If I click on send OTP then the OTP will got to victim’s number but I won’t be able to see it.

Press enter or click to view image in full size

I tried intercepting the request in Burp to see if the response is leaking the OTP or not, but no luck there. Then I opened the inspect element for the same page and investigated the mobile number field. As it can be seen in screenshot it is showing the mobile number field is “disabled”. I changed the status to “enabled” and I was able to edit the mobile number.

Press enter or click to view image in full size

At this point of time, I am already verified with the Victim’s mobile number the only thing I need is OTP to proceed further. After I enabled the mobile number field I changed the victim’s mobile number with my mobile number and hit on “Send OTP” button.

Press enter or click to view image in full size

Guess what!! I received the OTP on my number. Quickly, I entered the OTP.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

The moment I entered the OTP, got logged in into the victim’s account with complete access.

Press enter or click to view image in full size
Press enter or click to view image in full size

Issues with the web application:

1- The mobile number is exposed in the script

2- The “verify” process is validating the mobile number on server side but the “Send OTP” is not validating which led me to get the OTP on my number.

3- Further I tried and the application was also vulnerable to OTP bruteforcing.

Quickly made the POC and reported it to NCIIPC, received the usual response. Happy to investigate and secure the application.

Stay Curious Stay Protected!!
