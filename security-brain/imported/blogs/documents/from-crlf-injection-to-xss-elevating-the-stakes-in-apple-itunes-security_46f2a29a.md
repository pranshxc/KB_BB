---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-24_from-crlf-injection-to-xss-elevating-the-stakes-in-apple-itunes-security.md
original_filename: 2024-02-24_from-crlf-injection-to-xss-elevating-the-stakes-in-apple-itunes-security.md
title: 'From CRLF Injection to XSS: Elevating the Stakes in Apple iTunes Security'
category: documents
detected_topics:
- xss
- cors
- command-injection
- path-traversal
- automation-abuse
- supply-chain
tags:
- imported
- documents
- xss
- cors
- command-injection
- path-traversal
- automation-abuse
- supply-chain
language: en
raw_sha256: 46f2a29af21f3fdf95bdc3497ff33f3e43ed985257e47258f991b96838e9f78c
text_sha256: b19713f53c135a8ed751dcae7c083eb77f6b4f01e9b74d89b3c2d60f5744dc9a
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# From CRLF Injection to XSS: Elevating the Stakes in Apple iTunes Security

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-24_from-crlf-injection-to-xss-elevating-the-stakes-in-apple-itunes-security.md
- Source Type: markdown
- Detected Topics: xss, cors, command-injection, path-traversal, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `46f2a29af21f3fdf95bdc3497ff33f3e43ed985257e47258f991b96838e9f78c`
- Text SHA256: `b19713f53c135a8ed751dcae7c083eb77f6b4f01e9b74d89b3c2d60f5744dc9a`


## Content

---
title: "From CRLF Injection to XSS: Elevating the Stakes in Apple iTunes Security"
url: "https://xelkomy.medium.com/from-crlf-injection-to-xss-elevating-the-stakes-in-apple-itunes-security-597dc435fd82"
authors: ["Khaled Mohamed (@0xElkomy)"]
programs: ["Apple (iTunes)"]
bugs: ["CRLF injection", "XSS"]
publication_date: "2024-02-24"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 409
scraped_via: "browseros"
---

# From CRLF Injection to XSS: Elevating the Stakes in Apple iTunes Security

From CRLF Injection to XSS: Elevating the Stakes in Apple iTunes Security
Khaled Mohamed
Follow
3 min read
·
Feb 23, 2024

406

4

Press enter or click to view image in full size
Description

بسم الله الرحمن الرحيم

Get Khaled Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Approximately eighteen months ago, I discovered a significant vulnerability within Apple iTunes, starting with a Carriage Return Line Feed (CRLF) issue. Through persistent effort, this initial finding was escalated to reveal a Cross-Site Scripting (XSS) vulnerability, showcasing the potential for extensive exploitation. Additionally, in the latter stages of investigation, a colleague contributed by identifying a Cross-Origin Resource Sharing (CORS) exploit within the same endpoint where the CRLF was found, further emphasizing the critical nature of the security flaw we uncovered.

Discover Stage

On a Friday, similar to today, I discovered a vulnerability while running my bash script to aggregate subdomains and Wayback Machine URLs for each, subsequently analyzing them with tools like Dalfox and Nuclei. Despite initially finding nothing, my focus shifted to the main Apple domain (apple.com). While monitoring traffic through the Burp Suite proxy, I stumbled upon a subdomain utilized as an API by the main domain for fetching iTunes offer data. This discovery was prompted by examining the source code of the main domain, where I noticed this subdomain accepted certain parameters.

Exploitation

I identified a subdomain within the iTunes.apple.com domain, referenced in the main website’s source code. This subdomain, which took specific parameters, was my focus. Using Burp Suite’s repeater tool, I began testing for vulnerabilities like XSS and LFI through fuzzing. A breakthrough was achieved when injecting %0d%0aSet-Cookie:%20attacker=exploit led to the successful reflection of the attacker=exploit cookie in the response page, indicating a potential security exploit.

Press enter or click to view image in full size
The Response from the apple subdomain with the cookie was reflected

Despite discovering a CRLF vulnerability, I encountered a challenge as the response was in JSON content-type, a scenario I’ve faced before where the reflection in JSON rendered the exploit less impactful. However, after some research and experimentation, I found that manually adjusting the content-type in the request successfully bypassed this limitation, marking a significant breakthrough in my exploration. This adjustment allowed the exploit to be reflected outside the JSON response, enhancing its potential impact.

Press enter or click to view image in full size
The Response from the apple subdomain with the Content-type was reflected

Ultimately, after successfully manipulating the content-type, I managed to intercept and reflect cookies back to myself. Furthermore, with the CORS vulnerability that my colleague Zyead identified on the same endpoint, we were able to capture cookies via a third-party domain, demonstrating a significant security flaw that could potentially be exploited by unauthorized entities to gain access to sensitive information.

As we conclude this brief exploration, I hope you’ve found the insights shared both enlightening and useful. Should you have any questions or wish to engage further on this topic, don’t hesitate to reach out to me on Twitter. Your feedback and inquiries are always welcome!

My Twitter (X)

Don’t Miss Our Company Cyber AR:
CyberAR | Penetration testing | Cyber Security
