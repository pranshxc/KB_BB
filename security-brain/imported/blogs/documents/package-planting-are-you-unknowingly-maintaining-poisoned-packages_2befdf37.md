---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-26_package-planting-are-you-unknowingly-maintaining-poisoned-packages.md
original_filename: 2022-04-26_package-planting-are-you-unknowingly-maintaining-poisoned-packages.md
title: 'Package Planting: Are You [Unknowingly] Maintaining Poisoned Packages?'
category: documents
detected_topics:
- supply-chain
- cloud-security
- xss
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- supply-chain
- cloud-security
- xss
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 2befdf374e0c5851792b397893c98ef05fb81b6c61d9564af75d31797de6ebf6
text_sha256: f68860f56eb16fa3fe46db99cc6c23a7bd9e3414086878490187efe8881b8b05
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Package Planting: Are You [Unknowingly] Maintaining Poisoned Packages?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-26_package-planting-are-you-unknowingly-maintaining-poisoned-packages.md
- Source Type: markdown
- Detected Topics: supply-chain, cloud-security, xss, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `2befdf374e0c5851792b397893c98ef05fb81b6c61d9564af75d31797de6ebf6`
- Text SHA256: `f68860f56eb16fa3fe46db99cc6c23a7bd9e3414086878490187efe8881b8b05`


## Content

---
title: "Package Planting: Are You [Unknowingly] Maintaining Poisoned Packages?"
url: "https://blog.aquasec.com/npm-package-planting"
final_url: "https://www.aquasec.com/blog/npm-package-planting/"
authors: ["Yakir Kadkoda"]
programs: ["GitHub"]
bugs: ["Logic flaw"]
publication_date: "2022-04-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2684
---

