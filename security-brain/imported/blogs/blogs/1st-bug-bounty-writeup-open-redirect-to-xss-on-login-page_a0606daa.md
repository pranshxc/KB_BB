---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-15_1st-bug-bounty-writeup-open-redirect-to-xss-on-login-page.md
original_filename: 2021-08-15_1st-bug-bounty-writeup-open-redirect-to-xss-on-login-page.md
title: '1st Bug Bounty WriteUp: Open Redirect To XSS on Login Page'
category: blogs
detected_topics:
- xss
- oauth
- command-injection
- api-security
tags:
- imported
- blogs
- xss
- oauth
- command-injection
- api-security
language: en
raw_sha256: a0606daa0c20c112edd9155fb01ab6657c7d2d0862c8387fe0e5745a86eb8633
text_sha256: 1fca1ab11c48d08c1e49bc926675796e89dc7c68770660cc3d127132900dc826
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# 1st Bug Bounty WriteUp: Open Redirect To XSS on Login Page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-15_1st-bug-bounty-writeup-open-redirect-to-xss-on-login-page.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `a0606daa0c20c112edd9155fb01ab6657c7d2d0862c8387fe0e5745a86eb8633`
- Text SHA256: `1fca1ab11c48d08c1e49bc926675796e89dc7c68770660cc3d127132900dc826`


## Content

---
title: "1st Bug Bounty WriteUp: Open Redirect To XSS on Login Page"
url: "https://nassimchami.medium.com/1st-bug-bounty-writeup-open-redirect-to-xss-on-login-page-313221da2879"
authors: ["Nassim Chami (@nvccim)"]
bugs: ["Open redirect", "XSS"]
publication_date: "2021-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3418
scraped_via: "browseros"
---

# 1st Bug Bounty WriteUp: Open Redirect To XSS on Login Page

Top highlight

1st Bug Bounty WriteUp: Open Redirect To XSS on Login Page
Nassim Chami
Follow
2 min read
·
Aug 15, 2021

256

2

Hello hackers Hope you are doing well, My name is Nassim, i’m a bug bounty hunter, started a few months, i was discover many vulnerabilities, and now i want to share interesting bug i found and how escalate from open redirect to reflected xss.

So let’s start, i was get invitation from private web application program let’s called redacted.net with 80 asset in scope, and i go check it one by one, i saw an interesting subdomain has email input :

Press enter or click to view image in full size

I start hunting and know how it work, i added random email and click on next, so here i notice somthing in URL, is looks like that :

https://subdomain.redacted.net/error_page?redirect_uri={redirect_url}&message={error_message}&extra_message={error_message}

Press enter or click to view image in full size

There three parameters, [message] and [extra_message] related to the errors message it print in the page and i can spoof it with other errors message,

Get Nassim Chami’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

the [redirect_uri] parametre related with button who redirect to the url who is in the parameter, So i change it with other url and i was seccessfully redirect it when i click to [Back To Login], I didn’t stop here, i want to escalate it to XSS, after 2 hours of trying to know how WAF is work I bypassed that, yeah! When doing the injection into javascript: as a javascript code, it looks like a WAF on hardening settings, although when the injection point are tags, it’s not. Anyway, what I learned when trying to bypass it :

document.location.href=’//t.co’ is blocked.
when trying to refer to that using strings contatenation let tt=’documen’;let yy=’t’;let uu=’.locatio’;let ii=’n’;let oo=’.hre’;let pp=’f’;let aa=tt+yy+uu+ii+oo+pp;a=’//example.com’;, it doesn’t work although it’s a valid code.
<tag> in javascript: context is blocked.
let a=’<tag’;let b=’>’;c=a+b is not.
let bb=’<svg onload=’ is blocked because onload event is triggered WAF.
let bb=’<svg onload’;let cc=’=’ is not.
(), `and let a=’(‘;let b=’)’` is blocked.
let a=’)’;let b=’(‘ is not ! .

So my final payload using strings concatenation:

let bb=’<svg onload’;let cc=’=’;dd=’promp’;ff=’)’;gg=’t(‘;hh=’>’;aa=bb+cc+dd+gg+ff+hh

Encode payload as URL :

%6c%65%74%20%62%62%3d%27%3c%73%76%67%20%6f%6e%6c%6f%61%64%27%3b%6c%65%74%20%63%63%3d%27%3d%27%3b%64%64%3d%27%70%72%6f%6d%70%27%3b%66%66%3d%27%29%27%3b%67%67%3d%27%74%28%27%3b%68%68%3d%27%3e%27%3b%6c%6c%3d%62%62%2b%63%63%2b%64%64%2b%67%67%2b%66%66%2b%68%68

I replace my payload in redirect_uri and works successfully

Press enter or click to view image in full size

Twitter : www.twitter/nvccim

Thank you for reading, see you in next blog .
