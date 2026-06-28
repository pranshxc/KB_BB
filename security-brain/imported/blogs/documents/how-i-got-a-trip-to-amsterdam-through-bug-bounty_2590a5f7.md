---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-07_how-i-got-a-trip-to-amsterdam-through-bug-bounty.md
original_filename: 2019-04-07_how-i-got-a-trip-to-amsterdam-through-bug-bounty.md
title: How I got a trip to amsterdam through bug bounty
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 2590a5f7c927495aa818a00e2d2d588cd9889f71695a2864766a640e354affe7
text_sha256: 5d912f7e24956430a0925440052280eb66f2843479b7b01741ea0d4b3420a783
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I got a trip to amsterdam through bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-07_how-i-got-a-trip-to-amsterdam-through-bug-bounty.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2590a5f7c927495aa818a00e2d2d588cd9889f71695a2864766a640e354affe7`
- Text SHA256: `5d912f7e24956430a0925440052280eb66f2843479b7b01741ea0d4b3420a783`


## Content

---
title: "How I got a trip to amsterdam through bug bounty"
page_title: "How I got a trip to amsterdam through bug bounty - Ninad Mathpati"
url: "https://ninadmathpati.com/how-i-got-a-trip-to-amsterdam-through-bug-bounty/"
final_url: "https://ninadmathpati.com/2019/04/07/how-i-got-a-trip-to-amsterdam-through-bug-bounty/"
authors: ["Ninad Mathpati (@ninad_mathpati)"]
bugs: ["Bruteforce"]
publication_date: "2019-04-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5322
---

[Bug Bounty](https://ninadmathpati.com/category/bug-bounty/)

## How I got a trip to amsterdam through bug bounty

![](https://ninadmathpati.com/wp-content/uploads/2019/04/brute-force-attack.png)

Hello guys welcome to my blog, Let me tell this is my first blog and will be further writing more blogs on critical vulnerabilities that i found, I hope you would find it interesting.  
So without wasting time lets move forward, Here I would like to share how I got a trip to Amsterdam with all expenses paid for 5 days. 

At this moment a majority of them would have thought the Vulnerability would be a server-side issue, but Unfortunately, its a simple Vulnerability leading to full account takeover. The vulnerability was in the login portal, I guess some of you are familiar with this vulnerability.  
First of all, let me tell you about this vulnerability which I like very much because it pays good enough & I have found it many times in different ways and the vulnerability is Full Account takeover, Account takeover can be through any method we just need to take over the account in any possible way, here the account takeover was done by Brute force on login portal. Now, what is it and how to find it?  
For those who don’t know what Brute force attack is? 

> _Brute force is a way of trying to bypass the login form or it might be any other form which needs a password to open that file or system. In simple words, we can say it’s just the process of guessing the password._
> 
>  
> 

Here what I did was I created an account and was just checking for its requests and responses by intercepting the request through burpsuit, after some time checking for the minor vulnerabilities, I went to the forgot password page. Now the real problem was here when I was requesting a password for my account the server was by default setting a new password for my account and sending it to me via mail. When I received mail I saw the password was in a format such as  
“Ab3CdF” 

![](https://ninadmathpati.com/wp-content/uploads/2020/09/Capture-1024x369-1.jpg)

and it was a 6 digit password, to reconfirm the combination I requested the password for 100 times by this I got to know that there is no rate limiting implemented on the login page and forgot password page, Now we have the format of the password and nobody is gonna check us if we use it for brute forcing the account but it’s a 6 words password still we get a hell lot of passwords and its nearly (56,800,235,584) this much, now it’s really a lot of passwords for checking one account but we have the password format, So Here we can write a python script for generating the password or there are many other tools which will do the work for you. Thus once we generate the passwords we can use the burp-suit intruder (some thing like this) 

![](https://ninadmathpati.com/wp-content/uploads/2020/09/Screenshot-251_LI.jpg)

to carry out the brute force attack. Thus this leads to Full account takeover.

  
Thus this was all about this Vulnerability. There are many other ways for full account takeover and I guess this is the easiest one to understand,  
I will be writing blogs, one by one on various ways to take over the account and my other bug bounty experiences. so this is it for the day, thank you for reading the blog. Meet you soon with something more exciting things in bug bounty/ penetration testing. 

[__ April 7, 2019](https://ninadmathpati.com/2019/04/07/how-i-got-a-trip-to-amsterdam-through-bug-bounty/)[ __Ninad Mathpati](https://ninadmathpati.com/author/hacher2202/)

[ __](https://www.facebook.com/sharer/sharer.php?u=https://ninadmathpati.com/2019/04/07/how-i-got-a-trip-to-amsterdam-through-bug-bounty/ "Share on Facebook") [ __](https://twitter.com/share?url=https://ninadmathpati.com/2019/04/07/how-i-got-a-trip-to-amsterdam-through-bug-bounty/ "Share on Twitter") [ __](http://www.linkedin.com/shareArticle?mini=true&url=https://ninadmathpati.com/2019/04/07/how-i-got-a-trip-to-amsterdam-through-bug-bounty/ "Share on LinkedIn") [ __](http://www.digg.com/submit?url=https://ninadmathpati.com/2019/04/07/how-i-got-a-trip-to-amsterdam-through-bug-bounty/ "Share on Digg")
