---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-05_appsmith-patches-full-read-ssrf-vulnerabilities-reported-by-cloudsek.md
original_filename: 2022-10-05_appsmith-patches-full-read-ssrf-vulnerabilities-reported-by-cloudsek.md
title: Appsmith Patches Full-Read SSRF Vulnerabilities Reported by CloudSEK
category: documents
detected_topics:
- cloud-security
- ssrf
- api-security
- mobile-security
- command-injection
- path-traversal
tags:
- imported
- documents
- cloud-security
- ssrf
- api-security
- mobile-security
- command-injection
- path-traversal
language: en
raw_sha256: 796c70364e79f6ac84731a5e6fdb033b3de1cc013e27a4cb213bdf87e4934022
text_sha256: 314fcdc4b4a1dc42b636285fa6c8703f668d8d5e899df325a4b3417f0947c309
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# Appsmith Patches Full-Read SSRF Vulnerabilities Reported by CloudSEK

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-05_appsmith-patches-full-read-ssrf-vulnerabilities-reported-by-cloudsek.md
- Source Type: markdown
- Detected Topics: cloud-security, ssrf, api-security, mobile-security, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `796c70364e79f6ac84731a5e6fdb033b3de1cc013e27a4cb213bdf87e4934022`
- Text SHA256: `314fcdc4b4a1dc42b636285fa6c8703f668d8d5e899df325a4b3417f0947c309`


## Content

---
title: "Appsmith Patches Full-Read SSRF Vulnerabilities Reported by CloudSEK"
page_title: "Appsmith Patches Full-Read SSRF Vulnerabilities Reported by CloudSEK | CloudSEK"
url: "https://cloudsek.com/appsmith-patches-full-read-ssrf-vulnerabilities-reported-by-cloudsek/"
final_url: "https://www.cloudsek.com/blog/appsmith-patches-full-read-ssrf-vulnerabilities-reported-by-cloudsek"
authors: ["Sparsh Kulshrestha (@d0tdotslash)", "Shashank Bharthwal (@xscorp7)"]
programs: ["Appsmith"]
bugs: ["SSRF"]
publication_date: "2022-10-05"
added_date: "2022-10-06"
source: "pentester.land/writeups.json"
original_index: 2084
---

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6a0ec8ca3360db61383a435c_cross_icon_ticker%20\(1\).avif)

