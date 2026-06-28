---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-27_reflected-xss-on-stack-overflow.md
original_filename: 2018-04-27_reflected-xss-on-stack-overflow.md
title: Reflected XSS on Stack Overflow
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
raw_sha256: 74f07e3ef64649ef24d2d5a5d109e8bfde2f190a07e0b9e08d5092c10e077ff7
text_sha256: c8f8051f08f83db61bb0d5377b3df578790cfe1bc1df320dc3cac9a58dd6d48f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS on Stack Overflow

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-27_reflected-xss-on-stack-overflow.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `74f07e3ef64649ef24d2d5a5d109e8bfde2f190a07e0b9e08d5092c10e077ff7`
- Text SHA256: `c8f8051f08f83db61bb0d5377b3df578790cfe1bc1df320dc3cac9a58dd6d48f`


## Content

---
title: "Reflected XSS on Stack Overflow"
url: "https://medium.com/@newp_th/reflected-xss-on-stack-overflow-b8366a855472"
authors: ["ssid (@newp_th)"]
programs: ["Stack Overflow"]
bugs: ["Reflected XSS"]
publication_date: "2018-04-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5896
scraped_via: "browseros"
---

# Reflected XSS on Stack Overflow

Reflected XSS on Stack Overflow
newp_th
Follow
2 min read
·
Apr 27, 2018

202

3

This is @newp_th. Today I want to share with you a Reflected XSS which I found in Stack Overflow.

While i was testing some other domain and doing spider activity in burpsuite, I checked issues tab whether any issues were popped up. Suddently i got to know Stack Overflow is vulnerable to XSS (i used reflector extension https://github.com/elkokc/reflector). So i decided to test that domain of Stack Overflow.

Reflector extension:

Burp Suite extension is able to find reflected XSS on page in real-time while browsing on web-site and include some features as:

Highlighting of reflection in the response tab.
Test which symbols is allowed in this reflection.
Analyze of reflection context.
Content-Type whitelist.

Get newp_th’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When i was going through the Stack Overflow domain, I noticed a vulnerable parameter in Cookie!!, I put a simple payload “></script><img src=x onerror=alert(1)> into the prov parameter.

Press enter or click to view image in full size
Request

After cheking the reponse from IE, Got the XSS POPUP!!!!

Press enter or click to view image in full size

Note:
Dedicated to my friend Renjith(https://ae.linkedin.com/in/renjith-tc-bb9b40a1), I greatly appreciate the time you’ve taken to share your knowledge with me

HOF on the way!!!!

Press enter or click to view image in full size

Timeline
Feb 14th -Report submitted
Feb 19th -Triaged
April 3rd -Fixed
