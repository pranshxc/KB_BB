---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-09_demographic-misconfiguration-on-facebook-live_2.md
original_filename: 2022-03-09_demographic-misconfiguration-on-facebook-live_2.md
title: Demographic Misconfiguration on Facebook live
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: 4738791edb07fce69238dcd90dd51c0317c4f6578aa21b5f19c5521cedb5c035
text_sha256: 14ee30229fdfd13cd8769f35124a60239dc64cf7086465c287da1fbb4419d512
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Demographic Misconfiguration on Facebook live

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-09_demographic-misconfiguration-on-facebook-live_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `4738791edb07fce69238dcd90dd51c0317c4f6578aa21b5f19c5521cedb5c035`
- Text SHA256: `14ee30229fdfd13cd8769f35124a60239dc64cf7086465c287da1fbb4419d512`


## Content

---
title: "Demographic Misconfiguration on Facebook live"
url: "https://prajwoldhungana487.medium.com/demographic-misconfiguration-9359910c6fcf"
authors: ["Prajwol Dhungana (@PrajwolDhunga14)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2022-03-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2840
scraped_via: "browseros"
---

# Demographic Misconfiguration on Facebook live

Demographic Misconfiguration on Facebook live
Prajwol Dhungana
Follow
2 min read
·
Mar 9, 2022

68

Press enter or click to view image in full size

Hi there, I am with a new bug bounty writeup that I recently found.

In facebook there is an ability for page admin to crosspost the live video to their second page with audience restriction.

When the live video is shared with audience restriction(eg: age 25+, women, and region as Nepal). When the live video was shared crossposting to the next page, during the live session the restricted users were not able to view the live video but when the admin decides to post that live video in both page. The first page from where the live video was started the video gets post customly but the second page where the live video was crossposted posts the live video publically.

Timeline:

December 12, 2021: Initial report sent

December 23, 2021: Closed as Informative

Get Prajwol Dhungana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

December 29, 2021: I opened the report with further clarification

Janaury 13, 2022: Triaged

February 23, 2022: Bounty rewarded+ time delay bonus

March 3, 2022: Confirmation of fix from Facebook and me

Later, this issue was incomplete fix and when I re-reported the problem, they responded that there are several methods to get around audience settings, such as establishing an account with a different age or using a VPN to shift countries. As a result, we do not consider audience bugs to be privacy breaches, and we will not compensate users who report them.

Poc: https://youtu.be/F9jFG8NkEEU

Thank you for taking the time to read my article. Have a great day!

You can follow me on Facebook or Instagram if you would like to stay connected with me.
Buy me Momo
