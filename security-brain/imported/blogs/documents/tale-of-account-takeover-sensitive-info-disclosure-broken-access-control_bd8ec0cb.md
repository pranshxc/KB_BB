---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-10_tale-of-account-takeover-sensitive-info-disclosure-broken-access-control.md
original_filename: 2019-07-10_tale-of-account-takeover-sensitive-info-disclosure-broken-access-control.md
title: Tale of account takeover — Sensitive info Disclosure + Broken Access Control
category: documents
detected_topics:
- access-control
- xss
- password-reset
- idor
- command-injection
- otp
tags:
- imported
- documents
- access-control
- xss
- password-reset
- idor
- command-injection
- otp
language: en
raw_sha256: bd8ec0cbd1161a8fbb50b15447f96becd208b43d61e1c71131df9b3e920d0742
text_sha256: 713c8cd0e4969b2d741ebd219382643f46021c2b700b0ab2d9871dbcf6770a46
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of account takeover — Sensitive info Disclosure + Broken Access Control

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-10_tale-of-account-takeover-sensitive-info-disclosure-broken-access-control.md
- Source Type: markdown
- Detected Topics: access-control, xss, password-reset, idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `bd8ec0cbd1161a8fbb50b15447f96becd208b43d61e1c71131df9b3e920d0742`
- Text SHA256: `713c8cd0e4969b2d741ebd219382643f46021c2b700b0ab2d9871dbcf6770a46`


## Content

---
title: "Tale of account takeover — Sensitive info Disclosure + Broken Access Control"
url: "https://medium.com/@sakyb7/tale-of-account-takeover-sensitive-info-disclosure-broken-access-control-cea0a5e3a1fd"
authors: ["Md Saqib (@sakyb7)"]
bugs: ["IDOR", "Account takeover"]
bounty: "2,650"
publication_date: "2019-07-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5159
scraped_via: "browseros"
---

# Tale of account takeover — Sensitive info Disclosure + Broken Access Control

Top highlight

Tale of account takeover — Sensitive info Disclosure + Broken Access Control
Saqib Chand
Follow
4 min read
·
Jul 10, 2019

607

5

Hi
Mates, Myself 
Md Saqib
 from India I'm new to this bug hunting community, hope you are doing good. Today I'm gonna share an interesting Tale of Account Takeover Vulnerability on hackerone private Program. The vulnerability is a chaining of sensitive information disclosure(auth_token) of users through IDOR and bypassing password confirmation through broken access control. So let's get started! 😉

The program is a job portal site, as it is a private program we will call it as redacted.com, So I just signup as a candidate and testing for some CSRF and stored XSS on profile but I had no luck so I decided to create another account to test some IDORs and to get the understanding of how the site is working like registration, login, forgot password etc.. while create a new account I was intercepting every request of the site and seeing the response of it.. While Registering The site first asks for the email of the user to check it is already registered or not and then I enter a new email address there and checked the response

Press enter or click to view image in full size
Leaking Auth_Token

I was like wait! What?? 🙄

“redirect_url”:“/?auth_token=_v2_8dsf8as
df12ad4f5a4sdf56as1df65asdf56sd4ff&contact_id=11cb26ae&e
xpire=1152315525”

This Looks interesting to me…. I go ahead and change the email to already existing account.

Press enter or click to view image in full size
Indirect Object Reference on auth leakage

And I got auth_token of an existing account which means I can get anyone’s auth_token with this endpoint “/candidate/create” this is damm interesting. I just need to figure it out that how I can abuse it, Then I immediately look for the burp suite proxy history to see where the Auth_Token is used… and its very simple

https;//redacted.com/?auth_token=d8fs4ds8fdsf84
dsf8dsfads8fasd6f84dsf684dsafccv68f4&contact_id=52z1d5d4
&expire=1152315525

And I fired up incognito mode in the browser and hit the above link... AND BOOM!!! I was logged in the victim’s account... Oh yeah, account takeover. Amazing! I clicked on the profile to see if I can change the password or email of the victim’s account.. and you know what..? I can't see the profile of the victim...

Press enter or click to view image in full size

OOhhhh Shit password confirmation!!!!! 😥 I was like 🤮

I decided to anyhow to bypass this shit.!

Get Saqib Chand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you guys remember I told that I successfully logged into the victim’s account but when I click on profile it's asking for password confirmation which means somehow account is identified with this current cookie. So if I can change the email of the victim and then I can request the new password on my email.

Press enter or click to view image in full size

I log in to my account to check how changing an email functionality works. I found this endpoint used to update email/change email ‘/api/profile’ which takes PATCH request with JSON formatted data `{“email_address”:“attackers@gmail.com”}`.

So I created a PATCH request on “https://redacted.com/api/profile” with my new email and JSON formatted body ‘{“email_address”:“mynewmail@gmail.com”}’ with victim’s cookie.

Press enter or click to view image in full size
Voila! Success!!

As you can see below I successfully bypass password confirmation by changing the email of the victim to attacker’s mail, now I can request for password reset link in my mail and reset the password of the victim due to broken authentication on profile update endpoint.

Press enter or click to view image in full size

Awesome! I was was Awarded 2500$ for this report and report resolved with 4 days..

After the resolved of this report I found another endpoint which can bypass the confirm password protection by changing the email address of the victim the endpoint look likes this “/contact/api/update/v1” and awarded again 150$ for the bypass.

Thank you, everyone! Hope you guys enjoyed this writeup.

Twitter: @sakyb
