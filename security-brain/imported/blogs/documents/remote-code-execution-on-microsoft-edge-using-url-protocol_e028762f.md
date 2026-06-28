---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-01_remote-code-execution-on-microsoft-edge-using-url-protocol.md
original_filename: 2019-05-01_remote-code-execution-on-microsoft-edge-using-url-protocol.md
title: Remote code execution On Microsoft edge using URL Protocol
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: e028762fac1d672f2ee2e006abb638392312a30d49227c2a5a54c473ad77bfbe
text_sha256: 42f0613f5eacabfd9944faa53ab4ae9ac4e64d2edcbc3cc3a2078620e8ca75a8
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Remote code execution On Microsoft edge using URL Protocol

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-01_remote-code-execution-on-microsoft-edge-using-url-protocol.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `e028762fac1d672f2ee2e006abb638392312a30d49227c2a5a54c473ad77bfbe`
- Text SHA256: `42f0613f5eacabfd9944faa53ab4ae9ac4e64d2edcbc3cc3a2078620e8ca75a8`


## Content

---
title: "Remote code execution On Microsoft edge using URL Protocol"
url: "https://medium.com/@mattharr0ey/remote-code-execution-on-microsoft-edge-url-protocol-a67d0f96b32d"
authors: ["Matt harr0ey (@harr0ey)"]
programs: ["Microsoft"]
bugs: ["RCE"]
publication_date: "2019-05-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5275
scraped_via: "browseros"
---

# Remote code execution On Microsoft edge using URL Protocol

Remote code execution On Microsoft edge using URL Protocol
Jihad Abdrazak
Follow
3 min read
·
May 2, 2019

19

Press enter or click to view image in full size

Introduction

Hello everyone and welcome to my first bug ever in ‘RCE’ section and I hope this is a good beginning.

The topic of this blog post is: ‘RCE’ on Microsoft edge using URL protocol by some bugs and locations in registry that I found a few time ago, ( Using Jsffile and Wsffile). I’m glad guys but If ‘MSRC’ team patched It and I got bounty that would be a great thing for me but nothing of these options happened because there are some reason they did patch my bugs on the time.

The reasons are:
They determined the bugs I sent and knew a lot of information about them but they gave me just ‘appreciation and/or thanks’ although I saw some people submitted bugs the same I sent and they got their patches.

See below the message I got from ‘MSRC team’

The message I received was seen in

Press enter or click to view image in full size

As you can see above the message was sent by ‘MSRC team’ and that contains some words mean:

Get Jihad Abdrazak’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

They understood the bug but It haven’t got place in the list of acknowledgement that they created in their website for acknowledgements and the patches as well.
By the way, I wouldn’t say I need the money that they give everyday for researchers and I don’t think It’s the end in ‘Cyber security’.

As I understood when I saw the message. they patched the bug without update and so far both ‘JSFFILE’ and ‘WSFFILE’ have been removed from ‘Registry editor’ by ‘MSRC team’. let’s go to see the steps to do ‘RCE’.

First we can take a test if the proof of concept work or no, but I’m sure 100% It’s not going to work after It was removed.
I think my answer was 100% correct.

(JSFFILE and WSFFILE)

Press enter or click to view image in full size
Press enter or click to view image in full size

It hasn’t worked since they removed it from ‘Registry editor’.
but all of these reasons don’t mean: I hadn’t record any proof of concept before they pathed the bug.

Press enter or click to view image in full size

You can enjoy watching the video I released before patches.

https://www.youtube.com/watch?v=zJPrAzUfWHc

Conclusion: Matt harr0ey
Author: Matt harr0ey
