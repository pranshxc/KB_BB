---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1378175'
original_report_id: '1378175'
title: Ingress-nginx annotation injection allows retrieval of ingress-nginx serviceaccount
  token and secrets across all namespaces
weakness: Code Injection
team_handle: kubernetes
created_at: '2021-10-22T03:49:19.336Z'
disclosed_at: '2022-08-13T18:13:23.850Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: https://github.com/kubernetes/ingress-nginx
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# Ingress-nginx annotation injection allows retrieval of ingress-nginx serviceaccount token and secrets across all namespaces

## Metadata

- HackerOne Report ID: 1378175
- Weakness: Code Injection
- Program: kubernetes
- Disclosed At: 2022-08-13T18:13:23.850Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I submitted the following report to security@kubernetes.io:
> I've been exploring CVE-2021-25742 and believe I've discovered a variant (although it appears there may be many). Most template variables are not escaped properly in `nginx.tmpl`, leading to injection of arbitrary nginx directives. For example, the `nginx.ingress.kubernetes.io/connection-proxy-header` annotation is not validated/escaped and is inserted directly into the `nginx.conf` file.
>
> An attacker in a multi-tenant cluster with permission to create/modify ingresses can inject content into the connection-proxy-header annotation and read arbitrary files from the ingress controller (including the service account).
>
> I've created a secret gist demonstrating the issue against ingress-nginx v1.0.4: https://gist.github.com/amlweems/1cb7e96dca8ada8aee8dc019d4163f2c

## Impact

An attacker with permission to create/modify ingresses in one namespace can inject content into the connection-proxy-header annotation and read arbitrary files from the ingress controller (including the service account). This service account has permission to read secrets in all namespaces.

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
