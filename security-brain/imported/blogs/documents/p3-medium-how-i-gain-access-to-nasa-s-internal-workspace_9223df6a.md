---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-03_p3-medium-how-i-gain-access-to-nasas-internal-workspace.md
original_filename: 2024-09-03_p3-medium-how-i-gain-access-to-nasas-internal-workspace.md
title: 'P3 (Medium) : How I Gain Access To NASA''s Internal Workspace?!'
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: 9223df6af7c7bc6d2df3aed8f0d216cd85104a1186bc17e47510caeaf5135a65
text_sha256: e48d6d7f60e57ba8686a5e3a9b4a11ce7cf7a32af83d4be1593cf9faef0fbd66
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# P3 (Medium) : How I Gain Access To NASA's Internal Workspace?!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-03_p3-medium-how-i-gain-access-to-nasas-internal-workspace.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `9223df6af7c7bc6d2df3aed8f0d216cd85104a1186bc17e47510caeaf5135a65`
- Text SHA256: `e48d6d7f60e57ba8686a5e3a9b4a11ce7cf7a32af83d4be1593cf9faef0fbd66`


## Content

---
title: "P3 (Medium) : How I Gain Access To NASA's Internal Workspace?!"
url: "https://medium.com/@srishavinkumar/p3-medium-how-i-gain-access-to-nasas-internal-workspace-d0896fee563c"
authors: ["Sri Shavin Kumar"]
programs: ["NASA"]
bugs: ["Information disclosure"]
publication_date: "2024-09-03"
added_date: "2024-09-04"
source: "pentester.land/writeups.json"
original_index: 22
scraped_via: "browseros"
---

# P3 (Medium) : How I Gain Access To NASA's Internal Workspace?!

Sri Shavin Kumar
2 min read
·
Sep 3, 2024

--

5

Introduction

Hey everyone, I’m C. Sri Shavin Kumar, an ordinary guy who is passionate about cybersecurity, constantly exploring ways to enhance digital defenses and protect against online threats.

And guess what? I’m back with another finding! So, I was doing a bit of Google Dorking, using simple search queries to find interesting stuff online, but before that

What is Google Dorking?

Google Dorking aka Google Hacking is a powerful technique used to find hidden or sensitive information on websites by using advanced search operators in Google. It involves crafting specific search queries, often called "dorks," to uncover things like exposed files, login pages, and internal documents that aren’t meant to be publicly accessible. Essentially, it’s a way to use Google as a powerful tool to find unintended or overlooked data.

Back to the topic, I came across something unexpected.

Get Sri Shavin Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With a simple search query:

site:"*.nasa.gov" | "slack"

I found a PDF document on NASA’s website that contained a direct link to their internal Slack workspace.

Press enter or click to view image in full size

Naturally, I couldn’t resist clicking on it (because who wouldn’t?), and boom—just like that, I was in! I was able to use any Gmail account to have the access to their internal discussions. 🚀

Press enter or click to view image in full size
Press enter or click to view image in full size
Impact:

Anyone can join the slack workspace with any Gmail account. Moreover, slack channels often hold confidential information—internal conversations, sensitive documents, project plans, and much more. Anyone who gets in could access all of this.

Wrapping Up

This little adventure shows that even the best organizations can have security gaps. It’s a great reminder that Google Dorking can reveal hidden vulnerabilities, and staying vigilant is key. Cybersecurity is everyone’s responsibility, so keep an eye out and stay curious!

Timeline

Submitted : 19 July 2024

Triaged: 7 Aug 2024

Accepted: 9 Aug 2024 (P3 Medium)

Disclosure: 28 Aug 2024

Thanks for reading! Hope you enjoyed it :D . Happy hunting! Stay tuned for more from me.

Follow Me :

https://www.instagram.com/_.iamsh4vk?igsh=cDFvZnJxNDhlc2tz
