---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '89505'
original_report_id: '89505'
title: Self-XSS in posts by formatting text as code
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2015-09-18T04:55:10.911Z'
disclosed_at: '2015-11-10T18:33:51.508Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self-XSS in posts by formatting text as code

## Metadata

- HackerOne Report ID: 89505
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2015-11-10T18:33:51.508Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi I have found an XSS in Slack. To reproduce the issue, just follow this:

1. Go to your Slack account (accountname.slack.com)

2. Below you will see a plus (+) sign, click that, there will be three options, click "Create Post"

3. You will be redirected to a page where you will create it.

4. Type the payload. I used: <svg onload=alert(domain)>. then Highlight it..  on the left side, there are symbols... click it and choose this symbol: ( <>) which is for code..

5. XSS Pop-up

Youtube video for clearer details:

https://youtu.be/dIvNeb2aRrU


THANKS!

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
