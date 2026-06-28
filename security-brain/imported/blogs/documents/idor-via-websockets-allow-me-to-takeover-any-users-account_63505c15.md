---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-14_idor-via-websockets-allow-me-to-takeover-any-users-account.md
original_filename: 2021-02-14_idor-via-websockets-allow-me-to-takeover-any-users-account.md
title: IDOR via Websockets allow me to takeover any users account
category: documents
detected_topics:
- idor
- jwt
- command-injection
- password-reset
- otp
- csrf
tags:
- imported
- documents
- idor
- jwt
- command-injection
- password-reset
- otp
- csrf
language: en
raw_sha256: 63505c15ed5015ebfc174448d68ec375c3f952357ae605ef4ea29de30e1ec712
text_sha256: cf53c83728029b44038d0711ea1ed92970c1b97c00c2e6d229ad92317477496d
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR via Websockets allow me to takeover any users account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-14_idor-via-websockets-allow-me-to-takeover-any-users-account.md
- Source Type: markdown
- Detected Topics: idor, jwt, command-injection, password-reset, otp, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `63505c15ed5015ebfc174448d68ec375c3f952357ae605ef4ea29de30e1ec712`
- Text SHA256: `cf53c83728029b44038d0711ea1ed92970c1b97c00c2e6d229ad92317477496d`


## Content

---
title: "IDOR via Websockets allow me to takeover any users account"
url: "https://mokhansec.medium.com/idor-via-websockets-allow-me-to-takeover-any-users-account-23460dacdeab"
authors: ["Mohsin Khan (@tabaahi_)"]
bugs: ["IDOR"]
bounty: "450"
publication_date: "2021-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3909
scraped_via: "browseros"
---

# IDOR via Websockets allow me to takeover any users account

IDOR via Websockets allow me to takeover any users account
Mohsin khan
Follow
4 min read
·
Feb 14, 2021

626

Hi everyone I hope you all are doing great and scoring lots of bounties. I am Mohsin khan I am from India and I do bug bounty full time for 1 year now. I found lots of bugs in the last year.

Today I am sharing one of my finding which allows me to take over all users account. It was out of scope domain bug but they paid me a bounty ❤. Without further ado let’s start.

It was a private program and I don’t have permission to disclose any information about the target so let’s call it example.com. Let me give you a basic idea about functionality of a program.

It is an online meeting platform where you can create your team. You can invite users, you can follow users and you can permit users like admin, normal user, etc.

Now I start the burp suite and started checking how to change the name, email functionality works. I found that there is an X-token header. It was a JWT token and as you know if the JWT token is there It means it is almost impossible to find CSRF. At least on this website. I tried to remove the token and tried to change information but nothing work website gave me 401.

I don’t know much about bug classes mostly I only hack on login, save info, signup. so Now I create another account but this time I am checking every request and response. Like how signup is working & responses.

I found that when you click on signup after POST request one WebSocket request is sent which contains UUID and email, username, etc. I tried to change the UUID to my first account (Account A)UUID and I got an error.

Email already exists.

I was like

Press enter or click to view image in full size

Now I understand why the website giving me an Email exist error. because user B’s account is now already created and I can’t use the same email. Now I change UUID to my account A UUID and change email and now I got no response but when I go to my first account (account A) and reload the page I logged out.

I immediately try to login again (with account A email) but I got an error. (After changing the email, the website logout the user to log in again. We can confirm we changed account A email successfully. As you know I already know account A password. but we can request a password reset link because now we control account A) now I understood and I try to login with a new email, and Now I have logged in to user A account successfully.

Team: How you manage to find UUID?

Get Mohsin khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As I told you before it was an online meeting platform. By going to the user’s profile and clicking on the following user button you can grep users UUID easily.

Press enter or click to view image in full size

It was P2 but I rewarded P3 bounty. Because it was out of scope domain.

Press enter or click to view image in full size
Press enter or click to view image in full size

But when triager make your Critical to P3

Press enter or click to view image in full size

Takeaway:

Always play with login, signup, and change info functionality. There is always something for you
In this program, 40+ hackers were invited but they didn’t find it because I think most hackers don’t look for WebSockets. So check everything because we never know where will found the bug.
Be creative as you can see I change UUID and I got an error because not changed the email so spend more time.
It is so easy to find a critical bug you don’t need to do a Ph.D. xD. Learn one bug and spend lots of time with the program.

Resources

Airbnb - Web to App Phone Notification IDOR to view Everyone's Airbnb Messages
Airbnb recently created a new feature called Experiences which allows you to book things to do rather than places to…

buer.haus

Insecure Direct Object Reference (IDOR) - Intigriti
An Insecure Direct Object Reference can be one of the easiest bugs yet they can have a very big impact. IDOR is still a…

blog.intigriti.com

Tip for beginner

When I started after few months I started doing collaborations. It helps me to learn a lot. Most of the time I hack with my friends, If you want to collaborate you can dm me on Twitter. There is the platform called findhunters

Collaboration Opportunities | findhunters
Every bug hunter has a unique approach. Hunters who collaborate are able to make use of different techniques…

findhunters.com

You can collab with lots of hackers and learn a lot together. Go checkout findhunters. ❤

I hope you enjoy reading. If you have any questions feel free to ask me on Twitter https://twitter.com/mokhansec .
