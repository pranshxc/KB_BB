---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '872190'
original_report_id: '872190'
title: Plaintext storage of a password on kubernetes release bucket
weakness: Plaintext Storage of a Password
team_handle: kubernetes
created_at: '2020-05-12T19:19:27.083Z'
disclosed_at: '2021-01-07T18:30:33.292Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: k8s.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- plaintext-storage-of-a-password
---

# Plaintext storage of a password on kubernetes release bucket

## Metadata

- HackerOne Report ID: 872190
- Weakness: Plaintext Storage of a Password
- Program: kubernetes
- Disclosed At: 2021-01-07T18:30:33.292Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Report Submission Form

## Summary:
During my recon I found these two buckets dl.k8s.io and dl.kubernetes.io which actually redirects to https://storage.googleapis.com/kubernetes-release/.
By searching the string "password" under https://storage.googleapis.com/kubernetes-release/ I found a file called rsyncd.password (https://storage.googleapis.com/kubernetes-release/archive/anago-v1.10.0-alpha.1/k8s.io/kubernetes/_output-v1.10.0-alpha.1/images/kube-build:build-734df85a63-5-v1.9.2-1/rsyncd.password) where the password "**VmvrL2DyKbJB5jb5EkNfqYPpmLBf0LjS**" is stored in plaintext.
{F825675}
{F825676}
This password is used in this script https://storage.googleapis.com/kubernetes-release/archive/anago-v1.10.0-alpha.1/k8s.io/kubernetes/_output-v1.10.0-alpha.1/images/kube-build:build-734df85a63-5-v1.9.2-1/rsyncd.sh. The script rsyncd.sh is used to set up and run rsyncd to allow data to move into and out of our dockerized build system.
{F825677}
From the github repo https://github.com/kubernetes/release we can see what is anago where this password was found.
{F825678}

## Fix:
Delete the file https://storage.googleapis.com/kubernetes-release/archive/anago-v1.10.0-alpha.1/k8s.io/kubernetes/_output-v1.10.0-alpha.1/images/kube-build:build-734df85a63-5-v1.9.2-1/rsyncd.password.

## Impact

Storing password in plaintext in a public bucket on the web is a security bad practice. People that used or still using the anago-v1.10.0-alpha.1 could have their environment compromised if an attacker use this leaked password and the username k8s defined here https://storage.googleapis.com/kubernetes-release/archive/anago-v1.10.0-alpha.1/k8s.io/kubernetes/_output-v1.10.0-alpha.1/images/kube-build:build-734df85a63-5-v1.9.2-1/rsyncd.sh.

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
