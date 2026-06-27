---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '232994'
original_report_id: '232994'
title: API Does Not Apply Access Controls to Translations
weakness: Improper Access Control - Generic
team_handle: weblate
created_at: '2017-05-29T23:17:30.883Z'
disclosed_at: '2017-06-02T11:23:24.335Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-access-control-generic
---

# API Does Not Apply Access Controls to Translations

## Metadata

- HackerOne Report ID: 232994
- Weakness: Improper Access Control - Generic
- Program: weblate
- Disclosed At: 2017-06-02T11:23:24.335Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary
=======

The /api/ does not enforce access control on the translation files, allowing anyone to download full translation files. See the screenshot for an example project being viewed by an anonymous account that is configured to have no permissions.

Description
=======
On my local setup running Weblate 2.15-dev, I removed all permissions from the Guest group and restarted the server. When I tried to navigate to the test project through the UI the usual way at URL http://192.168.1.129:8000/projects/testproject/, I received an Access Denied message.

However I was able to find the project details through the API at http://192.168.1.129:8000/api/components/testproject/testcomponent/translations/ and even download the translations file by clicking on the "file_url" link, which in my case is "http://192.168.1.129:8000/api/translations/testproject/testcomponent/en_CA/file/".

Assessment
=======
I am marking this as Medium because from what I have seen the access controls are not that important to Weblate's mission and it does not seem designed to keep translations secret, although the existence of access controls through the web app suggests that this is something that people wanted enough to implement. If enforcing the read access controls is of any importance, then I would treat this with higher severity.

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
