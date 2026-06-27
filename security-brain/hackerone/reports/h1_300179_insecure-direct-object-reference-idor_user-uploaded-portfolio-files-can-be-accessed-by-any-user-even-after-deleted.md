---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300179'
original_report_id: '300179'
title: User uploaded portfolio files can be accessed by any user even after deleted
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mavenlink
created_at: '2017-12-23T08:01:43.798Z'
disclosed_at: '2019-02-27T23:40:35.604Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# User uploaded portfolio files can be accessed by any user even after deleted

## Metadata

- HackerOne Report ID: 300179
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mavenlink
- Disclosed At: 2019-02-27T23:40:35.604Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Reproduction:
=========

1. Login as a user, e.g: user1
2. Create a portfolio by going to https://app.mavenlink.com/users/1234567-user1/work_samples/new
note: replace 1234567-user1 with the actual user id/name endpoint.
3. Uploading any file to the new portfolio and click save. On the right side of profile info, you will see the created portfolio with attached file,
4. Click on the file, notic the link is https://app.mavenlink.com/attachments/xxxxxxxx Where xxxxxxxx is the file ID in 8 number lenght.
5. Copy the file link and open it in other browser with different login user, e.g: user2, you will see the file is accessible.
6. On user1, delete the file/portfolio.
7. The link is still accessible,

This is my uploaded portfolio file: https://app.mavenlink.com/attachments/79279255 (I've delete all the portfolio on the web interface),

Recommend fix:
- Provide mechanism to check if the uploaded file link is associated with coresponding account.
- Delete the uploaded file (in AWS?) with portfolio as user desired.

## Impact

As user profile and portfolio (with files) can only seen if the user is in the same team/group, otherwise the information should be private, as going throgh any profile link (https://app.mavenlink.com/profiles/[user-id]) getting "Private Profile" message

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
