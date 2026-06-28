---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-01_dom-based-xss-in-microsoft.md
original_filename: 2017-06-01_dom-based-xss-in-microsoft.md
title: DOM Based XSS In Microsoft
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
raw_sha256: 389d8b699f4860b4a8801d2299159b3d75b491e42c909d317c958e02c8439650
text_sha256: 2a0404a013d1605486abff585f1deb929c7d9b5979e3a04181c6c8e1d5df64fa
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# DOM Based XSS In Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-01_dom-based-xss-in-microsoft.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `389d8b699f4860b4a8801d2299159b3d75b491e42c909d317c958e02c8439650`
- Text SHA256: `2a0404a013d1605486abff585f1deb929c7d9b5979e3a04181c6c8e1d5df64fa`


## Content

---
title: "DOM Based XSS In Microsoft"
page_title: "DOM Based XSS In Microsoft - Miscellaneous Ramblings of a Cyber Security Researcher"
url: "https://www.rafaybaloch.com/2017/06/dom-based-xss-in-microsoft.html"
final_url: "https://www.rafaybaloch.com/2017/06/dom-based-xss-in-microsoft.html"
authors: ["Rafay Baloch (@rafaybaloch)"]
programs: ["Microsoft"]
bugs: ["DOM XSS"]
publication_date: "2017-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6189
---

![](https://twimg0-a.akamaihd.net/profile_images/1272438885/DOMInatrixss.png)  
Lately, i have been researching on DOM based XSS a bit, In my previous post i talked about the [DOM based XSS i found inside AVG](http://www.rafayhackingarticles.net/2013/02/dom-based-xss-in-avg.html), DOM based XSS is caused due to lack of input filtering inside client side javascripts, since most of the code is moving towards client side, therefore DOM based xss have been very common now a days, It is predicted by the experts that the DOM based xss mostly occurs in the websites that heavily rely upon javascripts.  
  
I have reported several DOM based XSS inside Microsoft, most of them were due to the lack of input filtering/sanitization inside of the several tracking scripts such as sitecatalyst and riotracking scripts as they often introduce some vulnerable sources and sinks. With that being said, let's take a look at the POC of the attack:  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxPqEPcD8qpYQSaGDH46-yra0Zci0C97AUq6We_nKSTBunrnrs5-74_Z4ozp0OToZH5jkDRCZODHE6ncA3uP-1ELkQwUugnBcMBJ3Cj_w9ylkJk4gOY44DQ5aQn4FCHthPT2D6fxGoeZQ/s640/MS+DOMXSS.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxPqEPcD8qpYQSaGDH46-yra0Zci0C97AUq6We_nKSTBunrnrs5-74_Z4ozp0OToZH5jkDRCZODHE6ncA3uP-1ELkQwUugnBcMBJ3Cj_w9ylkJk4gOY44DQ5aQn4FCHthPT2D6fxGoeZQ/s1600/MS+DOMXSS.png)

  
The vulnerability occurs due to lack of filtering being done inside **riotracking script**(Line 58), There are other microsoft domains that are also using the same tracking script vulnerable to DOM based XSS, see if you can find one?.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4e5DTzlkywmrAH_A8GBmThyKv9BiJeffOO9kaD7RJ1weX4G6pfS72qGAuAhdFJfA4xnUgUbBsvPKmQT8HVnoP7m_B0bYdNl85S5pNwW6YvbGHGm8EfSdfJ_5jwcbPBliq52NnSGaLemI/s640/Untitled.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4e5DTzlkywmrAH_A8GBmThyKv9BiJeffOO9kaD7RJ1weX4G6pfS72qGAuAhdFJfA4xnUgUbBsvPKmQT8HVnoP7m_B0bYdNl85S5pNwW6YvbGHGm8EfSdfJ_5jwcbPBliq52NnSGaLemI/s1600/Untitled.png)
