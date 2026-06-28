---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-10-10_open-redirect-scanner-with-ubercom.md
original_filename: 2016-10-10_open-redirect-scanner-with-ubercom.md
title: Open Redirect Scanner with Uber.com
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 2cfd7c2269686cf1f51b73656c1a25315ab94830913b94b5d9e180a7ef6b9076
text_sha256: 91b698ac17300b73f97193a03f7e9a388129d5fcb465f2c2995c36df2204161c
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Open Redirect Scanner with Uber.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-10-10_open-redirect-scanner-with-ubercom.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `2cfd7c2269686cf1f51b73656c1a25315ab94830913b94b5d9e180a7ef6b9076`
- Text SHA256: `91b698ac17300b73f97193a03f7e9a388129d5fcb465f2c2995c36df2204161c`


## Content

---
title: "Open Redirect Scanner with Uber.com"
url: "https://medium.com/bugbountywriteup/open-redirect-scanner-c72cd60d0bf"
authors: ["Ak1T4 (@akita_zen)"]
programs: ["Uber"]
bugs: ["Open redirect"]
publication_date: "2016-10-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6251
scraped_via: "browseros"
---

# Open Redirect Scanner with Uber.com

Open Redirect Scanner with Uber.com
Ak1T4
Follow
2 min read
·
Oct 10, 2016

158

3

Searching for dummies redirect :)

WTF is an open redirect scanner?

Unvalidated redirects and forwards are possible when a web application accepts untrusted input that could cause the web application to redirect the request to a URL contained within untrusted input. By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials. Because the server name in the modified link is identical to the original site, phishing attempts may have a more trustworthy appearance. Unvalidated redirect and forward attacks can also be used to maliciously craft a URL that would pass the application’s access control check and then forward the attacker to privileged functions that they would normally not be able to access.

Reference: https://www.owasp.org/index.php/Open_redirect

The scanner:

During a research to uber i needed a tool who scan the trace of the requests for viewing the jumps to final url destination and see if a list of uber domains can force to redirect to other external site. With a few line of codes python was the best solution for this. Why is dangerous an open redirect? because an attacker can send an url and force to redirect the user to a malicious site, execute evil scripts or phishing sensitive data.

Here is an example video with the open redirect scanner tool:

The scanner find an open redirect of uber subdomains and show how is forced to load www.yahoo.com site:

The issue was reported but Uber decides not fixed beacuse not considered a risk for its users

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How is works?

The scanner shows a 303 error code (see others) when the domain is vuln

The attacks:

For example this domain in uber is vuln to open redirect -> https://trip.uber.com/

we can send to a user this evil url with a payload -> https://trip.uber.com//yahoo.com/%2F.. and the user is redirected to the yahoo.com site .. we can ofuscate the url for cheat the user with any encode available

The code:

Here is the python code i write to follow the requests to a final destination and see if the open redirect works. Basically the scanner load a list of subdomains an add a payload to the final url seeing where he goes

Enjoy and Happy Hacking! :)

Regards,

Ak1T4
