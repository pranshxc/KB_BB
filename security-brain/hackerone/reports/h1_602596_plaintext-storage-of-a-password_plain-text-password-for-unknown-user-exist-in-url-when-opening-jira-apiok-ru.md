---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '602596'
original_report_id: '602596'
title: Plain text password for 'unknown' user exist in URL when opening jira.apiok.ru
weakness: Plaintext Storage of a Password
team_handle: ok
created_at: '2019-06-06T21:06:59.152Z'
disclosed_at: '2019-06-17T15:25:55.439Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: '*.ok.ru'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- plaintext-storage-of-a-password
---

# Plain text password for 'unknown' user exist in URL when opening jira.apiok.ru

## Metadata

- HackerOne Report ID: 602596
- Weakness: Plaintext Storage of a Password
- Program: ok
- Disclosed At: 2019-06-17T15:25:55.439Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Documentation at https://api.mail.ru/docs/guides/billing/ 
has a link to http://apiok.ru/jira/documents/ 
which redirects to https://jira.apiok.ru/secure/CreateIssue.jspa?pid=-2&os_username=unknown&os_password=X7:1OEh3

This pair of username & password - is effective login & password to JIRA system and allows to create new tickets/save filters/upload attachments (which can be used to provide malicious content)


I admit it can be incorrect realization of anonymouse tickets submission (which is possible at least since Fbe, 2016 https://confluence.atlassian.com/jirakb/how-to-allow-users-to-create-issues-anonymously-192551.html)

## Impact

Plain password text can help to undestand pattern of password generation for other accounts
Fishing is posible using official link to apiok.ru subdomain, i.e. http://jira.apiok.ru/secure/temporaryattachment/1585b6ba1084b134047a663dd8e698efc3a87e21/temp236609509878930861_test.png (and here can be png-bob for example which is accessible for everyone)

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
