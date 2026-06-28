---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-30_a-weird-xss.md
original_filename: 2021-03-30_a-weird-xss.md
title: A weird XSS
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: c323e5d4bb675d71670373f53706a1f1f890f61bc5a5862b8b646cb178131b27
text_sha256: 02e2676712ae7a4d36e7cd283b7591b882b2cca521638cda55fd903b6226791a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# A weird XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-30_a-weird-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `c323e5d4bb675d71670373f53706a1f1f890f61bc5a5862b8b646cb178131b27`
- Text SHA256: `02e2676712ae7a4d36e7cd283b7591b882b2cca521638cda55fd903b6226791a`


## Content

---
title: "A weird XSS"
url: "https://infosecwriteups.com/a-weird-xss-77c13d135c9f"
authors: ["gato the wizard"]
bugs: ["Reflected XSS"]
publication_date: "2021-03-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3782
scraped_via: "browseros"
---

# A weird XSS

A weird XSS
gato the wizard
Follow
4 min read
·
Mar 30, 2021

36

2

Hi friends, how are you? Today I came to do my first writeup to tell you how I stopped exploring in XSS in a slightly different way, so here we go.

For a brief introduction, my “hacker name” gato (gato is cat in Brazilian portuguese and it is because I want to prove that curiosity only strengthens the cat), I am 19 years old, I love technology and I recently started in the area of information security.

So come on!

As the bug was not fixed, for ethical reasons, I will call the site redacted.xxx.br!

Part 1: The search

It all started with a simple desire to find a bug on some website and make an extra buck, the situation is not easy in Brazil… So I was surfing the web, until it fell on a .xxx.br site, and I know that government websites have a very bad security history, I thought I’d look over the application and see if I found anything. I started injecting malware into the simplest inputs, but everything seemed very well sanitized, so I decided to get a little heavier.

Part 2: The tools

I started to enumerate subdomains using the Sublist3r tool, but nothing strange, so I went to the ParamSpider tool to analyze the parameters of the hosts found. The list was huge, especially as I picked up both likes with a 200 return, and those with 404 (always good to see if something reflects on poorly constructed 404 pages).

As I had not yet tried to automate the process, I opened all the links in the list to see if it had reflected or not (you can use the Httpx tool, that with the parameters -match-string and -match-regex, you can search for your reflection), until I found the following page:

Press enter or click to view image in full size

As you can see, although the parameter is all lower case, it was reflected so that the first letter was upper case, and the rest lower case, a simple treatment for proper names!

Get gato the wizard’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to inject a payload to see if it would be executed, but the behavior was applied in my alert (1), and the method was not executed.

Part 3: The injection

As I was out of patience, I did what every kiddie sript would do, I started to Ctrl + C and Ctrl + V all the payloads I found on the internet. Did it work? Of course, not hahahhaha.

I decided to give my head some time, I went to drink some water, breathe a little. It was there that I happened to remember when I was little and I was learning to play chess, the teacher would set up challenges, where the pieces were placed in a certain way on the board, and in a certain amount of movements I had to checkmate (win the game). So I went back to the computer, and with the mentality of chess challenges, I started to see XSS in the same way. Every movement I make, the application can defend itself in some way, if my movement does not have a positive effect, I undo it and start again.

I started researching some ways to perform HTML injection, because at first it was what was working. Until I arrived at the HTML Charset table, using the numeric value of the character, preceded by ‘&’ and ‘#’, it is possible to display the character on screen.

Press enter or click to view image in full size
The & # characters are encoded in URL (%26 and%23 respectively) so that they are not treated as URL construction symbols

When I clicked enter and saw that my character had not been changed to uppercase, I broke into a huge smile.

Finishing the tests, I ended up with the following payload: <img%20src=x%20onerror=”%26%2397%26%23108%26%23101%26%23114%26%23116(1)”>. In that alert, it is being sent as HTML encoding.

Press enter or click to view image in full size

My tips for you are:

Tools are great, but it’s the way you use them that make them great!
Be patient, if I need to get off the computer for a while, throw something, and then come back with a clear head!
Stay curious!

And that’s it! I hope you enjoyed!

Buy Me a Coffee! (please think about! the dollar is worth five times the Brazilian real)
