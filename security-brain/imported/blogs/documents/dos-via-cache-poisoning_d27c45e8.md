---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-17_dos-via-cache-poisoning.md
original_filename: 2023-05-17_dos-via-cache-poisoning.md
title: DOS via cache poisoning
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: d27c45e8d37cff595bdd9b7929ed1d9fd57bbbb7be6d0832d779537835a452be
text_sha256: 42877ce7f7e8a7ee2a00e9048ba1f3fe78bb194cf6093cebdee036a6b34959e0
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# DOS via cache poisoning

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-17_dos-via-cache-poisoning.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `d27c45e8d37cff595bdd9b7929ed1d9fd57bbbb7be6d0832d779537835a452be`
- Text SHA256: `42877ce7f7e8a7ee2a00e9048ba1f3fe78bb194cf6093cebdee036a6b34959e0`


## Content

---
title: "DOS via cache poisoning"
url: "https://medium.com/@zhero_/dos-via-cache-poisoning-38f3a87f997c"
authors: ["Allam Rachid (@blank_cold)"]
bugs: ["Web cache deception", "DoS"]
publication_date: "2023-05-17"
added_date: "2023-05-18"
source: "pentester.land/writeups.json"
original_index: 1146
scraped_via: "browseros"
---

# DOS via cache poisoning

DOS via cache poisoning
Rachid.A
Follow
8 min read
·
May 17, 2023

302

7

Press enter or click to view image in full size
source: somewhere on twitter

Today I’m going to talk about cache, denial of service, and a vulnerability I recently found in a very large company.

Hello hunters, let’s take a closer look at how cache poisoning works and how I was able to exploit this vulnerability to get a DOS on the home page of a large company.

To start, what is a (web) cache?

A cache is an intermediate memory system used to temporarily store data in order to optimize rendering performance when browsing a website.

There are several caching systems:

Client-side (local) -> Browser caching, storage on user’s machine.
Server side -> This approach makes it possible to store for a limited period — more or less long — the response of certain requests and avoids overloading the server by serving users making a similar request a response directly from the cache. This significantly improves site performance because the web server is much less busy.
Press enter or click to view image in full size
Source: PortSwigger

You will surely have understood that the caching system that interests us here is the server side. If we assume that:
- the cache provides an identical response to users who have made a similar request
- cached responses are stored for a limited time

What happens if we cache a malicious version (save) of the site and this version is then served to users who visit the site after us?

Cache Poisoning

Definition from PortSwigger: Web cache poisoning is an advanced technique whereby an attacker exploits the behavior of a web server and cache so that a harmful HTTP response is served to other users.

A successful web cache poisoning attack can lead to several types of attacks depending on the nature of the payload stored — in the cache — by the attacker: HTMLi, XSS, Open redirection, DOS..

Cache behavior

In order to exploit the behavior of the cache as an attacker it is necessary to understand how it works. I said earlier: “the cache provides an identical response to users who made a similar request”, but how does the cache define that it is a similar request?

This is where “Cache Keys” come in : when the cache receives a request, it compares some of its components (request line, host, some headers, etc.) with the requests from the responses it has saved.

We can imagine that all of these components — called cache keys — form like a “fingerprint”, if this request “fingerprint” is found then the cache returns the corresponding response, otherwise — considering that it has not saved the corresponding response to the request — it forwards the request to the web server.

The components of the request that are not included in the cache key are called “unkeyed”, the cache does not take them into consideration during the comparison, which is very interesting for an attacker: if one of these unkeyed — any header — is reflected on the response in a dangerous way (HTMLi, XSS, DOS..), this will allow:

To store a “poisoned” response in the cache
Serve this response to users. The cache will not consider the header added by the attacker during the comparison because it is not part of the cache keys

This will result in cache poisoning.

Cache keys vary and depend on the configuration of the cache in question, sometimes only the request line and host are included, and all other components of the request are unkeyed. It is therefore essential — as an attacker — to go through a phase of analysis and understanding of the target cache in order to identify the cache keys, the caching duration, etc.

From cache poisoning to DOS

I had the opportunity to exploit some cache-related vulnerabilities on different programs and I recently found — in fairly short time intervals — two cache poisoning leading to a DOS, one of which was on a very big company.

The first thing to do to identify this type of vulnerability is to analyze the server response:

Press enter or click to view image in full size
HTTP response
First important element here: the “X-Cache” header, we see that its value is “HIT” indicating that the response comes from the cache. Otherwise, its value would have been “MISS”, I specify that the presence of X-Cache is not systematic. Sometimes similar headers perform the same function and are quite easily identifiable, the value being HIT or MISS.
Second important element: the “Age” header, indicating the number of seconds since the cached (storage) of the response/resource that was served to us. This header is sometimes accompanied by the “Cache-Control” header containing the caching directives, an important directive for us — missing in the above response — is “max-age” indicating the time limit in seconds for storing the resource.
The information transmitted by these two headers is particularly useful for an attacker to know exactly when to send his malicious request so that it is cached.
Third important element: the “Vary” header can be a great help when identifying the cache key, Vary is often used to specify additional headers to be part of the cache key ; “Accept-Encoding” and “x-wf-forwarded-proto” in the case of our answer above, but it can also include user-agent or even cookies.. etc. I specify that there are sometimes additional headers forming part of the cache key not being specified in “Vary”.
Cache Buster

