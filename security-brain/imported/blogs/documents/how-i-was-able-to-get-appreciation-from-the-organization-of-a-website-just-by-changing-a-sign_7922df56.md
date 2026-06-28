---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-23_how-i-was-able-to-get-appreciation-from-the-organization-of-a-website-just-by-ch.md
original_filename: 2021-06-23_how-i-was-able-to-get-appreciation-from-the-organization-of-a-website-just-by-ch.md
title: How i was able to get Appreciation from the organization of a website just
  by changing a sign..!!!
category: documents
detected_topics:
- information-disclosure
- command-injection
tags:
- imported
- documents
- information-disclosure
- command-injection
language: en
raw_sha256: 7922df562f1b59e1e0b36f7ecd4279b2c258c44dfbea0fb3e8316fb3cfa131c2
text_sha256: 8fab632e65413e94e67dc2830cdecc8d06e3cb03efb16af25204c31dc569d1de
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to get Appreciation from the organization of a website just by changing a sign..!!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-23_how-i-was-able-to-get-appreciation-from-the-organization-of-a-website-just-by-ch.md
- Source Type: markdown
- Detected Topics: information-disclosure, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `7922df562f1b59e1e0b36f7ecd4279b2c258c44dfbea0fb3e8316fb3cfa131c2`
- Text SHA256: `8fab632e65413e94e67dc2830cdecc8d06e3cb03efb16af25204c31dc569d1de`


## Content

---
title: "How i was able to get Appreciation from the organization of a website just by changing a sign..!!!"
url: "https://fardeen-ahmed.medium.com/how-i-was-able-to-get-appreciation-from-the-organization-of-a-website-just-by-changing-a-sign-661042c97a98"
authors: ["Fardeen Ahmed (@fardeenahmed411)"]
bugs: ["Information disclosure", "Source code disclosure"]
publication_date: "2021-06-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3552
scraped_via: "browseros"
---

# How i was able to get Appreciation from the organization of a website just by changing a sign..!!!

How i was able to get Appreciation from the organization of a website just by changing a sign..!!!
Fardeen A.
Follow
2 min read
·
Jun 23, 2021

31

Hi there, This write-up is for the beginners who are into the bug-bounties, and are searching for new-way of finding vulnerabilities. This was my approach, so let’s start.

Press enter or click to view image in full size

The vulnerable website was, as an example : https://example.com/index.html/

This was normal to use index.html page. So i took the website, intercepted in Burpsuite and used the function of “Spidering” in Burpsuite.

I saw that there was a webpage loading as : https://example.com/hello.txt~/ (This letter/symbol is known as delimiter)

This was quite suspicious. Then, a sense came within me, of “Replacing extensions with symbol”. So, i replaced “hello.txt~” with “hello~.txt”

Nothing happened…!!!!!!

Now, went to change “hello.txt” to “hello~”

Nothing happened…!!!!!!

Get Fardeen A.’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thought that there is no vulnerability and it is quite decent now to “Not Report any vulnerability”

Then before closing the website, i went through technologies used in the website using “Wappalyzer” :- https://www.wappalyzer.com/

Press enter or click to view image in full size

While going through, i saw that “https://example.com/index.html” loads as “https://example.com/index.html~/” in Page Source Code.Source Code Disclosure.

I took the website page code seriously, and removed index.html, with just “index~” and I hit enter key.

And there i was able to get source code disclosure of the website and get to know about SQL queries working at the back…which was a complete “Sensitive Information Disclosure”.

It fetched me Appreciation for finding a new type of vulnerability at the platform.

Tips : Use the special symbols (~, !, @, #, $, % etc) only when there is acceptance of it in the source code of the page, else it will be a time waste.

— — — ======— H@ppY_H@ck1nG —======== — — —
