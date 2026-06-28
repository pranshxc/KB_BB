---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-03_a-unique-xss-scenario-in-smartsheet-1000-bounty.md
original_filename: 2019-02-03_a-unique-xss-scenario-in-smartsheet-1000-bounty.md
title: A Unique XSS Scenario in SmartSheet || $1000 bounty
category: documents
detected_topics:
- xss
- idor
- ssrf
- sqli
- command-injection
tags:
- imported
- documents
- xss
- idor
- ssrf
- sqli
- command-injection
language: en
raw_sha256: 1627576b4d36b177ff96f91dd081dfdbd26bf35fce159b94330cc77c634dceb8
text_sha256: 577cd27aea823b1af8ce8bb1bad04c7108bc4d21f03fc60cce38010ddf50b230
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# A Unique XSS Scenario in SmartSheet || $1000 bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-03_a-unique-xss-scenario-in-smartsheet-1000-bounty.md
- Source Type: markdown
- Detected Topics: xss, idor, ssrf, sqli, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1627576b4d36b177ff96f91dd081dfdbd26bf35fce159b94330cc77c634dceb8`
- Text SHA256: `577cd27aea823b1af8ce8bb1bad04c7108bc4d21f03fc60cce38010ddf50b230`


## Content

---
title: "A Unique XSS Scenario in SmartSheet || $1000 bounty"
url: "https://medium.com/@rohanchavan/a-unique-xss-scenario-1000-bounty-347f8f92fcc6"
authors: ["Rohan Chavan (@rohanchavan1918)"]
programs: ["Smartsheet"]
bugs: ["Stored XSS"]
bounty: "1,000"
publication_date: "2019-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5435
scraped_via: "browseros"
---

# A Unique XSS Scenario in SmartSheet || $1000 bounty

A Unique XSS Scenario in SmartSheet || $1000 bounty.
Just another XSS POC writeup ..!!!
Rohan Chavan
Follow
6 min read
·
Feb 3, 2019

198

2

TLDR: This is an writeup of a recent bug which I found in smartsheet .It was an stored xss, but the way it was getting triggered was really great from the perspective for hackers, js was getting executed when any user clicks on the malicious notification , this could let any user takeover any account (with vertical and horizontal privileges ) which increased the severity of the Bug.The security team of the program was very professional and understood the scenario very well.

Before we move forward, I’d really like to thank the smartsheet security team for this coordinated disclosure.

Hello guyzz .!!! Thanks for your support and blessings.I hope you all are doing fine and are excited to read about this writeup because of the click-bait Title. So without wasting any time further, lets get straight into it.

Its only been 2–3 months since I started bug-bounty.Before that I used to spend most of my time on hackthebox.eu and play CTFs ,back then I had tried bugbounty but I wasnt getting anything , after getting a -ve signal on my H1 profile because of NA’s , I got frustrated/depressed and left that track. (One of the Biggest mistake I ever did)

From the last two month I decided to give 3 hours a day to bugbounty because I wanted to give oscp and didn’t wanted to put that burden on my parents back (P.S I am a student and not yet working).So the only option I was seeing to earn that money for my OSCP fees was BugBounty. And it worked out ..!!!

I started with Points only programs in bugcrowd (Yeah I love bugcrowd, already had a bad experience with h1) because professional hunters don’t hunt for points.I was also testing wordpress plugins, most of them are Damn Buggy. Last month I reported around 5 bugs but this was the scenario.

report’s stats

But then I got my first bounty from ZOHO, ( I have provided a link to it at the end of this writeup) .Then I saw smartsheet in the bugcrowd programs directory,

Press enter or click to view image in full size

It has a very catchy tagline which intimate any hacker/researcher to test their skills on the program. I was like ..!!

Challenge Accepted ..!!

I then read the program rules and scope, I saw a lot of researchers in recently joined (more than 500) as it was an old program, which makes it even tough. But I wanted to test myself. It was around 5pm when I started basic recon, started a nmap full port scan (this is the habit of all the HTB dudes, everything starts with NMAP …hahaha). Since it was going to take a while, i decided to signup and see what it actually is, because till that moment I had never came across that platform. I signed up and started wandering here and there, trying what all privilages do a normal user have. In that program a user is able to make a sheet somewhat similiar to Ms. Excel (Go signup and check them out ..!!!). we could give access of that sheet to various users of that program to manage the sheet, suppose I am tester , and I could give access to other person suppose victim1 , It is a cool feature isnt it ? but wait ..!!! whenever tester makes any change in the document, victim1 could be notified about it. (This is the main attack scenario, have written in brief about it further.)

So I spent next few hours trying a lot of things like IDOR, sqli, also xss’s but since it was an old program mostly all the user inputs were properly sanitized and handled.

It was really testing me.

I started at 5pm and it was 9 pm now, I had dinner and started again at 9:30. But I had decided to not give up easily on it, like i used to do earlier.I motivated myself and got mentally prepared to spend next 2–3 days on it.Now I started fuzzing their api, and left it to run and got back to the main webapp. I was manually going through each and every request and response had lots of repeater tabs open , things started getting messy.

It was now 11 pm, I plugged in my earphones psy-trance was playing and I was in the Trip of hacking.

It popped my mind that I haven’t tried SSRF yet, and saw that I can attach link through attachment’s. I linked scanme.nmap.org:22 and in the link name parameter I entered the payload “><img src=x onerror=”alert(1)”> .But this time I enabled the notifications, and attached the link to the document.After a minute I saw the notification appeared. I clicked on the notification and saw that the html content after clicking on notification got a bit misplaced because of the above payload. Then I saw the markup near the link name parameter. and modified the payload as “>”><img src=x onerror=”alert(1)”> and attached the link.

XSS payload

Attached the link , nothing happened on the sheet. I continued to look for other things, After a few minutes I got the notification that attachment has been added to the document.

Notification

When I clicked on that notification XSS got executed ..!!!

Press enter or click to view image in full size
XSS triggered ..!!!

So we now have an XSS, but how can I increase the impact !!! If you have read above , there is a feature in smartsheet which would allow you to notify/alert other users, what if another user suppose victim ,gets the malicious notification and he clicks on it ?? Yes then he will be truly a victim of the attack.It could be an account takeover. If attacker attaches an malicious attachment, and the true owner of that page clicks on the notification, his account would be compromised.

Get Rohan Chavan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We have an Account Takeover ..!!!

Until this It was around 12.30 pm. I wrote a nice report and made a video POC and submitted the report on bugcrowd.

I did it ..!!!

Report Time Line :

Submitted report on Bugcrowd — 3 October 2018 19:21:24 UTC.

Requested more info — 5 October 2018.

Info Provided — 6 October 2018.

Report Triaged — 10 October 2018.

Awarded 20 points and $1000–12 October 2018

Requested for disclosure — 12 October 2018.

Status changed to Resolved — 16 October 2018.

Agreed for coordinated disclosure — 16 October 2018.

Write up published — 3 February 2019.

Thanks for reading ..!!!

I am looking for an opportunity in infosec (mostly an Internship, or part time jobs). I am good in Web Application security , also am a certified php developer and python enthusiast. I have written some hacking tools and other cool stuff. So if You hire for your company I would like to apply (Remote or in Mumbai). You can find me here https://p5yph3r.github.io/

Some of my other writeups :-

My Writeup on Zoho Bug ..!!!

$100 Bounty in 300 seconds isn’t bad !!!
Hey guyzz …!!! I hope you are fine and doing absolutely awesome in your own fields. Thanks for the awesome response on…

medium.com

Social Engineering — because there is no patch for Human Stupidity ..!!!
Before God we are all equally wise — and equally foolish.

medium.com

Writing A Simple Directory Bruteforcing Tool with 25 Lines of Python
It was a boring friday noon, I was in my college having DSP (Digital Signal Processing) practicals, it was actally a…

www.secjuice.com
