---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '386614'
original_report_id: '386614'
title: Slack Token exposed over internet (Github)
weakness: Cleartext Storage of Sensitive Information
team_handle: rocket_chat
created_at: '2018-07-25T09:15:44.993Z'
disclosed_at: '2019-07-11T13:58:21.854Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Slack Token exposed over internet (Github)

## Metadata

- HackerOne Report ID: 386614
- Weakness: Cleartext Storage of Sensitive Information
- Program: rocket_chat
- Disclosed At: 2019-07-11T13:58:21.854Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** Slack token is exposed in public github​ repositoty​ 

**Description:** [This file](https://github.com/RocketChat/RCMarkdownParser/blob/1b8a052bcd38bcf459ecb6bb644daa7d70769434/.travis.yml) on one of your github​ repos contains a Slack token for the R​ocketChat​ account.

As noted in the official documentation, if this is to be published, it should be encrypted, which isn't the case here.

## Releases Affected:

RCMarkdownParser file on the latest github​ master branch

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)
 
1. Go to https://github.com/RocketChat/RCMarkdownParser/blob/1b8a052bcd38bcf459ecb6bb644daa7d70769434/.travis.yml
2. Notice the slack token present which can be used to access the account and communications.

## Supporting Material/References:

Screenshot attached.

## Suggested mitigation

Remove the slack token from the repo and also from the history

## Impact

The token can be used to control the account and read internal communications.

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
