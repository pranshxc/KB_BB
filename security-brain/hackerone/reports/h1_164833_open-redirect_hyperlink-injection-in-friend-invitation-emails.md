---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164833'
original_report_id: '164833'
title: Hyperlink Injection in Friend Invitation Emails
weakness: Open Redirect
team_handle: algolia
created_at: '2016-08-31T20:08:40.066Z'
disclosed_at: '2016-10-07T11:35:54.715Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- open-redirect
---

# Hyperlink Injection in Friend Invitation Emails

## Metadata

- HackerOne Report ID: 164833
- Weakness: Open Redirect
- Program: algolia
- Disclosed At: 2016-10-07T11:35:54.715Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description 

A user can change their last name to a URL in order to send email invitations containing malicious hyperlinks.

## Steps to Reproduce
1. Create a new Algolia account with the last name `http://example.com`.
2. Navigate to `My Account > Referrral`
3. Send an invitation to an email address that you control

You will receive a new email with the last name being a link to a potentially malicious site.

## Consequences
This permits users to send malicious/phishing links to potential clients. It could also have an effect on how spam filters treat algolia.com emails.

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
