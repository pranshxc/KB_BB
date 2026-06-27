---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '863979'
original_report_id: '863979'
title: Compromise of node can lead to compromise of pods on other nodes
team_handle: kubernetes
created_at: '2020-05-01T12:26:35.494Z'
disclosed_at: '2020-10-30T21:54:31.857Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: https://github.com/kubernetes/kubelet
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Compromise of node can lead to compromise of pods on other nodes

## Metadata

- HackerOne Report ID: 863979
- Weakness: 
- Program: kubernetes
- Disclosed At: 2020-10-30T21:54:31.857Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Kubernetes team, 

## Summary:
If an attacker manages to escape a (eg. privileged) container and gains access to the underlying node it can replace the Kubelet process listening on port 10250/10255 on the node. A fake Kubelet server issueing 301 redirects can trick 'kubectl' (or other clients) into issueing commands against a other pods in the cluster.  This attack bypasses firewalling configurations where nodes cannot talk directly to eachother on port 10250/10255 and also works when port 10250 requires authentication since kubectl is happy to resend the Authorization header / bearer token when a 301redirect is received. 

## Kubernetes Version:
1.14.10

## Component Version:
kubelet/kubectl

## Steps To Reproduce:

  1. Attacker escapes container 
  2. Attacker issues a 'kill -9 `pidof kubelet`; python fakekubet.py  (see attachment)
  3. Attacker waits for a /exec request coming in to the fakekubelet.py server, and redirects it (with an arbitrary command) to another node.  

Example exec request for 'hello-app'  by kubectl:
10.138.0.10 - - [01/May/2020 11:28:55] "POST /exec/default/hello-server-7f8fd4d44b-j5rsc/hello-app?command=%2Fbin%2Fs&input=1&output=1&tty=1 HTTP/1.1" 307 - 

Example response by the fakekubelet: 
HTTP/1.1 301 Redirect
Location: https://10.138.0.8/exec/default/victim-67c59cd9f4-vm5dl/nginx?command=/bin/arbitrary_command_here&error=1&input=1&output=1&tty=0

  4. kubectl follows the redirect and contacts the victim node, requesting /exec as specified by fakekubelet.py (can also redirect to 'master')
  5. arbitrary command is executed on the victim node


## Supporting Material/References:
attachment 1:  fakekubelet.py
attachment 2: ugly_diagram.png
related Kubelet code: https://github.com/kubernetes/kubernetes/blob/4a6935b31fcc4d1498c977d90387e02b6b93288f/pkg/kubelet/server/server.go#L257-L263


I hope this helps!

Kind regards, 
Offensi.com

Wouter ter Maat

## Impact

execute arbitrary command in victim's pod

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
