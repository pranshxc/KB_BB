---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1215251'
original_report_id: '1215251'
title: Bypass of privacy filter / tracking pixel blocker
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2021-06-02T09:59:35.702Z'
disclosed_at: '2021-08-11T09:21:17.590Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: nextcloud/mail
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Bypass of privacy filter / tracking pixel blocker

## Metadata

- HackerOne Report ID: 1215251
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2021-08-11T09:21:17.590Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
------------

When the mail app receives inline images, it will block them for privacy reasons to prevent tracking pixels (`The images have been blocked to protect your privacy`).

This block works correctly for most remote resources (in addition to images, remote CSS files, iframes, and some CSS attributes are also blocked). 

However, it is still possible to inject images via some CSS attributes (specifically, `list-style-image` and `background-image`), thus bypassing the block and enabling tracking of users.


POC
---

Send a mail with the following body to an email address that is connected to Nextcloud Mail (the HTML code can for example be sent via thunderbird by clicking insert -> HTML):

```
    <style>
        big {
            background-image: url(https://www.google.com/logos/doodles/2021/celebrating-frank-kameny-6753651837108392-l.png);

        }
        ul {
            list-style-image: url(https://www.google.com/logos/doodles/2021/celebrating-frank-kameny-6753651837108392-l.png);
        }
    </style>
    <big>test</big>

    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
```

Open the message to see that the remote image is included directly, bypassing the privacy filter. An attacker can now replace `www.google.com` with a log server they control to log when users open the mail.

## Impact

bypass of image privacy filter which prevents tracking scripts from gathering users IP addresses and information on when they view an email.

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
