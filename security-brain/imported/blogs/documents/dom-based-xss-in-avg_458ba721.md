---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-02-26_dom-based-xss-in-avg.md
original_filename: 2013-02-26_dom-based-xss-in-avg.md
title: DOM Based XSS In AVG
category: documents
detected_topics:
- xss
- sso
- command-injection
tags:
- imported
- documents
- xss
- sso
- command-injection
language: en
raw_sha256: 458ba7215c6233f49e9dd14f96e29aac82be28410d2befb36f3f74dbf87b9e9d
text_sha256: b7792f4544d43c8ec1131850d7993115648b8af42ea0dca2e5cae4f84ffd5d5b
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# DOM Based XSS In AVG

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-02-26_dom-based-xss-in-avg.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `458ba7215c6233f49e9dd14f96e29aac82be28410d2befb36f3f74dbf87b9e9d`
- Text SHA256: `b7792f4544d43c8ec1131850d7993115648b8af42ea0dca2e5cae4f84ffd5d5b`


## Content

---
title: "DOM Based XSS In AVG"
page_title: "DOM Based XSS In AVG - RHA Blog"
url: "http://www.rafayhackingarticles.net/2013/02/dom-based-xss-in-avg.html"
final_url: "http://www.rafayhackingarticles.net/2013/02/dom-based-xss-in-avg.html"
authors: ["Rafay Baloch (@rafaybaloch)", "David Vieira-Kurz (@secalert)"]
programs: ["AVG"]
bugs: ["DOM XSS"]
publication_date: "2013-02-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6409
---

![](https://twimg0-a.akamaihd.net/profile_images/1272438885/DOMInatrixss.png)

  
Lately, i have been researching on DOM based XSS a bit, Recently i found a DOM based XSS in AVG, DOM based XSS is caused due to lack of input filtering inside client side javascripts, since most of the code is moving towards client side, therefore DOM based xss have been very common now a days, It is predicted by the experts that the DOM based xss mostly occurs in the websites that heavily rely upon javascripts.  
  
With that being said, let's take a look at the DOM based XSS POC:  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCokSGWCDwUf43eAB1f7B0gAWLhR7bpzYx3dM-JZ9slSsorkP1-_U39TKcT8sNus0J4xqrBqF4p66uwnMyOSE8M1zFfS0rj_PjkBV3nUQMyfzoR-S6phbOyiOYvIBKoPFlkbaktNVf-n8/s640/AVG.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCokSGWCDwUf43eAB1f7B0gAWLhR7bpzYx3dM-JZ9slSsorkP1-_U39TKcT8sNus0J4xqrBqF4p66uwnMyOSE8M1zFfS0rj_PjkBV3nUQMyfzoR-S6phbOyiOYvIBKoPFlkbaktNVf-n8/s1600/AVG.png)  
  
  
The vulnerability is the result of lack of escaping done in "js_stdfull.js". The following is the screen shot of the vulnerable code causing the DOM based XSS:  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhukQ2LJ0oELu1OYOMcXvRVl9rYkkyXH_7-hj2EefkoutHQz4d-EtClIr6XLCIQbzrWkYv13X7GD0zgMty-Yzf_nBVMuTlSyNbHI5D9X9bgJBVu1jrUu_J1OE5A-VN5BcQemONkOT8kxgY/s640/AVG-DOM-XSS.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhukQ2LJ0oELu1OYOMcXvRVl9rYkkyXH_7-hj2EefkoutHQz4d-EtClIr6XLCIQbzrWkYv13X7GD0zgMty-Yzf_nBVMuTlSyNbHI5D9X9bgJBVu1jrUu_J1OE5A-VN5BcQemONkOT8kxgY/s1600/AVG-DOM-XSS.png)

  

**Vulnerable code:**  
  
//display the correct tab based on the url (#name) var pathname = $(location).attr('href');var urlparts = pathname.split("#");  
  
I would like to give full credits to **David Vieira-Kurz from Majorsecurity.com (@secalert)** , for helping me sort out the vulnerable code.  
  
Yet another security researcher, David Sopas also found the same issue but on the English version of the site:  
**  
http://labs.davidsopas.com/2013/01/avg-vulnerable-to-dom-xss.html**
