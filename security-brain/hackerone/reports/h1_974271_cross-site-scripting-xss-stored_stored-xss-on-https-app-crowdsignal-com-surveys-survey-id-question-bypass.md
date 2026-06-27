---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '974271'
original_report_id: '974271'
title: Stored XSS on https://app.crowdsignal.com/surveys/[Survey-Id]/question - Bypass
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2020-09-03T18:53:46.553Z'
disclosed_at: '2020-11-18T14:20:21.496Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 75
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on https://app.crowdsignal.com/surveys/[Survey-Id]/question - Bypass

## Metadata

- HackerOne Report ID: 974271
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2020-11-18T14:20:21.496Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I hope all is well!

I found a stored xss on https://app.crowdsignal.com/

Steps:
* Go to `https://app.crowdsignal.com/dashboard`
* Create a survey.
* Go to `https://app.crowdsignal.com/quizzes/{survey-id}/question`
* Add `Multiple Choice`
* Click `Add media` button.
* Select `Embed Media`
* Paste this: `[dailymotion id=x8oma9]`
* Insert it.
* Open Burp Suite and click `Save` button.
* Return to burp suite and paste xss payload to `media[11111111]` parameter: `[dailymotion id=x8oma9"><svg/onload=prompt(document.domain)>]`
* Forward the request and refresh the page. You will see xss alert.

This isn't self xss because I saw users who Team plan can invite other users to their dashboards. So attacker can steal victim's cookies.

Also I recorded a poc video for you:   
{F975177}

## Impact

Stealing cookies.

Best Regards,
@mygf

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
