---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-27_how-i-bypassed-netflix-profile-lock.md
original_filename: 2021-12-27_how-i-bypassed-netflix-profile-lock.md
title: How I Bypassed Netflix Profile Lock?
category: documents
detected_topics:
- oauth
- access-control
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- oauth
- access-control
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 4bdfaa374a379ac87fb3e2be6489d22075ae1df65dca38e10190fe6b40f041d1
text_sha256: 665e632490b5486dd36c6379636363bcdd9607177de1c079b535897e46cae512
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I Bypassed Netflix Profile Lock?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-27_how-i-bypassed-netflix-profile-lock.md
- Source Type: markdown
- Detected Topics: oauth, access-control, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `4bdfaa374a379ac87fb3e2be6489d22075ae1df65dca38e10190fe6b40f041d1`
- Text SHA256: `665e632490b5486dd36c6379636363bcdd9607177de1c079b535897e46cae512`


## Content

---
title: "How I Bypassed Netflix Profile Lock?"
url: "https://infosecwriteups.com/how-i-bypassed-netflix-profile-lock-43901be1307c"
authors: ["Krishnadev P Melevila (@Krishnadev_P_M)"]
programs: ["Netflix"]
bugs: ["Logic flaw"]
publication_date: "2021-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3059
scraped_via: "browseros"
---

# How I Bypassed Netflix Profile Lock?

How I Bypassed Netflix Profile Lock?
Krishnadev P Melevila
Follow
3 min read
·
Dec 27, 2021

789

8

Hi hackers,

My name is Krishnadev P Melevila, To know more about me, Just search “Who is Krishnadev P Melevila” On Google or Ask your Google Assistant.

This time, It's a big fish!!! Yes, it’s Netflix!!!!

The vulnerability is that one can easily bypass Netflix profile lock with response manipulation.

Profile lock means, In Netflix, there is an option to add multiple users to one account and for the multiple accounts they can set up a profile lock for each profile with a 4 digit pin. So when someone login to the main account they are asked “Who is watching?”

HYPERLINK -> https://drive.google.com/file/d/1HkE2cd_wTX8pvyP6zv-mI4wQoyfp5iw0/view?usp=share_link (NO RELATION TO THIS WRITEUP, PART OF A GAME :))

Press enter or click to view image in full size

so after clicking profile they need to enter the profile pin to access the browse section. But there is a vulnerability in that feature. Steps to reproduce is given below:

Step 1: Visit https://www.netflix.com/ and login with your account then you will be asked “ Who is watching?” like the above screenshot

Step2: Here all users except guests and children have profile locks. So we are going to bypass this lock.

Get Krishnadev P Melevila’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step3: To do that we need to know at least one profile pin, say the profile pin of Krishnadev is 1704 then I will enter that pin and intercept the response of that request on burp and copy that whole success response.

HTTP/2 200 OK
X-Robots-Tag: noindex, nofollow
X-Frame-Options: DENY
X-Debug-Tz: GMT+5.50
X-Netflix.request.toplevel.uuid: 7d4b8b6b-fed5-44de-973b-1e14de56366f-422157414
X-Netflix.execution-Time: 6
Content-Type: application/json;charset=UTF-8
Date: Mon, 27 Dec 2021 03:48:33 GMT
Content-Length: 48
Via: 2 i-01d773509d78ec561 (us-west-2)
Server: api-prod-website i-00db4a31230d33cec
X-Xss-Protection: 1; mode=block; report=https://www.netflix.com/ichnaea/log/freeform/xssreport
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization,Content-Type,Content-Encoding,Accept,X-Netflix.application.name,X-Netflix.application.version,X-Netflix.esn,X-Netflix.device.type,X-Netflix.certification.version,X-Netflix.request.uuid,X-Netflix.originating.request.uuid,X-Netflix.user.id,X-Netflix.oauth.consumer.key,X-Netflix.oauth.token,X-Netflix.ichnaea.request.type,X-Netflix.Request.Routing,X-NETFLIX-PREAPP-PARTNER-ID, X-NETFLIX-PREAPP-INTEGRITY-VALUE, X-Netflix.Request.Priority,X-Netflix.Retry.Client.Policy,X-Netflix.Client.Request.Name,X-Netflix.Request.Retry.Policy,X-Netflix.Request.Retry.Policy.Default,X-Netflix.request.client.user.guid,X-Netflix.Request.NonJson.Headers,X-Netflix.esnPrefix,X-Netflix.browserName,X-Netflix.browserVersion,X-Netflix.osName,X-Netflix.osVersion,X-Netflix.uiVersion,X-Netflix.clientType,X-NETFLIX-PERSONALIZATION-ID,X-NETFLIX-DET-TOKEN,X-NETFLIX-DET-PARTNER-PAI,X-NETFLIX-RESPONSE-OVERRIDDEN,X-NETFLIX-DET-DEPRECATION
Access-Control-Expose-Headers: X-Netflix.Retry.Server.Policy,X-Netflix.Response.Tag,X-Netflix.Geo.Info,X-Netflix.request.inbound.identity.changed,Via,X-Netflix.Retry.Server.Policy.retryAfterSeconds,X-Netflix.Retry.Server.Policy.maxRetries,X-Ftl-Error,X-Netflix.uiVersion
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Origin: https://www.netflix.com
X-Originating-Url: http://www.netflix.com/api/shakti/v5185b692/profileLock
X-Netflix.nfstatus: 1_1
Set-Cookie: <REDACTED>
X-Netflix.proxy.execution-Time: 16
{"codeName":"S-Icarus-6.Alster","success":true}

Step4: Now let us bypass the profile lock of any other user, To do that first enter a wrong pin for any user and intercept the response of that request and replace the response with the above success response. and BOOM!! We got access to the Other user profiles without any authentication.

I reported this to Netflix, But they said that:

Hi krishnadevpmelevila,
The functionality is only intended as a barrier for children accessing mature content within an account. Local bypass, such as this one, is considered Won't Fix. Your effort is appreciated and we hope that you will continue to research and submit any future security issues you find.

But, My doubt is that, Then what is the use of that feature?

Don’t forget to follow me on medium and other social media. Also please give your 50 claps for this write-up and that's my inspiration to write more!!

My Instagram handle: https://instagram.com/krishnadev_p_melevila

My Twitter handle: https://twitter.com/Krishnadev_P_M

My LinkedIn handle: https://www.linkedin.com/in/krishnadevpmelevila/

My Personnel website: http://krishnadevpmelevila.com/
