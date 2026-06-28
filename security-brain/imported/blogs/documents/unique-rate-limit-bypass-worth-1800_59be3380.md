---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-27_unique-rate-limit-bypass-worth-1800.md
original_filename: 2022-11-27_unique-rate-limit-bypass-worth-1800.md
title: Unique Rate limit bypass worth 1800$
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 59be33801933410d3a258356b071a886f033388c5937cb6d26e874c8c1e04a90
text_sha256: 45788ddd055151f5464d939f3cfd48838a841ed2eb5fe8b74e402e5fbc07764a
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Unique Rate limit bypass worth 1800$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-27_unique-rate-limit-bypass-worth-1800.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `59be33801933410d3a258356b071a886f033388c5937cb6d26e874c8c1e04a90`
- Text SHA256: `45788ddd055151f5464d939f3cfd48838a841ed2eb5fe8b74e402e5fbc07764a`


## Content

---
title: "Unique Rate limit bypass worth 1800$"
url: "https://infosecwriteups.com/unique-rate-limit-bypass-worth-1800-6e2947c7d972"
authors: ["Manav Bankatwala (@ManavBankatwala)"]
bugs: ["Rate limiting bypass", "Captcha bypass"]
bounty: "1,800"
publication_date: "2022-11-27"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1850
scraped_via: "browseros"
---

# Unique Rate limit bypass worth 1800$

1

Top highlight

Unique Rate limit bypass worth 1800$
Manav Bankatwala
Follow
3 min read
·
Nov 27, 2022

1K

10

Hello people,

While this is my first writeup on one of my finding of bypassing Rate limit to which I was awarded 1800$. Keeping it straight and simple, Here it goes.

Since few months, I have been trying to focus on rate limits and their security mechanism. I have read lots of write-ups of bypassing rate limits and gathered all of the methodologies in my checklist.

So I got this target one day which states that rate limit is out of scope with a note that they are completely secured from any type of rate limits on any endpoint. I decided to give a try on bypassing it even if it was out of scope just to prove the company statement wrong.

How they implemented rate limit security mechanism?

On any of their endpoint, there were 2 things responsible for preventing rate limit attacks.

X-Recaptcha-Token header
X-Security-Token header
Press enter or click to view image in full size

So, this X-Recaptcha-Token header consists of the captcha token and X-Security-Token consists of a long value, every time a new request is made, value for both of this parameter changes. So probably, we can’t even send same request more than 1 time. So if I removed the “X-Recaptcha-Token”, It showed an error that “captcha token invalid or not found”. This is how they implemented a strong rate limit security mechanism.

How I was able to bypass it?

After reviewing some responses, I found that there is a header “X-Disbaled-Recaptcha: 0”. I immediately removed the previous header from request and added this “X-Disabled-Recaptcha” header with value “1”. On sending this request instead of getting an error that “Recaptcha token is invalid or not found”, it showed a different error stating “Security token is invalid or alread used.” YES, you guessed it right. We were able to bypass the recaptcha token mechanism but still the security token was preventing and I tried every method to bypass the security token check but nothing worked. So I just though that it is not vulnerable and there’s no way to bypass this mechanism.

Get Manav Bankatwala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After few days, again I opened up that burp file and started to observe all the endpoints. To my surprise I found an endpoint which was responsible for generation of that “Security Token” and there was no rate limit mechanism only to that particular endpoint. Now, the normal behaviour of security tokens should be that as soon as new token is generated, the old one should be expired immediately even if it is unused. To my surprise I manually copied 10 security tokens and sent the request with header “X-Disabled-Recaptcha: 1”. All of the requests went successfull. YES!! That’s it. We bypassed the mechanism.

How I exploited it?

I created a simple script to create 1000 unique security tokens using the previously found endpoint.

Press enter or click to view image in full size

Imported this token into intruder. Added the header “X-Disabled-Recaptcha: 0” and started the attack.

Press enter or click to view image in full size
And we bypassed it on each and every endpoint.

At last, I told them that I was able to bypass their mechanism on all of their endpoints making their bold statement wrong to which they rewarded me 1800$ even if it was out of scope.

That’s it guys, I will surely write about some of my unique findings.

Share it guys, will share something amazing soon.

Follow me on:

https://www.linkedin.com/in/manavbankatwala/
