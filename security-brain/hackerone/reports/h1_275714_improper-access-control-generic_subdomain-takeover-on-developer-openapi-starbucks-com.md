---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '275714'
original_report_id: '275714'
title: Subdomain takeover on developer.openapi.starbucks.com
weakness: Improper Access Control - Generic
team_handle: starbucks
created_at: '2017-10-09T17:46:08.293Z'
disclosed_at: '2018-02-17T16:34:37.814Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
asset_identifier: Other non domain specific items
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Subdomain takeover on developer.openapi.starbucks.com

## Metadata

- HackerOne Report ID: 275714
- Weakness: Improper Access Control - Generic
- Program: starbucks
- Disclosed At: 2018-02-17T16:34:37.814Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

### Summary: 
Subdomain `developer.openapi.starbucks.com` is vulnerable to subdomain takeover via Mashery service. The reason why it's worked unfortunately not fully clear to me.

### Details:
Doing my recent research on starbucks.com subdomains, I stumbled upon http://developer.openapi.starbucks.com/ The server returned 200 response with the following {F227581} The `Server` header of HTTP responce was `Mashery Proxy` so it gave me an idea, that I should go and try register an trial account at https://www.mashery.com/

After registering an account and confirming it, I got access to the dashboard. Under the `Portal Settings` menu there was an option to add your own domain name. I added developer.openapi.starbucks.com as my domain and I get no error. After I went to the http://developer.openapi.starbucks.com/ and saw welcome page {F227586} which gave me understanding that I can serve my own content under developer.openapi.starbucks.com

### PoC:
I added simple js code to the Welcome page `alert(document.domain)` for this proof-of-concept.
To confirm it just click this link http://developer.openapi.starbucks.com/

### Impact:
As I can serve my own content without any restrictions, with this webpage I can set up a campaign to steal user cookie sessions, or use it to steal credentials, or for phishing purposes. 

Please let me know, if you need more information!

Thanks,
Danil

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
