---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-23_all-about-getting-first-bounty-with-idor_2.md
original_filename: 2020-06-23_all-about-getting-first-bounty-with-idor_2.md
title: All About Getting First Bounty with IDOR
category: documents
detected_topics:
- idor
- access-control
- command-injection
- automation-abuse
- cloud-security
- mobile-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- automation-abuse
- cloud-security
- mobile-security
language: en
raw_sha256: cbc9d2ef8e3fee78f7357ab9f37a5276504ea91289511c7164b3d0d7fa8d17df
text_sha256: 3645b221eeb9241b97e494d33f1bcbf22129958603afd52c6cbe18be0edcd8e1
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# All About Getting First Bounty with IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-23_all-about-getting-first-bounty-with-idor_2.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, automation-abuse, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `cbc9d2ef8e3fee78f7357ab9f37a5276504ea91289511c7164b3d0d7fa8d17df`
- Text SHA256: `3645b221eeb9241b97e494d33f1bcbf22129958603afd52c6cbe18be0edcd8e1`


## Content

---
title: "All About Getting First Bounty with IDOR"
url: "https://medium.com/bugbountywriteup/all-about-getting-first-bounty-with-idor-849db2828c8"
authors: ["Mukul Trivedi (@M0hn1sh)"]
bugs: ["IDOR"]
publication_date: "2020-06-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4473
scraped_via: "browseros"
---

# All About Getting First Bounty with IDOR

Mukul Trivedi (M0hn1sh)
Follow
4 min read
·
Jun 23, 2020

1.5K

4

All About Getting First Bounty with IDOR

Press enter or click to view image in full size

Hello All,

In April ’20, I started reading and practising about IDOR, for the first few days it was looking hard to find IDOR vulnerability. So I went back to different practise labs to get a wider Idea about this vulnerability and various ways to exploit this vulnerability. I have practised on DVWA, bWAPP, and Portswigger Academy.

According to OWASP :

“ Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability attackers can bypass authorization and access resources in the system directly, for example database records or files. Insecure Direct Object References allow attackers to bypass authorization and access resources directly by modifying the value of a parameter used to directly point to an object. Such resources can be database entries belonging to other users, files in the system, and more.”

Writeups and Mindmap which I followed are shared at the end of this writeup.

In this writeup I am sharing few of the scenarios which I reported to a Program. Lets say, I have created 3 users on a website which are User_1, User_2 and User_3 with the same role and permission :

Scenario #1 : There was a functionality, when a user creates a post and someone can like, comment and share that post on their profile. But while checking this functionality I noticed that the other user can only mention the author of that post in the comment and the mentioned person receives the notification of the same.

Get Mukul Trivedi (M0hn1sh)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Detailed attack scenario :

User_1 created a post.
Now when User_2 comments on that post, I noticed that I can mention only author of that post which in this case is User_1.
So, captured the comment (comment is : Please check @User_1) request in Burp and JSON data was passing like this:
{“text”:”Please check @[User_1 name]”,”mentions”:[{“uid”:”random 9 digits",”key”:”User_1 name"}],”message_id”:random 9 digits}
in the above JSON data, the uid is of User_1 and By visiting the profile of User_3 and by doing “inspect element” on the profile picture of User_3, I can get the uid of user_3.
So in the JSON data, changed User_1 name to User_3 name in the both values and replaced uid of User_1 to uid of User_3.
Finally I was able to mention any other user in that post and the mentioned user gets notification of it.

Program rewarded me $$$ for this bug and this was my first ever bounty :D

Scenario #2 : There was a functionality to either Join a group or Create a group, after creating a group the user gets a group_code which he can share with other users and that referred user will get add in the group without approval of owner of the group.

Detailed attack scenario :

User_1 selects on “Create a group” and after giving a name and adding discription to the group, User_1 gets a refer_code (random 6 words eg. pgytsd) for the group.
Now User_2 selects to “Join a group” and enters pgytsd in the code and I captured this request.
So, in “Join a group” request the JSON data was passing like below :
{“membership”:{“access_code”:”pgytsd”}}
I just needed to change or bruteforce on the access_code
After changing the group code I was getting added into Any users group and also in the Burp response, User_2 was able to see the name and description of that group also the name and uid of the owner of that group.

Another IDOR and again I was rewarded $$$ for this bug.

#Blogs /Writeups :

How-To: Find IDOR (Insecure Direct Object Reference) Vulnerabilities for large bounty rewards |…
The following is a guest blog post from Mert & Evren, two talented researchers from Turkey. IDOR vulnerabilities are of…

www.bugcrowd.com

swisskyrepo/PayloadsAllTheThings
Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied…

github.com

Insecure Direct Object Reference (IDOR) — Intigriti
An Insecure Direct Object Reference can be one of the easiest bugs yet they can have a very big impact. IDOR is still a…

blog.intigriti.com

IDOR Bugs are Pure Love($7k+$250)
Hi Hunters! Greeting for the Day, This is to inform you that , I cannot disclose the name of the company because of Non…

medium.com

How critical is IDOR vulnerability? Can it take down a whole company? ~ Ninad Mathpati
Hello people, hope you are doing good and playing well with security! Today I am here again with a topic known as…

ninadmathpati.com

A Less Known Attack Vector, Second Order IDOR Attacks
Most of you probably familiar within the vulnerability types “IDOR (Insecure Object Direct Reference)” and second order…

blog.usejournal.com

Everything You Need to Know About IDOR (Insecure Direct Object References)
I’ve started a new journey in this quarantine times and decided to investigate OWASP Top 10 and write about it as much…

medium.com

List of bug bounty writeups
Home AMA Challenges Cheatsheets Conference notes The 5 Hacking NewsLetter The Bug Hunter Podcast Tips & Tricks…

pentester.land

Insecure Direct Object Reference Prevention
Insecure Direct Object Reference (called IDOR from here) occurs when a application exposes a reference to an internal…

cheatsheetseries.owasp.org

How to find more IDORs
And maximize their impact while hunting for bugs.

medium.com

#Mindmap :

Web App Pentest
Web App Pentest 2.1.1. POC 2.1.1.1. Subdomain Take-over poc's github -https://hackerone.com/reports/363778 aws …

www.mindmeister.com

#Burp Extensions :

Autorize
Autorize is an extension aimed at helping the penetration tester to detect authorization vulnerabilities, one of the…

portswigger.net

Auto Repeater
This extension automatically repeats requests, with replacement rules and response diffing. It provides a…

portswigger.net

There is a video by STÖK, which explains very well about how to use Autorize and Auto Repeater :

As this is my first writeup, sorry if there is any mistake :D

Connect with me :

Linkedin : https://in.linkedin.com/in/m0hn1sh

Twitter : https://twitter.com/M0hn1sh
