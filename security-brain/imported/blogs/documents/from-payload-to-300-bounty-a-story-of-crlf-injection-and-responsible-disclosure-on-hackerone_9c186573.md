---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-16_from-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-.md
original_filename: 2023-04-16_from-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-.md
title: 'From payload to 300$ bounty: A story of CRLF injection and responsible disclosure
  on HackerOne'
category: documents
detected_topics:
- sso
- xss
- command-injection
- path-traversal
- supply-chain
tags:
- imported
- documents
- sso
- xss
- command-injection
- path-traversal
- supply-chain
language: en
raw_sha256: 9c18657347ad0c1ffdc09c2f79e2a5d9b163eb641bc9ab0199edb91e37f4f85b
text_sha256: 3793646048e5600e27d8c5156bf6c3bb05851321ed3d93e8fba1a943af69cfc0
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-16_from-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, path-traversal, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `9c18657347ad0c1ffdc09c2f79e2a5d9b163eb641bc9ab0199edb91e37f4f85b`
- Text SHA256: `3793646048e5600e27d8c5156bf6c3bb05851321ed3d93e8fba1a943af69cfc0`


## Content

---
title: "From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne"
url: "https://infosecwriteups.com/from-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-on-hackerone-eeff74aff422"
authors: ["Karthikeyan.V (@karthithehacker)"]
bugs: ["CRLF injection"]
bounty: "300"
publication_date: "2023-04-16"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1263
scraped_via: "browseros"
---

# From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne

From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne
Karthikeyan.V
Follow
3 min read
·
Apr 16, 2023

162

2

Press enter or click to view image in full size

As a bug bounty hunter, I’m always on the lookout for security vulnerabilities that I can report to companies and earn rewards. Recently, I discovered a CRLF injection vulnerability on a popular website through the HackerOne platform, and in this blog post, I’m going to share how I found it and the impact it had.

First, let me explain what CRLF injection is. CRLF stands for “Carriage Return Line Feed”, which are special characters used to represent the end of a line in various protocols, including HTTP. An attacker can inject CRLF characters into an HTTP header, which can lead to various attacks, such as HTTP response splitting, cross-site scripting, and cookie manipulation.

During my bug bounty testing, I used my crlfi tool, I created this tool for the purpose of detect the CRLF injection Bug. You can install it on your machine by running the following command: “npm install crlfi -g”. It is supported on Windows, Mac, and Linux operating systems. To learn more about how to use it, please visit my Github repository “https://github.com/karthi-the-hacker/crlfi”.

After a few minutes of scanning, I was able to obtain a vulnerable output with the payload.

I noticed that the location header value was not properly sanitized, and I was able to inject CRLF characters into it using a simple payload like “%0d%0a” Example http://example.com/%0D%0ATest-Header:karthithehacker .

This allowed me to manipulate the server’s response and inject arbitrary content into it, such as fake headers or even JavaScript code.

To demonstrate the impact of the vulnerability, I created a proof of concept that injected a fake “Set-Cookie” header into the server’s response, which could be used to steal session cookies and perform session hijacking attacks. I reported the vulnerability to the company through the HackerOne platform, and they confirmed it and rewarded me with a bounty.

Technical Content : https://karthithehacker.com/blogs/crlf-in-h1-poc.html

Press enter or click to view image in full size

The lesson here is that even seemingly harmless headers can be vulnerable to CRLF injection, and it’s important to properly sanitize user input before using it in HTTP headers. As a bug bounty hunter, it’s also important to keep an eye out for these types of vulnerabilities, as they can have a significant impact on the security of a web application.

Tips:- Downgrade the HTTPS to HTTP and inject CRLF payloads

POC Video :

In conclusion, CRLF injection is a powerful technique that attackers can use to manipulate HTTP headers and perform various attacks. By understanding how it works and how to prevent it, we can help make the web a safer place for everyone.

Get Karthikeyan.V’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Connect with me:

Twitter: https://twitter.com/karthithehacker

Instagram: https://www.instagram.com/karthithehacker/

LinkedIn: https://www.linkedin.com/in/karthikeyan--v/

Website: https://www.karthithehacker.com/

Github : https://github.com/karthi-the-hacker/

npmjs: https://www.npmjs.com/~karthithehacker

Youtube: https://www.youtube.com/karthithehacker

Thank you

Karthikeyan.V
