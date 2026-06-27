---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '683792'
original_report_id: '683792'
title: XSS through chat messages
team_handle: vanilla
created_at: '2019-08-28T13:53:28.543Z'
disclosed_at: '2020-04-02T09:55:18.686Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: '*.vanillacommunities.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# XSS through chat messages

## Metadata

- HackerOne Report ID: 683792
- Weakness: 
- Program: vanilla
- Disclosed At: 2020-04-02T09:55:18.686Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

vulnerability name: cross site scripting through chat messages

vulnerability description:
cross site scripting is a vulnerability that allows an attacker to send malicious code(usually in javascript form)
to another user
Because a browser cannot know if the script should be trusted or not,
it will execute the script in user context allowing the attacker to access any cookies or sessions tokens retained 
by the browser.

payload;
<svg<script> onmou<script>seover</script>="alert('xss')">hii</svg</script>>

vulnerable url:http://4gcommunity.vanillacommunities.com/messages/4
## Steps to reproduce:
step 1.Go to http://4gcommunity.vanillacommunities.com/messages/4
step 2 .Go to Add message and send  any one payload as messages
step 3.when victim get messagenotification in bottom left as seen in screenshot,
take cursor over there,it will give "xss".

## Impact

1-> attacker can be used for stealing cookies 
2->As it is through messaging so easily,whomever payload sent will be affected.

POC:Screenshot and video enclosed in attachment

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
