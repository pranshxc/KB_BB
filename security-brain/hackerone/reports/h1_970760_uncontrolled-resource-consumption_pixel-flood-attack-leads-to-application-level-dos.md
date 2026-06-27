---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '970760'
original_report_id: '970760'
title: Pixel Flood Attack leads to Application level DoS
weakness: Uncontrolled Resource Consumption
team_handle: cs_money
created_at: '2020-08-30T15:13:07.542Z'
disclosed_at: '2020-11-05T11:05:47.954Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: support.cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Pixel Flood Attack leads to Application level DoS

## Metadata

- HackerOne Report ID: 970760
- Weakness: Uncontrolled Resource Consumption
- Program: cs_money
- Disclosed At: 2020-11-05T11:05:47.954Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello Team,
      I had gone through your policy and I saw that DoS is out of scope but I am not sure about Application level DoS. The another reason to report  this attack because it affects  real customers who want to chat with your support team. I had tested this with two accounts 

1. From Account 1 I had tried to send 64K * 64K resolution image 
2. Simultaneously from Account 2 I had tried to  send normal image (with different Internet Connection).
3. The response was 502 for both images.

## Steps To Reproduce:
1.  Go to cs.money and login with Account1, Login Account2 on different device with different Internet Connection.
2.  Now Find Support symbol.
3.  Click on attachments and upload "lottapixel.jpg"  from Account1. 
4. Simultaneously upload normal image from Account2.  


## Supporting Material/References:
https://hackerone.com/reports/752073
https://hackerone.com/reports/752010
If you need more information please let me know.

  * [attachment / reference]
From: Device 1,  Account1 
Image "lottapixel.jpg" is Payload
Image "502.PNG" is proof of attack is successful.

From: Device 2, Account2
Image "upload timing from account2.png" and "Account2.png"  is proof that real users are also affected.

## Impact

Real User are not able to send images to the support team.  It affects to the availability  of resource.  I had recorded 1.2 min downtime. 
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
