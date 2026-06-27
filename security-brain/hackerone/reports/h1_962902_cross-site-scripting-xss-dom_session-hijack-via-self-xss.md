---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '962902'
original_report_id: '962902'
title: Session Hijack via Self-XSS
weakness: Cross-site Scripting (XSS) - DOM
team_handle: rocket_chat
created_at: '2020-08-20T03:22:36.914Z'
disclosed_at: '2021-01-17T16:51:18.491Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Session Hijack via Self-XSS

## Metadata

- HackerOne Report ID: 962902
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: rocket_chat
- Disclosed At: 2021-01-17T16:51:18.491Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** It's possible to hijack a session by tricking the user to perform a Self-XSS on the drag and drop functionality in the chat.

**Description:** Self-XSS is an underrated vulnerability that can have a harmful impact on the users of the application like here, after we get access to the user's session we can read chats, change (some) info and lock the account by activating the 2FA.  

## Releases Affected:

  * Tested on 3.5.2 and 3.5.3 (current version)

## Steps To Reproduce:

  1. Serve the image (payload) using Python's HTTP server.
  1. Trick the user to drag and drop the image inside a chat.
  1. Get the **Meteor.loginToken** from the server logs.
  1. Open that instance of Rocket Chat in a browser.
  1. Add the **Meteor.loginToken** as an item in the local storage.
  1. The site automatically redirects to the session.
  1. Profit!

## Supporting Material/References:

  * GIF file explaining the PoC.
  * HTML file with the payload.

## Suggested mitigation

  * Sanitize the drag and drop functionality of chat text box striping the tags.

## Impact

The attacker can gain access to the user session and read chats, change (some) info and lock the account by activating the Two-Factor Authentication, even alter the server configuration depending on the account privileges.

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
