---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-17_how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty.md
original_filename: 2019-08-17_how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty.md
title: How I was able to earn 1000$ with just 10 minutes of bug bounty?
category: documents
detected_topics:
- password-reset
- xss
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- xss
- command-injection
- otp
language: en
raw_sha256: f232ae36c77da7157f2e872ea23254b445645220bd556b8603603e463641bdb3
text_sha256: bcf58f56af1b0f04664ab12de1dd10432068958f64a018be353aa894d25d7b8b
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to earn 1000$ with just 10 minutes of bug bounty?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-17_how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty.md
- Source Type: markdown
- Detected Topics: password-reset, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `f232ae36c77da7157f2e872ea23254b445645220bd556b8603603e463641bdb3`
- Text SHA256: `bcf58f56af1b0f04664ab12de1dd10432068958f64a018be353aa894d25d7b8b`


## Content

---
title: "How I was able to earn 1000$ with just 10 minutes of bug bounty?"
page_title: "How I was able to earn 1000$ with just 10 minutes of bug bounty? - Ninad Mathpati"
url: "https://ninadmathpati.com/how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty/"
final_url: "https://ninadmathpati.com/2019/08/17/how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty/"
authors: ["Ninad Mathpati (@ninad_mathpati)"]
bugs: ["Password reset"]
bounty: "1,000"
publication_date: "2019-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5078
---

[Bug Bounty](https://ninadmathpati.com/category/bug-bounty/)

## How I was able to earn 1000$ with just 10 minutes of bug bounty?

![](https://ninadmathpati.com/wp-content/uploads/2019/08/client-side-attacks-768x404-1.jpg)

Hello, Guys, I m back with a new blog on bug bounty, I found this bug recently on independent bug bounty program, thought of sharing it.

So here I would like to share how I got 1000$ with just 10 minutes of bug hunting,

here you will get to know the importance of **_client-side vulnerabilities_** ,

So here’s how it went on, earlier during my engineering 4th year, I had too much free time. This was the time I learnt a lot about this field, That time my daily schedule was like, 

**_Eat- > Sleep -> Bug Hunting -> Repeat_**

A few months back, I thought to let’s give it a try so I just picked a random website lets to say **_asdf.com_**

Now, asdf.com is a cryptocurrency exchange website, and in a general way I tried to scan the website while doing the testing I came across the login page and got to know that we can create an account and so after creating the account I found out a place where we could request for password reset for our account. On the login page there was an option of reset password so just to give it a check I requested for my password reset through that reset option, The forgot password link was something like this, 
  
  
  **_www.asdf.com/resetpsswd/email=hacker2202@asdf.com &token=aknajdnskvbskfv34tr34nj3rrff33grjqw_**

Here if you notice, there’s and email change option. I tried changing the email address and checking the link and what a stroke of luck it was just 5 minutes of testing I got the bug, but after changing the email I was not able to change the password as the site has 2-factor authentication implemented.

As the 2-factor authentication was implemented I thought we cannot do anything of it now as altering the email doesn’t work, but suddenly I saw a mail-in my altered email inbox it was from the asdf.com it was like,

I got a new reset password link of that account to my altered email address.

So what was happening was 

when we are requesting a password reset for our account we were getting a mail and that reset password link had token expiration vulnerability ( it was not expiring the token after one use)

2nd the problem was when I was altering the email and processing the link I was able to get a new reset link to my altered email address of the victim’s account (not exactly same but something like Http pollution attack)

  * ![](https://ninadmathpati.com/wp-content/uploads/2020/09/1000.png)

So in this way, I was able to earn good, client-side attacks also pay very well if we show the **_attack scenario properly_**.

What might be the fix for this type of issues?

  * _Token Verification & Expiration._
  * _Avoiding unnecessary Parameters Like Email_
  *  _Implementation of 2 Factor-Authentication._
  * _Most importantly checking the workflow of that section_

This was just an example for client-side attack I will be discussing in detail about client-side attacks in my further blogs (Will publish it soon)

> “So Next time you see any parameter try to play with it who knows you might get lucky and get some bucks added to your account”

This blog I have only made for the specific findings only, Do Subscribe to my blog if you find it useful!!!

**_Hint for the next blog:_** Is it possible to hijack a browser through XSS?

[__ August 17, 2019](https://ninadmathpati.com/2019/08/17/how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty/)[ __Ninad Mathpati](https://ninadmathpati.com/author/hacher2202/)

[ __](https://www.facebook.com/sharer/sharer.php?u=https://ninadmathpati.com/2019/08/17/how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty/ "Share on Facebook") [ __](https://twitter.com/share?url=https://ninadmathpati.com/2019/08/17/how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty/ "Share on Twitter") [ __](http://www.linkedin.com/shareArticle?mini=true&url=https://ninadmathpati.com/2019/08/17/how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty/ "Share on LinkedIn") [ __](http://www.digg.com/submit?url=https://ninadmathpati.com/2019/08/17/how-i-was-able-to-earn-1000-with-just-10-minutes-of-bug-bounty/ "Share on Digg")
