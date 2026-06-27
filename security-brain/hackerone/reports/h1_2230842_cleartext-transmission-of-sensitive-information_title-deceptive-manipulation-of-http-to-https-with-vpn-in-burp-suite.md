---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2230842'
original_report_id: '2230842'
title: 'Title: Deceptive Manipulation of HTTP to HTTPS with VPN in Burp Suite'
weakness: Cleartext Transmission of Sensitive Information
team_handle: portswigger
created_at: '2023-10-29T02:55:41.864Z'
disclosed_at: '2023-10-31T09:10:56.646Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 67
asset_identifier: Burp Suite Pro/Community
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: high
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Title: Deceptive Manipulation of HTTP to HTTPS with VPN in Burp Suite

## Metadata

- HackerOne Report ID: 2230842
- Weakness: Cleartext Transmission of Sensitive Information
- Program: portswigger
- Disclosed At: 2023-10-31T09:10:56.646Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description:
I identified a deceptive behavior in the Burp Suite application, combined with the use of a VPN, that can potentially mislead attackers into thinking a website has downgraded from HTTPS to HTTP when it is still using HTTPS. This action may not pose a significant threat, but it can lead to attacker misdirection. The scenario can be categorized under CWE-319: Cleartext Transmission of Sensitive Information.

Steps to Reproduce:

    Set up the target website and ensure that it uses HTTPS for secure communication.

    Open the Burp Suite application and configure it to intercept and manipulate traffic between the client and server.

    Initiate a session with the target website through Burp Suite's proxy.

    In Burp Suite, manipulate the response to make the attacker believe the website has downgraded to HTTP (e.g., modify response headers).

    Use a VPN for added anonymity during this process.

    Observe the attacker's response and their behavior, as they might adapt their attack techniques thinking the connection is unencrypted.

## Impact

Deception: The attacker is misled into thinking the connection is unencrypted (HTTP), which might lead them to adjust their attack techniques. This can provide a slight advantage to the defenders.

    Wasted Resources: The attacker may allocate unnecessary resources to exploit an apparently vulnerable HTTP connection, which can be seen as a waste of their time and efforts.

    False Sense of Security: On the flip side, if the attacker believes the website has downgraded to HTTP, they might not take encryption and security precautions as seriously, potentially leading to data breaches if they act recklessly.

And Reputational damage due to when the attacker finds out it is really HTTPS not HTTP they might find a different application besides burp suite

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
