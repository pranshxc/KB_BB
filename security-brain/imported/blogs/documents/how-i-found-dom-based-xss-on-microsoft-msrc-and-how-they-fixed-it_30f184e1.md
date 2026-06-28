---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-23_how-i-found-dom-based-xss-on-microsoft-msrc-and-how-they-fixed-it.md
original_filename: 2023-02-23_how-i-found-dom-based-xss-on-microsoft-msrc-and-how-they-fixed-it.md
title: How I found DOM-Based XSS on Microsoft MSRC and How they fixed it
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- supply-chain
language: en
raw_sha256: 30f184e18f90fc2087fc1a89caa9ab12b70dbc991c99ee834b46e8b958e1bcd6
text_sha256: 7b1be36853dbc6e20105a4abf2702986d760f3d0ce872c19bb4ac8bdb8a646c8
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# How I found DOM-Based XSS on Microsoft MSRC and How they fixed it

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-23_how-i-found-dom-based-xss-on-microsoft-msrc-and-how-they-fixed-it.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `30f184e18f90fc2087fc1a89caa9ab12b70dbc991c99ee834b46e8b958e1bcd6`
- Text SHA256: `7b1be36853dbc6e20105a4abf2702986d760f3d0ce872c19bb4ac8bdb8a646c8`


## Content

---
title: "How I found DOM-Based XSS on Microsoft MSRC and How they fixed it"
url: "https://m3ez.medium.com/how-i-found-dom-based-xss-on-microsoft-msrc-and-how-they-fixed-it-8b71a6020c82"
authors: ["Supakiad S. (@Supakiad_Mee)"]
programs: ["Microsoft"]
bugs: ["DOM XSS"]
publication_date: "2023-02-23"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1483
scraped_via: "browseros"
---

# How I found DOM-Based XSS on Microsoft MSRC and How they fixed it

Top highlight

Supakiad S. (m3ez)
 highlighted

How I found DOM-Based XSS on Microsoft MSRC and How they fixed it
Supakiad S. (m3ez)
Follow
5 min read
·
Feb 23, 2023

163

2

Microsoft MSRC ฺBlog site: Dom-based XSS Vulnerability

Table of Contents
Introduction
Background of DOM-Based XSS
Finding and Analyzing the Vulnerable Code
Reporting the Vulnerability to Microsoft
How MSRC Team Fixing the Vulnerability
Disclosure Timelines
Introduction

In this blog post, I am excited to share my experience of discovering a DOM-Based XSS vulnerability on the Microsoft Security Response Center (MSRC) website, and how the Microsoft Security Team quickly and efficiently resolved the issue by fixing the vulnerability.

Background of DOM-Based XSS

DOM-based XSS vulnerabilities usually arise when JavaScript takes data from an attacker-controllable source, such as the URL, and passes it to a sink that supports dynamic code execution, such as eval() or innerHTML (in this case). This enables attackers to execute malicious JavaScript, which typically allows them to hijack other users' accounts.

For more information, please refer to:

DOM Based XSS | OWASP Foundation
What is DOM-based XSS (cross-site scripting)? Tutorial & Examples | Web Security Academy (portswigger.net)
Finding and Analyzing the Vulnerable Code

On February 12th, 2023, I read on the MSRC blog that they had released a new MSRC Blog Site, which started on February 9th, 2023.

Press enter or click to view image in full size
New MSRC Blog Site | MSRC Blog | Microsoft Security Response Center

The aforementioned blog post announced that the MSRC Blog Site had been refreshed with a new look and improved site performance, search functionality, categories, and tags. That indicates new development functions have been added to the site.

Here is a step-by-step guide that outlines how I found and analyzed the vulnerable code and determined the root cause of the issue.

Get Supakiad S. (m3ez)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I started by using the search function and looking at the website’s HTML source code. I discovered that the search.js file was being loaded and the search query was being added to the URL as a query parameter.

Press enter or click to view image in full size
https://msrc.microsoft.com/blog/search/?query=m3ez

