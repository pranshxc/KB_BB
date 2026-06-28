---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-08_information-disclosure-through-signup-endpoint.md
original_filename: 2021-01-08_information-disclosure-through-signup-endpoint.md
title: Information Disclosure through Signup Endpoint
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: adf56bb0e77e0275f71152f2a4f87648f8bdb25cf0a4680126f06ed41b41336c
text_sha256: c424de5ef983fd45b65e3250e912734e9b204665ab952cae06681b86902fd1c0
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Information Disclosure through Signup Endpoint

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-08_information-disclosure-through-signup-endpoint.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `adf56bb0e77e0275f71152f2a4f87648f8bdb25cf0a4680126f06ed41b41336c`
- Text SHA256: `c424de5ef983fd45b65e3250e912734e9b204665ab952cae06681b86902fd1c0`


## Content

---
title: "Information Disclosure through Signup Endpoint"
url: "https://orthonviper.medium.com/information-disclosure-through-signup-endpoint-86d2d66dfef1"
authors: ["Sunil Yedla (@sunilyedla2)"]
bugs: ["Information disclosure"]
publication_date: "2021-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4017
scraped_via: "browseros"
---

# Information Disclosure through Signup Endpoint

Top highlight

Information Disclosure through Signup Endpoint
Sunil Yedla
Follow
2 min read
·
Jan 6, 2021

510

3

Hello everyone, Hope you all are having a good day! Today’s Writeup explains how I was able to fetch any registered users FirstName, LastName and Phone number details through signup end-point, which ideally should not happen as per Targets workflow. Let’s get into the details : )

I found this target in Bugcrowd, let’s call this domain as: <redacted>.com. Since the target does not have wide scope I directly landed on signup and started checking the functionalities. Later and went ahead and created a new account and landed on Dashboard page. I found couple of bugs which were falling under P4 severity, so hoping to find any cool bug. Then suddenly this writeup I read a week ago flashed in my mind.

Always be Active and Learn from others

This Writeup talks about, when there is no proper validation, if an attacker signup with already registered victims email by giving a new password, that will change the password of existing victims account leading to Full Account Takeover. I got curious and immediately logged out of my account and proceeded to create new account page. For creating a new account user should first give email Id value.

In the background website analyses if given email ID is registered or not. Here in my cases, After entering registered Email Id, I’ve got an error response like this: “You already have a <redacted> account. Please continue by entering your <redacted> password below.” All my hopes are gone.

But then I thought why not check the server request. So I quickly setup Burp suite, signed up again with same email and entered a Random password. I was surprised to see the server request, the request body looks like this:

Get Sunil Yedla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

{“email”:”<Victims_Email>”,”password”:”Randompas”,”verifyPassword”:”Randompas”,”firstName”:”<firstname of victim>”,”lastName”:”<lastname of victim>”,”phoneNumber”:”<victims phonenumber>”}

Impact here is that an attacker can fetch the FirstName, LastName and Phone number details of any registered users but according to the website workflow this should not happen. Quickly created a Report and submitted through Bugcrowd. For better understanding adding steps below

Steps

[Victim] In browser-1, create a new account with email: <redacted>@gmail.com and Pass: Pass123!
[Attacker] In browser-2, Go to signup form Enter registered email Id: <redacted>@gmail.com
[Attacker] You will see error message like this: “You already have a <redacted> account. Please continue by entering your <redacted> password below.”
[Attacker] Since you do not know the password Enter random password and capture the request in burp suite
[Attacker] Check the server request body.

Happy to share this find with you all. Maybe If you found anything interesting feel free to share. Ping me on Twitter if you have any queries. Good Day!
