---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-05_new-npm-flaws-let-attackers-better-target-packages-for-account-takeover.md
original_filename: 2022-04-05_new-npm-flaws-let-attackers-better-target-packages-for-account-takeover.md
title: New npm Flaws Let Attackers Better Target Packages for Account Takeover
category: documents
detected_topics:
- supply-chain
- cloud-security
- mfa
- rate-limit
- sso
- idor
tags:
- imported
- documents
- supply-chain
- cloud-security
- mfa
- rate-limit
- sso
- idor
language: en
raw_sha256: c3b421e1dabc105835cf53240f72277212cee7c90ff0306fcdbb923ae85c3de5
text_sha256: efc4f419523a2b0745a4a23e8b2066f224711aea9f7955a5a2765384fad78f62
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# New npm Flaws Let Attackers Better Target Packages for Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-05_new-npm-flaws-let-attackers-better-target-packages-for-account-takeover.md
- Source Type: markdown
- Detected Topics: supply-chain, cloud-security, mfa, rate-limit, sso, idor
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `c3b421e1dabc105835cf53240f72277212cee7c90ff0306fcdbb923ae85c3de5`
- Text SHA256: `efc4f419523a2b0745a4a23e8b2066f224711aea9f7955a5a2765384fad78f62`


## Content

---
title: "New npm Flaws Let Attackers Better Target Packages for Account Takeover"
page_title: "NPM Flaws Let Attackers Target Packages for Account Takeover"
url: "https://blog.aquasec.com/npm-supply-chain-attack"
final_url: "https://www.aquasec.com/blog/npm-supply-chain-attack/"
authors: ["Yakir Kadkoda"]
programs: ["GitHub"]
bugs: ["Information disclosure"]
publication_date: "2022-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2743
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

# New npm Flaws Let Attackers Better Target Packages for Account Takeover

