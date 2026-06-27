---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1032086'
original_report_id: '1032086'
title: csi-snapshot-controller crashes when processing VolumeSnapshot with non-existing
  PVC
weakness: NULL Pointer Dereference
team_handle: kubernetes
created_at: '2020-11-12T07:20:20.713Z'
disclosed_at: '2020-12-03T01:31:59.488Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: github.com/kubernetes-csi
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- null-pointer-dereference
---

# csi-snapshot-controller crashes when processing VolumeSnapshot with non-existing PVC

## Metadata

- HackerOne Report ID: 1032086
- Weakness: NULL Pointer Dereference
- Program: kubernetes
- Disclosed At: 2020-12-03T01:31:59.488Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

I was asked by Kubernetes Product Security and H1 Employee @turtle_shell to open a new report with the same details as report #995699.

# Summary:
csi-snapshot-controller crashes when processing VolumeSnapshot with non-existing PVC

# Kubernetes Version:
1.19

# Component Version:
snapshot-controller from external-snapshotter repo ver 3.0.0
https://github.com/kubernetes-csi/external-snapshotter/releases/tag/v3.0.0

# Steps To Reproduce:
1.   Install Kubernetes 1.19 with snapshot-controller v3.0.0
2.   Create VolumeSnapshot object with empty spec.volumeSnapshotClass and spec.source.persistentVolumeClaimName = <non-existing PVC name 

    ```
    apiVersion: snapshot.storage.k8s.io/v1beta1
    kind: VolumeSnapshot
    metadata:
      name: new-snapshot
    spec:
      source:
        persistentVolumeClaimName: blabla
    ```
3.   watch snapshot-controller die

# Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

snapshot-controller log:

    E0929 06:42:38.147021       1 snapshot_controller_base.go:338] checkAndUpdateSnapshotClass failed to setDefaultClass the snapshot source PVC name is not specified
    E0929 06:42:38.147118       1 runtime.go:78] Observed a panic: "invalid memory address or nil pointer dereference" (runtime error: invalid memory address or nil pointer dereference)
    goroutine 161 [running]:
    k8s.io/apimachinery/pkg/util/runtime.logPanic(0x1446fc0, 0x201e670)
            /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/runtime/runtime.go:74 +0xa6
    k8s.io/apimachinery/pkg/util/runtime.HandleCrash(0x0, 0x0, 0x0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/runtime/runtime.go:48 +0x89
    panic(0x1446fcit sh0, 0x201e670)
        /usr/lib/golang/src/runtime/panic.go:969 +0x175
    github.com/kubernetes-csi/external-snapshotter/v3/pkg/common-controller.(*csiSnapshotCommonController).syncSnapshotByKey(0xc0001f8e00, 0xc0006a6ae0, 0x19, 0x0, 0xbc)
        /go/src/github.com/kubernetes-csi/external-snapshotter/pkg/common-controller/snapshot_controller_base.go:215 +0x9d7
    github.com/kubernetes-csi/external-snapshotter/v3/pkg/common-controller.(*csiSnapshotCommonController).snapshotWorker(0xc0001f8e00)
        /go/src/github.com/kubernetes-csi/external-snapshotter/pkg/common-controller/snapshot_controller_base.go:188 +0xed
    k8s.io/apimachinery/pkg/util/wait.BackoffUntil.func1(0xc0006ba8b0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:155 +0x5f
    k8s.io/apimachinery/pkg/util/wait.BackoffUntil(0xc0006ba8b0, 0x1774260, 0xc0001f0030, 0x1, 0xc00002a1e0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:156 +0xad
    k8s.io/apimachinery/pkg/util/wait.JitterUntil(0xc0006ba8b0, 0x0, 0x0, 0x1, 0xc00002a1e0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:133 +0x98
    k8s.io/apimachinery/pkg/util/wait.Until(0xc0006ba8b0, 0x0, 0xc00002a1e0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:90 +0x4d
    created by it shgithub.com/kubernetes-csi/external-snapshotter/v3/pkg/common-controller.(*csiSnapshotCommonController).Run
        /go/src/github.com/kubernetes-csi/external-snapshotter/pkg/common-controller/snapshot_controller_base.go:139 +0x2ae
    panic: runtime error: invalid memory address or nil pointer dereference [recovered]
            panic: runtime error: invalid memory address or nil pointer dereference
    [signal SIGSEGV: segmentation violation code=0x1 addr=0xa0 pc=0x12b1d97]

## Impact

DoS of snapshot-controller. It's restarted by Kubernetes, but it dies processing the same VolumeSnapshot again and again.

* Users can't create snapshots of their volumes.
* Kubernetes (snapshot-controller) does not clean up VolumeSnapshotContent objects when user deletes a VolumeSnapshot and its Retain policy is Delete.

All other Kubernetes functionality is not impacted.

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
