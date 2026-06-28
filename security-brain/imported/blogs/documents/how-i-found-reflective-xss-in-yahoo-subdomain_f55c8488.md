---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-03_how-i-found-reflective-xss-in-yahoo-subdomain.md
original_filename: 2017-09-03_how-i-found-reflective-xss-in-yahoo-subdomain.md
title: How I found Reflective XSS in Yahoo Subdomain
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
raw_sha256: f55c84882e27db51a25abe01a2ce639edb5d061107bdad1581ec55345a89695d
text_sha256: 3c70b7bf8068c5ba63c747e4b8eebce650138dddf1ebdefdfc4356bf10b39891
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I found Reflective XSS in Yahoo Subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-03_how-i-found-reflective-xss-in-yahoo-subdomain.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f55c84882e27db51a25abe01a2ce639edb5d061107bdad1581ec55345a89695d`
- Text SHA256: `3c70b7bf8068c5ba63c747e4b8eebce650138dddf1ebdefdfc4356bf10b39891`


## Content

---
title: "How I found Reflective XSS in Yahoo Subdomain"
url: "https://medium.com/@SyntaxError4/how-i-found-reflective-xss-in-yahoo-subdomain-3ad4831b386e"
authors: ["Syntax Error (@SYNTAXERRORBA)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Reflected XSS"]
publication_date: "2017-09-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6109
scraped_via: "browseros"
---

# How I found Reflective XSS in Yahoo Subdomain

How I found Reflective XSS in Yahoo Subdomain
Syntax Error
Follow
3 min read
·
Sep 4, 2017

308

2

When 2017 started,I had a bounty goal of finding a bug in Yahoo but I never actually got time to look into their program. One day I planned to go for it.So here is the writeup on how I found Reflective XSS on a yahoo subdomain. This is my first writeup so please ignore any mistakes that you find.

First step was to find subdomains on yahoo and the tool I used was Sublist3r(https://github.com/aboul3la/Sublist3r)

Press enter or click to view image in full size

Once I had the list,I started checking the subdomains one by one.During that time my attention went to one of the subdomains: https://hkfood.yahoo.com

There was a search bar on the site to lookup for recipes and I initially tried couple of payloads to see what characters were filtered.For my luck, my inital payload itself worked and I could pop XSS

Vulnerable URL : http://hkfood.yahoo.com/search_result#keywords=“/>.<<img src=x onerror=alert(1)//”&gt;>&lt;&gt;&page=1

Press enter or click to view image in full size

I reported the bug to Yahoo and the bug was Resolved the very next day.I rechecked the Vulnerable URL and was not able to reproduce the issue.

Get Syntax Error’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After 2 days,I was getting Bored and thought about retesting around the same XSS bug.This time I found that <script><img> tags were being filtered.

So I started trying different combination of payloads to see if I can break the URL. To get <script> tag working,I broke it in pieces like below and added that to the old vulnerable URL and Hurray!!!

Payload: <scr<script>ipt>alert(1)</scr</script>ipt>

Press enter or click to view image in full size

Tips:

Always Retest your bugs after its marked Resolved.There is a good chance that you will find a bypass.
I have seen some folks using tools/scripts to get sublist3r output in hyperlinks format.You can simply copy sublist3r output, paste it in gmail and mail it to yourself to get the output URL’s as hyperlinks.

Thanks for taking time to read my blog. For any questions, you can get in touch with me at Syntaxerror
