---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '774896'
original_report_id: '774896'
title: Kubelet resource exhaustion attack via metric label cardinality explosion from
  unauthenticated requests
weakness: Uncontrolled Resource Consumption
team_handle: kubernetes
created_at: '2020-01-14T18:01:27.545Z'
disclosed_at: '2020-10-31T10:26:46.443Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: https://github.com/kubernetes/kubernetes
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Kubelet resource exhaustion attack via metric label cardinality explosion from unauthenticated requests

## Metadata

- HackerOne Report ID: 774896
- Weakness: Uncontrolled Resource Consumption
- Program: kubernetes
- Disclosed At: 2020-10-31T10:26:46.443Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
Malicious clients can potentially DOS a kubelet by sending a high amount of specially crafted requests to the kubelet's HTTP server. 

For each request the kubelet updates/sets 3 metrics:
- [kubelet_http_requests_total (Counter)](https://github.com/kubernetes/kubernetes/blob/v1.17.0/pkg/kubelet/server/metrics/metrics.go#L33-L44)
- [kubelet_http_requests_duration_seconds (Histogram with 7 buckets)](https://github.com/kubernetes/kubernetes/blob/v1.17.0/pkg/kubelet/server/metrics/metrics.go#L46-L56)
- [kubelet_http_inflight_requests (Counter)](https://github.com/kubernetes/kubernetes/blob/v1.17.0/pkg/kubelet/server/metrics/metrics.go#L58-L66)

Each metric has the label `path` which will contain the path of each request.
It does not matter if the request is authenticated or not - The metrics will be set/updated regardless.
With each unique path, the kubelet creates 16 new time series.
By sending a high amount of requests with random path values, the kubelet's memory usage will grow and eventually the kubelet will get OOM killed.

It's also possible that the kubelet evicts all workloads before being OOM killed (Which might be worse than an OOM kill) 

The corresponding kubelet server code: https://github.com/kubernetes/kubernetes/blob/v1.17.0/pkg/kubelet/server/server.go#L859-L865

## Kubernetes Version:
- v1.17.0 kubeadm (tested)
- v1.16.4 kubeadm (tested)
- v1.15.7 kubeadm (tested)

## Component Version:
Kubelet

## Steps To Reproduce:
```bash
NODE_NAME="my-poor-node"
NODE_IP="192.168.1.100"

# Perform random requests from an unauthenticated client
curl --insecure https://${NODE_IP}:10250/foo
curl --insecure https://${NODE_IP}:10250/bar
curl --insecure https://${NODE_IP}:10250/baz

# Run in a dedicated shell to be able to get the metrics
kubectl proxy

# Load metrics from node
# For each path (foo, bar, baz) 16 time series got created
curl http://127.0.0.1:8001/api/v1/nodes/${NODE_NAME}/proxy/metrics 2>&1 | grep 'kubelet_http_requests_total\|kubelet_http_requests_duration_seconds\|kubelet_http_inflight_requests'

# Perform more random requests & see the output of the metrics endpoint to grow.
```

## Supporting Material/References:

A gist with an additional go tool which spams the kubelet
https://gist.github.com/mrIncompetent/c6cbe483298c36668374363baf52a35d

## Impact

Kill the kubelet / Make the kubelet consume all resources so it starts to evict pods.

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
