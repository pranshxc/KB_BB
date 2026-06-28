---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-23_bugbounty-how-i-was-able-to-hack-any-user-account-via-password-reset.md
original_filename: 2018-05-23_bugbounty-how-i-was-able-to-hack-any-user-account-via-password-reset.md
title: '#BugBounty — ''How I was able to hack any user account via password reset?'''
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: e6fe874cf05e3f477784f5922fea2d4e0feb28ed6fb85c444c7261c83b777b56
text_sha256: 6c7a1f5259881fca68c21372128a3e14ac58e4b947cb733f476874ca7df9b554
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — 'How I was able to hack any user account via password reset?'

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-23_bugbounty-how-i-was-able-to-hack-any-user-account-via-password-reset.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `e6fe874cf05e3f477784f5922fea2d4e0feb28ed6fb85c444c7261c83b777b56`
- Text SHA256: `6c7a1f5259881fca68c21372128a3e14ac58e4b947cb733f476874ca7df9b554`


## Content

---
title: "#BugBounty — 'How I was able to hack any user account via password reset?'"
page_title: "#BugBounty — “How I was able to hack any user account via password reset?” | by Dr. Gupta | Medium"
url: "https://medium.com/@BgxDoc/bugbounty-how-i-was-able-to-hack-any-user-account-via-password-reset-9009d84d94ff"
authors: ["Bikash Gupta (@BgxDoc)"]
bugs: ["IDOR", "Account takeover", "Password reset"]
publication_date: "2018-05-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5870
scraped_via: "browseros"
---

# #BugBounty — "How I was able to hack any user account via password reset?"

#BugBounty — “How I was able to hack any user account via password reset?”
Dr. Gupta
Follow
2 min read
·
May 23, 2018

280

4

Hi Guys,

During my recent bug bounty hunt, I came across a critical and yet simple vulnerability. We, all have had the moment when we make these accounts at various websites and barely use them and when we try to login back to those websites, we had to reset password.
A similar incident happened when I was trying to login to this website let’s say www.example.com , I couldn’t remember the password and then I clicked on forget password.

So let’s hack.

So, wwww.example.com sent me the password reset email and I noticed base64 encoding in the link. I quickly checked the link in Burp suite and it was like this:

https://www.example.com/members/update-password/<base64 encoded>/<base64 encoded2>

I used the inbuilt burp suite decoder and decoded it.
first one was decoded to : <email address>- -<company name>
second one was decoded to : <GMT +00 DateTime>- -<company name>

Get Dr. Gupta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then i checked for new account verification email. After signing up I got a verification email which was like this:

https://www.example.com/members/email-verification<base64 encoded>/<base64 encoded2>

As you can see both the forget password link and verification link was just using Base64 encoding in it’s link which decodes to email address of which i was trying to reset password or verify and — and the last one was company name; the second one was decoded to the GMT timestamp when i requested to forget password or trying to register along with — and again company name.

Here comes the next step of compromising user account. By visiting Facebook page of that company, I found many emails of valid user accounts in the comments.I was going to reset the password of one of that email but remembered it won’t be ethical. Never test users account without company permission, better create another test account and test.

An attacker can get valid users email from the Facebook page comments and reset their password which will lead to account takeover of any user. Never share your email address publicly.

I reported this vulnerability to the concerned company, and they were quick to patch it. I thank the company for the small token of appreciation :)

Thanks for reading!

~ BgxDoc ( https://twitter.com/BgxDoc )
