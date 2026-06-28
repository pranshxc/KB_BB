---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-11_bypassing-2fa-using-openid-misconfiguration.md
original_filename: 2021-06-11_bypassing-2fa-using-openid-misconfiguration.md
title: Bypassing 2FA using OpenID Misconfiguration
category: documents
detected_topics:
- otp
- mfa
- jwt
- sso
- access-control
- command-injection
tags:
- imported
- documents
- otp
- mfa
- jwt
- sso
- access-control
- command-injection
language: en
raw_sha256: 488237dc0cd0c7e5aaeedeef2e5b8168c13f92365268e8d83c9fc82ba6f15b60
text_sha256: 2c3b8e454258f357641ed8d5d794e0f1475e52febc43833ff4f7706eea435726
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing 2FA using OpenID Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-11_bypassing-2fa-using-openid-misconfiguration.md
- Source Type: markdown
- Detected Topics: otp, mfa, jwt, sso, access-control, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `488237dc0cd0c7e5aaeedeef2e5b8168c13f92365268e8d83c9fc82ba6f15b60`
- Text SHA256: `2c3b8e454258f357641ed8d5d794e0f1475e52febc43833ff4f7706eea435726`


## Content

---
title: "Bypassing 2FA using OpenID Misconfiguration"
url: "https://youst.in/posts/bypassing-2fa-using-openid-misconfiguration/"
final_url: "https://youst.in/posts/bypassing-2fa-using-openid-misconfiguration/"
authors: ["Youstin (@iustinBB)"]
bugs: ["2FA / MFA bypass", "Broken authentication"]
publication_date: "2021-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3586
---

Two factor authentication is rapidly becoming a norm in all authentication systems, however faulty implementation can often times render the defense mechanism useless. There's plenty of write-ups going through vulnerabilities such as missing rate limits, improper access controls and token leakage, but this short write-up will present a unique bypass caused by a misconfiguration in an OpenID implementation.

The target was a company with over 50 worldwide brands, with a lot of them using the company's OpenID system for authentication. The company's main website was in this case, the Identity Provider and each brand / website that relied on it, had to implement it and configure the OpenID flow. When testing a website that was recently added to the program's scope, I noticed that unlike others, this one was enforcing two factor authentication through Google Authenticator. Looking at the requests sent in the background, I noticed that when clicking the login button a request simillar to this one is sent:

![](/images/req.png)

The first thing that stood out was the `acr_values` parameter. I haven't encountered it before when looking at OpenID flows, so I thought it was some custom configuration that would lead to an easy 2FA bypass. The first and obvious idea was to try removing the `otp` value and only keeping the `password` value. While I was correctly redirected to the Identity Provider's login page, upon logging in with correct credentials, I was always facing a 401 if the `otp` value was removed.

After further testing, It became increasingly apparent that this was not a rushed 2FA implementation, but it was a well established protocol explained in [RFC 8176](https://datatracker.ietf.org/doc/html/rfc8176).

_Typically, each "amr" value provides an identifier for a family of closely related authentication methods. For example, the "otp" identifier intentionally covers OTPs (One-Time Passwords) based on both time and HMAC (Hashed Message Authentication Code). Many relying parties will be content to know that an OTP has been used in addition to a password; the distinction between which kind of OTP was used is not useful to them. Thus, there's a single identifier that can be satisfied in two or more nearly equivalent ways._

Basically, the `acr_values` parameter would tell the Identity Provider what authentication methods the client requests. Upon fulfilling the login flow, the callback to the client website will contain a JWT, which if decoded, would contain the AMR value used like so:

`{"alg":"HS256","typ":"JWT"}.{"state":"123456789","auth_time":1234,"amr":["pwd","otp"] ...`

Tampering with the values before and after logging in with the identity provider were just welcomed by a bunch of 401 errors, so I gave up on that idea quite fast.

Section 5 of [RFC 8176](https://datatracker.ietf.org/doc/html/rfc8176) states the following security considerations when implementing AMR:

_taking a dependence upon particular authentication methods may result in brittle systems since the authentication methods that may be appropriate for a given authentication will vary over time._

Therefore, OpenID configurations relying on AMR should make sure to only accept trusted and validated authentication methods. Authentication methods that may be appropriate for a given authentication will vary over time, both because of the evolution of attacks on existing methods and the deployment of new authentication methods.

Reading the above had me thinking that there might be some other available acr values I could test. The second section of the rfc lists 22 defined authentication methods, so I decided to test a few. Shortly after, upon switching the `acr_values` value from `otp+password` to `sms+password` and entering the credentials, I was greeted with the following image:

![](/images/sms.png)

This was looking promising, so I used a one time SMS verification service and followed through the proccess. Upon adding the phone number and confirming ownership, I succesfully skipped the Google Authenticator window and was also logged in. I reported the issue and it was triaged and paid as High severity. The team let me know that this was caused because the client website had both OTP and SMS enabled, even though there was no UI for enabling sms as a two factor authentication method. This is a clear case on how easy it is to misconfigure the AMR protocol and introduce unwanted security vulnerabilities.
