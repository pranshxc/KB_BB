---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-31_leaky-vessels-docker-and-runc-container-breakout-vulnerabilities.md
original_filename: 2024-01-31_leaky-vessels-docker-and-runc-container-breakout-vulnerabilities.md
title: 'Leaky Vessels: Docker and runc container breakout vulnerabilities'
category: documents
detected_topics:
- sso
- cloud-security
- supply-chain
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- sso
- cloud-security
- supply-chain
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: 9e4bbf127f2ac4d72535048f37d9e67db193bad1d37c801a3eb7a7f78f673253
text_sha256: 6c65c34a362b67557a4a4984dcf5e77c04ad2ea408b86977cccb9ad6be6d4faf
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Leaky Vessels: Docker and runc container breakout vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-31_leaky-vessels-docker-and-runc-container-breakout-vulnerabilities.md
- Source Type: markdown
- Detected Topics: sso, cloud-security, supply-chain, command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `9e4bbf127f2ac4d72535048f37d9e67db193bad1d37c801a3eb7a7f78f673253`
- Text SHA256: `6c65c34a362b67557a4a4984dcf5e77c04ad2ea408b86977cccb9ad6be6d4faf`


## Content

---
title: "Leaky Vessels: Docker and runc container breakout vulnerabilities"
page_title: "Leaky Vessels: Docker and runc Container Breakout Vulnerabilities - January 2024 | Snyk Labs"
url: "https://snyk.io/blog/leaky-vessels-docker-runc-container-breakout-vulnerabilities/"
final_url: "https://labs.snyk.io/resources/leaky-vessels-docker-runc-container-breakout-vulnerabilities/"
authors: ["Rory McNamara (@PsychoMario)"]
programs: ["Docker", "opencontainers (runc)"]
bugs: ["Container escape"]
publication_date: "2024-01-31"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 469
---

Snyk security researcher Rory McNamara, with the Snyk Security Labs team, identified four vulnerabilities — dubbed "Leaky Vessels" — in core container infrastructure components that allow container escapes. **An attacker could use these container escapes to gain unauthorized access to the underlying host operating system from within the container.** Once an attacker gains access to the underlying host operating system, they could potentially access whatever data was on the system, including sensitive data (credentials, customer info, etc.), and launch further attacks. Upon discovery and verification, the Security Labs team initiated the process for responsible disclosure of the vulnerabilities, starting by notifying Docker, who, after review, forwarded one of the vulnerabilities to the open source `runc` security group. The disclosure timeline is below. 

Because these vulnerabilities affect widely used low-level container engine components and container build tools, **Snyk strongly recommends that users check for updates from container build and runtime vendors, including Docker, Kubernetes vendors, cloud container services, and open source communities. You should upgrade systems running container engines and container build tools as soon as fixes are released by your providers.**

## About the vulnerabilities

