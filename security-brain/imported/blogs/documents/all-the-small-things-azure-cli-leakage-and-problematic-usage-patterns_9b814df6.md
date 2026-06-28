---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-14_all-the-small-things-azure-cli-leakage-and-problematic-usage-patterns.md
original_filename: 2023-11-14_all-the-small-things-azure-cli-leakage-and-problematic-usage-patterns.md
title: 'All the Small Things: Azure CLI Leakage and Problematic Usage Patterns'
category: documents
detected_topics:
- cloud-security
- supply-chain
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- cloud-security
- supply-chain
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 9b814df67f6e37a3f37d2e8aee2973a1ed3bf00abe59a4566bbe0ad14c460e8a
text_sha256: e06aec915b1b7ac016cb4ee81b516e1c9f6496cfb3f4afb224dffd4fa272d080
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# All the Small Things: Azure CLI Leakage and Problematic Usage Patterns

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-14_all-the-small-things-azure-cli-leakage-and-problematic-usage-patterns.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `9b814df67f6e37a3f37d2e8aee2973a1ed3bf00abe59a4566bbe0ad14c460e8a`
- Text SHA256: `e06aec915b1b7ac016cb4ee81b516e1c9f6496cfb3f4afb224dffd4fa272d080`


## Content

---
title: "All the Small Things: Azure CLI Leakage and Problematic Usage Patterns"
url: "https://www.paloaltonetworks.com/blog/prisma-cloud/secrets-leakage-user-error-azure-cli/"
final_url: "https://www.paloaltonetworks.com/blog/cloud-security/secrets-leakage-user-error-azure-cli/"
authors: ["Aviad Hahami (@_0xffd)"]
programs: ["Microsoft (Azure)"]
bugs: ["CI/CD", "Information disclosure"]
publication_date: "2023-11-14"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 674
---

