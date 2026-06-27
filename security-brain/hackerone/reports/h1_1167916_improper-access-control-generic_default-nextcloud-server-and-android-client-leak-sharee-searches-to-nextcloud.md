---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1167916'
original_report_id: '1167916'
title: Default Nextcloud Server and Android Client leak sharee searches to Nextcloud
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2021-04-18T18:12:19.132Z'
disclosed_at: '2021-06-15T19:11:31.101Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Default Nextcloud Server and Android Client leak sharee searches to Nextcloud

## Metadata

- HackerOne Report ID: 1167916
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2021-06-15T19:11:31.101Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

On a clean Nextcloud setup the functionality "Search global and public address book for users" is enabled.

Now when searching for a sharee to share with. The lookup parameter is not passed to the server. Resulting in
https://github.com/nextcloud/server/blob/master/apps/files_sharing/lib/Controller/ShareesAPIController.php#L144

the lookup being true. So the lookup server of Nextcloud will be searched by default.
It seems that the lookup server is down now. But this seems to be an error I assume?

## Impact

Anybody sharing trough the android app. Leaks their sharee searches to the Nextcloud lookup server.
Now the server can can only see the origin Nextcloud server (or rather the IP of that). Still. This should not be leaked by default.

On the web and desktop there is first a local search. And only if the user explicitly presses the search globally the lookup server is queried. (to be fair this could also be more clear that it actually sends data to other systems)

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
