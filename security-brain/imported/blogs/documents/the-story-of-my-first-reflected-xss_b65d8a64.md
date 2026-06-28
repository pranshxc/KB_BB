---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-03_the-story-of-my-first-reflected-xss.md
original_filename: 2023-03-03_the-story-of-my-first-reflected-xss.md
title: The Story of My First Reflected XSS
category: documents
detected_topics:
- xss
- idor
- command-injection
tags:
- imported
- documents
- xss
- idor
- command-injection
language: en
raw_sha256: b65d8a64b415bf1ec5c7471fb27162a45d626869297410a61215e197c0460700
text_sha256: 144d70d43fe0a169379797ad43f990b6f33e6970fd699ea7cf89b0209e1d1c82
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# The Story of My First Reflected XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-03_the-story-of-my-first-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `b65d8a64b415bf1ec5c7471fb27162a45d626869297410a61215e197c0460700`
- Text SHA256: `144d70d43fe0a169379797ad43f990b6f33e6970fd699ea7cf89b0209e1d1c82`


## Content

---
title: "The Story of My First Reflected XSS"
url: "https://medium.com/@ahmedelbolaqy/the-story-of-my-first-reflected-xss-c24fbfef2dc6"
authors: ["Ahmed Kamal Abu_Elwafa (@AhmedKa01184061)"]
bugs: ["Reflected XSS"]
publication_date: "2023-03-03"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1440
scraped_via: "browseros"
---

# The Story of My First Reflected XSS

The Story of My First Reflected XSS
Ahmed Kamal AbuElwafa
Follow
2 min read
·
Mar 3, 2023

12

1

Hello guys, hope you all are doing well, This is my second writeup on medium, I’m Ahmed Kamal a Security Researcher and bug bounty hunter from Egypt.
In this writeup, I am going to talk about a Reflected XSS Vulnerability on a VDP on my lovely platform bugcrowd , But Due to the company’s policy I can’t reveal the name of the target let’s say example.com
I am sharing with you my first Reflected XSS finding, which I’ve found 1 month ago, which unfortunately got duplicated but no problem I’ll share the steps of the finding.

come on here

Below are the tools that I use in testing xss but in this bug, i didn’t use all of them because the Rxss was in the search box on the home page so didn’t need to collect parameters for the domain.
Tools:
Paramspider:- https://github.com/devanshbatham/ParamSpider
Gxss:- https://github.com/KathanP19/Gxss
kxss:- https://github.com/Emoe/kxss
xsstrike:- https://github.com/s0md3v/XSStrike

First, i entered a random string on the search box to see what’ll happen
https://subdomain.example.com/search?q=test
then I saw that the word was reflected on the page
you can automate this step using Gxss “which checks a bunch of URLs that contain reflecting params” with the command below :
echo “https://subdomain.example.com/search?q=test" | Gxss
which indicated that the value of the q parameter gets reflected in the page.
let’s move to the next step where we want to know the appropriate payload for exploitation
this step contains two processes, first, find the unfiltered parameter then find the perfect payload for that
usually, i automate this whole process using kxss and XSStrike as shown below:-
echo “https://www.kayenta.bie.edu/sys/search?q=test" | kxss
the result was something like this

Press enter or click to view image in full size
usage of kxss

then moved to xsstrike with the command below:

Get Ahmed Kamal AbuElwafa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

python3 xsstrike.py -d https://www.example.com/search?q=test
the result was something like that

Press enter or click to view image in full size
usage of xsstrike

the final payload looked like this :

https://www.exapmle.com/search?q=%3Chtml%0aonmouseOver%0a=%0a(prompt)``//

when i tested it in the browser it worked successfully and prompt box arised, then i reported it and got duplicated…

that’s all
thanks for reading and have a nice day…

Feel free to connect with me on:

Twitter:-https://twitter.com/AhmedKa01184061

Facebook:-https://www.facebook.com/abo.elwafa.5817
