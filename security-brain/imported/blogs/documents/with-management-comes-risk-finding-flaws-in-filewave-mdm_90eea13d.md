---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-25_with-management-comes-risk-finding-flaws-in-filewave-mdm.md
original_filename: 2022-07-25_with-management-comes-risk-finding-flaws-in-filewave-mdm.md
title: 'With Management Comes Risk: Finding Flaws in FileWave MDM'
category: documents
detected_topics:
- mobile-security
- supply-chain
- sso
- access-control
- ssrf
- xss
tags:
- imported
- documents
- mobile-security
- supply-chain
- sso
- access-control
- ssrf
- xss
language: en
raw_sha256: 90eea13d1f3ef5c79c35ff7ecdff117acf6f6b008eb28de9b3bb6e9bf39521b0
text_sha256: ed504c0f83f3d2d0afa831c354313c702477f6aa54fb243c52aec8cc7ba38b79
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# With Management Comes Risk: Finding Flaws in FileWave MDM

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-25_with-management-comes-risk-finding-flaws-in-filewave-mdm.md
- Source Type: markdown
- Detected Topics: mobile-security, supply-chain, sso, access-control, ssrf, xss
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `90eea13d1f3ef5c79c35ff7ecdff117acf6f6b008eb28de9b3bb6e9bf39521b0`
- Text SHA256: `ed504c0f83f3d2d0afa831c354313c702477f6aa54fb243c52aec8cc7ba38b79`


## Content

---
title: "With Management Comes Risk: Finding Flaws in FileWave MDM"
page_title: "Uncovering FileWave Mobile Device Management (MDM) Vulnerabilities | Claroty"
url: "https://claroty.com/team82/blog/with-management-comes-risk-finding-flaws-in-filewave-mdm"
final_url: "https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm"
authors: ["Claroty's Team82 (@Claroty)"]
programs: ["Filewave"]
bugs: ["Authentication bypass", "Hardcoded credentials", "Information disclosure"]
publication_date: "2022-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2405
---

