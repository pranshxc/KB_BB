---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-28_information-disclosure-to-account-takeover.md
original_filename: 2021-07-28_information-disclosure-to-account-takeover.md
title: Information Disclosure to Account Takeover
category: documents
detected_topics:
- oauth
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- oauth
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: e8cca7235c3a396aef7dd94978434d92fbee9f3a400aae12753e740184e7a7d9
text_sha256: e318960c9417cc731ad7c87fc96c0b13617a13a365f2d7be1ea62c8e0a63fc02
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Information Disclosure to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-28_information-disclosure-to-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `e8cca7235c3a396aef7dd94978434d92fbee9f3a400aae12753e740184e7a7d9`
- Text SHA256: `e318960c9417cc731ad7c87fc96c0b13617a13a365f2d7be1ea62c8e0a63fc02`


## Content

---
title: "Information Disclosure to Account Takeover"
url: "https://sunilyedla.medium.com/information-disclosure-to-account-takeover-a21b2b54147a"
authors: ["Sunil Yedla (@sunilyedla2)"]
bugs: ["Information disclosure", "OAuth", "Account takeover", "Authentication bypass"]
publication_date: "2021-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3470
scraped_via: "browseros"
---

# Information Disclosure to Account Takeover

Sunil Yedla
 highlighted

Sunil Yedla
 highlighted

Information Disclosure to Account Takeover
Sunil Yedla
Follow
3 min read
·
Jul 28, 2021

497

6

Hi everyone! This is Sunil Yedla, Bug bounty hunter from Andhra Pradesh, India. Hope you all are healthy and safe. Today’s writeup is my recent find on external private program where I was able to completely takeover any users account who signed up using OAuth flow or connected social accounts without victims interaction. As always I will try to keep my writeup not soo technical so that it will be easy to understand for any beginner. Let’s start!

On July 9th, I found couple of Low/Medium severity vulnerabilities on an external private program. One of the vulnerability is happening at this endpoint: https://<target.tld>/proxyservices/v1/users/validate?searchUser =<Victims_email>

What is the Initial vulnerability?

This vulnerability is captured when user is intercepting login requests, when user enter credentials and click on login then the system will first verify if that users exists in targets database or not. The vulnerability at this endpoint: /proxyservices/v1/users/validate?searchUser =<Victims_email> is that, in the response full details of the registered user is displayed which includes, their status, plan, phone number etc,. I reported this responsibly on July 9th.

Press enter or click to view image in full size

Escalating the Vulnerability:

Get Sunil Yedla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am not sure why but on July 13th I was retesting the same endpoint but this time I have given email address which is connected to google Social account. I got an additional parameter value this time. i.e, ``idToken`` it is a base 64 encoded data and even after decoding I found couple of other token values but not sure where to use it. So I kept that aside and move to another target.

Press enter or click to view image in full size

In the evening, I again started re-testing this target and when I captured OAuth sign-in, I found ``idToken`` parameter in the request . You already knew what I would do here : )

So I quickly created two accounts on target and connected OAuth to both accounts. For clarity let’s call the two accounts as attacker@gmail.com and victim@gmail.com. Attacker now send a GET request to this endpoint: https://<target.tld>/proxyservices/v1/users/validate?searchUser =victim@gmail.com and copy the idToken value from the response. Now Login as attacker@gmail.com using social account [Google]and capture the request in Burpsuite. The request will be like this:

POST /proxyservices/v1/auth/add/SocialMailUser HTTP/1.1
Host: target.tld
XXX

— — — — — — — — — — — — — — -274014344326728136281788800409
Content-Disposition: form-data; name=”idToken”

<Attackers_idToken>
— — — — — — — — — — — — — — -274014344326728136281788800409
Content-Disposition: form-data; name=”authType”

SOCIAL_GMAIL
— — — — — — — — — — — — — — -274014344326728136281788800409
Content-Disposition: form-data; name=”genPassword”

<genpassword>
— — — — — — — — — — — — — — -274014344326728136281788800409 —

Now simply replace ``idToken`` value of attacker with victim’s and send the request [Keep the genpassword value as it is]. The attacker will successfully Login to victims account without victims interaction.

This was reported responsibly to the Private program on July 13th and the bounty is not yet rewarded. I hope this writeup is informational, feel free to share your feedback via twitter Sunil Yedla . Stay positive and Share Positivity.
