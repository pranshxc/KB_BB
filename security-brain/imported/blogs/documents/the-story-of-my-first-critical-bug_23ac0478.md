---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-29_the-story-of-my-first-critical-bug.md
original_filename: 2020-11-29_the-story-of-my-first-critical-bug.md
title: The Story of my first critical bug
category: documents
detected_topics:
- sqli
- xss
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- sqli
- xss
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 23ac0478b808adbefc852770b28bc48bce94523d045db35d8847e64d6371f26f
text_sha256: 62dd9662612f72e6f10b387997b1fc747d116b1efd897228558d797d2ac7bb69
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# The Story of my first critical bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-29_the-story-of-my-first-critical-bug.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `23ac0478b808adbefc852770b28bc48bce94523d045db35d8847e64d6371f26f`
- Text SHA256: `62dd9662612f72e6f10b387997b1fc747d116b1efd897228558d797d2ac7bb69`


## Content

---
title: "The Story of my first critical bug"
url: "https://shellbr3ak.medium.com/the-story-of-my-first-critical-bug-93a5920d6c43"
authors: ["Shellbr3ak (@0xShellbr3ak)"]
bugs: ["SQL injection"]
publication_date: "2020-11-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4104
scraped_via: "browseros"
---

# The Story of my first critical bug

The Story of my first critical bug
Shellbr3ak
Follow
4 min read
·
Nov 23, 2020

136

2

3 months ago I got my first infosec job as a Threat Intelligence Analyst, and I can’t tell how happy I was to get this job. However my application wasn’t meant to be (I’m looking for a job as threat intel analyst) instead it was about web penetration testing. So after getting this job, my team leader asked me to conduct a web penetration test on one of our clients’ website and I did ( it was the second time he asks me to conduct a pentest) though I’m interested in web penetration testing, I didn’t have any real-life experiences as I’m used to practice only on CTF platforms such as HackTheBox, TryHackMe, and Portswigger labs, but in my head I was like; why not!! after all, this is what I was training for. So without speaking too much, I’ll start telling my story how I found my first critical bug (it was really fun though).

For the sake of our clients’ privacy I’ll name the company as “redacted.com”.

After I tested almost every single website owned by that company and prepared my report, which didn’t have anything of interest (only a few notes about some security misconfigurations and brute force protection bypass things), I texted my team leader to tell him that I finished my pentest and I’m ready to hand over the report, but my team leader wasn’t available that moment, so he called me saying “Explain what you’ve found quickly because my laptop’s battery is dying”, but since my report had many notes (as I said, only misconfiguration stuff, though I was really happy that I found them) I asked my team leader to charge his laptop and call me when they are available.

So, I had extra few minutes to review my report to see if I missed anything or any website that I didn’t test well, and indeed there was a website that I’d forgotten to test, but I had a short amount of time so I thought “I can’t test a website in 10 mins or what so ever, so I’m just gonna run a scanner and do some simple manual tests”.

The Target Server is acting very strangely:

On that subdomain, let’s call it subdomain.redacted.com there was a search bar and whatever is submitted into it gets rendered in the response page. That moment, I had only three vulnerabilities on top of my head to test for:

1 — XSS

2 — SSTI

3 — SQLi

So I started testing for XSS but I didn’t get anything, then I moved to SSTI, after fuzzing for a bit, I noticed that the backend technology in use is ASP.NET which doesn’t have any template engines, so my testing for SSTI turned out to be meaningless :(

Lastly, I was going to start testing for SQLi, and I was like, ASP.NET is a really good platform to make secure web apps, and since SQLi is one of the most critical bugs, there’s no way this app is vulnerable to SQLi, so I won’t waste my time. (10 mins have passed since my team leader told me that they’re gonna call me back in 3 mins), so I decided to test for SQLi real quick.

As I mentioned before the target server was running ASP.NET as a backend technology, and the OS is (for sure) Windows server, so chances are the RDBMS is going to be MSSQL (yet I submitted some payloads for other dbms’s) but I focused on MSSQL the most.

Get Shellbr3ak’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As it’s known for everyone, the first payload to submit when looking for SQLi is a comment so I submitted this payload into the URL:

https://subdomain.redacted.com/?search= ‘ or 1=1 —

and

https://subdomain.redacted.com/?search=” or 1=1 —

I didn’t get any indication that the server might be vulnerable, but something deep inside me told me to go further and try other payloads.

Since (‘ or 1= 1— ) is a very well known payload to test for SQLis, I thought of changing the number 1 like (‘ or 3=3 — ) in case there’s a firewall blocking the expression of (1=1), or instead of triggering an “always true” condition, let’s try to submit an “always false” condition

like (‘ or 1=2 — ), and indeed the server responded in a strange way, yet it wasn’t enough to assume that it’s really vulnerable, but I was completely out of ideas, and I didn’t know what payload I should use, so I took a 2 min break and collected my thoughts about SQLi attacks (I’ve learned them from PortSwigger Academy), and indeed there was a payload I’ve forgotten to try, (though it’s the most effective one to detect blind SQLis) which is “TIME DELAY”.

So I submitted the payload “ ‘ WAITFOR DELAY ‘00:00:10’ “, and the server really took some time to respond, but that moment my internet connection was slow as hell, so I couldn’t determine if the delay was because of my slow internet speed or the server really responded to my payload, so I intercepted the request with burp to measure the response time accurately, and indeed the response time was 10 sec and a few milliseconds, so I changed the payload and forced a delay for 20 seconds and that really worked, but a part of me wasn’t convinced that I really found a SQLi (My very first real-life bug), so I forced a delay of 1 minute, and INDEED that worked :).

After making sure that the website is vulnerable to SQLi, I edited my report and included the new notes about the SQLi, and then called my team leader to hand over the report.

Remediation:

Never trust user input
Always check user-supplied data

Bug Bounty Tip:

Never underestimate time delay payloads.
Don’t rely on automated scanners.

So that was the write up I hope u guys enjoyed it, and I’ll see you all in the next write up :)
