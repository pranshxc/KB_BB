---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-08_bypass-xss-filter-using-html-escape.md
original_filename: 2020-05-08_bypass-xss-filter-using-html-escape.md
title: Bypass XSS filter using HTML Escape
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
raw_sha256: d9dd8a1cc3b0b9099fbdadea0296ff2b95ae4d433ac7768bae33e36f9100c679
text_sha256: 91852237f530c4fc1bb0d6550712634ed8c96365e5041412f5dc6fd0a72fa629
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass XSS filter using HTML Escape

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-08_bypass-xss-filter-using-html-escape.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `d9dd8a1cc3b0b9099fbdadea0296ff2b95ae4d433ac7768bae33e36f9100c679`
- Text SHA256: `91852237f530c4fc1bb0d6550712634ed8c96365e5041412f5dc6fd0a72fa629`


## Content

---
title: "Bypass XSS filter using HTML Escape"
url: "https://medium.com/@adonkidz7/bypass-xss-filter-using-html-escape-f2e06bebc8c3"
authors: ["Syahri Ramadan (@adonkidz7)"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "4,133.70"
publication_date: "2020-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4597
scraped_via: "browseros"
---

# Bypass XSS filter using HTML Escape

Top highlight

Bypass XSS filter using HTML Escape
Syahri Ramadan
Follow
2 min read
·
May 8, 2020

219

2

after all the bugs were fixed, I was still curious and wanted to try again, then I tried the first day and it failed :(
because it is blocked by csp
I tried using this payload:

<noscript> <p title=” </noscript>
<style onload= alert(document.domain)//”> *{/*all*/color/*all*/:/*all*/#f78fb3/*all*/;} </style>

Press enter or click to view image in full size

I had almost given up because nothing happened and was just a waste of time, the next day I did not continue until the third day.
and on the fourth day the same as the first day, just wasting time and nothing happened.
and on the fifth day, I tried it using HTML Escape on my payload.

Get Syahri Ramadan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and this is the final result of my payload using HTML Escape:
<noscript> &amp;lt;p title=” &lt;/noscript&gt;
&lt;style onload= alert(document.domain)//&quot;&gt; *{/*all*/color/*all*/:/*all*/#f78fb3/*all*/;} &lt;/style&gt;

Press enter or click to view image in full size
Press enter or click to view image in full size

I managed to bypass XSS filter using HTML Escape tools from the website W3cubTools, and here is the link: https://tools.w3cub.com/html-escape-unescape

After reporting to the Google Security Team, they gave me an award of $4133.70

Press enter or click to view image in full size

Timeline
Reporting Date - Apr 6, 2020, 3:34 PM
Nice Catch - Apr 9, 2020, 10:56 AM
Reward - Apr 21, 2020, 11:23 PM
Fixed - May 4, 2020, 6:20 PM
Thank you for visiting, hopefully useful for everyone ❤
