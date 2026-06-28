---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-07_stored-xss-on-product-description-high-400.md
original_filename: 2021-01-07_stored-xss-on-product-description-high-400.md
title: Stored XSS on Product Description [HIGH] — $400
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: f1d377805c522966e93ce3de5d14376d909c15f40b95e6b3c4d07731694abd71
text_sha256: 82787907ad52ba60eb3552252c4f4552a516a0ec3abac61102caeab0fcd85f6c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Product Description [HIGH] — $400

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-07_stored-xss-on-product-description-high-400.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `f1d377805c522966e93ce3de5d14376d909c15f40b95e6b3c4d07731694abd71`
- Text SHA256: `82787907ad52ba60eb3552252c4f4552a516a0ec3abac61102caeab0fcd85f6c`


## Content

---
title: "Stored XSS on Product Description [HIGH] — $400"
url: "https://emanuel-beni.medium.com/stored-xss-on-product-description-high-400-2f078fd70fd2"
authors: ["Emanuel Beni Harijanto"]
bugs: ["Stored XSS"]
bounty: "400"
publication_date: "2021-01-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4022
scraped_via: "browseros"
---

# Stored XSS on Product Description [HIGH] — $400

Stored XSS on Product Description [HIGH] — $400
Emanuel Beni Harijanto
Follow
3 min read
·
Jan 7, 2021

124

2

Disclaimer: I do not have permission to disclose the report, therefore I needed to heavily redact this writeup. Thank you and happy reading!

Press enter or click to view image in full size
Photo by Benny Samuel on Unsplash

Stored cross-site scripting is a vulnerability where an application would store untrusted malicious code from users. The combination of being lethal whilst having a low attack complexity has placed XSS at number 7 of OWASP Top 10. In this writeup, I will be explaining to y’all readers how I was able to find a Stored XSS on one of the biggest E-commerce sites in Asia.

As we all know, most e-commerce websites allow sellers to add their own product descriptions on their product pages. Since this is one of the attack vector for Stored XSS, I decided to input the following XSS payloads for shallow testing;

“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)// — Polyglot Payload
‘“>><marquee><img src=x onerror=confirm(1)></marquee>”></plaintext\></|\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>’ →”></script><script>alert(1)</script>”><img/id=”confirm&lpar;1)”/alt=”/”src=”/”onerror=eval(id&%23x29;>’”><img src=”http://i.imgur.com/P8mL8.jpg"> — Polyglot Payload
%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e — URL Encoded
‘“><a href=’www.anything.com’>Click Here</a> — HTML Injection Check

I would normally rely on the above XSS payloads to check for possible reflection since it is basically impossible to check using all of the payload available out there. After inputting the payloads, I would then check for HTML injection first, meaning executed HTML tags. If the web application executes HTML tags, there is a good chance that it can be leveraged to an XSS. In this case, I was fortunate enough that the web application is executing some of my HTML tags. Sadly, it is not executing my script tags.

Get Emanuel Beni Harijanto’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After a couple of hours tempering the endpoint with XSS payloads, I reached the following conclusion:

The web application is implementing WAF (Web Application Firewall)
WAF is stripping sensitive keywords such as; ‘javascript’ and ‘alert’
The product description uses Markdown to parse the user’s input

For those of you who don’t know what Markdown is, it is a lightweight markup language that you can use to add formatting elements to plaintext text documents. Since Markdown offers high customizability for users, misconfiguration often happens. I decided to spend the next hour searching for possible payloads that would allow me to bypass the above conditions. After reading multiple blog posts, I found out that one of the most common bypasses is using Unicode encoding, therefore I tried to input the following payload:

<a href=j&#97v&#97script:&#97lert(document.cookie)>ClickMe</a>

XSS and HTML Injection is Successful

Fortunately, the web application decodes the Unicode to plaintext and execute the payload when the anchor tag is clicked. Due to the impact and placement of the bug, I submitted this issue as a high severity issue. Thankfully, the security team agrees and rewarded me with a total of $400 after 2 months of waiting.

Press enter or click to view image in full size
Clicking the anchor tag would prompt the document.cookie

Drop a clap and comment if you want me to do another write-up. Thank you for your time and have a nice day!
