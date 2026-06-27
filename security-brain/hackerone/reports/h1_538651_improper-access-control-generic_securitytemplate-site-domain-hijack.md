---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '538651'
original_report_id: '538651'
title: securitytemplate.site domain hijack
weakness: Improper Access Control - Generic
team_handle: ed
created_at: '2019-04-15T13:53:15.126Z'
disclosed_at: '2019-04-15T15:38:29.667Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: securitytemplate.site
asset_type: URL
max_severity: none
tags:
- hackerone
- improper-access-control-generic
---

# securitytemplate.site domain hijack

## Metadata

- HackerOne Report ID: 538651
- Weakness: Improper Access Control - Generic
- Program: ed
- Disclosed At: 2019-04-15T15:38:29.667Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

# Security-template
I realized that your [security-template project](https://github.com/EdOverflow/security-template) domain name seems to have expired, http://securitytemplate.site doesn't serve your content.

# Penultimate
I also found that it's possible to takeover the PenultimateIO's Twitter account. It seems that you have deleted the account, but it is possible to recreate it, as you can see on the screenshot ([https://twitter.com/settings/account](https://twitter.com/settings/account)):

{F469141}
{F469142}

I didn't change my username, but knowing that Twitter indicates it as available, I consider it achievable.

There are several references to the penultimateIO Twitter account, on your Twitter and on the Penultimate Github. 

- https://twitter.com/EdOverflow/status/965559093476954112
- https://github.com/Penultimate/challenges/wiki
- https://github.com/Penultimate/challenges/blob/master/XSS/000000-xss.html
- https://github.com/Penultimate/challenges/blob/master/XSS/000001-xss.html

Your Twitter and the Penultimate's Github are out of scope, as well as social engineering, but due to the ease of implementation I prefer to report it.



Have a nice day,
Florian

## Impact

This can be used by an attacker to conduct social enginerring attacks.

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
