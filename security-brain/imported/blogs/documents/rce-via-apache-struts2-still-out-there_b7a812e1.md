---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-27_rce-via-apache-struts2-still-out-there.md
original_filename: 2020-02-27_rce-via-apache-struts2-still-out-there.md
title: RCE via Apache Struts2 - Still out there.
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: b7a812e1a61ce7524d90a6161b453038f3474ce0bd05928a6768246f25a9fa9e
text_sha256: 614687236e926ba6635af5f84d79c97ebee6f5dbffcb95193cb78b6dfa0c21b0
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# RCE via Apache Struts2 - Still out there.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-27_rce-via-apache-struts2-still-out-there.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b7a812e1a61ce7524d90a6161b453038f3474ce0bd05928a6768246f25a9fa9e`
- Text SHA256: `614687236e926ba6635af5f84d79c97ebee6f5dbffcb95193cb78b6dfa0c21b0`


## Content

---
title: "RCE via Apache Struts2 - Still out there."
url: "https://medium.com/@abhishake100/rce-via-apache-struts2-still-out-there-b15ce205aa21"
authors: ["Abhishek (@abhishake100)"]
bugs: ["RCE"]
publication_date: "2020-02-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4749
scraped_via: "browseros"
---

# RCE via Apache Struts2 - Still out there.

RCE via Apache Struts2 - Still out there.
Abhishek
Follow
2 min read
·
Feb 27, 2020

208

2

Apache Struts2 was discovered years ago but still we can find instances of it around the internet.

Press enter or click to view image in full size

Curated list of Bug bounty programs — https://bugbountydirectory.com

I reported a few vulnerabilities to this website and so they gave me another website that they owned to see if i could find any vulnerabilities in them.

Press enter or click to view image in full size

Within a few days i managed to find few Reflected XSS and CSRF issues. After reporting it to them they said that they were aware of the issues and are in the process of fixing it.

After looking here and there i didn't find anything valuable to report.

I knew that the web app was running java with the help of wappalyzer and so by doing bit of google-fu i found endpoints that were ending with .action

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

site:redacted.com filetype:action

Press enter or click to view image in full size

If you find endpoints ending with .action, .do, .go that means that the website is running Struts2 and might be vulnerable. To exploit this we send a Content-Type header that has a specially crafted message.

Content-Type: %{#context[‘com.opensymphony.xwork2.dispatcher.HttpServletResponse’].addHeader(‘Namehere’,4*4)}.multipart/form-data

Content-Type: .multipart/form-data~%{#context[“com.opensymphony.xwork2.dispatcher.HttpServletResponse”].addHeader(“Namehere”,4*4)}

These are the 2 headers, you can try both to check if the server performs the multiplication of the numbers or any other operation.

Press enter or click to view image in full size

In my case the second one worked and it added a new header Abhishek: 16 which proves that the server is vulnerable.

This is enough to prove that RCE exists but for POC i used the below script to run commands and i had root access on the server.

mazen160/struts-pwn
python struts-pwn.py --url 'http://example.com/struts2-showcase/index.action' -c 'id' python struts-pwn.py --list…

github.com

Press enter or click to view image in full size

I reported it quickly and they fixed it within couple of days. Hope you learned something, if you liked then please share.

Follow me on twitter — https://twitter.com/abhishekY495

Thank You.
