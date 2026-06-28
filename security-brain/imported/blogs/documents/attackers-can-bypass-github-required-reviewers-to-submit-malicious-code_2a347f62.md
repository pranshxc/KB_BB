---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-08_attackers-can-bypass-github-required-reviewers-to-submit-malicious-code.md
original_filename: 2022-09-08_attackers-can-bypass-github-required-reviewers-to-submit-malicious-code.md
title: Attackers Can Bypass GitHub Required Reviewers to Submit Malicious Code
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- api-security
- supply-chain
language: en
raw_sha256: 2a347f62e2cab8201b4433f23c80c7e55bc7f8dd79d0bdf5ec4462be9ce1e993
text_sha256: 22e788054f152a3c129166fb6e1b4eafb000709e5e9766ebf9469ee2e1093830
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Attackers Can Bypass GitHub Required Reviewers to Submit Malicious Code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-08_attackers-can-bypass-github-required-reviewers-to-submit-malicious-code.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `2a347f62e2cab8201b4433f23c80c7e55bc7f8dd79d0bdf5ec4462be9ce1e993`
- Text SHA256: `22e788054f152a3c129166fb6e1b4eafb000709e5e9766ebf9469ee2e1093830`


## Content

---
title: "Attackers Can Bypass GitHub Required Reviewers to Submit Malicious Code"
url: "https://www.legitsecurity.com/blog/bypassing-github-required-reviewers-to-submit-malicious-code"
final_url: "https://www.legitsecurity.com/blog/bypassing-github-required-reviewers-to-submit-malicious-code"
authors: ["Noam Dotan"]
programs: ["GitHub"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2022-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2184
---

**SHARE:** [](https://twitter.com/intent/tweet?text=https://www.legitsecurity.com/blog/bypassing-github-required-reviewers-to-submit-malicious-code) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.legitsecurity.com/blog/bypassing-github-required-reviewers-to-submit-malicious-code)

_Update: a few weeks after this publication, GitHub decided to fix the issue and employed the mitigation we recommended to them in our initial report. The mitigations section of this post was updated accordingly; read it to make sure your repositories are well-configured and safe from this kind of attack._

Code reviews are an essential security guardrail, but GitHub’s required code reviewers' settings might be giving you a false sense of security – they can easily be bypassed by any collaborator with reviewer permissions.

See how an attacker can use a compromised account to submit malicious code and merge it into your repository’s main branch while bypassing code review restrictions in this post.

## TL;DR

  * GitHub’s required reviewers capability can be bypassed if currently using this setting to require at least one code review before merging code.

  * Any code reviewer reviewing code can simply submit malicious code on pull requests during the review process and merge that code to the main branch without review.

  * GitHub does not currently provide users the ability to eliminate this risk directly.

Even if you followed every agile development best practice perfectly, there are still risks in agile software development. Agile has proven that it offers more benefits than drawbacks, so it’s important to [understand the potential security risks](https://www.legitsecurity.com/blog/re-thinking-application-security-for-devsecops-and-scale) so that you can mitigate them ahead of time.

## What are Required Reviewers?

A typical development workflow looks like the following:

  1. The developer diverges from the repository’s main development branch

  2. Then the developer adds/deletes/modifies the code as needed.

  3. Finally, a second person must review and approve the changes before that code can be merged back to the main branch.

![securing code review in the software development lifecycle](https://www.legitsecurity.com/hs-fs/hubfs/dev%20process%20with%20review.jpeg?width=1694&name=dev%20process%20with%20review.jpeg)

To support this common workflow, GitHub introduced the concept of **Protected Branches.** A protected branch is a branch that contains restrictions on who can modify it and how.

For example, the below configuration enforces any developer who wants to push code to the main branch to create a pull request and _also_ get approval from a second, _authorized_ person to approve pull requests.

![securing default main branch](https://www.legitsecurity.com/hs-fs/hubfs/securing%20default%20main%20branch.png?width=1724&name=securing%20default%20main%20branch.png)

![branch protection settings to secure the main branch](https://www.legitsecurity.com/hs-fs/hubfs/branch%20protection%20settings%20to%20secure%20the%20main%20branch.png?width=1690&name=branch%20protection%20settings%20to%20secure%20the%20main%20branch.png)

(A complete list of Branch Protection rules can be found in [GitHub’s documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches").)

For obvious reasons, GitHub doesn’t allow developers to authorize their own pull requests – otherwise, there’d be no point in requiring a “required approval.”

However, I’ve discovered that there is an easy method a developer can use to authorize their own pull requests: _pull request hijacking._

## What is Pull Request Hijacking?

Any user authorized to approve pull requests can modify existing pull requests of other users as desired. After modifying the existing pull requests, they can approve and merge the code _without requiring approval_**.** This works because the original pull request was opened by another user (i.e., “User A”), and GitHub doesn't recognize that a different user (i.e., “User B”) modified it.

You can test this yourself:

  1. Find an open pull request.

  2. Modify it or even replace the entire branch content

  3. Approve your own modifications

  4. Bypass required approvals for your modified code

## **Responsible Disclosure: GitHub Response**

When disclosing pull request hijacking to GitHub, they responded that GitHub is working as intended in this scenario.

> “This is an intentional design decision and is working as expected. We may make this functionality more strict in the future, but don't have anything to announce right now. As a result, this is not eligible for reward under the Bug Bounty program.” _-GitHub_

We believe that GitHub didn’t fix this issue because the resulting experience might be too restrictive for modern development teams. There are many frequent and harmless cases in which developers collaborate on the same branch. For example, if I fixed a small typo when reviewing another developer's code, it makes some sense that I should also be allowed to go ahead and push that code.

## **How to Protect Yourself From Pull Request Hijacking**

The following defensive techniques will protect your business from malicious code submissions during a pull request hijack attempt. In addition to these two techniques, you can also lower the risk of malicious code in various ways, like strengthening authentication requirements for developers that are also reviewers and practicing the least privileges in relation to your GitHub organization.  
  

### New: Require Approval For The Most Recent Pusher

This mitigation measure was implemented after the initial publication of the blog. When activated, it ensures that all changes made to the code are reviewed by another person before being merged. This ensures that any updates to the code are approved, even if the original pull request was modified by someone else.

![Require approval from a different user for recent push](https://www.legitsecurity.com/hubfs/Screen%20Shot%202022-12-06%20at%209-58-52-png.png)

### Require At Least Two Reviewers

Configure GitHub to require more than one reviewer. This way, even if an existing pull request is modified and approved by the same user, it would still need a review from an additional person. You can configure this with your GitHub settings, as pictured below.

![improve github code review security by requiring 2 reviewers](https://www.legitsecurity.com/hs-fs/hubfs/improve%20github%20code%20review%20security%20by%20requiring%202%20reviewers.png?width=832&name=improve%20github%20code%20review%20security%20by%20requiring%202%20reviewers.png)

### Restrict Who Can Push To Matching Branches

GitHub allows you to create a “personal branch” pattern for each developer that no other developer could modify (pictured below).

![example branch name pattern aligning to developer specific branch](https://www.legitsecurity.com/hs-fs/hubfs/example%20branch%20name%20pattern%20aligning%20to%20developer%20specific%20branch.png?width=853&name=example%20branch%20name%20pattern%20aligning%20to%20developer%20specific%20branch.png)

![secure settings for branch naming protection strategy](https://www.legitsecurity.com/hs-fs/hubfs/secure%20settings%20for%20branch%20naming%20protection%20strategy.png?width=836&name=secure%20settings%20for%20branch%20naming%20protection%20strategy.png)

In this example, if my branch name pattern is " _noam/*."_ I can configure that only Noam can push to this branch. Due to this, a different developer reviewing Noam’s code cannot hijack Noam’s branch to submit malicious code.

## Legit Security Can Help

A pre-requisite to hardening your GitHub required reviewer configurations is to have visibility into your development pipelines, know where you are using GitHub, whether or not you are requiring code reviews, and whether you have stale or inactive accounts with reviewer permissions. Legit Security can provide visibility and answers to these questions [in minutes](https://info.legitsecurity.com/rapid-risk-assessment "https://info.legitsecurity.com/rapid-risk-assessment"). In addition, Legit helps you holistically assess security and compliance risks in your development pipelines across other SCMs and also other developer systems like build servers and artifact registries. Learn more about Legit by visiting our [platform page](/platform/aspm "https://www.legitsecurity.com/software-supply-chain-security-platform") or [booking a demo](https://info.legitsecurity.com/demo "https://info.legitsecurity.com/demo") with us today.

Need guidance on AppSec for AI-generated code?

Download our new whitepaper.

![Legit-AI-WP-SOCIAL-v3-1](https://www.legitsecurity.com/hubfs/Legit-AI-WP-SOCIAL-v3-1.png)

###
