---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-08_coreplague-severe-vulnerabilities-in-jenkins-server-lead-to-rce.md
original_filename: 2023-03-08_coreplague-severe-vulnerabilities-in-jenkins-server-lead-to-rce.md
title: 'CorePlague: Severe Vulnerabilities in Jenkins Server Lead to RCE'
category: documents
detected_topics:
- xss
- cloud-security
- supply-chain
- command-injection
- automation-abuse
- sso
tags:
- imported
- documents
- xss
- cloud-security
- supply-chain
- command-injection
- automation-abuse
- sso
language: en
raw_sha256: 3673eefd1b5a66ed391f0b9964ca540cfe9777fc40eef1848a5423165c9e6f38
text_sha256: 70e2e6453fdb65bb7e39d2ebf6e5c1d5176ca4d86a5386d3e1ead40164e6836a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# CorePlague: Severe Vulnerabilities in Jenkins Server Lead to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-08_coreplague-severe-vulnerabilities-in-jenkins-server-lead-to-rce.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, supply-chain, command-injection, automation-abuse, sso
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `3673eefd1b5a66ed391f0b9964ca540cfe9777fc40eef1848a5423165c9e6f38`
- Text SHA256: `70e2e6453fdb65bb7e39d2ebf6e5c1d5176ca4d86a5386d3e1ead40164e6836a`


## Content

---
title: "CorePlague: Severe Vulnerabilities in Jenkins Server Lead to RCE"
page_title: "Critical Vulnerabilities in Jenkins Server Lead to RCE"
url: "https://blog.aquasec.com/jenkins-server-vulnerabilities"
final_url: "https://www.aquasec.com/blog/jenkins-server-vulnerabilities/"
authors: ["Ilay Goldman (@GoldmanIlay)", "Yakir Kadkoda"]
programs: ["Jenkins"]
bugs: ["RCE", "XSS", "Security code review"]
publication_date: "2023-03-08"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1406
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

# CorePlague: Critical Vulnerabilities in Jenkins Server Lead to RCE

