---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-01_unauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmach.md
original_filename: 2023-05-01_unauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmach.md
title: Unauthorized access to the admin panel via leaked credentials on the WayBackMachine
category: documents
detected_topics:
- idor
- xss
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- idor
- xss
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: c986545f09eab249e47d47e787fd03b7425f787428aedd8329658bb4632f06a1
text_sha256: 346389468b2b7bbfe0cac97c8b397dbe6b9116c324906e55ffa67fe02475c6d0
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthorized access to the admin panel via leaked credentials on the WayBackMachine

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-01_unauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmach.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `c986545f09eab249e47d47e787fd03b7425f787428aedd8329658bb4632f06a1`
- Text SHA256: `346389468b2b7bbfe0cac97c8b397dbe6b9116c324906e55ffa67fe02475c6d0`


## Content

---
title: "Unauthorized access to the admin panel via leaked credentials on the WayBackMachine"
url: "https://infosecwriteups.com/unauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmachine-55c3307141c6"
authors: ["Arman (@M7arm4n)"]
bugs: ["Information disclosure"]
publication_date: "2023-05-01"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1206
scraped_via: "browseros"
---

# Unauthorized access to the admin panel via leaked credentials on the WayBackMachine

Unauthorized access to the admin panel via leaked credentials on the WayBackMachine
M7arm4n
Follow
2 min read
·
May 1, 2023

152

2

Hello my friends, Today I want to talk about one of my admin panel bypass methods which leads me to easily bypass the admin panel.

In my pervasive write-up, I noticed the power of the Wayback Machine and how it helped me to discover the hidden endpoints and exploit an XSS on a famous bank, Here is the write-up:

Let’s Hacking Citizens Bank
Hi Guys, Here is another write-up about how I hacked the Citizens Bank and how chrome extensions helped me in this way…

infosecwriteups.com

So, Today I want to show you how to think out of the box and use this.

Let’s talk about the recon part, The program specified that the target.com domain was in scope, and after subdomains enumeration, I started fuzzing the directories of one of the subdomains and finally arrived at a specific path.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When you opened the desired path, a message was displayed requiring a username and password to access this path, which was received as a GET Base parameter.

I started searching Google and the Wayback Machine and GitHub and all the indexes, but I couldn’t find anything that pointed directly to this particular path in the target.com domain to maybe finds some sensitive information could be found.

While searching on Google, I came across some sites that seem to be using the source of the subdomain, but these domains were not in scope. To test I opened the directory in the out-of-scope domains. for one of them, my Wayback Machine extension was activated and some archived paths were detected.

I opened the archived paths and found a few usernames, passwords, and specific endpoints. I replaced them in the subdomain in scope and one of them worked correctly and I got access to the admin panel. Now I’m In.

Press enter or click to view image in full size

Thank you for following me here, Don’t forget to follow me for more write-ups.

Twitter 🐦

AI-Powered Cyber Threat Detection and Response: SIEM and Compliance solution powered by AI, real-time correlation, and threat intelligence. Built for simplicity, reduced noise and affordability. Learn More
