---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-23_how-i-bypassed-practos-firewall-and-triggered-a-xss.md
original_filename: 2017-09-23_how-i-bypassed-practos-firewall-and-triggered-a-xss.md
title: How i bypassed Practo’s firewall and triggered a XSS.
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: c5882a6d69f675b4bdc23249209866a97406b49b82057ef7015d505d5aeef251
text_sha256: 287cf1c16c9ca6938a91222e5f613707c15ab6bcf849d7098f246778f981257d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How i bypassed Practo’s firewall and triggered a XSS.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-23_how-i-bypassed-practos-firewall-and-triggered-a-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `c5882a6d69f675b4bdc23249209866a97406b49b82057ef7015d505d5aeef251`
- Text SHA256: `287cf1c16c9ca6938a91222e5f613707c15ab6bcf849d7098f246778f981257d`


## Content

---
title: "How i bypassed Practo’s firewall and triggered a XSS."
url: "https://medium.com/bugbountywriteup/how-i-bypassed-practos-firewall-and-triggered-a-xss-b30164a8f1dc"
authors: ["Vipin Chaudhary (@vipinxsec)"]
programs: ["Practo"]
bugs: ["XSS"]
publication_date: "2017-09-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6092
scraped_via: "browseros"
---

# How i bypassed Practo’s firewall and triggered a XSS.

Vipin Chaudhary
Follow
2 min read
·
Sep 23, 2017

240

3

How i bypassed Practo’s firewall and triggered a XSS.

One night after submitting few bug reports, i was browsing practo.com and then i thought of looking for vulnerabilities on it.

After some time i came to know that they have firewall blocking all the XSS payloads so i had to try something advance, but somehow i managed to get HTML Injection on their main domain.

Press enter or click to view image in full size

Then i started digging deep to get a XSS, but Firewall :( then i thought of going back to brutelogic’s blog and see if it’s possible to bypass it or not.

Most of the JS event handlers like onmouseover, onload, onclick was blocked by firewall but after experimenting a lot oncopy worked and triggered a XSS.

Press enter or click to view image in full size

The payload which worked was :

Get Vipin Chaudhary’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<vipin oncopy = prompt(document.domain)>

I reported this issue to Practo and they fixed it within few hours.

It was when i just started into security research/bug bounty, it was a great learning experience for me.

So guys when you are stuck in such situations just keep on digging and look out for help from other researchers and their blogs it will help for sure.

I hope it was helpful for you too.

Thanks for reading, Have a great day.
