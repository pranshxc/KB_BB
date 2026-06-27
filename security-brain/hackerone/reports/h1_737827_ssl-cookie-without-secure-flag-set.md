---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737827'
original_report_id: '737827'
title: SSL cookie without secure flag set
team_handle: stripo
created_at: '2019-11-15T17:04:57.380Z'
disclosed_at: '2020-10-13T13:38:04.844Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# SSL cookie without secure flag set

## Metadata

- HackerOne Report ID: 737827
- Weakness: 
- Program: stripo
- Disclosed At: 2020-10-13T13:38:04.844Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Issue background
If the secure flag is set on a cookie, then browsers will not submit the cookie in any requests that use an unencrypted HTTP connection, thereby preventing the cookie from being trivially intercepted by an attacker monitoring network traffic. If the secure flag is not set, then the cookie will be transmitted in clear-text if the user visits any HTTP URLs within the cookie's scope. An attacker may be able to induce this event by feeding a user suitable links, either directly or via another web site. Even if the domain that issued the cookie does not host any content that is accessed over HTTP, an attacker may be able to use links of the form http://example.com:443/ to perform the same attack.
To exploit this vulnerability, an attacker must be suitably positioned to eavesdrop on the victim's network traffic. This scenario typically occurs when a client communicates with the server over an insecure connection such as public Wi-Fi, or a corporate or home network that is shared with a compromised computer. Common defenses such as switched networks are not sufficient to prevent this. An attacker situated in the user's ISP or the application's hosting infrastructure could also perform this attack. Note that an advanced adversary could potentially target any connection made over the Internet's core infrastructure.
Issue remediation
The secure flag should be set on all cookies that are used for transmitting sensitive data when accessing content over HTTPS. If cookies are used to transmit session tokens, then areas of the application that are accessed over HTTPS should employ their own session handling mechanism, and the session tokens used should never be transmitted over unencrypted communications.

## Impact

An attacker may be able to induce this event by feeding a user suitable links, either directly or via another web site. Even if the domain that issued the cookie does not host any content that is accessed over HTTP, an attacker may be able to use links of the form http://example.com:443/ to perform the same attack.

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
