---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-14_snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system.md
original_filename: 2024-02-14_snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system.md
title: 'Snap Trap: The Hidden Dangers Within Ubuntu’s Package Suggestion System'
category: documents
detected_topics:
- cloud-security
- supply-chain
- sso
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- cloud-security
- supply-chain
- sso
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 7f4aea7589cfd04a342fbf2d3adba3156d184d90adace6033de17b8edde09fd3
text_sha256: ce795e5eb6025ab4731e8a4ffdffa3470fd7c7e214d293b376d49c86aefd6dab
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Snap Trap: The Hidden Dangers Within Ubuntu’s Package Suggestion System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-14_snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, sso, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `7f4aea7589cfd04a342fbf2d3adba3156d184d90adace6033de17b8edde09fd3`
- Text SHA256: `ce795e5eb6025ab4731e8a4ffdffa3470fd7c7e214d293b376d49c86aefd6dab`


## Content

---
title: "Snap Trap: The Hidden Dangers Within Ubuntu’s Package Suggestion System"
page_title: "The Hidden Dangers Within Ubuntu's Package Suggestion System"
url: "https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/"
final_url: "https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/"
authors: ["Ilay Goldman (@GoldmanIlay)"]
programs: ["Ubuntu"]
bugs: ["Supply chain attack"]
publication_date: "2024-02-14"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 433
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

# Snap Trap: The Hidden Dangers Within Ubuntu’s Package Suggestion System

