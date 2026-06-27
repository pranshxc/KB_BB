---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '154529'
original_report_id: '154529'
title: 'Bookmarks: Delete all existing bookmarks of a user'
weakness: Privilege Escalation
team_handle: nextcloud
created_at: '2016-07-28T07:48:03.410Z'
disclosed_at: '2016-08-08T09:28:32.416Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- privilege-escalation
---

# Bookmarks: Delete all existing bookmarks of a user

## Metadata

- HackerOne Report ID: 154529
- Weakness: Privilege Escalation
- Program: nextcloud
- Disclosed At: 2016-08-08T09:28:32.416Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

A logical bug in the bookmark app makes it possible to delete all the existing bookmarks of the user. 

Here are the steps to reproduce: 
- Create  couple of valid bookmarks
- Import a bookmark.html file that contains the line **<a href="">Bookmark</a>**. All the bookmarks of the user is replaced with blank url and Bookmark as description. 
- This is potentially a risk where a user could be sent malicious html file to delete the bookmarks or this could even happen unintentionally if the user uploads a html with blank urls. 

The logical flaw resides in the method **/apps/bookmarks/controller/lib/bookmarks.php** -> **addBookmark**  where SQL query will select all the bookmarks and update them.

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
