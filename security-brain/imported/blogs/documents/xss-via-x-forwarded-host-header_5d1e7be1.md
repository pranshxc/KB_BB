---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-30_xss-via-x-forwarded-host-header.md
original_filename: 2022-01-30_xss-via-x-forwarded-host-header.md
title: XSS via X-Forwarded-Host header
category: documents
detected_topics:
- xss
- command-injection
- otp
tags:
- imported
- documents
- xss
- command-injection
- otp
language: en
raw_sha256: 5d1e7be1af696ae077a72941393d4665d50e751d05285d70cb34ee0a38fdb205
text_sha256: a13e8139938bae425ffacf6be14e5540da32b260b8aa71c7dac534a491f7318c
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# XSS via X-Forwarded-Host header

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-30_xss-via-x-forwarded-host-header.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `5d1e7be1af696ae077a72941393d4665d50e751d05285d70cb34ee0a38fdb205`
- Text SHA256: `a13e8139938bae425ffacf6be14e5540da32b260b8aa71c7dac534a491f7318c`


## Content

---
title: "XSS via X-Forwarded-Host header"
url: "https://medium.com/@abhijeetbiswas_/xss-cross-site-scripting-via-x-forwarded-host-header-20be114d4254"
authors: ["Abhijeet Biswas (@abhijeetbiswas_)"]
programs: ["Omise"]
bugs: ["XSS", "Host header injection"]
bounty: "200"
publication_date: "2022-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2964
scraped_via: "browseros"
---

# XSS via X-Forwarded-Host header

XSS via X-Forwarded-Host header
Abhijeet Biswas
Follow
3 min read
·
Jan 30, 2022

185

3

whoami

I am Abhijeet Biswas, a Security Researcher. I have been studying, practicing, and learning about Web Application Security Vulnerabilities and Bug Bounties.

This is my first blog.

Let’s first understand, what is XSS?

Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application. Cross-site scripting vulnerabilities normally allow an attacker to masquerade as a victim user, to carry out any actions that the user is able to perform, and to access any of the user’s data. If the victim user has privileged access within the application, then the attacker might be able to gain full control over all of the application’s functionality and data.

Press enter or click to view image in full size
How does XSS work?

Cross-site scripting works by manipulating a vulnerable website’s source code/storage system so that it returns malicious JavaScript to users. When the malicious code executes inside a victim’s browser, the attacker can fully compromise their interaction with the application by stealing session cookies, user credentials, tokens, secrets, etc.

XSS Payloads :

<script>alert(“Hacked_by_Oblivion”)</script>

<img src/onerror=prompt(document.cookie)>

Let’s understand, what is the X-Forwarded-Host header?

The HTTP X-Forwarded-Host header is a request-type header de-facto standard header. This header is used to identify the original request made by the client. Because the hostnames and the ports differ in the reverse proxies at that time this header took the lead and identify the original request. This header can also be used for debugging, creating location-based content. So this header kept the privacy of the client. The root version of this header is HTTP Forwarded.

LET’S ATTACK!!

So I went to the webpage https://www.omise.co/ , captured the request in Intercept and sent the request to Repeater, and added

Get Abhijeet Biswas’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

X-Forwarded-Host: bing.com

and checked whether the bing.com is reflected anywhere in the response or not.

Press enter or click to view image in full size

As you can see in the above image, it was refecting on the sign-in button. So I decided to add an XSS payload after X-Forwarded-Host: bing.com

After adding XSS payload:

X-Forwarded-Host: bing.com”><img src/onerror=prompt(document.cookie)>

I checked wheater it was still reflecting or not?

Press enter or click to view image in full size

As you can see in the above image XSS payload was refecting on the sign-in button.

When I sent this request to the browser, BOOM!! The JavaScript alert box displayed some cookie information as shown in the image given below.

Press enter or click to view image in full size
Impact :

This flaw allows attackers to pass rogue JavaScript to unsuspecting users. The user’s browser has no way to know the script should not be trusted, so it will execute the script, and because the browser thinks the script came from a trusted source, i.e. your website, a malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with your site. These scripts can even rewrite the content of the HTML page.

Report Link: https://hackerone.com/reports/1392935
