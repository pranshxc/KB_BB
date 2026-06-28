---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-29_how-i-bypassed-reflected-xss-in-well-known-platform.md
original_filename: 2022-08-29_how-i-bypassed-reflected-xss-in-well-known-platform.md
title: How I bypassed Reflected XSS in well-known platform
category: documents
detected_topics:
- xss
- sso
- idor
- command-injection
- rate-limit
- csrf
tags:
- imported
- documents
- xss
- sso
- idor
- command-injection
- rate-limit
- csrf
language: en
raw_sha256: 0f9ad880e9d7ae42b0bcf7225602e8838c183b8c9f97b04bc9f59bd6b6a6bdb2
text_sha256: 982e76c0762286d8e3bc55d1a9075c0f376b35577b112e85694cd4ef91f57552
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed Reflected XSS in well-known platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-29_how-i-bypassed-reflected-xss-in-well-known-platform.md
- Source Type: markdown
- Detected Topics: xss, sso, idor, command-injection, rate-limit, csrf
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `0f9ad880e9d7ae42b0bcf7225602e8838c183b8c9f97b04bc9f59bd6b6a6bdb2`
- Text SHA256: `982e76c0762286d8e3bc55d1a9075c0f376b35577b112e85694cd4ef91f57552`


## Content

---
title: "How I bypassed Reflected XSS in well-known platform"
url: "https://moustadif.medium.com/how-i-bypassed-reflected-xss-in-well-known-platform-274c07f97674"
authors: ["Iori Yagami"]
bugs: ["XSS"]
publication_date: "2022-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2248
scraped_via: "browseros"
---

# How I bypassed Reflected XSS in well-known platform

Iori Yagami
 highlighted

How I bypassed Reflected XSS in well-known platform
Iori Yagami
Follow
3 min read
·
Aug 29, 2022

136

3

What is a XSS attack

Cross-site scripting (XSS) is a web application vulnerability that permits an attacker to inject code, (typically HTML or JavaScript), into the contents of an outside website. When a victim views an infected page on the website, the injected code executes in the victim’s browser. Consequently, the attacker has bypassed the browser’s same origin policy and is able to steal private information from a victim associated with the website

What is a reflected XSS attack

Reflected XSS attacks, also known as non-persistent attacks, occur when a malicious script is reflected off of a web application to the victim’s browser.

The script is activated through a link, which sends a request to a website with a vulnerability that enables execution of malicious scripts. The vulnerability is typically a result of incoming requests not being sufficiently sanitized, which allows for the manipulation of a web application’s functions and the activation of malicious scripts.

To distribute the malicious link, a perpetrator typically embeds it into an email or third party website (e.g., in a comment section or in social media). The link is embedded inside an anchor text that provokes the user to click on it, which initiates the XSS request to an exploited website, reflecting the attack back to the user.

Enumeration

I did’nt invest a lot in enumeration and discovering due to a bug exist in the main domain www.redacted.com

by doing google dork i found a path with param: redirect?t=

site:www.redacted.com inurl:redirect

Get Iori Yagami’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tested it for open redirection but it didn’t work and suddenly I cheked the source code and i observed that my code was there inside a <script> </script> tag

Exploitation of r-XSS vulnerability

Reflected XSS bugs can be exploited to steal cookies, capture passwords and perform CSRF …

I injected my first code : </script> alert(‘1’) <script></script> trying to close the script and open a malicious script but there was a filter in place that broke all my script and tags <script>, <img> …

It took me about 2 days to figure out the right payload to bypass the filter :

</</script>script> <</svg>svg/onload=alert`xss`>//

Press enter or click to view image in full size
xss payload to bypass

and the final URL / POC was like:

https://www.redacted.com/iammore/redirect?t=%3C/%3C/script%3Escript%3E%20%3C%3C/svg%3Esvg/onload=alertxss%3E//

AND BOOM!! Reflected XSS!!

Press enter or click to view image in full size
xss poopup

I send this repport to the team, And in about 1 week, this vulnerability was fixed and rewarded me.

Never Give up

https://www.linkedin.com/in/jawad-moustadif/
