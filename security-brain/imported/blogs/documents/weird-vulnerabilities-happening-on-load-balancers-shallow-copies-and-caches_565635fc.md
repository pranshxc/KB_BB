---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-11_weird-vulnerabilities-happening-on-load-balancers-shallow-copies-and-caches.md
original_filename: 2020-02-11_weird-vulnerabilities-happening-on-load-balancers-shallow-copies-and-caches.md
title: Weird Vulnerabilities Happening on Load Balancers, Shallow Copies and Caches
category: documents
detected_topics:
- automation-abuse
- idor
- access-control
- xss
- sqli
- command-injection
tags:
- imported
- documents
- automation-abuse
- idor
- access-control
- xss
- sqli
- command-injection
language: en
raw_sha256: 565635fc9dbea68f2dae2031ab3d4121f9be9de5e507236461e7b51cd734ab43
text_sha256: d2639a3204a2a6857bb679223998698a7da6a4b2163f821f587118cac9a4e8e8
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Weird Vulnerabilities Happening on Load Balancers, Shallow Copies and Caches

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-11_weird-vulnerabilities-happening-on-load-balancers-shallow-copies-and-caches.md
- Source Type: markdown
- Detected Topics: automation-abuse, idor, access-control, xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `565635fc9dbea68f2dae2031ab3d4121f9be9de5e507236461e7b51cd734ab43`
- Text SHA256: `d2639a3204a2a6857bb679223998698a7da6a4b2163f821f587118cac9a4e8e8`


## Content

---
title: "Weird Vulnerabilities Happening on Load Balancers, Shallow Copies and Caches"
url: "https://medium.com/@ozguralp/weird-vulnerabilities-happening-on-load-balancers-shallow-copies-and-caches-9194d4f72322"
authors: ["Ozgur Alp (@ozgur_bbh)"]
bugs: ["Information disclosure"]
bounty: "1,500"
publication_date: "2020-02-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4776
scraped_via: "browseros"
---

# Weird Vulnerabilities Happening on Load Balancers, Shallow Copies and Caches

Weird Vulnerabilities Happening on Load Balancers, Shallow Copies and Caches
Ozgur Alp
Follow
6 min read
·
Feb 11, 2020

192

When looking for security vulnerabilities on a web application - either for bug hunting or a penetration test project -, I always check 2 things at last when I was clearing my testing up on a target:

Searching used user account’s personal information on the HTTP responses via Burp History Log such as username, e-mail address, phone number etc.
Analyzing all gathered e-mail addresses on the HTTP responses via Burp Passive Scan

The main reason for conducting these items was actually trying to find different attack endpoints especially for the attacks such as IDOR and Access/Privacy issues at first. However, in time, it is evolved to an essential clearing up item for me which also allowed me discovering super strange bugs I have ever did. I will share some examples of these vulnerabilities - which you probably missed the similars in the back due to not paying any attention to them.

#Example 1 — A Weird Load Balancer Misconfiguration

This was the first time I was ever seen a situation like this before. While I was checking the all gathered e-mail addresses on the HTTP responses on Burp Passive Scan results, I saw a gmail e-mail address which does not belongs to mine. While I checked where this was existing, I saw a script code line like this on an endpoints HTML source code:

Press enter or click to view image in full size
Weird user information on the javascript block

It was super strange because when I was sending the main request to the repeater and repeat the request again, I was seeing my own e-mail address, user id and user settings instead of this one leaked. So how this happened and I gathered any other’s e-mail address?

After some testing, I figured out that not having a specific “cookie” on the prior request of this request was confusing the load balancer configuration and returning another user’s information on the javascript block! So whoever visits this website within deleting all cookies, was actually gathering another user’s e-mail address at first on the HTTP responses. However, since it was just happening on the source-code, probably nobody discovered that issue before.

Repeating this process was leaking thousands of registered users sensitive information like on the below.

Press enter or click to view image in full size
Another leaked user’s information, which was probably doing some tests with “+synack” registered e-mail address :)

Reported it & earned approximately $400 bounty from it.

#Example 2 — Whitelist My E-mail Please

After finding the first of my weird example, I started to paying attention for these kind of issues much longer on my testings. After a few days, I found out 17 strange e-mail addresses existing on a script block again assigned as whitelistExternalUserEmails parameter value, on a very common web page’s home page.

Press enter or click to view image in full size
Leakage of 17 e-mail addresses on script block

I checked these e-mail addresses on the pages such as registration or forgot password to see whether they are already registered users or not for the application and it came out all was working accounts. This figured out lately that whitelisted users for that application excluded from some security controls (Still wonder what is exactly, maybe WAF?), however this security configuration was also adding a script block mistakenly to the main page.

Get Ozgur Alp’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reported it & earned approximately $800 bounty from it within an incentive.

#Example 3 — Load Balancer Strikes Again

On a penetration testing project I involved on that time period, I found a similar leakage like the first example that I shared, on my Burp Passive Scanner Log as:

Press enter or click to view image in full size
Another user’s information is leaked on the script block again

The difference between the first and this one was, I actually never reproduced it again and gathered any other users information, no matter what I tried. With the confidence of my prior experience & help of the being this one a penetration testing project, I shared my finding and concerns within client directly. After an investigation from their side, client found out why the issue happened and explained it within the following words:

Due to a shallow copy of an object in back-end, an object with references to other customer data was cached. When that object is returned, the vulnerable page is rendered with multiple instances of customer data.”

So it was a one time thing per hour happening, which was actually super hard to both find and reproduce as well. With the help of aligning stars & Burp Passive scanner, glad that I found it out and client resolved!

#Example 4 — Steal My Authorization Header Please

While I was searching my registered user’s username on the HTTP responses I visited, I found out that one JavaScript file contains it, within also my authorization security header for the application API’s! Classical XSSI vector, right?

Well, before trying an XSSI, I found out that deleting all session cookies for that request still returns my username and authorization header such as:

Press enter or click to view image in full size
Leakage of username & authorization header in JS response

Which was a very strange behavior that I didn’t expected at all. Steps I continued tested:

Changing loc parameter was deleting all leaked information on the response.
Visiting same endpoint from second user account was also returning the second users information.
Deleting all the session cookies was returning the second user’s information again.

Could it be?

Well, because it was a javascript file, the file was cached at the CDN within having different parameter values. So changing loc parameter to an invalid one such as phishing & sending it to the victim & clicked to the link as victim were causing the caching of the victims authorization header as JS file!

Press enter or click to view image in full size
Caching the victim’s authorization header

At first sight, this vulnerability was a similar one to the Web Cache Deception Attack but it was actually more from that. Since this JS files were actually cached without any user interaction on the normal process of the application, within valid loc parameters, which were actually the referrer endpoints that was calling to javascript file, it was possible to also gather other users usernames and authorization headers within brute-forcing loc parameter which could be gathered from Burp History Log. Automation of this system and running it repetitively may actually let an attacker to steal all authenticated users information.

Reported it & earned approximately $300 bounty from it, which is reduced because the leaked authorization header was not too privileged to conduct user operations; still an underrated one in my opinion. Even so, it was enough to find this kind of unique vulnerability when I first started bug hunting which was exactly 3 years ago.

Last Words

Especially for bug bounty world, instead of checking just generic well known vulnerability types such as XSS, CSRF or SQLi’s, searching this kind of logical misconfigurations on the systems may enrich your attack vector database. While on the short-term it could be seen as waste of time, on the long-term it could return both as payouts and excitements of new discoveries.
