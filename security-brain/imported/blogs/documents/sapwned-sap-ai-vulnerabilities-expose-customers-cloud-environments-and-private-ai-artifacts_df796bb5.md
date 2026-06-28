---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-17_sapwned-sap-ai-vulnerabilities-expose-customers-cloud-environments-and-private-a.md
original_filename: 2024-07-17_sapwned-sap-ai-vulnerabilities-expose-customers-cloud-environments-and-private-a.md
title: 'SAPwned: SAP AI vulnerabilities expose customers’ cloud environments and private
  AI artifacts'
category: documents
detected_topics:
- cloud-security
- sso
- jwt
- access-control
- ssrf
- command-injection
tags:
- imported
- documents
- cloud-security
- sso
- jwt
- access-control
- ssrf
- command-injection
language: en
raw_sha256: df796bb5c2688d566c8f88f3e562c6b736df1dbd678699add773df638aef1c43
text_sha256: 3c3273ec9d2fed138eade327aab932bf36ab9960bccc4e19949ff7309dc06cf0
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# SAPwned: SAP AI vulnerabilities expose customers’ cloud environments and private AI artifacts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-17_sapwned-sap-ai-vulnerabilities-expose-customers-cloud-environments-and-private-a.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, jwt, access-control, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `df796bb5c2688d566c8f88f3e562c6b736df1dbd678699add773df638aef1c43`
- Text SHA256: `3c3273ec9d2fed138eade327aab932bf36ab9960bccc4e19949ff7309dc06cf0`


## Content

---
title: "SAPwned: SAP AI vulnerabilities expose customers’ cloud environments and private AI artifacts"
page_title: "SAPwned: SAP AI vulnerabilities expose customers’ cloud environments and private AI artifacts | Wiz Blog"
url: "https://www.wiz.io/blog/sapwned-sap-ai-vulnerabilities-ai-security"
final_url: "https://www.wiz.io/blog/sapwned-sap-ai-vulnerabilities-ai-security"
authors: ["Hillai Ben-Sasson (@hillai)", "Shir Tamari (@shirtamari)", "Nir Ohfeld (@nirohfeld)", "Sagi Tzadik (@sagitz_)", "Ronen Shustin (@ronenshh)"]
programs: ["SAP"]
bugs: ["AI", "Cloud", "Kubernetes", "Privilege escalation", "Missing authentication"]
publication_date: "2024-07-17"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 160
---

# 

**Does AI have an isolation problem?**

Over the past months, we on the Wiz Research Team have conducted extensive tenant isolation research on multiple AI service providers. We believe these services are more susceptible to tenant isolation vulnerabilities, since by definition, they allow users to run AI models and applications – which is equivalent to executing arbitrary code. As AI infrastructure is fast becoming a staple of many business environments, the implications of these attacks are becoming more and more significant. 

