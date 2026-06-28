---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-02_the-database-handover-a-dumb-mistake-critical-bug_2.md
original_filename: 2022-09-02_the-database-handover-a-dumb-mistake-critical-bug_2.md
title: The Database Handover | A Dumb Mistake | Critical BUG
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- otp
- rate-limit
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- otp
- rate-limit
- information-disclosure
language: en
raw_sha256: 53ed0940e3426b6a6b75df2f01cf6e696606a3e03cb008bc23b9f5b7098442c6
text_sha256: 9f40a0c95ba4941635a210805cb4fd286a7f9c45e3475855cd6823fdec2ca8ee
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# The Database Handover | A Dumb Mistake | Critical BUG

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-02_the-database-handover-a-dumb-mistake-critical-bug_2.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, otp, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `53ed0940e3426b6a6b75df2f01cf6e696606a3e03cb008bc23b9f5b7098442c6`
- Text SHA256: `9f40a0c95ba4941635a210805cb4fd286a7f9c45e3475855cd6823fdec2ca8ee`


## Content

---
title: "The Database Handover | A Dumb Mistake | Critical BUG"
url: "https://mr23r0.medium.com/the-database-handover-a-dumb-mistake-critical-bug-f73c99e72e40"
authors: ["Saransh Saraf (@mr23r0)"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2022-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2225
scraped_via: "browseros"
---

# The Database Handover | A Dumb Mistake | Critical BUG

The Database Handover | A Dumb Mistake | Critical BUG
Saransh Saraf aka (MR23R0)
Follow
4 min read
·
Sep 2, 2022

222

4

Hi hackers & Security Enthusiasts, I’m Saransh Saraf and this a simple bug with a critical Impact. I hope you’ll enjoy it and learn something from it.

Press enter or click to view image in full size
The Wakeup Call :

Have you ever used these type of tools ?

ShareIt
Xender
Inshare
ShareMe

If yes, then you’re gonna enjoy it, if you never used it than I don’t believe that you ever lived your 13 age 😂 Go and try using one now before reading it further.

“These tools are used to share Data from one device to another, and sometimes also helps to switch devices (move data from one to another)”

The Beginning of the Story :

I had a Pentesting Contract from a big German Company, and I earned 1000 Euros from it….. :) For :

Email Verification Bypass (2 Methods)
Stored Cross Site Scripting
Insecure Direct Object reference (IDOR) leaking Employee Data
Broken Link Hijacking
Press enter or click to view image in full size
first round

So I again Started to look for more bugs and called it #2 Round. I had mapped the whole infrastructure in the #1st Round.

So this time I had small and well-mapped scope for testing, So I started to revisit my old issues (to try bypassing these) but this “Broken link hijacking” returned as a weird result,…. For fixing it The Company changed the whole child company name & also the domain.

The Ritual of Comparing :

After visiting the new domain “IAMNEW.COM” I saw something really terrible form of “moving on”. All subdomains were totally Identical…. and I started to get demotivated that I’m not gonna find anything new here, but by mistake I viewed my wappalyzer and saw “Wordpress 4.8” banner.

Finally seeing some way to find bugs
The Ritual of Background Enumeration :

I quickly started my WPSCAN but I didn’t get any amazing results, Obviously I was sad & frustrated… so I gave myself 30 minutes and started thinking what can I do now, but after a couple of thoughts I got a spark I recalled A Line of my Mentor/ Inspiration “If you wanna do something to make sure you do your best”

Get Saransh Saraf aka (MR23R0)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Without waiting a minute I made a WordPress API token and ran it in the background, meanwhile I started my manual recon and testing but No luck :(
So I came to look at the WpScan results, And saw “debug.log is publicly accessible"

The Ritual of Dumb Mistakes :

I started looking at the log, and I found list of Users and some Auth keys and reported it as an “Information disclosure”

Press enter or click to view image in full size

But I was still feeling dumb, my Gut feeling was telling me that I’m missing something, So I again started to look at the log and I found the Database Name so I again added it in my previous “Information disclosure”

But still, something was missing, “my mind was keeping telling me to look deeper you dumb idiot” so took a cup of tea and viewed the log on my TV (for better preview) after reading 580 lines of logs I found the treasure:

Press enter or click to view image in full size
backup

But I again did the dumb mistake, I saw that the backup size is >500MB so reported it as Possible Denial of Service (DOS) because I was unable to extract it, I never encountered a file like this backup before. :(

The Miracle :

The Next Day I was still thinking about this file “. Daf” questing myself why? Why are you so dumb?

So I started again looking for the answers, after reading some threads on stackoverflow.com I moved myself to YouTube and after trying multiple search queries I finally found a video and really great tutorial :

Windows Tool

After navigating nested folders, I’ve found the Database backup SQL file under: dup-installer/database.sql
It was containing All users, password hashes and much more juicy stuff :)

The BUG :

As we have used the file transfer applications, similar thing is available in Wordpress which is called “Duplicator” which allows the admin to make a copy of the existing Wordpress Application and it’s too easy to use.

But sometimes developer forgets to remove the Backup files to remove from the new server (domain)

Simple isn’t it?

Discovery :

There is a list of files that you may find in the backup:

wp-config.bak (wordpress config backup)
All users Info
full database backup (containing Users with password hashes & articles)
all articles (including unlisted & drafts)
all wordpress files (for static analysis)

You may have to dig between folders and unique files, but I can promise you one thing at the end of the I’ll be worth it.

I’m constantly working on discovering new vulnerabilities so stay connected for more content. :)

Linkedin :

https://www.linkedin.com/in/saransh-saraf-2b514b20b
