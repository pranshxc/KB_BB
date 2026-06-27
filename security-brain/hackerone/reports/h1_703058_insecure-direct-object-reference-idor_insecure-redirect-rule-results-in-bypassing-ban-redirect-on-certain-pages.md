---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '703058'
original_report_id: '703058'
title: Insecure redirect rule results in bypassing ban redirect on certain pages
weakness: Insecure Direct Object Reference (IDOR)
team_handle: roblox
created_at: '2019-09-27T16:31:08.051Z'
disclosed_at: '2020-04-26T06:10:02.222Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 214
asset_identifier: '*.roblox.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Insecure redirect rule results in bypassing ban redirect on certain pages

## Metadata

- HackerOne Report ID: 703058
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: roblox
- Disclosed At: 2020-04-26T06:10:02.222Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Description
Account bans on Roblox work via redirect rules. If an user attempts go to a page that's outside a whitelisted set of rules, they'll be redirected back to the ban page.

After researching, I've found that the following rules are whitelisted and bypass this redirect:
- Any URLs ending in a file extension (except for .aspx, .ashx)
- https://www.roblox.com/request-error/*
- https://www.roblox.com/login/*
- https://www.roblox.com/info/*
- https://www.roblox.com/support/ *
- https://www.roblox.com/*/membership/*

All of these seem okay, except for `https://www.roblox.com/*/membership/*`. The `/membership/` part is not anchored to the start of the URL.

In ASP.NET, we can actually insert paths after the extensions `.aspx` and `.ashx`, which will just be ignored by the server.

This allows us to access any pages ending in `.aspx/.ashx` without a ban-redirect, just by appending `/membership/` after the extension. Ex.: https://www.roblox.com/my/money.aspx/membership/

## Impact

An attacker would be able to access the following pages/apis with a banned account:
- Create/update assets - https://data.roblox.com/Data/Upload.ashx
- Post comments on assets - https://www.roblox.com/API/Comments.ashx
- Trade Items (Unverified)   - https://www.roblox.com/Trade/tradehandler.ashx
- Use any other page or API ending in .ashx/.aspx

A moderator couldn't do anything to stop the attacker from performing these actions. Bans would be ineffective.

Another thing I would like to mention is that banned accounts can access ANY web apis at api.roblox.com, without a need for a bypass or anything.

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
