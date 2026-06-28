---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-25_fun-with-cors-misconfiguration-ii.md
original_filename: 2020-04-25_fun-with-cors-misconfiguration-ii.md
title: Fun With CORS Misconfiguration — II
category: documents
detected_topics:
- xss
- cors
- command-injection
- information-disclosure
tags:
- imported
- documents
- xss
- cors
- command-injection
- information-disclosure
language: en
raw_sha256: c65c42f7f1239df48b33251535042b7f34ec14c84922a6f966d7ae89b8c8045d
text_sha256: 2ee506cb4175d04945bdd581d17ecf7d80c347513a886471cc14bb569c01c7bb
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Fun With CORS Misconfiguration — II

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-25_fun-with-cors-misconfiguration-ii.md
- Source Type: markdown
- Detected Topics: xss, cors, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c65c42f7f1239df48b33251535042b7f34ec14c84922a6f966d7ae89b8c8045d`
- Text SHA256: `2ee506cb4175d04945bdd581d17ecf7d80c347513a886471cc14bb569c01c7bb`


## Content

---
title: "Fun With CORS Misconfiguration — II"
url: "https://medium.com/@amangupta566/fun-with-cors-misconfiguration-ii-927caccfe932"
authors: ["Aman Gupta (@gupt4j1)"]
bugs: ["CORS misconfiguration", "XSS"]
publication_date: "2020-04-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4631
scraped_via: "browseros"
---

# Fun With CORS Misconfiguration — II

Fun With CORS Misconfiguration — II
Aman Gupta
Follow
2 min read
·
Apr 25, 2020

127

Hello all again, I hope everything in going well on your ends. Today I will explain further about CORS misconfiguration leading to sensitive information leaks!!!!

If you haven’t read my previous blog, Please do refer the below link:

CORS Misconfiguration Leads To Steal Sensitive Information Disclosure
Hello everyone, today I am going to share CORS misconfiguration can leads to sensitive information disclosure.

medium.com

So this time the web application, vulnerable.com was trusting all its subdomains. Meaning that any subdomain can take the sensitive data, its meaningful because that’s their domain so they can trust their own domain. But the things can go wrong if attacker finds some vulnerability on the subdomain and use it to exploit the CORS misconfiguration.

This time the scenario was like this:

GET /sensitiveData HTTP/1.1
Host: vulnerable.com
Origin: https://example.vulnerable.com

This is the response I received from the server:

HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://example.vulnerable.com
Access-Control-Allow-Credentials: true
...

Press enter or click to view image in full size

Now it’s confirmed that the application trusts all its subdomain. The server settings to CORS was something like this:

Access-Control-Allow-Origin: *.vulnerable.com

So to exploit this misconfiguration we can try to find two vulnerabilities on their subdomains:

Cross-Site Scripting on any of the subdomain.
Subdomain takeover: So that we can craft our own JavaScript on that subdomain and can fool the victim.

I tried finding the vulnerabilities on the subdomain and I found reflected XSS on one of their subdomain, say: https://test.vulnerable.com.

Press enter or click to view image in full size

Now the only thing I need to do is to inject Malicious JavaScript on that subdomain and engage victim to visit that page.

Get Aman Gupta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Injecting the following payload into the subdomain where XSS exists will result to the exploitation of CORS misconfiguration:

function cors(){var xhttp=new XMLHttpRequest();xhttp.onreadystatechange=function(){if (this.readyState ==4&& this.status==200){alert(this.responseText)}};xhttp.open(“GET”, “https://vulnerable.com/auth/user”, true);xhttp.withCredentials=true;xhttp.send();}

So the name parameter in the subdomain was vulnerable and the XSS payload was like:

“ onclick=”[payload]

So it will get injected and CORS misconfiguration exploited successfully.

Thanks for reading.

Feedback and suggestions are most welcome!!

Twitter: https://twitter.com/gupt4j1
