---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-29_how-i-was-able-to-takeover-accounts-on-foxitcom.md
original_filename: 2021-06-29_how-i-was-able-to-takeover-accounts-on-foxitcom.md
title: How I was able to Takeover Accounts on Foxit.com
category: documents
detected_topics:
- password-reset
- command-injection
tags:
- imported
- documents
- password-reset
- command-injection
language: en
raw_sha256: 7a7817283dced1c972bfa6878cc12b0b7d6aeee655d4f23dd69f468ca67d2b42
text_sha256: 2cfe731cab3e8ba5e0fde34ee4a95e05d3bc34bde589c5647018e04e2bdb343b
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to Takeover Accounts on Foxit.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-29_how-i-was-able-to-takeover-accounts-on-foxitcom.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `7a7817283dced1c972bfa6878cc12b0b7d6aeee655d4f23dd69f468ca67d2b42`
- Text SHA256: `2cfe731cab3e8ba5e0fde34ee4a95e05d3bc34bde589c5647018e04e2bdb343b`


## Content

---
title: "How I was able to Takeover Accounts on Foxit.com"
url: "https://medium.com/techiepedia/how-i-was-able-to-takeover-any-account-on-foxit-com-7a08efa0144f"
authors: ["Jefferson Gonzales (@gonzxph)"]
bugs: ["Password reset", "Account takeover"]
publication_date: "2021-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3534
scraped_via: "browseros"
---

# How I was able to Takeover Accounts on Foxit.com

How I was able to Takeover Accounts on Foxit.com
Jefferson Gonzales
Follow
3 min read
·
Jun 29, 2021

261

3

Hello to all Security Researchers and Bug Hunters who is reading this blog, Im Jefferson Gonzales also new in bug hunting, so without wasting your time lets beggin

First I used dork to find a Responsible Disclosure Program and while searching I found foxit.com

I created an account on foxit.com and exploring the functionalities but I found nothing inside, then I logout my account and testing the forgot password functionality.

Press enter or click to view image in full size

First I put my email and submit, then I got my reset password link in my email like this

Press enter or click to view image in full size

Nothing suspicious on the link, then I review my history on burp suite and I got this request while requesting a reset password

Press enter or click to view image in full size

As you can see in the image above the parameter “resetPasswordUrl:” is the same as the link in my reset password that sent to my email earlier

Me thinking what if I change the link inside the “resetPasswordUrl:” to https://google.com?

Then I change to https://google.com and I got this request sent to my email

Press enter or click to view image in full size

And Boom! It was successful, using this vulnerability I can takeover any account only knowing the email of the victim

Get Jefferson Gonzales’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s try to test the account takeover with burp collaborator

First I reset the password of my victims email and change the “resetPasswordUrl:” with my burp collaborator link

Press enter or click to view image in full size

And the victim received a message like this

Press enter or click to view image in full size

If the victim click that link I will received the response in my burp suite collaborator like this

Press enter or click to view image in full size

Then I can takeover the victims account

Reported time: June 9, 2021
Bug Fixed: June 22, 2021
Appreciation by Foxit
Press enter or click to view image in full size

Thank you for reading this writeup 😁

Contact me on

Twitter: @gonzxph

LinkedIn: @gonzxph
