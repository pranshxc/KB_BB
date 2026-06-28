---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-02_vulnerable-github-actions-workflows-part-2-actions-that-open-the-door-to-cicd-pi.md
original_filename: 2022-05-02_vulnerable-github-actions-workflows-part-2-actions-that-open-the-door-to-cicd-pi.md
title: 'Vulnerable GitHub Actions Workflows Part 2: Actions That Open the Door to
  CI/CD Pipeline Attacks'
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: bf51aef7f9f9e0fa9ba0a9f8a73c4989648258416b616ab3c8fec2ee01aed772
text_sha256: 6fd2fe77daebb996d57325192f6e4439f0f0c97de16a4d0d1f52f283a34f3afe
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerable GitHub Actions Workflows Part 2: Actions That Open the Door to CI/CD Pipeline Attacks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-02_vulnerable-github-actions-workflows-part-2-actions-that-open-the-door-to-cicd-pi.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `bf51aef7f9f9e0fa9ba0a9f8a73c4989648258416b616ab3c8fec2ee01aed772`
- Text SHA256: `6fd2fe77daebb996d57325192f6e4439f0f0c97de16a4d0d1f52f283a34f3afe`


## Content

---
title: "Vulnerable GitHub Actions Workflows Part 2: Actions That Open the Door to CI/CD Pipeline Attacks"
page_title: "Vulnerable GitHub Actions Workflows: CI/CD Pipeline Attacks"
url: "https://www.legitsecurity.com/blog/github-actions-that-open-the-door-to-cicd-pipeline-attacks"
final_url: "https://www.legitsecurity.com/blog/github-actions-that-open-the-door-to-cicd-pipeline-attacks"
authors: ["Noam Dotan"]
bugs: ["Privilege escalation", "CI/CD"]
publication_date: "2022-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2672
---