We will be presenting our findings from this research project at the upcoming Black Hat conference, in our session “[ _Isolation or Hallucination? Hacking AI Infrastructure Providers for Fun and Weights_](https://www.wiz.io/events/blackhat-wiz-talk)”. 

For the latest installment of this project, we researched SAP’s AI offering, aptly named “SAP AI Core.” This is our 3rd report in the series, following our research on the [_Hugging Face_](https://www.wiz.io/blog/wiz-and-hugging-face-address-risks-to-ai-infrastructure) and [_Replicate_](https://www.wiz.io/blog/wiz-research-discovers-critical-vulnerability-in-replicate) platforms. This blog will explore the vulnerability chain and detail our findings, dubbed “SAPwned,” while also looking at the potential impact and broader takeaways for securing managed AI platforms. 

# 

**Executive Summary**

The AI training process requires access to vast amounts of sensitive customer data, which turns AI training services into attractive targets for attackers. SAP AI Core offers integrations with HANA and other cloud services, to access customers’ internal data via cloud access keys. These credentials are highly sensitive, and our research goal was to determine if potential malicious actors could gain access to these customer secrets.

Our research into SAP AI Core began through executing legitimate AI training procedures using SAP’s infrastructure. By executing arbitrary code, we were able move laterally and take over the service – gaining access to customers’ private files, along with credentials to customers’ cloud environments: AWS, Azure, SAP HANA Cloud, and more. **The vulnerabilities we found could have allowed attackers to access customers’ data and contaminate internal artifacts – spreading to related services and other customers’ environments.**

Specifically, the access we gained allowed us to: 

  * Read and modify Docker images on SAP’s internal container registry 

  * Read and modify SAP’s Docker images on Google Container Registry 

  * Read and modify artifacts on SAP’s internal Artifactory server 

  * Gain cluster administrator privileges on SAP AI Core’s Kubernetes cluster 

  * Access customers’ cloud credentials and private AI artifacts 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAABv/EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAWAQADAAAAAAAAAAAAAAAAAAAAAQP/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCDAVMAAf/Z)

Step-by-step illustration of our research findings 

The root cause of these issues was the ability for attackers to run malicious AI models and training procedures, which are essentially code. After reviewing several leading AI services, we believe the industry must improve its isolation and sandboxing standards when running AI models. 

All vulnerabilities have been reported to SAP’s security team and fixed by SAP, as acknowledged [_on their website_](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/credits-for-security-researchers.html?anchorId=M7#M7). We thank them for their cooperation. No customer data was compromised. 

Following is a technical dive into our vulnerability chain and findings. 

Crying Out Cloud### [SAPwned: SAP AI Core vulnerabilities - Special Guest: Hillai Ben-SassonThe Wiz Research Team uncovered serious vulnerabilities in SAP AI Core, revealing potential risks in #AI infrastructure.](/crying-out-cloud/sapwned-sap-ai-core-vulnerabilities-special-guest-hillai-ben-sasson)[Listen now](/crying-out-cloud/sapwned-sap-ai-core-vulnerabilities-special-guest-hillai-ben-sasson)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOTIwIiBoZWlnaHQ9IjEwODAiPjwvc3ZnPg==)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoVDh0QDg0NFh0VERUVFxMdHSIVFhUaHysjGh0oHSEWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHRAOHDscIhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAAABQIDBv/EAB0QAAICAgMBAAAAAAAAAAAAAAEDAAIEERIhQQX/xAAVAQEBAAAAAAAAAAAAAAAAAAAEA//EABgRAAMBAQAAAAAAAAAAAAAAAAABAwIS/9oADAMBAAIRAxEAPwBqtCW5gMbZq6VQBU+SbvkLx27raUmvJwqT1Iy1tiatIS8GVYdCE0lsNYqDqETxsmqo/9k=)](/crying-out-cloud/sapwned-sap-ai-core-vulnerabilities-special-guest-hillai-ben-sasson)

# 

**Introduction: The research begins**

SAP AI Core is a service that allows users to develop, train and run AI services in a scalable and managed way, utilizing SAP’s vast cloud resources. Similar to other cloud providers (and AI infrastructure providers), the customer’s code runs within SAP’s shared environment – posing a risk of cross-tenant access. 

Our research began as an SAP customer, with basic permissions allowing us to create AI projects. So, we started out by creating a regular AI application on SAP AI Core. SAP’s platform allowed us to provide an Argo Workflow file, which in turn spawned a new Kubernetes Pod according to our configuration. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBg8OEAgTFg0NGQ8NDg0SDhENDQ4YFxMZGBYVFhUaHysjGh0oHSEWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0PEBAOHC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABEAGAMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAAABAYDAv/EAB0QAAIBBAMAAAAAAAAAAAAAAAAEBQIDMjUBMTT/xAAWAQEBAQAAAAAAAAAAAAAAAAACAAH/xAAXEQEBAQEAAAAAAAAAAAAAAAAAAgEh/9oADAMBAAIRAxEAPwDEPuMVyREw8zSz0UNWWqZHEkYss1NYiV7LpEPs8yYOcRYa4lMQYHGle2JHd9QBaNvcRtAAQv/Z)

Example Argo Workflow configuration on SAP AI Core 

This allowed us to run our own arbitrary code within the Pod by design – no vulnerability needed. However, our environment was quite restricted. We quickly realized our Pod had extremely limited network access, as enforced by an Istio proxy sidecar – so scanning the internal network wasn’t an option for us. Yet. 

## 

**Bug #1: Bypassing network restrictions with the power of 1337**

The first thing we tried was to configure our Pod with “interesting” privileges. However, SAP’s admission controller blocked all the dangerous security options we tried – for example, running our container as `root`. 

Despite that, we found two interesting configurations that the admission controller failed to block. 

The first is `shareProcessNamespace`, which allowed us to share the process namespace with our sidecar container. Since our sidecar was the Istio proxy, we gained access to Istio’s configuration, including an access token to the cluster’s centralized Istiod server. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBhYICAgLDQoLDhgNCgoODRENFgoNFxUZGBYTFhUaHysjGh0oKRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OFQoNHC8cFh0vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAkAGAMBIgACEQEDEQH/xAAYAAEAAwEAAAAAAAAAAAAAAAAFAQIEAP/EAB8QAAEDAwUAAAAAAAAAAAAAAAACAwQBBSEREzIzNP/EABcBAAMBAAAAAAAAAAAAAAAAAAECAwD/xAAXEQEAAwAAAAAAAAAAAAAAAAAAAQIR/9oADAMBAAIRAxEAPwAKO01tYqFXplNUaCETqMN34GqUJIYQiJk4tN8hBXIB/9k=)

