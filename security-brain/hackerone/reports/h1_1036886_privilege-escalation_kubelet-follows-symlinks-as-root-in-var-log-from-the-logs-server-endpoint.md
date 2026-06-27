---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1036886'
original_report_id: '1036886'
title: Kubelet follows symlinks as root in /var/log from the /logs server endpoint
weakness: Privilege Escalation
team_handle: kubernetes
created_at: '2020-11-17T16:54:29.472Z'
disclosed_at: '2021-04-01T18:13:00.639Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/kubernetes/kubelet
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Kubelet follows symlinks as root in /var/log from the /logs server endpoint

## Metadata

- HackerOne Report ID: 1036886
- Weakness: Privilege Escalation
- Program: kubernetes
- Disclosed At: 2021-04-01T18:13:00.639Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Privilege escalation from a  pod, to root read permissions on the entire filesytem of the node, by creating symlinks inside /var/log.
The kubelet is simply serving a fileserver at /var/log:

_kubernetes\pkg\kubelet\kubelet.go:1371_
```golang
if kl.logServer == nil {
		kl.logServer = http.StripPrefix("/logs/", http.FileServer(http.Dir("/var/log/")))
	}
```
The kubelet naturally runs as root on the node, so this basically gives the ability for pods with write permissions to /var/log directory a directory traversal as a root user on the host (potentially taking over the whole cluster by getting secret keys)
An easy fix is checking the symlink destination, to figure out whether it is inside /var/lib/docker or other whitelisted paths to not break to mechanism of logs correlations

A while back, I discovered this bug, when you didn't had the Bug Bounty program. 
I Published the following blog:
https://blog.aquasec.com/kubernetes-security-pod-escape-log-mounts
Describing the vulnerability.

(it  requires RBAC permissions to read logs, or a kubelet configured with AlwaysAllow. and a mount point to any child directory inside /var/log)
I researched some log collectors projects in github, seems like alot of them are freely using this mount point.
As a user I would not imagine those projects can potentially take clusters. 

## Kubernetes Version:
All versions

## Component Version:
The kubelet

## Steps To Reproduce:
  1. create a pod with a mount path to `/var/log`
  1. create a symlink in the mount point: `/var/log/rootfs_symlink -> /`
  1. curl from within the pod: `https://<ip_of_node>:10250/logs/rootfs_symlink/etc/shadow`

## Supporting Material/References:
https://blog.aquasec.com/kubernetes-security-pod-escape-log-mounts
https://github.com/danielsagi/kube-pod-escape

## Impact

Root read permissions on the entire filesystem of the node

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