[](https://www.aquasec.com/authors/yakir-kadkoda/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

April 5, 2022

![New npm Flaws Let Attackers Better Target Packages for Account Takeover](https://www.aquasec.com/wp-content/uploads/2022/04/No-Title-Argon-npm-research-blog-image.jpg)

For the past few years, cybercriminals have been hijacking popular npm packages by taking over maintainers’ accounts. As part of our research at Team Nautilus, we discovered two flaws in the npm platform related to two-factor authentication (2FA). An attacker can use these flaws to target npm packages for account takeover attacks. We reported these findings to the npm team (GitHub), which quickly fixed the underlying security gaps.

However, our analysis shows that 32% of the top 35 npm packages are still at risk of account takeover from their dependencies’ owners. This can enable attackers to poison the root package or other npm packages that depend on those popular packages and, as a result, affect millions of npm users. In this blog, we’ll explore the details of the research and examine the security risks of direct and transitive dependencies on npm packages.

## npm and JavaScript

According to the [2021 Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-language), JavaScript is the most used programming language for the ninth year in a row. 65% of developers have used this language in the past year.

For those who are unfamiliar with npm, it stands for [Node Package Manager](https://www.javascripttutorial.net/nodejs-tutorial/what-is-npm/#:~:text=Npm%20stands%20for%20Node%20Package,and%20share%20their%20source%20code). Basically, it’s a package manager for the Node JavaScript platform. npm is also the world’s largest software registry, used by millions of developers to publish and share their code.

![2021-Stack-Overflow-Insights](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-1-2021-Stack-Overflow-Insights.jpg)

2021 Stack Overflow Insights

These days, developers use a lot of third-party open source packages throughout the software development process, which puts them at risk of [software supply chain attacks](https://arxiv.org/abs/2112.10165). Popular package managers such as npm and their users are frequently the targets. Typically, adversaries will embed malicious code directly into a benign package or into one of its direct or transitive dependencies.

A notorious example is [UA-Parser-JS](/npm-library-supply-chain-attack?_ga=2.264576711.97554855.1649160330-461876756.1649160330), an npm package with millions of weekly downloads, which was quickly updated after being compromised with crypto mining and password-exfiltration malware.

How big a problem is this? A [recent report](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021) shows that software supply chain attacks have increased by 650% in 2021 on top of year-over-year growth of 430% in 2020, where attackers injected malicious code into benign packages

If you’re interested to learn more about the various abuse methods and [weaknesses of npm](https://www.aquasec.com/cloud-native-academy/supply-chain-security/npm-vulnerabilities/), it’s worth reading the excellent article [“What are Weak Links in the npm Supply Chain?”](https://arxiv.org/abs/2112.10165)

An attacker can gain access to the desired package in several ways. One method is to obtain one of the package maintainers’ credentials.

According to a [study](https://github.com/ChALkeR/notes/blob/master/Gathering-weak-npm-credentials.md) published in 2017, a security researcher was able to gain direct access to 14% of all npm packages (or indirect access to 54% of packages). He used brute force attacks or reused passwords discovered in other breaches, causing [mass password resets](https://blog.npmjs.org/post/161515829950/credentials-resets) across npm users.

Due to the structure of npm, hijacked or malicious packages have a greater impact. npm encourages creating small packages that solve a single problem. This leads to a multitude of smaller packages that each rely on several other packages.

As a result of the credential compromise research mentioned above, the researcher was able to access some of the most widely used packages, granting him access to a [much broader range of valuable packages](https://duo.com/decipher/hunting-malicious-npm-packages) than he would have otherwise been able to access.

![Picture-2](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-2.jpg)

For example, here’s a [dependency graph](https://deps.dev/npm/express/4.17.2/dependencies/graph) for express, one of the top-10 popular packages on npm, which has a weekly average of 25M downloads as of April 2022.

Attackers who gain access to express’ direct or transitive dependencies are likely to compromise the whole package.

Reality is more complicated because there are several aspects to consider that may affect the root package by one of its dependencies: pinning dependencies, package-lock.json, inability to overwrite a published package, and more. Matthew Bryant reviews several of them in [“Zero-Days” Without Incident – Compromising Angular via Expired npm Publisher Email Domains](https://thehackerblog.com/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/).

[A study from 2019](https://www.usenix.org/conference/usenixsecurity19/presentation/zimmerman) found that on average packages implicitly trust 79 third-party packages and 39 maintainers. Additionally, popular packages often influence more than 100,000 other packages, which makes them a prime target for attacks.

### Security-focused improvements of npm

The [security of npm](https://www.aquasec.com/cloud-native-academy/supply-chain-security/npm-vulnerabilities/) has improved over time as the community became more aware of its security risks.

From February 2022, npm requires 2FA for all maintainers of top-100 npm packages by their dependencies.

Two-factor authentication is [also planned](https://github.blog/2022-02-01-top-100-npm-package-maintainers-require-2fa-additional-security/) for high-impact packages, which are any packages with more than 1 million weekly downloads or 500 dependencies.

For maintainers, 2FA is important because it immediately reduces the risks associated with compromised passwords. If a password is leaked, guessed, or even phished, it’s no longer enough to give an intruder access. Without confirmation of the second factor, a password is useless.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-3.jpg)

Furthermore, npm launched enhanced login verification – it will require additional verification to allow you to log in. A [one-time password](https://docs.npmjs.com/receiving-a-one-time-password-over-email) will be sent to the email address associated with your account if you don’t have 2FA enabled.

But setting up 2FA is always a stronger practice because a one-time password alone isn’t sufficient. If your password for npm was leaked, it’s likely that the password for your private email account has been compromised as well. In many cases, it will be the same password, which allows an attacker to bypass the one-time password sent to your email.

These improvements are all good news from the security perspective. Maintainers without 2FA for package hosting, releasing a new version, or signing in to their npm account are often weak links in the software supply chain.

However, as the saying goes, “A chain is only as strong as its weakest link”. It’s also necessary to enforce the same requirements for the maintainers of direct and transitive package dependencies to ensure package security.

### npm information disclosure: 2FA enumeration

In our study, we tried to find out how many of the popular npm packages, whose maintainers were forced to enable 2FA, were still at risk of account takeover because the maintainers of their direct and transitive dependencies weren’t using 2FA.

Our first challenge was to determine whether users of npm had enabled or disabled 2FA. After all, information like this shouldn’t be available to every user.

It turns out that there’s a simple way to discover it. As a creator of a package, any npm user can be added as a maintainer.

As a result, we can:

  * Create and publish an npm package
  * Browse to package settings page on – [https://www.npmjs.com/package/<packlage_name>/access](https://www.npmjs.com/package/%3cpacklage_name%3e/access)
  * Add the npm user you’re looking to enumerate for 2FA as a maintainer. As an example, before attempting to log in to their account with the leaked password

The user 2FA status will be displayed in the maintainer window:

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-4.jpg)

This feature is meant to protect developers and show how secure the user is when adding the user as a maintainer of a package. But it can also be abused.

In February 2022, we reported these issues to the npm staff via the bug bounty program of GitHub on [HackerOne](https://hackerone.com/github?type=team) and got this answer:

_“It’s a previously identified issue and is being tracked internally. We are actively working on remediating”._

In March 2022, the fix was rolled out, and npm no longer shows a maintainer’s 2FA status.

### npm information disclosure: ‘enforced tfa’ enumeration

As part of the study, we found a way to determine if a particular maintainer must enable 2FA and whether an organization requires its employees to use 2FA.

Any unauthenticated user can inquire if ‘enforced_tfa’ is enabled on another npm user or organization as well as determine if the user is a staff member and other details.

We were surprised to find out that every user or organization profile on npm included this information!

Here are the steps you can reproduce:

  1. Make a request to [https://www.npmjs.com/~<username](https://www.npmjs.com/~%3cusername)> or https://www.npmjs.com/org/<scope_name>
  2. View the responsefrom the request.
  3. Extract the value of ‘enforced_tfa’ and ‘isStaff’ in window.context json.

For example, we can see that Facebook (`fb user`) requires by npm to enable two-factor authentication.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-6.jpg)

We reported the following issues to the npm staff via the bug bounty program of GitHub on [HackerOne](https://hackerone.com/github?type=team). The issue was validated and fixed.

### Timeline of the information disclosure for ‘enforced tfa’ enumeration

  * **14-02-2022:** The issue was reported to GitHub’s bug bounty program at HackerOne.
  * **14-02-2022:** Initial response received from GitHub that they were looking into the issue.
  * **17-02-2022:** Issue confirmed by the GitHub security team.
  * **25-03-2022:** Issue patched on npmjs.com.

### npm research: Technical details

Now that we have a way to determine whether a user has 2FA enabled, we can calculate the percentage of the top npm packages at risk of account takeover from the maintainers of the packages’ dependencies (in case they haven’t enabled 2FA).

A user will be considered at risk when both of the following conditions are met:

  * 2FA isn’t enforced
  * An old/current password has been leaked

To determine this, we’ll use the [haveibeenpwned](https://haveibeenpwned.com/) API and the ‘enforced_tfa’ method to enumerate the enforced 2FA status of npm users.

We’ll write a short Python script that will summarize the results. To simplify the process, we’ll run the script on top-35 npm packages as of February 2022 (displayed on npmjs.com), and then we’ll check the enforced 2FA status of dependency maintainers and a password leak status.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-7.jpg)

It’s worth highlighting that if a false value is returned from the enforced_2fa variable, it doesn’t necessarily mean that the user hasn’t enabled 2FA. However, in this study, we will treat this user as a maintainer that hasn’t enabled 2FA yet so that we can assess the potential risk.

It’s also important to remember that if the package depends on a particular version of another package, attackers won’t be able to affect its dependencies. But in many cases, this may lead to other problems, such as vulnerable packages that are left unpatched.

Also, the package typically depends on its [version using](https://docs.npmjs.com/about-semantic-versioning) the ~/^ symbols, which indicate patches and minor releases. This gives an attacker the opportunity to push malicious packages with patches or minor releases that would directly affect the dependent package.

In addition, even if a package requires a specific version of another package, an attacker with control over one of the maintainers’ accounts can mark the package as vulnerable to push downstream packages to update to the attacker’s malicious package version.

Matthew Bryant provides more details about the impact of this in the article [“Zero-Days” Without Incident – Compromising Angular via Expired npm Publisher Email Domains”](https://thehackerblog.com/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/).

![python](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-8-python.gif)

To simplify the study, we marked a package at risk if at least one route allows dependencies to update the root package with malicious code. During the study, we found that there’s more than one way to do this in most cases.

The following data was obtained for the top-35 popular npm packages after executing the code above. The results refer to February 2022, and you can find the detailed statistics in the appendix.

### npm research: A statistical analysis

Based on our analysis, 32% of top-35 npm packages are still at risk of account takeover from their dependencies’ owners, which allows attackers to abuse the root package.

![owners-and-indirect-owners-of-top-35-npm-packages](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-9-owners-and-indirect-owners-of-top-35-npm-packages.jpg)

It’s also important to note that when it comes to devDependencies, the outcome can be serious.

Practically, the results for devDependencies indicate a 72% exposure rate. Which means the maintainers of these devDependencies haven’t enabled two-factor authentication, and the root package doesn’t use a specific version of these dependencies (i.e., the root package uses the ~/^ symbols).

Furthermore, sometimes packages required in devDependencies are relatively negligible. The download average of devDependencies isn’t high (less than one million downloads) compared to production dependencies, which won’t require their maintainers to enable 2FA by [npm](https://github.blog/2022-02-01-top-100-npm-package-maintainers-require-2fa-additional-security/).

In the following attack vectors, an attacker can gain direct access to the workspace of a root package’s maintainer.

Also, the results imply that whenever there are more indirect maintainers than the direct maintainers of a specific popular package, the package is at risk. There are cases where this ratio is dozens of times and even 125 times in the case of the body-parser package.

A package with many maintainers presents many opportunities to perform account takeovers and social engineering attacks. This is also true for direct and indirect dependencies as well as devDependencies packages.

### ms package: The broader the community, the bigger the risk

Now let’s look more closely at the [ms package](https://www.npmjs.com/package/ms). This package converts various time formats to milliseconds and is relatively small. As of April 2022, this package has 164m downloads a week with about 3200 dependent packages.

The main issue with this package is a large number of maintainers — almost 130.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-10.jpg)

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-11.jpg)

If a package doesn’t depend on a specific version of ms, it might be at serious risk. Like in the case of the humanize-ms package (6M weekly downloads), which depends on ms ^2.0.0 version.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-12.jpg)

Attackers could hide their identity by compromising one of the maintainers’ profiles to take advantage of an oversight by a large team. You can argue that many maintainers also give more supervision, and this is the nature of open source. This is true, but there must also be a limit.

In case you were wondering, about 66% of the ms package maintainers haven’t yet enforced 2FA, and variations of their passwords had been previously leaked.

Another way to avoid the risk of indirect maintainers’ account takeover is by “pinning” dependencies. For example, 78% of indirect maintainers of the debug package are at risk. However, there’s no way to affect the root package (debug package) because it uses the absolute version of dependencies in the package.json file.

The risks described above will be remediated once npm enforces 2FA for all maintainers of packages with more than 1 million downloads.

### Taking it to the extreme: “no-one-left-behind” package

Have you ever heard of the “[no-one-left-behind](https://www.npmjs.com/package/no-one-left-behind)” package? It depends on almost 1000 npm packages from 2018. Imagine how many dependencies and indirect owners this package has and in how many ways it can be affected. Of course, this is an extreme case of dependencies, but it illustrates the point well.

![no-one-left-beind](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-13-no-one-left-beind.jpg)

The dependency graph for the “no-one-left-behind” package

### In summary

In recent years, open source projects and npm in particular have improved their security. However, attackers are also evolving their methods and tools.

As opposed to defenders, attackers only need a single success (one compromised package in our case) to launch an [attack kill chain](https://www.aquasec.com/cloud-native-academy/application-security/cyber-kill-chain/).

According to our study, npm packages with a large number of maintainers are at higher risk of abuse. Developers need to take this into account and at least pin their dependencies while using them.

It’s up to us as developers to minimize the attack surface and make account takeover more challenging for attackers. Otherwise, the results can be damaging to the whole community.

Finally, we strongly encourage developers who contribute to open source and create packages to enable 2FA on all their accounts to keep their communities safe.

We’d like to thank the GitHub/[npm security](https://www.aquasec.com/cloud-native-academy/supply-chain-security/npm-vulnerabilities/) team for their quick response and professional remediation process.

### How Argon can help

  * Argon solution can identify a variety of anomalies in open source packages in use and detect suspicious behavior such as described in this blog.
  * Argon provides visibility into the software supply chain and notifies teams of any deviations from the organization’s 2FA policy.

![](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-14.jpg)

  * Argon can alert teams not only to vulnerabilities in their code but also to misconfigurations and poor security policies in the organization.

### Appendix

![appendix](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-15-appendix.jpg)

**Published under:** [SECURITY RESEARCH](https://www.aquasec.com/category/research/)

**Tags:** [Aqua Open Source](https://www.aquasec.com/tag/aqua-open-source/), [Software Supply Chain Security](https://www.aquasec.com/tag/software-supply-chain-security/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

Yakir Kadkoda was the Director of Security Research at Aqua’s research team, Team Nautilus. 

[](https://www.linkedin.com/in/yakir-kadkoda?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BeZHGPSEWTw60pu3BUApmPA%3D%3D) [](https://twitter.com/YakirKad)

[](https://www.facebook.com/sharer/sharer.php?u=https://www.aquasec.com/blog/npm-supply-chain-attack/) [](https://twitter.com/share?url=https://www.aquasec.com/blog/npm-supply-chain-attack/&text=New%20npm%20Flaws%20Let%20Attackers%20Better%20Target%20Packages%20for%20Account%20Takeover) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.aquasec.com/blog/npm-supply-chain-attack/&title=New%20npm%20Flaws%20Let%20Attackers%20Better%20Target%20Packages%20for%20Account%20Takeover)

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
