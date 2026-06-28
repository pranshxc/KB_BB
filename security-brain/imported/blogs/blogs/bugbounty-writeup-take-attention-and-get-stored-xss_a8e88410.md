---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-14_bugbounty-writeup-take-attention-and-get-stored-xss.md
original_filename: 2019-08-14_bugbounty-writeup-take-attention-and-get-stored-xss.md
title: BugBounty WriteUp — take attention and get Stored XSS
category: blogs
detected_topics:
- xss
- ssrf
- command-injection
- csrf
- api-security
tags:
- imported
- blogs
- xss
- ssrf
- command-injection
- csrf
- api-security
language: en
raw_sha256: a8e88410bbf1d474f882680ff52b088d3946802f4a0c007cac1e4d2bbed465ef
text_sha256: 1be3549cd45d401e9b86542ff67c7de6f9387a88cbab54f5ebbd24d69ad3ed60
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# BugBounty WriteUp — take attention and get Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-14_bugbounty-writeup-take-attention-and-get-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `a8e88410bbf1d474f882680ff52b088d3946802f4a0c007cac1e4d2bbed465ef`
- Text SHA256: `1be3549cd45d401e9b86542ff67c7de6f9387a88cbab54f5ebbd24d69ad3ed60`


## Content

---
title: "BugBounty WriteUp — take attention and get Stored XSS"
url: "https://medium.com/@04sabsas/bugbounty-writeup-take-attention-and-get-stored-xss-495dd6eab07e"
authors: ["Oleksandr Opanasiuk (@Lekssik2)"]
bugs: ["Stored XSS"]
publication_date: "2019-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5083
scraped_via: "browseros"
---

# BugBounty WriteUp — take attention and get Stored XSS

BugBounty WriteUp — take attention and get Stored XSS
Oleksandr Opanasiuk
Follow
3 min read
·
Aug 14, 2019

143

Hi all,

The sponsor of this writeup is the attention for minor features that allowed me to get a good xxxx reward.

Press enter or click to view image in full size
Press enter or click to view image in full size

So, let’s imagine that we have a Web Application “WA”, that allows you to create users, companies and invite users to the company.

The functional of inviting worked like this — the user received a letter in the mail, where it was said: “You were invited to join company Hackerman. Accept invite[link]”

As the site allowed us to name of company contain “<> etc — I put the name of company as:

And you know what… I got such invite on email:

So I got such things earlier, and in principle… we can already report at this point, since this allows us to generate HTML messages by mail and send on behalf of the web application. (I used to find such a vulnerability on the site of one mobile giant, there we could change some parameters in the post request for registration, and then the link to confirm the account came with a broken HTML).

Get Oleksandr Opanasiuk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But… I sat on the site a little more and found that the site has internal notifications that you were invited — and when you go to the notification page — a window appears that says about the invitation. And you know what? They also did not filter html on this page :))))))

Sooo, lets register comapany a”><svg\onload=alert(1)> and — for all the users that we invite — they receive notifications about the invitation, thereby activating the Stored XSS.

Press enter or click to view image in full size

And after reporting and confirmation of vulnerability — a team member wrote to me that the problem with the email is a duplicate, but the previous hacker didn’t say anything about the Stored XSS! It’s a pity, because it turns out he missed such functionality and such critical vulnerability :(

While I was writing this WriteUp, I suddenly started to feel sorry for myself too — I remembered the #bugbountytips from intigrity — and there was a picture like “Found SSRF — exploit RCE, found Self-XSS — exploit Stored XSS with the help of CSRF, Found Stored XSS — exploit Account Takeover”. And only now I realized that I could work a little more and get much more, even P1. I hope you do not repeat my mistakes, always take the maximum impact from any vulnerability!

Find out more writeups (LOL 1 more xd)— https://twitter.com/Lekssik2 — will try to make them in more quantity and describe more interesting bugs.

Have a good day and wish you success in all your endeavors! :)

Oleksandr Opanasiuk
The latest Tweets from Oleksandr Opanasiuk (@Lekssik2). Great manager and not bad pentester https://t.co/qJyb7tVAtx…

twitter.com
