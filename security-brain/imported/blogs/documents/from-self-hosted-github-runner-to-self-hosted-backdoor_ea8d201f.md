---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-26_from-self-hosted-github-runner-to-self-hosted-backdoor.md
original_filename: 2022-10-26_from-self-hosted-github-runner-to-self-hosted-backdoor.md
title: From Self-Hosted GitHub Runner to Self-Hosted Backdoor
category: documents
detected_topics:
- supply-chain
- access-control
- mfa
- api-security
- sso
- saml
tags:
- imported
- documents
- supply-chain
- access-control
- mfa
- api-security
- sso
- saml
language: en
raw_sha256: ea8d201fd4e6694aee14f726062f27245e91fe6872d1ae24ff4367cdf3eda076
text_sha256: b954a962b65ad16e0bd429917480707c2df73ec20476a3479f7018949331cf70
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# From Self-Hosted GitHub Runner to Self-Hosted Backdoor

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-26_from-self-hosted-github-runner-to-self-hosted-backdoor.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, mfa, api-security, sso, saml
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `ea8d201fd4e6694aee14f726062f27245e91fe6872d1ae24ff4367cdf3eda076`
- Text SHA256: `b954a962b65ad16e0bd429917480707c2df73ec20476a3479f7018949331cf70`


## Content

