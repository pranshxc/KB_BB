---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '29491'
original_report_id: '29491'
title: homograph attack. IDNs displayed in unicode in bug reports and on external
  link warning page
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-09-30T18:51:48.699Z'
disclosed_at: '2014-10-09T17:08:05.146Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# homograph attack. IDNs displayed in unicode in bug reports and on external link warning page

## Metadata

- HackerOne Report ID: 29491
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-10-09T17:08:05.146Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

the IDN: http://ebаy.com/

is a homograph for the latin ebay.com. if you click that first link, youm might think that you are going to ebay.com. in fact, you are going to a homograph url http://xn--eby-7cd.com/

more info http://www.chromium.org/developers/design-documents/idn-in-google-chrome

more info http://www.charset.org/punycode.php?encoded=http%3A%2F%2Fxn--eby-7cd.com%2F&decode=Punycode+to+normal+text

it would be safer to show the punycode version of the url so that it would be apparent that something weird is going on. that is, show http://xn--eby-7cd.com/ instead of http://ebаy.com/

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
