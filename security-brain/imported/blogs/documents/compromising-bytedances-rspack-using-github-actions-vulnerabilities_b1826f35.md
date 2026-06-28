---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-31_compromising-bytedances-rspack-using-github-actions-vulnerabilities.md
original_filename: 2024-05-31_compromising-bytedances-rspack-using-github-actions-vulnerabilities.md
title: Compromising ByteDance’s Rspack using GitHub Actions Vulnerabilities
category: documents
detected_topics:
- supply-chain
- sso
- idor
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- supply-chain
- sso
- idor
- command-injection
- otp
- rate-limit
language: en
raw_sha256: b1826f356b5e1935799a109984970bd54c94b222144955e063d67e840dee0dce
text_sha256: 64cd25b6f66c6bf04e2f25f7d4eb4f22a0129129d7a6f444bfc9e60c6f1a7f5f
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Compromising ByteDance’s Rspack using GitHub Actions Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-31_compromising-bytedances-rspack-using-github-actions-vulnerabilities.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, idor, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `b1826f356b5e1935799a109984970bd54c94b222144955e063d67e840dee0dce`
- Text SHA256: `64cd25b6f66c6bf04e2f25f7d4eb4f22a0129129d7a6f444bfc9e60c6f1a7f5f`


## Content

---
title: "Compromising ByteDance’s Rspack using GitHub Actions Vulnerabilities"
page_title: "Compromising ByteDance's Rspack using GitHub Actions Vulnerabilities | Praetorian"
url: "https://www.praetorian.com/blog/compromising-bytedances-rspack-github-actions-vulnerabilities/"
final_url: "https://www.praetorian.com/blog/compromising-bytedances-rspack-github-actions-vulnerabilities/"
authors: ["Adam Crosser", "John Stawinski"]
programs: ["ByteDance (Rspack)"]
bugs: ["CI/CD", "Pwn Request"]
publication_date: "2024-05-31"
added_date: "2024-06-05"
source: "pentester.land/writeups.json"
original_index: 268
---

Skip to content

**Meet Constantine – Find Mythos-level vulnerabilities in your code. It proves them, patches them, PRs them back. Autonomously.**

[ Download Datasheet ](/resources/constantine-datasheet/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

  * Platform  Close Platform Open Platform

#### [Praetorian Guard Platform](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Services  Close Services Open Services

#### [Penetration Testing Services](/penetration-testing/)

  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)
  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)

#### [Advanced Offensive Security](/advanced-penetration-testing/)

  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)
  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)

#### [Continuous Offensive Security](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Why Praetorian  Close Why Praetorian Open Why Praetorian

#### [Customer Case Studies](/customer-success-in-cybersecurity/)

  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)
  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)

#### Resources

  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)
  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)

#### Use Cases

  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)
  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)

  * About  Close About Open About

#### [About Praetorian](/praetorian-offensive-cybersecurity-company/)

  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)
  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)

