---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '679969'
original_report_id: '679969'
title: CSS Injection to disable app & potential message exfil
weakness: Improper Input Validation
team_handle: slack
created_at: '2019-08-22T20:11:41.820Z'
disclosed_at: '2019-11-09T17:09:35.512Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: slack.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# CSS Injection to disable app & potential message exfil

## Metadata

- HackerOne Report ID: 679969
- Weakness: Improper Input Validation
- Program: slack
- Disclosed At: 2019-11-09T17:09:35.512Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Tested on Slack for MacOS v4.0.2 - I've marked this as code injection since there was no "css injection"

1. In the app go to Preferences -> Sidebar
2. Enable custom theming 
3. Set the column BG to `#FFFFFF;} html {display:none;}`
4. The app will no-longer render (this survives re-installs)

If this theme were to be shared to someone unsuspecting they would be unable to use slack, even surviving a reinstall (on mac, untested on other platforms).

Furthermore it _might_ be possible to exfil message data using CSS only. As seen here it is _possible_ to keylog via CSS only https://github.com/maxchehab/CSS-Keylogging/ however I have not been able to come up with a proper PoC of this.

I've marked this as low for now as I don't have a PoC exiling data however I have shown that it is possible to inject to completely disable the app.

## Impact

The app is no longer able to render - there might be the possibility of data exfil but I didn't get a PoC working.

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
