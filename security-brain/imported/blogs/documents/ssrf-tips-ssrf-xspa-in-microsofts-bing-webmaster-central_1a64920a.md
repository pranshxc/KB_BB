---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-09_ssrf-tips-ssrfxspa-in-microsofts-bing-webmaster-central.md
original_filename: 2019-04-09_ssrf-tips-ssrfxspa-in-microsofts-bing-webmaster-central.md
title: 'SSRF Tips: SSRF/XSPA in Microsoft’s Bing Webmaster Central'
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 1a64920a832e8662f0ada9d838bfb98864badc49a619f8d91776ba8697a57943
text_sha256: 25569b3d3a417b822e46e346fab072650bd117ddc909ca1a260ad1d5e3c963cc
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF Tips: SSRF/XSPA in Microsoft’s Bing Webmaster Central

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-09_ssrf-tips-ssrfxspa-in-microsofts-bing-webmaster-central.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `1a64920a832e8662f0ada9d838bfb98864badc49a619f8d91776ba8697a57943`
- Text SHA256: `25569b3d3a417b822e46e346fab072650bd117ddc909ca1a260ad1d5e3c963cc`


## Content

---
title: "SSRF Tips: SSRF/XSPA in Microsoft’s Bing Webmaster Central"
url: "https://medium.com/@elberandre/ssrf-trick-ssrf-xspa-in-microsofts-bing-webmaster-central-8015b5d487fb"
authors: ["Elber Andre (@Elber333)"]
programs: ["Microsoft"]
bugs: ["SSRF", "XSPA"]
publication_date: "2019-04-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5320
scraped_via: "browseros"
---

# SSRF Tips: SSRF/XSPA in Microsoft’s Bing Webmaster Central

SSRF Tips: SSRF/XSPA in Microsoft’s Bing Webmaster Central
Elber Andre
Follow
2 min read
·
Apr 9, 2019

191

Today I’m going to talk about a trick that might be useful for BugHunters.

While I was looking for a few things about BugBounty, I found a report where the author talked about an SSRF
which he had found in Bing’s Webmaster Central, and reported to Microsoft.
In the Bug it describes that it was able to list internal ports and the services of that application.

More info on: https://blog.0daylabs[.]com/2015/08/09/SSRF-in-Microsoft-bing/

Seeing this I thought “What if I try a new bypass on this fix?”, I like challenges, so I opened my browser and started testing.

Press enter or click to view image in full size

First I tried a list of payloads that resolved to ‘127.0.0.1’, but their filter did not allow those addresses.

Press enter or click to view image in full size

As they were blocking access via the address ‘127.0.0.1’, and also registering ip addresses,
I used the “.nip.io” domain to be able to bypass that first check along with the ip ‘127.127.127.127’.

127.127.127.127.nip.io

Press enter or click to view image in full size
Press enter or click to view image in full size

It was enough to deduce that I had been able to access their local address.

Get Elber Andre’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Note that with “127.127.127.127” it does a redirect to “/toolbox/webmaster/”

After that I tried to access a nonexistent directory, to check the server responses.

Press enter or click to view image in full size
Conclusion:

Setting up a domain to resolve the address ‘127.127.127.127’ I was able to bypass the old fix, list internal ports and directories in the local address of Bing Webmaster,
sometimes many administrative panels are configured to be accessed only locally, which could be found by scanning directories through this SSRF.

Follow me :D http://twitter.com/elber333
