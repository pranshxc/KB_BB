---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-16_my-first-and-last-crit-of-2020-on-hackerone.md
original_filename: 2021-01-16_my-first-and-last-crit-of-2020-on-hackerone.md
title: My first and last crit of 2020 on Hackerone
category: documents
detected_topics:
- rate-limit
- idor
- xss
- command-injection
- password-reset
- csrf
tags:
- imported
- documents
- rate-limit
- idor
- xss
- command-injection
- password-reset
- csrf
language: en
raw_sha256: cda68fe5d1bd15c4a821e2c500be12c41ea6cdd45d313a69a9617baa1e246980
text_sha256: a890e141206a8480729ae20a403f73f1d9d633daaea7f2ca191baaafed67f1ff
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# My first and last crit of 2020 on Hackerone

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-16_my-first-and-last-crit-of-2020-on-hackerone.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, xss, command-injection, password-reset, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `cda68fe5d1bd15c4a821e2c500be12c41ea6cdd45d313a69a9617baa1e246980`
- Text SHA256: `a890e141206a8480729ae20a403f73f1d9d633daaea7f2ca191baaafed67f1ff`


## Content

---
title: "My first and last crit of 2020 on Hackerone"
url: "https://takester.medium.com/my-first-and-last-crit-of-2020-on-hackerone-702a694781b0"
authors: ["Takester (@dhiraj_ramteke)"]
bugs: ["Lack of rate limiting", "Bruteforce", "IDOR", "Password reset", "Account takeover"]
publication_date: "2021-01-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3990
scraped_via: "browseros"
---

# My first and last crit of 2020 on Hackerone

Takester
 highlighted

My first and last crit of 2020 on Hackerone
Takester
Follow
3 min read
·
Jan 16, 2021

147

Hi friends, I hope you all doing good✌️.

In the month of December 2020 I picked some VDP’s on hackerone. When I was scrolling down this particular target seems interesting to me as it has various wild scope domains and has high crowd of researchers and if I report bugs on top level domains only, then there are maximum chances of getting it duplicate, so to avoid duplicates I googled about the program got various domains from there official site which may not found by other reseachers.

While doing my recon I got this one domain say redacted.com, at first glance it was normal target not having much functionality in it. It only has basic functionality like user registration and user reset password, so to understand the fuctionality I stated to use it as normal user and analyzed it as below.

User registration — ->User account operations — ->User password reset.

Get Takester’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

During the process I tried various bugs like CSRF, XSS, clickjacking etc. but no sucess. The target redacted.com has special feature that it doesn’t provides you full functionality until the admin gives you permissions, so to get permissions a user needs to send request to admin and after verification, the user gets permissions to access the full features. Now you must have think of BXSS and popup the XSS payload at admin side and yes I tried but no sucess.

Second day, when I woke up I fired my burp and stared hunting on the same target, but this time I looked at password reset functionality. During password reset user gets 4 digit pin on his mail, so first thing I tried to check rate limit and it actually worked, the target did not have any rate limit on the reset password functionality. I was able to takeover account of any users with valid mail id. [Note: User get assigned a user id which was getting send on mail as a pin to reset the password]

Press enter or click to view image in full size

It was consider as high severity bug and I was happy that I got my first high severity bug on it. After two-three days I thought of having another look at the target in hoping to get some low hanging bugs as I was clicking on each and every functions I got the weird endpoint like https://redacted.com/user/123 where 123 is userid, this link has the request that I submitted to admin including my name, email id and mobile number in it (that is default functionality of the target after sending the request, the form will be at users dashboard with users details in it), so I copied the link and open it in incognito mode and wholla 🎉🎉 it showed me all the details including name, mobile number and email id. After changing the uid I was able to get other users data too😲😲🎉🎉.

Then I linked the password reset vulnerability with this vulnerability and able to takeover every users account in a few seconds, as I was having the vaid userid and mail of that particular user.

I hope you guys learn something from it and if so give a nice clap.

Thank You!! keep hacking✌️…
