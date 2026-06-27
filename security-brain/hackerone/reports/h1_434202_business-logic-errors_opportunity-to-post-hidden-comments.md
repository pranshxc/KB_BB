---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '434202'
original_report_id: '434202'
title: Opportunity to post hidden comments
weakness: Business Logic Errors
team_handle: x
created_at: '2018-11-05T06:45:41.903Z'
disclosed_at: '2018-12-11T23:33:19.337Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Opportunity to post hidden comments

## Metadata

- HackerOne Report ID: 434202
- Weakness: Business Logic Errors
- Program: x
- Disclosed At: 2018-12-11T23:33:19.337Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Twitter allows to comment on anyone's tweet. While testing this feature, observed that one can post comment on tweet which will be invisible to the victim whom the reply was posted and would be visible to any other twitter user.
This can allow an Attacker to abuse victim on a tweet. The catch here is victim cannot even know that attacker posted on his tweet but any other twitter user can see that tweet.

**Steps to reproduce**

1. Attacker login to Twitter
2. Attacker blocks victim using Block@victim button at https://twitter.com/<victim>
3. Attacker opens any popular tweet of victim
4. Attacker abuses victim in the tweet reply
5. Victim cannot see the tweet reply posted by Attacker but any other user can see that reply.

**Recommendation**
If a person blocks a twitter user then he/she should not be allowed to post on any of the blocked user tweets.

## Impact

This can allow an Attacker to abuse victim on a tweet. The catch here is victim cannot even know that attacker posted on his tweet but any other twitter user can see that tweet.

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
