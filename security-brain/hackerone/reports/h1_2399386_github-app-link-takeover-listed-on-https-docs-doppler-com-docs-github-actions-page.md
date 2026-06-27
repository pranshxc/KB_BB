---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2399386'
original_report_id: '2399386'
title: Github app(link) Takeover Listed on "https://docs.doppler.com/docs/github-actions"
  page
team_handle: doppler
created_at: '2024-03-02T17:17:29.802Z'
disclosed_at: '2024-03-15T15:54:34.506Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
---

# Github app(link) Takeover Listed on "https://docs.doppler.com/docs/github-actions" page

## Metadata

- HackerOne Report ID: 2399386
- Weakness: 
- Program: doppler
- Disclosed At: 2024-03-15T15:54:34.506Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
GitHub Apps are a type of integration that allows developers to extend the functionality of GitHub and automate workflows within the GitHub platform. 
developers can install the github app on need.

A Github app presented on `https://docs.doppler.com/docs/github-actions` was vulnerable to takeover. With this the attacker can achieve his needs and whoever goes to the link and install the app can be vulnerable.


## Steps To Reproduce:

  1. go to `https://docs.doppler.com/docs/github-actions`
  2. scroll unit you see this link:
  
{F3093438}
  
3.you could observe the following:
{F3093440}

# Mitigation:
Removing or replacing the github app link

## Impact

A GitHub app takeover can have significant repercussions, including unauthorized access to sensitive data, manipulation of code leading to vulnerabilities or disruptions in workflows, and a loss of trust in both the app developer and the GitHub platform. Additionally, there's a risk of data exfiltration, reputational damage, and potential legal consequences. Such incidents highlight the importance of robust security measures and proactive risk management to prevent unauthorized access and mitigate the impact of security breaches within the GitHub ecosystem.

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
