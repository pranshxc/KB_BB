---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1173411'
original_report_id: '1173411'
title: Nextcloud update checks leaks information
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2021-04-23T18:40:54.418Z'
disclosed_at: '2021-05-01T10:53:03.940Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Nextcloud update checks leaks information

## Metadata

- HackerOne Report ID: 1173411
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2021-05-01T10:53:03.940Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

I think this is more of a privacy concern than a security concern. However I wanted to check here first. Please direct me to an other suitable location if needed.

It is in relation to https://github.com/nextcloud/server/blob/master/lib/private/Updater/VersionCheck.php#L78

This is sending several things related to servers to Nextcloud. Especially the 'installedat' seems to have a very high likely hood to be unique for an instance. Allowing Nextcloud to track instances when doing the requests.

I especially wonder why you chose this method here. Instead of the 'appstore' approach were you just have an big blob and have the server figure everything out.

Other than that I could not find any mention about what data is send to Nextclouds servers and why.  One could argue that pinging the updates.nextcloud.com has a legitimate reason. However I doubt that regarding the more track sensitive information. And even then it would be OK if you'd communicate about this clearly.

Again sorry if this is the wrong place. But I didn't wanna post this publicly if it is in any way sensitive.

## Impact

This could potentially cause legal issues if you are sending data that is not needed and identifiable.

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
