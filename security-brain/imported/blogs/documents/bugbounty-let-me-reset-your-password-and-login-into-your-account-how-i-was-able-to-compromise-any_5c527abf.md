---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-14_bugbounty-let-me-reset-your-password-and-login-into-your-account-how-i-was-able-.md
original_filename: 2018-03-14_bugbounty-let-me-reset-your-password-and-login-into-your-account-how-i-was-able-.md
title: '#BugBounty — “Let me reset your password and login into your account “-How
  I was able to Compromise any User Account via Reset Password Functionality'
category: documents
detected_topics:
- rate-limit
- password-reset
- sso
- idor
- command-injection
- otp
tags:
- imported
- documents
- rate-limit
- password-reset
- sso
- idor
- command-injection
- otp
language: en
raw_sha256: 5c527abf38db525a5f9927fec735a61609eaee9e488ad2b4677f27db9b1eb561
text_sha256: 538762d0a50f9603007e201babfa795d5aea7fbaff73801869d1ea2281c7f9f0
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — “Let me reset your password and login into your account “-How I was able to Compromise any User Account via Reset Password Functionality

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-14_bugbounty-let-me-reset-your-password-and-login-into-your-account-how-i-was-able-.md
- Source Type: markdown
- Detected Topics: rate-limit, password-reset, sso, idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5c527abf38db525a5f9927fec735a61609eaee9e488ad2b4677f27db9b1eb561`
- Text SHA256: `538762d0a50f9603007e201babfa795d5aea7fbaff73801869d1ea2281c7f9f0`


## Content

---
title: "#BugBounty — “Let me reset your password and login into your account “-How I was able to Compromise any User Account via Reset Password Functionality"
page_title: "#BugBounty — “Let me reset your password and login into your account “-How I was able to Compromise any User Account via Reset Password Functionality | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bugbounty-how-i-was-able-to-compromise-any-user-account-via-reset-password-functionality-a11bb5f863b3"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["Logic flaw", "Password reset", "Account takeover"]
publication_date: "2018-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5950
scraped_via: "browseros"
---

# #BugBounty — “Let me reset your password and login into your account “-How I was able to Compromise any User Account via Reset Password Functionality

#BugBounty — “Let me reset your password and login into your account “-How I was able to Compromise any User Account via Reset Password Functionality
Avinash Jain (@logicbomb)
Follow
3 min read
·
Mar 14, 2018

1.1K

7

Hi Guys,

One more interesting blog explaining an interesting vulnerability that I founded a while back in one of the Mobile Wallet Companies of India.

To login into any online website , we need to have an username which can be user’s registered mail id and password that he has set for it and if he doesn’t remember his password, there is a Reset Password Feature which comes to help. While researching out for the vulnerability around this feature , I found a logical flaw by which I was able to reset any user password and login with the same to takeover any user’s account.

Let’s now enter into the explanation-

When I clicked on Reset password functionality for the account “testaccount09@gmail.com”, I received a mail saying “To reset the password , please click on the below link-” and the link was something —

http://www._________.com/account/resetpassword? id=296417&token=dGVzdGFjY291bnQwOUBnbWFpbC5jb20=&vit=MjAxNi8xMC8yNQ==

2. Here ‘id’ is the identification number associated with the user account and ‘token’ is the base64 decoded registered mail ID of the user which here is “testaccount09@gmail.com” and ‘vit’ is the base64 decoded time stamp whose value in this case is “2016/10/25”

3. Researching more, I have found that the timestamp parameter is the expiry date of the reset password link which here was 2 days ahead from the time user clicked on the reset password option.

4. Here comes the step of compromising user account.By user enumeration on the same page, I found one valid user account, generated forgot password link for it and now begins the task for finding the right reset password link, I replaced the mail id of the user and encoded it to base64 and kept the timestamp value to 2 days ahead of the current date.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Victim mail id — varun09811@gmail.com

Base64 encoded value (Parameter = token) — dmFydW4wOTgxMUBnbWFpbC5jb20=

Timestamp value (Parameter = vit) — MjAxNi8xMC8yNQ=

5. Another part comes here is to find “id” associated with that particular user mail id. Since it’s a 6 digit code so I tried brute forcing it (fortunately no rate limiting was set ) and after a while, I found the right id associated with the victim mail id which happens to be id=254346 .( yes, this is something time consuming ).

6. So the tampered URL looks like -

http://www._________.com/account/resetpassword/?id=254346&token=dmFydW4wOTgxMUBnbWFpbC5jb20=&vit=MjAxNi8xMC8yNQ=

I loaded the link in the browser, and I was presented with “Set new password” ,

New Password Set Page

I reset his password and was successfully able to login into his account. I had the complete access to his account, can use his wallet money , change registered mobile number and everything!

I reported this vulnerability to the concerned enterprise, and they were quick to patch it within 2 days. I thank the company for the small token of appreciation :)

Thanks for reading!

~Logicbomb (https://twitter.com/logicbomb_1)
