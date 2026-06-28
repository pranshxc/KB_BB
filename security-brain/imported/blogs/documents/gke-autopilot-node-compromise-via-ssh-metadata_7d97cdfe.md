---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-05_gke-autopilot-node-compromise-via-ssh-metadata.md
original_filename: 2021-03-05_gke-autopilot-node-compromise-via-ssh-metadata.md
title: GKE Autopilot Node Compromise via SSH Metadata
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 7d97cdfeb34db0bfbedd3e9dc9e79cf77604ef7b1b6896caa5dbd34c9f3ca493
text_sha256: 6abf44e13a11feb54f35e7c5699886c5d5e1951d635dc2e909be5c295bbf88a6
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# GKE Autopilot Node Compromise via SSH Metadata

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-05_gke-autopilot-node-compromise-via-ssh-metadata.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `7d97cdfeb34db0bfbedd3e9dc9e79cf77604ef7b1b6896caa5dbd34c9f3ca493`
- Text SHA256: `6abf44e13a11feb54f35e7c5699886c5d5e1951d635dc2e909be5c295bbf88a6`


## Content

---
title: "GKE Autopilot Node Compromise via SSH Metadata"
page_title: "GKE Autopilot Node Compromise via SSH Metadata | Anthony Weems"
url: "https://lf.lc/vrp/181521559c/"
final_url: "https://amlw.dev/vrp/181521559c/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["Container escape"]
bounty: "1,337"
publication_date: "2021-03-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3838
---

#  GKE Autopilot Node Compromise via SSH Metadata 

March 5, 2021

### Vulnerability Details#

GKE Autopilot provides many default security controls to protect the node, including protections against privileged pods and limitations on hostPath volume mounts.

The nodes are configured to pull from the compute metadata SSH keys list. As documented [here](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys), a user with `compute.projects.setCommonInstanceMetadata` can set project-wide SSH keys. To prevent users from simply logging in to the nodes directly, the nodes use an sshd configuration to set all user shells to /sbin/nologin. However, they do not restrict SSH tunneling. We can set up a SOCKS proxy and use this proxy to access the compute metadata service on the nodes (normally protected by the GKE metadata server). This enables the standard kubelet bootstrapping attack (with one difference). To demonstrate:

  1. Create an autopilot cluster and use `kubectl get node -o wide` to view node IP addresses
  2. Configure project wide SSH keys here: <https://console.cloud.google.com/compute/metadata/sshKeys>
  3. Download the following file: [socks.sh](/assets/vrp/181521559b-socks.sh)
  4. Run `socks.sh <username> <node IP>` using your username from step 2 and a node IP address from step 1. This script automates the following steps: 
  * Set up a SOCKS proxy to a given node
  * Download the kube-env attribute from the metadata service on the node
  * Extract the TPM key and certificate from kube-env
  * Create a CSR for `OU=system:masters CN=kubernetes-admin` (which is exempt from the Autopilot gatekeeper policies)
  * Submit the CSR to the Kubernetes API using the TPM key and cert
  * Approve the CSR with a “Kubernetes Engine Admin” user (note: the Autopilot gatekeeper policy prohibit this user from simply creating their own CSR)
  * Use the newly signed cert to launch a privileged pod and compromise the node

**Screenshot of working exploit:** ![Screenshot of working exploit](/assets/vrp/181521559b-exploit.png)

### Attack Scenario#

The Autopilot documentation describes the motivation for its security controls as:

> In order for GKE to offer management of the nodes and provide you with a more streamlined operational experience, there are a few restrictions and limitations when compared to GKE Standard. Some of these limitations are security best practices, while others allow Autopilot clusters to be safely managed.

A user with `compute.projects.setCommonInstanceMetadata` permission in the project could bypass the security controls in the cluster and gain privileged access to the managed Kubernetes nodes. Using this access, they could read all secrets in the cluster (including those outside their provisioned access) or explore the attack surface of the Autopilot control plane.

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