[How AI Changes the Attack Chain](https://www.aquasec.com/blog/known-techniques-unknown-speed-how-ai-changes-the-attack-chain/) [Sign in](https://cloud.aquasec.com/signin) [Contact](https://www.aquasec.com/about-us/contact-us/) [Support](https://support.aquasec.com/support/home) [We're hiring!](/about-us/careers/)

[Aqua Security](https://www.aquasec.com "Aqua Security")

[Platform](https://www.aquasec.com/aqua-cloud-native-security-platform/)

[Solutions](https://www.aquasec.com/solutions/aws-container-security/)

[Resources](https://www.aquasec.com/resources/)

[Company](/about-us/)

Platform

[ Aqua Platform Unified Cloud Security Gain full visibility, reduce cloud and AI security risks, and stop attacks with Aqua’s fully integrated CNAPP.  Platform overview ](/aqua-cloud-native-security-platform/)

  * [All platform Integrations](https://www.aquasec.com/integrations/)
  * [Aqua CNAPP in action](https://www.aquasec.com/demo/)

[Aqua Open SourceDriving security innovation in the cloud native community](https://www.aquasec.com/products/open-source-projects/)

  * [Trivy](https://trivy.dev/)
  * [Tracee](https://www.aquasec.com/products/tracee/)

Code Security

  * [Scanning & Assurance Scan artifacts across the entire software development lifecycle](https://www.aquasec.com/products/container-scanning)
  * [Software Supply Chain SecurityProtect your code, tools, and processes](/products/software-supply-chain-security/)
  * [Vulnerability ManagementAdvanced Code-to-Cloud vulnerability management to reduce noise and fix fast](/products/container-vulnerability-scanning/)

Runtime Security

  * [Container SecurityFull lifecycle advanced protection for containerized applications ](https://www.aquasec.com/products/container-security/)
  * [Cloud Workload Protection (CWPP)Runtime protection for every cloud native workload](/products/cwpp-cloud-workload-protection/)
  * [Hybrid-Cloud & Multi-Cloud SecurityCode to Cloud security for hybrid and multi-cloud deployments](https://www.aquasec.com/use-cases/multi-cloud-and-hybrid-cloud/)

Posture Management

  * [CI/CD Pipeline SecurityAutomate DevSecOps](https://www.aquasec.com/use-cases/devops-security/)
  * [Kubernetes SecurityHolistic Kubernetes Security for the Enterprise](https://www.aquasec.com/products/kubernetes-security/)
  * [Cloud Security Posture ManagementExtend traditional CSPM with workload visibility](https://www.aquasec.com/products/cspm/)

What's New?

  * [Operationalizing AI Security: Protecting Workloads Where AI Runs](https://www.aquasec.com/blog/operationalizing-ai-security-protecting-ai-workloads/)
  * [Patch, Ditch, Dodge, or Deal? Your Call on Vulnerabilities](https://www.aquasec.com/blog/patch-ditch-dodge-deal-vulnerability-prioritization/)
  * [Securing LLM Apps with Aqua: Beyond the OWASP Checklist](https://www.aquasec.com/blog/secure-llm-applications-aqua-beyond-owasp-list/)
  * [What’s Really Happening in Your Containers? Aqua’s Risk Assessment Has the Answer](https://info.aquasec.com/aqua_csra)

Solutions

Use Cases

  * [Automate DevSecOpsSecurity and speed without compromise](/use-cases/devops-security/)
  * [GenAI Application SecuritySecure GenAI Applications from Code to Runtime](https://www.aquasec.com/solutions/ai-application-security/)
  * [Detection and ResponseCloud native detection & Response (CNDR)](https://www.aquasec.com/use-cases/cndr-cloud-native-detection-and-reponse/)
  * [Hybrid-Cloud & Multi-CloudSecurity for hybrid and multi-cloud deployments](https://www.aquasec.com/use-cases/multi-cloud-and-hybrid-cloud/)
  * [Prove ComplianceControls for PCI, HIPAA, GDPR, and beyond](/use-cases/container-auditing-compliance/)

[Solutions](/solutions/aws-container-security/)

  * [Docker SecurityEnterprise-Grade security for Docker environments](https://www.aquasec.com/solutions/docker-container-security/)
  * [AWS Cloud SecurityProtect cloud native workloads on AWS](/solutions/aws-container-security/)
  * [Google Cloud SecuritySecure K8s apps on Google Cloud Platform](/solutions/google-cloud-kubernetes-security/)

  * [OpenShift SecurityCloud Native Security for Red Hat OpenShift ](/solutions/red-hat-openshift-container-security/)
  * [VMware Tanzu SecurityNative security across VMware Tanzu](/solutions/vmware-tanzu/)
  * [Azure Cloud SecurityComplete Security for Azure Container Workloads](/solutions/azure-container-security/)

[Industry](https://www.aquasec.com/solutions/federal/)

  * [FederalCNAPP solution for Federal Government](https://www.aquasec.com/solutions/federal/)

  * [Financial ServicesOne platform for financial services](https://www.aquasec.com/solutions/finance)

[ ![](https://www.aquasec.com/wp-content/uploads/2025/06/Hybrid-cloud-multi-cloud-resource-thumbnail.jpg) eBook Hybrid Cloud, Multi-Cloud, Every Cloud, Secured. Get your copy ](https://info.aquasec.com/multicloudsecurity)

Resources

[ The best of cloud native Aqua Blog Expert insight, best practices and advice on cloud native security, trends, threat intelligence and compliance Read the Blog ](https://www.aquasec.com/blog/)

  * [SEC vs. SolarWinds: A Cybersecurity Game Changer for CISOs](https://www.aquasec.com/blog/sec-vs-solarwinds-ciso)
  * [Accenture and Aqua Partner to Empower Cloud Security](https://www.aquasec.com/blog/accenture-and-aqua-partner-to-empower-cloud-security)

Resources

  * [Resources CentereBooks, Data sheets, Whitepapers, Webinars, and much more](https://www.aquasec.com/resources/)
  * [The Cloud Native ChannelCloud native security webinars & videos](https://www.aquasec.com/resources/virtual-container-security-channel/)
  * [AquademyThe Aqua academy](https://aquademy.aquasec.com/)

  * [Cloud Native WikiThe educational center for everything cloud native](https://www.aquasec.com/cloud-native-academy/)
  * [Docker Containers](https://www.aquasec.com/cloud-native-academy/docker-container/)
  * [Software supply chain security](/cloud-native-academy/supply-chain-security/supply-chain-security-mitigating-the-supply-chain-threat/)
  * [Cloud security](https://www.aquasec.com/cloud-native-academy/cspm/cloud-security/)
  * [Kubernetes](https://www.aquasec.com/cloud-native-academy/kubernetes-101/kubernetes-complete-guide/)
  * [Application Security](https://www.aquasec.com/cloud-native-academy/application-security/application-security/)
  * [DevSecOps](https://www.aquasec.com/cloud-native-academy/devsecops/devsecops/)

[ ![](https://www.aquasec.com/wp-content/uploads/2019/08/Horizontal-Dark-Abyss.svg) Aqua research team Security research focused on the cloud native stack to identify new threats and attack vectors More security research  ](https://www.aquasec.com/research/)

[ 2023 Annual Aqua Nautilus Research  
A Comprehensive Cloud Native Threat Report ](https://info.aquasec.com/2023-cloud-native-threat-report)

Company

Recognized Leadership

  * [ CISO Choice Awards Winner for Cloud Workload Protection Platform (CWPP) ](https://info.aquasec.com/ciso-choice-awards?utm_source=zoom&utm_campaign=cwpp&utm_content=ciso_awards)
  * [ Forrester Consulting: The Total Economic Impact™ of Aqua CNAPP 90% Reduction in vulnerability research and detection time ](https://info.aquasec.com/forrester-tei)
  * [ Frost & Sullivan CNAPP report Top innovation leader ](https://info.aquasec.com/frost-sullivan-cnapp)

  * [About Us](/about-us/)
  * [Newsroom](/about-us/news/)
  * [Customers](/customers/)
  * [Partners](/partners/)

  * [Careers](/careers/)
  * [Support](https://success.aquasec.com/)
  * [Services](https://www.aquasec.com/services/)
  * [Upcoming Events](/events/)

Connect

  * [Contact](/about-us/contact-us/)
  * [Twitter](https://twitter.com/AquaSecTeam)
  * [Facebook](https://www.facebook.com/AquaSecTeam)
  * [Linkedin](https://www.linkedin.com/company/aquasecteam)
  * [Instagram](https://www.instagram.com/aquaseclife/)

[News](/about-us/news/)

[ ![](https://www.aquasec.com/wp-content/uploads/2024/06/Aqua-Logo-Color-RGB-2022-300x300-1-140x140.jpg) Aqua Security Turns Runtime Intelligence into Action with Agentic Response, Debuts Risk Dashboards ](https://www.aquasec.com/news/aqua-security-turns_runtime_intelligence_into_action_with_agentic_response_risk_daskboards/) [ ![](https://www.aquasec.com/wp-content/uploads/2023/06/Newsroom-logos-forbes-140x140.jpg) Aqua Security Goes All In On Runtime Protection ](https://www.forbes.com/sites/tonybradley/2026/02/12/aqua-security-goes-all-in-on-runtime-protection/) [ ![](https://www.aquasec.com/wp-content/uploads/2024/06/Aqua-Logo-Color-RGB-2022-300x300-1-140x140.jpg) Aqua Security Doubles Down on Runtime to Deliver Measurable Cloud Risk Reduction ](https://www.aquasec.com/news/aqua-security-doubles-down-on-runtime-to-deliver-measurable-cloud-risk-reduction/)

Search

Get Started

[Aqua Blog](https://www.aquasec.com/blog/)

# Package Planting: Are You [Unknowingly] Maintaining Poisoned Packages?

Threat Alert

[](https://www.aquasec.com/authors/yakir-kadkoda/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

April 26, 2022

![Package Planting: Are You \[Unknowingly\] Maintaining Poisoned Packages?](https://www.aquasec.com/wp-content/uploads/2022/04/No-Title-Package-Planting-npm-banner.jpg)

Aqua’s Team Nautilus found a logical flaw in npm that allows threat actors to masquerade a malicious package as legitimate and trick unsuspecting developers into installing it. Up until recently, npm allowed adding anyone as a maintainer of the package without notifying these users or getting their consent. Since you could assign poisoned packages under any popular maintainers, we named this logical flaw and its implications “package planting”. We reported these techniques to the npm team and they fixed the underlying issue.

## What is package planting?

Npm users can add others as package maintainers without getting these users’ approval.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture10-2.jpg)

An attacker can create a malicious npm package and add a few users as its maintainers. If the attacker carefully handpicks these future maintainers, this will affect the reputation and appearance of the package. In other words, an attacker can build a malicious package and add trusted and popular maintainers.

For instance, the package [lodash](https://www.npmjs.com/package/lodash) is highly popular and credible. If we add its owners [Mathias](https://www.npmjs.com/~mathias), [jdalton](https://www.npmjs.com/~jdalton), and [bnjmnt4n](https://www.npmjs.com/~bnjmnt4n) to a new, malicious package, many developers may be tricked into thinking that this package is legitimate and even appealing.

Below are a couple of scenarios for package planting.

## Masquerading a malicious package

An attacker can take any malicious package and masquerade it to look legitimate and attractive by using package planting. Here, we illustrate the concept and show how it was possible to take advantage of this flaw:

  1. Create and publish an npm package with the name `fb_npm_package`.  
![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture1-Apr-27-2022-03-45-24-92-PM.jpg)![fb_nmp_package ](https://www.aquasec.com/wp-content/uploads/2024/01/Picture2.jpg-1.png)
  2. Add the users we wish to incriminate as owners. In this case, we chose to use npm and the Facebook npm profiles.![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture3-Apr-27-2022-03-46-37-64-PM.jpg)![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture4-Apr-27-2022-03-47-27-86-PM.jpg)  
3\. Remove ourselves from the package.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture5-Apr-27-2022-03-48-30-84-PM.jpg)

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture6-Apr-27-2022-03-49-11-18-PM.jpg)

So, with these three simple steps, npm and Facebook are now the owners of our package, and it looks legitimate from all perspectives. The new “forced maintainer” isn’t aware that someone added him as the package maintainer.

The main problem is that any npm user can perform this and add other npm users as maintainers of their own package. The proper invite confirmation mechanism would have prevented this: as it currently works when adding a user to your organization on npm or when inviting collaborators on GitHub.

## Developer defamation

An attacker can use package planting to create a malicious package, add developers in npm he wishes to defame, and report to npm that these developers are abusing the platform. This can lead to embarrassing the developer or even banning them from the platform. If you think that this scenario isn’t plausible, here’s an interesting story that will change your mind.

[WhatsApp banned users](https://www.reddit.com/r/whatsapp/comments/dg5hsd/permanent_ban/) that were part of the groups with insensitive names that may imply illegal or malicious activity. [In some cases](https://www.reddit.com/r/whatsapp/comments/dg5hsd/permanent_ban/), a member of the group as a joke changed the name of the group to the one that suggested illegal activity. As a result, each member of the group was immediately blocked on WhatsApp.

In other cases, a malicious actor created a new group, added other contacts (whose WhatsApp settings allowed this), then renamed the group, which caused WhatsApp to ban all its team members.

## The patch: Confirmation mechanism

Npm promptly fixed the flaw after we reported it by adding a confirmation mechanism for all new package maintainers.

At the moment, the issue has been resolved, and adding a new maintainer without confirmation from the user is no longer possible.

![](https://www.aquasec.com/wp-content/uploads/2024/01/7.jpg)

Now, when you invite new maintainers, an email with an invitation link will be sent to their email address:

![](https://www.aquasec.com/wp-content/uploads/2024/01/8-1.jpg)

## Summary

The issue described in this blog was fixed by npm, and there’s no way to replicate it at this moment. We’d like to thank the GitHub/npm security team for their quick response and professional remediation process.

Over the past few years, open source projects have significantly improved their security. However, attackers get more sophisticated and come up with new ways to exploit them.

Eventually, developers are responsible for what open source packages they use when building applications. To mitigate the risks, it’s important to use reliable sources for any third-party components and to secure your environment with solutions that can detect software supply chain threats such as package planting.

Finally, npm users should check that all the packages that are listed under their name truly belong to them, to make sure they weren’t added to any projects without their consent.

## The timeline of the discovery

  * 10-02-2022: The issue was reported to GitHub’s bug bounty program at HackerOne.
  * 13-02-2022: Response received from GitHub that this issue is being tracked internally and they are actively working on remediating it.
  * 26-04-2022: Issue patched on npmjs.com.

**Published under:** [SECURITY RESEARCH](https://www.aquasec.com/category/research/)

**Tags:** [Security Threats](https://www.aquasec.com/tag/security-threats/), [Software Supply Chain Security](https://www.aquasec.com/tag/software-supply-chain-security/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

Yakir Kadkoda was the Director of Security Research at Aqua’s research team, Team Nautilus. 

[](https://www.linkedin.com/in/yakir-kadkoda?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BeZHGPSEWTw60pu3BUApmPA%3D%3D) [](https://twitter.com/YakirKad)

[](https://www.facebook.com/sharer/sharer.php?u=https://www.aquasec.com/blog/npm-package-planting/) [](https://twitter.com/share?url=https://www.aquasec.com/blog/npm-package-planting/&text=Package%20Planting%3A%20Are%20You%20%5BUnknowingly%5D%20Maintaining%20Poisoned%20Packages%3F) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.aquasec.com/blog/npm-package-planting/&title=Package%20Planting%3A%20Are%20You%20%5BUnknowingly%5D%20Maintaining%20Poisoned%20Packages%3F)

Need to secure enterprise workloads? 

Aqua Cloud Native Application Protection Platform (CNAPP)

Go cloud native with the experts!

[Get Demo](https://www.aquasec.com/demo)

[Aqua Security](https://www.aquasec.com "Aqua Security")

Aqua Security is the pioneer in securing containerized cloud native applications from development to production. Aqua's full lifecycle solution prevents attacks by enforcing pre-deployment hygiene and mitigates attacks in real time in production, reducing mean time to repair and overall business risk. The Aqua Platform, a Cloud Native Application Protection Platform (CNAPP), integrates security from Code to Cloud, combining the power of agent and agentless technology into a single solution. With enterprise scale that doesn’t slow development pipelines, Aqua secures your future in the cloud. Founded in 2015, Aqua is headquartered in Boston, MA and Ramat Gan, IL protecting over 500 of the world’s largest enterprises. 

[![Read Aqua Security reviews on G2](https://www.aquasec.com/wp-content/themes/aqua3/images/g2_gray_8.png)](https://www.g2.com/products/aqua-security/reviews?utm_source=review-widget "Read reviews of Aqua Security on G2")

[](https://www.instagram.com/aquaseclife/ "instagram") [](https://www.linkedin.com/company/aquasecteam "linkedin") [](https://www.youtube.com/c/AquasecTeam "youtube") [](https://twitter.com/AquaSecTeam "twitter") [](https://github.com/aquasecurity "git") [](https://www.facebook.com/AquaSecTeam "facebook")

Use Cases

  * [Automate DevSecOps](/use-cases/devops-security/)
  * [Modernize Security](/use-cases/cloud-workload-security/)
  * [CNDR Cloud Native Detection & Response](/use-cases/cndr-cloud-native-detection-and-reponse/)
  * [Compliance and Auditing](/use-cases/container-auditing-compliance/)
  * [Serverless Containers & Functions](/products/serverless-container-functions/)
  * [Hybrid and Multi Cloud](/use-cases/multi-cloud-and-hybrid-cloud/)
  * [Federal Cloud Native Security](/solutions/federal/)

Environments

  * [Kubernetes Security](/products/kubernetes-security/)
  * [OpenShift Security](/solutions/red-hat-openshift-container-security/)
  * [AWS Security](/solutions/aws-container-security/)
  * [Azure Cloud Security](/solutions/azure-container-security/)
  * [Google Cloud Security](/solutions/google-cloud-kubernetes-security/)
  * [Security for VMware Tanzu](/solutions/vmware-tanzu/)
  * [Docker Security](/solutions/docker-container-security/)
  * [IBM Z Security](https://www.aquasec.com/solutions/ibm-z-security/)

Partners

  * [Technology Partners](/partners/#technology-alliances)
  * [Partner With Us](/partners/#partner-with-us)

Resources

  * [Aqua Security Research](/research/)
  * [The Cloud Native Wiki](/cloud-native-academy/)
  * [Kubernetes 101](/cloud-native-academy/kubernetes-101/kubernetes-complete-guide/)
  * [AWS Cloud Security](/cloud-native-academy/cspm/aws-cloud-security/)
  * [Docker 101](/cloud-native-academy/docker-container/)
  * [The Cloud Native Channel](/resources/virtual-container-security-channel/)
  * [O’Reilly Book: Kubernetes Security](https://info.aquasec.com/kubernetes-security)
  * [CNAPP 101](https://www.aquasec.com/cloud-native-academy/cnapp/what-is-cnapp/)
  * [CSPM 101](https://www.aquasec.com/cloud-native-academy/cspm/cloud-security-posture-management-cspm/)
  * [Container Security 101 ](https://www.aquasec.com/cloud-native-academy/container-security/container-security/)
  * [Learn with Aquademy!](https://aquademy.aquasec.com/)
  * []()

About Us

  * [About Aqua](/about-us/)
  * [Newsroom](/about-us/news/)
  * [Careers](/about-us/careers/)
  * [Brand Guidelines](/brand/)
  * [Trust, Security & Compliance](/trust/security/)
  * [Aqua Cloud Native Protection FAQ](/aquarantee-cloud-native-protection-warranty/)
  * [Professional services](https://www.aquasec.com/services/)

Get in Touch

  * [Aqua Blog](https://www.aquasec.com/blog/)
  * [Contact Us](/about-us/contact-us/)
  * [Success Portal](https://success.aquasec.com/)

Products

  * [Cloud Native Security Platform](/aqua-cloud-native-security-platform/)
  * [CSPM Cloud Security](/products/cspm/)
  * [Container Security](/products/container-security/)
  * [Kubernetes Security](/products/kubernetes-security/)
  * [Serverless Security](/products/serverless-container-functions/)
  * [Cloud VM Security](/products/cloud-vm-security/)
  * [Dynamic Threat Analysis (DTA)](/products/container-analysis/)
  * [Container Vulnerability Scanning](/products/container-vulnerability-scanning/)
  * [Open Source Container Security](/products/open-source-projects/)
  * [Platform Integrations](/integrations/)

[Get Started](/demo/)

Copyright © 2026 Aqua Security Software Ltd. [Privacy Policy](/privacy/) | [Terms of Use](/terms-of-use/) | [Cookie Policy](/cookie-policy/) | Your Privacy Choices | 

Accessibility Tools

Normal text size Medium text size Large text size

* * *

Normal display Black & White display High contrast display

* * *

Stop transitions and animations Underline Links