On January 31, 2024, the [_maintainers_](https://github.com/opencontainers/runc) of `runc`, a CLI tool for spawning and running containers on Linux, announced a vulnerability ([_CVE-2024-21626_](https://security.snyk.io/vuln?search=CVE-2024-21626)) that allows for an order-of-operations container breakout centered around the `WORKDIR` command. Exploitation of this vulnerability can result in container escape to the underlying host operating system. This could occur by _running_ a malicious image or by _building_ a container image using a malicious Dockerfile or upstream image (i.e. when using `FROM`). The patched version, `runc` 1.1.12, was released on January 31, 2024, at around 3:00 PM EST, per the maintainers.

You can read more details about the vulnerability in this [_high-level_](/resources/cve-2024-21626-runc-process-cwd-container-breakout/) article, which outlines the `runc` vulnerability itself. In addition, Rory and the Snyk Labs team identified three other container escape vulnerabilities for a total of four vulnerabilities, listed below, with links to the corresponding CVEs and overview articles:

  * [_CVE-2024-21626_](https://security.snyk.io/vuln?search=CVE-2024-21626): [_runc process.cwd & leaked fds container breakout_](/resources/cve-2024-21626-runc-process-cwd-container-breakout/)

  * [ _CVE-2024-23651_](https://security.snyk.io/vuln?search=CVE-2024-23651): [_Buildkit Mount Cache Race_](/resources/cve-2024-23651-docker-buildkit-mount-cache-race/)

  * [ _CVE-2024-23653_](https://security.snyk.io/vuln?search=CVE-2024-23653): [_Buildkit GRPC SecurityMode Privilege Check_](/resources/cve-2024-23653-buildkit-grpc-securitymode-privilege-check/)

  * [ _CVE-2024-23652_](https://security.snyk.io/vuln?search=CVE-2024-23652): [_Buildkit Build-time Container Teardown Arbitrary Delete_](/resources/cve-2024-23652-buildkit-build-time-container-teardown-arbitrary-delete/)

## Tools available from Snyk to help detect these vulnerabilities

These vulnerabilities affect underlying container infrastructure and build tools rather than container images. [Snyk Container](https://snyk.io/product/container-vulnerability-management/) is designed to help developers eliminate vulnerabilities in their container images, and so these vulnerabilities are outside the scope of what Snyk's products are currently designed to evaluate. However, Snyk developed two open source tools that serve as **reference implementations** for detecting exploit attempts. Please note that these tools are not covered under [Snyk Support](https://snyk.io/services/), but rather as examples for the community. 

### Runtime exploit detection (leaky-vessels-runtime-detector)

The [_new Helios team_](https://snyk.io/news/snyk-acquires-runtime-data-pioneer-helios/) at Snyk has built a **runtime detection** tool for this vulnerability, which can be found at [_leaky-vessels-runtime-detector_](https://www.github.com/snyk/leaky-vessels-dynamic-detector), released under the Apache-2.0 license. This standalone tool, released under the Apache-2.0 license, provides a reference implementation for detecting the vulnerabilities as they are executed. The tool ties eBPF hooks to kernel- and user-level functions and to a package detector. This allows them to report invocations of container build and running containers if they match any patterns that indicate a possible exploitation attempt. Note that not all Linux distributions or versions support eBPF, and it's unlikely that customers would be able to leverage it on cloud service providers.

### Static container command detection (leaky-vessels-static-detector)

The second tool is a static analysis program, [_leaky-vessels-static-detector_](https://www.github.com/snyk/leaky-vessels-static-detector), also released under the Apache-2.0 license, that scans Dockerfiles and image layers to detect commands that appear to be trying to exploit the vulnerabilities. The tool provides JSON-format output that indicates if it has detected any questionable commands. It's important to note that each hit will need to be manually inspected to determine if they are indeed exploits as opposed to legitimate usage of container build commands.

We are releasing these two tools as open source to provide the community with _reference implementations_ for detecting potential exploit attempts. The runtime tool is likely to provide a higher level of confidence in findings than the static tool. However, given the nature of the exploits and the build commands, both tools will likely have some false negative and false positive results. The community can use the tools as examples to create their own tools, or run the tools in their environments. It's important to note that these tools neither fix the vulnerabilities nor block their exploitation, however, the tools will help to identify risk areas. The most prudent path is for customers to update impacted container orchestration platforms as patches become available. 

## Are there any active exploits?

The Snyk team has performed ad hoc checks of Dockerfiles from public registries based on the images we see being used most frequently. This is not exhaustive, but in our research, we did not find evidence suggesting that these vulnerabilities have been exploited. Snyk recommends that you continue monitoring your own environment and check your containers until patches are made available and deployed. Given the nature of the issues, Snyk has created two open source tools, outlined above, a dynamic tool to help demonstrate the detection of the actions from the vulnerabilities at runtime, and a static tool to scan images and Dockerfiles to serve as an indicator of potential exploit.

## How to prepare for remediation

Remediation should be done at the infrastructure and code tooling level. Look for announcements or releases, if applicable, from the provider or vendor of your container build and orchestration systems. You will likely need to update your Docker daemons and Kubernetes deployments, as well as any container build tools that you use in CI/CD pipelines, on build servers, and on your developers' workstations. It’s also important to screen existing containers using tools like the ones Snyk built to determine if your orchestration nodes or build infrastructure have already been impacted.

Here are some updates that we've collected from widely used tools and services:

**Date**| **Entity**| **Information**  
---|---|---  
31-Jan-2024| Maintainers of `runc`| Released [1.1.12](https://github.com/opencontainers/runc/releases/tag/v1.1.12) addressing relevant vulnerabilities  
31-Jan-2024| Snyk| Released the reference implementations [_leaky-vessels-dynamic-detector_](https://www.github.com/snyk/leaky-vessels-dynamic-detector) and [_leaky-vessels-static-detector_](https://www.github.com/snyk/leaky-vessels-static-detector) to the community to identify potentially questionable containers and images  
31-Jan-2024| containerd| Released version [_1.6.28_](https://github.com/containerd/containerd/releases/tag/v1.6.28)  
31-Jan-2024| Docker| Docker [_released_](https://www.docker.com/blog/docker-security-advisory-multiple-vulnerabilities-in-runc-buildkit-and-moby/) buildkit 0.12.5 and moby 25.0.2 and 24.0.9  
31-Jan-2024| GCP| [ _Released_](https://cloud.google.com/support/bulletins#gcp-2024-005) an update to `runc` 1.1.12  
31-Jan-2024| Ubuntu| [ _Released_](https://ubuntu.com/security/notices/USN-6619-1) an update to `runc` 1.1.12  
31-Jan-2024| AWS| [ _Released_](https://aws.amazon.com/security/security-bulletins/AWS-2024-001/) an update to `runc` 1.1.12  
  
## Anatomy of a disclosure

The timeline for vulnerabilities can be complex, especially when there are multiple entities involved. It's imperative that the disclosures are handled responsibly so bad actors don’t learn of them before fixes are readily available. 

In this case, the vulnerabilities were initially discovered two months ago. At that point, Snyk began the process for responsible disclosure. Here's a timeline of some key milestones in the process.

**Timeframe**| **Item**  
---|---  
Week of 20-Nov-2023| Rory McNamara initially discovered the vulnerabilities. He began the internal verification process and additional research to validate findings and build POC exploits.  
11-Dec-2023| Initial disclosure sent to Docker with all vulnerabilities, and Docker ACKed the same day.  
12-Dec-2023| Snyk received a request from Docker to forward the WORKDIR vulnerability to `runc`, as it was deemed their responsibility.  
13-Dec-2023| Rory was added as a Github Security Advisory (GHSA) collaborator for the Arbitrary Delete and `grpc` Docker/Buildkit vulns (both initially opened 11-Dec-2023).  
19-Dec-2023| Rory was added as GHSA collaborator to WORKDIR by `runc` (initially opened 11-Dec-2023).  
20-Dec-2023| Rory was added as GHSA collaborator for the cache race vulnerability.  
02-Jan-2024| `runc` CVE assigned (Github CNA).  
17-Jan-2024| `runc` sends an announcement to their security mailing list including the patches & embargo date of 31-Jan-2024.  
24-Jan-2024| Docker vulnerabilities CVEs assigned (GitHub CNA).  
31-Jan-2024| All four "Leaky Vessels" vulnerabilities announced publicly.  
31-Jan-2024| Runc released version 1.1.12 which fixes the vulnerabilities.  
31-Jan-2024| Snyk released the reference implementations [_leaky-vessels-dynamic-detector_](https://www.github.com/snyk/leaky-vessels-dynamic-detector) and [_leaky-vessels-static-detector_](https://www.github.com/snyk/leaky-vessels-static-detector) to the community to identify potentially questionable containers and images.  
  
Each step along the way involves collaboration within and between organizations — not only commercial organizations, but often the teams that maintain the components, which are often made up of a cross-section of the community.

## About Snyk's Security Labs team

Snyk's Security Labs team has helped to responsibly disclose over [_3,200 vulnerabilities_](https://security.snyk.io/disclosed-vulnerabilities) in key packages across a variety of ecosystems. We work closely with open source package maintainers in order to ensure all vulnerabilities are responsibly and efficiently addressed. Our security expertise is one of the reasons that Snyk is trusted by so many [_big names_](https://snyk.io/platform/security-intelligence/) across the security industry. If you find what you think is a vulnerability and don't know how to proceed to responsibly disclose it, [_fill out this form_](/vulnerability-disclosure/) and our teams can help.

## Was Snyk impacted?

For information about how Snyk addresses vulnerabilities in our own environment, visit the [_Snyk Trust Portal_](https://trust.snyk.io).

## Summary

We will update this blog as we learn more, and we'll be holding a webinar Tuesday, February 6 at 11 AM ET for [_Leaky Vessels Container Breakout Vulnerabilities - What You Need to Know_](https://go.snyk.io/240206_leaky_vessels_container_breakout_vulnerabilities.html). Snyk technical experts will provide an in-depth technical review of one of the Leaky Vessels vulnerabilities, what caused it, how it can be exploited, and, most importantly, how it can be mitigated through upgrades and monitoring.

We encourage you to reach out with any questions you have about the vulnerabilities. For the open source tools, create a GitHub ticket on the respective tools ([_dynamic-detector_](https://www.github.com/snyk/leaky-vessels-dynamic-detector/issues) and [_static-detector_](https://www.github.com/snyk/leaky-vessels-static-detector/issues)) or reach out on the [_Snyk community Discord_](https://snyk.io/community/). 

For more information, about Leaky Vessels, check out:

  * [Leaky Vessels — runc Vulnerability Explained (YouTube)](https://www.youtube.com/watch?v=eu684ocRmDA)

  * [Leaky Vessels deep dive: Escaping from Docker one syscall at a time (article)](/resources/leaky-vessels-container-vuln-deep-dive/)

  * [Hands-on lesson: runc process.cwd Container breakout vulnerability (Snyk Learn)](https://learn.snyk.io/lesson/cve-2024-21626-runc-process-cwd-container-breakout/)

_This article is provided for informational purposes only. Snyk is not responsible for any errors or omissions, or for the results obtained from the use of this information._

## Change log

  * January 31, 2024, 3 p.m. ET: Initial release

  * January 31, 2024, 6 p.m. ET: Added CVE URLs; added updates from AWS, containerd, GCP, Docker, and Ubuntu

  * Feb 7, 2024, 1 p.m. ET: YouTube video and deep dive links added to Summary section

  * Feb 8, 2024, 10 a.m. ET: Snyk Learn lesson added to Summary section
