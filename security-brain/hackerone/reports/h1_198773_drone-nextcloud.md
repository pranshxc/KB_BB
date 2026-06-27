---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198773'
original_report_id: '198773'
title: Drone Nextcloud
team_handle: nextcloud
created_at: '2017-01-16T16:55:07.885Z'
disclosed_at: '2017-02-12T19:28:53.973Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
---

# Drone Nextcloud

## Metadata

- HackerOne Report ID: 198773
- Weakness: 
- Program: nextcloud
- Disclosed At: 2017-02-12T19:28:53.973Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Greetings,

On drone : https://drone.nextcloud.com

We observe this :
----

{F152818}

I noticed that it's possible to alter the url to write what you want :
----

   https://drone.nextcloud.com/rbcafe/settings/settings/badges

{F152817}

In fact it could be anything :
----

   https://drone.nextcloud.com/lonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnlonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn/settings/settings/badges

{F152819}

The default value of the url can be extracted with a google-dorking on drone.nextcloud.com : inurl:drone.nextcloud.com

- https://drone.nextcloud.com/nextcloud/updater
- https://drone.nextcloud.com/nextcloud/server/settings/badges

Using this we can find new data :
-------------------------------

https://drone.nextcloud.com/nextcloud/server/

{F152820}

https://drone.nextcloud.com/nextcloud/server/4182/1

{F152821}

Buttons Follow and restart are fully clickable, but there is no purpose because, I'm not logged In. Regarding the screenshot in the first observation (F152818), pages should be blocked and remains protected if the login is not valid. The paths should also remains protected from indexation.

Best regards
@Rbcafe

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
