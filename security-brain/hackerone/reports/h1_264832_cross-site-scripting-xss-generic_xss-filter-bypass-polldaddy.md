---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '264832'
original_report_id: '264832'
title: xss filter bypass [polldaddy]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2017-08-30T20:06:15.434Z'
disclosed_at: '2017-10-01T15:56:17.013Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss filter bypass [polldaddy]

## Metadata

- HackerOne Report ID: 264832
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2017-10-01T15:56:17.013Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

previously reported xss https://hackerone.com/reports/107405 which is fixed, but i am able to bypass that fix. 

Payload for bypass : `<a href="javascript&colon;alert&lpar;document&period;domain&rpar;">Click Here</a>` 

# Steps:
-  Login into Polldaddy account polldaddy.com
- go to ___POLLS___  and create new poll
- in answers. enter xss payload `<a href="javascript&colon;alert&lpar;document&period;domain&rpar;">Click Here</a>` 

{F217173}

- Save it 
-  go here :where you can edit style  https://polldaddy.com/polls/XXXXX/style-edit/  
{F217170}

scroll down and click on it , xss will trigger.
{F217172}

Ref: https://hackerone.com/reports/107405

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
