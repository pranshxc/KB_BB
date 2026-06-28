---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-30_2fa-bypass-by-changing-request-method.md
original_filename: 2022-01-30_2fa-bypass-by-changing-request-method.md
title: 2fa Bypass by changing Request method
category: documents
detected_topics:
- mfa
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- mfa
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 69bfd5312dd78821a329296f26edb8c028f430cd8e28dd130022823d3b271556
text_sha256: e5c8e3ea7501954b09704907d172c3e60aa4ac9aa2516597df391bec2f1c496b
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# 2fa Bypass by changing Request method

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-30_2fa-bypass-by-changing-request-method.md
- Source Type: markdown
- Detected Topics: mfa, xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `69bfd5312dd78821a329296f26edb8c028f430cd8e28dd130022823d3b271556`
- Text SHA256: `e5c8e3ea7501954b09704907d172c3e60aa4ac9aa2516597df391bec2f1c496b`


## Content

---
title: "2fa Bypass by changing Request method"
url: "https://medium.com/@arthbajpai277/2fa-bypass-by-changing-request-method-to-delete-500fd0ed12b8"
authors: ["Arth Bajpai (@arth_bajpai)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2022-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2965
scraped_via: "browseros"
---

# 2fa Bypass by changing Request method

2fa Bypass by changing Request method
Arth Bajpai
Follow
4 min read
·
Jan 29, 2022

160

7

Hello Everyone My name is Arth Bajpai, I’m from Lucknow, India, and I’m back with my third write-up about a 2fa Bypass which I Found a while ago.

So I received a Invitation to a private Program on Bugcrowd let’s assume target.com,

After receiving invitation I started checking it immediately and found some issues like few XSS, HTML injection and few more low hanging fruits,I had a feeling that I can find more on this So I Kept looking, and noticed 2fa function which has option to set SMS on phone number as 2fa, So I tried to check if OTP is getting leaked in response or somewhere to possibly find a 2fa Bypass there but it didn’t worked, tried to bypass 2fa via response manipulation and it didn’t worked either and none of known methods till that day didn’t worked either

So I thought About disabling it to check 2fa disable functionality, It had a button placed in front of 2fa to disable it and the best part was it didn’t require a password and was a single click 2fa disable,

I know what you guys are thinking, it occurred to me immediately as well and I clicked on disable, took request on burp and and created a CSRF POC of it expecting that I can disable 2fa via CSRF, Opened the CSRF POC on second browser/Account , But it showed error and it didn’t worked at all

Press enter or click to view image in full size

I tried to Bypass the CSRF by changing method, but it was validating the request based on cookie so couldn't do much and had to leave that function, and left the website as well after reporting few other vulnerabilities

After a while I looked again and couldn't find much bugs except few low hanging fruits which I really love to report, After reporting those I moved on and started testing other websites

After almost 2 months of receiving invitation I was having a Conversation with my friend about 2fa function of some other website, which had kind of same implementation about how we can bypass 2fa there , although we couldn’t find a way to bypass that website 2fa as well :(

After finishing conversation I was on my way home on Bike, And there is a really interesting thing about me, When I ride bike all I think about is possible vulnerabilities on possible targets, I get a lot of innovative ideas there, I know it’s weird but that it works :p

I thought why not try changing request method on 2fa screen itself as there is just a slight change in request on resending sms and deleting 2fa and there is no password confirmation on disabling 2fa plus it validates requests based on cookie and it was generated at the time of login so it was very much possible

Note:- It had 2 steps to login, First enter Id and password and then enter OTP to get access of account

As soon as I got home I opened my laptop to look for it,

Get Arth Bajpai’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so resend sms request kinda looked like

POST /api/v2/mfa/resend

and delete one kinda looks like

DELETE /api/v2/mfa

See that’s what I was thinking about , not of a much difference and request validates everything based on cookie and I have a Cookie as I followed 1 step out of 2 to get access into account

I entered Id Password and got to 2fa screen, where I needed to enter correct OTP to get into account,

I clicked on Resend SMS, took request on burp and changed the request method from POST to DELETE and removed resend from it and forwarded the request and boom 2fa disabled

Now Using this I can bypass 2fa of anyone easily within seconds ,

Reported it immediately but turned out to be duplicate

Still a pretty good one and I will say it’s my best/favorite 2fa bypass till date and wanted to share with you all so that you can learn from it

As always don’t forget to follow me on twitter and Linked , I will give away 2 pentester labs subscription to random persons as soon as I hit 1k followers on twitter, details of it will be shared soon so don’t forget to follow

Twitter link — https://twitter.com/arth_bajpai

Linked In- https://www.linkedin.com/in/arth-bajpai-6699681b3/

till next time bye bye take care
