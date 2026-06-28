---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-14_theoretically-possible-to-practical-account-takeover_2.md
original_filename: 2020-11-14_theoretically-possible-to-practical-account-takeover_2.md
title: Theoretically Possible To Practical Account Takeover
category: documents
detected_topics:
- idor
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 6b103f260a0bd5175129fd6f7c3f38adfcf0c15fb13bd2fb883d265871fd5048
text_sha256: 92df08a797a225f8d85d5282a82b2774f2f0b36f4b5a5666658b8a6c1104d3f8
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Theoretically Possible To Practical Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-14_theoretically-possible-to-practical-account-takeover_2.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `6b103f260a0bd5175129fd6f7c3f38adfcf0c15fb13bd2fb883d265871fd5048`
- Text SHA256: `92df08a797a225f8d85d5282a82b2774f2f0b36f4b5a5666658b8a6c1104d3f8`


## Content

---
title: "Theoretically Possible To Practical Account Takeover"
url: "https://ironfisto.medium.com/theoretically-possible-to-practical-account-takeover-c9383ab03f76"
authors: ["Mukul Lohar (@ironfisto)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2020-11-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4135
scraped_via: "browseros"
---

# Theoretically Possible To Practical Account Takeover

Theoretically Possible To Practical Account Takeover
Mukul Lohar
Follow
2 min read
·
Nov 13, 2020

120

Hey InfoSec Community,

This one is the last account takeover I found and wanted to share about it. It was a good chain of IDOR with some recon and understanding of the application.

So it was a crypto mining web app and developed by a Russian solo developer. At first glance, the app seems very secure because the crypto withdrawal process was not a single-step process. They were verifying the person’s identity also.

So I straight tried to test account takeover even though the impact was just knowing the amount of crypto assets victims have.

POC
Created two accounts with email and noted the primary key of both accounts which was UUID.
Went to the reset password function and entered the email id and got the reset password link which kind of looked like this
https://domain.tld/changePassword/{user-primary-key-id}/{reset-token}

3. Looking at the link first thought was like this looks vulnerable. And you know the rest what I will try :P

I replaced user primary key to victim primary key

https://domain.tld/changePassword/{victim-primary-key-id}/{attacker-reset-token}

Request

POST /changePassword/62c4ffb0-be57-11e8-a68e-8d01686939c8/378fce7754fcdadebb6de5d778753c9916ffed192c942756b45bfeabd4e856f00799a6db002a292eb5cfe007208cc7b1 HTTP/1.1

Request Body

{"password":"urhacked"}

Response to this request was 200 and I was able to take over the account of any user. But any user is a false claim. Because I don’t know the victim’s email id or UUID primary key. So its theoretically possible attack and my test account were attacking each other.

Get Mukul Lohar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So Next part was to figure out how to get UUID. I understood the applications and there was referral functionality and the link looked like this

https://domain.tld/?source=4vyryrtfhf

So now we have a source referral parameter belonging to the victim. But it doesn’t leak UUID. I found another endpoint that takes the source referral parameter.

https://domain.tld/fast/4vyryrtfhf
Press enter or click to view image in full size
SEE VICTIM UUID

And see now I have victim UUID.
So with google dorks, I was able to get as many as source parameters of any user and get the UUID. And takeover any user account on the applications.

4. Next I just need to use my account to get the reset password token and use victim UUID in the reset password link. That’s how I was able to take over the victim account.

So That’s quick write up on the theoretically possible to practical account takeover.

Rewarded fraction of ETH.

I am looking for an opportunity specific to infosec roles. I have two years of back end development experience and one-year pen testing experience also.

Reach out to me on twitter -> https://twitter.com/ironfisto

Bye
