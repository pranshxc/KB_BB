---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '44157'
original_report_id: '44157'
title: Open Redirection Security Filter bypassed
weakness: Open Redirect
team_handle: vimeo
created_at: '2015-01-17T14:57:43.298Z'
disclosed_at: '2015-06-28T15:50:24.025Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- open-redirect
---

# Open Redirection Security Filter bypassed

## Metadata

- HackerOne Report ID: 44157
- Weakness: Open Redirect
- Program: vimeo
- Disclosed At: 2015-06-28T15:50:24.025Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The application is vulnerable to Open Redirection using a basic filter bypass which it was using for security against open redirection.

Here is the vulnerable link:
https://vimeo.com/tools/edit?image=http://securityidiots.com?vimeocdn.com/.png

Weakness in filter against Open Redirect.: Actually the application is using the below given filters against open redirection.
1. URL must contain "vimeocdn.com/"
2. It should end with an image extention for example jpg, png etc

The problem with the above filter can be seen in my payload, as i included both of the requirements and still redirected the user to my url.

Solution : Below changes can be made to the security.
If "https://f.vimeocdn.com/" is the URL for images then hardcode it and take the rest of input from GET so that in any case we will have "https://f.vimeocdn.com/" before the URL and user wont be able to do a open redirect to any other domain.

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
