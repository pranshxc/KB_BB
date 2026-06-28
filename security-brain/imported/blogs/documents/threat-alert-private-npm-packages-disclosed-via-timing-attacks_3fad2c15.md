---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-12_threat-alert-private-npm-packages-disclosed-via-timing-attacks.md
original_filename: 2022-10-12_threat-alert-private-npm-packages-disclosed-via-timing-attacks.md
title: 'Threat Alert: Private npm Packages Disclosed via Timing Attacks'
category: documents
detected_topics:
- supply-chain
- cloud-security
- access-control
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- supply-chain
- cloud-security
- access-control
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 3fad2c1501768b45a150ac5eff5ba2c8e9bebf8dde28527e57e9952183c1f52a
text_sha256: e0121aecb99dacfa8277c869ebf41cc9c73842cf1dbc8afc374ef1a368fe61eb
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Threat Alert: Private npm Packages Disclosed via Timing Attacks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-12_threat-alert-private-npm-packages-disclosed-via-timing-attacks.md
- Source Type: markdown
- Detected Topics: supply-chain, cloud-security, access-control, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `3fad2c1501768b45a150ac5eff5ba2c8e9bebf8dde28527e57e9952183c1f52a`
- Text SHA256: `e0121aecb99dacfa8277c869ebf41cc9c73842cf1dbc8afc374ef1a368fe61eb`


## Content

---
title: "Threat Alert: Private npm Packages Disclosed via Timing Attacks"
url: "https://blog.aquasec.com/private-packages-disclosed-via-timing-attack-on-npm"
final_url: "https://www.aquasec.com/blog/private-packages-disclosed-via-timing-attack-on-npm/"
authors: ["Yakir Kadkoda"]
programs: ["GitHub"]
bugs: ["Timing attack", "Supply chain attack"]
publication_date: "2022-10-12"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2055
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

# Threat Alert: Private npm Packages Disclosed via Timing Attacks

Threat Alert

