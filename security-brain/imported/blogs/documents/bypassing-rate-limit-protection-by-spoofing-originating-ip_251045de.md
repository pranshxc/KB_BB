---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-30_bypassing-rate-limit-protection-by-spoofing-originating-ip.md
original_filename: 2017-08-30_bypassing-rate-limit-protection-by-spoofing-originating-ip.md
title: Bypassing Rate Limit Protection by spoofing originating IP
category: documents
detected_topics:
- command-injection
- rate-limit
tags:
- imported
- documents
- command-injection
- rate-limit
language: en
raw_sha256: 251045de57ef7b6e62eb0c3fb6d86e5c19f9cfe502fecbce7743faa3ac7b05f8
text_sha256: 44ed5a9ccac177bc112b91286ab12558f33ee2c0140e37e1c908c033b4a64e24
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Rate Limit Protection by spoofing originating IP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-30_bypassing-rate-limit-protection-by-spoofing-originating-ip.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `251045de57ef7b6e62eb0c3fb6d86e5c19f9cfe502fecbce7743faa3ac7b05f8`
- Text SHA256: `44ed5a9ccac177bc112b91286ab12558f33ee2c0140e37e1c908c033b4a64e24`


## Content

---
title: "Bypassing Rate Limit Protection by spoofing originating IP"
url: "https://medium.com/@arbazhussain/bypassing-rate-limit-protection-by-spoofing-originating-ip-ff06adf34157"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["Bruteforce"]
publication_date: "2017-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6119
scraped_via: "browseros"
---

# Bypassing Rate Limit Protection by spoofing originating IP

Top highlight

Bypassing Rate Limit Protection by spoofing originating IP
Arbaz Hussain
Follow
2 min read
·
Aug 30, 2017

622

4

Severity: Medium

Complexity: Easy

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Weakness : Spoofing Originating IP

Most Application’s use X-Forwarded-For common method for identifying the originating IP address of the client.
We All know that using X-Forwarded-For: IP Header Can sometime’s Bypass Ratelimit Protection.
Sometimes Adding Two Times X-Forwarded-For: IP Header Instead of One time Can Bypass Ratelimit Protection
During testing one of the private hackerone target . They blocked my IP after 30–40 attempts because of fuzzing .
Following are the Test Cases i Tried to Bypass their Protection.
They Blocked My IP
Press enter or click to view image in full size

2. Trying Host Header Injection Way : (No Success)

Press enter or click to view image in full size

3. Trying X-Forwarded-For to Spoof Originating IP : (No Success)

Press enter or click to view image in full size

4. Trying with X-Forwarded-For: IP Header 2x times Instead of One time, Bypass Ratelimit Protection

Press enter or click to view image in full size
Press enter or click to view image in full size
I Asked Developer what make’s this behaviour , They SAID :

¯\_(ツ)_/¯
