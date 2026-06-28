---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-13_logic-flaw-i-can-block-you-from-accessing-your-own-account_2.md
original_filename: 2024-09-13_logic-flaw-i-can-block-you-from-accessing-your-own-account_2.md
title: 'Logic Flaw: I Can Block You from Accessing Your Own Account'
category: documents
detected_topics:
- access-control
- race-condition
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- race-condition
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 29947674d9bebcc35fd5d1efca2aca3b19eccef276f1dd430f7772eef13a72d8
text_sha256: 6df0a35f7a54ecef920ca5f09e37434697bd2bf5f611effe1cdfa9bf749262c4
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# Logic Flaw: I Can Block You from Accessing Your Own Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-13_logic-flaw-i-can-block-you-from-accessing-your-own-account_2.md
- Source Type: markdown
- Detected Topics: access-control, race-condition, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `29947674d9bebcc35fd5d1efca2aca3b19eccef276f1dd430f7772eef13a72d8`
- Text SHA256: `6df0a35f7a54ecef920ca5f09e37434697bd2bf5f611effe1cdfa9bf749262c4`


## Content

---
title: "Logic Flaw: I Can Block You from Accessing Your Own Account"
url: "https://medium.com/@hashimamin/logic-flaw-i-can-block-you-from-accessing-your-own-account-63fc2a88bb72"
authors: ["Hashim Amin"]
bugs: ["Logic flaw"]
publication_date: "2024-09-13"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 4
scraped_via: "browseros"
---

# Logic Flaw: I Can Block You from Accessing Your Own Account

Logic Flaw: I Can Block You from Accessing Your Own Account
Hashim Amin
Follow
5 min read
·
Sep 13, 2024

739

10

Press enter or click to view image in full size

Hey Hackers, This’s mrhashimamin. Ever been part of a forum? Ah, the good old days. I still remember all my failed, time-wasting attempts to become famous on those meme forums— creating cringey memes and hardly trying to get my name on the leaderboard.

Press enter or click to view image in full size
KnowYourMeme leaderboard - Just an example of what i’m talking about
So, what’s the point? Why are we talking about this now?

Well, that’s what this is about. After encountering duplicates and N/As in a few Bug Bounty programs (as a beginner), I came across a new program with a pretty solid scope. It includes a forum for customer support, resolving issues, and answering questions. What caught my interest was the ranking/points system, which is based on things like answering questions, solving issues, and sending badges, among other activities.

Press enter or click to view image in full size
Forum homepage

After some real user testing (which was super helpful), I discovered that liking anything on the forum earned me 5 points. Naturally, I tried automating it with Intruder and tested for race conditions, but didn’t find much at first. However, as always, I knew I needed to dig deeper.

After a while, I discovered something even more interesting. When I liked and then unliked a post, the likes count on my profile changed, but my points didn’t! So, all I had to do was repeatedly like and unlike posts to climb the leaderboard. Is that the end of the story? Not even close! 😆

0 points, right?

When I repeated the process using some Burp Suite tricks (I’ll dive deeper into that later), I gained around 130 points. But of course, I wanted more! 😆

During further user testing, I discovered that anyone could access user notifications. At first, I thought it was a Broken Access Control (BAC), but after reading the docs, I realized it works as intended— you can view another user’s notifications, just not control them. But you can still like and unlike them… you see where I’m going with this?

By doing the same like-unlike trick on any user’s notification, I racked up 20 points! Fast, but I still wanted more! 😆

So, I thought about sending the attacker a badge. When I checked my notifications (the attacker’s), I repeated the same like-unlike process on the badge the victim had sent me. This time, I earned 30 points with each like and unlike. And that’s how I finally got my name on the leaderboard!!!!

And here’s where the fun begins! After racking up all those points, my account got blocked. 😢

Get Hashim Amin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, every time I try to log in, I’m stopped by a sad black screen!

So sad, right?

No, not at all! When I got that message, I thought, ‘Can I do this to anyone’s account?’ And the answer was yes. I could easily go to anyone’s post or action, repeat my awesome process, and boom. They’d lose access to their account for good!

But How and Why?

First, let me walk you through how I repeated the process over and over.

You’ll need three requests: [like, unlike, profile (or any page)].

Send a like on any post/action and highlight it as green.
Unlike it and highlight it as red.
Go to your profile (or any page on the forum) and highlight it as blue.
Open Burp Suite macros and select the green and red requests. (here)
Send the blue request to Intruder, choose Null payloads, set the concurrent requests to 1, and start the attack.
Now, the attacker racks up tons of points, and the poor victim is blocked from the forum.
Black screen of death?

When the server responds with a 400 Bad Request, it means the server detected something wrong with the victim’s request, likely due to corrupted state or malformed data caused by our exploit.

I have a couple of theories about this:

The backend might be detecting that the victim is receiving a lot of requests on their post/action in a short period, leading to their account being blocked. However, this raises the question of why I, as the victim, didn’t receive a block message like ‘You’re blocked’ or any indication that something was wrong and the server know that. Why didn’t anything happen to me as the attacker, I wasn’t maliciously triggering the Web Application Firewall (WAF)?
The second theory is that the server didn’t properly validate or rate-limit the requests, which could have overwhelmed or corrupted the request-handling mechanism. This could result in improper handling of user data, causing the user to be locked out or their account to be invalidated.

As this appears to be a logic flaw, and without more information or insights, it’s challenging to develop further theories, as it’s a black box testing.

What Now?

After reporting this bug to the program, it took them 20 days to respond. They marked it as informational! Can you believe this?

Press enter or click to view image in full size

After all, this write-up isn’t just about the bounty or the points. It’s about sharing my ideas with you. So, let me know your thoughts in the comments. Thanks, and keep hacking 3>