---
title: "From Self-Hosted GitHub Runner to Self-Hosted Backdoor"
page_title: "From Self-Hosted GitHub Runner to Self-Hosted Backdoor | Praetorian"
url: "https://www.praetorian.com/blog/self-hosted-github-runners-are-backdoors/"
final_url: "https://www.praetorian.com/blog/self-hosted-github-runners-are-backdoors/"
authors: ["Adnan Khan (@adnanthekhan)", "Mason Davis", "Matt Jackoski"]
programs: ["GitHub"]
bugs: ["CI/CD", "Lateral movement", "Post-exploitation"]
publication_date: "2022-10-26"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 1983
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

  * [Corporate Security](https://www.praetorian.com/category/corporate-security/)

# From Self-Hosted GitHub Runner to Self-Hosted Backdoor

  * [Adnan Khan](https://www.praetorian.com/author/adnan-khan/), [Mason Davis](https://www.praetorian.com/author/mason-davis/), [Matt Jackoski](https://www.praetorian.com/author/matt-jackoski/)
  * [ October 26, 2022 ](https://www.praetorian.com/blog/2022/10/26/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/Screen-Shot-2022-10-25-at-3.48.00-PM.png)

## Overview

Continuous Integration and Continuous Delivery (CI/CD) systems are powerful and configurable tools within modern environments. At Praetorian, we are seeing organizations migrate to SaaS solutions like GitHub (GitHub.com) as their source code management and CI/CD solution, instead of on-premises tools like BitBucket, Bamboo, and Jenkins. On our Red Team engagements , we routinely employ advanced tradecraft to reach our attack objectives. Recently, we have successfully targeted CI/CD environments to gain expanded network access.

This post will outline how compromised GitHub access can be used to pivot into an organization’s internal environment and often lead to an attacker achieving their objectives, with little to no visibility into an attacker’s actions until it is too late. Our focus is to outline a threat model for organizations that utilize GitHub and leverage self-hosted runners in conjunction with GitHub Actions. We will additionally provide recommendations for security controls that an organization could implement to protect against attackers seeking to conduct this style of attack.

## **Primer**

GitHub is unique in that its primary offering is an Internet facing SaaS tool that provides source control management and a CI/CD system called GitHub Actions. Furthermore, [ GitHub offers several paid solutions to customers](https://github.com/pricing), but we found that many features that are essential to building effective security controls require the most expensive plan. Praetorian leveraged weak security configurations and GitHub’s inherently weak security model to conduct an attack that led to a persistent foothold within an organization’s internal network.

### **GitHub Actions**

GitHub Actions allow the execution of code specified within workflows as part of the CI/CD process. GitHub Actions can be executed on ephemeral runners hosted within Azure or on self-hosted runners executing the GitHub Actions agent software. Many organizations opt to utilize self-hosted runners due to cost savings and integration with internal network infrastructure for package deployments.

If not configured correctly, self-hosted runners can lead to devastating security impacts for an organization. GitHub’s documentation makes no claims to security here; rather, it clearly states:

“Self-hosted runners for GitHub do not have guarantees around running in ephemeral clean virtual machines, and can be persistently compromised by untrusted code in a workflow.”

### **GitHub Access**

##### **Traditional Authentication**

GitHub allows logging in via traditional username and password authentication through the web interface as well as through the official GItHub command line interface. Users can configure multi-factor authentication (MFA) when logging in through the CLI or web application.

##### **Personal Access Tokens**

GitHub classic Personal Access Tokens (PAT), under their current implementation, are a security risk for organizations. The problem stems from the fact that GitHub connects tokens to a _user,_ not the organization. If a token is generated with the **repo** scope, that token will have the same access that the user has to _all_ repositories accessible by that user. Suppose the user is an administrator to a private repository within their employer’s GitHub organization, but they created a token to work on a personal project at home. In that case, the token will still have administrative access to their employer’s GitHub repository.

To make matters worse, when a classic PAT exists for a GitHub Teams customer, restricting whether a user’s PAT can work on the organization’s repositories is impossible. Likewise, an organization has no way to inventory valid classic PATs associated with their users.

## **The Attack**

On one of our Red Team engagements, we obtained access to a GitHub personal access token associated with a machine account. There are many different ways that a developer could accidentally disclose a PAT that they have generated, such as phishing, personal laptop compromise, and accidental inclusion in command line logs.

This token possessed the **repo** scope. Our Red Team then identified and exploited the use of self-hosted runners and created a malicious GitHub Actions workflow to obtain persistence on the runner. This opened the door for privilege escalation and lateral movement.

Figure 1 shows our complete attack path.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20301'%3E%3C/svg%3E)

_Figure 1: A diagram of our attack path using GitHub PATs._

**Attack Steps:**

  1. Obtained GH access token
  2. Identified use of Self-Hosted Runners
  3. Updated existing GitHub Action to run a payload
  4. Triggered malicious GH action
  5. Received Malware Check-in to Praetorian C2

This organization grouped the GitHub runners into a pool for the entire organization. Any developer in the organization could create a project that utilized GitHub Actions. Upon a trigger event under this configuration, an available runner would pick up the workflow and begin executing code specified in the YAML file specified within the repository. By default, all repositories within an organization have GitHub Actions enabled, and the default configuration is to have a single runner group for the organization.

### **Enumeration**

##### **Exposed Tokens**

As we see in Figure 2, GitHub states clearly that PATs are sensitive, but let us explore the actions that could allow a PAT to be leaked or disclosed.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20578%20212'%3E%3C/svg%3E)

_Figure 2: GitHub’s warning regarding the sensitivity of personal access tokens._

  * **Git Clone Operations:** When a user clones a repository with HTTPS using a PAT, the token is stored in plaintext within the .git folder. Simply running `git remote -v` will disclose the token. Suppose a developer clones a repo they are working on with their personal account and shares it, not knowing that the token is saved, as Figure 3 demonstrates. In that case, they could inadvertently provide access to their employer’s repositories. An example of a `git clone` using a GitHub token for authentication is

  
  
  git clone https://[[email protected]](/cdn-cgi/l/email-protection)/org/repo

  * **GitHub API calls and security logging:** A user could make GitHub API calls with curl, and have their commands logged by an EDR agent, which could then be ingested into a SIEM.
  * **Malware:** GitHub tokens start with the recognizable string ‘ghp_’, as Figure 3 demonstrates. Malware authors could write custom malware to search bash history and locally-cloned git repos for tokens and send it to the attacker. This is very simple to write and is unlikely to trigger any detections for custom code. An attacker even could sneak this into legitimate tools that developers are likely to use, such as a malicious Vim plugin.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20589%2053'%3E%3C/svg%3E)

_Figure 3: GitHub tokens start with the ‘ghp_’ string, which are stored on the filesystem for repositories cloned using HTTPS._

The red team had retrieved a valid GH token through an exposure vulnerability. We were then able to authenticate to the organization GH instance and navigate through available repositories. We eventually discovered a repository that contained secrets in an old commit. One of them was another PAT for the same user, which contained the **admin:org** , **repo** , and **workflow** scopes. This broadened the type of attacks that we could utilize.

The **repo** scope alone cannot update or create new workflows, but _can_ run a workflow by updating a branch that is already configured to execute workflows or by creating a new branch. If a workflow file calls a shell script or Makefile within the repo as part of a build step, then an attacker can simply update that file in order to execute code they control.

### **Payload Creation**

Our Red Team identified that certain self-hosted runners had Docker installed, and the user running the GitHub runner process was a member of the _docker_ group. This meant that the host could execute a docker container, which could provide root-level access to the host depending on the invocation. Our Red Team utilized this privilege escalation path to obtain root access on the self-hosted runners.

This also provided some degree of evasion from EDR solutions present on the host. We utilized an Alpine Linux Docker container and configured it to download a malicious payload we hosted on GitHub in an encrypted zip. Furthermore, if an attacker executes a Docker container in detached mode, it will persist beyond the execution of the job and will prevent the runner from hanging.

### **Persistence**

We achieved persistence by using Docker; however, we could still choose to run a task in the background from a GitHub Action. Typically, a GitHub Action will clean up all orphan processes upon termination. This theoretically would prevent an attacker from simply executing a background task with nohup or disown. A little-known environment variable does allow processes initiated by the workflow to persist beyond the initial execution, though.

By setting the RUNNER_TRACKING_ID environment variable to 0, the GitHub Actions runner will not attempt to clean up any child process still running after the action completes. An attacker can use this to spawn a persistent background process to obtain a foothold on the action runner itself.

If a workflow calls a shell script, adding `export RUNNER_TRACKING_ID=0` before executing any command will prevent the cleanup step from terminating the orphan process. To test this, we had our runner execute the following lines of code within a shell script:
  
  
  export RUNNER_TRACKING_ID=0 && nohup python3 -c "import time; time.sleep(100)" &
  
  
  sleep 25

While the sleep command executed, the Python script ran with the parent process specified. Termination of the sleep 25 killed the parent process, but the Python process continued to run with pid 1 as a parent.
  
  
  ghrunner    2501       1  0 19:33 pts/0    00:00:00 python3 -c import time; time.sleep(100)
  
  
  ghrunner    2501    2499  0 19:33 pts/0    00:00:00 python3 -c import time; time.sleep(100)

### **Execution**

To trigger our attack, we identified a repository with enabled GitHub Actions and an existing workflow. We created a new branch within that repository and updated the workflow YAML file to run only on self-hosted runners. This workflow file ran bash code that downloaded a payload from an external GitHub repository that we controlled and executed a payload. With the **repo** scope, we could find code called by the existing YAML file and modify it to perform our malicious actions.

This led to an implant callback from within our client’s environment. We utilized this foothold to move laterally and gain substantial access within that environment.

### **Cleanup**

After executing our payload, we utilized GitHub API calls to delete the workflow runs associated with our branch and the branch itself. These API calls required the **workflow** scope. However, an attacker could simply skip this step.

## **Detection & Mitigation**

Due to GitHub restricting security features based on plan tier, some recommendations will vary based on the plan in use. Pertinent aspects of GitHub’s security guide are available for reference [ here](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions) .

### **Logging Blind Spots**

Organizations that use GitHub have no visibility into traffic to GitHub.com unless GitHub exposes that information in their audit logs. This is because, as a Saas solution, all connections go directly to GitHub.com.

We performed a thorough evaluation of GitHub’s audit logging functionality prior to conducting the self-hosted runner attack. We saw the following two issues with GitHub’s audit logging:

  * Lack of visibility into GET requests made against the GitHub API with PATs
  * Restriction of what we view as essential logging capabilities

The first issue with GitHub’s audit log is that it currently does not capture events where an attacker is simply querying information about an organization. If an attacker obtains a PAT with _no other knowledge about it_ , they can use a combination of REST API requests and git operations to learn:

![](https://www.praetorian.com/wp-content/uploads/2024/06/Screen-Shot-2022-10-25-at-3.48.00-PM.png)

This leads into the next issue: many security features that Praetorian considers essential for an organization are locked behind GitHub’s highest price tier, as Figure 4 highlights.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20316'%3E%3C/svg%3E)

_Figure 4: GitHub documentation noting that certain logging capabilities are available only at the most expensive tier._

##### Implications for Teams Plan Users

The more affordable Teams plan lacks certain audit logging features that would enable an organization’s SoC to learn of an attacker’s actions before it is too late. In particular, any clone, fetch, or push actions do not generate audit log events for customers that use Teams’ price tier. This means that if an attacker obtained a GitHub PAT that allowed access to a private organization on the Teams plan, they could clone _every single_ _repository_ within that organization without the generation of audit log events.

Within the attack chain, the time between the attacker conducting the first clone operation and executing their attack is the defender’s largest detection window. This is where an attacker will be enumerating repositories for existing workflows and determining what code they can modify, as Figure 5 shows.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20649'%3E%3C/svg%3E)

_Figure 5: The series of steps an attacker must take, with red denoting the steps that bracket the optimal detection window._

Furthermore, the REST API is only enabled for Enterprise customers, while other organizations must utilize the web interface to view audit logs. This makes it impossible for organizations on the Teams plan to develop a real-time detection to alert defenders of possible malicious activity.

Similarly to how the git clone, push, and fetch events required the more expensive plan, the workflow events associated with executing a GitHub action are not viewable by users on the Teams plan. [ To query them](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/orgs#get-the-audit-log-for-an-organization) , the user must have access to the Audit Log API under the Enterprise plan. Following is an example query that retrieves audit log events associated with workflow run creations:
  
  
  '''
  
  curl 
  
    -H "Accept: application/vnd.github+json" 
  
    -H "Authorization: Bearer <YOUR-TOKEN>" 
  
    https://api.github.com/orgs/ORG/audit-log?phrase=action:workflows.created_workflow_run
  
  '''

### **Pay-gated Security Strikes Again**

Only organizations on the Enterprise Plan can create multiple runner groups. Organizations using the Teams plan can either add runners to this default group or configure them on a per-repository basis, as seen in Figure 6.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20175'%3E%3C/svg%3E)

_Figure 6: The option to use either a default group or one-off configuration for runners under the GitHub Teams plan._

This restriction is unfortunate because it creates a situation where developer productivity and security controls are placed directly at odds.

### **Fine-Grained Access Tokens**

On October 18th, 2022, GitHub announced a beta for[ **fine-grained access tokens**](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/) . These tokens allow granular permissions settings, organization-level approval, and insight into tokens.

This is a step in the right direction for organizations because it shifts the visibility of tokens that apply to an organization from user accounts to the organization itself. Unfortunately, this feature currently is an all-or-nothing setting. An administrator can disable all PATs for an organization, but there is no way to retain classic PAT functionality to facilitate a smooth transition of systems that currently rely on them while disabling them for standard organization members.

### **General**

  * Adopt a zero-trust security posture concerning self-hosted runners. Minimize access to the broader internal network.
  * Configure an egress allow-list policy for connections from the runner to the Internet.
  * Re-cycle runners routinely. When leveraging a runner pool, developing tooling to disable, delete, and re-register runners can prevent attackers from establishing a long-term foothold on a single runner. GitHub’s API can be used to programmatically provision runners. Combining this with containerization can allow quickly cycling runners with little overhead.
  * Ensure that EDR and/or anti-virus solutions are running on self-hosted runners.
  * Treat the ability to run an action on a runner as equivalent to running actions for any repository which utilizes that runner. If repositories in your organization have more restricted access, make sure they do not share runners with repositories with fewer restrictions.

### **Teams**

  * Enable actions only for selected repositories, as demonstrated in Figure 7.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20531'%3E%3C/svg%3E)

_Figure 7: Opting for selected repositories to use GitHub Actions rather than all repositories._

  * Configure self-hosted runners at the repository level and not the organization for any repositories containing more sensitive source code.

### **Enterprise**

  * Enable SAML SSO for the organization. This will require that all personal access tokens are individually authorized to the organization.
  * Consume workflow log events into a SIEM
  * Log the **org_credential_authorization.grant event** and capture the description to determine whether it is associated with a PAT SSO authorization, as in Figure 8.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%2072'%3E%3C/svg%3E)

_Figure 8: Logging the org_credential_authorization.grant event and capturing its description._

  * Log actor IP addresses in audit logs. **This will require adjusting the default setting,** as shown in Figure 9. We recommend enabling this so events associated with token compromise can be detected. A detection on `git clone` entries combined with source IP checks will detect any incidence of enumeration of repositories themselves conducted by an attacker.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20251'%3E%3C/svg%3E)

_Figure 9: The setting for IP disclosure is not enabled by default._

### **People**

  * Ensure that developers are trained to understand the security implications of their CI/CD configuration and the important role they play in ensuring the security of the organization.
  * Encourage developers to utilize fine-grained personal access tokens even if it is not possible to switch to them exclusively in the immediate term.

## **What’s Next?**

We hope that Microsoft will alter its stance on security features offered with lower-tier plans. Self-hosted runners expose organizations to considerable risk if not configured correctly. Therefore, if lower-cost plans support self-hosted runners, they also should include the full suite of security features necessary to monitor them _before_ an attacker has already obtained code execution. The next blog post in our CI/CD series will show how we executed a similar attack on self-hosted runners for GitLab, which is a competing SCM and CI/CD platform.

_At Praetorian, we understand the latest CI/CD attacks and how to best secure your organization’s CI/CD environment against sophisticated attackers._[_Let our experts_](https://www.praetorian.com/contact/) _guide you through the process of building detections against malicious CI/CD activity or test the robustness of your existing defense._

## About the Authors

![Adnan Khan](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Adnan Khan](https://www.praetorian.com/author/adnan-khan/)

Adnan focuses on Red-Teaming, DevOps Security, and Exploit Development.

[ ](https://www.linkedin.com/in/adnanekhan)

![Mason Davis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Mason Davis](https://www.praetorian.com/author/mason-davis/)

Mason is a Red Team operator at Praetorian, focused on objective-based Red Team operations, CI/CD and supply chain exploitation, and advancing internal and open-source offensive tooling.

[ ](https://www.linkedin.com/in/mason-davis/)

![Matt Jackoski](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Matt Jackoski](https://www.praetorian.com/author/matt-jackoski/)

Matt is a Red Team operator at Praetorian and currently is focused on performing adversarial emulation engagements for clients. Matt has a background in computer science and engineering with a focus in offensive security.

[ ](https://www.linkedin.com/in/matthew-jackoski/)

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
