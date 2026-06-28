---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-13_story-of-5000-bounty-for-grafana-panel-access-in-apple.md
original_filename: 2022-08-13_story-of-5000-bounty-for-grafana-panel-access-in-apple.md
title: Story of 5000$ bounty for Grafana Panel Access in Apple
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: 99fda16ff0547c61ff7e425ec0944b18e8f7882d859434106779883dda3220a4
text_sha256: 5654c834206ffe8a79400a2f5266dcc0755827d24c2c2cd85b6c091fe6df1ac0
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Story of 5000$ bounty for Grafana Panel Access in Apple

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-13_story-of-5000-bounty-for-grafana-panel-access-in-apple.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `99fda16ff0547c61ff7e425ec0944b18e8f7882d859434106779883dda3220a4`
- Text SHA256: `5654c834206ffe8a79400a2f5266dcc0755827d24c2c2cd85b6c091fe6df1ac0`


## Content

---
title: "Story of 5000$ bounty for Grafana Panel Access in Apple"
url: "https://medium.com/@lovely.goyal1998/story-of-5000-bounty-for-grafana-panel-access-in-apple-89c93ab4486f"
authors: ["hckerl00 (@lokeshg62498939)"]
programs: ["Apple"]
bugs: ["Missing authentication", "Information disclosure"]
bounty: "5,000"
publication_date: "2022-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2316
scraped_via: "browseros"
---

# Story of 5000$ bounty for Grafana Panel Access in Apple

Story of 5000$ bounty for Grafana Panel Access in Apple
@hckerl00
Follow
3 min read
·
Aug 13, 2022

246

3

Press enter or click to view image in full size

W
ho am I ?

My name is Lokesh(@hckerl00) & I am a bug bounty hunter. Here I’m sharing a small write-up on one of my bug in apple.

H
ow was the process of My Finding ?

I started my hunting after reading the write-up of Ahmad Halabi on Apple.

So After reading (on 21st july) this Write-up, I started my recon for Apple domains. Because Apple have large amount of Domains, I started with their *.apple.com Domain.

Important Part of My Recon: For Get some change in my recon, I gathered some information about recon from Medium’s write-up. After one day, I got one write-up Muhammad Daffa. You must check this write-up.

S
o, on 23 July I started subdomain enumeration using below tools:

Subfinder, Amass, Asset-finder, Sublist3r

This tools provided me ~1lac domains. Then I collected all subdomains and tried two things:

At the beginning, I find live subdomains from above domains list

cat sub.txt | httpx | tee -a live_sub.txt

List of live subdomain was large which didn’t interest me. So, I focused on Gather Information through Nuclei 🠓.

In addition, I used all subdomains (~1 lacs) to run with nuclei which took me a day for get half subdomains details:

cat sub.txt | nuclei -t “Your-Templates-Location”

Here, I got large number of information from NUCLEI. So i started looking for LOW, MEDIUM, HIGH & CRITICAL Severity bug. Here I got Bad Luck……….

Didn’t get the Severity bug, So I started looking for some keywords in INFO Severity result of NUCLEI where I got one keyword GRAFANA, This keyword was showing result with “INFO” Severity.

One more thing, Keyword was not present in url, It showed in Template names.

Here I thought, may be if this panel had Vulnerable/Old version then I can try Template based Injection bug of GRAFANA. That’s my first choice for grafana panel 😉…

Get @hckerl00’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I Opened this url and I totally shocked by the result….

Press enter or click to view image in full size

BOOM, I got the access on Grafana panel without login, I have high privilege access like read, write, execute & Delete etc…

Here, I got lots of information like API SERVER, Internal IP address of Managers (10+)(IP’s 10.*.*.* and 172.*.*.*), and other information (AWS).

After 5 min of Getting this panel, I was like…

PROCESS of Report: My Report patched within 1 hour after getting first response from Apple Team. And Got the Hall of fame after 13 days in their list.

Press enter or click to view image in full size

Timeline:

26-July-2022, 5:38 PM → Submitted Report

27-July-2022, 2:40 AM → First Response From Apple Team (Verified)

27-July-2022, 3:26 AM → Second Response From Apple Team (Bug Patched)

10-Aug-2022 → Bounty Announced 5000$ From Apple Team

Press enter or click to view image in full size

You can also read my first write-up of my first 1000$ bounty, using given link in below: https://m0di-b0nd.blogspot.com/2021/08/pixel-flood-via-file-uploading.html

You can connect with me on:

Twitter || Linkedin

Thank to all of you for reading this write-up

Regards