[](https://www.aquasec.com/authors/ilay-goldman/)

[Ilay Goldman](https://www.aquasec.com/authors/ilay-goldman/)

February 14, 2024

![Snap Trap: The Hidden Dangers Within Ubuntu’s Package Suggestion System](https://www.aquasec.com/wp-content/uploads/2024/02/No-title-Blog-main-image-snap-suggestions.jpg)

Aqua Nautilus researchers have identified a security issue that arises from the interaction between Ubuntu’s `command-not-found` package and the snap package repository. While `command-not-found` serves as a convenient tool for suggesting installations for uninstalled commands, it can be inadvertently manipulated by attackers through the snap repository, leading to deceptive recommendations of malicious packages.

Additionally, our research indicates that as many as 26% of commands associated with APT (Advanced Package Tool) packages are vulnerable to impersonation by malicious actors. This issue could pave the way for supply chain attacks affecting Linux users and Windows running WSL. This blog delves into the operational details of `command-not-found`, the risks associated with installing compromised snap packages, and the various attack vectors that could be exploited.  

## The command-not-found package

The `command-not-found` package, is installed by default on Ubuntu, it provides an invaluable service to Linux users: it suggests packages to install when they attempt to execute a command in Bash or Zsh that isn’t available on their system. This is achieved through the implementation of the `command_not_found_handle` function, which Bash calls whenever it encounters an unrecognized command.

The package offers suggestions for both [APT](https://ubuntu.com/server/docs/package-management) and [snap](https://snapcraft.io/) packages. For instance, if a user tries to run `ifconfig` and it’s not installed, the package will recommend installing `net-tools` via apt:

![The package offers suggestions for both apt and snap packages.](https://www.aquasec.com/wp-content/uploads/2024/02/ifconfig-only-apt-suggestion.jpg)

Figure 1: Recommendation to install the ‘net-tools’ package via apt

Similarly, when users attempt to run the `code` command, which is associated with Visual Studio Code, they will receive a recommendation to install the `code` package via snap.

![Recommendation to install the 'code' package via snap](https://www.aquasec.com/wp-content/uploads/2024/02/code-snap-only-suggestion.jpg)

Figure 2: Recommendation to install the ‘code’ package via snap

If a command corresponds to both a snap and an apt package, the `command-not-found` package will suggest both options, as in the case of the `mojo` command:

![Package suggests both options, as in the case of the ‘mojo’ command:](https://www.aquasec.com/wp-content/uploads/2024/02/mojo-snap-and-apt-suggestion.jpg)

Figure 3: The package offers suggestions for both apt and snap packages.

### Understanding the ‘command-not-found’ suggestion algorithm

The `command-not-found` package is equipped with an internal database that associates commands with popular APT packages, it’s important to note that the command name may differ from the package name (like the example of the `ifconfig` command with the `net-tools` package above). This database is only updated when the `command-not-found` package itself is upgraded.

In contrast, for snap packages, the package relies on the `snap advise-snap` command. This functionality, provided by snap, references its own regularly updated database sourced from the [Snap Store](https://snapcraft.io/store).

How does the system decide which package to recommend? To understand this, we can delve into the code snippet below from the `command-not-found` package.

![Code snippet from the ‘command-not-found’ package.](https://www.aquasec.com/wp-content/uploads/2024/02/command-not-found-sourcecode.jpg)

Figure 4: Code snippet from the ‘command-not-found’ package.

The process begins with the `command-not-found` package utilizing the `get_packages` function to identify corresponding APT packages and the `get_snaps` function to retrieve matching snap packages. Subsequently, it assesses several conditions to provide the most accurate suggestion possible. If no exact matches are found within both snap and APT repositories, it attempts to recommend similar commands, accounting for potential typos. In cases where exact matches exist, the suggestion hinges on the number of results, this is because there may be multiple snap or APT packages associated with the same command.

With our understanding of the suggestion mechanism employed by the `command-not-found` package, which relies on the APT and snap repositories, an important question arises: How feasible is it for an attacker to manipulate this system to have their malicious package recommended by the `command-not-found` package?

While APT packages operate on the host operating system without any restrictions, not just anyone can contribute a package to the official APT repositories. The developers must undergo an acceptance process before they are allowed to upload a package.

For these reasons and given that the `command-not-found` package’s APT database isn’t updated regularly, our focus shifts to the potential for attackers to publish malicious packages in the snap repository. 

### Restrictions of snap packages

Now that we’ve established our interest in examining snap packages, it’s crucial to explore the restrictions the snap team has put upon publishers and their packages.

First, we need to understand the confinement level. There are 2 major levels of snap confinement:

  * **Strict** confinement, which is used by most of the snap packages. Strictly confined snaps run in a sandboxed environment, they cannot access files, network, processes, or any other system resources (more details can be found here)
  * **Classic** , which runs on the host’s machine just like an APT package without any restrictions.

This raises an immediate question: why wouldn’t a malicious actor just choose to distribute a classic snap? The safeguard here is the requirement for manual review by the snap team for snaps requesting certain privileges, such as classic confinement. However, not all applications require the complete set of permissions that classic confinement provides while still needing access to specific local system resources. To address this requirement, the interface mechanism was developed.

#### Snap interfaces

Snap interfaces serve as controlled gateways for strictly confined snap packages, enabling them to interact with external resources that are typically off-limits in a sandboxed environment. There are numerous interfaces (a comprehensive list is available [here](https://snapcraft.io/docs/supported-interfaces)), each one of them effectively creates controlled “cracks” in the sandbox walls. Through these openings, snaps can engage with the host’s resources or the environments of other running snaps.

![A partial list of the available snap interfaces.](https://www.aquasec.com/wp-content/uploads/2024/02/list_of_interfaces.jpg)

Figure 5: A partial list of the available snap interfaces.

In the image above, we can observe a partial list of the available snap interfaces. Some interfaces grant snaps substantial privileges, allowing them to access and manipulate sensitive system resources, including account management and sound recording. Others provide more benign capabilities, such as ‘audio-playback,’ which simply permits a snap to play audio.

These interfaces can be categorized based on their auto-connect property. This property determines which interfaces can be attached to a snap package automatically (marked as yes), and which require manual approval by the snap team, just like classic confinement, before they can be published in the store. 

### The dangers of malicious strict snap packages

Our investigation concentrates on the most probable tactics an attacker might employ using malicious snap packages. With this in mind, we’re particularly interested in the capabilities of a snap package that does not trigger any manual review. Specifically, we aim to uncover what an attacker could potentially achieve with a strictly confined snap package, one that leverages only interfaces set to auto-connect without requiring manual approval.

#### The desktop interfaces

Although most of the permissive interfaces require manual review, the desktop interfaces can be connected automatically. These interfaces allow applications that have a Graphical User Interface (GUI) to connect to the display server and show windows on the host system.

In Linux, the display server is a program responsible for managing the graphical output and input on the system, enabling the Graphical User Interface (GUI). Applications communicate with the display server using specific display server protocols. Two examples of such protocols are X11 and Wayland. X11 has been a longstanding display server protocol, while Wayland is a newer protocol aimed at providing a more modern and secure windowing system to replace X11.

The main issue here is that the sandbox confinements strength depends on the capabilities of the display server. Consequently, outdated display servers like the X Window System, which uses the X11 protocol, lack real security separation between windows of different applications. This allows snaps that connect to the X11 interface to eavesdrop on other windows and potentially capture keystrokes from the host machine.

This issue is known to Canonical and [Matthew Garrett](https://twitter.com/mjg59) wrote a [blog](https://mjg59.dreamwidth.org/42320.html) about it in 2016, emphasizing the security gaps that snap confinement has on X11.

He released an [open-source tool](https://github.com/mjg59/xevilteddy) that demonstrates this flaw. I compiled this PoC with a few alterations and ran it on Ubuntu 22:

<https://1665891.fs1.hubspotusercontent-na1.net/hubfs/1665891/snap_teddy_video.mp4>

We can observe in the video above, how executing a snap called `friendlyteddy`, that is strictly confined, can steal the credentials of a user typing them on the host.

While the snap team declare they want to path a transition from the insecure X server to safer display server protocols like Wayland, X server is still commonly used by distributions today. While Wayland is the default protocol in ubuntu 22, the X server still comes installed by default and there are many articles and posts on how to switch in Ubuntu to use the X server instead of Wayland – <https://linuxconfig.org/how-to-use-x-instead-of-wayland-on-ubuntu-22-04>.

#### Kernel vulnerabilities

Even if you avoid using the insecure X11 protocol, there are still risks associated with installing malicious snap packages. The host and all other active snap packages share the same kernel. This means that if there’s a vulnerability within the kernel that a snap package can exploit, it could breach the sandboxing and allow full control over the host system. Numerous vulnerabilities are discovered in the Linux kernel annually. In 2023 alone, there were 282 reported vulnerabilities (according to [stack.watch](https://stack.watch/product/linux/linux-kernel/)). While each vulnerability varies in severity and not all can be exploited through a snap container, the potential threat remains significant.

Furthermore, snaps have an auto-update feature that automatically updates the version of the installed snap to the newest available. While this is good for patching vulnerabilities in the snap package itself, there are also security implications. This feature could be utilized by malicious actors to deploy exploits targeting new vulnerabilities. For instance, an attacker might impersonate a trusted package. Upon the discovery of a critical Linux kernel vulnerability, they could push a malicious update to the snap repository. As a result, the auto-update mechanism would automatically distribute the rogue version to all users, exploiting the kernel vulnerability before the users have had a chance to apply any security patches. 

### Command-Not-Found impersonation of packages

With a foundational understanding of snap packages and the risks associated with installing a malicious one, we circle back to our primary concern: the `command-not-found` package. Our objective now is to investigate how an attacker could potentially exploit the `command-not-found` system to deceive users into installing his malicious package.

#### Snap package commands aliases

Snap’s [documentation](https://snapcraft.io/docs/commands-and-aliases) specifies that to prevent conflicts from different snaps exposing the same application names, the snap’s commands format is `<snap name>.<application name>`. When the snap name is identical to the application name, the command simplifies to just `<snap name>`.

Take, for instance, a scenario where the snap is named `code` and the application is `vscode`, the command executed would be `code.vscode`. Conversely, if the application name also happens to be `code`, aligning with the snap name, the command simplifies from `code.code` to just `code`.

Should a developer wish for their snap to execute a command that deviates from the `<snap name>.<application name>` format and is not simply `<snap name>`, they must request an alias. Such a request initiates a manual review process in which the requested alias is voted on to ensure it aligns with the application.

However, since the registered name is merely an alias rather than the official snap name, the actual snap name remains up for grabs. This means that an attacker could potentially register the corresponding snap name, thereby impersonating the command.

Let’s look at an example.

![Package recommends installing the snap 'tarquin'.](https://www.aquasec.com/wp-content/uploads/2024/02/tarquingui-command-prior-poc.jpg)

Figure 6: Package recommends installing the snap ‘tarquin’.

In the image above, we observe that upon entering the command `tarquingui`, the ‘command-not-found’ package recommends installing the snap `tarquin`. The command `tarquingui` doesn’t match the snap name exactly, which indicates that `tarquingui` is an alias for the `tarquin` snap (the alias request details can be found [here](https://forum.snapcraft.io/t/request-alias-for-tarquingui/25347)). However, as previously noted, since an alias does not equate to a snap name reservation, this leaves room for an attacker to register the `tarquingui` snap name and publish their own snap package under it.

Below is the output of the command, after we published a snap with the name `tarquingui`:

![After we published a snap with the name ‘tarquingui’ ](https://www.aquasec.com/wp-content/uploads/2024/02/tarquingui-command-after-poc.jpg)

Figure 7: after we published a snap with the name ‘tarquingui’

An attacker could systematically review all command aliases through the Snap Store API to identify any alias whose snap name is still available. Upon finding one, they could register a new snap under that name, creating an opportunity to deceive users into installing a malicious package.

It is important to note that the documentation states that an alias is not necessarily unique, and there could be potential conflicts.

#### APT packages commands

We’ve already examined how snap packages could be impersonated, but the possibility of impersonating APT packages presents another concern. As previously mentioned, the `command-not-found` utility relies on a local database located at `/var/lib/command-not-found/commands.db`, which links commands to their corresponding APT packages, guiding users to make accurate installations.

We wanted to examine how many commands listed in this local database could be exploited by an attacker by registering them as snap package names. This would potentially lead to the `command-not-found` utility suggesting a malicious snap package alongside the legitimate APT package.

Upon querying the Snap Store for each command to check for available snap package names, the findings were startling. **We discovered that 26% of the APT package commands were available, presenting a substantial security risk, as they could be registered under an attacker’s account.**

For example, one of these packages is the `jupyter-notebook` package:

![Recommendation of installing the ‘jupyter-notebook’ package via apt](https://www.aquasec.com/wp-content/uploads/2024/02/jupyter-notebook_only_apt_suggestion-12.46.56.jpg)

Figure 8: Recommendation of installing the ‘jupyter-notebook’ package via apt

The maintainers of the `jupyter-notebook` APT package had not claimed the corresponding snap name. This oversight left a window of opportunity for an attacker to claim it and upload a malicious snap named `jupyter-notebook`. Below is the output following our registration of the `jupyter-notebook` snap name and the upload of a dummy “malicious” package:

![The output following our registration of the ‘jupyter-notebook’ snap name ](https://www.aquasec.com/wp-content/uploads/2024/02/jupyter-apt-and-snap-updated-version.jpg)

Figure 9: The output following our registration of the ‘jupyter-notebook’ snap name

We can observe that the command-not-found utility suggests the snap package first, even before the original APT package. This behavior could potentially mislead users into installing the snap package.

The real danger lies in the scale of this issue. While a single malicious snap package posing as a legitimate APT or snap package is troubling, the prospect of an attacker systematically exploiting 26% of the APT package commands, including those with aliases in the snap store, could have devastating consequences.

#### Typosquatting attacks

Beyond matching the exact name of a widely used command, attackers can also leverage typosquatting tactics. This involves taking advantage of common typographical errors made by users.

For instance, consider what could occur if a user accidentally types `ifconfigg` instead of `ifconfig`:

![User accidentally types ‘ifconfigg’ instead of ‘ifconfig’, and it corrects him to ifconfig](https://www.aquasec.com/wp-content/uploads/2024/02/ifconfigg-typosquatting-before.jpg)

Figure 10: User accidentally types ‘ifconfigg’ instead of ‘ifconfig’, and it corrects him to ifconfig

In the example shown above, the command-not-found package helpfully corrects the user, suggesting the `net-tools` package for the mistyped `ifconfig` command. However, the situation becomes more problematic when an attacker capitalizes on these common mistakes by registering a snap with the typo, such as `ifconfigg`.

![‘command-not-found’ suggest the malicious ifconfigg package](https://www.aquasec.com/wp-content/uploads/2024/02/ifconfigg-typosquatting-after.jpg)

Figure 11: ‘command-not-found’ suggest the malicious ifconfigg package

As demonstrated before, the `command-not-found` utility typically corrects the user by suggesting the correct `net-tools` package for the mistyped `ifconfig` command. However, should an attacker register a snap with the name `ifconfigg`, the `command-not-found` would mistakenly match it to this incorrect command and recommend the malicious snap (as demonstrated in the image above), bypassing the suggestion for `net-tools` altogether. 

### Summary and mitigation

The risk of attackers exploiting the `command-not-found` utility to recommend their own malicious snap packages is a pressing concern. The true peril lies in the potential scope of this issue, with attackers capable of mimicking thousands of commands from widely-used packages. Past instances of malicious packages appearing in the Snap Store highlight this issue (see references: [Snapcraft Forum](https://forum.snapcraft.io/t/fake-crypto-apps/37070?u=d0od), [The Next Web)](https://thenextweb.com/news/canonical-finds-hidden-crypto-miners-in-the-linux-snap-app-store).

It remains uncertain how extensively these capabilities have been exploited, underscoring the urgency for heightened vigilance and proactive defense strategies.

To safeguard against such threats, users and package maintainers should adopt several preventative measures:

  * Users should verify the source of a package before installation, checking the maintainers’ credibility and the recommended platform (whether snap or APT).
  * Snap developers with an alias should promptly register the corresponding name if it aligns with their application to prevent misuse.
  * Developers of APT packages are encouraged to register the associated snap name for their commands, preemptively securing them from potential impersonation by attackers.
  * Aqua customers can block the execution of `APT` and `snap` in containerized workloads. The runtime solutions can detect malicious behavior stemming from exploitation of this issue.

**Published under:** [SECURITY RESEARCH](https://www.aquasec.com/category/research/)

**Tags:** [Vulnerability Management](https://www.aquasec.com/tag/vulnerability-management/)

[Ilay Goldman](https://www.aquasec.com/authors/ilay-goldman/)

Ilay Goldman is a Security Researcher at Aqua's research team, Team Nautilus. He specializes in uncovering and analyzing novel security threats and attack vectors in cloud native environments, as well as in supply chain security and open-source vulnerabilities. Before joining Aqua, he gained experience as a red team member. Ilay has also been an active public speaker, presenting his expertise at major cybersecurity events such as Black Hat and RSA.

[](https://www.linkedin.com/in/ilaygoldman/)

[](https://www.facebook.com/sharer/sharer.php?u=https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/) [](https://twitter.com/share?url=https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/&text=Snap%20Trap%3A%20The%20Hidden%20Dangers%20Within%20Ubuntu%26%238217%3Bs%20Package%20Suggestion%20System) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/&title=Snap%20Trap%3A%20The%20Hidden%20Dangers%20Within%20Ubuntu%26%238217%3Bs%20Package%20Suggestion%20System)

Table of Contents

  * The command-not-found package
  * Understanding the 'command-not-found' suggestion algorithm
  * Restrictions of snap packages
  * The dangers of malicious strict snap packages
  * Command-Not-Found impersonation of packages
  * Summary and mitigation

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
