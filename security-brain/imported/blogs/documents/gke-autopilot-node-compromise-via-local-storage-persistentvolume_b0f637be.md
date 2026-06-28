---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-01_gke-autopilot-node-compromise-via-local-storage-persistentvolume.md
original_filename: 2021-03-01_gke-autopilot-node-compromise-via-local-storage-persistentvolume.md
title: GKE Autopilot Node Compromise via local-storage PersistentVolume
category: documents
detected_topics:
- command-injection
- otp
- api-security
tags:
- imported
- documents
- command-injection
- otp
- api-security
language: en
raw_sha256: b0f637be8ac2ab0209c9667280a9c055a86e8dc7a8481e8188b2b0c4ded5baaa
text_sha256: 7c5501f17a97259f64f126dc1d2688a925f5eb417ae4e90333ed1459014cd1d8
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# GKE Autopilot Node Compromise via local-storage PersistentVolume

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-01_gke-autopilot-node-compromise-via-local-storage-persistentvolume.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `b0f637be8ac2ab0209c9667280a9c055a86e8dc7a8481e8188b2b0c4ded5baaa`
- Text SHA256: `7c5501f17a97259f64f126dc1d2688a925f5eb417ae4e90333ed1459014cd1d8`


## Content

---
title: "GKE Autopilot Node Compromise via local-storage PersistentVolume"
page_title: "GKE Autopilot Node Compromise via local-storage PersistentVolume | Anthony Weems"
url: "https://lf.lc/vrp/181521559a/"
final_url: "https://amlw.dev/vrp/181521559a/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["Container escape"]
bounty: "1,337"
publication_date: "2021-03-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3847
---

#  GKE Autopilot Node Compromise via local-storage PersistentVolume 

March 1, 2021

### Vulnerability Details#

GKE Autopilot provides many default security controls to protect the node, including protections against privileged pods and limitations on hostPath volume mounts. However, these security configurations did not prevent PersistentVolumes with the “local-storage” storage class. The “local-storage” class can be used to mount files from the node into a pod, similar to hostPath volume mounts. This can be abused to mount sensitive files/directories from the node into a pod and elevate permissions. To demonstrate, we mount the /run path from the node, which contains docker.sock, and can be used to further compromise the node.

Use the following steps to reproduce:

  1. Create an Autopilot cluster
  2. Authenticate to the Autopilot cluster via `gcloud container clusters get-credentials` and verify `kubectl get nodes` succeeds
  3. (optionally create a user with limited access to create pods and persistent volumes, or use the “Kubernetes Engine Developer” role)
  4. Download the following files and place them in the working directory: [exploit.sh](/assets/vrp/181521559a-exploit.sh) [docker.yaml](/assets/vrp/181521559a-docker.yaml)
  5. Run the exploit.sh script which performs the following steps: 
  * Creates a dummy pod to cause the autoscaler to provision a node
  * Waits for the dummy pod to be in the ready state and records its node name
  * Deploys the docker.yaml file to the cluster, which contains a persistent volume that mounts /run from that node into a new pod
  * Deletes the dummy pod, allowing our exploit pod to be scheduled on the same node
  * Execs in the exploit pod and runs the following command to launch a root shell on the node:

  
  
  docker -H unix:///host/docker.sock run --rm -it --privileged --net=host --pid=host \
  alpine nsenter --mount=/proc/1/ns/mnt -- /bin/bash
  

**Screenshot of the working exploit:** ![Screenshot of the working exploit](/assets/vrp/181521559a-exploit.png)

### Attack Scenario#

The Autopilot documentation describes the motivation for its security controls as:

> In order for GKE to offer management of the nodes and provide you with a more streamlined operational experience, there are a few restrictions and limitations when compared to GKE Standard. Some of these limitations are security best practices, while others allow Autopilot clusters to be safely managed.

A user with access to create pods and persistent volumes in the Autopilot cluster could bypass the security controls in the cluster and gain privileged access to the managed Kubernetes nodes. Using this access, they could read all secrets in the cluster (including those outside their provisioned access) or explore the attack surface of the Autopilot control plane. Additionally, this user can retrieve a service account token from the node metadata service for the default compute service account.

### Timeline#

  * 2021-03-01: Initial report to Google VRP
  * 2021-03-01: Issue triaged
  * 2021-03-04: Internal bug report filed
  * 2021-03-05: Additional variants reported ([vrp/181521559b](/vrp/181521559b), [vrp/181521559c](/vrp/181521559c))
  * 2021-03-09: Internal bug report updated
  * 2021-04-01: Additional variant reported ([vrp/181521559d](/vrp/181521559d))
  * 2021-04-06: Internal bug report updated
  * 2021-04-08: VRP issued reward ($1337 per variant)
  * 2021-06-07: Issue reported fixed
  * 2021-09-10: Retested and verified only variant “a” is fixed
  * 2021-09-11: Issue reopened
