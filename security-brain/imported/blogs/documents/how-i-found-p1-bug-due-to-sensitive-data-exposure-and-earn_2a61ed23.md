---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-15_how-i-found-p1-bug-due-to-sensitive-data-exposure-and-earn-.md
original_filename: 2021-11-15_how-i-found-p1-bug-due-to-sensitive-data-exposure-and-earn-.md
title: How I Found P1 bug Due to Sensitive data exposure And Earn $$$$
category: documents
detected_topics:
- access-control
- xss
- sqli
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- access-control
- xss
- sqli
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 2a61ed2315333cfd92bac40e8bfcc7dff503e4cf3dbcca57b698a979fec20908
text_sha256: f99b9d2f478f8e7dc997d62eefa5c5ec63b69a46b96cda1751aa283ae3b966d9
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found P1 bug Due to Sensitive data exposure And Earn $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-15_how-i-found-p1-bug-due-to-sensitive-data-exposure-and-earn-.md
- Source Type: markdown
- Detected Topics: access-control, xss, sqli, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `2a61ed2315333cfd92bac40e8bfcc7dff503e4cf3dbcca57b698a979fec20908`
- Text SHA256: `f99b9d2f478f8e7dc997d62eefa5c5ec63b69a46b96cda1751aa283ae3b966d9`


## Content

---
title: "How I Found P1 bug Due to Sensitive data exposure And Earn $$$$"
page_title: "How I found P1 bug due to Sensitive data exposure and earn $$$$ | Medium"
url: "https://piyushshuklabug.medium.com/how-i-found-p1-bug-due-to-sensitive-data-exposer-and-earn-99ebcb342bcd"
authors: ["Piyush shukla (@PiyushShukla__)"]
bugs: ["Information disclosure"]
publication_date: "2021-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3170
scraped_via: "browseros"
---

# How I Found P1 bug Due to Sensitive data exposure And Earn $$$$

How I Found P1 bug Due to Sensitive data exposure And Earn $$$$
Safe Edges
Follow
2 min read
·
Nov 15, 2021

331

5

.

Hello ,Hackers I hope you all are doing great. Keep finding bugs and even if you are not finding them, keep putting efforts in it . Here we will talk about a bug which I found recently.

So recently I started a program which is program.com . A small intro about program.com , it is a bug bounty platform like bugcrowd and hackerone. So i decide to find bug in private program.

Now lets’ begin

so i started searching bugs in program like my fav ATO and xss,sqli,htmli.. etc

Press enter or click to view image in full size

But it didn’t work! :(

Get Safe Edges’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After investing lot of time in these bugs i tried finding some juicy data . I went through my profile page and opened view source page, and started searching token or any api key but suddenly i saw that my email , user id and other sensitive data was visible on the source page. I thought because i have logged in thats why my data is available , but then i logged out of my account ( in program every users profile are publicly available in site ) and i simply searched http://program.com/bugtester , and opened my profile and went to the view page source and ,

BOOM !!

I was shocked that i can see my whole data without any authorization , now i was thinking about how i can access other users data too , now i simply use “ wayback urls “ i get lots of username and then i opened users one by one and check page source , AND YES I can access every users data without any authorization

I immediately created poc and submitted an issue in program. After 2–3 days i received reply like this

Now bug is Fixed

Tips = Patience is a key
