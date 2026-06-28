---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-01_gke-autopilot-node-compromise-via-race-condition.md
original_filename: 2021-04-01_gke-autopilot-node-compromise-via-race-condition.md
title: GKE Autopilot Node Compromise via Race Condition
category: documents
detected_topics:
- command-injection
- otp
- race-condition
- webhooks
- api-security
tags:
- imported
- documents
- command-injection
- otp
- race-condition
- webhooks
- api-security
language: en
raw_sha256: dc4b1842a59fb350d7157ef0a399122fcd72af584ea007a79e669509f3a08e0e
text_sha256: c2455a4e473938333fc138aac0e4922a95ab6ad3869f9161356e7c3151d2cc8a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# GKE Autopilot Node Compromise via Race Condition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-01_gke-autopilot-node-compromise-via-race-condition.md
- Source Type: markdown
- Detected Topics: command-injection, otp, race-condition, webhooks, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `dc4b1842a59fb350d7157ef0a399122fcd72af584ea007a79e669509f3a08e0e`
- Text SHA256: `c2455a4e473938333fc138aac0e4922a95ab6ad3869f9161356e7c3151d2cc8a`


## Content

---
title: "GKE Autopilot Node Compromise via Race Condition"
page_title: "GKE Autopilot Node Compromise via Race Condition | Anthony Weems"
url: "https://lf.lc/vrp/181521559d/"
final_url: "https://amlw.dev/vrp/181521559d/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["Container escape"]
bounty: "1,337"
publication_date: "2021-04-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3777
---

#  GKE Autopilot Node Compromise via Race Condition 

April 1, 2021

### Vulnerability Details#

GKE Autopilot provides many default security controls to protect the node, including protections against privileged pods and limitations on hostPath volume mounts.

There is a race condition during provisioning of the Autopilot OPA policies that allows an attacker to bypass the intended controls by simply creating their malicious resource while the OPA policies are being provisioned. To demonstrate, use the following steps:

  1. Download the file [deploy.yaml](/assets/vrp/181521559d-deploy.yaml)
  2. Create an Autopilot cluster
  3. While the cluster is being created, run the following commands (replacing $name):

  
  
  while true; do
  gcloud container clusters get-credentials $name && break;
  done
  while true; do
  timeout 1 kubectl apply -f deploy.yaml && break;
  done
  kubectl exec -it deploy/priv -- nsenter --mount=/proc/1/ns/mnt -- /bin/bash
  

Observe that the privileged deployment initially fails to create for the following reasons:

  * `The connection to the server 34.69.12.113 was refused - did you specify the right host or port?`
  * `GKEAutopilot authz: the request was sent before policy enforcement is enabled`
  * `Internal error occurred: failed calling webhook "validation.gatekeeper.sh": Post https://localhost:8787/v1/admit?timeout=5s: dial tcp [::1]:8787`

After a few minutes have passed, the deployment will succeed and allow the user to exec into their new privileged pod.

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
