---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129862'
original_report_id: '129862'
title: Stored XSS on [your_zendesk].zendesk.com in Facebook Channel
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2016-04-11T16:27:13.292Z'
disclosed_at: '2016-06-01T21:16:03.496Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on [your_zendesk].zendesk.com in Facebook Channel

## Metadata

- HackerOne Report ID: 129862
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2016-06-01T21:16:03.496Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have found a stored XSS in the Facebook Channel options at ```https://[your_zendesk].zendesk.com/agent/admin/facebook/facebook_auth```.

The XSS is a result of improperly escaping Facebook Page names.

Steps to reproduce
-------------------------

1. Create a facebook page with the following title/page name:

    ```Foobar" onmouseover=location&#x3d;'javascript:alert\x28document.domain\x29'```

    (I had to play around with this a bit to get it working correctly as Facebook has strict policies on the page name. If the page already exists, try to replace `Foobar` with any other random string)
2. Create your own zendesk account and then go to ```https://[your_zendesk].zendesk.com/agent/admin/facebook/facebook_auth``` to add a facebook page.
3. After adding the page created in Step 1, hover over the "Unlink" button to trigger the XSS. See also attached screenshot.

Attack scenario
--------------------
Obviously anyone with the permissions to add facebook pages can trigger this stored XSS and attack the admins with the usual XSS attacks.

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
