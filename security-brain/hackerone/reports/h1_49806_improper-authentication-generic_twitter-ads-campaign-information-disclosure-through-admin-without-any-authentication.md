---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49806'
original_report_id: '49806'
title: Twitter Ads Campaign information disclosure through admin without any authentication.
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-03-02T15:00:30.732Z'
disclosed_at: '2015-04-25T08:22:05.808Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Twitter Ads Campaign information disclosure through admin without any authentication.

## Metadata

- HackerOne Report ID: 49806
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2015-04-25T08:22:05.808Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Twitter !!

I just wanted to report a major flaw which I found in https://ads.twitter.com , hoping it make twitter more secure and I am glad for being a part of it.

**Vulnerability Name**:  OWASP:A6 Sensitive data Exposure

**Vulnerable URL**: https://ads.twitter.com/admin/accounts_typeahead.json?query=*****

**Vulnerability Overview**: Information Disclosure without any *authentication* .

**Proof of Concept:**
   - Log into twitter account first.
   - Go to this URL https://ads.twitter.com/admin/accounts_typeahead.json?query=avicoder
   - Change the query string to any other account or screen_name ex: *microsoft*
   - You can view all the information about the account associated with the  campaign.
   - Usually this information is only visible to members of campaign.
   - Look at user_name_info element in JSON POC which actually exposing the members associated with campaign. 

**I attached the json file when I query my account in private window..
Its gives me all information about members linked to the campaign without any need of being (admin,manager,analyst)**

I made this report short  unlike my previous reports but it is to the point.
Please revert back if more information is needed. 

*Happy to help*
#:)#
**avicoder**

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
