---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '674866'
original_report_id: '674866'
title: Conversation API Leaks Details Of UnAuthorized Conversations
weakness: Improper Access Control - Generic
team_handle: vanilla
created_at: '2019-08-16T06:40:48.969Z'
disclosed_at: '2020-03-25T19:41:33.034Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/vanilla/community
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Conversation API Leaks Details Of UnAuthorized Conversations

## Metadata

- HackerOne Report ID: 674866
- Weakness: Improper Access Control - Generic
- Program: vanilla
- Disclosed At: 2020-03-25T19:41:33.034Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

If a user creates a conversations, and then leaves, all API calls and web access to that conversation is locked down. Except for one particular API call which allows you to see details about ongoing conversations you have since left as long as you created the conversation in the first place. 

## Steps to reproduce:

1. Ensure that the "member" role has API Token access. 
2. Create a new user with this role, and send a conversation to anyone. 
3. Leave said conversation. 
4. On the web/API calls to read this conversation and message should fail. However you should still be able to do the following API call : 
https://vanilla.com:444/api/v2/conversations/?insertuserid=yourUserId&access_token=accessToken
Which leaks details like who has been added to the conversation after you left, extra messages etc. 

## Code Details

I noticed that *most* calls to conversations run through the method `inConversation` which checks whether a user is *still* in the conversation, and if they have left they don't have access to it. But I assume this was too heavy to run in this particular API call because it returns a list. 

For this particular API call if you don't pass in the `insertuserid` param, then it will indeed check the userconversation table and make sure you are still participating in the conversation. But if you pass in `insertuserid` it instead bypasses this check and just returns all conversations you started, irrespective if you are still in them.

## Impact

Gain information about conversations they no longer have access to.

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
