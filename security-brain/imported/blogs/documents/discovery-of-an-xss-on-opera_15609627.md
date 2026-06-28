---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-10_discovery-of-an-xss-on-opera.md
original_filename: 2023-05-10_discovery-of-an-xss-on-opera.md
title: Discovery of an XSS on Opera
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 156096272628d96c741848a4e535efeeb207f7cf56d8751355f6b5e2038ad21d
text_sha256: 29dcddd5b0c0e05e69c91aa3809809eff95b30971ec091d8a7b5e0e67a887180
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Discovery of an XSS on Opera

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-10_discovery-of-an-xss-on-opera.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `156096272628d96c741848a4e535efeeb207f7cf56d8751355f6b5e2038ad21d`
- Text SHA256: `29dcddd5b0c0e05e69c91aa3809809eff95b30971ec091d8a7b5e0e67a887180`


## Content

---
title: "Discovery of an XSS on Opera"
url: "https://infosecwriteups.com/discovery-of-an-xss-on-opera-f029f6522ec5"
authors: ["Arman (@M7arm4n)"]
programs: ["Opera"]
bugs: ["XSS"]
publication_date: "2023-05-10"
added_date: "2023-05-11"
source: "pentester.land/writeups.json"
original_index: 1172
scraped_via: "browseros"
---

# Discovery of an XSS on Opera

Discovery of an XSS on Opera
M7arm4n
Follow
2 min read
·
May 10, 2023

132

1

Discovering XSS in large companies is one of my hobbies. Today I want to talk about Opera XSS which took 15 minutes. The power of finding XSS so fast is searching out-of-the-box endpoints. To do this, you first need to find a list of all subdomains, even the ones that don’t give you results (404, 403, etc.). And then find all old existing or recently added endpoints.

Choosing the domain I’m going to work on is usually graded based on what’s found on it. For example, if two XSS vulnerabilities are found in a domain, I look for the third one because a programmer may repeat the same mistake in different places.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I usually use the C99 site to quickly find subdomains

But unfortunately, this time the results that were listed for me were very few and I doubted their completeness. that’s why I decided to brute force subdomains with Knock.

Press enter or click to view image in full size
Press enter or click to view image in full size

And here we found 4 more subdomains which brings us to the vulnerability. I didn’t care about the rest of the subdomains anymore and started looking at those four subdomains. First I started collecting all the old endpoints with katana and archive.

cat subs.txt | waybackurls > path.txt; cat subs.txt | katana >> path.txt ; cat path.txt | uro > path.txt2 ; cat path.txt2 | httpx -sc 

Unfortunately or fortunately, I didn’t get any results this time, which means the results are all fresh and new. I started recon manually and opened one of the subdomains and it led me to such a path:

https://game.target.tld/staticgames/wordsearch?url=https://site.tld/pmm/wordsearch

I changed the URL’s parameter value to XSS payload:

javascript:alert(origin)

and Bingo, the alert fired for me 😎🥂. Easy Payload = Good Recon

Thank you for following me here, Don’t forget to follow me for more write-ups.

Twitter 🐦

AI-Powered Cyber Threat Detection and Response: SIEM and Compliance solution powered by AI, real-time correlation, and threat intelligence. Built for simplicity, reduced noise and affordability. Learn More
