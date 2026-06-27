---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145495'
original_report_id: '145495'
title: 'nextcloud.com: Directory listening for ''wp-includes'' forders'
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-06-17T18:02:13.368Z'
disclosed_at: '2016-06-17T18:10:38.465Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# nextcloud.com: Directory listening for 'wp-includes' forders

## Metadata

- HackerOne Report ID: 145495
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-06-17T18:10:38.465Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello guys,

**_Details:_**
The web server is configured to display the list of files contained in this directory. As a result of a misconfiguration - end user / attacker able to see content of the folders with systemically important files

**_Vulnerable place:_**
/wp-includes directory

when I tried to navigate to this directory via your domain - service responses me 'Access forbidden', but if I will navigate to the same directory via IP address (http://88.198.160.129/) - service will reflects whole entry.

**_PoC:_**
{F100046}

**_Impact:_** 
Exposing the contents of a directory can lead to an attacker gaining access to source code or providing useful information for the attacker to devise exploits, such as creation times of files or any information that may be encoded in file names. The directory listing may also compromise private or confidential data.

**_Remediation:_**
- Configure your web server to prevent directory listings for all paths beneath the web root;
- Place into each directory a default file (such as index.htm) that the web server will display
instead of returning a directory listing.

Let me know if you have any question.

Thanks for your attention,
Stas

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
