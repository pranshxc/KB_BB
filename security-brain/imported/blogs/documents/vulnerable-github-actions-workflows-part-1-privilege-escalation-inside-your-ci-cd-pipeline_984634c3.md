---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-04_vulnerable-github-actions-workflows-part-1-privilege-escalation-inside-your-cicd.md
original_filename: 2022-04-04_vulnerable-github-actions-workflows-part-1-privilege-escalation-inside-your-cicd.md
title: 'Vulnerable GitHub Actions Workflows Part 1: Privilege Escalation Inside Your
  CI/CD Pipeline'
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 984634c304b8ba93a90b7dd1af4e4ab4b35c4a3342b39db439c5b13476c3c58d
text_sha256: fcfa2076688085d8cfc9a6bd89d3694fd3202f21fec31034b6ad507ec59c1fda
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerable GitHub Actions Workflows Part 1: Privilege Escalation Inside Your CI/CD Pipeline

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-04_vulnerable-github-actions-workflows-part-1-privilege-escalation-inside-your-cicd.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `984634c304b8ba93a90b7dd1af4e4ab4b35c4a3342b39db439c5b13476c3c58d`
- Text SHA256: `fcfa2076688085d8cfc9a6bd89d3694fd3202f21fec31034b6ad507ec59c1fda`


## Content

---
title: "Vulnerable GitHub Actions Workflows Part 1: Privilege Escalation Inside Your CI/CD Pipeline"
page_title: "Vulnerable GitHub Actions Workflows: Privilege Escalation"
url: "https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability"
final_url: "https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability"
authors: ["Noam Dotan"]
programs: ["GitHub"]
bugs: ["Privilege escalation", "CI/CD"]
publication_date: "2022-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2754
---

**SHARE:** [](https://twitter.com/intent/tweet?text=https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability)

At Legit Security, we’re focused on preventing software supply chain attacks and securing the SDLC for our customers and the broader cybersecurity community. We recently discovered GitHub-Actions pipeline privilege escalation vulnerabilities that can open the door to software supply chain attacks and we’re publishing this technical disclosure blog to assist organizations in remediating it.

This is important to us because, a) each insecure open source project might be the weak link in our customer's supply chain and could lead to massive security issues; and b) we want to make the software development ecosystem secure for everyone to use.

In this blog post, we will share some important findings from our GitHub Actions security research and recommend how you can keep your pipelines secure. GitHub is an extremely popular source code management system. One carefully targeted exploit of this vulnerability could have massive downstream consequences, so in addition to the responsible disclosure we've already made directly to GitHub, we want to do everything we can here at Legit Security to inform the community. 

## TL;DR

  * The Legit Security research team has uncovered a vulnerability where the attacker can exploit a vulnerable build script in GitHub Actions to modify an organization’s software code or build artifacts
  * GitHub Actions is a powerful and flexible platform that enables building complex CI/CD pipelines easily with the help of the open-source community.
  * “workflow_run” event is a unique GitHub Actions pipeline trigger that executes privileged pipelines and if not used cautiously could lead to major security issues.
  * Thousands of repositories use “workflow_run” trigger. We found various common vulnerable workflow configuration code patterns that are susceptible to a privilege escalation attack, i.e., can give attackers the ability to run highly privileged code inside the CI/CD pipeline.
  * Once a “workflow_run” privilege escalation vulnerability is exploited, an attacker could use the elevated permissions to trigger a supply chain attack by modifying repository resources (e.g. tags, artifacts, releases, etc).
  * The attacker could steal repository secrets and potentially some organization secrets, allowing lateral movement inside the organization and further increasing the blast radius of his attack.

## GitHub Actions In A Nutshell

GitHub Actions is a CI/CD platform built within GitHub, both in its cloud service and on-prem Enterprise Server; it allows a project to run custom functionality in response to events on GitHub. For example, every time new code is merged, a workflow can be triggered to build the code, test it, and deploy a new version.

Essential points about GitHub Actions: 

  * Workflows code is stored **inside the repository** , i.e., developers can change them.
  * Workflows can access sensitive secrets (e.g., credentials for database access).
  * Workflows triggered from forked repositories don’t have access to sensitive secrets.

## GitHub Actions Insecure Practices

GitHub introduced the notion of pwn request in a [blog post](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/) from December 2020; a pwn request is a pull request that exploits vulnerabilities in the project workflows in order to access the project secrets or modify its content. Why is this interesting? The format in which open source projects are developed is the following:

  * Contributors fork the desired open source project.
  * They make the necessary changes and open pull requests back to the base repository.
  * A project maintainer goes through the changes and approves/declines the changes.

