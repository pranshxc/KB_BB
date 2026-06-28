---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-02_how-i-get-5x-swag-from-sony.md
original_filename: 2022-11-02_how-i-get-5x-swag-from-sony.md
title: How I Get 5x Swag From Sony
category: documents
detected_topics:
- xss
- information-disclosure
- idor
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- xss
- information-disclosure
- idor
- command-injection
- otp
- rate-limit
language: en
raw_sha256: b375d3edfeab23a29d15e0c7fb7482154705bc7dc6c554bf825aee5ae2e99142
text_sha256: 2e29ec39713b9032d623fe3f95374b373f57b290dd59373a8972f83f34a07c17
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# How I Get 5x Swag From Sony

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-02_how-i-get-5x-swag-from-sony.md
- Source Type: markdown
- Detected Topics: xss, information-disclosure, idor, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `b375d3edfeab23a29d15e0c7fb7482154705bc7dc6c554bf825aee5ae2e99142`
- Text SHA256: `2e29ec39713b9032d623fe3f95374b373f57b290dd59373a8972f83f34a07c17`


## Content

---
title: "How I Get 5x Swag From Sony"
url: "https://medium.com/@0xnaeem/how-i-get-5x-swag-from-sony-102dbefd0c2c"
authors: ["Naeem Ahmed Sayed (@0xNaeem)"]
programs: ["Sony"]
bugs: ["DOM XSS", "Directory listing", "Default credentials", "Information disclosure"]
publication_date: "2022-11-02"
added_date: "2022-11-03"
source: "pentester.land/writeups.json"
original_index: 1962
scraped_via: "browseros"
---

# How I Get 5x Swag From Sony

Naeem Ahmed Sayed (0xNaeem)
Follow
3 min read
·
Nov 2, 2022

253

2

How I Get 5x Swag From Sony
Press enter or click to view image in full size

A
ssalamu Alaikum
I am Naeem Ahmed Sayed.
This is my 2nd bug hunting writeup. I started to bug bounty on January 2020. I want to share with community all the vulnerabilities I have found.

I Always like to choose for large scope programs bcz improve myself . So I chose SONY.

Anyway, let’s start

Recon is My Life

I started with subdomain enumeration. Firstly, I want to tell everyone i don’t use any tool only use browser and brain on subdomain enumeration I used crt.sh, bgp.he.net, shodan and acquisition find sub-domains and org related domain. example bgp.he.net to get some org name for shodan recon like org:”Sony Inc” 200 some time ssl.cert.subject.cn:”domain.com” in this my write-up my every finding Shodan Recon .

So, the topic of this write-up will be Share.

DOM XSS CVE-2021–24891
Directory Listing To Private Token Leak
Admin Panel Access Default Credentials
Information Disclosure (logs exposed)
Admin Panel Access Default Credentials Bypass Previous Report

CASE 1: DOM XSS CVE-2021–24891

shodan recon like org:”Sony Pictures Entertainment Inc” 200 and find interested sub-domain when check wappalyzer it’s running wordpress cms and page builder Elementor 3.4.8

Press enter or click to view image in full size

my habit when i get any version i search it google and the result i found dom xss on elementor

Press enter or click to view image in full size

CASE 2: Directory Listing To Private Token Leak

Press enter or click to view image in full size

shodan recon win

Get Naeem Ahmed Sayed (0xNaeem)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

CASE 3,5: Admin Panel Access Default Credentials

shodan recon to get this login panel and try username: Administrator password=***REDACTED***

And when Program Fix this bug and i check this ip this ip down the program But same panel running another ip how i bypass simple shodan recon ssl.cert.subject.cn:”sub.domain.com” 200

CASE 4: Information Disclosure (logs exposed)

When I Acquisitions About Sony I find cool domain

Follow Sony on Index.co
Consumer and professional electronics, gaming, entertainment and financial services.

index.co

then simply search site:*.domain.com and get juicy information Index of /conf/logs/

Press enter or click to view image in full size

For now I have 5 SWAGs from SONY.

And All Are Bug I find my phone ..

I’m not expert in English.

So forgive me ..

Allah Hafiz

Thank you !!!
