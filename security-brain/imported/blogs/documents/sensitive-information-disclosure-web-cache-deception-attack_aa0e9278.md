---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-26_sensitive-information-disclosure-web-cache-deception-attack.md
original_filename: 2019-06-26_sensitive-information-disclosure-web-cache-deception-attack.md
title: 'Sensitive Information Disclosure: Web Cache Deception Attack'
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: aa0e92780c971e744743e5868c4025de0367f8049c9c9d5dbb0c4cbefeafc8b0
text_sha256: 4431822ea444f750e7c17637ff97e1d8648a05797a1417cfda621014f698d238
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Sensitive Information Disclosure: Web Cache Deception Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-26_sensitive-information-disclosure-web-cache-deception-attack.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `aa0e92780c971e744743e5868c4025de0367f8049c9c9d5dbb0c4cbefeafc8b0`
- Text SHA256: `4431822ea444f750e7c17637ff97e1d8648a05797a1417cfda621014f698d238`


## Content

---
title: "Sensitive Information Disclosure: Web Cache Deception Attack"
url: "https://medium.com/@dr.spitfire/sensitive-information-disclosure-web-cache-deception-attack-bcac6cb9cd86?sk=a2557f0c557ff38876141c2d94b296dd"
authors: ["Wasim Shaikh (@Wa_sim_sim)"]
programs: ["Intuit"]
bugs: ["Information disclosure"]
publication_date: "2019-06-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5184
scraped_via: "browseros"
---

# Sensitive Information Disclosure: Web Cache Deception Attack

InfoSec Brothers
Follow
4 min read
·
Jun 26, 2019

119

Sensitive Information Disclosure: Web Cache Deception Attack

Dear infosec community,

Great to see you back!!!

Thank you so much for sharing my last few write-ups on Twitter, LinkedIn and even on Facebook! Because of your encouragement and enormous support, I was able to see statistics of my story readers going high. This is huge for me!!!

In this write-up, I am going to explain to you guys another attack scenario known as “Web Cache Deception Attack”. Let’s understand it briefly.

Web Cache :

Did it ever occur to you that when you send the request to access some files such as .css, .js, .jpg and .txt sometimes, you get the response from the web server very quickly as compare to the requests you send in order to retrieve other data? Yes, if you have noticed, it happens. It happens because of the concept known as Cache. When we send the request, the server will categories the requests in two ways (in this context), request to access dynamic content and request to access static content. The files that I mentioned earlier comes under the category of static content. Websites often tend to use web cache functionality (for example over a CDN, a load balancer, or simply a reverse proxy). The purpose is simple: store files that are often retrieved such as static data files, to reduce latency from the web server.

Let’s understand what happens behind the wall in the eyesight of spitfire.

Get InfoSec Brothers’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Consider a website, “http://www.example.com” is hosted behind the CDN, a load balancer or a reverse proxy. A user sends the request to access the home page of a website after login. A user sent a request “http://www.example.com/home.php”. A web server sends the response back to the user with the content that he/she gets after authentication. A user sends another request like, “http://www.example.com/files/abcd.css” and the server responds back. However, when the server sends back this request, the reverse proxy (deployed between the user and the web server) stores that data in its cache considering it as static content. When next time a user requests abcd.css file, reverse proxy will not send that request to the web server, instead, it will serve the user with the data that it had stored in its cache. Thus, the request for static data is not reaching the web server again. So, to sum up, given below is the actual scenario,

I hope, I was able to explain the concept of reverse proxy or cache to all of you very briefly and very well. If you have understood this, let’s move ahead and I will explain to you the advantage the attacker takes keeping the concept of Web Cache in the mind.

Web Cache Deception:

As the attacker knows the website is hosted behind some kind of proxies, CDNs or load balancer. The attacker will access “http://example.com”. After the authentication, the attacker is getting the next page and that is “http://example.com/home.php”. The attacker will send a URL that will look like request to access the static web pages those are available to access to anyone even without authentication. So the crafted URL by the attacker is “http://example.com/home.php/test.css”. However, as there is no such web page, the web server responds back with the data for “http://example.com/home.php”. But the URL in the browser looks like “http://example.com/home.php/test.css”. So, in this scenario, the attacker is getting data for “http//example.com/home.php” even he has requested “http://example.com/home.php/test.css”. This is the best case scenario to test the web cache deception attack. Now, when the request from an unauthenticated source will go, the proxy server will not send that request to the Web server, instead, the proxy server will respond back with the data that must be seen only by the authenticated user. Given below is the scenario that is described by Omar Gil while describing his bug bounty 
PayPal Engineering
.

Press enter or click to view image in full size
Condition to test Web Cache Deception

Web Cache Deception Attack by Spitfire

Please watch below video POC,

After reporting above bug to 
Intuit
, 
Intuit QuickBooks
, I got the Hall of Fame from them.

Press enter or click to view image in full size
Wasim Shaikh Will be here as long as the Intuit is there!

I hope I have explained to you the concept of cache, how to find the cache deception vulnerability. Following are widely accepted suggestions to prevent or to fix the Web Cache Deception Vulnerability.

Mitigation
Configure the cache mechanism to cache files only if their HTTP caching headers allow. That will solve the root cause of this issue.
If the cache component provides the option, configure it to cache files by their content type.
Configure the web server so that for pages such as http://www.example.com/home.php/non-existent.css, the web server doesn’t return the content of “home.php” with this URL. Instead, for example, the server should respond with a 404 or 302 response.

To have a deep understanding of this attack scenario, please visit the following blog by Omar Gil.

Web Cache Deception Attack
Web cache deception is a new web attack vector that puts various technologies and frameworks at risk. 1. Websites often…

omergil.blogspot.com

./RedirectYourselfToSomewhereElse

To know about my upcoming write-ups and to read them, follow me on Medium and Twitter: https://twitter.com/Wa_sim_sim

Thank you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