* [Blog](https://www.paloaltonetworks.com/blog)
  * [Cloud Security](https://www.paloaltonetworks.com/blog/cloud-security/)
  * [CI/CD](https://www.paloaltonetworks.com/blog/cloud-security/category/ci-cd/)
  * All the Small Things: Azu... 

# All the Small Things: Azure CLI Leakage and Problematic Usage Patterns

[ ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paloaltonetworks.com%2Fblog%2Fcloud-security%2Fsecrets-leakage-user-error-azure-cli%2F)

[ ](https://twitter.com/share?text=All+the+Small+Things%3A+Azure+CLI+Leakage+and+Problematic+Usage+Patterns&url=https%3A%2F%2Fwww.paloaltonetworks.com%2Fblog%2Fcloud-security%2Fsecrets-leakage-user-error-azure-cli%2F)

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paloaltonetworks.com%2Fblog%2Fcloud-security%2Fsecrets-leakage-user-error-azure-cli%2F&title=All+the+Small+Things%3A+Azure+CLI+Leakage+and+Problematic+Usage+Patterns&summary=&source=)

[ ](//www.reddit.com/submit?url=https://www.paloaltonetworks.com/blog/cloud-security/secrets-leakage-user-error-azure-cli/)

[ ](mailto:?subject=All the Small Things: Azure CLI Leakage and Problematic Usage Patterns)

Link copied 

By [Aviad Hahami](/blog/author/aviad-hahami/ "Posts by Aviad Hahami")

Nov 14, 2023

11 minutes

[CI/CD](/blog/cloud-security/category/ci-cd/)

[Products and Services](/blog/category/products-and-services/)

[AppSec](/blog/tag/appsec/)

[Azure](/blog/tag/azure/)

[Cloud Research](/blog/tag/cloud-research/)

[DevOps](/blog/tag/devops/)

[GitHub Actions](/blog/tag/github-actions/)

At the beginning of July 2023, I took a stroll around the [azure/login](https://github.com/Azure/login) GitHub Action repository. Looked through the repository’s issues section, I immediately noticed [issue number 315](https://github.com/azure/login/issues/315). The issue was titled “ _SECURITY: Azure/login in some cases leaks Azure Application Variables to the GitHub build log_ ”. And don’t you just love when things leak stuff? I had to click! Let’s see what’s up.  

## Excuse Me? You Dropped Your Environment Variables

The issue reported by [@NoCopy](https://github.com/NoCopy) stated that “azure/login in some cases leaks Azure Application Variables to the GitHub build log.” The user included an example workflow, a relevant az command use case and an example output that contains alleged credentials.

Figure 1: Security issue reported in the Azure/login project

Well this is pretty straight forward, I thought. You tell me that the Azure CLI simply outputs environment variables to [CI/CD](/cyberpedia/what-is-the-ci-cd-pipeline-and-ci-cd-security) logs without anyone (or at least without many people) knowing? And I can simply try to find these occurrences in the wild? (Remember – “some cases”). That doesn’t sound hard. I decided to give it a shot.

A search for the string shown in the report, “az webapp config appsettings”, using GitHub’s code search, yielded the following result in a [Microsoft-owned repository](https://github.com/Azure-Samples/copilot-nodejs-todo/blob/d927453bb92a0521bd3de416af33c73b90a40a2c/.github/workflows/deploy.yml#L49). See line 49 in figure 2.

Figure 2: GitHub Actions workflow running an az CLI command

Ok, I thought, let’s see if it’s really that easy.

I clicked the View Runs button at the top to see the GitHub Actions workflow logs, scrolled to the relevant step of the workflow run, and then saw these two lurking around:

Figure 3: Microsoft’s workflow logs exposing sensitive information

Well, that was easy. I smiled.

Seeing that the issue is indeed true, I did an initial lookup while also trying to see if I can find other commands.

The initial lookup yielded five vulnerability reports, four to Microsoft and one to GitHub. Throughout the research, I was able to disclose more findings to some other groups that I can’t disclose, per their requests. I reported the findings to the relevant vulnerability disclosure programs, and all were all accepted and fixed. The findings' severities ranged from informative to critical.

## The Azure CLI: Bug or Feature?

In fact, many az functions (which are being run using the Azure CLI) echo back the accessed/created/updated/deleted resource alongside their environment variables, secrets, etc.

Down the line, I also found the following issues:

  1. <https://github.com/Azure/login/issues/27> \- [Security: Potential leak of az secrets on cmdline]
  2. <https://github.com/Azure/k8s-create-secret/issues/3> \- [Security: Pass secrets with --from-file instead of over the command line]

Both of these issues showed environment variables echoing back to the log. That said, I didn’t find a bug here. The Azure CLI actually echoes back this information as intended, so there’s nothing buggy regarding the tool or its output.

What’s actually problematic is the combination of _where_ this tool is running and _who_ can access the run logs.

So while the Azure CLI doesn’t perform anything buggy, when executed in a pipeline with the echoed credentials stored in the pipeline’s log, we suddenly find ourselves in a “who should be able to read the logs” kind of problem.

For public repositories and pipelines, this problem is easy to see and understand — random internet stalkers (_comme moi!_) shouldn’t access your production database keys.

For private repositories you may get a false sense of security due to the “private” title. But given one compromised account/token with the lowest “READ” permissions — suddenly an actor can access raw production credentials and possibly escalate their privileges. Whoops.

Moving on, I wanted to find more variants and occurrences. To do so, I cloned the Azure CLI repo and looked through the various modules ( == about 64 options for different CMDs when running ``az CMD, e.g., “az webapp”), searching for existing leaks in CI logs using command variants.

Figure 5: az commands list

## Observing Usage Patterns of the Azure CLI in the Wild, Wild GitHub Actions

When I looked at the Azure CLI usages, I noted that even for cases where the tool was “supposed” to leak credentials, the developers’ use differentiated between a full leak or the mitigation of it.

Where some developers didn’t know about the tool’s tendency to emit sensitive data, others did know (or at-least played it safe) and proactively mitigate the problem.

Classifying the usages, I found three main variations of usage patterns when using Azure CLI in GitHub actions.

### Pattern 1: Folks Who Didn’t Know

Use cases among people who didn’t anticipate the issue are especially problematic and an easy target for attackers. The developers weren’t aware that the tool is spewing their credentials, so they didn’t put any mitigations in place. This implies, then, that their logs contain raw sensitive information.

In some implementations, though, I saw developers getting “saved by the bell”. This is when the developers defined the about-to-be-echoed credentials as secrets in the workflow — but mainly for the input phase. GitHub Actions later masked, or partially masked, the output of the tool, protecting the tool users. Whether they knew about the nature of the output of the tool, I can’t tell.

In the majority of the “saved by the bell” cases, I wasn’t able to find full raw credentials. For the remaining cases, I encountered partial or insufficient maskings that still left secrets and sensitive data exposed. So no bell today.

Figure 6: Workflow logs with masking and credentials leakage

### Pattern 2: Folks Who Had It Right

Some developers knew, or assumed, that the Azure CLI would leak sensitive data. In these workflows, the developers either manually masked the entirety of the returned values or stored the responses in variables rather than letting them echo to the log. This usage pattern yielded zero credentials. Kudos!

### Pattern 3: The Folks Who Almost Had It Right

Incidents where folks who almost escaped without mishap but didn’t make it in the end were unfortunate to witness and yet fun to find. These incidents happened where developers set up separate pipelines for `create` and `delete` actions (or equivalent).

To explain, let’s look at an example. Let’s assume there's a resource definition in a pipeline called Pipeline A that consumes a secret called “MY_SECRET”. When Pipeline A runs and executes the `az` command, it prints the echoed secret from the Azure CLI response — but masked. This is because GitHub Actions identifies the string as sensitive information, as it should, and masks the string for us (similar to pattern 2; see figure 7).

Figure 7: Pipeline A, defining a secret

Meanwhile, its sibling pipeline, Pipeline B, performs other actions on the same resource, like `delete`. This time the secret “MY_SECRET” isn’t needed to execute the `delete` command and is not defined or used in Pipeline B.

So, when Pipeline B executes the `delete` command, the Azure CLI echoes the resource data securely created by Pipeline A back to Pipeline B! And since Pipeline B never defined “MY_SECRET” as a secret, GitHub Actions doesn’t mask the returned credentials. Eventually, we find ourselves with a pipeline emitting raw credentials to its log, similar to pattern 1.

Figure 8: Pipeline B log leaking the secret

## How to Safely Use Azure CLI in Pipelines

So how can you sleep at night without knowing if your Azure CLI usage will emit sensitive information?

If you’re working solely with private repositories and CI instances, you’re “saved” by the authentication and authorization mechanisms you have. The problem remains bad, just not as bad as it would be for public repositories. Make no mistake, though. Relying on the privacy of your repositories and CIs is an incident waiting to happen, so don’t do it.

To mitigate the issue, you have a few options, depending on your needs.

Prior to trying to handle the output in the log, you should consider replacing the static values in the applications with a more robust mechanism. Azure has a [solution using its Key Vault feature](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/key-vault-parameter?tabs=azure-cli), and by utilizing [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep), for example, you could replace the static sensitive values in your applications settings with references to secrets stored in the vault. Doing so will make all the ‘leakages' in the tool harmless, as the settings will now reference secrets instead of containing their values.

If you need to use the output of the az command, you could do either of the following:

  1. Store the output in a variable so it doesn’t get echoed to the log and use it later in your workflow. This holds up, for example, when testing the return code of an “az” invocation or grepping specific parts of the output.
  2. Use JMESPath queries when fetching information with the tool using the built-in “\--query” feature.

JMESPath (JSON Matching Expression paths) is a query language for searching JSON documents that allows you to declaratively extract elements from a JSON document.

By [using JMESPath you could directly access the desired property](https://learn.microsoft.com/en-us/cli/azure/query-azure-cli?tabs=concepts%2Cbash) in the tool’s response and output only the relevant section/value.

If you don’t need the output of the az command, you could:

  1. Redirect the output to `/dev/null` — This is a basic redirection option you could use to mute the output. Apply it like: “az webapp config ... &> /dev/null”. Note that it’s best to pipe both streams (stdout + stderr) to the location-of-no-return, as Azure CLI sometimes emits the credentials as a part of its error messages. In other words, a simple “az ... > /dev/null” may not suffice.
  2. Use the Azure CLI “output” option — Although I’ve seen a low number of usages of this option, Azure allows setting the desired output format using the “\--output/-o” option. This [option supports various values](https://learn.microsoft.com/en-us/cli/azure/format-output-azure-cli), and for our purposes we could use the “\--output none” option.
  3. Selective masking [Not recommended] — You could go and start masking every returned value in your pipeline, but this will generate a headache and require attention and maintenance, as the usage will change with time. And the tool will change. And GitHub Actions will change. And TL;DR … I do not recommend this approach.

## Famous Last Words

This lookup was fun and a cool thing to accidentally pick up from a random GitHub issues pile. As I stated in the beginning of this post, the bug isn’t sophisticated or actually a bug at all. The usage patterns of Azure CLI, though, are “bugged” and should be reported.

So while we love the relative new ease of cloud-services usage in 202x, we need to remain mindful of what’s printing into those logs, where the logs reside and who can read them.

Happy coding!

## Update: Collaborating with Microsoft on CVE-2023-36052

In addition to solving the issues reported on their open-source projects, Microsoft validated the issues with the Azure CLI and assigned [CVE-2023-36052](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36052) with a CVSS score of 8.6. [Microsoft then made changes to the Azure CLI](https://msrc.microsoft.com/blog/2023/11/microsoft-guidance-regarding-credentials-leaked-to-github-actions-logs-through-azure-cli/), Azure Pipelines and GitHub Actions. They published a new release of Azure CLI as part of their November 2023 Patch Tuesday. By avoiding echoing secrets, the new release prevents leakage in CI pipeline logs, developers' machines, and log aggregators.

We recommend updating the Azure CLI versions used in CI runners and developers’ machines to 2.54, to make sure no secrets are printed to the logs.

## Learn More

Because of the data they store and the workloads they run, CI/CD systems are among the most critical and sensitive assets in your organization. Discover how to apply policy-as-code, implement an effective secrets scanning strategy, adopt least-privileged access, and establish robust logging and monitoring with our [CI/CD Security Checklist](/resources/datasheets/cicd-security-checklist). 

If you haven’t tried Prisma Cloud and would like to, we’d love for you to experience a free[ 30-day Prisma Cloud trial](/prisma/request-a-prisma-cloud-trial).

* * *

## Related Blogs

###  [Data Security Posture Management](/blog/cloud-security/category/data-security-posture-management/), [Products and Services](/blog/category/products-and-services/)

#### [Are Cloud Serverless Functions Exposing Your Data?](https://www.paloaltonetworks.com/blog/cloud-security/secure-access-cloud-serverless-functions/)

###  [AppSec](/blog/cloud-security/category/appsec/), [CI/CD](/blog/cloud-security/category/ci-cd/), [Products and Services](/blog/category/products-and-services/)

#### [Drive Towards Preventing Breaches and Pipeline Attacks with Prisma Cloud](https://www.paloaltonetworks.com/blog/cloud-security/cicd-security-cnapp-risk-prevention/)

###  [CI/CD](/blog/cloud-security/category/ci-cd/), [DevOps](/blog/cloud-security/category/devops/)

#### [Unpinnable Actions: How Malicious Code Can Sneak into Your GitHub Actions Workflows](https://www.paloaltonetworks.com/blog/cloud-security/unpinnable-actions-github-security/)

###  [CI/CD](/blog/cloud-security/category/ci-cd/), [Products and Services](/blog/category/products-and-services/)

#### [Abusing Repository Webhooks to Access Internal CI/CD Systems at Scale](https://www.paloaltonetworks.com/blog/cloud-security/repository-webhook-abuse-access-ci-cd-systems-at-scale/)

###  [CI/CD](/blog/cloud-security/category/ci-cd/), [Products and Services](/blog/category/products-and-services/)

#### [AppSec for the Modern Engineering Ecosystem](https://www.paloaltonetworks.com/blog/cloud-security/appsec-engineering-ecosystem/)

###  [Cloud NGFW](/blog/network-security/category/cloud-ngfw/), [Products and Services](/blog/category/products-and-services/)

#### [Cloud NGFW is Essential for AWS & Azure Cloud Traffic Protection](https://www.paloaltonetworks.com/blog/network-security/cloud-ngfw-is-essential-for-aws-azure-cloud-traffic-protection/)

###  Subscribe to Cloud Security Blogs! 

Sign up to receive must-read articles, Playbooks of the Week, new feature announcements, and more.

![spinner](https://www.paloaltonetworks.com/blog/wp-content/themes/panwblog2023/dist/images/ajax-loader.gif) Sign up 

Please enter a valid email.

By submitting this form, you agree to our [Terms of Use](/legal-notices/terms-of-use) and acknowledge our [Privacy Statement](/legal-notices/privacy). Please look for a confirmation email from us. If you don't receive it in the next 10 minutes, please check your spam folder.

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply. 

## Get the latest news, invites to events, and threat alerts

Enter your email now to subscribe!

Sign up __

By submitting this form, you agree to our [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use) and acknowledge our [Privacy Statement](https://www.paloaltonetworks.com/legal-notices/privacy). 

Sign up __

Get the latest news, invites to events, and threat alerts

Enter your email now to subscribe!

Sign up __

By submitting this form, I understand my personal data will be processed in accordance with [Palo Alto Networks Privacy Statement](/legal-notices/privacy) and [Terms of Use.](/legal-notices/terms-of-use)

Sign up __

Products and Services

  * [ AI-Powered Network Security Platform ](/network-security)
  * [ Secure AI by Design ](/ai-security)
  * [ Prisma AIRS ](/prisma/prisma-ai-runtime-security)
  * [ AI Access Security ](/sase/ai-access-security)
  * [ Cloud Delivered Security Services ](/network-security/security-subscriptions)
  * [ Advanced Threat Prevention ](/network-security/advanced-threat-prevention)
  * [ Advanced URL Filtering ](/network-security/advanced-url-filtering)
  * [ Advanced WildFire ](/network-security/advanced-wildfire)
  * [ Advanced DNS Security ](/network-security/advanced-dns-security)
  * [ Enterprise Data Loss Prevention ](/sase/enterprise-data-loss-prevention)
  * [ Enterprise IoT Security ](/network-security/enterprise-device-security)
  * [ Medical IoT Security ](/network-security/medical-device-security)
  * [ Industrial OT Security ](/network-security/medical-device-security)
  * [ SaaS Security ](/sase/saas-security)

  * [ Next-Generation Firewalls ](/network-security/next-generation-firewall)
  * [ Hardware Firewalls ](/network-security/hardware-firewall-innovations)
  * [ Software Firewalls ](/network-security/software-firewalls)
  * [ Strata Cloud Manager ](/network-security/strata-cloud-manager)
  * [ SD-WAN for NGFW ](/network-security/sd-wan-subscription)
  * [ PAN-OS ](/network-security/pan-os)
  * [ Panorama ](/network-security/panorama)
  * [ Secure Access Service Edge ](/sase)
  * [ Prisma SASE ](/sase)
  * [ Application Acceleration ](/sase/app-acceleration)
  * [ Autonomous Digital Experience Management ](/sase/adem)
  * [ Enterprise DLP ](/sase/enterprise-data-loss-prevention)
  * [ Prisma Access ](/sase/access)
  * [ Prisma Browser ](/sase/prisma-browser)
  * [ Prisma SD-WAN ](/sase/sd-wan)
  * [ Remote Browser Isolation ](/sase/remote-browser-isolation)
  * [ SaaS Security ](/sase/saas-security)

  * [ AI-Driven Security Operations Platform ](/cortex)
  * [ Cloud Security ](/cortex/cloud)
  * [ Cortex Cloud ](/cortex/cloud)
  * [ Application Security ](/cortex/cloud/application-security)
  * [ Cloud Posture Security ](/cortex/cloud/cloud-posture-security)
  * [ Cloud Runtime Security ](/cortex/cloud/runtime-security)
  * [ Prisma Cloud ](/prisma/cloud)
  * [ AI-Driven SOC ](/cortex)
  * [ Cortex XSIAM ](/cortex/cortex-xsiam)
  * [ Cortex XDR ](/cortex/cortex-xdr)
  * [ Cortex XSOAR ](/cortex/cortex-xsoar)
  * [ Cortex Xpanse ](/cortex/cortex-xpanse)
  * [ Unit 42 Managed Detection & Response ](/cortex/managed-detection-and-response)
  * [ Managed XSIAM ](/cortex/managed-xsiam)

  * [ Next-Generation Identity Security ](/idira)
  * [ Privileged Access Management ](/idira/human/privileged-access-management)
  * [ Identity and Access Management ](/idira/human/identity-and-access-management)
  * [ Endpoint Privilege Manager ](/idira/human/endpoint-privilege-manager)
  * [ Identity Governance ](/idira/human/identity-governance)
  * [ Workforce Password Management ](/idira/human/workforce-password-management)
  * [ Agentic Identities ](/idira/agentic)
  * [ Secrets Management ](/idira/machine/secrets-management)
  * [ Unified Secrets Governance ](/idira/machine/unified-secrets-governance)
  * [ Application Credentials Delivery ](/idira/machine/application-credentials-delivery)
  * [ Vendor Privileged Access ](/idira/human/vendor-privileged-access)
  * [ Threat Intel and Incident Response Services ](/unit42)
  * [ Proactive Assessments ](/unit42/assess)
  * [ Incident Response ](/unit42/respond)
  * [ Transform Your Security Strategy ](/unit42/transform)
  * [ Discover Threat Intelligence ](/unit42/threat-intelligence-partners)

Company

  * [ About Us ](/about-us)
  * [ Careers ](https://jobs.paloaltonetworks.com/en/)
  * [ Contact Us ](/company/contact-sales)
  * [ Corporate Responsibility ](/about-us/corporate-responsibility)
  * [ Customers ](/customers)
  * [ Investor Relations ](https://investors.paloaltonetworks.com/)
  * [ Location ](/about-us/locations)
  * [ Newsroom ](/company/newsroom)

Popular Links

  * [ Blog ](/blog/)
  * [ Communities ](/communities)
  * [ Content Library ](/resources)
  * [ Cyberpedia ](/cyberpedia)
  * [ Event Center ](https://events.paloaltonetworks.com/)
  * [ Manage Email Preferences ](https://start.paloaltonetworks.com/preference-center)
  * [ Products A-Z ](/products/products-a-z)
  * [ Product Certifications ](/legal-notices/trust-center/compliance)
  * [ Report a Vulnerability ](/security-disclosure)
  * [ Sitemap ](/sitemap)
  * [ Tech Docs ](https://docs.paloaltonetworks.com/)
  * [ Unit 42 ](https://unit42.paloaltonetworks.com/)
  * [ Do Not Sell or Share My Personal Information ](https://panwedd.exterro.net/portal/dsar.htm?target=panwedd)

  * [ Privacy ](/legal-notices/privacy)
  * [ Trust Center ](/legal-notices/trust-center)
  * [ Terms of Use ](/legal-notices/terms-of-use)
  * [ Documents ](/legal)

Copyright © 2026 Palo Alto Networks. All Rights Reserved

  * [ ](https://www.youtube.com/user/paloaltonetworks)
  * [ ](/podcasts/threat-vector)
  * [ ](https://www.facebook.com/PaloAltoNetworks/)
  * [ ](https://www.linkedin.com/company/palo-alto-networks)
  * [ ](https://twitter.com/PaloAltoNtwks)
  * EN __

Select your language
