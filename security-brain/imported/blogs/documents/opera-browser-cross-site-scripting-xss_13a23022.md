---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-05_opera-browser-cross-site-scripting-xss.md
original_filename: 2020-12-05_opera-browser-cross-site-scripting-xss.md
title: Opera Browser Cross Site Scripting (XSS)
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 13a230224c375be17e93b12211fccb901cb3655223951116589ca734f8922175
text_sha256: 0065015558567420d02c35c128be49185cffd2d041f2beee894ccfe493645e8d
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Opera Browser Cross Site Scripting (XSS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-05_opera-browser-cross-site-scripting-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `13a230224c375be17e93b12211fccb901cb3655223951116589ca734f8922175`
- Text SHA256: `0065015558567420d02c35c128be49185cffd2d041f2beee894ccfe493645e8d`


## Content

---
title: "Opera Browser Cross Site Scripting (XSS)"
url: "https://nmochea.medium.com/this-post-is-about-an-reflected-xss-that-i-found-on-opera-browser-application-which-could-have-been-39823a22045d"
authors: ["Neil Mark Ochea (@nmochea)"]
programs: ["Opera"]
bugs: ["XSS", "Android"]
publication_date: "2020-12-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4089
scraped_via: "browseros"
---

# Opera Browser Cross Site Scripting (XSS)

Opera Browser Cross Site Scripting (XSS)
Neil Mark Ochea / mhl_0xnmo
Follow
3 min read
·
Dec 5, 2020

16

While using opera browser for android I noticed something strange the address bar in opera browser replaced by the reader mode and the web title added.

I know that I can trigger the xss in reader mode but i dont know where so this my conclusion visit the website with xss payload and click the reader mode then xss will trigger.

I was on the website I looked in reader mode but it did not show up hmm wtf so i looked another website, again, again but still not showing up the reader mode, I would have given up

but an idea entered my mind what if I compose my own payload and that is what I will read in reader mode maybe the xss payload trigger, so what site i can compose my payload and then i remember about google calendar you can write title and description its perfect for what I’m looking for.

Get Neil Mark Ochea / mhl_0xnmo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step to Reproduce

Open opera browser goto
Press enter or click to view image in full size
Create a new task with following

Title

Press enter or click to view image in full size

Description

Press enter or click to view image in full size
Then save the task then click the task and send it to your gmail.
Goto inbox open the message and copy the message id from url address
Insert the message id to this link
Press enter or click to view image in full size
Paste the link to the new tab and go, from the right top header click the reader mode then the xss will trigger
Hall of Fame

I’m added to Opera Security Hall of Fame in 2020 List of Hall of Fame.

Disclosure Timeline
September 23, 2020 — I emailed Opera Security Team regarding this vulnerability issue.
September 25, 2020 — I provided additional details and some screenshot as proof of concepts.
September 29, 2020 — The Opera Browser released an updated, the security team emailed me that the vulnerability has been fixed and ask me to reproduce again to confirmed the fixed.

Thanks for reading this article, I hope you guys learn something new today. Please share this article to spread the knowledge.

Don’t forget to follow and connect with me through LinkedIn, and Twitter.
