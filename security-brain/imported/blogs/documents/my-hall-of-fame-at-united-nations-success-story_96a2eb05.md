---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-27_my-hall-of-fame-at-united-nations-success-story.md
original_filename: 2022-08-27_my-hall-of-fame-at-united-nations-success-story.md
title: My Hall of Fame at United Nations Success Story
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- clickjacking
- api-security
language: en
raw_sha256: 96a2eb058b66f10070015ea46d41c8031aa16a405098424b9cc43d06620ddbba
text_sha256: 2cb689dd915a1067fad1805e19e73c5a647599fd14ff9f9bcd7285a7cf011784
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# My Hall of Fame at United Nations Success Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-27_my-hall-of-fame-at-united-nations-success-story.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `96a2eb058b66f10070015ea46d41c8031aa16a405098424b9cc43d06620ddbba`
- Text SHA256: `2cb689dd915a1067fad1805e19e73c5a647599fd14ff9f9bcd7285a7cf011784`


## Content

---
title: "My Hall of Fame at United Nations Success Story"
page_title: "How I entered United Nations Hall of Fame as an 18y/o Ethical Hacker! | InfoSec Write-ups"
url: "https://joshuaarulsamy.medium.com/my-hall-of-fame-at-united-nations-success-story-97675232aed7"
authors: ["Joshua Arulsamy (@Joshua_Arulsamy)"]
programs: ["United Nations"]
bugs: ["XSS"]
publication_date: "2022-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2256
scraped_via: "browseros"
---

# My Hall of Fame at United Nations Success Story

How I got into United Nations Hall of Fame as an 18y/o Ethical Hacker!
Joshua Arulsamy
Follow
3 min read
·
Aug 27, 2022

162

For anyone aspiring to build a career in cybersecurity, Hall of Fames play a major role, like anyone and everyone as a young aspiring ethical hacker it was my dream too and it was a surprise to me when it turned into a reality one day. Here is how I made my dream come true.

If you’re thinking Hall of Fame at United Nations is a great deal and it demands extraordinary skills to enter United Nations Hall of Fame! This is for you.

Press enter or click to view image in full size
Photo by Jonathan Ansel Moy de Vitry on Unsplash

Is it Hard to Enter United Nations HOF?

The simple answer is No.

If Entering United Nations is your goal it's not at all a great deal , go ahead and explore vulnerabilities like clickjacking which is very common in UN sites and try to increasing the severity of it and Report it to infosec@un.org , it’s just time consuming and not hard , But the real fun is doing something interesting and new that justifies your presence in the Hall Of Fame , Here is the Story of how I made it to United Nations Hall of Fame by Finding XSS in one of the UN owned subdomains .

Press enter or click to view image in full size
Photo by Max Bender on Unsplash

The core step in finding any vulnerability in any domain is subdomain enumeration, I personally use amass, subfinder and sublist3r you can use use any tool of your choice but combining the goodness of all these tools is a better idea so that you don’t miss any subdomain. If you’re an absolute beginner you can try online tools like DNSDumpster , Virustotal or any such enumeration tool available online. On enumeration I got a lot of active subdomains, had been a while I guess something around 8000 subdomains. One domain caught my attention https://mdgs.un.org , I moved on to explore further and I tried brute forcing the directories.

Now I Found something amazing,

https://mdgs.un.org/query.asp

Get Joshua Arulsamy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This gave me some hope that this has some juice in it!

I tried various XSS payloads on the search field there and finally one payload worked for me,

Payload : x” onmouseover=alert(1) x=”

After the successful execution of the payload, I found an alert pop up each time the mouse cursor crosses the Search field.

It was a Reflected XSS!!!!!

Press enter or click to view image in full size
Photo by Fauzan Saari on Unsplash

I reported the vulnerability to United Nations infosec@un.org , on 19th of January and waited for almost 2 months.

On March 16 Finally my name Joshua Arulsamy was added to the Hall of Fame.

Finally, My Name was Added to the Infosec Hall of Fame

Find my name here: Hall of Fame | Office of Information and Communications Technology

Thank You so much for reading, do follow me here on medium and on LinkedIn for more amazing content!

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
