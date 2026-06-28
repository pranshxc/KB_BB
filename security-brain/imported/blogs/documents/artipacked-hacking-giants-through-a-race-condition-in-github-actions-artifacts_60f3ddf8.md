---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-13_artipacked-hacking-giants-through-a-race-condition-in-github-actions-artifacts.md
original_filename: 2024-08-13_artipacked-hacking-giants-through-a-race-condition-in-github-actions-artifacts.md
title: 'ArtiPACKED: Hacking Giants Through a Race Condition in GitHub Actions Artifacts'
category: documents
detected_topics:
- supply-chain
- cloud-security
- jwt
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- cloud-security
- jwt
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 60f3ddf88cc0557ff842e4f10973222adc063ca2ff829307556b5b92bb0cc56a
text_sha256: 04b8777597a006f90a95a8664325ae4ae7e538ac65814363ff3109cf673be800
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# ArtiPACKED: Hacking Giants Through a Race Condition in GitHub Actions Artifacts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-13_artipacked-hacking-giants-through-a-race-condition-in-github-actions-artifacts.md
- Source Type: markdown
- Detected Topics: supply-chain, cloud-security, jwt, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `60f3ddf88cc0557ff842e4f10973222adc063ca2ff829307556b5b92bb0cc56a`
- Text SHA256: `04b8777597a006f90a95a8664325ae4ae7e538ac65814363ff3109cf673be800`


## Content

---
title: "ArtiPACKED: Hacking Giants Through a Race Condition in GitHub Actions Artifacts"
url: "https://unit42.paloaltonetworks.com/github-repo-artifacts-leak-tokens/"
final_url: "https://unit42.paloaltonetworks.com/github-repo-artifacts-leak-tokens/"
authors: ["Yaron Avital (@yaronavital)"]
programs: ["GitHub", "Google (Firebase)", "Microsoft", "AWS", "Red Hat", "Canonical (Ubuntu Adsys)", "OWASP"]
bugs: ["Race condition", "CI/CD"]
publication_date: "2024-08-13"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 75
---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# ArtiPACKED: Hacking Giants Through a Race Condition in GitHub Actions Artifacts

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 11 min read 

Related Products

