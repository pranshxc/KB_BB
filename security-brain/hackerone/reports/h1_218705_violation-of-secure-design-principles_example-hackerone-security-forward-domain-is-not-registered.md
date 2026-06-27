---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218705'
original_report_id: '218705'
title: Example HackerOne security@ forward domain is not registered
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2017-04-05T09:56:53.195Z'
disclosed_at: '2017-04-10T17:45:56.997Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- violation-of-secure-design-principles
---

# Example HackerOne security@ forward domain is not registered

## Metadata

- HackerOne Report ID: 218705
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2017-04-10T17:45:56.997Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Description

In [this how-to article](https://support.hackerone.com/hc/en-us/articles/218142843-How-to-forward-emails-to-the-HackerOne-inbox), `@security-h1-forward.com` appears as a valid HackerOne domain for forwarding security issues. This domain is not registered. The actual flow does **not** include this domain, but I think it's confusing enough to consider the risk of someone mistakenly using the domain listed in the article (for example people that do not understand the *exempli gratia* abbreviation) 

{F173415}

I am not entirely sure whether this would qualify as a security issue but I do think it is something you should consider fixing. The risk is low, but the impact is high (both the exposure of incoming security reports without them being forwarded to the actual vendor and a false credibility for the domain), and a fix would be rather easy to implement. 

### Steps To Reproduce

1. Register `security-h1-forward.com` for **[$1](https://www.godaddy.com)**
2. Set up catch all e-mail forwarding to your e-mail address
3. Wait for security reports to come in that are mistakenly send to the domain mentioned in the help article

I'm aware of the fact that `support.hackerone.com` is excluded from the scope, but since it's not a vulnerability is the actual software itself, I thought it'd be OK to report it.

Best regards,


Inti

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