#### [Join Praetorian](/careers/#job-opening)

  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)
  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)

  * [ Platform Demo  ](/praetorian-guard-demo/)

  * [ Contact Us  ](/contact-us/)

  * [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

# Compromising ByteDance’s Rspack using GitHub Actions Vulnerabilities

  * [Adam Crosser](https://www.praetorian.com/author/adam-crosser/), [John Stawinski](https://www.praetorian.com/author/john-stawinski/)
  * [ May 31, 2024 ](https://www.praetorian.com/blog/2024/05/31/)

![Figure 1: We observed that the “Release Canary” workflow was configured to run on issue comment and would execute if the issue comment contained the keyword “!canary”.](https://www.praetorian.com/wp-content/uploads/2024/06/1-release-canary-workflow.png)

## Overview

Recently, we identified several critical Pwn Request vulnerabilities within GitHub Actions used by the [Rspack](https://github.com/web-infra-dev/rspack/) repository. These vulnerabilities could allow an external attacker to submit a malicious pull request, without the requirement of being a prior contributor to the repository, and compromise the following secrets:

  * NPM Deployment Token Compromise: Exploitation of the Pwn Request vulnerability allowed us to compromise the NPM deployment key used to deploy Rspack. This NPM token was used to push new Rspack packages (80,000 weekly downloads).
  * GitHub Personal Access Token (PAT) Compromised: We leveraged persistent access to the self-hosted runner to compromise a privileged GitHub PAT with administrative privileges on the Rspack GitHub repository.

_Background: Rspack is a Rust-based JavaScript bundler that implements functionality similar to WebPack for JavaScript bundling and packaging. Rspack aims to differentiate itself by acting as a highly performant version of WebPack and even claims that it is up to five to ten times faster than WebPack. This is primarily because Rspack is written in Rust and designed from the ground up with performance in mind._

Had an attacker exploited these vulnerabilities, they could have leveraged this access to perform a supply chain attack against downstream users of Rspack. This is quite serious as Rspack is often leveraged within CI/CD pipelines and on developer machines. In both cases, these systems are often quite privileged, and we’ve frequently seen that compromise of CI/CD infrastructure allows an attacker to gain privileged access to production environments. After assessing the impact of the vulnerability, we observed that the Rspack NPM package had over eighty thousand weekly downloads.

We decided to release this blog post on the issues we identified in Rspack to raise awareness of Pwn Request vulnerabilities, especially when a repository also uses self-hosted runners. Despite its high impact and prevalence, this particular bug class remains underappreciated within the security and broader engineering and development communities.

_As part of our vulnerability disclosure process, we promptly reported these vulnerabilities to ByteDance after the initial discovery and confirmation of the issues. In this case, we reported the vulnerability to the core RSPack team who remediated the problems within an hour of disclosure. ByteDance also performed an incident response, which involved rotating all the secrets associated with impacted repositories and confirming that no prior exploitation of the issues had occurred before the research Praetorian performed._

## What is a Pwn Request vulnerability?

Pwn Request vulnerabilities arise from scenarios where an attacker submits malicious input to a target repository and can trigger the execution of attacker-controlled code within a privileged context of the Github action. In this case, we identified two GitHub actions that ran on issue comment events and would checkout and run code from an attacker-controlled branch if a specific keyword was included in a pull request comment.

If you are interested in learning more about these vulnerabilities and GitHub action security, Adnan Khan has previously published an excellent blog post on the Praetorian blog titled [_Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More_](https://www.praetorian.com/blog/pwn-request-hacking-microsoft-github-repositories-and-more/). Jaroslav Lobacevski also published [an excellent three-part series](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/) on the Github securitylab blog, which deep dives into securing GitHub actions and provides some useful additional context on Pwn Request vulnerabilities.

## Identifying the Vulnerable GitHub Actions

The two vulnerable workflows we identified were the “Release Canary” and “Diff Assets” workflows. Both of these workflows functioned in a similar manner by running any time a user commented a keyword of “!diff” or “!canary” on an open pull request. In both cases, these workflows would checkout and run code from an attacker-controlled branch.

The diff workflow used a privileged PAT and ran on a self-hosted runner, while the canary workflow was passed a privileged NPM deployment secret that could be used to deploy new versions of the Rspack NPM package. First, we will walk through the “Release Canary” workflow exploitation.

## Analyzing the Release Canary Workflow

When examining the “Release Canary” workflow, we noticed that the workflow ran on an issue comment and then performed a check that the comment ran on a pull request and contained the keyword “!canary” in the comment body (see Figure 1).

We then observed that the workflow would check out the branch from the submitted pull request and execute a script named “x” with an NPM token secret passed as an environment variable. This execution flow would allow an attacker to modify the “x” script within their malicious branch and exfiltrate the NPM deployment secret and GitHub secret passed to the workflow (see Figure 2).

![Figure 1: We observed that the “Release Canary” workflow was configured to run on issue comment and would execute if the issue comment contained the keyword “!canary”.](https://www.praetorian.com/wp-content/uploads/2024/06/1-release-canary-workflow.png)

_Figure 1: We observed that the “Release Canary” workflow was configured to run on issue comment and would execute if the issue comment contained the keyword “!canary”._

![Figure 2: We observed that the workflow, when executed, would first checkout the code from the attacker’s pull request and run a script named “x” from the attacker branch with the deployment NPM token and a privileged GitHub secret with write access to the repository.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201034%20942'%3E%3C/svg%3E)

_Figure 2: We observed that the workflow, when executed, would first checkout the code from the attacker’s pull request and run a script named “x” from the attacker branch with the deployment NPM token and a privileged GitHub secret with write access to the repository._

## Exploiting the “Release Canary” Workflow

At this point, we could submit our own malicious pull request with a modified “x” script and exfiltrate all the environment variables passed to the script within the workflow to a remote Burp collaborator server. We submitted our pull request and commented “!canary” to trigger execution of the workflow. Within a few minutes we obtained the NPM deployment secret and a GITHUB_TOKEN assigned to the workflow with write access to the repository and the ability to modify releases (see Figure 3). We also demonstrated the ability to backdoor GitHub releases (see Figure 4) and compromise the Rspack NPM package (see Figure 5).

![Figure 3: We successfully exfiltrated the NPM deployment token for Rspack by exploiting the Pwn Request vulnerability within the “Release Canary” workflow.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201044%20702'%3E%3C/svg%3E)

_Figure 3: We successfully exfiltrated the NPM deployment token for Rspack by exploiting the Pwn Request vulnerability within the “Release Canary” workflow._

![Figure 4: We demonstrated the ability to modify the releases section of the Rspack repository, but then promptly reverted the change to avoid alarming end-users of the software by modifying the release](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201046%20430'%3E%3C/svg%3E)

_Figure 4: We demonstrated the ability to modify the releases section of the Rspack repository, but then promptly reverted the change to avoid alarming end-users of the software by modifying the release_

![Figure 5: We observed that Rspack averaged around seventy to eighty-thousand weekly downloads.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201050%20738'%3E%3C/svg%3E)

_Figure 5: We observed that Rspack averaged around seventy to eighty-thousand weekly downloads._

## Exploiting the Diff Assets Workflow

Pwn Request exploitation typically does not require the use of self-hosted runners. However, using self-hosted runners on a repository can increase the impact of a Pwn request vulnerability. To investigate this impact, we compromised a self-hosted runner used by the Diff Assets workflow within the Rspack repository. Ultimately, we could execute the following steps, which led to the compromise of a GitHub Personal Access Token (PAT) with complete administrative privileges over the Rspack repository.

### 1\. Install Persistence

We exploited a Pwn Request vulnerability within the Diff Assets workflow, similar to the Release Canary workflow, to install persistence on the self-hosted runner using the [Runner-on-Runner](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/#preparing-the-payload) (RoR) C2 technique (see Figure 6).

![Figure 6: We achieved code execution on the non-ephemeral self-hosted runner by using our own GitHub self-hosted runner for command and control.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201012%20690'%3E%3C/svg%3E)

_Figure 6: We achieved code execution on the non-ephemeral self-hosted runner by using our own GitHub self-hosted runner for command and control._

### 2\. Investigate Docker Containers

While investigating Docker containers, we noticed several containers on the self-hosted runner processing workflows from other GitHub Actions jobs within the Rspack repository (see Figure 7).

![Figure 7: The ec2-linux-* Docker containers were self-hosted runners that executed workflows from the Rspack repository.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201026%20232'%3E%3C/svg%3E)

_Figure 7: The ec2-linux-* Docker containers were self-hosted runners that executed workflows from the Rspack repository._

### 3\. Trigger the “Diff Assets” workflow

The “Diff Assets” workflow executed within a Docker container on the compromised self-hosted runner using the secrets.Rspack_REPORT_ACCESS_TOKEN GitHub secret (see Figure 8).

![Figure 8: We found a workflow that was passed a privileged secret and ran on a self-hosted runner, but wasn’t vulnerable to a Pwn Request vulnerability.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201012%20314'%3E%3C/svg%3E)

_Figure 8: We found a workflow that was passed a privileged secret and ran on a self-hosted runner, but wasn’t vulnerable to a Pwn Request vulnerability.___

We couldn’t steal this secret directly with the Pwn request, but we could trigger this workflow and then tamper with the workflow execution during run-time, which would include the GitHub secret. We triggered the workflow with the Issue Comment trigger.

### 4\. Exfiltrate Environment Variables

Using “Docker exec” on the compromised self-hosted runner, we exfiltrated the container’s environment variables by executing the “Diff Assets” workflow. The Rspack_REPORT_ACCESS_TOKEN was included in these environment variables (see Figure 9).

![Figure 9: We successfully obtained the GitHub secret associated with the workflow by leveraging our position on the self-hosted runner.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201026%20518'%3E%3C/svg%3E)

_Figure 9: We successfully obtained the GitHub secret associated with the workflow by leveraging our position on the self-hosted runner._

### 5\. Analyzing PAT Access with [Gato](https://github.com/praetorian-inc/gato)

The PAT belonged to a user with access to multiple GitHub organizations. Notable access included administrative control over the Rspack repository (see Figure 10) and administrative privileges over entire GitHub organizations, including the [Rspack-contrib](https://github.com/rspack-contrib) organization. For detailed explanations of GitHub Actions post-exploitation techniques similar to the ones used during this attack, check out the recent critical [TensorFlow](https://www.praetorian.com/blog/tensorflow-supply-chain-compromise-via-self-hosted-runner-attack/) and [PyTorch](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/) attack walkthroughs.

![Figure 10: We used Gato to enumerate the PAT’s permissions.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201036%20544'%3E%3C/svg%3E)

_Figure 10: We used Gato to enumerate the PAT’s permissions._

## How can I Detect these Issues Automatically?

We have integrated our open-source [Gato](https://github.com/praetorian-inc/gato) utility into our [Chariot offensive security platform](/proactive-cybersecurity-technology/). This allows Chariot to continually perform enumeration of GitHub repositories to identify common configuration issues, such as the usage of self-hosted runners on public repositories. Adnan Khan has also been developing Gato-X, an experimental fork of Gato that can automatically identify Pwn Request vulnerabilities at scale. We plan on integrating Gato-X into the platform once it is released.

![Figure 11: An example screenshot where we leveraged Chariot to enumerate public repositories with self-hosted runners configured across a variety of GitHub organizations.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201058%20592'%3E%3C/svg%3E)

_Figure 11: An example screenshot where we leveraged Chariot to enumerate public repositories with self-hosted runners configured across a variety of GitHub organizations._

## Remediation

After reaching out to Rspack maintainers, they quickly removed the vulnerable workflows from the Rspack repository. The repository still utilizes self-hosted runners, which could heighten the impact of future vulnerabilities if they are discovered.

## Conclusion

In this article, we discussed some of the dangers inherent to Pwn Request vulnerabilities and how self-hosted runners can be exploited to harvest secrets from other workflows that share the self-hosted runner server. We wanted to continue to highlight the risk of these vulnerabilities, given their severity and prevalence combined with a general lack of awareness of these vulnerabilities within the broader developer and security communities. We also provided some additional resources for those looking to learn more about these vulnerabilities and how they can be exploited.

## About the Authors

![Adam Crosser](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Adam Crosser](https://www.praetorian.com/author/adam-crosser/)

Adam is an operator on the red team at Praetorian. He is currently focused on conducting red team operations and capabilities development.

[ ](https://www.linkedin.com/in/adam-crosser-366263265)

![John Stawinski](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [John Stawinski](https://www.praetorian.com/author/john-stawinski/)

John is a Red Team Operator at Praetorian, focused on covert operations, CICD + supply chain security, corporate engagements, and public vulnerability research.

[ ](https://www.linkedin.com/in/john-stawinski-72ba87191/)

## Catch the Latest

Catch our latest exploits, news, articles, and events.

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 19, 2026

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

## [GhostPack Necromancy: Reforging C# Tools with WasmForge](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[ Read More ](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 17, 2026

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

## [FreeBSoD: Leveraging Language Models to Find and Exploit Kernel Bugs (Part 1 of 2)](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[ Read More ](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

  * [Uncategorized](https://www.praetorian.com/category/uncategorized/)

  * June 16, 2026

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## [Sharing is Caring: SMB Secret Scanning with Sulla](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

[ Read More ](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## Ready to Discuss Your Next Continuous Threat Exposure Management Initiative?

Praetorian’s Offense Security Experts are Ready to Answer Your Questions

[ Get Started ](/contact-us/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

##### [Praetorian Guard Platform](https://www.praetorian.com/guard)

  * [ Continuous Threat Exposure Management ](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [ Attack Surface Management ](https://www.praetorian.com/guard/attack-surface-management/)
  * [ Vulnerability Management ](/chariot/vulnerability-management/)
  * [ Cyber Threat Intelligence ](/chariot/threat-intelligence/)
  * [ Continuous Penetration Testing ](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [ Breach and Attack Simulation ](https://www.praetorian.com/guard/breach-attack-simulation/)

##### Professional Services

  * [ AI/ML Penetration Testing ](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [ Application Penetration Testing ](/services/application-penetration-testing/)
  * [ Assumed Breached Exercise ](/services/assumed-breached-exercise/)
  * [ Attack Path Mapping ](https://www.praetorian.com/resources/attack-path-mapping/)
  * [ Automotive Penetration Testing ](/services/automotive-penetration-testing/#)
  * [ CI/CD Security Engagement ](/services/ci-cd-security-engagement/)
  * [ Cloud Penetration Testing ](/services/cloud-penetration-testing/)
  * [ IoT Penetration Testing ](/services/iot-penetration-testing/)
  * [ Network Penetration Testing ](/services/network-penetration-testing/)
  * [ NIST CSF Benchmark ](/services/nist-csf-benchmark/)
  * [ Purple Team ](/services/purple-team/)
  * [ Red Team ](/services/red-team/)

##### Use Cases

  * [ Bug Bounty Cost Reduction ](/services/bug-bounty-cost-reduction/)
  * [ FDA Testing and Monitoring ](/services/fda-testing-monitoring/)
  * [ Mergers and Acquisitions ](/services/mergers-acquisitions/)
  * [ Ransomware Prevention ](/services/ransomware-prevention/)
  * [ Rogue IT Identification ](/services/rogue-it-identification/)
  * [ Tool and Vendor Consolidation ](/services/tool-vendor-consolidation/)
  * [ Vendor Risk Management ](https://www.praetorian.com/services/vendor-risk-management/)

##### Company

  * [ About Us ](https://www.praetorian.com/about-us/)
  * [ Leadership Team ](https://www.praetorian.com/leadership-team/)
  * [ Press Releases ](/news/press-release/)
  * [ In the News ](/news/news)
  * [ Contact Us ](https://www.praetorian.com/contact-us/)
  * [ Resource Library ](https://www.praetorian.com/resources/)
  * [ Security Blog ](/blog/)
  * [ People Ops Blog ](/people-ops/)
  * [ Careers ](https://www.praetorian.com/careers/)
  * [ Culture ](https://www.praetorian.com/work-at-praetorian/)
  * [ Survival Kit ](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)

### Subscribe to our Newsletter

Catch our latest exploits, news, articles, and events.

[Privacy Policy](/privacy-policy/) | [Responsible Disclosure Policy](/responsible-disclosure-policy/) | [Terms of Service](/terms-of-service/) | [Terms and Conditions](/terms/)

Copyright © 2025. All Rights Reserved.

[ Linkedin-in ](https://www.linkedin.com/company/praetorian/) [ X-twitter ](https://twitter.com/praetorianlabs) [ Facebook-f ](https://www.facebook.com/praetorianlabs) [ Github ](https://github.com/praetorian-inc) [ Youtube ](https://www.youtube.com/user/PraetorianLabs)
