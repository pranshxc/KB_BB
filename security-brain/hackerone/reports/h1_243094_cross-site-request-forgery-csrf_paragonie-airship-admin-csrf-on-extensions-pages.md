---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243094'
original_report_id: '243094'
title: Paragonie Airship Admin CSRF on Extensions Pages
weakness: Cross-Site Request Forgery (CSRF)
team_handle: paragonie
created_at: '2017-06-25T20:55:09.292Z'
disclosed_at: '2017-10-16T05:48:14.764Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Paragonie Airship Admin CSRF on Extensions Pages

## Metadata

- HackerOne Report ID: 243094
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: paragonie
- Disclosed At: 2017-10-16T05:48:14.764Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
==========

The /bridge/admin/skyport/install endpoint, as well as some of the endpoints around it, are vulnerable to Cross-Site Request Forgery.

Description
=========
The functions in src/Cabin/Bridge/Controller/Skyport.php in the Airship project appear to all be vulnerable to Cross-Site Request Forgery.

I would have put this as a high, but from my code review it appears that not all of these functions actually work - for example, the installPackage function appears to passing a bash script to the "php" command, which just ends up printing the bash script. Code review can be misleading, so I may be wrong about it not working.

I put this as a medium because, if the logic actually does work (or works sometime in the future), then the ability to install packages is the kind of thing that has the potential to be converted into an RCE.

Please revise the severity as you see fit - I don't know your product well enough to do a proper assessment.

Proof of Concept
======
I have attached a simple file which I was able to use to demonstrate the CSRF against airship running in a docker instance. It appears that the extra password-protection of extensions is not enabled by default, although that may be just my developer setup.

See the attached csrf.html. The attached screenshot shows the result that was returned from the server after clicking the submit button in the attached file.

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
