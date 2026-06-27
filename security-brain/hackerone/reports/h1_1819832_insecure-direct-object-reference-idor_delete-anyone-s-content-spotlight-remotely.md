---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1819832'
original_report_id: '1819832'
title: Delete anyone's content spotlight remotely.
weakness: Insecure Direct Object Reference (IDOR)
team_handle: snapchat
created_at: '2023-01-01T16:06:51.521Z'
disclosed_at: '2023-03-06T21:32:15.042Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 694
asset_identifier: accounts.snapchat.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Delete anyone's content spotlight remotely.

## Metadata

- HackerOne Report ID: 1819832
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: snapchat
- Disclosed At: 2023-03-06T21:32:15.042Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Snapchat,
 Snapchat has viral video feature callled spotlight which alone was the biggest trend and increase snapchat users and profit in millions.
I found a way to delete anyone's spotlight remotely.

Please see the below poc:-

1. First go to https://my.snapchat.com/myposts and log in there.
2. You will see your posts .
3. Now turn burp suite and intercept.
4.Select any of your posts and click delete option.
5. Now capture the delete request. In delete request there is parameter of id


{"operationName":"DeleteStorySnaps","variables":{"ids":["███████"],"storyType":"SPOTLIGHT_STORY"},"query":"mutation DeleteStorySnaps($ids: [String!]!, $storyType: StoryType!) {\n  deleteStorySnaps(ids: $ids, storyType: $storyType)\n}\n"}

6. You just have to change this id parameter. You can easily get the id parameter. Now forward the request after replacing id with someone's else video id.

And the video of other user will get delete.

HOW TO GET ID PARAMETER

1. Whenever you share spotlight you can see the parameter in the url as:
https://story.snapchat.com/spotlight/█████


I have attached a video POC please check it out

## Impact

Delete anyone's Content Spotlight. Imagine deleting video biggest influencers and content creators.

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
