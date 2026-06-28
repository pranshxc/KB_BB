---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-28_admin-panel-accessed-via-sql-injection-ezy-boooom.md
original_filename: 2021-02-28_admin-panel-accessed-via-sql-injection-ezy-boooom.md
title: Admin Panel Accessed Via SQL Injection… (Ezy Boooom…😅)
category: documents
detected_topics:
- xss
- sqli
- ssrf
- command-injection
- path-traversal
tags:
- imported
- documents
- xss
- sqli
- ssrf
- command-injection
- path-traversal
language: en
raw_sha256: 95b0bbb953141922efb18d20ea77a29a370338b43515b71c79256729c8a5f83e
text_sha256: 0fbd56ff7e955f7e8118668f9ab0b2e9a4560b8afa607dbe5b6561ce81941b93
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Admin Panel Accessed Via SQL Injection… (Ezy Boooom…😅)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-28_admin-panel-accessed-via-sql-injection-ezy-boooom.md
- Source Type: markdown
- Detected Topics: xss, sqli, ssrf, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `95b0bbb953141922efb18d20ea77a29a370338b43515b71c79256729c8a5f83e`
- Text SHA256: `0fbd56ff7e955f7e8118668f9ab0b2e9a4560b8afa607dbe5b6561ce81941b93`


## Content

---
title: "Admin Panel Accessed Via SQL Injection… (Ezy Boooom…😅)"
url: "https://medium.com/@ratnadip1998/admin-panel-accessed-via-sql-injection-ezy-boooom-57dc60c2815f"
authors: ["Ratnadip Gajbhiye (@scspcommunity)"]
bugs: ["SQL injection"]
publication_date: "2021-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3854
scraped_via: "browseros"
---

# Admin Panel Accessed Via SQL Injection… (Ezy Boooom…😅)

Admin Panel Accessed Via SQL Injection… (Ezy Boooom…😅)
Ratnadip Gajbhiye
Follow
3 min read
·
Feb 28, 2021

450

8

Hello All,

I’m back again with a new write-up...
Again this article is about Admin Panel Access…( This is my 4th write-up on Admin Access more on the way…) 🤩

Consider company name as “target.com”.😅

I’m a very lazy person…😂 I don’t do anything manually… So I used some GitHub tools that you guys already know and my private tools too…🤔

Tools I used to find vulnerable URLs : waybackurls , gau , gf & gf patterns…🤗

I ran waybackurls & gau on “target.com” grabbed all the URL’s… (Total Urls found 10k+)😐

After that i used GF-Patterns for finding possible vulnerable urls (Like XSS,LFI,SSRF &SQLI..)🧐

Using GF-Patterns found 1k+ Possible SQL vulnerable urls but many of them are dead urls.😒

Httpx is another great tool by project discovery… I used httpx for filtering live urls…😋

After that i filters all the live Possible SQL urls using Httpx….(Total urls 379)🙄

Its impossible to check all 379 urls manually for SQL injection… I used my private tool for Identifying & Exploiting all the urls...😎

Get Ratnadip Gajbhiye’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I ran private tool on Possible SQL urls, After few minutes later tool indetifed SQL Injection vulnerability and also start auto exploiting the target…😇

So it’s enough to report but i dig more into DB and found admin Credentials..🥰

Now I got the credentials but don’t know where to use because i used my another tool “Admin finder” but there is no panel in targeted website. I tried all the possible things but no success… 😴

Then i checked source code of the website > ctrl+f then “https://” and i found many links but this “https://ws1.webservices.nl/” url grabbed my attention.😚

I open this url in new tab and surprisingly found login panel…🤭

I login this panel using that credentials…🥺

And successfully gained access to the admin panel…🤪

Press enter or click to view image in full size

I immediately reported this issue to the security team and in response the words of the security team made my day…😊

Press enter or click to view image in full size

Reported > Fixed after 25 days > $$$…🤩

Always dig more and never ever lose hopes…🙂

I hope you enjoyed this article and i apologize for my weak English if there is any mistakes in this post.😅
Thanks for reading my article, 😁
Stay home... Stay safe..😏
have a great day...🙂
