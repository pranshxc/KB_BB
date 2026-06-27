---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '912865'
original_report_id: '912865'
title: Stored XSS at https://app.smtp2go.com/settings/users/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: smtp2go-vdp
created_at: '2020-07-01T09:43:55.841Z'
disclosed_at: '2020-07-02T01:37:58.253Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
asset_identifier: app.smtp2go.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS at https://app.smtp2go.com/settings/users/

## Metadata

- HackerOne Report ID: 912865
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: smtp2go-vdp
- Disclosed At: 2020-07-02T01:37:58.253Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability :
A. Type:- Cross Site Scripting (Stored) 
B. Description:- Stored XSS, also known as persistent XSS, is the more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application.
Summary :
When you will create a particular user you will have to enter username and you can enter Xss payload than on webhooks it will fire that XSS.
As the website is not filtering the input provided by the user, that's why this problem is there.
Thank You.
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Create an account https://app.smtp2go.com and LOG IN using username and password.
  2. After that you will be redirected to dashboard and click on settings and then click on SMTP users.
  3. Click on Add SMTP USER and enter &#00;</form><input type&#61;"date" onfocus="alert(1)"> this payload on username and save it.
 4. After that down below click on webhooks and then continue and then ADD WEBHOOK and then from users select that user which we had created earlier and it will fire the pop up.  
I had attached the PoC you can see it.

## Supporting Material/References:


  * [attachment / reference]

## Impact

If one of these users executes malicious content, the attacker may be able to perform privileged operations on behalf of the user or gain access to sensitive data belonging to the user such as steal Cookies of user,etc.

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
