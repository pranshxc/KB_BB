---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176083'
original_report_id: '176083'
title: JavaScript URL Issues in the latest version of Brave Browser
team_handle: brave
created_at: '2016-10-16T04:20:48.479Z'
disclosed_at: '2016-10-17T20:10:50.552Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
---

# JavaScript URL Issues in the latest version of Brave Browser

## Metadata

- HackerOne Report ID: 176083
- Weakness: 
- Program: brave
- Disclosed At: 2016-10-17T20:10:50.552Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
* The URL javascript: can redirect users to any site, instead of executing JavaScript.

## Additional Notes
* Found as partners by @kicker (http://hackerone.com/kicker) and myself (@smelt).

## Products affected: 
* The current version of Brave Browser on Windows.
* The current mobile version of Brave Browser.

## Steps To Reproduce:
* Open Brave Browser
* Go to javascript:javascript: or javascript:javascript:hackerone.com in the Brave Browser.
* If using the **javascript:javascript:** link, the browser should redirect to your search engine's homepage.
* If using the **javascript:javascript:hackerone.com** link, the browser should redirect to HackerOne. (HackerOne was just an option, you can redirect to any URL.)

* This bug is different than the redirection bug previously disclosed, allowing addresses after @ to redirect to that site. The site can be redirected using simply the javascript: URL in this bug.

## Supporting Material/References:
* See attached video files.

Thanks for reviewing this report, and let me cross my fingers, that it's not a duplicate! :)

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
