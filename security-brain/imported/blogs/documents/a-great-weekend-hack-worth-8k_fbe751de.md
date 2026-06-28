---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-26_a-great-weekend-hackworth-8k.md
original_filename: 2022-11-26_a-great-weekend-hackworth-8k.md
title: A great weekend hack(worth $8k)
category: documents
detected_topics:
- access-control
- xss
- sqli
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- xss
- sqli
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: fbe751de02745c87896ce806bd9c0c59c598adf7fa8d93939cf29838c272aa2f
text_sha256: 3da1ffcf41cdb3cb127f69f09a671a374c24e68c1fa2d7443d065bd0d27ea06d
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# A great weekend hack(worth $8k)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-26_a-great-weekend-hackworth-8k.md
- Source Type: markdown
- Detected Topics: access-control, xss, sqli, idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `fbe751de02745c87896ce806bd9c0c59c598adf7fa8d93939cf29838c272aa2f`
- Text SHA256: `3da1ffcf41cdb3cb127f69f09a671a374c24e68c1fa2d7443d065bd0d27ea06d`


## Content

---
title: "A great weekend hack(worth $8k)"
url: "https://infosecwriteups.com/a-great-weekend-hack-worth-8k-9bfda8ab65b9"
authors: ["Manas Harsh (@ManasH4rsh)"]
bugs: ["SQL injection", "IDOR", "Stored XSS"]
bounty: "8,000"
publication_date: "2022-11-26"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1856
scraped_via: "browseros"
---

# A great weekend hack(worth $8k)

Top highlight

A great weekend hack(worth $8k)
Manas Harsh
Follow
4 min read
·
Nov 26, 2022

488

3

Press enter or click to view image in full size
Source: Google images

This post is a writeup of my recent findings on Synack which got me $8k for 5 bugs, on a single day.

So, I was hacking on a program which was in QR period(QR period is a specific time defined by Synack where researchers with best reports are rewarded), and I had 7 hours left when I saw it. I submitted 6 bugs on this one, in which 5 got rewarded and 1 got rejected. I will define how did I go ahead and find them:)

These were the bugs I found:-

2 SQL injections
2 Stored XSS
1 IDOR(read only)

SQL injections:- These SQL injections were error based SQL injections which I found from MATCH & REPLACE funtionality in Burp. In case you don’t know what is it, it looks something like this:-

Press enter or click to view image in full size
Source: Google images

Here, as you can see you can define param values and many other things to match and replace to your desired input. I added an item for Param Value where I had to change a param value for eg. test > test’ and I got a result from it. When match and replace finds it for you, you would be able to see a different response on burp itself. You can read more about it here. It looks something like this:-

Press enter or click to view image in full size
Source:- Portswigger

You can toggle between requests and it should give you the results. Later on, I sent it to SQLmap and I was able to fetch data from it. I don’t need to tell you how does it look like, if you are reading this you probably already know:)

2nd SQL injection came in the same way, I just added test’’ instead of test’ this time and it came on another endpoint where I could escalate it further and dump data. I had to get in touch with multiple super talented SRTs for this one though. Thanks to them:)

Stored XSS:- I got two of them and won both! These XSS were quite simple and went straight. I just had to use this payload twice in input fields. I tried a few though, they didn’t work, but this one did. I just had to bypass a few filters seeing the JS output and it got reflected:)

Get Manas Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

‘><input autofocus onfocus=alert(1)>

This happened twice and it was fun to exploit them. I reckon people would’ve reported more than 30–35 XSS with same payload since its a famous one, where you use autofocus attribute to reflect JS.

IDOR:-

I submitted two IDORs too but somehow payout didn’t come that way. I could see the data of other folks with changing IDs, pretty simple. Found it on two places but got accepted in only one report. I wonder why I didnt win the 2nd. IDORs are pretty common and you still see them here and there. I used AutoRepeater for this one, which is a burp extension and it also has an option to match and replace things:)

So, a total payout:-

SQL injections:- $2900*2

XSS Injection:- $880*2

IDOR(which got accepted on an broken access Control’s payout):- $387

Tips:- Use Match and replace funtion to automate your game in bounties, and the most important one:- Write great reports, really great ones. Include everything there. Resources, Video POCs etc. Also, screenshots with every steps in a clear way.

As you can see, there was really nothing new here but what you can take from it is, spend time and check everything:) Error based SQLIs are still there, you might find one today/tonight:)

Until next time ❤

If you liked my work:- Buy me a coffee!

Twitter:- @manasH4rsh

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