[](https://www.aquasec.com/authors/yakir-kadkoda/)[](https://www.aquasec.com/authors/ilay-goldman/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)[Ilay Goldman](https://www.aquasec.com/authors/ilay-goldman/)

October 12, 2022

![Threat Alert: Private npm Packages Disclosed via Timing Attacks](https://www.aquasec.com/wp-content/uploads/2022/10/No-Title-Blog-Image-Private-Packages-Disclosed-Via-Timing-Attack-on-npm.jpg)

We at Aqua Nautilus have discovered that npm’s API allows threat actors to execute a timing attack that can detect whether private packages exist on the package manager. By creating a list of possible package names, threat actors can detect organizations’ scoped private packages and then masquerade public packages, tricking employees and users into downloading them. This kind of attack is linked to a broader category of supply chain attacks. Over the past few years, we’ve seen an increase in the volume and variety of such attacks in the wild. In this blog we’ll dig deeper into this issue and demonstrate how you can mitigate the risks.

## Timing Attack to Detect Private Packages on npm

Our research has shown that by using a timing attack a threat actor can detect the existence of private packages via npm’s API.

For instance, when an unauthenticated user is sending to the npm’s API a `GET` request (`https://registry.npmjs.org/@<scope_name>/<secret_package_name>`) to receive information about a private (scoped) package, the response is that this package isn’t found (http 404 response), whether the package ever existed or not. In the screenshot below, you can see how we sent a request and received a `404 Not found` response (marked in red).

![Request returned 404-Not found as the request came from an unauthenticated and unauthorized user](https://www.aquasec.com/wp-content/uploads/2024/01/0.png)

Example showing how we can request API information about secret-packages, which is a private package under the random-organization scope using Postman.

This request returned `404-Not found` as the request came from an unauthenticated and unauthorized user. Additionally, we can see that the server responded after 686 milliseconds.

If a threat actor sends around five consecutive requests for information about a private package then analyzes the time taken for [npm](https://www.aquasec.com/cloud-native-academy/supply-chain-security/npm-vulnerabilities/) to reply, it is possible for them to determine whether the private package in fact exists. More accurately, this would show whether the package exists now or if it had existed in the past though is now deleted. In both cases, it would be the same result.

Due to this, we can assume that this flaw is embedded in the architecture of the API and is a result of the caching mechanism. To validate that this flaw exists, we conducted the following steps:

#### Creating a private package

As seen in the screenshot below, we created a private [npm](https://www.aquasec.com/cloud-native-academy/supply-chain-security/npm-vulnerabilities/) package and uploaded it.

![we created a private npm package and uploaded it](https://www.aquasec.com/wp-content/uploads/2024/01/1.png)

We then used the organization `random-organization` to upload the npm package `secret-package`. An authenticated user should easily be able to view this package including its name, while an unauthenticated user shouldn’t get any disclosure information about this package. As you can see below, we verified the existence of this package with an authenticated user that belongs to `random-organization` via browser.

![Verification of the existence package with authenticated user belonging to “random-organization” via browser](https://www.aquasec.com/wp-content/uploads/2024/01/2.png)

#### Executing a timing attack

We compared the time it takes to search for a private package that exists with a private package that doesn’t exist. For that, we generated a single consecutive request. But we didn’t find any significant differences.

From various systems, we started generating requests to receive private packages that did exist then compared the results with requests for private packages that did not. In doing so we found a noticeable difference!

Next, we collected and analyzed our findings to optimize the timing attack. We found that if we generated approximately five consecutive API requests as an unauthenticated user and looked for our new private package, it takes on average 648 milliseconds. Yet, if we generated about five consecutive API requests as an unauthenticated user to look for a private package that didn’t exist, it takes on average 101 milliseconds. Consider that if you try to replicate our exact results, there may be some differences due to connection strength and network speed. Still, the results should be quite similar.![Response time in microseconds](https://www.aquasec.com/wp-content/uploads/2024/01/3.png)

![Response time for private versus public packages](https://www.aquasec.com/wp-content/uploads/2024/01/4.png)As you can see in the graph and table above, it takes on average less time to get a reply for a private package that does not exist compared to a private package that does.

### Supply Chain Attack via Code Packages

Threat actors often seek various ways to penetrate your organization. Over the past few years, we’ve seen a dramatic increase by hundreds of percentage points in supply chain attacks.

In some cases, the threat actors’ goal is to gain access to open-source packages/projects and poison them.

Other times they masquerade as private or public packages/projects, deliberately misspelling their names in order to trick unsuspecting victims into downloading their malicious package instead of legitimate popular ones (i.e., installing the Python package ‘Padnas’ instead of ‘Pandas’).

When this occurs, it’s not surprising that these incidents get wide coverage in the media. For instance, Bleeping Computer recently published a story about a supply chain attack in [npm that impacted hundreds of websites and apps](https://www.bleepingcomputer.com/news/security/npm-supply-chain-attack-impacts-hundreds-of-websites-and-apps/). In another report, they explained the risks of [private package names exposure on npm](https://www.bleepingcomputer.com/news/security/npm-fixes-private-package-names-leak-serious-authorization-bug/).

### How attackers can merge everything to an attack

A Scoped Confusion attack usually starts with a threat actor who collects intelligence about a specific organization:

#### A possible package names list

With this in mind, we thought about a few methods that could be used to create a possible package names list:

  * Guess the names of the private packages used by a specific organization by performing a dictionary or a guessing attack.Attackers may try to improve the dictionary list of specific organizations’ private packages by looking for patterns or combinations in the organizations’ public packages. For example, a `contso` organization might have public packages that begin with `@contso/contso -*, @contso/cnt-*, @contso /core-*`.Prefixes like these can be used by an attacker to tweak his list.
  * Online public datasets (such as libreries.io) store historic information about packages. An attacker could search for public packages that were deleted since they may have been converted to private packages.
  * It’s possible for an attacker to map all the scoped packages on npm that don’t have public packages, then create phony malicious packages with the same name. Additionally, attackers can use the npm API to map packages by average download per week to identify the most widely used packages. For example, a package called `@graphql-codegen/visitor-plugin-common` receives 2.2M downloads per week. However, there in fact is no public package called `visitor-plugin-common` on npm. Thus, the attacker can create such a package in order to deceive users into installing it. It’s important to note that npm blocks you from creating and publishing public packages with the names of popular scoped packages, but this is not always the case.

#### Running a timing attack

Now that the attacker has a potential list of scoped private packages, a timing attack could be generated. Threat actors might tweak the algorithm to make minor modifications in their package names list in order to increase the chance of discovering an existing package.

Once the timing attack has finished running, the threat actors would analyze the results, retaining the packages with higher average response times – meaning that the private packages do exist.

#### Building public packages

Now that the threat actors have created a list of possible private scoped packages, they need to check that there are no public packages (package without a scoped) on npm with the same names, meaning they can create malicious package under the public scope of npm.

Note that we don’t encourage cybercrime. We merely describe here ways in which threat actors build their supply chain attacks.

### Summary & Mitigation

In this blog we’ve explained how we discovered a flaw in npm’s API which is disclosing information about organizations’ private packages. Threat actors have the capability to create a list of potential private package names and run timing attacks to verify their existence. Later, threat actors could create public packages masquerading as legitimate private ones and trick unknowing developers into downloading malicious packages.

We have disclosed this information to GitHub which, in response, replied that this architecture of the API is by design.

_“Architectural nuances prevent us from systematically preventing timing attacks from determining whether a specific package exists.”  
_

Here are some steps you can take to mitigate these risks:

  1. Gather a list of all your organization’s private and public packages on all the package management platforms.
  2. Actively look for typo squatting, lookalikes, or masquerading packages. Verify that there are no other packages with the same name as your internal private packages.
  3. If you find any similar packages, make sure that they do not contain malware and notify the relevant stakeholders.
  4. If you don’t find public packages similar to your internal packages, consider creating **public** packages as **placeholders** to prevent such attacks.
  5. If you would like to learn more about protecting yourself when using npm, you can read the following npm blog [Avoiding npm substitution attacks](https://github.blog/security/supply-chain-security/avoiding-npm-substitution-attacks/).

The timeline of the discovery:

  * **03-08-2022:** The issue was reported to GitHub’s bug bounty program at HackerOne.
  * **03-25-2022:** GitHub triaged and responded: “ _Because of these architectural limitations, we cannot prevent timing attacks from determining whether a specific private package exists on npm_ ”

**Published under:** [SECURITY RESEARCH](https://www.aquasec.com/category/research/)

**Tags:** [Security Threats](https://www.aquasec.com/tag/security-threats/), [Supply Chain Attacks](https://www.aquasec.com/tag/supply-chain-attacks/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

Yakir Kadkoda was the Director of Security Research at Aqua’s research team, Team Nautilus. 

[](https://www.linkedin.com/in/yakir-kadkoda?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BeZHGPSEWTw60pu3BUApmPA%3D%3D) [](https://twitter.com/YakirKad)

[Ilay Goldman](https://www.aquasec.com/authors/ilay-goldman/)

Ilay Goldman is a Security Researcher at Aqua's research team, Team Nautilus. He specializes in uncovering and analyzing novel security threats and attack vectors in cloud native environments, as well as in supply chain security and open-source vulnerabilities. Before joining Aqua, he gained experience as a red team member. Ilay has also been an active public speaker, presenting his expertise at major cybersecurity events such as Black Hat and RSA.

[](https://www.linkedin.com/in/ilaygoldman/)

[](https://www.facebook.com/sharer/sharer.php?u=https://www.aquasec.com/blog/private-packages-disclosed-via-timing-attack-on-npm/) [](https://twitter.com/share?url=https://www.aquasec.com/blog/private-packages-disclosed-via-timing-attack-on-npm/&text=Threat%20Alert%3A%20Private%20npm%20Packages%20Disclosed%20via%20Timing%20Attacks) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.aquasec.com/blog/private-packages-disclosed-via-timing-attack-on-npm/&title=Threat%20Alert%3A%20Private%20npm%20Packages%20Disclosed%20via%20Timing%20Attacks)

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
