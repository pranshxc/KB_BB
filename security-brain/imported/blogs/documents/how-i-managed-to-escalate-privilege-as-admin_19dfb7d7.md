---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-16_how-i-managed-to-escalate-privilege-as-admin.md
original_filename: 2020-06-16_how-i-managed-to-escalate-privilege-as-admin.md
title: How I managed to Escalate privilege as admin
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 19dfb7d7fd1c55b09835f626f938ec38c615fd0090b3f45916ed4016cebfa675
text_sha256: 6c2e27aa42c3e7854c2326221d70dbb22f87df369c3742846450656d9490da7d
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I managed to Escalate privilege as admin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-16_how-i-managed-to-escalate-privilege-as-admin.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `19dfb7d7fd1c55b09835f626f938ec38c615fd0090b3f45916ed4016cebfa675`
- Text SHA256: `6c2e27aa42c3e7854c2326221d70dbb22f87df369c3742846450656d9490da7d`


## Content

---
title: "How I managed to Escalate privilege as admin"
url: "https://medium.com/@abireena2002/how-i-managed-to-escalate-privilege-as-admin-94b8dc910d14"
authors: ["Abisheik Magesh (@AbisheikMagesh)"]
bugs: ["Lack of rate limiting", "Bruteforce", "Weak credentials"]
publication_date: "2020-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4491
scraped_via: "browseros"
---

# How I managed to Escalate privilege as admin

How I managed to Escalate privilege as admin
Abisheik Magesh
Follow
3 min read
·
Jun 18, 2020

83

Before we start :

i was participating on one of the big well known company's bug Bounty program which has very wide scope i will not mention the name of the company but lets focus on the vulnerability part

How it all started :

i got started with my recon workflow

On all the assets owned by example for long time by on that process i came across a sub domain called wechat.example.cn but first the site was down so long time as a part of my recon workflow i always use to check every resolves or not by opening all the domains on the chrome but this time i found something interesting wechat.example.cn was up and so i checked is there any admin directory yeah i was lucky i found admin directory on the site but it redirected (302) to login page so i tried to directly access the admin common end points like index.php but no success so now it’s time to dig deeper

How i managed to Escalate privilege as admin :

So i now i have got the admin panel of the yes your right i tried some common username:password as Admin:admin but still no success but i found something interesting the the Error message was your password was wrong wait which mean the username admin exist but only the password was wrong so we have found security misconfiguration which leads enumerate username but it was not a very big issue company may take it as accepted risk or out of scope

What is username enumeration ?

The username enumeration is an activity in which an attacker tries to retrieve valid usernames from a web application. The web applications are mostly vulnerable to this type of attack on login pages, registration form pages or password reset pages.

so i tried to chain the issue now we have the username so i tried to

brute force with the

common credential with burp intruder

(Probably common password top 100 )

When i started to brute force after the 10 request the server blocked my request so i stopped brute forcing the credential now i was like

WHAT THE HELL

tired to open the site on my Firefox on “private tab “ which was configured with the burp and tried to login the page i was blocked so i opened the same site on my chrome browser and login this time everything works fine so i tried to figure out what is going on

If they did not configure the Rate limiting functionality properly so an another low issue

What is rate limiting ?

Get Abisheik Magesh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Rate limiting is used to control the amount of incoming and outgoing traffic to or from a network. For example, let’s say you are using a particular service’s API that is configured to allow 100 requests/minute. If the number of requests you make exceeds that limit, then an error will be triggered.

And now a idea struck my mind if i can brute force the the admin credential by changing the user agent headers for every 10 request to avoid rate limit hit

So now i am trying use word list top 100

Which means i s i should use different user agent for that every 10 request to bypass the rate limit functionality

So i tried that method luckily the the first 10 request was (302 redirect ) to login page the Magic happened in the next 10 request i found a credential which (302 redirect ) to /admin/xxxxx endpoint then i used the credential to login and it got bypassed

i was like Yes i made it

What is a weak password or common password?

A weak password is short, common, a system default, or something that could be rapidly guessed by executing a brute force attack using a subset of all possible passwords, such as words in the dictionary, proper names, words based on the user name or common variations on these themes

Exploiting :

On the part to exploit the the panel i was visiting all the endpoint of the page on logs file i saw many logs on one i seen the admin use put request which mean we can upload a shell on the server

Vulnerability found during this process :

Username enumeration
Rate limit Bypass
Weak credential on login panel
Due to we have admin access we may have possibility potentially use PUT method to exploit the server

Take Away :

“Little drops make mighty ocean “
so as that chaining the low level issue to gain extra impact to the target

social media Handel :

Instagram : @_itsjust___.a.k.m.___

Facebook : @Abisheik Magesh