Accessing the Istio token via our sidecar container 

The other is `runAsUser` (and `runAsGroup`). Although we couldn’t be root, all other UIDs were allowed – including Istio’s UID, which ironically enough was `1337` (yeah, really). We set our UID to 1337 and successfully ran as the Istio user. Since Istio itself is [_excluded from Istio’s iptables rules_](https://istio.io/latest/docs/reference/config/analysis/ist0144/) – we were now running without any traffic restrictions! 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoOEw4NCgoLDhIODg0NDh0NDg4MFxoZGBYTFhUdHysjGh0oHRUWJDUlKC0vMjIyHSI4PTcwPCsxMi8BCgsLDg0NFQ0NHDscFhwvLy8vLy87Ly8vLy8vLy8vLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAgAGAMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAABAYB/8QAFxAAAwEAAAAAAAAAAAAAAAAAAAIDAf/EABYBAQEBAAAAAAAAAAAAAAAAAAIDAf/EABcRAAMBAAAAAAAAAAAAAAAAAAACEQH/2gAMAwEAAhEDEQA/AMitmWJFeztmnQFFMXCC26ygArBw/9k=)

Sending requests to the internal network – before and after UID 1337 

Free from our traffic shackles, we started scanning our Pod’s internal network. Using our Istio token, we were able to read configurations from the Istiod server and gain insight on the internal environment – which led us to the following findings. 

## 

**Bug #2: Loki leaks AWS tokens**

We found an instance of Grafana Loki on the cluster, so we requested the `/config` endpoint to view Loki’s configuration. The API responded with the full configuration, including AWS secrets that Loki used to access S3: 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLFAoVDhgODhEODh0VEh0aFyQZGBoWIhUmHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OFgsQHDscFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAoAGAMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABAUG/8QAHxAAAQMEAwEAAAAAAAAAAAAAAQADBQIEFTESFCER/8QAFgEBAQEAAAAAAAAAAAAAAAAAAgMB/8QAFxEAAwEAAAAAAAAAAAAAAAAAAAIRAf/aAAwDAQACEQMRAD8Aw8k6+7KD7Slbguh/wK3fgZPSTfA7Wlq4J4SI24u25M8aShWoykZLQQmTp//Z)

Configuration excerpt from SAP’s Loki server 

These secrets granted access to Loki’s S3 bucket, containing a large trove of logs from AI Core services (which SAP says aren’t sensitive) and customer Pods. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoPCAgVCgoLDhgKFRUVDhUVDRENFxUZGBYVFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0NEA0QEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABAUG/8QAHhAAAQMEAwAAAAAAAAAAAAAABAACBQEVITEDERP/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AM8SCO0aipDR4ro2naVLY3wphVRuJlsbhEU2VigrXtCdlOFlr0hSf//Z)

Partial file list from Loki’s S3 bucket 

## 

**Bug #3: Unauthenticated EFS shares expose user files**

Within the internal network, we found 6 instances of AWS Elastic File System (EFS), listening on port 2049. A [_common problem_](https://youtu.be/HcNmkCRXFdE) with EFS instances is their default configuration as public – meaning credentials aren’t needed to view or edit files, as long as you have network access to their NFS ports. These instances were no different, and using simple open-source NFS tools, we were able to freely access the shares’ contents. 

Listing files stored on these EFS instances has revealed mass amounts of [AI data](https://www.wiz.io/academy/ai-data-security), including code and training datasets, categorized by customer ID: 

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAANCAIAAAA8DjmHAAABYElEQVR42mWS627DMAiFAZNoe8U9wX7s7Vt5aiPDDhC7jWYh4gt8PhDrz/fXcRy9/95u/X7vvT+O53Bqre37/rHvn9u2izQzR9jz+YDh6z6YSVW2TVURLMrYoIs5yWXpZTTnBDMjkfC4AD6gTI3ZKDzyyxAq08AqT0U0Yzd4LMF24Bjb7kqsRMbcwJpGRUxQg8epO64+6cN4oDJOkRwKpTlKgxZ44HSBKiHnL2nmw0ws5JSiKjMGdjUpVVqbmZ6KWinKSSiK04QCNwYCxgsk6BELZ/4qJwSdik6LmPgn5glNXPQr9igL8KgI7ZLsNP+zApVS5Fn2IeLzSoMiJuwGTDOhxuKvJdcQZAr0xygWn3cEqpoFkFdytmZRJvvkSBQTn5awhilH7bbka4koq6dR6KTkQ0gYVjLHImeb6jQVzXxaiIWLIJQhIT7r4lngSY/zMNZrcvq3Ji1dNan05QtUJ39A7vvpZQi6bQAAAABJRU5ErkJggg==)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAPCAIAAABxxpiMAAABWklEQVR42o1SbXLFIAgEtOfrdHr/myTQXRDNe+2PEnRUYLN8zO/Pr4hwyH1f93XlSrn56DCKQNVETLkrFI/u0EgH+kxVGAS7ws25dF0iFUbgaLrVboTmmVZoXmWajfwpHsQMGltJBFEusVBIigdRB/qiyv9hn2NMPClNOpozEMdAMNjDJpVOoWReamQRFRjp8gK0k08Twjz96lqMiAJFaTp35hjJ6KOBjl9TcDo1UJHKaxYuvIFcfjGS/NtJ7RXIHpQPRJrIaNRrohRE1fEdqHagwBetcLY3K49Csmtq1RbEZLMgA4cwdr2a8wQS2WXOwagFRtpIZuo1QzVHFkTW8JqZ0N4l++1dtSWzcuyplAaqA8tiyShRLJ1EejS3cLKf18ehgKWHWLuMNZo7I9lNnDWdnelxkNUPfhEFqqtF78KSzQcboh9aCykk/gg9AFHdiLnPzSlec/yv/AC0Vyxi7dFvQAAAAABJRU5ErkJggg==)

Partial file list from two EFS shares; each folder represents a different customer ID

## 

**Bug #4: Unauthenticated Helm server compromises internal Docker Registry and Artifactory**

Our most interesting finding on the network was a service named Tiller, which is the server component of the Helm package manager (in version 2). 

Communication with Tiller is made via its gRPC interface on port 44134, which is by default exposed without any authentication. 

Querying this server on our internal network revealed highly privileged secrets to SAP’s Docker Registry as well as its Artifactory server: 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBhMICAgSFQ4LGBIPDQ4PFh0PFhENJx8ZGBYVGxUdHysjJh0oHRYWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0PFQ0OFS8oFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABUAGAMBIgACEQEDEQH/xAAZAAEBAAMBAAAAAAAAAAAAAAAABAEFBgP/xAAfEAABAwQDAQAAAAAAAAAAAAAAAgQFAQMRMhUhMRT/xAAWAQEBAQAAAAAAAAAAAAAAAAACAAH/xAAXEQEBAQEAAAAAAAAAAAAAAAAAAQIR/9oADAMBAAIRAxEAPwDins25XJakTmbcIc+Hpfc2qyWpO8rbU4zRIluRiNnXPJZx6CWMWlMpqDB5G4ftbaJHqhJeRT6DAKjsh26FSvdAAQP/2Q==)

