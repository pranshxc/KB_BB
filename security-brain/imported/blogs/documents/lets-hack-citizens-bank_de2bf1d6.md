---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-03_lets-hack-citizens-bank.md
original_filename: 2023-04-03_lets-hack-citizens-bank.md
title: Let’s Hack Citizens Bank
category: documents
detected_topics:
- sso
- idor
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- sso
- idor
- xss
- command-injection
- rate-limit
language: en
raw_sha256: de2bf1d60692b264f4fd13380cee18caf1acebfd562e47d592b499430269a490
text_sha256: dc19e48f1fabc8658355a47cd89d87631e48815c1df3fce9422d5afd1e83e1ab
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Let’s Hack Citizens Bank

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-03_lets-hack-citizens-bank.md
- Source Type: markdown
- Detected Topics: sso, idor, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `de2bf1d60692b264f4fd13380cee18caf1acebfd562e47d592b499430269a490`
- Text SHA256: `dc19e48f1fabc8658355a47cd89d87631e48815c1df3fce9422d5afd1e83e1ab`


## Content

---
title: "Let’s Hack Citizens Bank"
url: "https://infosecwriteups.com/lets-hacking-citizens-bank-9520e9c05cf9"
authors: ["Arman (@M7arm4n)"]
programs: ["Citizens Bank"]
bugs: ["XSS"]
publication_date: "2023-04-03"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1310
scraped_via: "browseros"
---

# Let’s Hack Citizens Bank

Let’s Hack Citizens Bank
M7arm4n
Follow
4 min read
·
Apr 3, 2023

160

3

Hello team, Here again, to review another of my findings but this time on the Citizens Bank, an American bank headquartered in Providence, Rhode Island, which operates in Connecticut, Delaware, etc.

Here is the Citizens Bank Responsible Disclosure Program

Same as ever we start our job with subdomains enumeration. I have two different tools for recon on an asset, One of them is working deep and one of them working fast. when I just want to list subdomains and organize the popular technologies and etc, I fired the fast one which runs multi public and private tools to only gather sources from the public and run server discovery on them by httpx.

I got around 150 results and by filtering technology, most of them were ASP.NET, and by filtering status, most of them were 200 or 40x. So I randomly opened some 40x statuses which httpx detected ASP.NET technology on them.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I always recommend my friends set up a separate browser only for hunting, We have thousands of extensions that help bug hunters discover vulnerabilities or reach sources faster. Here are some useful extensions.

The Shodan plugin tells you where the website is hosted (country, city), who owns the IP, and what other services/ ports are open. The Shodan plugin for Chrome automatically checks whether Shodan has any information for the current website. Is the website also running FTP, DNS, SSH, or some unusual service? With this plugin, you can see all the info that Shodan has collected on a given website/ domain.
HackTools is a web extension facilitating your web application penetration tests, it includes cheat sheets as well as all the tools used during a test such as XSS payloads, Reverse shells, and much more.
Wappalyzer is more than a CMS detector or framework detector: it uncovers more than a thousand technologies in dozens of categories such as programming languages, analytics, marketing tools, payment processors, CRM, CDN, and others.
Welcome to the Official Internet Archive Wayback Machine Browser Extension! Go back in time to see how a website has changed through the history of the Web. Save websites, view missing 404 Not Found pages, or read archived books & papers.
This tool takes a list of web pages in plain-text format and opens them all in new tabs. Paste the list into the text area (one website address per line), select your options, and click “Open URLs”.

So after that, I faced something special on one of the 404 subdomains, the subdomain has some records on the Wayback Machine, I opened some of them and tried to google dork to reach some endpoints. I finally found and feedback page. I start fuzzing parameters to find some reflective parameters after a while found 2 parameters, one of them reflected in the JS Context, and the other reflected in an input value tag.

The input of xss%22 was xss&qout; (encoded payload as HTML), So I tried URLencoed the whole payload, and the output reflected without any HTML encoding. I injected the following payload and boom the payload fired:

'-alert(origin)-' -> %27%2d%61%6c%65%72%74%28%6f%72%69%67%69%6e%29%2d%27

Thank you for following me here, Don’t forget to follow me for more write-ups.

Twitter 🐦
