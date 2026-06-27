---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '689997'
original_report_id: '689997'
title: Disclosure of Email title report in quick award paypout email (no content mode)
weakness: Information Disclosure
team_handle: security
created_at: '2019-09-07T04:06:06.929Z'
disclosed_at: '2019-10-11T18:12:19.939Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 61
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Disclosure of Email title report in quick award paypout email (no content mode)

## Metadata

- HackerOne Report ID: 689997
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-10-11T18:12:19.939Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello H1 Security Team

#Description
In report #645264 and #669776, email title disclosure has been fixed in no content settings.
However, there is one more area which needs to be fix - "Instant bounty Award Email".
In this email, even though email settings have been set as "No content", still it's displaying Report Title.


#Step to Reproduce
+ Go to Program Email settings `/program_name/email_settings` and set email Settings as "no content".
{F576922}

+ Now, Reward someone with quick Bounty Payout API.
```
curl "https://api.hackerone.com/v1/programs/42738/bounties" \
  -X POST \
  -u "dummy:xxxxxxxx" \
  -H "Content-Type: application/json" \
  -d @- <<EOD
    {
      "data": {
        "type": "bounty",
        "attributes": {
          "amount": 100,
          "reference": "aaaaa",
          "title": "SQL injection in example.com",
          "recipient": "example@example.com",
          "currency": "USD",
          "severity_rating": "high"
        }
      }
    }
EOD
```
+ In email, it's disclosing the Report Title even though Email settings has been set to "no content".
{F576923}

Thanks
Kunal

## Impact

+ Email report Title is been leaked in the settings as Email-notification: No content.

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
