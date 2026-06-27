---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1398617'
original_report_id: '1398617'
title: Broken Github Link Used in deployment docs of "github.com/kubernetes/kompose"
weakness: Improper Access Control - Generic
team_handle: kubernetes
created_at: '2021-11-12T07:35:41.279Z'
disclosed_at: '2021-12-16T00:24:26.712Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: https://github.com/kubernetes/kompose
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Broken Github Link Used in deployment docs of "github.com/kubernetes/kompose"

## Metadata

- HackerOne Report ID: 1398617
- Weakness: Improper Access Control - Generic
- Program: kubernetes
- Disclosed At: 2021-12-16T00:24:26.712Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
Kubernetes have a github project [github.com/kubernetes/kompose](https://github.com/kubernetes/kompose)
In the project there is a doc which have installation steps
In the steps, doc is referring to another github account repository to clone it and install.
But the github account was not registered on github.com
So I was able to takeover the account and host PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://github.com/kubernetes/kompose/blob/master/docs/maven-example.md
  2. Search for `Clone the example project from GitHub`
  3. You will see this clone command `$ git clone https://github.com/piyush1594/kompose-maven-example.git`
  4. Try accessing the repository using the link https://github.com/piyush1594/kompose-maven-example you will see the takeover message.

## Supporting Material/References:

- https://github.com/piyush1594/kompose-maven-example
- https://github.com/kubernetes/kompose/blob/master/docs/maven-example.md

{F1511533}

## Impact

An attacker can takeover the github repository and host malicious code on it. When any user will follow the setup steps and clone the repository, it will end up pulling code from attacker's controlled repository.
When user will try running further setup steps, it will end up executing attackers malicious code, which can lead to RCE.

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
