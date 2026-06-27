---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1092831'
original_report_id: '1092831'
title: Password reset token leak via "Host header"  on third party website
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2021-02-02T12:35:57.481Z'
disclosed_at: '2022-02-10T19:41:36.730Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: Shopify Third Party Store
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password reset token leak via "Host header"  on third party website

## Metadata

- HackerOne Report ID: 1092831
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2022-02-10T19:41:36.730Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,

#Product / URL
https://your-store.wholesale.shopifyapps.com/

#Description
It has been identified that the application is leaking Token to third party sites. In this case it was found that the Token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the reset password of user.


#Reproduction Instructions /
1) Send reset password link to your email address.
2)Now go to email, turn burp suite intercept on and click on reset password link. Check for the requests having the token in "host" as third party website. And copy the link
3)Now turn intercept off and reset the password.(with that link)
4)Now reset the password.

#Proof of Concept
F1180911

#Additional Information:
Note also that if users can author content within the application then an attacker may be able to inject links referring to a domain they control in order to capture data from URLs used within the application.

## Impact

As you can see in the `Host` the reset token is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can Use the Token easily.

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
