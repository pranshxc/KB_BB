---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116512'
original_report_id: '116512'
title: Markdown parsing issue enables insertion of malicious tags
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gratipay
created_at: '2016-02-15T08:08:07.472Z'
disclosed_at: '2017-08-21T13:28:46.303Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Markdown parsing issue enables insertion of malicious tags

## Metadata

- HackerOne Report ID: 116512
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gratipay
- Disclosed At: 2017-08-21T13:28:46.303Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Markdown tags and event handlers can be used to load malicious URLs in user's profile statement.

Here is the payload that when entered in user's profile statement leads to the following HTML:

Payload: _www.attacker.com/malicious.exe_

Resulting HTML:  "html": "<p><em><a href=\"http://www.attacker.com/malicious.exe\">www.attacker.com/malicious.exe</a></em></p>\n"

See the following screenshots for more details:

"Profile.jpg"
"request.jpg"
"response.jpg"

User can be redirected to malicious URLs and malware can be hosted on gratipay.com using this vulnerability.

Fix:

Disable the functionality for these markdown tags.

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
