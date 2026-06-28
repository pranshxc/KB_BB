---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-15_hacking-facebook-accounts-using-csrf-in-oculus-facebook-integration.md
original_filename: 2018-01-15_hacking-facebook-accounts-using-csrf-in-oculus-facebook-integration.md
title: Hacking Facebook accounts using CSRF in Oculus-Facebook integration
category: documents
detected_topics:
- oauth
- sso
- command-injection
- otp
- automation-abuse
- race-condition
tags:
- imported
- documents
- oauth
- sso
- command-injection
- otp
- automation-abuse
- race-condition
language: en
raw_sha256: e8ec8ccd236cf235b3359200fb0a02a0f4d0e9df2d66adb06d5139cf1856c0ca
text_sha256: 4324fa509f51331156c6ba50bb29fa376d80cad1482af18f0435cff5f13b13e3
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Facebook accounts using CSRF in Oculus-Facebook integration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-15_hacking-facebook-accounts-using-csrf-in-oculus-facebook-integration.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, otp, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `e8ec8ccd236cf235b3359200fb0a02a0f4d0e9df2d66adb06d5139cf1856c0ca`
- Text SHA256: `4324fa509f51331156c6ba50bb29fa376d80cad1482af18f0435cff5f13b13e3`


## Content

---
title: "Hacking Facebook accounts using CSRF in Oculus-Facebook integration"
page_title: "Hacking Facebook accounts using CSRF in Oculus-Facebook integration -  Josip Franjković"
url: "https://www.josipfranjkovic.com/blog/hacking-facebook-oculus-integration-csrf"
final_url: "https://www.josipfranjkovic.com/blog/hacking-facebook-oculus-integration-csrf"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
publication_date: "2018-01-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6011
---

#  [ Josip Franjković web security consultant ](/)

[Blog](/)

Bug bounties

##  Hacking Facebook accounts using CSRF in Oculus-Facebook integration 

written on January 15th, 2018

Oculus enables users to connect their Facebook accounts for a more "social" experience. This can be done using both the native Windows Oculus application and using browsers. I took a deeper look at the native Windows flow, and found a CSRF vulnerability which allowed me to connect a victim's Facebook account to attacker's Oculus account. Once connected, the attacker could extract the victim's access token, and use Facebook's GraphQL queries to take over the account. 

#### Steps to take over the victim's Facebook account:

  1. Using the attacker's Oculus account, create the following GraphQL mutation. The mutation should be sent to graph.oculus.com/graphql, with the attacker's Oculus access_token: 
  
  Mutation Test {
  facebook_sso_uri_generate( <input> ) { uri } }
  &query_params={"input":{"client_mutation_id":"1"}}

  2. The response will contain a link similar to this: https://www.oculus.com/facebook_login_sso/?username=josip.tester1&ext=1508804050&hash=AeQ6a90lgYfffT5k The idea behind the link is to enable a single click integration between the two services.  

  3. If the victim clicks on the link or visits a page which renders it as the src attribute on an <img> tag, their Facebook account will be connected to the attacker's Oculus account. In the background, the link actually **redirects to Facebook's OAuth flow, skips it, and then connects the two accounts.**

At this point I thought about reporting this to Facebook, since the attacker could view victim's partial friend list and other minor information, but decided to dig a bit deeper into the native application. The app's app.asar contained references to a GraphQL query which returned information about the connected Facebook account: 
  
  
  viewer(){ linked_accounts_info { facebook_account { **facebook_id** } } } 

Getting the Facebook ID is useless - it is public anyway. However...

  4. After a bit of guessing, I found out it is also possible to query for the victim's Facebook **access_token:**

  
  
  viewer(){ linked_accounts_info { facebook_account { **access_token** } } } 

