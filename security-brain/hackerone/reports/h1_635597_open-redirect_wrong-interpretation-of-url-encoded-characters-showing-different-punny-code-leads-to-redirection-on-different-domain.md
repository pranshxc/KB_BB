---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '635597'
original_report_id: '635597'
title: Wrong Interpretation of URL encoded characters, showing different punny code
  leads to redirection on different domain
weakness: Open Redirect
team_handle: x
created_at: '2019-07-04T12:19:54.553Z'
disclosed_at: '2019-08-26T16:55:39.330Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Wrong Interpretation of URL encoded characters, showing different punny code leads to redirection on different domain

## Metadata

- HackerOne Report ID: 635597
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2019-08-26T16:55:39.330Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary:
There is wrong interpretation of URL encoded characters at `https://twitter.com/safety/unsafe_link_warning` endpoint which could lead to different location then what is supposed to.

Although it shows warning but doesn't show warning about punny code characters.

##Description:
On following characters:

```
%E2%80%AE - RTLO Character
%E2%80%8E - LEFT-TO-RIGHT MARK
%E2%80%91 - Non breaking hyphen
%E2%80%A9 - PARAGRAPH SEPARATOR
%E2%80%AA 0 Right-to-left embedding
```
Interpretation of these characters is different but when we click continue button it will redirect you to some other location.

## Steps To Reproduce:

1. Go to following URL: https://twitter.com/safety/unsafe_link_warning?unsafe_link=https%3A%2F%2F%E2%80%AEmoc.rettiwt
2. You will see that its showing : https://twitter.com

{F522041}

But originally you will be redirected to https://xn--moc-4t7s.rettiwt/ when you click continue button.

##Argument:
> But it is not possible to have TLD 'rettiwt'.
* counter:
We can have URL as follows:
```
https://twitter.com/safety/unsafe_link_warning?unsafe_link=https%3A%2F%2F%E2%80%AEmoc.rettiwt.com
```

{F522042}



## Supporting Material/References:

  * screenshots.

## Impact

Wrong location redirection.

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
