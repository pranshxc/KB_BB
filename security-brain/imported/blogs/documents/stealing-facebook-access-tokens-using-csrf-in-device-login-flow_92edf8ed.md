---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-07-19_stealing-facebook-access_tokens-using-csrf-in-device-login-flow.md
original_filename: 2016-07-19_stealing-facebook-access_tokens-using-csrf-in-device-login-flow.md
title: Stealing Facebook access_tokens using CSRF in device login flow
category: documents
detected_topics:
- oauth
- command-injection
- otp
- csrf
- information-disclosure
tags:
- imported
- documents
- oauth
- command-injection
- otp
- csrf
- information-disclosure
language: en
raw_sha256: 92edf8ed7223123d280d23582757522ce231ee014c423d91528d2d80f438b925
text_sha256: fbb59edc125282b66ed3f99bdc3cc4884886407396fb1964e5eb0c3b392f37cb
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing Facebook access_tokens using CSRF in device login flow

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-07-19_stealing-facebook-access_tokens-using-csrf-in-device-login-flow.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp, csrf, information-disclosure
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `92edf8ed7223123d280d23582757522ce231ee014c423d91528d2d80f438b925`
- Text SHA256: `fbb59edc125282b66ed3f99bdc3cc4884886407396fb1964e5eb0c3b392f37cb`


## Content

---
title: "Stealing Facebook access_tokens using CSRF in device login flow"
page_title: "Stealing Facebook access_tokens using CSRF in device login flow -  Josip Franjković"
url: "https://www.josipfranjkovic.com/blog/hacking-facebook-csrf-device-login-flow"
final_url: "https://www.josipfranjkovic.com/blog/hacking-facebook-csrf-device-login-flow"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF", "OAuth", "Information disclosure"]
publication_date: "2016-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6280
---

#  [ Josip Franjković web security consultant ](/)

[Blog](/)

Bug bounties

##  Stealing Facebook access_tokens using CSRF in device login flow 

written on July 19th, 2016

Facebook has published a way to use OAuth on Internet of Things devices, called Facebook Login for Devices. You can read the documentation [here](https://developers.facebook.com/docs/facebook-login/for-devices). The usual flow is: 

  1. Application requests graph.facebook.com/oauth/device?type=device_code&client_id=1

to retreive a **hash code** and **user_code**

  2. The application tells the user to go to facebook.com/device and input the user_code 

  3. The user inputs the code and verifies the application through usual OAuth flow. user_code is then connected to application code. 
  
  https://www.facebook.com/v2.5/dialog/oauth?redirect_uri=https%3A%2F%2Fm.facebook.com%2Fdevice.php%3FuserCode%3D{**$user_code**}&client_id=1234

This is the mobile version of device login flow - redirect_uri points to a mobile domain. 

  4. The application can now request graph.facebook.com/oauth/device?type=device_token&client_id=1&code=hash_code

to gain the user **access_token**

The problem lies in step number 3: when user_code is connected to application_code, it is done like so: 
  
  
  https://m.facebook.com/device.php?userCode=**$userCode** &code=**$appCode**

As you can see, there is no CSRF protection, so I started building my proof of concept around that: 

  1. The attacker requests graph.facebook.com/oauth/device?type=device_code&client_id=1 to get the user_code (**abcd**) and hash code (**4567**) 

  2. Present a page to victim which will load 
  
  https://www.facebook.com/v2.5/dialog/oauth?redirect_uri=https%3A%2F%2Fm.facebook.com%2Fdevice.php%3FuserCode%3D**abcd** &client_id=1234

  3. The /dialog/oauth will redirect to 
  
  https://m.facebook.com/device.php?userCode=**abcd** &code=aZx...

which will succeed 

  4. The attacker now requests graph.facebook.com/oauth/device?type=device_token&client_id=1&code=**4567**

to get the **access_token** of the victim. 

To exploit this, attacker would need to know the victim has approved an application which has “Login for Devices” enabled, which makes it fairly hard to abuse - this is a perfect storm vulnerability.  
Through further testing, I found out that every app which has “Login from Devices” enabled, and “Web OAuth Login” disabled gets “m.facebook.com/device.php” automagically added as a valid redirect_uri. 

Theoretically, if a pre-approved official Facebook application is made for the future iToaster, this bug could have lead to info disclosure on any Facebook account, and perhaps more, depending on the app permissions. It was a long shot, and I found no such application (thanks [@phwd](https://twitter.com/phwd) for help here). 

Facebook has fixed this first by adding a re-confirmation prompt every time you try to use device login, and later by implementing CSRF protection through "state" OAuth parameter: 

![Facebook device flow re-confirmation](/resources/img/device-flow.png)

#### The timeline:

  * **December 8, 2015:** Bug reported 

  * December 9, 2015: Additional information sent, along with a proof of concept page 

  * December 11, 2015: Facebook confirms the vulnerability 

  * **February 1, 2016:** I ask for updates about the report 

  * February 10, 2016: Facebook informs me they have fixed the issue 

  * February 10, 2016: Nope, message was sent in error 

  * **February 18, 2016:** Bug is now fixed 

##### Random blog post

Bug bounties 

####  Getting any Facebook user's friend list and partial payment card details 

written on March 9th, 2018

[ Read more ](/blog/facebook-friendlist-paymentcard-leak)

![Josip Franjković](/resources/img/josip-franjkovic.jpg)

##### Josip Franjković

###### web security consultant

I enjoy breaking websites and participating in various bug bounty programs. 

##### You can contact me using:

  * [@JosipFranjkovic](https://twitter.com/josipfranjkovic) (DM open to everyone) 
  * [[email protected]](/cdn-cgi/l/email-protection#fb919488928bd59d899a959190948d9298bb9c969a9297d5989496)
  * [keybase.io/josipfranjkovic](https://keybase.io/josipfranjkovic)

All rights reserved © 2018.  
— Josip Franjković
