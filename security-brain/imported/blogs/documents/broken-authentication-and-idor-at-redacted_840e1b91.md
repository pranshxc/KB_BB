---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-21_broken-authentication-and-idor-at-redacted.md
original_filename: 2022-03-21_broken-authentication-and-idor-at-redacted.md
title: ($$$) Broken Authentication and IDOR at [REDACTED]
category: documents
detected_topics:
- idor
- xss
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 840e1b91637c8b3662b6d9c3f852ca9617652fd4b842afda4d60199ff5d0ecd2
text_sha256: 8d81019232cfb5c46cb07131c63f80b057f0fd4ee4cf1d4e06ae86a9aeeab139
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# ($$$) Broken Authentication and IDOR at [REDACTED]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-21_broken-authentication-and-idor-at-redacted.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `840e1b91637c8b3662b6d9c3f852ca9617652fd4b842afda4d60199ff5d0ecd2`
- Text SHA256: `8d81019232cfb5c46cb07131c63f80b057f0fd4ee4cf1d4e06ae86a9aeeab139`


## Content

---
title: "($$$) Broken Authentication and IDOR at [REDACTED]"
url: "https://wahaz.medium.com/broken-authentication-and-idor-at-redacted-646de8d508e6"
authors: ["Rizaldi Wahaz (@wah_haz)"]
bugs: ["IDOR"]
publication_date: "2022-03-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2797
scraped_via: "browseros"
---

# ($$$) Broken Authentication and IDOR at [REDACTED]

($$$) Broken Authentication and IDOR at [REDACTED]
Rizaldi Wahaz
Follow
4 min read
·
Mar 21, 2022

226

1

H
ello InfoSec community hope you guys are good, I want to share my finding in bug bounty about Broken Authentication and Insecure Direct Object Reference (IDOR) at [REDACTED], here we go 🔥

Proof of Concept

First is understanding the program, *.redacted.com is in scope so we can try to find all of the subdomain of the website. We can use tools to enumerate subdomain like Sudomy, Subfinder, Sublist3r, etc.

GitHub - screetsec/Sudomy: Sudomy is a subdomain enumeration tool to collect subdomains and…
Sudomy is a subdomain enumeration tool to collect subdomains and analyzing domains performing automated reconnaissance…

github.com

GitHub - projectdiscovery/subfinder: Subfinder is a subdomain discovery tool that discovers valid…
Subfinder is a subdomain discovery tool that discovers valid subdomains for websites. Designed as a passive framework…

github.com

GitHub - aboul3la/Sublist3r: Fast subdomains enumeration tool for penetration testers
Sublist3r is a python tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and…

github.com

After get the subdomin, I try to open and see one by one of them, then get one of the interesting subdomain that show the login page, I guess the login page was for the admin panel. So I go deeper and try to find something interesting in that subdomain.

GitHub - danielmiessler/SecLists: SecLists is the security tester's companion. It's a collection of…
SecLists is the security tester's companion. It's a collection of multiple types of lists used during security…

github.com

Try to fuzzing with common security wordlist https://admin.redacted.com/FUZZ, we can use fuzzing tools like gobuster, wfuzz, ffuf, etc. Found some wordlist is response with 200 and different length, then I try to open the url, but the page just showing same login page.

Wordlist login
Wordlist newsroom
GitHub - OJ/gobuster: Directory/File, DNS and VHost busting tool written in Go
Directory/File, DNS and VHost busting tool written in Go - GitHub - OJ/gobuster: Directory/File, DNS and VHost busting…

github.com

GitHub - xmendez/wfuzz: Web application fuzzer
Wfuzz has been created to facilitate the task in web applications assessments and it is based on a simple concept: it…

github.com

GitHub - ffuf/ffuf: Fast web fuzzer written in Go
A fast web fuzzer written in Go. ffuf has a channel at Porchetta Industries Discord server alongside of channels for…

github.com

So I try to check the source code with inspect element, surprisingly it’s totally different. There is redirect code in the client side

<script>window.location=”/login”;</script>

There is some option to check the page

Get Rizaldi Wahaz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Disable the javascript in browser
or Save and edit the source code locally
Source code

Comment the redirect code, then open the source code locally. Then voila the admin panel is shown. But ofc the data is can’t load, because the CSP (Content Security Policy).

Press enter or click to view image in full size
Admin panel

After that go deeper to the javascript source code. There is some javascript file included, and found some endpoint that interesting to test. After test some endpoint there is one endpoint vulnerable with IDOR.

https://admin.redacted.com/User/deleteImage

Press enter or click to view image in full size
Javascript source code

Then try to fire the post request in the postman with form data id with value 1, voila the response said

{“success”:true}

The avatar of the admin user is success deleted with that post request. Finally I immediately make the PoC then report to the Bug Bounty program.

Press enter or click to view image in full size
Bounty

Alhamdulillah give thanks to Allah SWT, my tips is go to deeper and try to manual analysis into the source code, look into all javascript files and test all endpoint. Thank you has been read my article ✌️

“Stay Hungry Stay Foolish” — Steve Jobs

Timeline
1 October 2021: Initial Report
4 October 2021: Report Validate by H1 Team
11 November 2021: Bug Fixed and Resolved
7 December 2021: $$$