Before going any further, I would quickly like to introduce an important concept to prevent some people from breaking sites in production.

source: somewhere on twitter

Some request components are often included in the cache key, starting with the URL parameters (except in specific cases):

Get Rachid.A’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

-> If the cache stores the response from: https://www.example.com/
-> And a user requests: https://www.example.com/?test=test

Then the cache — when comparing the cache keys — will not find an identical version and will forward the request to the server (the URL/request line being part of the cache key).
And it is precisely this behavior that we will use as researchers in order to carry out tests without compromising the target; during our tests, we will always add a parameter to the target URL so that the cached version — potentially poisoned — is only accessible from the URL containing our unique parameter. We will avoid harming the users of the platform in question and can carry out our tests quietly.

Performing an attack via its cache buster is obviously sufficient — and mandatory — for a proof of concept when writing the report.

Back to attack

After analyzing the server response I know that a cache system is in place and I am aware of two headers as part of the cache key:

- “Accept-Encoding”
- “x-wf-forwarded-proto”

I start by doing small tests to find interesting headers being “unkeyed” (not part of the cache key) like “X-Forwarded-For”, “X-Host”, “X-Forwarded-Scheme” .. etc but nothing conclusive.

I won’t go into the details of the different search methods to find a “Cache Deception” vulnerability here, but maybe in a future article, it doesn’t say anything conclusive during my tests at this level either.

On the other hand, I know that the “X-Timer” header — present in the response — is often reflected if a value is specified in the request. This header is harmless for a classic HTMLi/XSS type attack because it is reflected in the headers but not the HTML code, so I tried to cause an error in the back-end hoping that the error is saved in the cache :

Press enter or click to view image in full size
HTTP request/response

I open a second browser and then try to access the URL — containing my cache buster (?mycachebuster=zhero_):

Press enter or click to view image in full size
Browser view

DOS done! Making the main page completely inaccessible.

A few comments :

For the attack to be interesting, the DOS must be — in the best case — on the main homepage, the link to certain resources like a CSS or a font file does not have much impact.
It is sometimes necessary to resend the “poisoned” request several times so that it is stored in the cache. As you may have noticed from the answer above, no cache information appears. It is therefore through trial and error that it will be necessary to go through to understand the operation of the cache to be exploited.
It may be useful to perform a test via another IP address (from the same location) to ensure that the cache poisoning is effective.
This move was simple, but it is often necessary to adjust the headers of its request so that they correspond to the cache keys of the target: most often it is the User-Agent, the Accept-Encoding or Accept-Language. Otherwise, you will be unable to retrieve the poisoned response — from the cache — on another browser -> X-Cache (or similar header) will always return “MISS”.
Another DOS via cache poisoning

This time the “unkeyed key” that helped me was “X-Forwarded-Host”. Any value with this header caused a 404 error stored in the cache, making the main page of a large company completely inaccessible — of which you are surely the customers one way or another — :

Press enter or click to view image in full size
HTTP request/response

Checking from another browser :

Press enter or click to view image in full size
Browser view

DOS success! 💉

You will surely have understood that the same attack is possible without the cache buster. Even if the caching is limited in terms of time (longer or shorter depending on the configuration), it is very easy for an attacker to make this attack “permanent” using a small script returning “poisoned” requests at regular time intervals based on caching duration.

If you find an unusable “unkeyed” header — in terms of XSS etc — consider DOS as a last resort : If you manage to cause an error in the back-end and cache the response then you have your vulnerability (provided of course that the DOS is done on an interesting page and not a CSS or other resource).

Little extra tip: I read on an article by researcher bombon (H1 username) that it was possible to cause an 400 error by adding an illegal header when it comes to Akamai CDN, ex:

\: 

The caching of the error will then depend on the cache configuration.

Thank you for reading me, if you have any questions do not hesitate to let me know. Happy hunting 🏹

My Twitter account : https://twitter.com/zhero___
My Linkedin account : https://www.linkedin.com/in/rachid-allam-65477718a/

Take a look at my previous write-up titled : A successful prototype pollution chained to a DOM XSS

https://medium.com/bugbountywriteup/a-successful-prototype-pollution-chained-to-a-dom-xss-9887087b56a4

AI-Powered Cyber Threat Detection and Response: SIEM and Compliance solution powered by AI, real-time correlation, and threat intelligence. Built for simplicity, reduced noise and affordability. Learn More
