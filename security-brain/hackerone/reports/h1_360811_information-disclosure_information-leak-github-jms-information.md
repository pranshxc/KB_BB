---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '360811'
original_report_id: '360811'
title: Information Leak - Github - JMS Information
weakness: Information Disclosure
team_handle: starbucks
created_at: '2018-06-01T14:42:40.959Z'
disclosed_at: '2018-08-16T20:12:51.016Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: Other non domain specific items
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information Leak - Github - JMS Information

## Metadata

- HackerOne Report ID: 360811
- Weakness: Information Disclosure
- Program: starbucks
- Disclosed At: 2018-08-16T20:12:51.016Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

After some research, I found a leak on GitHub that might lead to accessing sensitive data of employees or clients (not sure based on the code). There is also a SAP S-user to access a cloud based HANA service. I have not confirmed what kind of data is in there to avoid potential legal issues. I will let you guys figure that out ;)

I am not sure who is the owner of the repository, but I can tell you that the SAP credentials are for someone at Starbucks China.

https://github.com/karaskay/personalware

Some interesting files:
https://github.com/karaskay/personalware/blob/989723f896eec67a50a9b9f59ceefc48a046049b/python/PycharmProjects/JMS36/testhttprequestjson.py
(SAP Cloud HANA credentials)

https://github.com/karaskay/personalware/blob/989723f896eec67a50a9b9f59ceefc48a046049b/python/PycharmProjects/JMS36/JMSproducerforsurvey.py
(starbuckstest domain credentials)

Thanks!

## Impact

High potential of an unauthorized access to PII data

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
