---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '966383'
original_report_id: '966383'
title: secret leaks in vsphere cloud controller manager log
weakness: Cleartext Storage of Sensitive Information
team_handle: kubernetes
created_at: '2020-08-25T00:29:42.471Z'
disclosed_at: '2020-11-29T21:23:27.388Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: https://github.com/kubernetes/kubernetes
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# secret leaks in vsphere cloud controller manager log

## Metadata

- HackerOne Report ID: 966383
- Weakness: Cleartext Storage of Sensitive Information
- Program: kubernetes
- Disclosed At: 2020-11-29T21:23:27.388Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
When create k8s cluster over vsphere and enable vsphere as cloud provider. With logging level set to 4 or above, secret information will be printed out in the cloud controller manager's log.

## Kubernetes Version:
1.18.6

## Component Version:
legacy cloud provider

## Steps To Reproduce:
[add details for how we can reproduce the issue, including relevant cluster setup and configuration]

  1. Configure vsphere as cloud provider and set logging level to 4 or above (https://cloud-provider-vsphere.sigs.k8s.io/tutorials/kubernetes-on-vsphere-with-kubeadm.html)
  2. Check vsphere cloud provider log when a secret is created or udpated as the secret informer is registered with and will be print out when the logging level set to 4 or above.
  
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
Source codes that print out the secret info:
https://github.com/kubernetes/kubernetes/blob/6d0f4749a59099171540d4fd7c9523b029e71ceb/staging/src/k8s.io/legacy-cloud-providers/vsphere/vsphere.go#L1503

https://github.com/kubernetes/kubernetes/blob/6d0f4749a59099171540d4fd7c9523b029e71ceb/staging/src/k8s.io/legacy-cloud-providers/vsphere/vsphere.go#L1527

Calling code path:
1.cmd/kube-controller-manager/app/controllermanager.go -> Run()
2.cmd/kube-controller-manager/app/controllermanager.go -> CreateControllerContext()
3. cmd/kube-controller-manager/app/cloudproviders.go -> createCloudProvider()
4. vendor/k8s.io/cloud-provider/cloud.go ->SetInformers()
5. staging/src/k8s.io/legacy-cloud-providers/vsphere/vsphere.go -> func (vs *VSphere) SetInformers(informerFactory informers.SharedInformerFactory)

  * [attachment / reference]

## Impact

If any kubernetes users or service accounts has privileges (e.g. GET pods/log  in the kube-system namespace), he will be able to view all the secrets data when a secret is created or updated which may contain sensitive data such as password or private key. Further, is the secret is a service account token, then the user may escalate his privileges.

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
