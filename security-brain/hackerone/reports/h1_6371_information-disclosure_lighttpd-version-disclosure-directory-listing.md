---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6371'
original_report_id: '6371'
title: Lighttpd version disclosure / directory listing
weakness: Information Disclosure
team_handle: khanacademy
created_at: '2014-04-08T00:38:30.887Z'
disclosed_at: '2014-04-12T22:06:49.246Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Lighttpd version disclosure / directory listing

## Metadata

- HackerOne Report ID: 6371
- Weakness: Information Disclosure
- Program: khanacademy
- Disclosed At: 2014-04-12T22:06:49.246Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello there,

the website at http://graphite.khanacademy.org/ isn't configured correctly.

It displays the lighttpd version as well the directory contents.
You should disable these features in your lighttpd.conf / php.ini.

PoC:

```
Index of /

Name	Last Modified	Size	Type
Parent Directory/	 	-  	Directory
index.lighttpd.html	2012-Jun-12 02:46:34	3.4K	text/html
lighttpd/1.4.28
```

Yours sincerely,
Sebastian Neef

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