[![Code to Cloud Platform icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Code to Cloud Platform](https://unit42.paloaltonetworks.com/product-category/code-to-cloud-platform/ "Code to Cloud Platform")[![Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
  * [Yaron Avital](https://unit42.paloaltonetworks.com/author/yaron-avital/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:August 13, 2024

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
  * [Artifacts](https://unit42.paloaltonetworks.com/tag/artifacts/)
  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/)
  * [GitHub](https://unit42.paloaltonetworks.com/tag/github/)
  * [Open source](https://unit42.paloaltonetworks.com/tag/open-source/)
  * [Red Hat](https://unit42.paloaltonetworks.com/tag/red-hat/)
  * [Ubuntu](https://unit42.paloaltonetworks.com/tag/ubuntu/)

  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/github-repo-artifacts-leak-tokens/?pdf=download&lg=en&_wpnonce=007ee71b73 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/github-repo-artifacts-leak-tokens/?pdf=print&lg=en&_wpnonce=007ee71b73 "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=ArtiPACKED:%20Hacking%20Giants%20Through%20a%20Race%20Condition%20in%20GitHub%20Actions%20Artifacts&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgithub-repo-artifacts-leak-tokens%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgithub-repo-artifacts-leak-tokens%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgithub-repo-artifacts-leak-tokens%2F&title=ArtiPACKED:%20Hacking%20Giants%20Through%20a%20Race%20Condition%20in%20GitHub%20Actions%20Artifacts "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgithub-repo-artifacts-leak-tokens%2F&text=ArtiPACKED:%20Hacking%20Giants%20Through%20a%20Race%20Condition%20in%20GitHub%20Actions%20Artifacts "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgithub-repo-artifacts-leak-tokens%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=ArtiPACKED:%20Hacking%20Giants%20Through%20a%20Race%20Condition%20in%20GitHub%20Actions%20Artifacts%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgithub-repo-artifacts-leak-tokens%2F "Share in Mastodon")

## Executive Summary

This research reviews an attack vector allowing the compromise of GitHub repositories, which not only has severe consequences in itself but could also potentially lead to high-level access to cloud environments. This is made possible through the abuse of GitHub Actions artifacts generated as part of organizations’ CI/CD workflows. A combination of misconfigurations and security flaws can make artifacts leak tokens, both of third party cloud services and GitHub tokens, making them available for anyone with read access to the repository to consume. This allows malicious actors with access to these artifacts the potential of compromising the services to which these secrets grant access. In most of the vulnerable projects we discovered during this research, the most common leakage is of GitHub tokens, allowing an attacker to act against the triggering GitHub repository. This potentially leads to the push of malicious code that can flow to production through the CI/CD pipeline, or to access secrets stored in the GitHub repository and organization.

While the research applies to both private and public GitHub repositories, this article focuses on the discovery of vulnerable public repositories. We uncover high-profile open-source projects owned by the biggest companies in the world, which before mitigation could have led to a potential impact on millions of their consumers. All of the disclosed cases were reported to the maintainers of these projects. We received great support from all teams, and were able to collaborate to mitigate all of the discoveries quickly and efficiently.

CI/CD environments, processes and systems are an essential part of modern software organizations. They’re responsible for the crucial flow of building, testing and delivering code to production. Naturally, CI/CD pipelines use highly sensitive credentials to authenticate against various types of services, creating a significant challenge to keep a high-level of [credential hygiene](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-06-Insufficient-Credential-Hygiene). This article covers the potential impact of insecure usage of GitHub Actions artifacts, as well as the methods and tools to protect against this threat.

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

  * [Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud) customers are better protected by the [attack path policies](https://docs.prismacloud.io/en/classic/cspm-admin-guide/prisma-cloud-policies/attack-path-policies) continuously monitoring and alerting on potential attack paths.
  * [The Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) can also be engaged to help with a compromise or to provide a proactive assessment to lower your risk.

## Exploring Workflow Artifacts

Knowing how sensitive CI/CD systems are, I had to follow a hunch I had about an overlooked feature called workflow artifacts in the leading source control platform and home of many open-source projects, GitHub.

I was quite convinced I’d find [sensitive data](https://www.paloaltonetworks.com/cyberpedia/sensitive-data) or credentials, and as it turned out, the discovery was even bigger than what I had envisioned. In fact, it impacted well-known open-source projects owned by Red Hat, Google, AWS, Canonical (Ubuntu), Microsoft, OWASP and others — and potentially reached millions of their product users.

## GitHub Actions Build Artifacts

In GitHub Actions, workflow build artifacts offer a powerful mechanism for persisting and sharing data across jobs within the same workflow. These artifacts can be any files generated during your build process, such as compiled code, test reports or deployment packages.

Artifacts ensure critical data isn't lost after a workflow finishes, making the data accessible for later analysis or deployment. This is particularly useful for sharing test results or deployment packages between dependent jobs. Overall, workflow build artifacts streamline your workflows by facilitating data transfer and promoting efficient execution within the GitHub Actions environment.

## The Hunch

GitHub Actions workflows frequently use secrets to interact with various cloud services and with GitHub itself. These secrets include the ephemeral, automatically created GITHUB_TOKEN used to perform actions against the repository. The Actions build artifacts are outputs generated by the execution of workflows, and once created, they’re stored for up to 90 days. In open-source projects, these artifacts are publicly available for anyone to consume.

So why not scan these artifacts for secrets?

Figure 1. GitHub Actions artifact.

This approach offers a straightforward method for identifying potential security risks.

I then compiled a list of popular open-source projects on GitHub and automated the sequence of downloading their artifacts and scanning them for secrets.

## Found Some Tokens, Now What?

My hunch was spot on. I found working tokens for various cloud services, including music streaming, cloud infrastructure and more. I also found something far more interesting — various GitHub tokens. Using them, though, was not straightforward.

Let's understand why and take a technical dive into the different types of tokens created by GitHub when a workflow runs.

## How GitHub Tokens Find Their Way into Artifacts

Two types of GitHub tokens kept popping up: GITHUB_TOKEN, which has a prefix of ghs_, and ACTIONS_RUNTIME_TOKEN, which is a JWT (JSON Web Token).

It's important to note that these tokens _weren’t part of the repository code_ but were only found in repository-produced artifacts. Before determining what I could do with them, I wanted to know how these tokens ended up inside artifacts in the first place.

Most GitHub users use the actions/checkout GitHub action for the obvious need of cloning their repository code for availability during the workflow run. The default behavior of actions/checkout is to persist credentials, which means the GITHUB_TOKEN is written to the local git directory, enabling it to run authenticated git commands against the repository. Most users, I’m willing to bet, aren’t aware of this default behavior and don't require the functionality. In many cases, after all, a simple clone is all that’s required for the workflow to do its job.

Figure 2: GitHub token encoded in base64 publicly accessible and embedded in an artifact of project CycloneDX by OWASP.

From what I’ve seen, users commonly — and mistakenly — upload their entire checkout directory as an artifact. The directory contains the hidden .git folder that stores the persisted GITHUB_TOKEN, leading the publicly accessible artifacts to contain the GITHUB_TOKEN.

As seen in Figure 3, the [microsoft/typescript-bot-test-triggerer](https://github.com/microsoft/typescript-bot-test-triggerer/blob/0ef06130c0f7d78e1da6704bc0b447eacd79455c/.github/workflows/deploy.yml#L39) project uploaded the entire checkout directory as an artifact, along with the persisted GITHUB_TOKEN stored in the .git directory.

Figure 3. Example of a Microsoft repository workflow uploading a valid GITHUB_TOKEN in an artifact.

Another mistake that had users exposing GitHub tokens in public artifacts occurred by using [super-linter](https://github.com/super-linter/super-linter), a well-known open-source code linter with a [widely used fork maintained by GitHub](https://github.com/github/super-linter).

Once the CREATE_LOG_FILE property of super-linter is set to True, super-linter creates a log file with lots of details, including environment variables. [CI/CD pipelines](https://www.paloaltonetworks.com/cyberpedia/what-is-the-ci-cd-pipeline-and-ci-cd-security) usually contain secrets loaded as environment variables — GitHub tokens included, meaning that logging them probably isn’t a good idea.

The super-linter log file is often uploaded as a build artifact for reasons like debuggability and maintenance. But this practice exposed sensitive tokens of the repository.

I [reported this to the maintainers of super-linter](https://github.com/super-linter/super-linter/pull/5473), and environment variables are no longer printed to its log file. The GitHub version was also updated.

## Abusing Leaked GitHub Tokens

And now, moving on to abusing these tokens.

The obvious choice would be leveraging the widely used GITHUB_TOKEN against the repository. It’s an ephemeral token created in any workflow job run and designed to allow workflows to interact with GitHub resources, like the workflow’s repository. The token can be set with limited scope and to expire on job completion, both of which will limit risk in the event of a token leakage.

During my research, though, I discovered that workflow artifacts are only available for download after the entire workflow finishes. Since the GITHUB_TOKEN expires when the job ends, I won’t be able to download the artifact and extract the token. Bummer! (Spoiler: This is just the beginning).

But I’m left with repos exposing their ACTIONS_RUNTIME_TOKEN, which is a JWT (JSON Web Token) with an expiration of about six hours according to the exp (expiration) property. ACTIONS_RUNTIME_TOKEN is an undocumented environment variable, used by several popular actions owned by GitHub, such as actions/cache and actions/upload-artifact, to manage caching and artifacts. Caching helps to speed up workflows by storing and reusing downloaded files or build results. We're already familiar with the role of artifacts.

Figure 4: Decoded ACTIONS_RUNTIME_TOKEN JWT token.

By tracking a workflow run from a project that leaked a token, I could download its artifacts within the six-hour window before the token expires. Extracting the token could then be used to manage cache and artifacts.

But workflow runtimes are unpredictable unless triggered by a schedule (cron). I automated a process that downloads an artifact, extracts the ACTIONS_RUNTIME_TOKEN, and uses it to replace the artifact with a malicious one.

Subsequent workflow jobs often rely on previously uploaded artifacts. Cases of this kind open the door for remote code execution (RCE) on the runner that runs the job consuming the malicious artifact. RCE can also occur if developers download and execute a malicious artifact, leading to compromised workstations.

The video below demonstrates an attack on the [SchemeCrawler project](https://github.com/schemacrawler/SchemaCrawler/blob/11ba4a48bb410e9c20a550bd00a793c82471ce89/.github/workflows/linter.yml#L55). I identified a public artifact that contains the ACTIONS_RUNTIME_TOKEN and used it to upload my own malicious artifact to replace the existing one.

Figure 5. A recorded attack on project SchemeCrawler, where I’ve injected a “malicious” artifact.

## The GITHUB_TOKEN Plot Twist

Cool as it was, I craved more. There were a lot of cases where I had a leaked GITHUB_TOKEN, and I wanted to use it and push unreviewed code to the repository. But as I mentioned, these tokens were useless.

Then, with incredible timing, GitHub announced [version 4 of the artifacts feature](https://github.blog/2024-02-12-get-started-with-v4-of-github-actions-artifacts/). It has impressive improvements, like 10x faster uploads. But one particular detail surprised me like an immediate call for action.

_“Another common request from our users was the ability to download artifacts from the UI or API while the workflow run is in progress.”  
_

As I read this sentence, my researcher spidey-senses tingled. It suggests that a race condition was just made possible, allowing the leaked GITHUB_TOKEN to be downloaded, extracted and used before the job finished and the token expired.

An attack flow might resemble the following:

  1. The attacker waits for a pipeline to be triggered.
  2. The repository triggers a pipeline.
  3. The pipeline inadvertently uploads an artifact that includes the GITHUB_TOKEN.
  4. Before the workflow job finishes, an attacker downloads the publicly available artifact.
  5. The attacker extracts the token from the artifact and uses it to push malicious code to the repository.
  6. The pipeline job ends, and the GITHUB_TOKEN is invalidated.

Figure 6: Attack flow.

## Pushing Code Before the Clock Runs Out

First, I created a list of open-source projects using the upload-artifact@v4 action. The list quickly grew, especially since GitHub announced the [deprecation of v3](https://github.blog/changelog/2024-04-16-deprecation-notice-v3-of-the-artifact-actions/), effective November 2024. Software dependencies bots automatically create pull requests updating to v4, which accelerated this process even further. I scanned the artifacts of each of these projects for secrets and was interested in the ones exposing their GITHUB_TOKEN.

It was time for my first attempt to push code to an open-source project. To avoid harming the project, I decided that creating a branch was sufficient, as it requires write permissions, same as pushing code.

I chose a project from the list where the workflow had the contents: write permission. Spoiler alert: Most of them did, which wasn't surprising, given my previous work exploring how popular [open-source projects manage their workflows’ permissions](https://www.paloaltonetworks.com/blog/prisma-cloud/github-actions-opt-out-permissions-model/).

No luck exploiting tokens! Every time I tried to use the leaked token, it had already expired, leading to a consistent "401 Unauthorized: message: Bad Credentials" error. Usually, artifacts are uploaded as the last step of the job. The job ends right after upload is complete. Downloading and extracting the vulnerable artifact proved just slow enough for the token to expire before I could leverage it. Reviewing the workflow build logs revealed the reason it failed — a two-second delay.

I returned to my list and selected a project where the artifact upload step didn’t bring the artifact to an end but was followed by additional steps, granting me an opportunity to steal and use the token before it expired.

It worked! I was able to create a branch (write operation) in an open-source project — [clair](https://github.com/quay/clair), even though as an external contributor, I obviously don't have permission to do that. I could simply push code following the same process.

Figure 7. Creation of branch impala in the “clair” open-source project by Red Hat.

Figure 8. Screen recording of the actual attack.

## Let’s Win More Races

While I successfully exploited the issue, I wanted to broaden the attack's applicability. Previously, the attack relied on the workflow job having subsequent steps after the artifact upload, granting me a window to use the token. To improve the success rate, I applied some good old engineering to make it more robust.

Downloading the artifact to my own machine was too slow.

Needing to be closer to the target, GitHub Actions presented a perfect solution. It can be triggered remotely, run on the same cloud infrastructure as our targets, meaning lower latency and much faster downloads, plus high configurability.

I needed to further optimize performance and reduce communication time, Since artifacts are compressed, I selectively extracted only the git config file, skipping most of the archive content. Also, I sent dozens of requests per second while staying under the GitHub rate limit and disabled certificate verification.

Eventually, I came up with this design:

  1. A machine that samples the target repository and waits for a workflow_run event (like an alert) to notify me when an attack is in progress.
  2. Once a workflow was running, a malicious GitHub Actions workflow, which I named "RepoReaper," was launched.
  3. The RepoReaper workflow waits for the exact moment an artifact containing a leaked token is present.
  4. The RepoReaper workflow downloads the artifact, extracts the token and uses it to create a branch via the REST API on the target repository.
  5. Target repository compromised. It could have easily contained malicious code.

Then, I could use this design to search and target open-source projects.

## Projects I’ve Helped Secure

The research laid out here allowed me to compromise dozens of projects maintained by well-known organizations, including firebase-js-sdk by Google, a JavaScript package directly referenced by 1.6 million public projects, according to GitHub. Another high-profile project involved adsys, a tool included in the Ubuntu distribution used by corporations for integration with Active Directory.

All open-source projects I approached with this issue cooperated swiftly and patched their code. Some offered bounties and cool swag. Here’s partial list of affected projects I’m allowed to disclose:

  * [firebase/firebase-js-sdk](https://github.com/firebase/firebase-js-sdk) (Google)
  * [microsoft/TypeScript-repos-automation](https://github.com/microsoft/TypeScript-repos-automation), [microsoft/json-schemas](https://github.com/microsoft/json-schemas), [microsoft/typescript-bot-test-triggerer](https://github.com/microsoft/typescript-bot-test-triggerer), [Azure/draft](https://github.com/Azure/draft) (Microsoft)
  * [Ubuntu/adsys](https://github.com/ubuntu/adsys) (Canonical)
  * [quay/clair](https://github.com/quay/clair) (Red Hat)
  * [CycloneDX/cdxgen](https://github.com/CycloneDX/cdxgen) (OWASP)
  * [opensearch-project/security](https://github.com/opensearch-project/security) (AWS)
  * [penrose/penrose](https://github.com/penrose/penrose)
  * [Aiven-Open/guardian-for-apache-kafka](https://github.com/Aiven-Open/guardian-for-apache-kafka)
  * [Deckhouse/Deckhouse](https://github.com/Deckhouse/Deckhouse)
  * [datalad/git-annex](https://github.com/datalad/git-annex)
  * [schemacrawler/SchemaCrawler](https://github.com/schemacrawler/SchemaCrawler)
  * [zama-ai/concrete-ml](https://github.com/zama-ai/concrete-ml)
  * [official-stockfish/Stockfish](https://github.com/official-stockfish/Stockfish)
  * [libevent](https://github.com/libevent/libevent)

This research was reported to GitHub's bug bounty program. They categorized the issue as informational, placing the onus on users to secure their uploaded artifacts.

## Stopping the Leak

My aim in this article is to highlight the potential for unintentionally exposing sensitive information through artifacts in GitHub Actions workflows. To address the concern, I developed a proof of concept (PoC) custom action that safeguards against such leaks.

The action uses the [@actions/artifact](https://www.npmjs.com/package/@actions/artifact) package, which is also used by the [upload-artifact](https://github.com/actions/upload-artifact) GitHub action, adding a crucial security layer by using an open-source scanner to audit the source directory for secrets and blocking the artifact upload when risk of accidental secret exposure exists. This approach promotes a more secure workflow environment.

You can find [upload-secure-artifact on the Palo Alto Networks GitHub](https://github.com/PaloAltoNetworks/upload-secure-artifact).

Figure 9. The action upload-secure-artifact failed the workflow due to the existence of a GITHUB_TOKEN in the uploaded artifact.

## Conclusion

As this research shows, we have a gap in the current security conversation regarding artifact scanning. GitHub's deprecation of Artifacts V3 should prompt organizations using the artifacts mechanism to reevaluate the way they use it.

Security defenders must adopt a holistic approach, meticulously scrutinizing every stage — from code to production — for potential vulnerabilities. Overlooked elements like build artifacts often become prime targets for attackers.

Reduce workflow permissions of runner tokens according to least privilege and review artifact creation in your CI/CD pipelines. By implementing a proactive and vigilant approach to security, defenders can significantly strengthen their project's security posture.

## Prisma Cloud and Other Palo Alto Networks Protection and Mitigation

Prisma Cloud detects vulnerable code that leaks the GITHUB_TOKEN within artifacts, equipping security teams to prevent attackers from using it to inject code into the repository, publishing packages or triggering pipelines, all of which could result in malicious code reaching production. The platform also offers policies to significantly reduce the potential impact of a breach — ensuring minimum permissions granted to pipelines, for example.

Figure 10. Prisma Cloud detects vulnerable code that leaks the GITHUB_TOKEN within artifacts.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America Toll-Free: 866.486.4842 (866.4.UNIT42)
  * EMEA: +31.20.299.3130
  * APAC: +65.6983.8730
  * Japan: +81.50.1790.0200

Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org/).

## Additional Resources

  * [Third-Party GitHub Actions: Effects of an Opt-Out Permission Model](https://www.paloaltonetworks.com/blog/prisma-cloud/github-actions-opt-out-permissions-model/) – Blog, Palo Alto Networks
  * [Demo: Discover if GitHub tokens are uploaded within workflow artifacts](https://interactive.prismacloud.io/share/7we0zyp62ykf) – Prisma Cloud

Back to top

### Tags

  * [Artifacts](https://unit42.paloaltonetworks.com/tag/artifacts/ "artifacts")
  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [GitHub](https://unit42.paloaltonetworks.com/tag/github/ "GitHub")
  * [Open source](https://unit42.paloaltonetworks.com/tag/open-source/ "open source")
  * [Red Hat](https://unit42.paloaltonetworks.com/tag/red-hat/ "Red Hat")
  * [Ubuntu](https://unit42.paloaltonetworks.com/tag/ubuntu/ "Ubuntu")

[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Harnessing LLMs for Automating BOLA Detection ](https://unit42.paloaltonetworks.com/automated-bola-detection-and-ai/ "Harnessing LLMs for Automating BOLA Detection")

### Table of Contents

  * 

### Related Articles

  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ The npm Threat Landscape: Attack Surface and Mitigations (Updated June 2) ](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/ "article - table of contents")
  * [ Frontier AI and the Future of Defense: Your Top Questions Answered ](https://unit42.paloaltonetworks.com/frontier-ai-top-questions-answered/ "article - table of contents")

## Related Cloud Cybersecurity Research Resources

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026 #### [Novel Technique to Detect Cloud Threat Actor Operations ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026 #### [DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of a gift card fraud campaign. A glowing skull and crossbones on a circuit board.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/07_Cybercrime_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 22, 2025 #### [Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign ](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/)

  * [CL‑CRI‑1032](https://unit42.paloaltonetworks.com/tag/cl-cri-1032/ "CL‑CRI‑1032")
  * [Microsoft](https://unit42.paloaltonetworks.com/tag/microsoft/ "Microsoft")
  * [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/ "phishing")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/ "Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image]()
