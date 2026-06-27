---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '337189'
original_report_id: '337189'
title: Tracking Bitwarden firefox addon users
team_handle: bitwarden
created_at: '2018-04-13T09:21:24.054Z'
disclosed_at: '2018-05-23T17:31:30.197Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/
asset_type: OTHER
max_severity: critical
tags:
- hackerone
---

# Tracking Bitwarden firefox addon users

## Metadata

- HackerOne Report ID: 337189
- Weakness: 
- Program: bitwarden
- Disclosed At: 2018-05-23T17:31:30.197Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Firefox web extension, generate a UUID for each web-extension and is specific to a user. Unlike chrome extensions. 
Which means whenever the user installs Bitwarden on Firefox, it generates a different extension ID for each user.
You can check the extension ID by about:debugging -> under extensions.

The problem occurs when Bitwarden prompts the user with the message:
 `Should Bitwarden remember this password for you?`.  [Screenshot attached]

This prompt is loaded as a local resource from `moz-extension://UUID/bar.html?add=1`, and this can be easily read by the website and any Javascript running on that page.

## Impact

Now, because this is UUID is unique to each user, it is a potential userID which can be used for tracking a user:
1. That a user is a Bitwarden user.
2. Multiple accounts used by the user across normal windows, private windows, containers.
3. Because this ID can also be read by a third-party javascript on the page:
    A.com/login.html has a third-party T.com
    B.com/login.html has a third-party T.com
Now because T.com can also read the UUID for Bitwarden, T.com can on their backend track that it's the same user visiting A.com and B.com. It will not matter whether the user has third-party cookies disabled or not, or is using some tracking protection. Hence, Bitwarden infects the browser ecosystem and breaks the privacy protections / private browsing mode.

This ID is accessible and remains same irrespective of :
- Private mode
 -Normal mode
- After browser restart
- Extension update.
- Clearing History / Local storage

The only way to remove this UUID is by deleting and re-installing the extension.

I am happy to help you with more concrete examples if needed. 
As a demo:
1. Firefox with Bitwarden extension installed.
2. Visit the page: https://cdn.cliqz.com/browser-f/fun-demo/tracking-bw-users.html

This is a known issue with Firefox webextensions you can find the details here:
https://bugzilla.mozilla.org/show_bug.cgi?id=1372288

As far as I can see, this needs to fixed at the extension level and not at Firefox level.

Please note, as of now I have only tested the resource loaded from this prompt. But this would be a problem anywhere the resource being loaded which is using the same pattern.

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
