---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-07_how-i-got-1000-by-clickjacking.md
original_filename: 2023-02-07_how-i-got-1000-by-clickjacking.md
title: How I Got +1000$ by Clickjacking
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
- clickjacking
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
- clickjacking
language: en
raw_sha256: cb484d87d4b3c9f7f52a5c6c270b66ac1f8166100293d8ed3814a857c931f673
text_sha256: 1344a801dad21176aabb896c82a96df4b83a071ec4c36d2b8f387eed8fa3a42c
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got +1000$ by Clickjacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-07_how-i-got-1000-by-clickjacking.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf, clickjacking
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `cb484d87d4b3c9f7f52a5c6c270b66ac1f8166100293d8ed3814a857c931f673`
- Text SHA256: `1344a801dad21176aabb896c82a96df4b83a071ec4c36d2b8f387eed8fa3a42c`


## Content

---
title: "How I Got +1000$ by Clickjacking"
url: "https://medium.com/@mydudehello91/how-i-got-1000-by-clickacking-233e89d76ffd"
authors: ["Aryan W13DOM (@NeuRosis23)"]
bugs: ["Clickjacking"]
bounty: "1,000"
publication_date: "2023-02-07"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1564
scraped_via: "browseros"
---

# How I Got +1000$ by Clickjacking

How I Got +1000$ by Clickjacking
W13DOM
Follow
4 min read
·
Feb 7, 2023

21

As-Salaam-Alaikum (Peace be unto you) Hello Amazing hackers My name is Aryan I am a Bug Bounty Hunter. This is my Third Write-up, hope You guys will enjoy it and learn something new from it.

In this story I’m explaining a vulnerability that I reported to a programs and i got +1000$ also secure 5 company with it in Hackerone, my english is not perfect and its not my mother language so please never mind if I have some problems with the grammar, all I need is you to understand what I'm talking about exactly.

First Of All , Clickjacking is an attack that fools users into thinking they are clicking on one thing when they are actually clicking on another. Its other name, user interface (UI) redressing, better describes what is going on.

How To Detect Manually and Tools:

At This Time We Know What is it , Now Time To How Can Find it When Some of Programs Put In OOS , There are a lot of ways to check the vulnerability on targets , First way check the target in the burp suite by the missing of headers known as ` X-Frame` Also You can use inspect element as this way :

1: Right-click on the page and select "Inspect." This will open the Chrome DevTools.
2: Click on the "Network" tab.
3: Refresh the page and look for a request to the website's main URL.
4: Click on the request to inspect its details.
Scroll down to the "Headers" section.

For both of them You should look at the headers So If the developer set the headers like as :
Missing The X-Frame
Missing CSP or Value isn't `none´ or `frame-ancestors´
The target may be vulnerable as i know, but if Set The X-Frame and CSP Value Equal to 'none' or 'frame-ancestors' means that the website protected and not vulnerable , the fast way you can use is the online tool called ` clickjacker.io´ Its all about how detect the vulnerability Manually or By Tool Also How We Know The Websites are Vulnerable.
The Last Point Use The Iframe Html Tag In Your Code To Embedding The Target To Your Server Or Localhost To Create a PoC.

How The Programs Triaged it?

As i mentioned above some of programs Don't triaged it without any Impact , so what should we do:)

Press enter or click to view image in full size
Press enter or click to view image in full size
Photo by Alvaro Reyes on Unsplash

In This Case we Should Going Deeply On The Target and Functionalities as Mr.Robot , I Talking about some cases that i found and i Saw._.

Get W13DOM’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First Case , Look At The Delete Account or Update Functionality , Some Programs Have this Functionality and Programs Triaged If You Found It In This way with Goof Proof Of Concept.

Second Case , Chaining With Another Vulnerability Such as Self-Xss , Csrf.

Sometimes You Found Self-Xss But As you know its OOS So To Deliver To Victims You Can Use With Clickjacking Then Report it as Valid Issue , For Csrf Sometimes Programs have an Endpoint about Csrf Token In That Case an Attacker can Bypass The Csrf Protection By Chaining the Clickjacking with Csrf That Leads To Update Password or Setting Etc.

Third Case , When You Found An Endpoint That Contain Sensitive Information Such as Credit Cards , Api Token , Access Token , Personal Information Etc .
You Can Use The Clickjacking To Steal it By Javascript or Burp Collaborator , if it happen and Report it Triaged as High or Critical

For Both Of Them To Create PoC Depend On Your Idea How To Deal With Them as Html and Css , Also Have Other Cases But You Should Focus The Functionality and Fire Your Brain as Hackers So You Can Get So Many Triage Report When You Beginner Or Intermediate Not Problem Just Hard Work:)

I Reported 5 Cases That Contain Above case Such as Deleting account and Self-Xss To ATO and Stealing Api Token , Two Of Them Rewarded Me 1000$ Alhamdulilah.

That's All About Clickjacking Cases and Detecting Also Known It, I Hope You Enjoy and learn Something new._. Let a Claps If You Liked -.-

Some Write-Ups You should Read It:

Chaining Csrf with Clickjacking>>>>https://link.medium.com/4MYmasC0cxb

Clickjacking to Steal Sensitive Informations>>https://link.medium.com/rnJ4miFJdxb

Metamask Reward Researchers That Found Clickjacking To Steal ETH >>>>https://link.medium.com/2rQPE9SJdxb

Chaining Self-Xss With Clickjacking>>>https://link.medium.com/zdmzfF8Jdxb

Follow me In Twitter : https://twitter.com/NeuRosis23

Subscribe My Youtube Channel:

https://youtube.com/@AryanGaming12
