---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158554'
original_report_id: '158554'
title: Hyperlink Injection in Friend Invitation Emails
weakness: Open Redirect
team_handle: instacart
created_at: '2016-08-11T19:23:55.377Z'
disclosed_at: '2016-09-12T19:59:24.395Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- open-redirect
---

# Hyperlink Injection in Friend Invitation Emails

## Metadata

- HackerOne Report ID: 158554
- Weakness: Open Redirect
- Program: instacart
- Disclosed At: 2016-09-12T19:59:24.395Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description

A user can change their name to a URL in order to send email invitations containing malicious hyperlinks.

# Steps to Reproduce

1. Create a new Instacart account with the first name `http://example.com`
2. Navigate to [https://www.instacart.com/store/referrals](https://www.instacart.com/store/referrals)
3. Send an email invitation to an email address that you control

You will receive a new email with the first word being a link to a potentially malicious site.

# Consequences

This permits users to send malicious/phishing links to potential clients. It could also have an effect on how spam filters treat `instacart.com` emails.

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
