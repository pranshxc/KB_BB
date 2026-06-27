---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '205360'
original_report_id: '205360'
title: Content-Injection/XSS ████
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2017-02-10T21:22:56.618Z'
disclosed_at: '2019-12-02T18:39:38.310Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Content-Injection/XSS ████

## Metadata

- HackerOne Report ID: 205360
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:39:38.310Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hi,

It is possible to inject content and vulnerable to reflected Cross Site Scripting.
Affected domain: https://██████████
Used browser: Mozilla.


## Impact

One of the most common XSS attack vectors is to hijack legitimate user accounts by stealing their session cookies. This allows attackers to impersonate victims and access any sensitive information or functionality on their behalf. Let's dissect how this can be achieved.

An attacker could inject fake login forms and ask for military credentials.

## Step-by-step Reproduction Instructions

1. XSS: https://██████/images.ashx?loc=%3C/div%3E%3Cimg%20src=%22youtube.com%22%20onerror=alert(%22TestingXSS%22)%3E

2. Content Injection: https://██████/images.ashx?loc=%3C/div%3E%3Cimg%20src=%22https://███.files.wordpress.com/2016/12/facebook-instagram-open-redirect.jpeg%22%3E

## Suggested Mitigation/Remediation Actions

Sanitize your input, by escaping HTML special characters.

Thanks,
Diogo Real

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
