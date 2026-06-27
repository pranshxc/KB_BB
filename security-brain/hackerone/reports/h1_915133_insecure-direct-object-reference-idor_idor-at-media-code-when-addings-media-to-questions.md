---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '915133'
original_report_id: '915133'
title: IDOR at 'media_code' when addings media to questions
weakness: Insecure Direct Object Reference (IDOR)
team_handle: automattic
created_at: '2020-07-04T03:53:42.237Z'
disclosed_at: '2020-11-18T14:22:27.150Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR at 'media_code' when addings media to questions

## Metadata

- HackerOne Report ID: 915133
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: automattic
- Disclosed At: 2020-11-18T14:22:27.150Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
When you add a question to your survey and click `Save`, it sends this request :
{F893416}

In this request, `media_code` is vulnerable for IDOR. If you change it to any media ID, you will see it on your question. 
And these IDs are sequential. So you can access to any user's media contents. 

## Steps To Reproduce:

  1. Create a survey
  1. Add any question like `Free Text` and open your proxy program
  1. Click to question and click `Save` 
  1. Your proxy program will catch the request
  1. Change the `media_code` parameter's value to a 7 digit number. Like `2013124` (my media content)
  1. Send the request, you will see the victim's media.

## Impact

Access to user's media contents

Thanks,
Bugra

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