**SHARE:** [](https://twitter.com/intent/tweet?text=https://www.legitsecurity.com/blog/github-actions-that-open-the-door-to-cicd-pipeline-attacks) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.legitsecurity.com/blog/github-actions-that-open-the-door-to-cicd-pipeline-attacks)

In this blog post, we’ll explore a bug we’ve found in a popular third-party action and how in some cases it could lead to your SDLC pipeline being compromised. This post is the 2nd one in the series of _Vulnerable GitHub Actions Workflows_ , following [Part 1: Privilege Escalation Inside Your CI/CD Pipeline](/blog/github-privilege-escalation-vulnerability).

We’ll demonstrate how a minor bug in a custom GitHub action could potentially lead to privilege escalation inside your CI/CD pipeline.

If you’re familiar with GitHub Actions feel free to jump straight to the technical part.

![GitHub CICD Pipeline Blog](https://www.legitsecurity.com/hs-fs/hubfs/GitHub%20CICD%20Pipeline%20Blog.jpg?width=571&name=GitHub%20CICD%20Pipeline%20Blog.jpg)

Nowadays, it is widely known that the security of your business depends not just on your code but on the entire software supply chain, which includes third-party components. Studies have shown that open-source software makes up 85-95% of the code base for 99% of applications. The Application Security industry is investing a lot of effort into SCA tools and the recently emerging [SBOM](https://www.legitsecurity.com/blog/what-is-an-sbom-sbom-explained-in-5-minutes "https://www.legitsecurity.com/blog/what-is-an-sbom-sbom-explained-in-5-minutes") generating tools to map 3rd party packages and libraries used by your software, their license, and the vulnerabilities they contain.

![Vulnerable GitHub Actions Workflows Part 2 | All Modern Digital Infrastructure](https://www.legitsecurity.com/hs-fs/hubfs/Screen%20Shot%202022-02-08%20at%2012.23.45.png?width=463&name=Screen%20Shot%202022-02-08%20at%2012.23.45.png)

But these components are not the only ones you should be worried about. Your CI/CD pipeline also contains 3rd party components that you are using, and your software supply chain security is affected by them just as much.

GitHub Actions provides a powerful and flexible CI/CD service thanks to the support of the broad open-source community that develops and maintains a long list of “actions” - helpful build steps developed by GitHub itself or other open-source maintainers.

## What are GitHub custom actions?

The GitHub Actions engine provides the ability to run jobs and steps, define triggers, and control the execution flow. Custom actions provide an extension to this engine by building functions that group multiple steps into one easy-to-use utility (similar to plugins in other CI/CD systems).

From GitHub’s [documentation](https://docs.github.com/en/actions/creating-actions/about-custom-actions "https://docs.github.com/en/actions/creating-actions/about-custom-actions"): “Actions are individual tasks that you can combine to create jobs and customize your workflow. You can create your own actions, or use and customize actions shared by the GitHub community.”

In a way, the option to write custom actions is what makes GitHub Actions such a powerful CI/CD system; it’s super easy to extend, has the power of the community, and integrates smoothly with the development process.

**But, and there is always a but, using third-party components exposes your CI/CD pipeline to threats.**

The super helpful and cool action you’re using might have been developed by a malicious actor, or it might have honest BUGS! The resulting impact differs between the cases:

  * Malicious action could steal your private repository source code, modify its content and artifacts, etc.

  * Buggy action exposes your workflow to vulnerabilities that might be later exploited by an adversary.

**If you use third-party actions it’s highly recommended you take the following actions:**

  * Limit GitHub token to the minimum required permissions

  * Pin the action to a specific commit

  * Allow only specific actions to be used in your organization

  * Read the action source code before using it

## Example of a buggy action That Can Lead to Attacks

Introducing ['dawidd6/action-download-artifact'](https://github.com/dawidd6/action-download-artifact)

This is a very useful custom action because it provides an API similar to GitHub’s official - ['actions/download-artifact'](https://github.com/actions/download-artifact). But extend it with extensive filtering capabilities and it allows for downloading artifacts from different workflows and even different repositories.

The action receives the following as input parameters:

  * `name` \- to download specific artifact or none for all artifacts

  * `path` \- where to extract the artifacts (artifacts are downloaded as zip files)

  * and many others, as can seen in the [README](https://github.com/dawidd6/action-download-artifact#readme "https://github.com/dawidd6/action-download-artifact#readme")

## Why is ‘action-download-artifact’ needed at all?

The standard GitHub’s owned custom action ‘actions/download-artifact’ can download artifacts only if they were created in the same workflow (i.e. same ‘run id’) they’re running in. It’s perfectly fine in normal inter-jobs communication (for example, a ‘build’ job builds the project and uploads the result as an artifact, then a ‘test’ job downloads the artifact created by the ‘build’ job and tests it, instead of rebuilding the project).

But what happens when the artifact is uploaded in one workflow and needs to be downloaded in a different one (i.e. different ‘run id’)? That’s where action-download-artifact comes into play, enabling us to download artifacts which were uploaded in different workflows.

‘action-download-artifact’ fills this gap by providing a way to download artifacts from different workflow run IDs.

Very useful! However, a problem arises with the case where `path` is not provided. The action’s documentation had an error, stating that the `path` defaults to the artifact name, while in fact, it defaults to `"./"`, meaning if it’s not provided, the artifact will be extracted to the current working directory.

Another important fact: when an artifact is extracted, files with the same name as the ones inside the archive will be overridden by the artifact files.

## The problem and Vulnerability

When using ‘action-download-artifact’ without providing the ‘path’ parameter, the artifact is extracted into the current directory, overriding files with identical names. So, if the current directory contains a file that is planned to be executed, an attacker could replace it with a malicious one and hijack the workflow execution.

![Vulnerable GitHub Actions Workflows Part 2 | Workflow Run](https://www.legitsecurity.com/hubfs/Screen%20Shot%202022-04-28%20at%2017-24-29-png.png)

The above workflow:

  1. Checks out the repository's main branch

  2. Downloads an artifact from a previous workflow

  3. Executes a script from the main branch

Theoretically, this is a perfectly legitimate and secure workflow. The workflow’s author couldn’t know they wrote vulnerable code without inspecting the action source code and understanding the security risk of unzipping malicious archive file. But since ‘action-download-artifact’ is vulnerable to file override, it could be easily exploited with the following workflow:

![Vulnerable GitHub Actions Workflows Part 2 | Workflow Run 2](https://www.legitsecurity.com/hubfs/Screen%20Shot%202022-04-28%20at%2017-23-40-png.png)

"some workflow" triggers the “workflow_run” from above. Note that the vast majority of workflows that use dawidd6/action-download-artifact are triggered on `workflow_run`, and attacking it will result in privilege escalation in the pipeline, as we [previously published](/blog/github-privilege-escalation-vulnerability). Any GitHub user can fork the vulnerable repository, create a pull request that modifies “some workflow” as above, and due to the nature of workflow_run - it will be triggered automatically (even when code review is required), and the poisoned `some_script.py` will be executed in a privileged context, allowing the attacker to steal secrets, modify artifacts, etc.

Note: Github’s original ‘download-artifact’ action, which is the basis for dawidd6’s action, is also extracting in the current directory as a default behavior, but it poses no risk since the official action can only be run in the same given workflow job where the upload occurred.

## **How to Better Protect Your Software Supply Chain**

Whenever you use '`dawidd6/action-download-artifact`' make sure you provide the following parameters:

  * ‘path’ - so the archive won’t be extracted in the current directory

  * ‘commit’ / ‘run_id’ - to make sure you download the artifact from a known source

## Summary and Responsible Disclosure

We notified dawidd6 about our findings, he [fixed the documentation error](https://github.com/dawidd6/action-download-artifact/commit/431e8a11312b5b66f86c76b40cd2f64cfeab54a0 "https://github.com/dawidd6/action-download-artifact/commit/431e8a11312b5b66f86c76b40cd2f64cfeab54a0") noted above but decided not to fix the fact that the default path is the current working directory since that fix is a breaking change.

Additionally, we notified a few vulnerable popular open-source projects regarding this issue, and they immediately fixed it.

Want to make sure your repos are working according to best practices? Legit Security can monitor your pipelines, raise issues when you’re at risk and help with remediation. [Contact us](/) or [book a demo](https://info.legitsecurity.com/demo) if you are interested in learning more.

To learn more best practices in software supply chain security, check out our guide: [Best Practices to Secure Your Software Supply Chains.](https://info.legitsecurity.com/best-practices-software-supply-chain-security)

Need guidance on AppSec for AI-generated code?

Download our new whitepaper.

![Legit-AI-WP-SOCIAL-v3-1](https://www.legitsecurity.com/hubfs/Legit-AI-WP-SOCIAL-v3-1.png)

###
