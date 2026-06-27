---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5933'
original_report_id: '5933'
title: Multiple Issues related to registering applications
weakness: Violation of Secure Design Principles
team_handle: coinbase
created_at: '2014-04-05T09:03:16.501Z'
disclosed_at: '2014-05-29T01:07:30.884Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Multiple Issues related to registering applications

## Metadata

- HackerOne Report ID: 5933
- Weakness: Violation of Secure Design Principles
- Program: coinbase
- Disclosed At: 2014-05-29T01:07:30.884Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

On the page https://coinbase.com/oauth/applications, an authenticated coinbase user can create an application and successfully submit it to the app gallery. 
 
After submitting, the app is pending review to be approved. However, while the app is in review, the coinbase user can send a URL (something like https://coinbase.com/apps/533fb2cb6e90eb79b9000103) to access the app to other users directly. In other words, the app is accessible to other users even without being reviewed by the coinbase team. The coinbase user might have malicious intentions and can trick other users to install the malicious app. 

Other users can also leave their reviews on this application. 

Lastly, after submitting an app for approval, there is an option to upload screenshots. There did not seem to be any restrictions on the kind of files that can be uploaded. I was able to upload an executable and I got a message saying it was successfully uploaded. I could not verify it because I believe it will only be visible once approved.

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
