---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-07_html-injection-to-xss-bypass-in-redactedcom.md
original_filename: 2019-12-07_html-injection-to-xss-bypass-in-redactedcom.md
title: HTML Injection to XSS bypass in [REDACTED.com]
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
raw_sha256: 08c6ab33ba26186a533b026fa6283b92348e5ee5461b98f1f216ad0baf9f6f4e
text_sha256: b68eb9b1bf602a016458070daf794b7e06d612b61ea054ffa7708e9fc74c09f3
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# HTML Injection to XSS bypass in [REDACTED.com]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-07_html-injection-to-xss-bypass-in-redactedcom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `08c6ab33ba26186a533b026fa6283b92348e5ee5461b98f1f216ad0baf9f6f4e`
- Text SHA256: `b68eb9b1bf602a016458070daf794b7e06d612b61ea054ffa7708e9fc74c09f3`


## Content

---
title: "HTML Injection to XSS bypass in [REDACTED.com]"
page_title: "Evan Ricafort | Blog: HTML Injection to XSS bypass in [REDACTED.com]"
url: "https://blog.evanricafort.com/2019/12/html-injection-to-xss-bypass-in.html"
final_url: "https://blog.evanricafort.com/2019/12/html-injection-to-xss-bypass-in.html"
authors: ["Evan Ricafort (@evanricafort)"]
bugs: ["Reflected XSS"]
bounty: "600"
publication_date: "2019-12-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4904
---

Howdy!  
  
In this article I will show this simple vulnerability that I found in <redacted.com>. A simple HTML Injection to XSS bypass due to improper sanitation. The web application has a Chat Room feature for their users/customers and due to the improper sanitation, the Room Name become the vulnerable input for the HTML & XSS.  
  
So long story short, here's the report timeline and proof of concept of this issue.  
  
**_\--Proof of Concept--_**  
  
1\. Go to https://<redacted.com>/<redacted>chat  
2\. Click Create Room  
3\. Input payload for the room name  
  
Payload: <input/onfocus=prompt(document.domain) autofocus>  
  
4\. Click Ok  
5\. You will notice that the room name will be an input box. now type on that box and see the result.  
  
In result; the payload will make an input box and when a user types any text on the input, the payload will trigger which can results into Cookie Stealing.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz1et8GWDgXXt1wvb_oxEilJrTxCYdw6avd0azEGF7YNQyy35A3FuX2F9HgObEAXxKm2f53ilI-4ro0qf2DwctoLEvkArRct0TsmCMT6Be9avwyoObeN452xxw82ZLQpb_8sZdeJe7/s640/Screenshot_3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz1et8GWDgXXt1wvb_oxEilJrTxCYdw6avd0azEGF7YNQyy35A3FuX2F9HgObEAXxKm2f53ilI-4ro0qf2DwctoLEvkArRct0TsmCMT6Be9avwyoObeN452xxw82ZLQpb_8sZdeJe7/s1600/Screenshot_3.png)

  
Tested in Firefox 56 Windows 10 Platform  
  
  
**_\--Timeline--_**  
  
Reported: Nov 12, 2019, 2:04 AM  
Fix Confirmation: Nov 25, 2019, 9:52 PM  
Bounty: $600  
  

> _Thanks. I believe it is the largest bounty we have ever paid (we are a very small company), but it was also the most serious/complex vulnerability ever reported._

  
So I hope you enjoy this write up and have a great day everyone!
