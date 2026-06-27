---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1987011'
original_report_id: '1987011'
title: '[Hubs] - Broken access control in placing objects in hubs room'
weakness: Improper Access Control - Generic
team_handle: mozilla
created_at: '2023-05-13T17:46:15.255Z'
disclosed_at: '2023-07-20T12:33:49.622Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 80
asset_identifier: hubs.mozilla.com
asset_type: URL
max_severity: none
tags:
- hackerone
- improper-access-control-generic
---

# [Hubs] - Broken access control in placing objects in hubs room

## Metadata

- HackerOne Report ID: 1987011
- Weakness: Improper Access Control - Generic
- Program: mozilla
- Disclosed At: 2023-07-20T12:33:49.622Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear team,

First of all, thank you for all the support you already have provided. I hope the migration to HackerOne is not too hard and wish you all of the best!

This was orginally submitted on the bug bounty service of Mozilla itself: https://bugzilla.mozilla.org/show_bug.cgi?id=1829735

## Summary:
In the settings of a hub, an admin user can disable the creation  an object or move deny to move any object. I found out that this is bypassable with the usage of certain `/<commands>` inside the chat feature. An attacker does not to be authenticated nor have joined the room to perform this attack. With some JavaScript magic, we can trick the browser thinking we are in the room, which we are not.

## Requirements:
* Two different browsers - for two accounts
 * Browser A : Admin that creates a room
* Browser B: Attacker

## Setup
You can skip the setup, if you want and make use of my instance: https://quikke.dev.myhubs.net/eE97EwL/quikke-test-server
1. In Browser A, go to https://hello.dev.myhubs.net/
2. Sign in & Create a room
3. Join the room
4. Click on the three dots in the right corner (More)
5. Room info and settings and click on edit (top right)
6. Disable the below listed settings:
   * Create and move objects
   * Pin objects

{F2351238}
7.Click on Apply

## Steps To Reproduce:
In Browser B, go to the room created by the attacker or you can use mine: https://quikke.dev.myhubs.net/eE97EwL/quikke-test-server . Join the meeting and noticed that only the Chat option is available. Open the chat and follow the below steps to create different objects with different settings:

###Add command -  spawn object
= Spawn a duck into the hub as a none admin. Users will still have the ability to open a menu to delete the duck
  1. Enter the following in the chat `/add https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb`

{F2351241}

###Add command -  spawn object with--no-menu flag
= Spawn a duck into the hub as a none admin that cannot be removed
  1. Enter the following in the chat `/add --no-menu https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb`

{F2351244}

###Add command Youtube video --no-menu
= Add a youtube video into the hub as a none admin that cannot be removed
  1. Enter the following in the chat `/add --no-menu https://www.youtube.com/watch?v=dQw4w9WgXcQ`

{F2351250}

**Note** The video cannot be stopped and spawned unlimited amount of times. Nor can the video be removed.

## Extra - Spectator
The same can also be done via spectator that did not join the room. In the JS file: webpack://hubs/src/message-dispatch.js , the following lines are just checked client side:

```javascript
dispatchCommand = async (command, ...args) => {
    const entered = this.scene.is("entered");
    uiRoot = uiRoot || document.getElementById("ui-root");
    const isGhost = !entered && uiRoot && uiRoot.firstChild && uiRoot.firstChild.classList.contains("isGhost");

    // TODO: Some of the commands below should be available without requiring room entry.
    if (!entered && (!isGhost || command === "duck")) {
      this.log(LogMessageType.roomEntryRequired);
      return;
    }
```

When enabling the debugging modus in Chrome browser, we are able to set `const entered = this.scene.is("entered");` to `const entered=true`. This will allows us to execute all above commands without entering the room. 

## Extra - SSRF
When adding our own server to the `/add` command, we can see several pingbacks coming in from the backend:

{F2351261}

Currently, still figuring out if this can be further exploited.

## Impact

An attacker is able to place different kinds of objects while the admin user specifically disables the creation of objects inside the room. The server does not validate the access control rules of the room when calling the websockets requests to create an object.

Example:
When you join the discord of the Mozilla Hubs community, you will notice that there are different online events are organised to show digital art. With this, an attacker could disturb the reputation of these artists. 

Let me know if there is anything unclear,

Quikke

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