[**🚀** CloudSEK becomes first Indian origin cybersecurity company to receive investment from **US state** fund Read more](https://www.cloudsek.com/ancmt/cloudsek-becomes-first-indian-origin-cybersecurity-company-to-receive-investment-from-a-u-s-state-fund)

[🚀 CloudSEK Becomes First Indian Cybersecurity Firm to partner with The Private OfficeRead more](https://www.cloudsek.com/ancmt/cloudsek-becomes-first-active-indian-cybersecurity-firm-to-partner-with-seed-group-a-company-of-the-private-office-of-sheikh-saeed-bin-ahmed-al-maktoum)

[**🚀** CloudSEK has raised **$19M Series B1 Round** – Powering the Future of Predictive CybersecurityRead more](https://www.cloudsek.com/blog/cloudsek-raises-19-million-in-series-b1-funding-to-scale-predictive-cybersecurity-platform)

[![CloudSEK Logo](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/634fc9354ba9486197b82cef_CloudSEK%20Logo.svg)](/?r=0)

Products

[Nexus AIAI Command center & Cyber Risk Quantification](/nexus)[XVigilDigital Risk protection](/xvigil)[BeVigilAttack Surface monitoring](/bevigil-enterprise)[SVigilThird party Risk Monitoring](/svigil)[Threat IntelligenceCyber Threat Intel, IAVs & More](/threat-intelligence)[BeVigil CommunityApplication Scanner](https://bevigil.com/?Ref=cloudsek.com)[ExposureCheck if your organisation's data is in a data breach](https://exposure.cloudsek.com/?Ref=cloudsek.com)[AIVigilAI Attack Surface Monitoring](/aivigil)

Solutions

[Cyber Threats MonitoringSurface, Deep, and Dark Web Monitoring](/cyber-threats)[Deep and Dark Web MonitoringThreat Monitoring Across the Hidden Web](/cyber-threats/dark-web-monitoring)[Brand Threats MonitoringProactive Brand Protection](/brand-monitor)[Infrastructure MonitoringCatch Risks Before Attacks](/bevigil-enterprise)[Partner Secret ScanningAPI/secret Exposure Detection](https://bevigil.com/bevigil-secrets-scanning-partner-program)[BeVigil Jenkins CIBeVigil-CI secures your mobile app builds](https://plugins.jenkins.io/bevigil-ci/)[BeVigil OSINT CLIUnified CLI/Python for BeVigil OSINT](https://github.com/Bevigil/BeVigil-OSINT-CLI)[![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/65a39c6759c55f9a7f741e12_link.webp)BeVigil Asset ExplorerThreat Monitoring Across the Hidden Web](https://bevigil.com/osint-api)

Resources

#### Resources

[BlogStay updated with the latest cybersecurity news, insights, and industry trends](/blog)[Threat IntelligenceGet up and running on new threat reports and techniques](/threatintelligence)[Knowledge BaseBasics of Cybersecurity and see more definitions](/knowledgebase)[Whitepapers & ReportsThe content team broke their backs making these reports](/whitepapers-reports)[Customer storiesLearn how our customers are making big changes. You have got good company!](/customers)[CloudSEK AcademyBe CloudSEK certified!](/cloudsek-academy)

#### Company

[IntegrationsWe are more connected than you know. Explore all Integrations](/integrations)[Partners100s of partners and one Shared goal; Secure future for all us](/partners)[About usLearn about our story and our mission statement](/about-us)[Life at CloudSEKA sneak peek at the awesome life at CloudSEK](/work-life)[Careers We're hiring!We are in love with undeniable talent. Join our team!](/openings)[EventsWe're hiring!Explore webinars, panels, and meetups powered by CloudSEK](/events)[LegalAll the boring but necessary legalese that legal made us add.](/privacy-policy)[ComplianceProven compliance with top security benchmarks.](/compliance)

#### Latest Whitepaper

[![CloudSEK: Global Threat Landscape Report 2025](https://cdn.prod.website-files.com/635e632477408d12d1811a64/6a0eb74496292c29c9bac8d2_Global_threat_landscape%20\(1\).png)Adversary Intelligence![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327cbe1af8775b77ba77_calendar_today.svg)24 Mar 26CloudSEK: Global Threat Landscape Report 2025](/whitepapers-reports/cloudsek-global-threat-landscape-report-2025)

Free Tools

[URL AnalyserScan for malicious links and phishing threats](/cyber-threats)[Deepfake AnalyserSpot manipulated videos and deepfake scams](https://community.cloudsek.com/)[ThreatLensA live feed of scams, phishing, and brand abuse](/brand-monitor)[Mobile App AnalyserDetect security flaws in mobile apps](https://bevigil.com/?Ref=cloudsek.com)[Asset ExplorerGain insights on digital assets and subdomains](https://bevigil.com/?Ref=cloudsek.com)[Data Exposure CheckerSee if your organization's data is on the Dark Web](https://exposure.cloudsek.com/?Ref=cloudsek.com)[![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/65a39c6759c55f9a7f741e12_link.webp)BeVigil Asset ExplorerThreat Monitoring Across the Hidden Web](https://bevigil.com/osint-api)

Log in[Schedule a Demo](/request-a-demo)

[Schedule a Demo](/request-a-demo)

[![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/68e38dafc403862b9dcf69c9_back%20arrow.svg)Back](/blog)

Vulnerability Intelligence

# Appsmith Patches Full-Read SSRF Vulnerabilities Reported by CloudSEK

Appsmith Patches Full-Read SSRF Vulnerabilities Reported by CloudSEK

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327cbe1af8775b77ba77_calendar_today.svg)

October 4, 2022

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327b64c4f7469e855e46_min.svg)

min

![](https://cdn.prod.website-files.com/635e632477408d12d1811a64/64062bbd7f82fa53cd0afdce_Appsmith-Patches-Full-Read-SSRF-Vulnerabilities.png)

Table of Content

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6862598a685f6b3011d16d51_keyboard_arrow_down.svg)

Example H2

Example H2

Subscribe to CloudSEK Resources

Get the latest industry news, threats and resources.

Subscribe

Authors : **Sparsh Kulshrestha** and **Shashank Bharthwal**  
Editor : Deepanjli Paulraj

## Executive Summary

**THREAT** | **IMPACT** | **MITIGATION**  
---|---|---  
CloudSEK ASM discovered post-authentication full read SSRF (Server-side request forgery) vulnerabilities in [Appsmith’s](https://www.appsmith.com/) REST Client ([CVE-2022-38298](https://nvd.nist.gov/vuln/detail/CVE-2022-38298)) and Elasticsearch ([CVE-2022-38299](https://nvd.nist.gov/vuln/detail/CVE-2022-38299)). |  The SSRF vulnerability can be exploited to access AWS/GCP metadata services and obtain temporary security credentials of the Appsmith cloud environment. | 

  * Disallow redirects in the HTTP Client of REST Import service.
  * Update to [versions 1.7.12 and above](https://github.com/appsmithorg/appsmith/releases).

  
  
## Introduction

In August 2022 [CloudSEK ASM](https://cloudsek.com/), which monitors our customers’ attack surfaces, discovered several internet exposed instances of Appsmith. Given that the instances were externally exposed, CloudSEK security researchers explored them for possible pre and post authentication vulnerabilities.

Since Appsmith does not have signup restrictions in the default installation, we focused on its post-auth functionalities, where we discovered Server Side Request Forgery (SSRF) vulnerabilities in its REST API plugin ([CVE-2022-38298](https://nvd.nist.gov/vuln/detail/CVE-2022-38298)) and Elasticsearch ([CVE-2022-38299](https://nvd.nist.gov/vuln/detail/CVE-2022-38299)), respectively.

SSRF vulnerabilities can be exploited to access the internal metadata of AWS/GCP. Since Appsmith offers a cloud version of their software hosted on AWS, SSRF vulnerabilities can have a high impact.

### What is Appsmith

[Appsmith](http://www.appsmith.com) is an open-source low-code tool that helps developers build dashboards and admin panels very quickly. It’s a platform that helps businesses build any custom internal application within hours.

### **How does Appsmith work?**

Appsmith dashboards and panels can be set up in 4 steps:

  * **Connect Datasource** : Integrate with a data source such as a database or an API. Appsmith has plug-and-play support for many databases and RESTful API interface to connect with most tools.
  * **Build UI** : Use customizable built-in widgets to build an app layout.
  * **Access Data** : Connect UI to the data source by writing queries and binding the data to widgets.
  * **Collaborate, Deploy, and Share** : It supports version control with Git, to track changes, create rollbacks, and to collaborate using git branches. Deploy the app and share it with other users.

### **SSRF Vulnerability in Appsmith’s REST Client (CVSS:3.0 Score: 8.8)**

One of Appsmith’s post-authentication functionalities allows users to connect to data sources using REST APIs. Appsmith’s REST Client can be used to invoke a REST Service API to create and execute queries. It can handle HTTP requests ranging from GET, POST, PUT, and PATCH, and users can also specify headers, if required, for authentication.

![Appsmith REST API](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a968cb2b07007_word-image-20980-1.png)Appsmith REST API

On replacing the API URL with a Burp Collaborator’s payload, we received an HTTP pingback immediately. However, when we tried to access the internal AWS metadata, we received a “Host not allowed” error.

![Error while accessing AWS metadata](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a967f06b07003_word-image-20980-2.png)Error while accessing AWS metadata

Since Appsmith is an open-source tool, we reviewed the code for this functionality and found that there is blacklist-based prevention that restricts users from accessing AWS metadata.

`private static final Set<String> DISALLOWED_HOSTS = Set.of(  
"169.254.169.254",  
"metadata.google.internal"  
);`  
---  
  
_List of Disallowed Domains_

`final String host = uri.getHost();  
if (StringUtils.isEmpty(host)  
|| DISALLOWED_HOSTS.contains(host)  
|| DISALLOWED_HOSTS.contains(InetAddress.getByName(host).getHostAddress())) {  
errorResult.setBody(AppsmithPluginError.PLUGIN_EXECUTE_ARGUMENT_ERROR.getMessage("Host not allowed."));  
errorResult.setRequest(actionExecutionRequest);  
return Mono.just(errorResult);  
}`  
---  
  
_Condition to validate hostname_

In an attempt to bypass the SSRF blacklist protection, we implemented a redirection server that redirects the decoy request to the blacklisted server.

![](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead16c42a96ee6eb07011_word-image-20980-3.png)

So, we set up a PHP redirect server, on our VPS, that redirects incoming requests to the AWS internal metadata endpoint. In this way, we were able to exploit this SSRF vulnerability. The following redirect.php file was hosted on our VPS:

`<?php  
$server = $_GET["server"];  
if($server == "gcp") {  
header("Location: http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/");  
}  
elseif($server == "aws") {  
header("Location: http://169.254.169.254/latest/meta-data/");  
}  
?>`  
---  
  
_Redirect.php file content_

Then we made a request to the above file from the Appsmith REST API and in response, we received the metadata from the AWS/GCP cloud.

![AWS security credentials of self-hosted Appsmith Cloud](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a969cdcb07008_word-image-20980-4.png)AWS security credentials of self-hosted Appsmith Cloud

![GCP metadata were fetched from the GCP compute engine](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a964d28b07004_word-image-20980-5.png)GCP metadata were fetched from the GCP compute engine

### **SSRF Vulnerability in Appsmith’s Elasticsearch (CVSS:3.0 Score: 8.2)**

One of Appsmith’s post-authentication functionalities allows users to connect to Elasticsearch databases as data sources.

![Adding an Elasticsearch database as a data source](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a9662e1b07006_word-image-20980-6.png)Adding an Elasticsearch database as a data source

Once the Elasticsearch database has been connected, select the query method and enter the path. We added the following path: _/latest/meta-data/iam/security-credentials/._ Leave the Body blank.

![](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a967d2cb07005_word-image-20980-7.png)

![Adding the path](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a960eb9b07002_word-image-20980-8.png)Adding the path

When this query is run, it returns the temporary security credentials for your AWS role.

![AWS security credentials](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a9671d4b0700b_word-image-20946-9-2.png)AWS security credentials

## **Impact**

While a post-authentication SSRF is not new, it can have significant impact since Appsmith offers a cloud version of their software hosted on AWS. Also, Appsmith does not have a signup restriction in the default installation. So if an Appsmith instance is exposed to the internet, anyone can signup and have access to the vulnerable functionality that has this SSRF vulnerability.

In this case, the SSRF vulnerabilities can be exploited to the AWS metadata IP address and obtain temporary security credentials to the cloud environment of self-hosted Appsmith.

This can have large-scale impact, given that over a 1000 Appsmith instances are exposed on the internet:

![](https://cdn.prod.website-files.com/635e632477408d12d1811a64/63bead15c42a96773eb0700c_word-image-20946-10-2.png)

## **Mitigation**

  * Disallow redirects in the HTTP Client of REST Import service.
  * Update to [versions 1.7.12 and above](https://github.com/appsmithorg/appsmith/releases).

## Responsible Disclosure

CloudSEK submitted this vulnerability to Appsmith via their well-defined vulnerability disclosure process. Subsequently, the Appsmith team fixed this issue in their next release. Appsmith versions 1.7.12 and above do not have this vulnerability.

### Timeline

Timeline for this disclosure process can be found below:

  * 05 Aug 2022: Disclosure of first SSRF to Appsmith
  * 05 Aug 2022: Initial response from Appsmith with acknowledgement for the vulnerability
  * 06 Aug 2022: Disclosure of second SSRF to Appsmith
  * 08 Aug 2022: Response from Appsmith with acknowledgement for the second vulnerability
  * 09 Aug 2022: Appsmith releases patch for both the vulnerabilities.
  * 10 Aug 2022: We filed for the CVE
  * 13 Sep 2022: CVE ID assigned by cve.org

## References

  * **#**[Traffic Light Protocol – Wikipedia](https://en.wikipedia.org/wiki/Traffic_Light_Protocol)
  * [Appsmith Documentation](https://docs.appsmith.com/)

![]()

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/686ba3b48c1afeb220817665_Facebook.svg)![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/686ba3b4e328c53c4143a1cf_twitter.svg)

No items found.

Subscribe to CloudSEK Resources

Get the latest industry news, threats and resources.

Subscribe

[](http://www.linkedin.com/shareArticle?mini=true&url=&title=&summary=&source= "Share on LinkedIn")

[](https://twitter.com/intent/tweet? "Tweet")

## Related Blogs

[![](https://cdn.prod.website-files.com/635e632477408d12d1811a64/68676b6013437ba10e1b5ed0_cisco%20update%201.jpg)This is some text inside of a div block.Vulnerability Intelligence![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327cbe1af8775b77ba77_calendar_today.svg)July 4, 2025![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327b64c4f7469e855e46_min.svg)3minCisco Unified Communications Manager CVSS 10 Vulnerability: 1K+ Assets Exposed to the InternetRead more![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6862452151f54f6dc0a74688_arrow.svg)](/blog/cisco-unified-communications-manager-cvss-10-vulnerability-1k-assets-exposed-to-the-internet)

[![](https://cdn.prod.website-files.com/635e632477408d12d1811a64/6839696827062971b693b440_Azure%20AD%20Users%20Exposed%20unsecured%20API.png)This is some text inside of a div block.Vulnerability Intelligence![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327cbe1af8775b77ba77_calendar_today.svg)May 30, 2025![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327b64c4f7469e855e46_min.svg)4min50,000+ Azure AD Users Exposed via Unsecured API: BeVigil Uncovers Critical FlawRead more![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6862452151f54f6dc0a74688_arrow.svg)](/blog/50-000-azure-ad-users-exposed-via-unsecured-api-bevigil-uncovers-critical-flaw)

[![](https://cdn.prod.website-files.com/635e632477408d12d1811a64/68302546bc66be5a2e5a652d_LFI%20vulnerability.png)This is some text inside of a div block.Vulnerability Intelligence![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327cbe1af8775b77ba77_calendar_today.svg)May 23, 2025![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/685d327b64c4f7469e855e46_min.svg)5minExposed and Exploitable: How an LFI Flaw Left a Travel Giant’s Server Files Open to HackersRead more![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6862452151f54f6dc0a74688_arrow.svg)](/blog/exposed-and-exploitable-how-an-lfi-flaw-left-a-travel-giants-server-files-open-to-hackers)

1

...

[](?78dcd286_page=2)

1 / 9

## Predict Cyber Threats against your organization

[Schedule a Demo](/request-a-demo)

Join our newsletter

We’ll send you a nice letter once per week. No spam.

![Untitled UI logotext](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/634fc9354ba9486197b82cef_CloudSEK%20Logo.svg)![Logo](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/63ccca15993f00c5bb4b42a7_untitled-ui-logo.webp)

Product

XVigilBeVigil[SVigilNew](/svigil)TutorialsPricingReleases

Company

About usCareersPressNewsMedia kitContact

Resources

BlogNewsletterEventsHelp centreTutorialsSupport

Use Cases

StartupsEnter***REDACTED-SUSPECT-TOKEN***Social

Twitte***REDACTED-SUSPECT-TOKEN***© 2077 Untitled UI

PrivacyGDPRDisclosure of Vulnerability

Products

[Nexus AI](/nexus)[XVigil](/xvigil)[BeVigil](/bevigil-enterprise)[SVigil](/svigil)[Threat Intelligence](/threat-intelligence)[CloudSEK Exposure](https://exposure.cloudsek.com/?ref=footer)[AIVigil](/aivigil)

Mobile App

[![Google Play button to download App
](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/65a397910cdede4ab2583442_en_badge_web_generic.png)](https://play.google.com/store/apps/details?id=com.cloudsek.bevigil&hl=cloudsekfooter&gl=US&pli=1)

Solutions

[Cyber Threats Monitoring](/cyber-threats)[Dark Web Monitoring](/cyber-threats/dark-web-monitoring)[Brand Threat Monitoring](/brand-monitor)[Infra Threat Monitoring](/infrastructure-monitor)[Partners Secret Scanning ](https://bevigil.com/bevigil-secrets-scanning-partner-program/?Ref=Footer)[BeVigil Jenkins CI](https://plugins.jenkins.io/bevigil-ci/?Ref=Footer)[BeVigil OSINT CLI](https://github.com/Bevigil/BeVigil-OSINT-CLI/?Ref=Footer)[BeVigil Asset Explorer](https://bevigil.com/osint-api/?Ref=footer)[Takedowns](/takedowns)

Resources

[Blogs and Articles](/blog)[Threat Intelligence](/threatintelligence)[Whitepapers and Reports](/whitepapers-reports)[Knowledge Base](/knowledgebase)[Integrations](/integrations)

Community

[Discord Community](https://discord.gg/h9hgFQC3qz)[Student Challenge](/student-challenge)

Company

[About us](/about-us)[Customers](/customers)[Partners](/partners)[Referral Program](/referral-program)[Life at CloudSEK](/work-life)[Secure Sips](https://www.cloudsek.com/work-life#securesips)[Careers](/openings)[Announcements](/announcements)[Press](/press)[Contact Us](/contact)

![CloudSEK Logo](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/634fc9354ba9486197b82cef_CloudSEK%20Logo.svg)

[](https://www.youtube.com/channel/UCuueHDbi46tSFrULlCTQakA)[](https://twitter.com/cloudsek)[![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/65a3899f4d2aa04c79ea33d0_instagram.webp)](https://instagram.com/cloudsek)[![Linkedin Icon
](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/65a6d0069161d4f7729cb2e4_linkedin%20\(1\).webp)](https://www.linkedin.com/company/cloudsek/)[](https://facebook.com/cloudsek)

At CloudSEK, we combine the power of Cyber Intelligence, Brand Monitoring, Attack Surface Monitoring, Infrastructure Monitoring and Supply Chain Intelligence to give context to our customers’ digital risks.

[GDPR Policy](/gdpr)[Privacy](/privacy-policy)[Vulnerability Disclosure](/security/vulnerability-disclosure)[DPA](/dpa)[Cookies Policy](/cookies-policy)[Sitemap](/sitemap)[LLM Info](https://www.cloudsek.com/llm-info)[EULA](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6995c72aebe76c31132b3915_End%20User%20License%20Agreement_CloudSEK%20Platform_2026.pdf)

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/68307354bdc768aff0580c37_ISO%209001.webp)

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6830736c9dc286aea76b38d8_iso-27001%202.webp)

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/68307377f9be14d54c2dbc46_SOC2.webp)

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/6830737b0a686269dd7a7f1a_Ggpr.webp)

![](https://cdn.prod.website-files.com/634fc5026f66af518e897c77/699c45da36a669af712d692f_IOS%2042001%20logo.png)
