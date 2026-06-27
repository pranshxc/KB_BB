---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145355'
original_report_id: '145355'
title: Stored XSS on Share-popup of a directory's Gallery-view
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-06-17T11:35:04.019Z'
disclosed_at: '2016-07-19T12:51:26.649Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on Share-popup of a directory's Gallery-view

## Metadata

- HackerOne Report ID: 145355
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2016-07-19T12:51:26.649Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
Nice with the program launch! Congrats!

I noticed that there was a Share-icon when toggling to the Gallery-view of a directory under "Nextcloud Files":
{F99938}

If your directory has a malicious name such as a HTML-payload: `<img src=x onerror=alert(1)>`, this HTML will run when clicking on the Share-icon:
{F99937}

I see that you have a proper CSP in place, but remember that Internet Explorer is not there yet:
{F99939}

Also, since any user could create files, a user could potentially execute this for an admin (if that admin is not using a CSP-supported browser that is).

Let me know if you need more information.

Regards,
Frans

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
