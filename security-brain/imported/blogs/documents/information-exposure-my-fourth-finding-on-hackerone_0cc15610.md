---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-17_information-exposure-my-fourth-finding-on-hackerone.md
original_filename: 2022-11-17_information-exposure-my-fourth-finding-on-hackerone.md
title: Information Exposure — My Fourth Finding on Hackerone!
category: documents
detected_topics:
- information-disclosure
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- information-disclosure
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: 0cc15610fb83465319878cd87532e7334832fbc3fb7afcc2e99187ae5d6efc74
text_sha256: 9f5a0c7ef9dfca51b960d7660d83d93c45499ee5bb14482b0ea28978ed4b6809
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Information Exposure — My Fourth Finding on Hackerone!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-17_information-exposure-my-fourth-finding-on-hackerone.md
- Source Type: markdown
- Detected Topics: information-disclosure, idor, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `0cc15610fb83465319878cd87532e7334832fbc3fb7afcc2e99187ae5d6efc74`
- Text SHA256: `9f5a0c7ef9dfca51b960d7660d83d93c45499ee5bb14482b0ea28978ed4b6809`


## Content

---
title: "Information Exposure — My Fourth Finding on Hackerone!"
url: "https://mehedishakeel.medium.com/information-exposure-my-fourth-finding-on-hackerone-4fc4461920c4"
authors: ["mehedishakeel (@mehedishakeel)"]
bugs: ["Directory listing", "Information disclosure"]
publication_date: "2022-11-17"
added_date: "2022-11-18"
source: "pentester.land/writeups.json"
original_index: 1902
scraped_via: "browseros"
---

# Information Exposure — My Fourth Finding on Hackerone!

Information Exposure — My Fourth Finding on Hackerone!
mehedishakeel
Follow
3 min read
·
Nov 17, 2022

275

2

Information Exposure Through Directory Listing — The bug title says everything about it. Find a path or URL on any website that's enable directory listing on your target website and by using that directory listing you have to access any sensitive information. It’s different version of Sensitive Information Disclosure vulnerability.

Press enter or click to view image in full size

Now let’s discuss how i get my fourth bug and what are the tools and technique i use,

It was a private program, So I am not authorized to include the real domain and company name into this write up. But I will try to explain everything in details so that you can imagine the scenario. On that target program scope I had 30+ domain and one of those domain look like the following example

*.mehedishakeel.com

So, I started with subdomain enumeration and basic information collecting with subfinder & httpx . In bug bounty hunting for collecting subdomains and basic info those tools are very useful and fast enough.

Luckily i, found a huge active subdomain list. Getting the result make me change my regular approach. I decided to stick with this targets for a long time. So, I started with the main domain

https://mehedishakeel.com

I open the URL in browser, manually visit every page but didn’t get anything interesting. I think of visiting a common juicy file name “robots.txt”. Unfortunately, i didn’t get anything special on that file.

Remember, always visit all the URL which is disallowed on /robots.txt file.

https://mehedishakeel.com/robots.txt

Then I open Wappalyzer add-on and get the following result,

It, was a huge list which contains some technology i didn’t know much about them. I started to learn the basic of all the technology used in this website.

Get mehedishakeel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But i don’t want to waste my time , So here i started to find sensitive information through directory searching using diresearch.

If you want to know, how to use “dirsearch” tool to find sensitive information , then go through my Information Disclosure — My First Finding on Hackerone! write-up.

By using these automate tool i found a very interesting directory like the following,

https://www.mehedishakeel.com/typo3conf/ext/

I visit that url and it’s enable directory listing, and by navigating every possible directory manually , i found an interesting directory ,

ext/static_info_tables

These directory contains two juicy file,

tables.sql 
tables_static.sql

I downloaded those two file and open them into notepad, and i see some sql query and some sensitive static data into those sql files.

I quickly reported that bug ,

That’s how I got my fourth resolved bug on hackerone. Thank you for reading!