Container registry and Artifactory credentials – exposed by Helm server query

Using these secrets’ read access, a potential attacker could read internal images and builds, extracting commercial secrets and possibly customer data. 

Using the secrets’ write access, an attacker could poison images and builds, conducting a supply-chain attack on SAP AI Core services. 

wiz academy### [AI Security Posture Management (AI-SPM): Why It Matters and How It Works ](/academy/what-is-ai-security-posture-management-ai-spm)[Read more](/academy/what-is-ai-security-posture-management-ai-spm)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDA2IiBoZWlnaHQ9IjExOTgiPjwvc3ZnPg==)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAMCAIAAAD3UuoiAAAB6ElEQVR42kWS63LdIAyEV0Jgzi1Jn7Dv/7fTHNugS+TjNDU7DMNYH2JZid8BBirQgA5c/ml57TAiMA02Arvy5m0PGoxZ4AWB748gOVBwzKfKfzljZyRhhjtrkBb2StGJFpYXpZwUHKX9OPZAtG9Fw1qxV2ySIB+hE2o8oyizN47OdGO5h/bvmrOj7ifIsniJbcHasNVYxbcU2XAdPA8QayGrHJcThPoIvUEvJIWKfDYzhkrsRxdZf8rX4ivbRrpnRzSUZkALLDvu4DvJg/QTfifrVGuC/pRwiplesG8cK8UTvoY/w9awLebmc9pQm2Fa3JrHNdjcPdIldtAEVYS4UZrqFsZk+Tq5UCiHIqb5hE+zOfN6hmG5VSZsUv6fXh92Mx0KkssuxlFKkDk8Iid/4SScKdJGY54k+/GEsqEP3LTcPD2SB9cHtyu342q/nmREGYu9lm36MrlNb5UXyTdOO2LPPqZbxmcnGd4n3VXeY3mn/sGXN+7X0phI6C+EIQUXgTZ+Dn62eOZCaCVaQcNp5g0H0251xEXpYTVBSUlBKuwIkGB9Jaoc4RbFW0M36io9QUwbsDv0ABGP0maCSoI+sFy5o9TDp3LmaLwC6fjJeztDH4XTO7iYq3poxsia4gC5XPPYqD+xTsIXRiBJeShHCFkAAAAASUVORK5CYII=)](/academy/what-is-ai-security-posture-management-ai-spm)

