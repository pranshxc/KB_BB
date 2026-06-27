---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221133'
original_report_id: '221133'
title: Sub Domain Takeover
team_handle: gratipay
created_at: '2017-04-15T04:58:00.526Z'
disclosed_at: '2017-10-24T16:13:22.787Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
---

# Sub Domain Takeover

## Metadata

- HackerOne Report ID: 221133
- Weakness: 
- Program: gratipay
- Disclosed At: 2017-10-24T16:13:22.787Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# One of Gratipay's sub domains points to Heroku with no app created.

## Description

Gratipay's sub domain http://www.gratipay.com.herokudns.com/ points to Heroku but is not in use. 

## Steps To Reproduce

###Details

 - Upon realization of vulnerability, installed and created a Heroku dependencies and application.

 - Added http://www.gratipay.com.herokudns.com/ to my list of domains through Heroku CLI. 

heroku domains:add www.gratipay.com.herokudns.com

After verifying my Heroku account this was easy to point the sub domain to my application. 

- Uploaded my application with text "B3nac sub domain takeover POC." and refreshed the domain to find it pointed to my application successfully.  
  
## Fix

If the domain is not in use, then it is recommended to point the dns entry away from the third party program.

## Supporting Material/References:

  * I've attached the uploaded takeover python application/website screenshot.

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
