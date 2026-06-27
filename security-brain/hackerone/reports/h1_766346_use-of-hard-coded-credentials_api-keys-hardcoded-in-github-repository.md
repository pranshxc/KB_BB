---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '766346'
original_report_id: '766346'
title: API Keys Hardcoded in Github repository
weakness: Use of Hard-coded Credentials
team_handle: rocket_chat
created_at: '2019-12-31T07:33:46.350Z'
disclosed_at: '2020-04-01T13:49:25.364Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- use-of-hard-coded-credentials
---

# API Keys Hardcoded in Github repository

## Metadata

- HackerOne Report ID: 766346
- Weakness: Use of Hard-coded Credentials
- Program: rocket_chat
- Disclosed At: 2020-04-01T13:49:25.364Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** API Keys is hard coded in one of the GitHub repository

**Description:** Key and google-services.json file is publically available in the RocketChat Android repository. 

## Releases Affected:

 * Latest Github Code

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)

**Fabric API Key**
 
  1. Go to this URL https://github.com/RocketChat/Rocket.Chat.Android/blob/638759d7b77375fd681f429d2e2d7ba59e602c45/app/src/main/AndroidManifest.xml
  2. Scroll down to the bottom
  3. You will see fabric APIKey hardcoded there

**google-services.json**

 1. Go to https://github.com/RocketChat/Rocket.Chat.Android/blob/30e95cc97d2fbec6c1d5f6fdad7350fbf60688d5/app/google-services.json
 2. You can see the complete google services config file


## Supporting Material/References:

  * Screenshot in attachment

## Suggested mitigation

  * Keys should not be pushed to the public repository

## Impact

1. Using Fabric key some attacker can mess up the complete analytics of the RocketChat Android App 
2. google-services.json can be used to access google services of RocketChats google account

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
