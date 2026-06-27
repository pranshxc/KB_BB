---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1763343'
original_report_id: '1763343'
title: Dependency confusion in https://github.com/hyperledger/aries-mobile-agent-react-native
weakness: Code Injection
team_handle: hyperledger
created_at: '2022-11-05T22:20:13.025Z'
disclosed_at: '2023-02-07T16:07:24.440Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- code-injection
---

# Dependency confusion in https://github.com/hyperledger/aries-mobile-agent-react-native

## Metadata

- HackerOne Report ID: 1763343
- Weakness: Code Injection
- Program: hyperledger
- Disclosed At: 2023-02-07T16:07:24.440Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
I found dependency confusion vulnerability in your aries mobile agent. 

The agent is installed through npm which then download thepublic packages required by the application. Those dependencies are defined through the package.json file. I found that your agent depends on the package "aries-bifold" that is not currently present in the public repository; an attacker could upload its malicious package and then gain remote code execution on every target installing the agent.
I limited my research on finding the missing package without uploading the "malicious" package on npm because https://github.com/hyperledger/aries-mobile-agent-react-native is not in scope (but is not out-of-scope either), but the methods to exploit this vulnerability are well documented here:
1) https://dhiyaneshgeek.github.io/web/security/2021/09/04/dependency-confusion/

More about this vulnerability from the researcher who discovered it:
2) https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610

Cheers,
r3drush

## Impact

Remote code execution to clients installing the agent

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
