---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-08_breaking-the-competition-bug-bounty-write-up.md
original_filename: 2020-03-08_breaking-the-competition-bug-bounty-write-up.md
title: Breaking the Competition (Bug Bounty Write-up)
category: documents
detected_topics:
- password-reset
- access-control
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- password-reset
- access-control
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 40ace3d33d4b26933afcaf17340ebb889c9a16eb1fc88d24088695b2003e6f12
text_sha256: de628c52a51e87785c30073f606391079033bb0584c188e18fef7fd786a13b0f
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking the Competition (Bug Bounty Write-up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-08_breaking-the-competition-bug-bounty-write-up.md
- Source Type: markdown
- Detected Topics: password-reset, access-control, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `40ace3d33d4b26933afcaf17340ebb889c9a16eb1fc88d24088695b2003e6f12`
- Text SHA256: `de628c52a51e87785c30073f606391079033bb0584c188e18fef7fd786a13b0f`


## Content

---
title: "Breaking the Competition (Bug Bounty Write-up)"
url: "https://medium.com/ctf-writeups/breaking-the-competition-bug-bounty-write-up-ca7cb7bc53f5"
authors: ["George O (@georgeomnet)"]
bugs: ["Race condition", "DoS", "Logic flaw", "Session management issue"]
publication_date: "2020-03-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4728
scraped_via: "browseros"
---

# Breaking the Competition (Bug Bounty Write-up)

Breaking the Competition (Bug Bounty Write-up)
George O
Follow
7 min read
·
Mar 8, 2020

337

1

1

In this post, I’ll be describing how I found 5 bugs on a private HackerOne program. The website that I attacked was a new CTF hosting provider, and I had actually participated in a CTF using this provider prior to being invited to their private program.

Please note that as the program is private, I can’t show the exact pages exploited, or show any of the exact code that I used to exploit them.

Race Condition in Flag Submission

Out of all bugs submitted, I believe that this had the highest severity. Essentially, if a CTF task was worth 100 points, the race condition vulnerability would let me obtain up to 1000 points for it!

Race conditions occur when multithreaded applications don’t synchronize properly. You can find a more in-depth explanation of this type of vulnerability here, but I’ll try to explain how it worked in this case.

Let’s say that the server-side code looked something like this:

Pseudo-code of back-end flag checker

In a single-threaded application, this pseudo-code would work perfectly. The program checks to see if the challenge has already been solved, and if not, checks whether the flag is correct/incorrect.

However, consider the following situation: An attacker submits two requests at the same time. This means that in a multi-threaded application, as most web-servers are, the code will run twice at the same time (or at least very close to each other).

Press enter or click to view image in full size
Thread A and Thread B running through the pseudo-code

If you look at the gif above, you’ll notice how although Thread B was triggered slightly after Thread A, it still managed to score the user an extra 100 points. This is because Thread A doesn’t set the “CHALLENGE_SOLVED” attribute to the user until line 8, which isn’t reached until after Thread B has passed the challenge solve check.

This is common in web applications due to the delay in data retrieval from a database. Often, during this delay, other threads can catch up to the original one and cause race condition vulnerabilities to occur.

In order to demonstrate this vulnerability to HackerOne, I did the following:

Create my own CTF on the platform
Join the CTF as a user
Use the race-the-web tool to send 100 requests to the site’s flag submission API endpoint
Verify the results on the leaderboard

Race-the-web is a tool created by Aaron Hnatiw, which allows for easy automated race condition testing. It’s written in Go, which means that the web requests are really efficient. My payload looked as follows:

Press enter or click to view image in full size
My race-the-web config.toml

One especially useful aspect of this tool is that it allows for a proxy to be set in the config for all requests, which means that I could easily debug my requests in Burp suite.

After some time, HackerOne got back to me with the following feedback:

HackerOne resposne to the bug.
DOS Any User on the Site
Finding the issue itself

This bug wasn’t quite as useful for attackers as the previous one, but it proved quite fun. The DOS wasn’t caused by a security misconfiguration, but was instead a logic error.

For a CTF to be created, some details need to be provided. This includes the obvious — CTF name, challenges, max participants, and CTF start/end dates.

I first tried exploiting the CTF name/challenges for XSS, but found nothing (the site was built on React, so XSS is almost impossible).

Steps for Self-DOS

I then tried setting the CTF end date to the the previous day, but this was blocked, which makes sense as the CTF start and end dates should both be either in the present or in the future. The developers had thought of this already, and had blocked this on both the front-end and the back-end. However, this could still be bypassed through the CTF start/end time setting.

It was possible to create a CTF that was set to start, for example, today at 10am, but finished today at 8am.

At first, I accidentally created this CTF and discovered my entire account was just Error 500s! The site had become completely unusable for my user. This was likely due to a lack of error catching in the back-end.

I raised this report on H1, detailing how an attacker who had access to a victim’s account could cause complete DOS to them:

Press enter or click to view image in full size
Initial HackerOne DOS report

However, as this was just a self-DOS, the HackerOne team asked me to explain how this was exploitable. As such, I had to increase the impact.

Increasing the impact

During some more testing, I discovered that all linked staff accounts also become unusable after this CTF is created. However, I decided that the impact of this would still be too low to bother re-reporting.

Get George O’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Creating a broken CTF may be good for self-DOS, but we need a way to affect all other users. Most users on the site don’t have permission to create CTFs, and can only join them — so I needed a way to allow users to join broken CTFs.

Steps to DOS all users

I first tried experimenting with forcing users to join the CTF through CSRF, but there was no way to get the broken CTF’s ID.

Instead, I realised that we can actually break the CTF after it’s been created! Between creating the CTF and officially starting it, we can edit some basic information (i.e. rules and max players) — and the start/end time was included in this.

As an attacker, this is really useful. We can create a CTF, send out invites to users, and then after they’ve joined, change the end time to sometime in the past. This would therefore break all accounts of users who joined. As this could affect anyone in the site, I felt comfortable re-submitting the bug.

Press enter or click to view image in full size
Second HackerOne DOS report.

This bug then got accepted, triaged and patched!

“Forgot Password” Link Valid after Email Change

This bug is admittedly far less severe than the other two, but was still validated and triaged.

Essentially, an attacker who once had access to a victim’s account can maintain persistence via the “Forgot Password” link.

Consider the following scenario:

An attacker gains access to a victim’s inbox.
The attacker issues a password reset on the CTF site to the compromised email.
The attacker copies the password reset link, and deletes the original email.

The user would then assume that it was only their inbox compromised — and the other sites are (at least likely) safe. However, consider the following too:

The victim changes their email password, thinking that the attacker can no longer access their accounts. They also setup a new email address to distance themselves from the attack.
The victim changes their email address on the CTF site, so that they cannot login anymore.
However, the attacker still has the password reset link from earlier! As such, they can use this to login to the victims account again — without even knowing the new email address.

Although this attack doesn’t allow for initial exploitation, it allows attacker persistence in an account.

This bug was marked as low, but was accepted!

Press enter or click to view image in full size
HackerOne response to my bug report.
Session Tokens Valid despite Password Change

This vulnerability was definitely more severe than the previous one, as the steps are far more simple for attackers to retain persistence in an account. However, it still doesn’t allow for inital exploitation and so isn’t all that fun.

Essentially, once an attacker gains access to an account, there’s no way to revoke their access.

On the site, the only way to invalidate session tokens was to logout of that session — but a victim can’t log an attacker out of theirs! Even if the user changes/resets their password (or email address), all sessions remain valid.

OWASP has a good article on session management that covers the do’s and don’ts, and this is described in detail there:

Session Management Cheat Sheet
Web Authentication, Session Management, and Access Control: A web session is a sequence of network HTTP request and…

owasp.org

This bug was accepted without discussion and is currently being fixed:

Press enter or click to view image in full size
HackerOne response to the bug submission.
Race Condition in Team CTFs

This bug was marked as informative and so I won’t go into too much detail, but after hours of research I want to write a little about it.

In the site, CTFs can be done in teams. Max team sizes are chosen by the CTF creator to ensure fair competition. However, through a similar exploit to that in the first bug (race condition in flag submission), this limit can be bypassed.

In my limited testing, I managed to get a team with a maximum of 2 players to have over 5 users in it.

Thoughts

Overall, this programme was really fun and I appreciate the efforts of the team in validating the reports (even though the resolution time was generally over a month). I got to compete against my other friends who were also looking at this, which helped motivate me more too.

Although no monetary reward was given from this programme, I’ve had some merch shipped out 🤠

Contact me:
Personal Website
Twitter: georgeomnet
Github: Ge0rg3
Discord: George#1234
