---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1173436'
original_report_id: '1173436'
title: Default settings leak federated cloud id to lookup server of all users
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2021-04-23T19:30:51.314Z'
disclosed_at: '2021-06-10T13:41:03.219Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Default settings leak federated cloud id to lookup server of all users

## Metadata

- HackerOne Report ID: 1173436
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2021-06-10T13:41:03.219Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

So with the default settings Nextcloud still sends requests to the lookup server if users update their profile. Even if none of the fields are set to 'published'. 
I must admit this is somewhat of a surprise as there is no reason for this. As long as the visibility of none of the fields change and none of them are published. 

The background job is inserted in the function
https://github.com/nextcloud/server/blob/master/apps/lookup_server_connector/lib/UpdateLookupServer.php#L62

And the DELETE that is executed
https://github.com/nextcloud/server/blob/master/apps/lookup_server_connector/lib/BackgroundJobs/RetryJob.php#L156

Looking at the lookup server code it seems to actually do the delete. Still users of course can't verify what is running there. So we have to assume the worst case scenario where the lookup server has a list of a significant portion of all the nextcloud users out there.

## Impact

The nextcloud server is still sharing the federated cloud id of every user to the lookupserver. Unless an admin explicitly disables the lookupserver.
Even if non of the fields are set to published.

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
