---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-06_csrf-to-one-tray-red-bull.md
original_filename: 2021-10-06_csrf-to-one-tray-red-bull.md
title: CSRF to one tray Red-bull
category: documents
detected_topics:
- command-injection
- csrf
- cloud-security
tags:
- imported
- documents
- command-injection
- csrf
- cloud-security
language: en
raw_sha256: ba18173a7f3c1b88d038a1d444ecbc0c8e3c99368505470656583f8ea63a31c0
text_sha256: 6de194dd2906143c7e7286a2f3aea716032286d6e2f8348a1a1582a3c8a23e1d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF to one tray Red-bull

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-06_csrf-to-one-tray-red-bull.md
- Source Type: markdown
- Detected Topics: command-injection, csrf, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `ba18173a7f3c1b88d038a1d444ecbc0c8e3c99368505470656583f8ea63a31c0`
- Text SHA256: `6de194dd2906143c7e7286a2f3aea716032286d6e2f8348a1a1582a3c8a23e1d`


## Content

---
title: "CSRF to one tray Red-bull"
url: "https://medium.com/@saneem7/csrf-to-one-tray-red-bull-6564cd884a47"
authors: ["Mohammed Saneem"]
programs: ["Redbull"]
bugs: ["CSRF"]
publication_date: "2021-10-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3259
scraped_via: "browseros"
---

# CSRF to one tray Red-bull

CSRF to one tray Red-bull
Mohammed Saneem
Follow
2 min read
·
Oct 5, 2021

71

1

Hi all,

I am Mohammed Saneem, a cyber security engineer and leisure time bug bounty hunter.

This blog is about how I was able to get bounty from redbull. All started when I saw people posting trays of redbull provided for finding flaws in the system, So I decided to test on the target.
Since Redbull has wide scope I did recon i.e., collected all the subdomain using different tools such as Sublist3r, Asset-finder, amass(used more than one tool to increase the scope). After collecting the subdomains sorted it and found live hosts using httprobe. My next step was to find any directories so i fuzzed using wordlist and found phpmyadmin panel. After getting phpmyadmin panel, I was wondering what I can do here. I checked in wappalyzer to check if it was using any outdated software wit vulnerability. Lucky me, it was using a outdated component and was vulnerable to CSRF. Quickly crafted POC and reported it and triaged as medium severity.

Get Mohammed Saneem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Note:

Whenever you get a older technologies check for vulnerability in it and exploit it (show impact to triage).
Check in google for similar public hackerone reports(This will help you a lot)

Since this was a CVE affecting phpmyadmin I knew the organization will be using this for all other website. So I thought of automating it. I wrote a nuclei template for it and scanned . Got many more subdomains with the same vulnerability.
You can use my template from official nuclei tool.

https://github.com/projectdiscovery/nuclei-templates/blob/master/cves/2019/CVE-2019-12616.yaml

This is my first writeup, Hope you learned something from it.

You can contact me via Linkedin