Then, I started analyzing the search.js file to find the root cause of the vulnerability.

At line 2296, the application checks whether a value exists in both the inputBox and searchResults before processing user input.
Press enter or click to view image in full size
search.js: 2296–2305
At line 2297, the application calls the param function to retrieve the value of the query parameter and stores it in the searchQuery parameter.
Press enter or click to view image in full size
search.js: 2389–2393
At line 2300, the application passes the searchQuery parameter to the executeSearch function.
Press enter or click to view image in full size
search.js: 2296–2305
In the executeSearch function, the application calls param function again and parses it into searchQueryTitle.innerHTML.
Press enter or click to view image in full size
search.js: 2306–2329
Conclusion

As shown in the previous steps, the code retrieves user input from the param function and directly set it as the innerHTML of a DOM element without proper input sanitation, allowing potential attackers to inject and execute malicious scripts in the victim’s browser.

For example
Press enter or click to view image in full size
https://msrc.microsoft.com/blog/search/?query=<img/src/onerror=alert(`m3ez`)>
Reporting the Vulnerability to Microsoft

To report the vulnerability, I followed the steps outlined on the Microsoft Security Response Center website

FAQs — Report an issue and submission guidelines (microsoft.com)

I provided them with a detailed report outlining the vulnerability and a proof of concept (PoC) that demonstrated the attack. You can find more information about how to report a vulnerability to Microsoft on my blog

Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022) | by Supakiad S. (m3ez)
Summary of Vulnerability

The vulnerability was found in the Microsoft MSRC Blog, specifically in the search functionality at https://msrc.microsoft.com/blog/search/. The vulnerability was caused by the unsanitized user input received from the “query” parameter, which is used to set the innerHTML of a DOM element in the search results. This made it for an attacker to inject malicious scripts and execute them in the victim’s browser, leading to a Dom-based XSS attack.

Vulnerable product: Microsoft MSRC Blog version: 1.1.02231.103–9e425f97

Vulnerable URL: https://msrc.microsoft.com/blog/search/

Vulnerable JavaScript: https://msrc.microsoft.com/blog/js/search.js

Vulnerable Function: param

Vulnerable Parameter: query

Testing Payload: <img/src/onerror=alert(1)>

Example PoC URL: https://msrc.microsoft.com/blog/search/?query=<img/src/onerror=alert(1)>

Proof of Concept (PoC)

I record a below VDO PoC to demonstrate the existence of a DOM-Based XSS vulnerability on the MSRC Blog Site.

Microsoft MSRC Blog: How I Discovered a Dom-based XSS Vulnerability — YouTube
How MSRC Team Fixing the Vulnerability

After discovering the vulnerability, I reported it to the MSRC team. They acknowledged the report and began investigating and fixing the issue.

The MSRC team implemented getSearchParamClean to replace the vulnerable param function.

Press enter or click to view image in full size
MSRC team implement getSearchParamClean to replace the vulnerable param function

The new function uses a Dompurify library to properly sanitize user input before using it to set the innerHTML of a DOM element. This would prevent any potential XSS attacks by removing any malicious scripts from user input before it is displayed on the page.

Press enter or click to view image in full size
getSearchParamClean function
Verify fixed vulnerability
Press enter or click to view image in full size
Before

Attempting to inject the XSS payload into the search query parameter should result in the payload being sanitized and not executed.

Press enter or click to view image in full size
After
Press enter or click to view image in full size
Disclosure Timelines

Here are the timelines for the vulnerability disclosure:

Feb 12, 2023 — Vulnerability Discovered and Reported through MSRC portal.
Feb 14, 2023 — MSRC ticket was moved to Review/Repro.
Feb 15, 2023 — MSRC rolled out a patch to fix the vulnerability.
Feb 23, 2023 — Public release of the security advisory.

I appreciate your feedback and would love to hear your thoughts on my blog. If you have any comments or suggestions, please feel free to reach out to me on:

LinkedIn: Supakiad S.

Twitter: (@Supakiad_Mee)

Thanks for your support!
