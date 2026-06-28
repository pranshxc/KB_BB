---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-10_unintended-behaviour-of-domain-got-me-p4.md
original_filename: 2020-09-10_unintended-behaviour-of-domain-got-me-p4.md
title: Unintended Behaviour of domain got me P4
category: documents
detected_topics:
- command-injection
- rate-limit
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- rate-limit
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: 10bdfb9a95de8ffd767144bccac7babae74e4b3c2f97fb384120f5280ffc3c60
text_sha256: b691a430963d638dc500014b2a35897df7d90bba03152ca1c0952d214fb94ea8
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Unintended Behaviour of domain got me P4

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-10_unintended-behaviour-of-domain-got-me-p4.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `10bdfb9a95de8ffd767144bccac7babae74e4b3c2f97fb384120f5280ffc3c60`
- Text SHA256: `b691a430963d638dc500014b2a35897df7d90bba03152ca1c0952d214fb94ea8`


## Content

---
title: "Unintended Behaviour of domain got me P4"
url: "https://medium.com/@gaupaler/unintended-behaviour-of-domain-got-me-p4-d6af19b5dcdd"
authors: ["Takester (@dhiraj_ramteke)"]
bugs: ["Logic flaw"]
publication_date: "2020-09-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4270
scraped_via: "browseros"
---

# Unintended Behaviour of domain got me P4

Unintended Behaviour of domain got me P4
Takester
Follow
2 min read
·
Sep 10, 2020

29

1

Press enter or click to view image in full size

Hi friends,

I hope you all doing well✌️.

Get Takester’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So this is my second writeup about the bug that I found in last month. Lets talk about it.

In my recon phase I got all subdomains and wayback data of target website for example “xyz.com”. Then I send all the subdomains for screenshot. After getting screenshots of all subdomains I went through them one by one.

While looking into them I saw one subdomain has interesting endpoint so, I bruteforce that subdomain and got nothing interesting😔. Fair enough I move towards other subdomains to get anything juicy so I can find something interesting, but at the end of day I got nothing and with that I went to sleep.

Second day when I woke up, I was going through my discoveries/data that I gathered last day and I saw some results in dirsearch folder, I went through it one by one and by doing that I landed on the subdomain “subdomain.xyz.com” that has /admin and when I visited it I got the admin log in panel, I tried to brute force it and got nothing. While brute forcing the admin panel I noticed it has some “version and name at bottom of the page” I googled it and got various results about it, I visited one of the result example “abc.com” I got the same page as I got on the “subdomain.xyz.com” same directories, even the same account that I registered on the “subdomain.xyz.com”, wait whatttt🧐!!!.

Then I searched about domain by reverselookup, dig, host etc and got to know that domains “abc.com” and “xyz.com” belonged to different organization… what😲???

Then I quickly reported that issue and got my P4🎉🎉🎉. So always go through your results, be curious be pocky to find juicy sttuff.

PS: Whenever you think something is not right search about it and if satisfied report it you may get reward for it or even your report may get rejected but don’t loose your hope!!!

I hope you guys learn something from it and if so give a nice clap.

Thank You!! keep hacking✌️…
