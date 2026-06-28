---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-15_how-i-accidentally-got-my-first-bounty-from-facebook.md
original_filename: 2020-09-15_how-i-accidentally-got-my-first-bounty-from-facebook.md
title: How I Accidentally Got My First Bounty From Facebook
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
- api-security
- cloud-security
language: en
raw_sha256: 8417f5c45b6b61fbd032469c61f662a35494bb434b675b41d95d2b51bd640436
text_sha256: 4ba19b8f4562907c7d87cabd6ca48da99b30c4b3875b2c2e19d3ea03cf9fbbe3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I Accidentally Got My First Bounty From Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-15_how-i-accidentally-got-my-first-bounty-from-facebook.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `8417f5c45b6b61fbd032469c61f662a35494bb434b675b41d95d2b51bd640436`
- Text SHA256: `4ba19b8f4562907c7d87cabd6ca48da99b30c4b3875b2c2e19d3ea03cf9fbbe3`


## Content

---
title: "How I Accidentally Got My First Bounty From Facebook"
url: "https://medium.com/bugbountywriteup/how-i-accidentally-got-my-first-bounty-from-facebook-facebook-bug-bounty-2020-c12bd2ad8575"
authors: ["Bishal Shrestha (@bishal0x01)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2020-09-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4262
scraped_via: "browseros"
---

# How I Accidentally Got My First Bounty From Facebook

How I Accidentally Got My First Bounty From Facebook
Facebook Bug Bounty 2020
Bishal Shrestha
Follow
4 min read
·
Sep 15, 2020

468

1

Hello readers,

After a very long time I am come back with a new write up. This write up is about how I got my first bounty from Facebook for reporting a functional security issue. So I hope this write up is not much technical. Note: If you don't have much time in reading this write up you can jump to the the video which is in the bottom of the write up!

Story about how this happened?

I was planned to do a meetup for a group using “Messenger Rooms”. Facebook has launched its latest videoconferencing feature, Messenger Rooms, which allows up to 50 people to video chat at a time. There’s no limit to how long you can talk, and you don’t even need a Facebook account to join a room. I already posted a status and another day I commented that “messenger room” join link so everyone can join using that link in the meeting. But after posting that link while i try to open that post. I got an error and did not able to view that post.

Press enter or click to view image in full size
After opening the comment I got this error.

At that moment I did not realized that it is an issue. Next day I again try to moderate that post but I still unable to do something! So I thought it is something. Then I requested to one of friend to view that group post from FB Lite. And he try open that link on FB lite he also get the same error. Then I decided to report it!

Whats write up is it about?

This write up is about how I got my first bounty from Facebook for reporting a security issue.

What is Bug Bounty?

Bug bounty is a reward that is paid to security researcher or bug bounty hunter who finds security flaws in the companies application or software. Some of companies offer money, some of companies gives recognition and gives thanks by mentioning researchers name in their website for reporting security issues. In the case of Facebook they offer reward($$$) and listed their name via https://www.facebook.com/whitehat/thanks/

How I reproduced this issue:

First I logged on two account as a attacker and user[victim] in a Facebook and FB lite.
As a attacker I go to the messenger application and copied the “messenger room” join link and go to the another user’s[victim’s] profile picture and commented that link using Facebook.
Then I opened the FB Lite as a victim and when try to open that comment. Victim will get an error! to open that comment along with other’s comment!

While I reporting the issue issue I only found on FB lite Group comment. But while further testing its affected to the every “Comment able section” including any user post, page post, event post etc.

Whats the impact of this issue?

Get Bishal Shrestha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

An attacker can simply comment the messenger room join link in the profile picture, FB pages, groups, events admin or any user will unable to moderate that comment!

Whats the root cause of this issue?

I asked to Facebook security team after fixed the issue. But they send this response “unfortunately we can not provide any further information on the fix or the root cause.”

If you found this kind of issue what should you do?

If you find any issue and which is related to security, privacy which it affects to the users or directly violates the user’s privacy. Then you can go to the www.facebook.com/whitehat/report and just fill the form with how you find the issue with steps and its impact! The Facebook Security Team will review and will get response accordingly!

Sometimes I thought FB Bug bounty is all about luck also! While searching for the bug we did not find or get lots of duplicates, informative but while we are not searching for it accidentally come :p :D But I did not mean hard work is not necessary or required! :) :D

This article might not be very interesting but I hope this article will a little help and gives some idea for beginners about bug bounty. Also I hope you will find some valid security issues in the future! Good luck!

Got a response with Bounty from Facebook!
Press enter or click to view image in full size
They enlisted me on their Hall of Fame page also (recently 98th number)

Timeline:

Initial Report sent :- Monday, July 13, 2020 at 1:38 PM

Reproduce:- Wednesday, July 15

Triaged:- Wednesday, July 15, 2020

Reward awarded:- Friday, August 28, 2020 at 3:14 PM

Issue fixed:- Wednesday, September 2

If you have any confusion regarding this write up or want to connected with me. You can ask or follow me in the twitter!

Video PoC: https://youtu.be/JP8AnDtO13o

Thank you for giving some time to reading my write up! See you in the next write up!

#StaySecure #StaySafe!