## 

**Bug #5: Unauthenticated Helm server compromises K8s cluster, exposing Google access tokens and customer secrets**

The Helm server was exposed to both read and write operations. While the read access exposed sensitive secrets (as can be seen above), the server’s write access allowed for a complete cluster takeover. 

Tiller’s `install` command takes a Helm package and deploys it to the K8s cluster. We created a malicious Helm package that spawns a new Pod with `cluster-admin` privileges, and ran the install command. 

We were now running with full privileges on the cluster! 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoQDggPCQ0WDhcJDgYHCxYNFhEYFxUZGCIVFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OEAoQEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAXAAEAAwAAAAAAAAAAAAAAAAAEAAUG/8QAHhAAAQQDAAMAAAAAAAAAAAAAAAEDBDECBSEREhT/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AMdu5zuOxTgL7HHJCcHb1UWfRVo56yaCJzMtzCTRA+DvmVRCT//Z)

Partial list of K8s permissions we obtained via Helm 

Using this access level, an attacker could directly access other customer’s Pods and steal sensitive data, such as models, datasets, and code. This access also allows attackers to interfere with customer’s Pods, taint AI data and manipulate models’ inference. 

Furthermore, this access level would have allowed us to view customers’ own secrets – even secrets that are beyond the scope of SAP AI Core. For example, our AI Core account contained secrets to our AWS account (for S3 data access), our SAP HANA account (for Data Lake access), and our Docker Hub account (to pull our images). Using our newfound access level, we queried for those secrets, and managed to access all of them in plaintext: 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgODw0HBw4HCA0ODQ0IDQkIDhEJFgkNFxMZGBYTIhUaHysjGikoHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0PFQoNFS8dFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABEAGAMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAAAgEH/8QAFhABAQEAAAAAAAAAAAAAAAAAAAER/8QAFwEBAAMAAAAAAAAAAAAAAAAAAgABA//EABcRAQEBAQAAAAAAAAAAAAAAAAABAiH/2gAMAwEAAhEDEQA/AOdSq1EVCpbkboYIHExUBKWxoKZv/9k=)