[](https://www.aquasec.com/authors/ilay-goldman/)[](https://www.aquasec.com/authors/yakir-kadkoda/)

[Ilay Goldman](https://www.aquasec.com/authors/ilay-goldman/)[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

March 8, 2023

![CorePlague: Critical Vulnerabilities in Jenkins Server Lead to RCE](https://www.aquasec.com/wp-content/uploads/2023/03/No-Title-Blog-Image-Jenkins-Blog-updated.jpg)

Aqua Nautilus researchers have discovered a chain of critical vulnerabilities, dubbed CorePlague, in the widely used Jenkins Server and Update Center ([CVE-2023-27898](https://nvd.nist.gov/vuln/detail/CVE-2023-27898), [CVE-2023-27905](https://nvd.nist.gov/vuln/detail/CVE-2023-27905)). Exploiting these vulnerabilities could allow an unauthenticated attacker to execute arbitrary code on the victim’s Jenkins server, potentially leading to a complete compromise of the Jenkins server.

Furthermore, these vulnerabilities could be exploited even if the Jenkins server is not directly reachable by attackers and could also impact self-hosted Jenkins servers.

![Critical Vulnerabilities in Jenkins Server Lead to RCE](https://www.aquasec.com/wp-content/uploads/2023/03/Gif_Jenkins.gif)

  

## **The Research in a Nutshell**

Jenkins is an open-source automation server that supports the software development lifecycle (SDLC) and can be customized using plugins to extend its functionality.

During our research, we found vulnerabilities in how Jenkins processes available plugins, which can result in security issues ranging from cross-site scripting (XSS) to [remote code execution (RCE)](https://www.aquasec.com/cloud-native-academy/cloud-attacks/remote-code-execution/).

The vulnerabilities are achieved through a stored XSS exploitable by a Jenkins plugin with a malicious core version, which attackers upload to the [Jenkins Update Center](https://github.com/jenkins-infra/update-center2/releases/tag/update-center2-3.15).

Once the victim opens the Available Plugin Manager on their Jenkins Server, the XSS is triggered, allowing attackers to run arbitrary code on the Jenkins Server utilizing the [Script](https://www.jenkins.io/doc/book/managing/script-console/) [Console API](https://www.jenkins.io/doc/book/managing/script-console/).

Importantly, the vulnerability is triggered without any additional action from the victim, and the exploitation does not require the manipulated plugin to be installed.

Attackers could exploit these vulnerabilities to compromise Jenkins Servers, even though they are not directly reachable because the public Jenkins Update Center – which is used by default on Jenkins Servers to obtain available plugin lists – could be injected by attackers.

We disclosed these vulnerabilities CVE-2023-27898 and CVE-2023-27905 to the Jenkins team in January 2023. The Jenkins team acknowledged the vulnerabilities and issued a patch for the Jenkins server. They also released a patch for the Jenkins Update Center. We appreciate their collaboration and professionalism during the disclosure process.

### **Frequently Asked Questions  
**

#### **Do I need to patch my Jenkins Servers?**

The Jenkins team released a patch for the public Jenkins Update Center on February 15, which mitigates some risks associated with this vulnerability since it is the first component involved. This is particularly significant since most Jenkins users rely on the public Jenkins Update Center for the list of the available Jenkins plugins. This means that if you rely on the public Jenkins Update Center to get plugins, your Jenkins server will be vulnerable but probably not exploitable. Thus, there is no immediate need to update it.  
However, if you use self-hosted or customized Update Centers, you are at risk.

#### **Which Jenkins Server versions are vulnerable?**

Jenkins servers running versions 2.270 through 2.393 (both inclusive), LTS 2.277.1 through 2.375.3 (both inclusive) are vulnerable (this blog will detail a limitation of exploitation for the latest versions) 

#### **Which Jenkins Update Center versions are vulnerable?**

Jenkins Update Centers with versions below 3.15 are vulnerable.

Detailed information is available in the [Jenkins Security Advisory 2023-03-08](https://www.jenkins.io/security/advisory/2023-03-08/).

### Some Basic Jenkins Definitions  

Artifact registry A binary repository manager used for storing and [managing software artifacts](https://www.jenkins.io/doc/developer/publishing/artifact-repository/). The Jenkins project uses its own Artifactory binary repository, to distribute core, library, and plugin releases.

Jenkins Update Center A component of the Jenkins automation server that provides access to a wide range of [plugins and updates for the Jenkins platform](https://www.jenkins.io/templates/updates/). It allows Jenkins administrators to easily discover, download, and install plugins that extend the functionality of their Jenkins server. This is also known as Jenkins community update sites.

**Jenkins Server** Jenkins is a widely used [open-source automation server](https://www.jenkins.io/) that enables continuous integration and delivery of software projects.  
  
**Jenkins plugins** are software components that extend the functionality of the Jenkins Server, enabling users to enhance and customize their experience, and the automation process. These [Jenkins plugins](https://www.jenkins.io/doc/book/managing/plugins/) offer features such as source code management, build triggers, notification mechanisms, and integrations with external tools and systems. They can be installed, updated, and managed via the Jenkins Update Center.  
The vulnerabilities we describe in our blog are related to Jenkins plugins. 

### **Improper Sanitation: The Jenkins Update Center**

Now that we have a clear understanding of what a Jenkins plugin is, let’s understand the process of creating a plugin so it will be available for everyone.

In short, the initial uploading process is to write a plugin in Java and submit a pull request to the Jenkins team. After review and approval, a GitHub repository will be created at https://github.com/jenkinsci/your_plugin_name, and you will be granted write access to it.

Furthermore, the Jenkins team grants you write access to the[ artifact registry](https://repo.jenkins-ci.org/ui/), allowing you to upload the compiled plugin.

Once the initial plugin release has been approved by the Jenkins team (which is usually just a procedural step), developers can release subsequent versions of the plugin without any involvement from the team.

As a result, an attacker could potentially upload a harmless plugin and then change it to a manipulated one without requiring any additional approval.

To publish a new version of a plugin to the artifact registry, developers must run the publish command, which builds the project and stores it in a designated folder. As illustrated in the image below (with _ascii-magician_ as the plugin name in this example):

![Directory containing artifacts of compiled plugin](https://www.aquasec.com/wp-content/uploads/2024/01/picture-1.png)

Once the build is complete, the publish command uploads the resulting artifacts (such as the `plugin_name.hpi`, `plugin_name.jar`, and `plugin_name-ver.pom` files) to the artifact registry.

Before we proceed let’s examine the `.hpi` file that was uploaded to the artifact registry.

![Understanding ascii-magician.hpi is a zip](https://www.aquasec.com/wp-content/uploads/2024/01/picture-2.png)

The `.hpi` file is actually a compressed zip file that contains various files and directories. Let’s take a closer look at the `META_INF/ MANIFEST.MF` file:

![image 3 - The generated Manifest file of a compiled plugin](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-3-other-colors.png)

The META-INF/MANIFEST.MF file contains key-value pairs that provide metadata about the plugin being published. (The Jenkins-Version is highlighted for future references.)

So far, we’ve provided an overview of the uploading process from the publisher’s perspective. Now after the artifacts are in the artifact registry, let’s shift our focus to the _Update Center_ that provides the plugins to the Jenkins Server.

The Update Center processes all the plugins in the artifact registry and generates the update-center.json file that contains metadata about all available plugins. This file can be found here: <https://updates.jenkins.io/update-center.json>

To illustrate, let’s take a brief look at an example of the metadata associated with a plugin:

![Example of a json metadata of a plugin](https://www.aquasec.com/wp-content/uploads/2024/01/Picture-4-New-colors.png)

In the image above, you can see some of the metadata of the pam-auth plugin. This metadata includes details such as build date, labels, URL for download and the requiredCore which is the minimum Jenkins-Version that is required for the plugin.

How is the metadata of the plugin added to this JSON file?  
The Update Center fetches the plugins from the artifact registry and for each plugin creates a JSON of metadata about the plugin. Here is how a part of the JSON is constructed:

![Example of a json metadata of a plugin](https://www.aquasec.com/wp-content/uploads/2024/01/picture-5.png)

From the [image](https://github.com/jenkins-infra/update-center2/blob/master/src/main/java/io/jenkins/update_center/json/PluginVersionsEntry.java) above, we can observe the JSONField of requiredCore is assigned from the HPI through the function hpi.getRequiredJenkinsVersion(). Let’s now examine this function:

![Code from the update-center2 showing the requiredCore attribute](https://www.aquasec.com/wp-content/uploads/2024/01/picture-6.png)

In this [image](https://github.com/jenkins-infra/update-center2/blob/update-center2-3.14/src/main/java/io/jenkins/update_center/HPI.java), we can see there is a use of the function getManifestAttributes().getValue(“Jenkins-Version“) which retrieves the value of the Jenkins-Version key from the Manifest file within the plugin’s HPI file (in the example of the manifest above it will return 2.361.3).

The code verifies that the obtained value is not _null_ and then assigns it to the requiredCore JSONField that was mentioned earlier. Therefore, there is no sanitization of the requiredCore field at the Update Center, allowing an attacker to input any string in this field.

In summary, the attacker can upload an HPI file containing a Manifest file with a Jenkins-Version field that can have any value without restrictions. This value will be inserted into the requiredCore field of the JSON located at <https://updates.jenkins.io/update-center.json>

### **CVE-2023-27905**

The Update Center is also a website where users can browse to view the available plugins and retrieve information about them. This can be done by accessing this URL https://updates.jenkins.io/download/plugins/plugin_name/ 

Now, let’s look at the following page:

![Code from the update-center2 retrieving the Jenknins-Version value from the plugin's Manifest](https://www.aquasec.com/wp-content/uploads/2024/01/picture-7.png)

On this [page](https://updates.jenkins.io/download/plugins/script-security/), we can view details about the script-security plugin, including the hashes and required Jenkins Server version for each version of the plugin.

In previous sections, we showed how an attacker can manipulate the Jenkins-Version attribute of a plugin by modifying its Manifest file, and that the Update Center does not perform any input sanitization on this field. Now, what if an attacker attempted to insert an XSS payload into the Jenkins-Version attribute, such as:  
<image src =q onerror=prompt(8)>

Let’s examine the code that generates this page: ![picture 8](https://www.aquasec.com/wp-content/uploads/2024/01/picture-8.png)

As we can observe from the [code](https://github.com/jenkins-infra/update-center2/blob/master/src/main/java/io/jenkins/update_center/IndexHtmlBuilder.java), the value of requiredJenkinsVersion is directly appended to the HTML without any escaping.

Therefore, an attacker can potentially upload a plugin with the XSS payload shown earlier in the Jenkins-Version attribute.

Then, when a user accesses the URL of the plugin https://updates.jenkins.io/download/plugins/attacker_plugin, the payload will be executed in their browser:

![Code from the update-center2 not escaping the requiredJenkinsVersion parameter](https://www.aquasec.com/wp-content/uploads/2024/01/picture-9.png)

This vulnerability has been identified as CVE-2023-27905, and the Jenkins team has patched it on their hosted website. 

### **CVE-2023-27898**

In our previous demonstration of the vulnerability, we identified an XSS on the user in the site [updates.jenkins.io](http://updates.jenkins.io), which could be exploited for various malicious purposes. As our objective was to identify potential threats to internal networks within the context of the Jenkins Server, we continued our search.

Given that the attacker can control the requiredCore value of a plugin uploaded to the Jenkins update site, it is critical to examine how the Jenkins Server will handle this value.

#### How are the Jenkins Server and the Jenkins Update Center connected?

The Jenkins Server interacts with the Jenkins Update Center to obtain information about available plugins and to download and install updates and plugins for the Jenkins Server.

The Jenkins Server obtains the available plugin list from the URL <https://updates.jenkins.io/update-center.json> and stores a copy of it. 

This list is updated automatically, or manually by triggering an update through the Check now button on the Available Plugins page in the Jenkins Server.

![XSS triggered on the plugin's page in the updates.jenkins.io site](https://www.aquasec.com/wp-content/uploads/2024/01/picture-10.png)  
Where is the requiredCore value, controlled by the attacker, used?

Whenever a Jenkins admin accesses the _Available Plugin Manager_ page (http://<Jenkins_URL>/manage/pluginManager/available) to search for a plugin,

the available plugin list that the Jenkins Server retrieves from the Update Center is processed by the Jenkins Server.

For each available plugin within the list, the Jenkins Server checks if the plugin was built for a newer version of Jenkins Server [by comparing](https://github.com/jenkinsci/jenkins/blob/bedd4fe/core/src/main/java/hudson/model/UpdateSite.java#L1395-L1402) the plugin’s requiredCore version of the plugin to the current Jenkins Server version.

![Code of the Jenkins Server comparing plugin core version to it's own version](https://www.aquasec.com/wp-content/uploads/2024/01/picture-11.png)

If built for a newer version, the[ Jenkins Server](https://github.com/jenkinsci/jenkins/blob/bedd4fe/core/src/main/java/hudson/PluginManager.java#L1483-L1485) will return the following message: “Warning: This plugin is built for Jenkins {attacker control requiredCore} or newer. Jenkins will refuse to load this plugin if installed.”

![Code of the Jenkins Server shwoing error message embeded with the requireCore of the plugin](https://www.aquasec.com/wp-content/uploads/2024/01/picture-12.png)

This warning will eventually be rendered by the [available.hbs](https://github.com/jenkinsci/jenkins/blob/bedd4fe/war/src/main/js/templates/plugin-manager/available.hbs#L33-L37) file:

![ Code of the Jenkins Server rendering the warning message without escaping](https://www.aquasec.com/wp-content/uploads/2024/01/picture-13.png)

The issue here is that the previous warning message will be rendered using the[ triple-stash {{{ Handlebars](https://handlebarsjs.com/guide/#html-escaping) notation. Which means, any values inside these triple-stash handlebars notation will not be escaped.

In this case, attackers can manipulate the requiredCore version in the warning message, allowing [malicious scripts](https://www.aquasec.com/cloud-native-academy/vulnerability-management/malicious-code/) contained within the message to execute without being properly escaped.

In summary, the attacker has uploaded a Jenkins plugin with a malicious core version e.g., 9.9.9<image src =q onerror=prompt(8)> to the Jenkins Update Center.

Now because the Jenkins plugin with the malicious core version is bigger than the victim Jenkins server version, a warning message will be displayed. (Assume the victim has Jenkins version 2.270, which means the malicious plugin version starts with _9.X.payload_ considers for a larger version of Jenkins server according to the isForNewerHusdon function.) 

As a result, whenever a Jenkins admin accesses the _Available Plugin Manage_ r page (http://<Jenkins_Server>/manage/pluginManager/available) to install or search for a plugin, the malicious core version will render, displaying a warning message and triggering the XSS.

It’s important to note that the XSS vulnerability will be triggered without installing any malicious plugins; simply the presence of a malicious plugin in the feed is enough to activate the vulnerability.

### **The Tiering** Mechanism

From the previous section, it seems that an attacker can easily compromise every Jenkins server in the world. However, this is not entirely accurate.

The Jenkins team implemented a site tiering mechanism to show only plugins that are compatible with the current Jenkins Server, meaning the requiredCore version of the plugin is older than the Jenkins Server. Since the requiredCore version is older, the warning message shown earlier will not appear, and the requiredCore value will not be processed as HTML, making it safe from the XSS.

In order to determine if there are any vulnerable versions, it is essential for us to possess a basic understanding of the tiering mechanism.

When the Jenkins Server wants to update the list of available plugins, it sends a request to the JSON in the update center along with a version parameter that matches the Jenkins server version, for example: <https://updates.jenkins.io/update-center.json?version=2.332.3>

The Update Center then employs this version parameter to redirect the request to a distinct URL, which corresponds to a different JSON. For instance, the previously mentioned URL would redirect to <https://updates.jenkins.io/dynamic-stable-2.332.3/update-center.json>

The JSON of this particular version will contain all the plugins that require a version of requiredCore that is either 2.332.3 or earlier.

In the interest of simplicity, we will not delve into the complete tiering mechanism. Nonetheless, it’s important to note that not all versions have an individual page, and the earliest version to possess a dedicated page is one that has been released for less than 400 days (we have simplified this explanation).

Therefore, if a Jenkins Server version that is older than 400 days makes the request, it will be redirected to the oldest version that has an individual page.

For instance, in the present time, the oldest version that has a dedicated page is 2.319.2. Consequently, if a Jenkins Server with an earlier version, such as 2.319, submits the following request: https://updates.jenkins.io/update-center.json?version=2.319.1 

The request will be redirected to https://updates.jenkins.io/dynamic-stable-2.319.2/update-center.json 

We understand that the JSON located at _h_ ttps://updates.jenkins.io/dynamic-stable-2.319.2/update-center.json contains all the plugins that require a version of requiredCore that is 2.319.2 or earlier. Nonetheless, the Jenkins Server that initiated the request has an older version of 2.319.1. As a result, the Jenkins Server will receive plugins that require a newer version of requiredCore than its own and, therefore, display the warning message as shown earlier.

Having established the existence of versions that display the warning message, the question arises: how can we exploit it?  
To achieve this, we need to select the oldest version with a page, which is currently 2.319.2 (although it will eventually change due to the 400-day limitation). We then modify it to a lower version, say 2.319.1.1, and attach our XSS payload. For example:  
2.319.1.1 <image src =q onerror=prompt(8)>

Now when an Administrator opens the _Available Plugin Manager_ page:

![ Image of XSS triggered on the local Jenkins Server available plugins page](https://www.aquasec.com/wp-content/uploads/2024/01/picture-14.png)

The XSS attack succeeds, thereby enabling the attacker to execute arbitrary JavaScript on the victim’s browser within the context of the Jenkins Server website.

This makes all Jenkins versions earlier than 2.319.2 exploitable at this time of writing.

### **From XSS to RCE**

Having established that the XSS attack is successful, we decided to test if we could escalate it to RCE on the Jenkins Server. At present, our custom JavaScript is running on the Jenkins admin’s browser, giving us the same privileges as the admin. This means we can perform any task that the admin is capable of, including running Groovy code on the Jenkins Server through the [Script Console API](https://www.jenkins.io/doc/book/managing/script-console/).

In the following steps, we will demonstrate how the attacker, by exploiting the vulnerability, can obtain a [reverse shell](https://www.aquasec.com/cloud-native-academy/cloud-attacks/reverse-shell-attack/) to their machine via the Groovy Script Console.

The initial payload that the attacker may insert into the Jenkins-Version attribute in the Manifest file is as follows:

![ Example of XSS payload of attacker](https://www.aquasec.com/wp-content/uploads/2024/01/picture-15.png)

In short, the payload instructs the browser to retrieve a JavaScript file from the attacker’s server https://attackers_machine/evil.js and execute its contents within the scope of the Jenkins Server.

Here’s an example of the JavaScript file (evil.js) that will be served to the victim by the attacker’s server:

![Example of Javascript file served by attacker to recieve reverse shell](https://www.aquasec.com/wp-content/uploads/2024/01/picture-16.png)

In the JavaScript code, we specified the attacker’s IP address and port for the [reverse shell payload](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#groovy) in Groovy.

Next, we combined all the necessary data and issued a POST request to the _/script_ endpoint to execute the Groovy code on the private Jenkins Server.

After the malicious _Groovy code_ is executed by the Jenkins Server:

![xample of attacker recieving reverse shell and executing command on the victim's Jenkins Server](https://www.aquasec.com/wp-content/uploads/2024/01/picture-17.png)

The attacker’s C2 receives the [reverse shell](https://www.aquasec.com/cloud-native-academy/cloud-attacks/reverse-shell-attack/) from the victim’s Jenkins Server!

Now the attacker is granted full control over the entire Jenkins infrastructure. This level of access enables the attacker to manipulate builds, inject harmful code into artifacts and execute additional malicious activities.

### **Bringing the malicious plugin to the front**

By default, Jenkins Server only displays the most frequently downloaded plugins in the main feed. 

The attacker can use certain techniques to bring the malicious plugin to the main page of the available plugin feed or increase the likelihood that it will be rendered on the _Available Plugin Manager_ page:

  1. Since the search function is based on any keywords found in the plugin description, an attacker can utilize this by uploading a plugin that contains all plugin names and popular keywords embedded in the description.  
To make it even more difficult to detect, attackers can embed a lot of plugin names and popular terms in an HTML tag such as the <a> tag, for example <a href=”long_text”> .</a>  
Since this tag is permitted, the plugin won’t appear suspicious. During our testing, we found that almost every search we conducted returned the malicious plugin.
  2. It’s possible to boost the download count of a specific plugin and increase its popularity by submitting requests from fake instances.

### **Attack steps summary**

**Step 1** | An attacker creates an initial innocent plugin and gains upload permissions.  
---|---  
**Step 2** | The attacker modifies the HPI file with the XSS payload inside the Jenkins-Version attribute.  
Step 3 | The attacker uploads the modified HPI to the public Jenkins artifact registry.  
**Step 4** | The _Update Center_ fetches the plugin and stores the payload in the JSON of available plugins.  
**Step 5** | The _Jenkins Server_ fetches the new JSON from the Jenkins Update Center.  
**Step 6** | An admin of a vulnerable Jenkins Server opens the Available Plugin Manager page.  
**Step 7** | The XSS payload of the attacker is executed, executing malicious commands on the Jenkins Server with the permissions of the admin via the /script endpoint.  
**Step 8** | The attacker compromises the Jenkins Server  
  
### **Disclosure timeline  
**

16 Jan 2023 | Aqua Research team reported the vulnerabilities to Jenkins security team.  
---|---  
16 Jan 2023 | Jenkins security team confirmed the vulnerabilities.  
15 Feb 2023**** | Jenkins has released a [fix](https://github.com/jenkins-infra/update-center2/releases/tag/update-center2-3.15)[ for update-center2](https://github.com/jenkins-infra/update-center2/releases/tag/update-center2-3.15) and patched the public Jenkins Update Center.  
8 Mar 2023 | Jenkins has released a fix for Jenkins Server and announced [Security Advisory](https://www.jenkins.io/security/advisory/2023-03-08/) CVE-2023-27898 and CVE-2023-27905.  
  
### **In Summary**

Several important lessons can be drawn from our research. 

Firstly, as opposed to Jenkins older than 400 days, which were immediately exploitable, we discovered that Jenkins Servers under 400 days old were vulnerable to these vulnerabilities but could not be exploited immediately. However, if these servers were not updated and remained out-of-date, they could be exploitable in the future. This underscores the importance of maintaining a regular update schedule for all components of the environment, which can help to prevent known and unknown vulnerabilities from being exploited.

Secondly, our research highlights the importance of defense-in-depth strategies for securing environments. It is critical to have multiple layers of protection in place to safeguard the environment and its components from vulnerabilities. By implementing different security measures, even if one component is compromised, the other layers of protection can mitigate the damage and prevent the attacker from escalating their attack.

### **Prevention with Aqua Platform**

We recommend a defense-in-depth approach, using multiple controls at key points to prevent security incidents.

[Scanning your SDLC environments](https://www.aquasec.com/cloud-native-academy/supply-chain-security/secure-software-development-lifecycle-ssdlc/) with a tool like [Aqua Trivy](https://www.aquasec.com/products/trivy/) can help ensure that your version of Jenkins is not vulnerable to known vulnerabilities.

We recommend implementing further controls to protect your environments in case any vulnerabilities were exploited in your environment. For instance, you can scan your workloads for suspicious and malicious behavior in runtime with open-source tools such as Tracee. If you use the [Aqua CNAPP](https://www.aquasec.com/cloud-native-academy/cnapp/what-is-cnapp/) we highly recommend using CNDR.

This solution is designed to empower security teams to detect and prevent cyberattacks at various stages of development using strong tools such as drift prevention, which prevents downloading and running malicious elements, and [Cloud Native Detection and Response (CNDR)](https://www.aquasec.com/use-cases/cndr-cloud-native-detection-and-reponse/), an[ eBPF](https://www.aquasec.com/cloud-native-academy/devsecops/ebpf-linux/)-based tool designed to detect malicious behavior in runtime.

**Published under:** [SECURITY RESEARCH](https://www.aquasec.com/category/research/)

**Tags:** [CI/CD](https://www.aquasec.com/tag/ci-cd/), [Security Threats](https://www.aquasec.com/tag/security-threats/)

[Ilay Goldman](https://www.aquasec.com/authors/ilay-goldman/)

Ilay Goldman is a Security Researcher at Aqua's research team, Team Nautilus. He specializes in uncovering and analyzing novel security threats and attack vectors in cloud native environments, as well as in supply chain security and open-source vulnerabilities. Before joining Aqua, he gained experience as a red team member. Ilay has also been an active public speaker, presenting his expertise at major cybersecurity events such as Black Hat and RSA.

[](https://www.linkedin.com/in/ilaygoldman/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

Yakir Kadkoda was the Director of Security Research at Aqua’s research team, Team Nautilus. 

[](https://www.linkedin.com/in/yakir-kadkoda?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BeZHGPSEWTw60pu3BUApmPA%3D%3D) [](https://twitter.com/YakirKad)

[](https://www.facebook.com/sharer/sharer.php?u=https://www.aquasec.com/blog/jenkins-server-vulnerabilities/) [](https://twitter.com/share?url=https://www.aquasec.com/blog/jenkins-server-vulnerabilities/&text=CorePlague%3A%20Critical%20Vulnerabilities%20in%20Jenkins%20Server%20Lead%20to%20RCE) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.aquasec.com/blog/jenkins-server-vulnerabilities/&title=CorePlague%3A%20Critical%20Vulnerabilities%20in%20Jenkins%20Server%20Lead%20to%20RCE)

Table of Contents

  * **The Research in a Nutshell**
  * **Improper Sanitation: The Jenkins Update Center**
  * **CVE-2023-27905**
  * **CVE-2023-27898**
  * **The Tiering** Mechanism
  * **From XSS to RCE**
  * **Bringing the malicious plugin to the front**
  * **Attack steps summary**
  * **In Summary**
  * **Prevention with Aqua Platform**

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