![Frame 1 \(1\)](https://www.legitsecurity.com/hs-fs/hubfs/Frame%201%20\(1\).png?width=1575&name=Frame%201%20\(1\).png)  

Now, since the workflow files are stored within the repository source code, the contributor can add a workflow file inside the forked copy of the repository, which will run automatically upon “pull-requesting” to the base repository, and it will run in the context of the base repository. Consequently, secrets will be pulled from the base repository secret store, CPU time used will be charged from the base repository organization, artifacts will be uploaded to the base repository artifact server, etc. This has serious security implications since the contributor could be any user, potentially with malicious intentions; they should not have access to these resources.

GitHub introduced two security measures to defend against this kind of malicious contribution and we will show how they can be bypassed.

## 1\. Required approval for first-time contributors

To deal with bad actors abusing GitHub Actions (mainly to mine crypto currencies), GitHub requires project maintainer to approve workflow runs for first-time contributors, from [GitHub blog](https://github.blog/2021-04-22-github-actions-update-helping-maintainers-combat-bad-actors/):

“pull requests from first-time contributors will require manual approval from a repository collaborator with write access before any Actions workflows run. When a first-time contributor opens a pull request, they’ll see a message that a maintainer must approve their Actions workflow before it runs.”

This is indeed a good security measure and makes pwn request attacks more complicated. Yet, a determined adversary could gain the project maintainers trust, for example by contributing some innocent pull request (e.g., fixing a typo) and then initiating the attack.

## 2\. Restricted permission 

Since external contributors are not part of the project core team, they shouldn't have access to the project sensitive secrets (e.g., DB tokens, deployment keys, etc.); hence GitHub restricts workflows from forked repositories to a read-only token which only allows users to checkout the repository code (to test, lint and more) with no access to secrets. Yet, modern workflows are usually more complex than just running tests and require some more extensive permissions to function, for example:

  * Labeling pull requests
  * Uploading test results
  * Notifications
  * And more

GitHub introduced two special event types to support such workflows: pull_request_target and workflow_run.

“pull_request_target” security risks are well documented, and a noticeable warning message is shown in GitHub official documentation: [Events that trigger workflow - GitHub Docs](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target). 

On the contrary, “workflow_run”, which shares the same security risks, didn’t receive the same attention, but it should. Let’s see why.

Introducing workflow_run: 

According to GitHub documentation:

“This event occurs when a workflow run is requested or completed. It allows you to execute a workflow based on execution or completion of another workflow. The workflow started by the workflow_run event is able to access secrets and write tokens, even if the previous workflow was not. This is useful in cases where the previous workflow is intentionally not privileged, but you need to take a privileged action in a later workflow.”

In short, workflow_run event is a callback that runs after another workflow is finished/requested in a privileged context. For example, if you want to label a pull request based on test results, you could create workflow_run workflow, which listens for failing workflows and then labels them.

![GitHub Action workflow to label failed pull requests.](https://www.legitsecurity.com/hubfs/image-png-Mar-18-2022-06-29-51-20-PM.png)

The interesting part about this event is that it could be viewed as a client-server model where the workflow_run triggered workflow is the server and the forked pull request is the client, thus as in any client-server architecture, if the server doesn’t handle client input cautiously, it may be subject to various security issues, such as file overrides, running attacker-controlled files, code injection, script injection, and more - all of which eventually allow a privilege escalation attack on the CI/CD pipeline.

Thousands of repositories are potentially susceptible to this kind of attack, some of which are very popular with tens of thousands of stars. We had the capacity to analyze some repositories that use 'workflow_run' as trigger and discovered many popular repositories (with more than 1,000 stars, among which 5 with more than 10K stars) are indeed vulnerable to this kind of attack. We estimate many more repositories using an unsafe 'workflow_run' can be exploited in various ways.

Below are some examples of vulnerable workflow patterns that we have found.

### 2A. Running Attacker Code 

The following workflow is building an updated version of the package docs whenever a package is published:

![GitHub Action to deploy docs after successful package publish.](https://www.legitsecurity.com/hubfs/image-png-Mar-18-2022-06-31-16-47-PM.png)

  * line 16: “workflow_run.head_sha” is the triggering commit.

The workflow checks out untrusted code within the privileged context; from this point on, the workflow should be considered insecure; there are many ways code execution may happen, in this example, “npm install” and “npm run” are controlled by the triggering workflow.

For instance, an attacker can modify the package.json file to contain the following lines:

![Example script with 'build-docs' command executing controlled code.](https://www.legitsecurity.com/hubfs/image-png-Mar-18-2022-06-31-51-00-PM.png)

Thereby tricking the workflow to run the malicious code when reaching line 27: “npm run build-docs”.

There are many more examples for similar attacks, from running a bash script to docker build.

You should never check out user code in workflow_run context. 

### 2B. Insecure Usage of Artifacts

Instead of checking out the code, the advised method of communication between workflow and workflow_run is via artifacts – the unprivileged workflow runs its jobs and uploads the results as artifacts which the privileged job downloads and continue processing.

Although this is the preferred way, these artifacts should be considered untrusted and treated with caution.

![GitHub Actions workflow example with conditional artifact download and deployment steps.](https://www.legitsecurity.com/hubfs/image-png-Mar-18-2022-06-32-41-14-PM.png)

  * line 16: download the artifact that was uploaded by the unprivileged workflow.
  * line 26: store the artifact data inside an output variable.

In the above example, the untrusted input is interpolated inside the bash script in line 31, leading to script injection. 

For instance, the below code snippet will inject attacker-controlled script into the bash command in line 31:

![GitHub Actions workflow with potential code execution risk.](https://www.legitsecurity.com/hubfs/image-png-Mar-18-2022-06-33-09-57-PM.png)

Thus, the final command after interpolation will be: “echo; echo attacker controlled code; #”.

You should always use environment variables to insert input variables inside scripts instead of using string interpolation.

## Impact

The impact of taking over privileged pipeline is two-fold:

First, the attacker could modify the repository build artifacts, releases and tags and in some cases modify the main branch code, thereby initiating a supply chain attack.

Second, using the repository’s sensitive secrets, the attacker could expand the attack to additional SDLC assets.

GitHub Actions can be quite risky because of their nature (distributed, Git-Ops based – meaning your code is also CI script), and any user can submit a malicious change request that would exploit these vulnerabilities.

## Responsible disclosure

We have submitted our finding to GitHub, along with some suggested mitigations, and they closed our disclosure as “informational”, claiming they have published the aforementioned blogpost in the past. However, given the quantity of vulnerable repos, we believe it would be more secure to alert users in GitHub’s documentation about the dangers of workflow_run and suggest mitigating controls, such as the labeling mechanism they added in other vulnerable workflows.

We have also reached out to some of the most popular repos and alerted their maintainers that their CI/CD is at risk, how it can be exploited and suggested fixes. For example, a repository in Nginx Inc.'s organization was found to be vulnerable, and after our disclosure they fixed the issue.

## What you can do to protect yourselves

  * We’ve contributed ‘workflow_run’ issues detections to the [OSSF Scorecards Project](https://github.com/ossf/scorecard/pull/1818). Using scorecard in your projects is recommended and now will detect unsafe usage of ‘workflow_run’.
  * Restrict the GitHub token permissions only to the required ones; this way, even if the attackers will succeed in compromising your workflow, they won’t be able to do much.
  * Use workflow input as environment variables instead of interpolation. This will prevent script injection.
  * Never check out user code, code execution might happen in many ways, some of which are very hard to detect thus avoiding checkout is highly recommended.
  * If possible, check that the triggering workflow doesn’t belong to a forked repository, and if it does require human approval as explained in this blog post: [Using Environment Protection Rules to Secure Secrets When Building External Forks with pull_request_target](https://dev.to/petrsvihlik/using-environment-protection-rules-to-secure-secrets-when-building-external-forks-with-pullrequesttarget-hci)

## How can Legit Security help

The Legit Security platform connects to your GitHub organization and detects vulnerable workflows in real-time, and much more. If you are concerned about these vulnerabilities and others across your software supply chain, consider our free [Rapid Risk Assessment](https://info.legitsecurity.com/rapid-risk-assessment?hsLang=en). The assessment takes less than 2 hours to complete and provides immediate insight into vulnerabilities across your software supply chain, including the ones listed in this post. 

Or to learn more about other attack patterns documented by popular frameworks check out [The 3 Riskiest Software Supply Chain Attack Patterns Across Frameworks](https://info.legitsecurity.com/top-3-riskiest-software-supply-chain-attack-patterns).

Stay safe!

Need guidance on AppSec for AI-generated code?

Download our new whitepaper.

![Legit-AI-WP-SOCIAL-v3-1](https://www.legitsecurity.com/hubfs/Legit-AI-WP-SOCIAL-v3-1.png)

###