Accessing customer secrets using our K8s permissions 

The same query also revealed an SAP access key to Google Container Registry, named `sap-docker-registry-secret`. We have confirmed that this key grants both read and write permissions – further enlarging the scope of a potential supply-chain attack. 

# 

**Takeaways**

Our research into SAP AI Core demonstrates the importance of defense in depth. The main security obstacle we were facing was Istio blocking our traffic from reaching the internal network. Once we were able to bypass that obstacle, we gained access to several internal assets that did not require any additional authentication – meaning the internal network was perceived as trusted. Hardening those internal services could have minimized the impact of this attack and downgraded it from a complete service takeover to a minor security incident. 

In line with our previous Kubernetes-related vulnerabilities, this research also demonstrates the tenant isolation pitfalls of using K8s in managed services. The crucial separation between the control plane (service logic) and the data plane (customer compute) is being impacted by the K8s architecture, which allows logical connections between them through APIs, identities, shared compute, and software-segmented networks. 

Furthermore, this research demonstrates the unique challenges that the AI R&D process introduces. AI training requires running arbitrary code by definition; therefore, appropriate guardrails should be in place to assure that untrusted code is properly separated from internal assets and other tenants. 

### [Wiz AI Security Posture Management (AI-SPM)Accelerate AI adoption securely with continuous visibility and proactive risk mitigation across your AI models, training data, and AI services.](https://www.wiz.io/solutions/ai-security-posture-management)[Learn More](https://www.wiz.io/solutions/ai-security-posture-management)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDAwIiBoZWlnaHQ9IjIyNTAiPjwvc3ZnPg==)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLEBALDhgQDg0YDhgVFhUNFxsdGiIVIhUdHysjGh0oHRYWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLAg0OHBAQHDsoIhw7OzsvLy87OzsvOzs7Ozs7Ozs7Oy87Oy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAABBQAEBv/EAB0QAAEEAwEBAAAAAAAAAAAAAAEAAgMFBAYSIRT/xAAWAQEBAQAAAAAAAAAAAAAAAAAFBgT/xAAcEQABBQADAAAAAAAAAAAAAAABAAMGEjECBSH/2gAMAwEAAhEDEQA/ANFVa1j/AAEFwRbreNGHHoKgy1ngwTySlI2HLJI6Kpw1Ojy1FWh4GI39TCxvjlEqtbGaZnpKiXbYmVdWO/RE+Bf/2Q==)](https://www.wiz.io/solutions/ai-security-posture-management)

# 

Disclosure timeline 

  * **Jan. 25, 2024** – Wiz Research reports security findings to SAP 

  * **Jan. 27, 2024** – SAP replies and assigns a case number 

  * **Feb. 16, 2024** – SAP fixes first vulnerability and rotates relevant secrets 

  * **Feb. 28, 2024** – Wiz Research bypasses the patch using 2 new vulnerabilities, reports to SAP 

  * **May 15, 2024** – SAP deploys fixes for all reported vulnerabilities 

  * **Jul. 17, 2024** – Public disclosure 

# 

Stay in touch! 

Hi there! We are Hillai Ben-Sasson ([_@hillai_](https://twitter.com/hillai)), Shir Tamari ([_@shirtamari_](https://twitter.com/shirtamari)), Nir Ohfeld ([_@nirohfeld_](https://twitter.com/nirohfeld)), Sagi Tzadik ([_@sagitz__](https://twitter.com/sagitz_)) and Ronen Shustin ([_@ronenshh_](https://twitter.com/ronenshh)) from the Wiz Research Team. We are a group of veteran white-hat hackers with a single goal: to make the cloud a safer place for everyone. We primarily focus on finding new attack vectors in the cloud and uncovering isolation issues in cloud vendors. 

We would love to hear from you! Feel free to contact us on Twitter or via email: [ _research@wiz.io_](mailto:research@wiz.io). 

Tags

[#Research](/blog/tag/research)[#AI](/blog/tag/ai)