A screenshot of the request and the response: ![Getting Facebook access_token from Oculus](/resources/img/oc-token-2.png) This is a **first-party access_token** , which also has access to Facebook's GraphQL endpoint - third party apps are not allowed to do that. Once you get such a token, you have **full control** of the account.  
By previously decompiling various Facebook apps, I had recorded some persisted GraphQL queries. I used these to prove the account takeover and add a new phone number to my test victim's account: 

  5. doc_id is the persisted query ID, matching the "SendConfirmationMutation" mutation which adds a new mobile phone. 
  
  graph.facebook.com/graphql?**doc_id=10153582085883380** &variables={"input":{"client_mutation_id":1,"actor_id":"FBID",
  "phone_number":"**+PHONENUMBER** "}}
  &access_token=**VICTIMTOKEN**
  

  6. After the confirmation code arrives, we can confirm it using "ConfirmPhoneCodeMutation": 
  
  graph.facebook.com/graphql?**doc_id=10153582085808380**
  &variables= {"input":{"client_mutation_id":1,"actor_id":"FBID",
  "confirmation_code":"**CODE** "}}&
  method=post&access_token=**VICTIMTOKEN**
  

  7. Finally, reset the victim's password using the attacker's confirmed mobile phone. 

#### Timeline:

  * **24th of October, 2017, 03:20** \- Report sent to Facebook 

  * 24th of October, 2017, 10:50 - First reply from Facebook 

  * **24th of October, 2017, 11:30** \- Temporary fix for the bug (disabled /facebook_login_sso/ endpoint) 

  * 30th of October, 2017 - Bug is now fixed. 

The fix was to check if the currently logged-in user on Oculus matches the username parameter from the SSO link, which means a login CSRF or response splitting or any other way to set victim's cookies would defeat it.  
A couple weeks later I found a login CSRF which could also be used to redirect the victim to an Oculus URL I chose - the perfect candidate to bypass the first fix. Steps to reproduce are the same as in the first bug, with an additional one between steps 2 and 3:  

After getting the /facebook_login_sso/ **$LINK** , the following request could be made using cURL to auth.oculus.com/nonce-redirect/
  
  
  curl -v --cookie "oc_ac_at=..snip.." --referer "https://auth.oculus.com/"  -d  "require_token_for=752908224809889&redirect_uri=https://www.oculus.com/account_receivable/?redirect_uri=**$LINK** "
  https://auth.oculus.com/nonce-redirect/

The response contained an /account_receivable/ link with a nonce, which logs the victim into the attacker's Oculus account, and then redirects to the SSO link, skips the OAuth flow, and connects the account.

#### Timeline:

  * **18th of November, 2017, 02:40** \- Report sent to Facebook 

  * 18th of November, 2017, 05:10 - First reply from Facebook 

  * **18th of November, 2017, 10:00** \- Temporary fix for the bug (disabled /facebook_login_sso/ endpoint once again) 

  * 11th of December, 2017 - Bug is now fixed. 

This time, the fix was to implement a CSRF check on the /account_receivable/ endpoint, AND add an additional click to confirm the link between Facebook and Oculus accounts. I believe this properly fixes the vulnerability without degrading user experience too much. 

As always, a big thank you to Facebook for running their bug bounty program. Shout-out to [Pete Yaworski](https://twitter.com/yaworsk) for proofreading this blog, and to [@phwd](https://twitter.com/phwd) for his awesome GraphQL / API [write-ups.](https://philippeharewood.com/)

##### Random blog post

Bug bounties 

####  Race conditions on the web 

written on July 12th, 2016

[ Read more ](/blog/race-conditions-on-web)

![Josip Franjković](/resources/img/josip-franjkovic.jpg)

##### Josip Franjković

###### web security consultant

I enjoy breaking websites and participating in various bug bounty programs. 

##### You can contact me using:

  * [@JosipFranjkovic](https://twitter.com/josipfranjkovic) (DM open to everyone) 
  * [[email protected]](/cdn-cgi/l/email-protection#43292c302a336d2531222d29282c352a2003242e222a2f6d202c2e)
  * [keybase.io/josipfranjkovic](https://keybase.io/josipfranjkovic)

All rights reserved © 2018.  
— Josip Franjković
