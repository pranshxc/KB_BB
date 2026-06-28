---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-12_in-cloud-we-trust-wrong-kubernetes-implementation-by-google-cloud-platform-micro.md
original_filename: 2020-01-12_in-cloud-we-trust-wrong-kubernetes-implementation-by-google-cloud-platform-micro.md
title: 'In Cloud we “Trust”: Wrong Kubernetes implementation by Google Cloud Platform
  & Microsoft Azure affecting customers'
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 8062597da1bb9a4923023813d35428f2539f4fffc2d5c4d0e2575079ec9fa384
text_sha256: 3f3847ddeff6c112923a510c1b6bbcb2cdffb92e505c4485a2cd8ae8b75576cd
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# In Cloud we “Trust”: Wrong Kubernetes implementation by Google Cloud Platform & Microsoft Azure affecting customers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-12_in-cloud-we-trust-wrong-kubernetes-implementation-by-google-cloud-platform-micro.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `8062597da1bb9a4923023813d35428f2539f4fffc2d5c4d0e2575079ec9fa384`
- Text SHA256: `3f3847ddeff6c112923a510c1b6bbcb2cdffb92e505c4485a2cd8ae8b75576cd`


## Content

---
title: "In Cloud we “Trust”: Wrong Kubernetes implementation by Google Cloud Platform & Microsoft Azure affecting customers"
url: "https://faun.pub/in-cloud-we-trust-wrong-kubernetes-implementation-by-google-cloud-platform-microsoft-azure-a60f50ba943f"
authors: ["Chen Cohen (@chencococococo)"]
programs: ["Microsoft", "Google"]
bugs: ["Old components with known vulnerabilities"]
publication_date: "2020-01-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4831
scraped_via: "browseros"
---

# In Cloud we “Trust”: Wrong Kubernetes implementation by Google Cloud Platform & Microsoft Azure affecting customers

In Cloud we “Trust”: Wrong Kubernetes implementation by Google Cloud Platform & Microsoft Azure affecting customers
Chen Cohen
Follow
4 min read
·
Jan 12, 2020

6

Kubernetes is the leading container orchestration platform for SMB and enterprises that provides a fast deployment, load balancing, high availability, resource monitoring and is now widely offered as a service on different Cloud providers.

Microsoft Azure

During a security analysis that I have done on a customer’s containers environment running on Azure AKS (Azure Kubernetes Service), I found that the Kubernetes deprecated read-only port (10255) that was designed for metrics and “health” checks, can be accessed from any container that has no restrictions to the host IP addresses. by default, Cloud providers does not restrict the connectivity between containers(pods) and the host machines(nodes). Moreover, Kubernetes have disabled this feature by default a few months ago on an official release of Kubernetes.

As a result of finding this deprecated read-only port (10255) is in use by default on Azure AKS, any user who can access this port (can be easily accessed via curl) can leak information about containers in the same namespace, such as:

· Containers name

· Containers IP addresses

· Ports in use

· Images used for containers deployment.

· Secrets stored as environment variable on the Kubernetes built-in vault

· and more.

In the beginning of October 2019, the issue was reported through Microsoft Security Center with detailed information.

Press enter or click to view image in full size
Microsoft’s answer for the first report

At first, Microsoft avoided taking responsibility and decided to close the report as “N/A” and defined the issue under the responsibility of Azure clients.

Get Chen Cohen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As a Security expert I could not accept such an issue to remain open without Microsoft taking responsibility of the issue as the clients are not responsible for the Kubernetes deployment as Azure AKS is basically Kubernetes-as-a-service and Microsoft should take care of the services they deploy and put their customers at risk. The next report was sent few days later and the following answer was received from Microsoft:

Press enter or click to view image in full size

On November 14, 2019, Microsoft confirmed that the issue is resolved and marked the case as completed

Currently the issue still affects all AKS clusters running version prior to “1.16.1 — preview version”. The default version suggested now while deploying new Kubernetes cluster on Azure is “1.14.8”. the only way to mitigate this issue is by upgrading the AKS cluster version to 1.16.1 or higher.

Google Cloud Platform

While I was waiting for an answer from Microsoft, I decided to check if this deprecated read-only port is still being used in other cloud providers (Google Cloud Platform and Amazon Web Services).

I found that this port is still in use in by GKE (Google Kubernetes Engine) service.

Since Google are the original author of Kubernetes, I though they would be the first to implement updates to their Kubernetes services.

I Immediately sent a report through Google issue tracker and the report was triage within 2 days. 2 weeks later Google have responded again saying that it is already a tracked-bug.

Once google answered that the bug is already being tracked, I have asked for an ETA of the fix and received the following answer:

Press enter or click to view image in full size

As seen from the picture, Google answer was commented on Nov 15th stating that the bug will likely be fixed by the end of the year. As of the date of writing this article (January 9, 2020) the bug is not yet fixed on Google Cloud and is currently affecting all GKE customers (including the latest “1.15.4-gke.22” version).

Amazon EKS customers are not affected.

Press enter or click to view image in full size

Follow us on Twitter 🐦 and Facebook 👥 and Instagram 📷 and join our Facebook and Linkedin Groups 💬.

To join our community Slack team chat 🗣️ read our weekly Faun topics 🗞️, and connect with the community 📣 click here⬇

If this post was helpful, please click the clap 👏 button below a few times to show your support for the author! ⬇
