---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '949295'
original_report_id: '949295'
title: Unrestricted File Upload on https://app.dropcontact.io/app/upload/
weakness: Unrestricted Upload of File with Dangerous Type
team_handle: dropcontact
created_at: '2020-08-01T15:56:54.602Z'
disclosed_at: '2020-08-11T10:45:15.009Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: app.dropcontact.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- unrestricted-upload-of-file-with-dangerous-type
---

# Unrestricted File Upload on https://app.dropcontact.io/app/upload/

## Metadata

- HackerOne Report ID: 949295
- Weakness: Unrestricted Upload of File with Dangerous Type
- Program: dropcontact
- Disclosed At: 2020-08-11T10:45:15.009Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi team,
 I found  Unrestricted File Upload Vulnerabilities on  https://app.dropcontact.io/app/upload/.

## Steps To Reproduce:

  1. Create an account in https://app.dropcontact.io/app/
  1. go to https://app.dropcontact.io/app/upload/
  1. try to upload html file , you will see message only (: .csv, .txt, .xls, .xlsx) allowed.
  1. change the HTML file extension to txt and try to upload it again 
  1. it work and the file successfully uploaded

## Supporting Material/References:
https://www.exploit-db.com/docs/english/45074-file-upload-restrictions-bypass.pdf
https://www.opswat.com/blog/file-upload-protection-best-practices

{F932903} 


## how to fix 
To avoid these types of file upload attacks: 
1. File type verification
1. Restrict specific file extensions 
1. add verification in both back-End and front-End

## Impact

this is not really impact because the app not report the full path for the files uploaded.
but if an attacker found a way to get the path . it wil be used to get attackes like xss or even rce .

Best Regards,
@omarelfarsaoui

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
