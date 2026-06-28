---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-06_xss-on-sony-subdomain.md
original_filename: 2020-01-06_xss-on-sony-subdomain.md
title: XSS on Sony subdomain
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: c9b579b8b5f72f5844d61222f420bae956e317c02aa07c481ffb21ea98704bcf
text_sha256: c37c25611cfa5ee5d89c43184def833796bcb40392138c0bc236f40ffd8f01a8
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# XSS on Sony subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-06_xss-on-sony-subdomain.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c9b579b8b5f72f5844d61222f420bae956e317c02aa07c481ffb21ea98704bcf`
- Text SHA256: `c37c25611cfa5ee5d89c43184def833796bcb40392138c0bc236f40ffd8f01a8`


## Content

---
title: "XSS on Sony subdomain"
url: "https://medium.com/@gguzelkokar.mdbf15/xss-on-sony-subdomain-feddaea8f5ac"
authors: ["Gökhan Güzelkokar (@gkhck_)"]
programs: ["Sony"]
bugs: ["Reflected XSS"]
publication_date: "2020-01-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4843
scraped_via: "browseros"
---

# XSS on Sony subdomain

XSS on Sony subdomain
Gökhan Güzelkokar
Follow
2 min read
·
Jan 7, 2020

636

8

Press enter or click to view image in full size

Hi guys. This is my first bug bounty writeup. I started to bug bounty on july 22, 2019. I want to share with community all the vulnerabilities I have found.

I choose for large scope programs when looking for bug bounty programs and for improve myself I don’t care about bounty now. So I chose SONY.

I started with subdomain enumaration. Firstly, I used crt.sh and I use the following to find potential sub-domains.

##Now does not support :(

%my%.sony.net

%jira%.sony.net

%jenkins%.sony.net

%test%.sony.net

%staging%.sony.net

%corp%.sony.net

%api%.sony.net

%ws%.sony.net

%.%.%.sony.net

Sometimes just random letters..

Get Gökhan Güzelkokar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

%p%.sony.net

%i%.sony.net

%ff%.sony.net

%co%.sony.net

Press enter or click to view image in full size
crt.sh

I found this one (ppf.sony.net). Then, I used assetfinder and httprobe by tomnomnom for subdomain enumeration and I found a deep sub-domain. Here is our target sub-domain. authtry.dev2.sandbox.dev.ppf.sony.net

assetfinder -subs-only ppf.sony.net | httprobe

authtry.dev2.sandbox.dev.ppf.sony.net

Then, I used dirsearch for secret directories. The default page appeared.

dirsearch.py -u “authtry.dev2.sandbox.dev.ppf.sony.net” -e html,json,php -x 403,500 -t 50

Press enter or click to view image in full size
Also, phpinfo is an information disclosure. I submitted another report

When I visit to index.php I got this page.

Press enter or click to view image in full size

As you can see we have 2 parameters and if you have parameters on the empty page, firstly try to get XSS. I tried get xss on the page and I got !!

Also my favorite payload : <img onerror=”{alert`1`}” src>

Press enter or click to view image in full size

Thank you !!!
