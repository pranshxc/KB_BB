---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-06_the-easiest-2500-i-got-it-from-bug-bounty-program.md
original_filename: 2021-03-06_the-easiest-2500-i-got-it-from-bug-bounty-program.md
title: The easiest $2500 I got it from bug bounty program
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
- mobile-security
language: en
raw_sha256: 01010ca0744d0d9637365938816bc008d7e9753e6499ad96260d4dc2a20e6fd3
text_sha256: 5a0f2a7048e889cdb85274851117e521b2df2b97337c64e6a3a706c4114aa40c
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# The easiest $2500 I got it from bug bounty program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-06_the-easiest-2500-i-got-it-from-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `01010ca0744d0d9637365938816bc008d7e9753e6499ad96260d4dc2a20e6fd3`
- Text SHA256: `5a0f2a7048e889cdb85274851117e521b2df2b97337c64e6a3a706c4114aa40c`


## Content

---
title: "The easiest $2500 I got it from bug bounty program"
url: "https://3bodymo.medium.com/the-easiest-2500-i-got-it-from-bug-bounty-program-8f47ea4aff22"
authors: ["Abdullah Mohamed (@3bodymo_)"]
programs: ["Uber"]
bugs: ["Information disclosure"]
bounty: "2,500"
publication_date: "2021-03-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3837
scraped_via: "browseros"
---

# The easiest $2500 I got it from bug bounty program

The easiest $2500 I got it from bug bounty program
Abdullah Abdelrazek
Follow
3 min read
·
Mar 5, 2021

494

5

Press enter or click to view image in full size

Hi
all, today I will talk about first vulnerability I found it. At that time, I knew little about information security, so I was not do scan or something like that, I used to use the application as a normal user, but curiosity pushed me to find this vulnerability.

How I found the vulnerability?

One day, my friend came to me to request a trip for his friend, when the driver arrived I wanted to give the driver number to my friend to give it to his friend to communicate with the driver, at that time I knew that Uber protects the numbers of drivers and customers, but I am a curious person so I clicked here and there until I found a new feature It allows you to send SMS to the driver. When I clicked on it, it was the surprising, the driver’s real number appeared to me. I gave the number to my friend to send it to his friend. Then I thought about what had happened, and I thought to myself that this was unusual behavior and thought it was a vulnerability!!

Read more about number anonymization feature…
How to reproduce the vulnerability?

At first, request a trip. After that, press the location of the arrow indicated in the picture below, in order to have a conversation with the driver.

Press enter or click to view image in full size

After that, click on the phone sign above, and two options will appear for you, the first is make a phone call with driver (if you click it, it will direct you to the Uber general number and you will not know the real driver’s number).

Press enter or click to view image in full size

The second option is to send a SMS to the driver and when you click on it, the real driver’s number will appear for you.

Press enter or click to view image in full size
How did I report the vulnerability?

I searched for Uber in hackerone and found that they have a program, I tried to send a report, but I could not, because my account is new and I do not have any signals, I contacted with hackerone’s support, but to no avail as well. I searched on Facebook and found a person called Khaled Hassan and he is a security researcher a long time ago and I decided to send the vulnerability to him in order to send it on my behalf (I never knew him at the time, but now he is one of my best friend).

Get Abdullah Abdelrazek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The vulnerability was fixed a month after it was send, and I was awarded my first bounty.

Press enter or click to view image in full size
Lessons learned
I had no experience in the field of information security when I found this vulnerability, but I have a curiosity that pushed me to click here and there until I found this vulnerability, so use the application or website and walk through it and understand how it works, then start your hacking, that will give you good results and you will find a lot of bugs.
Pay your attention to logic vulnerability.
When you suspect that you have found a vulnerability and you are not sure, consult a close friend of yours and do not lose hope.

Thanks for your reading, I hope my story was useful.

Timeline:

[Jan 29, 2020] — Bug reported

[Jan 31, 2020] — Triaged

[Mar 4, 2020] — Bug fixed

[Mar 6, 2020] — Rewarded $2500
