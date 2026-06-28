---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-27_my-journey-to-nokia-hall-of-fame-in-just-10-minutes.md
original_filename: 2023-03-27_my-journey-to-nokia-hall-of-fame-in-just-10-minutes.md
title: My Journey to Nokia Hall of Fame in just 10 minutes
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
raw_sha256: c4f996a173c64b40ee3f73ca788f1b2fa6c98f539fdcaf61d080b9ec826b8e42
text_sha256: 368bb1070ec8be9d096f3414f2a88b1260dd9dc4710edc6e218fe095fde748c4
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# My Journey to Nokia Hall of Fame in just 10 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-27_my-journey-to-nokia-hall-of-fame-in-just-10-minutes.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `c4f996a173c64b40ee3f73ca788f1b2fa6c98f539fdcaf61d080b9ec826b8e42`
- Text SHA256: `368bb1070ec8be9d096f3414f2a88b1260dd9dc4710edc6e218fe095fde748c4`


## Content

---
title: "My Journey to Nokia Hall of Fame in just 10 minutes"
url: "https://medium.com/@rajdipdeysarkar7/my-journey-to-nokia-hall-of-fame-in-just-10-minutes-4869c78c37e7"
authors: ["Rajdip"]
programs: ["Nokia"]
bugs: ["DOM XSS", "Open redirect"]
publication_date: "2023-03-27"
added_date: "2023-03-28"
source: "pentester.land/writeups.json"
original_index: 1337
scraped_via: "browseros"
---

# My Journey to Nokia Hall of Fame in just 10 minutes

My Journey to Nokia Hall of Fame in just 10 minutes
Rajdip
Follow
2 min read
·
Mar 27, 2023

148

1

Introduction

Hi, this is Rajdip, and I hope all of you are doing well. As a cybersecurity enthusiast, I am always on the lookout for opportunities to find vulnerabilities and report them to companies. Recently, I came across a LinkedIn post where someone mentioned making it to the Nokia Hall of Fame, and I was determined to make it there too. In just 10 minutes, I was able to find vulnerabilities that earned me a spot-on Nokia’s Honorary Hall of Fame list. In this article, I will share my journey and the steps I took to achieve this milestone.

Initial Recon:

My first step was to enumerate all the subdomains using sublister, subfinder, assetfinder, and knockpy and sort them to find unique sub-domains. With Nokia being a huge target, all subdomains were in scope. Once I had my list of unique domains, I ran nuclei on each one to scan for vulnerabilities.

// enumerate subdomains
subfinder -d domain.txt | httpx -sc --title | tee -a sub1.txt
assetfinder -subs-only -d domain.txt | httpx -sc --title | tee -a sub2.txt\
python3 knockpy.py domain.txt
sublist3r -d domain.txt | httpx -sc --title | tee -a sub4.txt
// sort domains 
cat sub1 sub2 sub3 sub4 | sort -u | tee -a unique.txt
// nuclei
nuclei -l unique.txt -o nuclei_result.txt

After taking a short break, I reviewed the results and was shocked to find that I had found 5 open redirects and 3 dom xss vulnerabilities. I quickly made reports and took POCs of each vulnerability and reported them to Nokia.

Response from Nokia

Within a day, I received a response from Nokia, thanking me for submitting my findings to them. Out of the five open redirect and three DOM XSS vulnerabilities I reported, five open redirects were found to be duplicates, but the three DOM XSS vulnerabilities were triaged. Nokia also informed me that they would address all similar findings and add my name to their Hall of Fame. A few days later, I was thrilled to discover my name on Nokia’s Honorary Hall of Fame list.

Press enter or click to view image in full size
HOF-Nokia
Final thought

Reconnaissance is key! While using scanners can be helpful, luck often plays a role in finding valid vulnerabilities. It’s essential to conduct thorough reconnaissance to identify potential attack surfaces and vulnerabilities. By doing so, you increase your chances of finding vulnerabilities that scanners may not detect.

Get Rajdip’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thanks for reading!!! Happy Hacking!!!!

follow me on LinkedIn — https://www.linkedin.com/in/rdsarkar/
