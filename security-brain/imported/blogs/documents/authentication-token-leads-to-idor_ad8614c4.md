---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-28_authentication-token-leads-to-idor.md
original_filename: 2020-07-28_authentication-token-leads-to-idor.md
title: Authentication Token Leads To IDOR
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- cors
- csrf
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- cors
- csrf
language: en
raw_sha256: ad8614c430a468a7c9fc514d13545e0b978137830dbb346b3e76235168b29665
text_sha256: ee48c4d7331c454b63fc5f16a5bcf2505f4e75298518a4e1fd66c37692142053
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Authentication Token Leads To IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-28_authentication-token-leads-to-idor.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, cors, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `ad8614c430a468a7c9fc514d13545e0b978137830dbb346b3e76235168b29665`
- Text SHA256: `ee48c4d7331c454b63fc5f16a5bcf2505f4e75298518a4e1fd66c37692142053`


## Content

---
title: "Authentication Token Leads To IDOR"
url: "https://tox7cv3nom.github.io/2020/07/28/authentication-token-bypass-leads-too-idor.html"
final_url: "https://tox7cv3nom.github.io/2020/07/28/authentication-token-bypass-leads-too-idor.html"
authors: ["mohit (@mohit29295572)"]
bugs: ["Authentication bypass"]
publication_date: "2020-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4377
---

## Introduction

Here is the article how i was able to bypass authentication token and able to exploit idor and add any user to add events of website ..before coming on main topic that how i find the vulnerablity let me clear your core concepts about authorization tokens

**Authorization tokens : They are used to authenticate user suppose a user partha visited a website and create their accounts authorization token verifies the user each time when partha logon in website web page gives him auth token ands when he logout then token get destroyed and each time when partha login to that website he gots a new token thats the work of auth tokens..it prevents from vulnerablities like idor,csrf and cors**

## Exploiting Vulnerablity

so that's the basic concept about authorization tokens.. now i tell my stort of getting idors i was really excited when i got a invitation program i decided to look at that program i saw there the site was implementing auth tokens for identifying users it creates a new token when user logged in each time and destroy the token when user logout from website after playing with request and response i saw there when the request was send with 'PATCH' method without auth token shows 401(unauthorized) response while the request with any other method without auth token it shows response 200 (ok).it means token not implemented properly :) i tried to change patch method to get but stil found 401 the other request other then 'patch' method are seems to be useless becoz there was no crucial data which i report to website so i decided to check every page which consist of GET or POST methods i fuzz every page there i saw there was option to register on event any one can register in event by uploading his/her resume and his name ..i quickly created another account on website and register my 2nd account on event and logout from my device and then i open burp and change email id,name and id no. to mine first account and remove auth token and bingo! i got registered on that event from my account with the resume and information of other candidate due to idor

**Tip: eveytime check all request and response check website architecture i.e how token works,how the website is behaving on ur query i.e responses 200,401,302 etc. and most important never give up everything is vulnerable just think out of box :)**

any private program ?

send it to : [@mohit](mailto:nhibtaungamain@gmail.com)

</div>
