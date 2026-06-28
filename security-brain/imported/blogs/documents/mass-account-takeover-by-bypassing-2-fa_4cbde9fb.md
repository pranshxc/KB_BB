---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-31_mass-account-takeover-by-bypassing-2-fa.md
original_filename: 2023-01-31_mass-account-takeover-by-bypassing-2-fa.md
title: Mass Account takeover by bypassing 2 FA
category: documents
detected_topics:
- mfa
- idor
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- mfa
- idor
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 4cbde9fb0582a2f83af1bd89561e957c377a8232caad1a99f00a66b9a5a04873
text_sha256: 215c700c6b80353053019f6d8d40e2a5e01cddf6bd72157767daa5cc054c2e16
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Mass Account takeover by bypassing 2 FA

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-31_mass-account-takeover-by-bypassing-2-fa.md
- Source Type: markdown
- Detected Topics: mfa, idor, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `4cbde9fb0582a2f83af1bd89561e957c377a8232caad1a99f00a66b9a5a04873`
- Text SHA256: `215c700c6b80353053019f6d8d40e2a5e01cddf6bd72157767daa5cc054c2e16`


## Content

---
title: "Mass Account takeover by bypassing 2 FA"
page_title: "Bypassing 2fa leads to account takeover"
url: "https://z-sec.co/mass-account-takeover"
final_url: "https://z-sec.co/mass-account-takeover"
authors: ["Zeeshan Mustafa (@by6153)"]
bugs: ["2FA / MFA bypass", "IDOR", "Account takeover"]
publication_date: "2023-01-31"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1599
---

# Mass Account takeover by bypassing 2 FA

UpdatedJanuary 16, 2026

•2 min read•[ __View as Markdown](/mass-account-takeover.md)

![Mass Account takeover by bypassing 2 FA](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1768597354826%2F39ee1690-9d1a-4ebe-8413-a7a824ab05cb.png&w=3840&q=75)

[ Z](https://hashnode.com/@zsec)

[Zeeshan M.](https://hashnode.com/@zsec)

[__](https://twitter.com/@by6153)[__](https://www.linkedin.com/in/zeeshanm0x0/)

[__Part of series Writeups](/series/writeups)

On this page

Admin account creation with normal userThings to remember

Hey fellow hackers,

I'm not gonna bore you with a long story of this pentest project. Last month I was working on a Pen-testing project and I found multiple critical & high vulnerabilities and I'll cover the interesting findings only. I won't share the name of the application let's assume it's redacted.com it has multiple subdomains but my focus was on the main domain. So, on the main domain, it has a login portal and from there users and admins can login to their dashboard. It was a grey box Pen-testing I tried to login as an admin with the admin credential and it was a successful login but it asked for the OTP since 2fa is enabled just for the admin, not for normal users. So, upon successful login it asks for OTP in the new HTTP request it asked only for userID and the parameter was OTPUserId=5 digit numbers by replacing this userId I was able to login to another user account and it wasn't validating the LoginOTP parameter. Later I found that without authentication just by sending a post request to that endpoint with the parameter "OTPUserId" and "LoginOTP" I was able to login just by providing anyone's userid.

Note: later I found that the same HTTP request plus parameter was already in their javascript file as an attacker without having any credentials I was able to login into anyone's account.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1675167092004/6b69f7e9-10a4-46ad-98e2-1b9ad8014c9e.png)

As you can see in the above Screenshot just by providing userid I was able to login into anyone's account. The first part is finished here.

# Admin account creation with normal user

So in the first part, you can see that an attacker was able to login into anyone's account without a username and password just by typing random userID. So after authentication into any user's account, I was able to navigate to the admin panel by just visiting https://redacted.com/admin/dashboard from there most of the admin functionalities were accessible and the interesting one was the "User Management" section I was able to create users with custom roles either admin or normal user and I created an admin account just for the testing purpose it was working I was admin without credential I was able to create an admin account and then take over the whole admin panel.

### Things to remember

By reading their Js code I was able to login into anyone's account without credentials and then I found that "/admin/dashboard" was accessible for authenticated users but doesn't check if the user is an admin or a normal user and then from "User Management" section I was able to create admin account.

**./exit**

[#ethical-hacking](/tag/ethical-hacking)[#hacking](/tag/hacking)[#pentesting](/tag/pentesting)[#account-takeover](/tag/account-takeover)[#2fa-bypass](/tag/2fa-bypass)
