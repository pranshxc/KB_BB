---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1379901'
original_report_id: '1379901'
title: CSRF on delete friend requests - Not protected with CSRF Token
weakness: Cross-Site Request Forgery (CSRF)
team_handle: xvideos
created_at: '2021-11-24T03:04:41.375Z'
disclosed_at: '2021-11-26T22:19:11.747Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 7
asset_identifier: www.xvideos.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on delete friend requests - Not protected with CSRF Token

## Metadata

- HackerOne Report ID: 1379901
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: xvideos
- Disclosed At: 2021-11-26T22:19:11.747Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:
Hello XVideos Security Team,

The is a possibility of CSRF on the POST method when deleting friend requests that are sent by the users. Any user can send the malicious contents to perform the post method in order to delete a friend request for a specific member.

## Steps To Reproduce:

  1. Login with your XVideos account and add the X user as a friend
  2. Go to your friends request sent and validate that the request is there on https://www.xvideos.com/account/friends/requests/sent 
  3. Select the user X that you want to delete then click on the button next to Cancel: "Checked" or "All"
  4. Intercept the request when the pop up message appear & after you click OK.
  5. Notice that this POST request to cancel the friend request is not protected by a CSRF token
  6. Using Burp Professional , right click on this request and under engagement tools select "Generate CSRF POC"
  7. Copy the HTML contents into a new HTML page as a proof of concept.
  8. Send this CSRF HTML page to the victim to delete the friend request of this specific X user
  9. Notice that the request deletes the Friend request.

## Supporting Material/References:
Refer to the attached video for more details

##Mitigation:
Add a CSRF token for the POST method to cancel or delete friend requests so it can be done only by the logged in user to confirm the activity.

## Impact

Attackers can send Victims this malicious content to victims to delete sent friend requests of specific users before they get accepted.

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
