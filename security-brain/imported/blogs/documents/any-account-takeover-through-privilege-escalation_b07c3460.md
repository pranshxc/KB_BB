---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-28_any-account-takeover-through-privilege-escalation.md
original_filename: 2021-02-28_any-account-takeover-through-privilege-escalation.md
title: Any Account Takeover Through Privilege Escalation
category: documents
detected_topics:
- password-reset
- access-control
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- password-reset
- access-control
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: b07c34601568a36fcbc86b0663787355b0e2cb9af69d9691c944effde3f4d7ac
text_sha256: 425b7e332f78cec87ba641d4847f1ccc0d71408212da6067dbd04089a4811736
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Any Account Takeover Through Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-28_any-account-takeover-through-privilege-escalation.md
- Source Type: markdown
- Detected Topics: password-reset, access-control, xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `b07c34601568a36fcbc86b0663787355b0e2cb9af69d9691c944effde3f4d7ac`
- Text SHA256: `425b7e332f78cec87ba641d4847f1ccc0d71408212da6067dbd04089a4811736`


## Content

---
title: "Any Account Takeover Through Privilege Escalation"
page_title: "Any Account Takeover Through Privilege Escalation - Shubham Chaskar"
url: "https://shubhamchaskar.com/ato-through-pe/"
final_url: "https://shubhamchaskar.com/ato-through-pe/"
authors: ["Shubham Chaskar (@chaskar_shubham)"]
bugs: ["Privilege escalation", "Account takeover"]
publication_date: "2021-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3858
---

S  h  u  b  h  a  m  C  h  a  s  k  a  r 

__[![Shubham Chaskar](https://shubhamchaskar.com/wp-content/uploads/2023/01/name-01.png)](https://shubhamchaskar.com/)

[![Shubham Chaskar](https://shubhamchaskar.com/wp-content/uploads/2023/01/name-01.png)](https://shubhamchaskar.com/)__

  * [Meet Shubham](https://shubhamchaskar.com/)

# Any Account Takeover Through Privilege Escalation

  * [ __Home](https://shubhamchaskar.com "Home")
  * [Bug-bounty](https://shubhamchaskar.com/category/bb/)
  * Any Account Takeover Through Privilege Escalation

![](https://shubhamchaskar.com/wp-content/uploads/2021/02/No-ATO-Sign.gif)

  * [__February 28, 2021](https://shubhamchaskar.com/2021/02/28/)
  * [ __2649 Views](https://shubhamchaskar.com/ato-through-pe/#respond)

Hello, I was eagerly waiting to share this with you! 🙂 Due to the two reasons.

  * It’s Account Takeover
  * And I wanted to tell you, “**How Important is to revisit your old target to pwn the new features**!”

I have already shared one of the write-up on **Privilege Escalation** on Facebook’s product! If you haven’t read that yet you can check [here.](https://shubhamchaskar.com/vpe-facebook-workplace/)

There are always questions in every newcomer’s mind, “This program is old. All great hackers have already participated, how can I get a bug in this product”?

The answer is, “**There are new features that are added to the product regularly and can be missed by anyone or other hackers might be busy with other programs”!  
** To be honest, it should be an encouraging fact that, “you are able to hack successfully even that was tested previously by some great experts!” It is just a game of perspective! 🙂  
You should consider signing up for a newsletter for your target!

**THE BUG:**

This Program is one of my favorites for a long time. I had a great run with it! I received details in an email of newly added features on my target’s product and I have decided to check and try my skills to pwn those features!  
While testing I have noticed one of the endpoints is disclosing “**Password reset token, Salt, Invitation token** ” which every hacker would love to have.” But what makes it more interesting is, that endpoint is only meant to be available for an admin user. When I found that endpoint I was an admin user and obviously, I wanted to achieve more impact. To do so I logged in with my lower Privileged user and hit the same API With the GET request.

The Following Image shows a lower Privileged user gets the password reset token of an admin user.

![](https://shubhamchaskar.com/wp-content/uploads/2021/02/edited-token-leak-1024x432.jpg)token leak to lower user

A user ID is an “MD5” hash that is accessible to everyone from the “employees” section. As you can see in the above image some juicy information is leaked by the application server.  
The Next step was to use that Reset Token to change the admin password and take over the admin account!

I went to forgot password page and I have requested a token for my lower privileged user(attacker)! After receiving the password reset link I captured the request and changed the token and submitted a new admin password. The request was successful and I was able to take over the admin account! As a matter of the fact, I was able to take over any account of the same organization! It could have been a disaster if a cross-organization account takeover was possible.

The following image shows the successful request for an admin account takeover!

![](https://shubhamchaskar.com/wp-content/uploads/2021/02/edited-password-reset-1024x316.jpg)admin account takeover

**I was able to find this bug just because I have subscribed to their newsletter!** As soon as I confirmed the issue I notified the team.

![](https://shubhamchaskar.com/wp-content/uploads/2021/02/edited-bc-confirm-1024x110.jpg)Dark Truth

**Timeline to remember:**

  * **09 Nov 2020 00:51:03 IST — Bug Reported**
  * **10 Nov 2020 18:39:41 IST — Bug Triaged**

  * **12 Nov 2020 22:05:46 IST — Something Good happened  
**

  * **24 Feb 2021 08:26:54 IST — Bug Patched**

**Impact:  
** The bug could allow any lower privileged user to takeover admin and/or any other normal user account!**  
**

This is one of the techniques to take over the account! Want to learn more other ways? Click here to check out these[slides](https://ninadmathpati.com/slides/) on account takeovers. Also, don’t forget to check out our [workbook.](https://shubhamchaskar.com/workbook/)

**What’s next?  
** I might share more write-ups but one interesting topic on [knoxss](https://knoxss.me/) is definitely coming in near future!

[mc4wp_form id=”594″]

#### Tags: 

[account takeover](https://shubhamchaskar.com/tag/account-takeover/) [bug-bounty](https://shubhamchaskar.com/tag/bb/) [Privilege escalation](https://shubhamchaskar.com/tag/pe/)

#### Share:

  * [__](https://www.facebook.com/sharer/sharer.php?u=https://shubhamchaskar.com/ato-through-pe/)
  * [__](https://twitter.com/share?text=Any%20Account%20Takeover%20Through%20Privilege%20Escalation&url=https://shubhamchaskar.com/ato-through-pe/)
  * [__](https://pinterest.com/pin/create/link/?url=https://shubhamchaskar.com/ato-through-pe/&media=https://shubhamchaskar.com/wp-content/uploads/2021/02/No-ATO-Sign.gif&description=Any%20Account%20Takeover%20Through%20Privilege%20Escalation)
  * [__](https://www.linkedin.com/shareArticle?mini=true&url=https://shubhamchaskar.com/ato-through-pe/&title=Any%20Account%20Takeover%20Through%20Privilege%20Escalation)

[__Previus PostVertical Privilege](https://shubhamchaskar.com/vpe-facebook-workplace/)

[Next Post A journey __](https://shubhamchaskar.com/xxe-to-ntlm/)

### 

#### Leave a comment

[Cancel reply](/ato-through-pe/#respond)

Save my name, email, and website in this browser for the next time I comment.

Post Comment

Δ

Copyright 2025 All Rights Reserved by Shubham Chaskar

  * [Home](https://shubhamchaskar.com/)
  * [Contact](https://shubhamchaskar.com/contact/)
  * [Faq](https://shubhamchaskar.com/faq/)
  * [Privacy Policy](https://shubhamchaskar.com/privacy-policy/)
  * [Workbook](https://shubhamchaskar.com/workbook/)
