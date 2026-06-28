---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-03_bugbounty-i-dont-need-your-current-password-to-login-into-your-account-how-could.md
original_filename: 2018-02-03_bugbounty-i-dont-need-your-current-password-to-login-into-your-account-how-could.md
title: '#BugBounty — ''I don''t need your current password to login into your account''
  - How could I completely takeover any user''s account in an online classified ads
  company.'
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: f728144c5370e8b5d9aa72e1b9d77a0f29354168eb97cd9e9869c4244bf27b31
text_sha256: 98bebad3736cf69c84d7628d59391af92e3018cfc9582831953378b819600553
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — 'I don't need your current password to login into your account' - How could I completely takeover any user's account in an online classified ads company.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-03_bugbounty-i-dont-need-your-current-password-to-login-into-your-account-how-could.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f728144c5370e8b5d9aa72e1b9d77a0f29354168eb97cd9e9869c4244bf27b31`
- Text SHA256: `98bebad3736cf69c84d7628d59391af92e3018cfc9582831953378b819600553`


## Content

---
title: "#BugBounty — 'I don't need your current password to login into your account' - How could I completely takeover any user's account in an online classified ads company."
page_title: "#BugBounty — “I don’t need your current password to login into your account” - How could I… | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bugbounty-i-dont-need-your-current-password-to-login-into-your-account-how-could-i-e51a945b083d"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["Authentication bypass"]
publication_date: "2018-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5987
scraped_via: "browseros"
---

# #BugBounty — "I don't need your current password to login into your account" - How could I completely takeover any user's account in an online classified ads company.

1

·

Top highlight

Avinash Jain (@logicbomb)
Follow
3 min read
·
Feb 3, 2018

1.1K

9

#BugBounty — “I don’t need your current password to login into your account” - How could I completely takeover any user’s account in an online classified ads company.

Hi Guys,

“User account compromise” ! Yes, you read right . This was an excellent vulnerability which I have found recently during my bug bounty hunting in India’s most popular online classified ads company.

“An OTP is more secure than a static password, especially a user-created password, which is typically weak” and we all agree to this but what if someone could bruteforce it and what if someone could bypass OTP authentication? That what makes it vulnerable and targeting the same , I carried out this critical piece of hunt. Let’s see into the details —

Forgot Password Page

While browsing through the website for some vulnerabilities , I went to the “Forget Password” functionality where it asked me to enter the registered mobile number .

OTP Verification Page

and as I entered the number , it sent me an OTP and after filing the right OTP in the form , it redirected me to “New password page” where I was allowed to set a new password for my account.

I firstly jumped into the most common and basic attack to bypass OTP — bruteforcing attack to see if there is any rate limiting or captcha being implemented but as I phrased it “most common and basic” , so it was not going to help me and captcha was also implemented there after 3 consecutive wrong attempts.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s dive into this more. When I entered the wrong OTP, I got the following as the response —

Press enter or click to view image in full size
Wrong OTP HTTP Response

Notice status parameter as “401” which means “ Unauthorized Error response” and that was obvious too as I entered the wrong OTP. Now to check whether it is just based on client side validation , I tried to bypass it . Captured the response , changed the “status” json parameter value to “200” and forwarded the response -

Press enter or click to view image in full size
Changed HTTP Response

But some validation was there and it throws me the error message-

Press enter or click to view image in full size
Invalid OTP Error Message

Might be the other parameters are causing the validation error so this time I removed all the json parameters and added the success parameter with the value to “true” so now the response json looks like —

Modified HTTP Response

and this time I was redirected to “Set Password Page” :D -

Forgot Password Page

I was able to set a new password for the user and using the changed password I was able to successfully login into the user’s account. This is how I could bypass OTP authentication and set a new password for the user and able to completely compromise his account using his mobile number.

Report details -

07-Jan-2018 — Bug Reported to the concerned company.

27-Jan-2018 — Bug was marked fixed.

03- Feb-2018 — Re-tested and confirmed the fix.

28-Feb-2018 — Rewarded by the company .

This was all about this interesting finding. ☺

Thanks!

~Logicbomb (https://twitter.com/logicbomb_1)
