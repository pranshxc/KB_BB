---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-20_missing-authorization-check-in-facebook-pages-manager.md
original_filename: 2017-07-20_missing-authorization-check-in-facebook-pages-manager.md
title: Missing Authorization check in Facebook Pages Manager
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 5be2ad5c72078ea6f6f32006e3a80ac12892703bab7290d07ecc351f4ace7ec9
text_sha256: a96132ce669ff0cc22ba6dc6b96e6959d8f4bf1c40ee681427d435fc42dc2c60
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Missing Authorization check in Facebook Pages Manager

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-20_missing-authorization-check-in-facebook-pages-manager.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5be2ad5c72078ea6f6f32006e3a80ac12892703bab7290d07ecc351f4ace7ec9`
- Text SHA256: `a96132ce669ff0cc22ba6dc6b96e6959d8f4bf1c40ee681427d435fc42dc2c60`


## Content

---
title: "Missing Authorization check in Facebook Pages Manager"
url: "https://medium.com/@arbazhussain/missing-authorization-check-in-facebook-pages-manager-9f7bd879ff33"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "1,000"
publication_date: "2017-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6145
scraped_via: "browseros"
---

# Missing Authorization check in Facebook Pages Manager

Missing Authorization check in Facebook Pages Manager
Arbaz Hussain
Follow
2 min read
·
Jul 20, 2017

62

Severity: Medium

Complexity: Easy

Weakness: Authorization/Permission Model

Discovery:

Basically it was an Missing Authorization Check in Facebook Page Manager while disconnecting facebook page with twitter handle.

I Used to see lot of post’s,who retweet or tweet anything on Twitter is get’s posted on Facebook .

Example : Tweet from Twitter
So i decided to test facebook authorization with twitter to find any Bug’s!
To link our page we have to go to :

www.facebook.com/twitter

I have created a demo page on facebook and As a ADMIN of page i had linked facebook page with twitter.
After that i made my second account as ‘ANALYST’ on that page. As you all know an ANALYST is an role with the least permissions. He shouldn’t have any privilege to open or change settings.
So as i previously mentioned it was an missing authorization check. I simply opened my second account in which i had the ‘ANALYST’ role and navigated to www.facebook.com/twitter when we open this link all our pages and accounts linked to twitter handle are shown, Also there was an option to unlink page from twitter. Yup i unlinked the page from twitter with ‘ANALYST’ role.

Reproduce:

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1) Create an page and link the page with twitter handle.

2) Make your second account an ANALYST of that page.

3) An Analyst is not allowed to make any changes in the page.

4) Now login to you second account (ANALYST ACCOUNT) and navigate to
www.facebook.com/twitter

5) You will see an unlink option click the unlink and the page will be unlinked from twitter.

VIDEO POC:

Bug Discovered on March 20, 2017
Fixed on 19 April