[ ![Team82 Logo](https://claroty.com/build/assets/team82-logo-white-BGiCQ9zb.svg) ](/team82)

  * [Research](/team82/research)
  * [Vulnerability Dashboard](/team82/disclosure-dashboard)
  * [Talks](/team82/talks)
  * [Tools](/team82/#tools)
  * [About](/team82/#about)

[ ![Claroty](https://claroty.com/build/assets/logo-solid-white-DcRiqKcD.svg) ](/)

[ Return to Team82 Research ](/team82/research)

# With Management Comes Risk: Finding Flaws in FileWave MDM

Noam Moshe 

/ July 25th, 2022

![FileWave MDM \(mobile device management\) Vulnerabilities Uncovered](/img/asset/YXNzZXRzL2ltYWdlOC5wbmc/image8.png?fm=webp&fit=crop&w=800&h=450&s=7d7cb458030a8e798e0d68ad3bef9dda)

Executive Summary

  * Team82 has uncovered and disclosed two critical vulnerabilities, CVE-2022-34907 and CVE-2022-34906, in FileWave’s mobile device management (MDM) system.

  * The vulnerabilities are remotely exploitable and enable an attacker to bypass authentication mechanisms and gain full control over the MDM platform and its managed devices. 

  * [CVE-2022-34907](https://claroty.com/team82/disclosure-dashboard/cve-2022-34907), an authentication bypass flaw exists in FileWave MDM before version 14.6.3 and 14.7.x, prior to 14.7.2. This vulnerability is similar in nature to the vulnerability that was recently identified in [F5 BIG-IP WAF](https://support.f5.com/csp/article/K23605346).

  * [CVE-2022-34906](https://claroty.com/team82/disclosure-dashboard/cve-2022-34906), a hard-coded cryptographic key, exists in FileWave MDM prior to version 14.6.3 and 14.7.x, prior to 14.7.2.

  * During our research, we found thousands of vulnerable internet-facing FileWave servers in numerous industries, including government agencies, education, and large enterprises.

  * [FileWave has addressed these vulnerabilities in a recent update](https://kb.filewave.com/pages/viewpage.action?pageId=55544244), and users are urged to apply the update. FileWave has also written a blog about its [resolution of these vulnerabilities](https://www.filewave.com/software-upgrade-to-resolve-critical-security-vulnerabilities/).

  * Team82 wishes to acknowledge and thank FileWave for its cooperation and coordination throughout this disclosure. These vulnerabilities were addressed in a prompt, complete fashion, users were notified, and the vast majority were verified as up to date. 

Below is a demonstration of Team82’s proof-of-concept exploit in action—described in the last section of this report. Our attack compromises the Filewave MDM, then infects each managed device with a phony ransomware sample:

>

## What is FileWave MDM?

FileWave MDM is a multi-platform mobile device management solution that allows IT administrators to manage, monitor, and view all of an organization’s devices. Currently, FileWave MDM supports a wide range of devices, from iOS and Android smartphones, MacOS and Windows tablets, laptops and workstations, and smart devices such as televisions. 

![FileWave MDM](/img/asset/YXNzZXRzL3Q4Mi1maWxld2F2ZS1ibG9nLWdyYXBoaWMtMDEucG5n/t82-filewave-blog-graphic-01.png?fm=webp&fit=crop&s=a4d206449cc513db74a42c7b3e183162) FileWave MDM manages mobile devices actively used across industries. 

Through FIleWave MDM, IT administrators can view and manage device configurations, locations, security settings, and other device data. Admins may use the MDM platform to push mandatory software and updates to devices, change device settings, lock, and, when necessary, remotely wipe devices. In order to do so, all managed devices report to the main server at set intervals, and in return, the server can issue commands to the device via file packages, software, and more.

In recent years, there have been attacks against endpoint management products, including one of the more high-profile [attacks targeting the Kaseya VSA](https://helpdesk.kaseya.com/hc/en-gb/articles/4403584098961-Incident-Overview-Technical-Details). Kaseya VSA is used by thousands of service providers for IT management, and it was compromised by the REvil ransomware gang and used to distribute ransomware on endpoints worldwide. More than 1,000 companies suffered substantial downtime because of this attack. 

REvil was able to exploit a zero-day vulnerability in the Kaseya VSA platform to bypass authentication and achieve arbitrary command execution. This allowed the attackers to leverage the standard VSA product functionality to deploy ransomware to managed endpoints. In response, the company shut down its VSA cloud and SaaS servers and issued a security advisory to customers, including those with on-premises deployments of VSA.

This incident shows that this attack vector still applies to management products and we must be vigilant and always on the lookout. 

One of the positive outcomes of Team82’s research was the quick response time by Filewave. Once we notified Filewave they quickly developed and deployed fixes to these issues and actively reached out to their customers. This shows the positive advancement of the response time to security issues by vendors which reduce the attack surface considerably.

## Authentication Flaws Discovered in FileWave MDM

An attacker who is able to compromise the MDM would be in a powerful position to control all managed devices, allowing the attacker to exfiltrate sensitive data such as a device’s serial number, the user’s email address and full name, address, geo-location coordinates, IP address, device PIN codes, and much more. Furthermore, attackers could abuse legitimate MDM capabilities to install malicious packages or executables, and even gain access to the device directly through remote control protocols.

![FileWave server managed devices](/img/asset/YXNzZXRzL2ltYWdlMTUucG5n/image15.png?fm=webp&fit=crop&s=f9a25aca0ec7077937559ef2dc8e92ff) Example of data Team82 managed to extract from a FileWave server, containing more than 10,000 managed devices.

During our research, we were able to identify a critical flaw in the authentication process of the FileWave MDM product suite, allowing us to create an exploit that bypasses authentication requirements in the platform and achieve super_user access, (the platform’s most privileged user).

By exploiting this authentication bypass vulnerability, we were able to take full control over any internet-connected MDM instance. In our research, we discovered more than 1,100 such instances, each containing an unrestricted number of managed devices. 

This exploit, if used maliciously, could allow remote attackers to easily attack and infect all internet-accessible instances managed by the FileWave MDM, below, allowing attackers to control all managed devices, gaining access to users’ personal home networks, organizations’ internal networks, and much more.

![Filewave Managed Devices](/img/asset/YXNzZXRzL2ltYWdlMTIucG5n/image12.png?fm=webp&fit=crop&s=b6edc8f498e01d123377368bfe58b061) An attacker capable of compromising a FileWave MDM server can exploit all managed devices. 

To fully understand the range and relevance of this vulnerability, we had to first know how many organizations actually use this product. In order to do so, we’ve used a few different methods which netted us with more than 1,100 different instances of FileWave MDM, each vulnerable to the vulnerabilities described below. Between those exposed services, we’ve discovered organizations from many different fields, including corporations, schools and educational institutions, government agencies and small-to-medium businesses.

## FileWave MDM Technical Details

#### Looking into CVE-2022-34907: Authentication Bypass

An important FileWave MDM component is the MDM web server, written in Python using the Django framework. It exposes TCP port 20443 and 20445

The web server handles not only client devices but also the admin’s GUI application. It retrieves device information from clients, handles device enrollment, and supplies commands to devices. For the admin, the web server returns data about client devices using different query methods, and allows the administrator to control all managed devices, including the ability to change a device configuration remotely, install packages on the device, and remotely control it.

Since this service should be accessible to mobile devices at all times, it is usually exposed to the internet, and handles both clients’ and admins’ requests. Its connectivity makes it a primary target in our research on this platform.

We discovered that this server handles different client types, each authenticating differently. Firstly, there are the mobile devices. By default devices can start the enrollment process and interact with the server without requiring any form of user-based authentication (although the option to require credentials in the enrollment process does exist in FileWave MDM). All enrolled devices are first placed in the “quarantine” group, a logical group of devices that are not part of the organization. This means that all routes that involve device enrollment do not require authentication, however since these routes do not allow us to exfiltrate sensitive data, or to take control over devices, this vector was less explored by us.

![FileWave MDM enrolment routes](/img/asset/YXNzZXRzL2ltYWdlMTEucG5n/image11.png?fm=webp&fit=crop&s=2a7f62d0f50133ba33a7f13b7aa3995c) FileWave MDM enrollment routes. Through this web server, mobile devices enroll to this specific instance and allow the IT administrators to manage their device.

Then, there is system administrator authentication. This method takes a username/password combination, and returns a valid token. Using this token, the IT admin could retrieve data about devices, change device configurations, and much more. In most cases, this token is checked correctly, and allows only valid users to access routes that require authentication. 

![FileWave MDM admin interface](/img/asset/YXNzZXRzL2ltYWdlMi5wbmc/image2.png?fm=webp&fit=crop&s=c1409267e594838202483b3881cd9b4e) The FileWave MDM admin interface. Through this interface, IT administrators can authenticate to the MDM platform.

Lastly, we researched the backend services running on the MDM server, which performs another type of authentication within this service. Except for the MDM web server, there are a few extra services that exist in the FileWave MDM ecosystem. One service in particular, the scheduler service, also written in Python, caught our attention. Its purpose is to schedule and execute specific tasks that the MDM platform needs to perform, and to call the corresponding callback whenever the tasks are completed.

As part of the business logic of the system, the web server uses the scheduler in many cases, and in return, the scheduler informs the web server whenever a task is finished. In order to do so, the scheduler calls some specific web routes in the web server, routes that are accessible only to authenticated and authorized users in the system. However, the scheduler does not know the administrator’s account details, and instead uses a hardcoded shared secret in order to authenticate to the web server. This shared secret does not change between each installation of FileWave MDM, nor between different versions of the system.

![SCHEDULER_SECRET](/img/asset/YXNzZXRzL2ltYWdlMS5wbmc/image1.png?fm=webp&fit=crop&s=ffbdf66107a9c8533a2b301dc70cfbfa) The SCHEDULER_SECRET variable is used by both the scheduler service and web server in order to verify and authenticate the scheduler. This is configured inside this file: /usr/local/filewave/django/filewave/settings_common.py.

In FileWave MDM platform, each route that requires valid authentication must inherit the FWAuthMixin class defined in /usr/local/filewave/django/fwauth/utillity.py (or any class that inherits this class). This check is performed inside the test_func function, where if this function returns True the request will be fulfilled, and if this function returns False, a 401 Unauthorized will be returned. When we looked into this function we found the code, below, (some code was redacted because it was irrelevant):

![FileWave MDM test_function](/img/asset/YXNzZXRzL2ltYWdlNy5wbmc/image7.png?fm=webp&fit=crop&s=f40bf6d93097651fe71c54b895e3a63a) The code of the test_function function that decides whether a user is authenticated.

As we can see, this function takes the Authorization header from the HTTP request, and compares it to the scheduler secret (after being base64 decoded). If they match, the request is given the permissions of the superuser account, which is the system’s administrator account. This means that if we know the shared secret and supply it in the request, we do not need to supply a valid user’s token or know the user’s username and password. Instead we will be granted access to the system using the superuser’s permissions (which are the highest permissions available).

![vulnerable FileWave MDM server](/img/asset/YXNzZXRzL2ltYWdlNi5wbmc/image6.png?fm=webp&fit=crop&s=d6004edf3b0b7fbe803e27d7a7acd080) A request to a vulnerable FileWave MDM server, passing the SCHEDULER_SECRET in its HTTP Authorization header, and therefore the server treats the request as if it was made by the scheduler service.

This vulnerability exists in FileWave up to version 13.1.3. However, when we tested this vulnerability against newer versions of the system, we learned it did not work. Something changed making the vulnerability above irrelevant in newer versions, so we decided to look into what that was in newer versions and find a bypass to this new security mechanism.

As it turns out, FileWave changed this logic inside the FWAuthMixin class, instead only accepting valid users’ tokens.

![test_func 13.1.3](/img/asset/YXNzZXRzL2ltYWdlOS5wbmc/image9.png?fm=webp&fit=crop&s=5d4ae79c6927bc142303e1742036e5fa) The code to the test_func function in versions newer than 13.1.3. We can see that the server no longer compares the authorization header to the scheduler secret.

This change had us stumped for a second, thinking our exploit is no longer viable. However, when we kept searching for new code, we discovered that FileWave added a new middleware (code which runs before requests are handled). This middleware, aptly named AppTokenMiddleware (and defined in /usr/local/filewave/django/fwauth/middleware.py) performs a similar action to the previous one used inside the older version of test_func function.

![middleware function code](/img/asset/YXNzZXRzL2ltYWdlMy5wbmc/image3.png?fm=webp&fit=crop&s=09a404b0e232c721cd9f06c4511ec672) The new middleware function code.

As we can see, this code looks really similar to the old code, comparing once again the Authorization Header to the scheduler secret. However, this time a new check is introduced, comparing request.gethost() to localhost. If we pass this check, we will once again be granted the permissions of the superuser. When we searched for what get_host returns, we reached this [documentation from Django](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.get_host):

![FileWave MDM Methods](/img/asset/YXNzZXRzL2ltYWdlNS5wbmc/image5.png?fm=webp&fit=crop&s=5c04f2c4ca83a9e752d92f725c813dc9)

As we can see, this value also comes from headers users supply, namely from the Host HTTP header. This means that because we supply this value, we can simply supply localhost as our value, thus passing this new check and gaining the super_user permissions.

![FileWave MDM Host header](/img/asset/YXNzZXRzL2ltYWdlMTAucG5n/image10.png?fm=webp&fit=crop&s=00e103bfaf0396ca7097d4b15ea18300) We can see that in this request in newer versions of FileWave MDM, the Host header is changed to bypass the new check and be localhost, thus passing the check and gaining the privileges of super_user.

Using this vulnerability, in either variety described above, we were able to gain highest privileges in all versions of the FileWave MDM. This allows us to gain the ability to attack and control every instance exposed to the internet. This enables us to control all of the servers’ managed devices, exfiltrate all sensitive data being held by the devices, including usernames, email addresses, IP addresses, geo-location etc, and install malicious software on managed devices.

## Proof-of-Concept: FileWave MDM Web Server Exploitation

In order to showcase this vulnerability and the severity and potential harm it can cause, we created a standard FileWave setup, and enrolled 6 devices of our own. Then, using this vulnerability, we exploited the MDM web server, which allowed us to leak data about all of the devices managed by this MDM server. 

Lastly, using regular MDM functionality which allows IT administrators to install packages and software on managed devices, we installed malicious packages on each controlled device, popping a fake ransomware virus on each of those managed devices. Doing so, we demonstrated how a potential attacker can leverage Filewave’s capabilities in order to take control over different managed devices.

We started our testbed with multiple devices connected to the Filewave server.

![Devices](/img/asset/YXNzZXRzL2ltYWdlMTMucG5n/image13.png?fm=webp&fit=crop&s=d2a74fd700ac651f56af84849b3aacc2)

Then, we ran our exploit in order to bypass authentication on the MDM server and gain administrative access to it. Using this access, we exfiltrated information about the managed devices, including their operation system, ecosystem, settings, and much more.

![Attacking FileWave MDM](/img/asset/YXNzZXRzL2ltYWdlMTQucG5n/image14.png?fm=webp&fit=crop&s=7b5fc9ffe8c959eb533069bdabcf793a)

Finally, We pushed a malicious package to all of the managed devices, which resulted in us being able to execute remote code on all devices. We used it to install fake ransomware on each device.

![FileWave MDM \(mobile device management\) Vulnerabilities Uncovered](/img/asset/YXNzZXRzL2ltYWdlOC5wbmc/image8.png?fm=webp&fit=crop&s=347073d37f83e51348832b00a7243db2)

### Acknowledgement

Team82 would like to thank Filewave for its coordination with us in working through this disclosure, and for its swift response in confirming our findings and swiftly patching these vulnerabilities. Filewave has addressed these issues in a [recent update, v14.7.2](https://fwkb.atlassian.net/wiki/spaces/DOW/pages/2556163/FileWave+Version+14.7.2?pageId=55544244), and worked with their customers to patch or update affected systems.

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm) [ __ Twitter ](https://twitter.com/intent/post?text=With Management Comes Risk: Finding Flaws in FileWave MDM&url=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm) [ __ ](mailto:?subject=With Management Comes Risk: Finding Flaws in FileWave MDM&body=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm)

![](https://claroty.com/build/assets/team82-newsletter-bg-BlXIsUMi.jpg)

Stay in the know Get the Team82 Newsletter

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm) [ __ Twitter ](https://twitter.com/intent/post?text=With Management Comes Risk: Finding Flaws in FileWave MDM&url=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm) [ __ ](mailto:?subject=With Management Comes Risk: Finding Flaws in FileWave MDM&body=https://claroty.com/team82/research/with-management-comes-risk-finding-flaws-in-filewave-mdm)

Recent Vulnerability Disclosures

  * ##### [CVE-2026-28256 A Use of Hard-coded, Security-relevant Constants vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28256)
  * ##### [CVE-2026-28255 A Use of Hard-coded Credentials vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 6.8 ](/team82/disclosure-dashboard/cve-2026-28255)
  * ##### [CVE-2026-28254 A Missing Authorization vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to access sensitive information through unprotected APIs. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28254)
  * ##### [CVE-2026-28253 A Memory Allocation with Excessive Size Value vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to cause a denial-of-service condition. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 7.5 ](/team82/disclosure-dashboard/cve-2026-28253)
  * ##### [CVE-2026-28252 A Use of a Broken or Risky Cryptographic Algorithm vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to bypass authentication and gain root-level access to the device. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 8.1 ](/team82/disclosure-dashboard/cve-2026-28252)

Solutions

  * [Claroty xDome Platform](/platform)
  * [Industrial Cybersecurity](/industrial-cybersecurity)
  * [Healthcare Cybersecurity](/healthcare-cybersecurity)
  * [Commercial Cybersecurity](/commercial-cybersecurity)
  * [Public Sector Cybersecurity](/public-sector-cybersecurity)

Threat Research

  * [Team82 Home](/team82)
  * [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard)
  * [Research](/team82/research)
  * [PGP Key](/team82/pgp-key)

Partners

  * [Partners](/partners)
  * [Technology Alliance Partners](/partners/technology-alliances)
  * [Channel Partners](/partners/channel-partners)
  * [Become a Partner](https://portal.claroty.com/#/page/partner-reg)
  * [Partner Login](https://portal.claroty.com/#/page/login)

Resources

  * [Resource Library](/resources)
  * [Blog](/blog)
  * [White Papers](/resources/white-papers)
  * [Reports](/resources/reports)
  * [Case Studies](/resources/case-studies)
  * [Datasheets](/resources/datasheets)
  * [Integration Briefs](/resources/integration-briefs)
  * [Videos](https://www.youtube.com/@claroty20)
  * [Claroty Nexus](https://nexusconnect.io)

Company

  * [About Us](/company)
  * [Careers](/careers)
  * [Leadership](/leadership)
  * [Newsroom](/newsroom)
  * [xCel Enablement & Training](/xcel-enablement-and-training)
  * [Trust Center](/trust)
  * [Customer Experience](/customer-experience)
  * [Events](/event-listing)
  * [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies)
  * [Contact Us](/contact-us)

[ ![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) ](/)

© 2026 Claroty. All rights reserved.

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)

[Terms & Conditions](/terms-conditions) / [Privacy Policy](/privacy-policy)

![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) __ Close Menu

  * [Platform](/platform) __

[The Claroty Platform](/platform) [Claroty CPS Protection Program](/cps-protection-program) [Claire, the AI Security Agent](/claire) [Asset Inventory](/platform/asset-inventory) [Exposure Management](/platform/exposure-management) [Network Protection](/platform/network-protection) [Secure Access](/platform/secure-access) [Threat Detection](/platform/threat-detection) [Operational Efficiency](/platform/operational-efficiency) [Integrations](/platform/integrations)

  * [Industries]() __

[Industrial Home](/industrial-cybersecurity) [Industrial Verticals](/industrial-cybersecurity/verticals) [Healthcare Home](/healthcare-cybersecurity) [Commercial Home](/commercial-cybersecurity) [Commercial Verticals](/commercial-cybersecurity/verticals)

  * [Public Sector](/public-sector-cybersecurity) __

[Public Sector Home](/public-sector-cybersecurity) [Federal Government Home](/public-sector-cybersecurity/us-government-cybersecurity) [SLED Home](/public-sector-cybersecurity/sled-government-cybersecurity)

  * [Customers](/customer-experience) __

[Customer Experience](/customer-experience) [Case Studies](/resources/case-studies) [xCel Enablement & Training for Customers](/xcel-enablement-and-training-for-customers)

  * [Partners](/partners) __

[Partners](/partners) [Technology Alliance Partners](/partners/technology-alliances) [Channel Partners](/partners/channel-partners) [Partner Login](https://portal.claroty.com/#/page/login)

  * [Threat Research](/team82) __

[Team82 Home](/team82) [Threat Intelligence](/threat-intelligence) [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard) [Research](/team82/research) [Talks](/team82/talks) [PGP Key](/team82/pgp-key)

  * [Resources](/resources) __

[Blog](/blog) [Reports](/resources/reports) [White Papers](/resources/white-papers) [Datasheets & Solution Overviews](/resources/datasheets) [Integration Briefs](/resources/integration-briefs) [Case Studies](/resources/case-studies) [On-Demand Webinars](/resources/webinars) [Visit our Nexus Website](https://nexusconnect.io)

  * [Company](/company) __

[About Us](/company) [Careers](/careers) [Leadership](/leadership) [Newsroom](/newsroom) [xCel Enablement & Training](/xcel-enablement-and-training) [Trust Center](/trust) [Events](/event-listing) [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies) [Contact Us](/contact-us)

  * [__Search](/search)

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)
