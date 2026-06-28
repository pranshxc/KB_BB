---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-08_reflected-xss-on-target-with-tough-waf-waf-bypass-.md
original_filename: 2023-02-08_reflected-xss-on-target-with-tough-waf-waf-bypass-.md
title: Reflected XSS on Target with tough WAF ( WAF Bypass )
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
raw_sha256: adca1593321bb80d6d87a25325b3741bd4b74a2f2a713871774229eb35d0ef2d
text_sha256: 741ae2e61ccac236d31c4ae85602a671a8674c7208fbcad93fc614ca2e5ec379
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS on Target with tough WAF ( WAF Bypass )

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-08_reflected-xss-on-target-with-tough-waf-waf-bypass-.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `adca1593321bb80d6d87a25325b3741bd4b74a2f2a713871774229eb35d0ef2d`
- Text SHA256: `741ae2e61ccac236d31c4ae85602a671a8674c7208fbcad93fc614ca2e5ec379`


## Content

---
title: "Reflected XSS on Target with tough WAF ( WAF Bypass )"
url: "https://jowin922.medium.com/reflected-xss-on-target-with-tough-waf-waf-bypass-3b7efd1ef2bc"
authors: ["Eagle_92"]
bugs: ["Reflected XSS", "WAF bypass"]
publication_date: "2023-02-08"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1561
scraped_via: "browseros"
---

# Reflected XSS on Target with tough WAF ( WAF Bypass )

Reflected XSS on Target with tough WAF ( WAF Bypass )
jowin922
Follow
2 min read
·
Feb 8, 2023

170

I was doing web pentest on a private program. The program had a very tough WAF even typing alert as a payload would be blocked by WAF.

This website had a vulnerable test page which was vulnerable to XSS, which the developers had forgotten to remove after development of the website was over. I had found this endpoint by directory bruteforcing.

The vulnerable endpoint was like below.

https://redacted.com/redacted/origin/test?charset=%C3%A9a

The charset parameter was vulnerable to XSS, However the WAF protecting the website was blocking any XSS payloads to be executed on the website.

I followed the portswigger methodology for WAFbypass mentioned on https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

The method is to first copy all tags from portswigger xss cheatsheet and send to the website with intruder ( For example, Replace FUZZ with tags from portwsigger cheatsheat for below link )

Get jowin922’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://redacted.com/redacted/origin/test?charset=<FUZZ>

Note the tags which are not blocked, then FUZZ with events from portswigger cheat sheet. Note the events which are not blocked.

Now select the event and tag which are not blocked, Portswigger cheatsheet will give you the WAF bypassed payload to use

Press enter or click to view image in full size

For the website I was testing, the only payload that worked was the below one. It only works on chrome browser.

“><xss onpointerrawupdate=console.log(‘XSS’)>Click_Here_Click_Here_Click_Here_Click_Here_Click_Here_Click_Here_Click_Here_ClickHere</xss>

When the user moves cursor over Click_Here, XSS will keep getting printed on the console showing javascript execution.

Press enter or click to view image in full size
