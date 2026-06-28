---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-10_content-security-policy-bypass-to-perform-xss-using-mime-sniffing.md
original_filename: 2020-12-10_content-security-policy-bypass-to-perform-xss-using-mime-sniffing.md
title: Content-Security-Policy Bypass to perform XSS using MIME sniffing
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: 6f16a93baaffb43b3d4b5d7c745ee5cfc0713d51e373f500e2d89b150201205f
text_sha256: 2d1b34ef28e4dad35290a789fec4f5ec9bdd5f3d6083ecdac834cf7a1d770eb3
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Content-Security-Policy Bypass to perform XSS using MIME sniffing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-10_content-security-policy-bypass-to-perform-xss-using-mime-sniffing.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `6f16a93baaffb43b3d4b5d7c745ee5cfc0713d51e373f500e2d89b150201205f`
- Text SHA256: `2d1b34ef28e4dad35290a789fec4f5ec9bdd5f3d6083ecdac834cf7a1d770eb3`


## Content

---
title: "Content-Security-Policy Bypass to perform XSS using MIME sniffing"
url: "https://kurtikleiton.medium.com/content-security-policy-bypass-to-perform-xss-3c8dd0d40c2e"
authors: ["Kleiton Kurti (@kleiton0x7e)"]
bugs: ["XSS", "CSP bypass"]
publication_date: "2020-12-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4079
scraped_via: "browseros"
---

# Content-Security-Policy Bypass to perform XSS using MIME sniffing

Top highlight

Content-Security-Policy Bypass to perform XSS using MIME sniffing
kleiton0x7e
Follow
5 min read
·
Dec 9, 2020

626

5

Summary

Recently, I performed a Cross Site Scripting vulnerability, however a normal XSS payload wasn’t being triggered because CSP was blocking external Javascript code (XSS) being executed. By finding another XSS vulnerability in another endpoint (which again is being blocked by CSP), I managed to combine them together leading into CSP bypassing and trigger XSS using MIME sniffing

Finding the first XSS

The following image shows the endpoint located in the index, which it’s parameter value is being reflected to the body of the website.

Instead of giving a string value, let’s try inputting an HTML simple payload. I entered <h1>kleiton0x00</h1> and hopefully the payload will be reflected and displayed as a HTML content.

Press enter or click to view image in full size

Cool, we have HTML Injection, so let’s try to leverage it into XSS. This time I entered the simplest XSS payload ever: <script>alert(1)</script>

If nothing gets filtered or blocked by WAF, we will be able to trigger the Javascript payload.

Press enter or click to view image in full size

Wait?! It got successfully injected into the website, but no alert 1?!?!? Looking at the page source, nothing was being filtered or removed.

Detecting CSP

While taking a look at Developer Tools of the browser (Console), I realised that the script is being blocked by Content-Security-Policy.

Press enter or click to view image in full size

What does this mean? Content Security Policy (CSP) is an added layer of security, specifically a HTTP Header which blocks external codes to be injected into a website. Usually a well-implemented CSP only allows script by internal entities (the domain itself).

First we have to detect how CSP works and from which source it allows the scripts to be loaded inside the website.

Looking at the HTTP Headers, specifically Content-Security-Policy: we can see that CSP has a rule to accept scripts from the website itself and it’s directories and subdomains. Looks like we are very limited as we can’t inject our own malicious Javascript.

Finding another vulnerable endpoint to XSS

Since we can’t bypass it, I decided to look around, trying to find more XSS. I opened the Page Source of the index, and while scrolling I noticed a php code which has an parameter. Interesting!

Without losing time, I immediately went to /js/countdown.php

Get kleiton0x7e’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In the end parameter, I put a simple string value to see how the website behaves.

Press enter or click to view image in full size

We see our string (kleiton0x00) being reflected into the source code. Super! We can start begin injecting our javascript code.

Breaking Javascript string to perform the second XSS

Instead of entering a simple string, let’s try to break the js string. How to do this? Based on the code, our reflected input is being added right after the numbers.

Add ); to close the current Javascript code in the 2nd line. The bracked ) will close the variable value and the ; will close the current javascript code in the 2nd line. Because the code is closed, we can add a new Javascript code, which of course is our malicious code, in our case alert(1);

Unfortunately there is codes left on the same line: *1000).getTime();

How to get rid of those? Easy, simply by commenting. So, at the end of our input, we add //

Our final payload would be:

);alert(1);//

Press enter or click to view image in full size

Great, based on the source code, we have injected successfully a Javascript code to the directory. We got a second XSS!

So the full URL would be: http://website.com/js/countdown.php?end=2534926825);alert(1);//

When going to the given URL, no XSS is being reflected. Why? Because our XSS is being again blocked by CSP.

Bypassing CSP with 2 XSS using MIME Sniffing

It’s time to combine the first XSS we found on index page and the second XSS we found on the countdown.php.

Let’s see how MIME sniffing can result in a XSS vulnerability. For an attacker to perform an XSS attack by leveraging MIME sniffing, there are certain preconditions that must be fulfilled. Note that, the preconditions are both on client side:

The attacker should be able to control content in the server’s response so that malicious JavaScript can be injected (the second XSS which we found)
The attacker should be able to introduce an executable context via HTML injection or Javascript Injection (the first XSS which we found)

Our XSS payload will be based on what we found on the first XSS (<script>alert(1)</script>). Instead of executing a Javascript, we will load the URL of countdown.php which is http://website.com/js/countdown.php?end=2534926825);alert(1);//

So, combining the XSS payload of the first one with the URL of the vulnerable php file, our final payload will be:

<script src=’http://website.com/js/countdown.php?end=2534926825);alert(1);//></script>

Press enter or click to view image in full size
can result in a XSS vulnerability. For an attacker to perform an XSS attack by

We bypassed CSP and successfully executed our alert(1) code using MIME Sniffing.
