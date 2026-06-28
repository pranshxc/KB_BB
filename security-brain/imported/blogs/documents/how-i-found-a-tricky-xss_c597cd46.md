---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-24_how-i-found-a-tricky-xss.md
original_filename: 2023-05-24_how-i-found-a-tricky-xss.md
title: how I found a tricky XSS
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
raw_sha256: c597cd465cc06683c6e53022e4d5a04512fe23b3b02af6577ec583a16ccf3e93
text_sha256: 5311872e94e9c162f189a8b27f4b1577cc89b3482549004d3557202a1d0b95f5
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# how I found a tricky XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-24_how-i-found-a-tricky-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `c597cd465cc06683c6e53022e4d5a04512fe23b3b02af6577ec583a16ccf3e93`
- Text SHA256: `5311872e94e9c162f189a8b27f4b1577cc89b3482549004d3557202a1d0b95f5`


## Content

---
title: "how I found a tricky XSS"
url: "https://medium.com/@ajzead660/how-i-found-a-tricky-xss-1adf25850d33"
authors: ["Ziad Ali"]
bugs: ["XSS"]
publication_date: "2023-05-24"
added_date: "2023-06-01"
source: "pentester.land/writeups.json"
original_index: 1119
scraped_via: "browseros"
---

# how I found a tricky XSS

how I found a tricky XSS
Ziad Shalaby
Follow
2 min read
·
May 24, 2023

79

2

Hello everyone, this is my first write-up, and I hope you find it enjoyable. I would appreciate any feedback you have. While XSS write-ups are quite common, I believe this one has some interesting and amusing aspects to it. Let’s get into it!

I encountered a website consisting of only one page, featuring a navbar and a search input in the center just like that

Press enter or click to view image in full size

Ahhh for the sake of clarity guys :D

In my attempts to find vulnerabilities, I tried various injection techniques in the URL input, but unfortunately, I couldn’t identify any weaknesses.

Get Ziad Shalaby’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

However, I turned my attention to the languages dropdown and made an intriguing discovery. When selecting a language, a request was sent to another endpoint, resulting in the creation of a new cookie named ‘language’ with a value corresponding to the chosen parameter.

What made this even more interesting was that the HTML LANG attribute utilized this cookie value to set the language on the page.

Based on this observation, we can proceed to craft a payload and send a link to the victim. When the victim opens the website, our payload will be executed due to the presence of the LANG attribute.

Press enter or click to view image in full size
Press enter or click to view image in full size

That concludes my write-up! I hope you enjoyed reading it ❤

Any feedback is greatly appreciated guys.
