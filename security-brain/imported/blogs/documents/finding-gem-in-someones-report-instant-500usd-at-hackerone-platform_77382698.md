---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-07_finding-gem-in-someones-report-instant-500usd-at-hackerone-platform.md
original_filename: 2019-09-07_finding-gem-in-someones-report-instant-500usd-at-hackerone-platform.md
title: 'Finding Gem in Someone’s Report: Instant $500USD at HackerOne Platform'
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 7738269812409ffdad839c13ff000c89ae9f4284e26e3376ae6394499fef744a
text_sha256: c786c0e8deb42c93382f88e30e6227e36ee61562e30088b36859246f7afa1e45
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Finding Gem in Someone’s Report: Instant $500USD at HackerOne Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-07_finding-gem-in-someones-report-instant-500usd-at-hackerone-platform.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7738269812409ffdad839c13ff000c89ae9f4284e26e3376ae6394499fef744a`
- Text SHA256: `c786c0e8deb42c93382f88e30e6227e36ee61562e30088b36859246f7afa1e45`


## Content

---
title: "Finding Gem in Someone’s Report: Instant $500USD at HackerOne Platform"
url: "https://medium.com/@hisokamorou12/finding-gem-in-someones-report-instant-500usd-at-hackerone-platform-9a1afa0df813"
authors: ["Hisoka Morou"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2019-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5046
scraped_via: "browseros"
---

# Finding Gem in Someone’s Report: Instant $500USD at HackerOne Platform

Finding Gem in Someone’s Report: Instant $500USD at HackerOne Platform
Hisoka Morou
Follow
2 min read
·
Sep 7, 2019

82

Browsing HackerOne Hacktivity has become part of my everyday routine. I love checking out the latest reports, figuring out how they work, and trying to replicate them myself. That’s actually how I landed my very first $500 bounty on the platform — it felt amazing!

By looking at the other side of the coin, I managed to bypass the fix that was originally implemented.

Douglas Day (aka the_arch_angel) submitted a report to HackerOne about the program’s email notification being ignored when adding an external contributor. It was disclosed on August 8, 2019, and that same day I jumped in to try reproducing the issue. The report was super clear, so I managed to mimic the scenario right away. According to the write-up, a fix was already implemented — and I confirmed it myself.

Learning from different researchers really helps me grow. I don’t stop reading an article until I fully understand it. Big thanks to the_arch_angel for submitting report #645264 — it was super easy to follow and replicate. While going through it, I noticed the report focused on adding contributors. That got me thinking: if you can add, there must be a way to remove — and that’s where my story begins. Digging deeper, I found a hidden gem in his report. By looking at the other side of the coin, I managed to bypass the fix that was originally implemented.

Get Hisoka Morou’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Journey to bypass:

Go to your Program’s report and invite any participant by clicking the Add Participant Link
Invited contributor will receive an email without the report Title (since it is already fixed)
Go back to Program’s report at the Participants Section hover the mouse cursor on the invited contributor’s email or username.
Press enter or click to view image in full size

4. Select REMOVE PARTICIPANT

5. HackerOne will send another email that the invitation has been revoked. But notice that the email sent to the email disclosed the Title that supposed to be masked.

Press enter or click to view image in full size

Instant bounty, isn’t it? Just dive in and start reading — you never know, you might stumble on a hidden gem just by going through someone else’s report.
