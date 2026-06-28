---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-08_its-all-about-2fa-bypass-or-account-takeover_2.md
original_filename: 2022-05-08_its-all-about-2fa-bypass-or-account-takeover_2.md
title: Its all about 2fa bypass, or Account Takeover
category: documents
detected_topics:
- command-injection
- password-reset
- mfa
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- password-reset
- mfa
- otp
- api-security
- cloud-security
language: en
raw_sha256: 190cf61726b72526cc70e9eba5609579078bb65c6d90fb9c7f651ca18db41743
text_sha256: a80749a5f1aeb99c4888c0b3e077f75a5755e790916fb0af3258d448ba9928ac
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Its all about 2fa bypass, or Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-08_its-all-about-2fa-bypass-or-account-takeover_2.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, mfa, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `190cf61726b72526cc70e9eba5609579078bb65c6d90fb9c7f651ca18db41743`
- Text SHA256: `a80749a5f1aeb99c4888c0b3e077f75a5755e790916fb0af3258d448ba9928ac`


## Content

---
title: "Its all about 2fa bypass, or Account Takeover"
url: "https://medium.com/@anjaneyulukanakatla1996/its-all-about-2fa-bypass-or-account-takeover-f9521f0a03b5"
authors: ["anjaneyulu kanakatla"]
bugs: ["Password reset", "Account takeover", "OTP bypass"]
publication_date: "2022-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2656
scraped_via: "browseros"
---

# Its all about 2fa bypass, or Account Takeover

Its all about 2fa bypass, or Account Takeover
anjaneyulu kanakatla
Follow
2 min read
·
May 8, 2022

60

Hello My Dear Buggies!!!

Happy to write my Second article in medium. kindly excuse me if any Grammarly mistakes in this article,still iam learner

I Hope your good,lets begin our show

Lets assume that its redacted.com. The program have full scope , when ever I choose the program . First thing to do for recon for finding any sensitive data in github, so I opened github searching for “readacted.com” apikeys unfortunately i didn’t find anything ,

So I Started playing reset functionality and but sadly nothing work, so just login my account. lets assume this has your.readacted.com after that I enabled 2fa function given my number , the otp has received entered otp, 2fa has enabled.lets play (actually when you registered an account its asking to create add your integration , i created my integration ) lets bypass 2fa , iam trying bypass 2fa by responace manipulation , and brute-forcing but didn’t work (the bgm starts) iam logout my account , iam thinking how to bypass.. after one hour break then iam started again, lets begin , i asked reste password function ( iam used this time my second browser ex: mozila ) changed the password , and still it asking 2fa ,here what i did i entred www.redacted.com there is login button, clicked login button. when i click that login button (its redirected to your integration page ) iam shock , still iam not login but when you click on your integration its redirected to your.readacted.com , still your not login but here there is option is there , click on your profile disable 2fa,change the email or phone number ,its lead to an Account takeover

Get anjaneyulu kanakatla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Submitted to program, still waiting for replay

IMPACT:

If an attacker may compromise your mail id and password,user may think iam safe with 2fa authentication(because user enable 2fa using phone number),but attacker can easily bypass 2fa (weak implenation 2fa authentication)

Thanks for reading

catch you in next writeup.bye bye

HAPPY HUNTING BUGGIES
