---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-07_auth-bypass-via-exposed-credentials.md
original_filename: 2022-10-07_auth-bypass-via-exposed-credentials.md
title: Auth Bypass Via Exposed Credentials
category: documents
detected_topics:
- sso
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: 03e092ca72bcdf0f5ebf2871e86be97d43f562f01a64958d15534fa3502e256e
text_sha256: 90f12d1a57e35591819819d3d797c8ff82ced29e2ba43f9017eed3d1c7211727
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# Auth Bypass Via Exposed Credentials

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-07_auth-bypass-via-exposed-credentials.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `03e092ca72bcdf0f5ebf2871e86be97d43f562f01a64958d15534fa3502e256e`
- Text SHA256: `90f12d1a57e35591819819d3d797c8ff82ced29e2ba43f9017eed3d1c7211727`


## Content

---
title: "Auth Bypass Via Exposed Credentials"
page_title: "Auth Bypass Via Exposed Credentials | crypt0g30rgy.github.io"
url: "https://crypt0g30rgy.github.io/post/AuthBypass"
final_url: "https://crypt0g30rgy.github.io/post/AuthBypass"
authors: ["g30rgy th3 d4rk (@Crypt0g30rgy)"]
bugs: ["Hardcoded API keys"]
bounty: "700"
publication_date: "2022-10-07"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 2072
---

# [crypt0g30rgy.github.io](https://crypt0g30rgy.github.io/)

# Auth Bypass Via Exposed Credentials

## How we got there

So it was on one of those days, i was feeling bored and kinda alone. When i feel like this i usually divulge into some hacking `(to fill that void😃)` So off i went to [Intigriti](https://app.intigriti.com/researcher) and i saw that a program i followed had an update `(funny story was i didn't recall having followed the program but i may have as well did, i get forgetful sometimes)`

After checking out the program lets call it jij0 [why](/post/why), i found that they had *.jij0.me on scope and they were rewarding bounties for it, upto €1500 for an exceptional bug.

So i said why not, up to this point the highest severity i ever got for my bug was high `(3 times)` via payment bypass `(Write-ups below)` or [Home](/).

So after i took the domain i headed to [c99 Subdomain finder](https://subdomainfinder.c99.nl/index.php), pasted the domain and clicked start scan `(No other tool you ask[still bored remember])`. Found several hundred domains.

Now i visted all the domains one by one i eventually got to a domain chat.jij0.me that redirected to microsoft online sso. But during the redirect it loaded the javascript files as most common JavaScript Frameworks connecting to a nodejs backend. Like the [PHP EAR Vulnerability](https://owasp.org/www-community/attacks/Execution_After_Redirect_\(EAR\))

I stopped the redirect to microsoft online sso by doing a view-source:<https://chat.jij0.me>. Found the main js file that was under <https://chat.jij0.me/js/index.js>

Since i new the backend was written under NODEJS i started searching for the NODE_ENV variable. I saw that it had refrence like the following
  
  
  {NODE_ENV:"production",VUE_APP_ADMIN_URL:"https://ADMIN.JIJ0.ME",VUE_APP_VLS_BASIC_AUTH:"Basic Y2hhdG1ldXA6b250d2l0dGVyMHgwMSEK",VUE_APP_ENV:"PROD",VUE_APP_USEBOUNCER_API_KEY=***REDACTED***,VUE_APP_VERSION:"1.33.7",BASE_URL:"/"}
  

After seing this i remember visiting <https://admin.jij0.me> which resulted in a 401 unauthorized error. To test the validity of the auth basic creds i requested the <https://admin.jij0.me/favicon.ico> which had previously returned a 401 error and this time i got a 200 OK

Sent the below request with burp.
  
  
  GET /favicon.ico
  HOST: admin.jij0.me
  Authorization: Basic ***REDACTED-SUSPECT-TOKEN***I was in and i could see so much information that was clearly not intended for the public. I felt good but was honestly scared a little, that feeling of getting a critical severity bug + being inside a government server was overwhelming at first.

> I immediately stopped testing and wrote a report including sceenshots and embedded the vulnerable code snipplet on my report.

## Reproduction Steps

  1. Headed to <https://chat.jij0.me/js/index.js>
  2. Searched and found the NODE_ENV values
  3. Visited <https://admin.jij0.me> to see 401 error
  4. Now add the creds chatmeup:ontwitter0x01! with chatmeup as the username & ontwitter0x01! the password
  5. Now i have access to a lot of data data
  6. I stopped testing at this point. But i believed an attacker can leverage this to escalate further.

## Report

After i found this bug i was super excited and shaking a little because i was in a goverment server viewing so much data.

` I had access to internal communications that exposed sensitive information. `

So i wrote up a detailed report fast and sent it to the program at intigriti. The report was triaged within 45 mins.

After waiting for two days i recieved a €700 bounty.

![basic](/images/basic.png)

## Contacts

### @[github](https://github.com/crypt0g30rgy) @[twitter](https://twitter.com/crypt0g30rgy) @[LinkedIn](https://www.linkedin.com/in/george-maina-waithaka-95a465214/) @[Intigriti](https://app.intigriti.com/profile/g30rgyth3d4rk) @[hackerone_old](https://hackerone.com/crypt0p3n3tr4t0r?type=user)
