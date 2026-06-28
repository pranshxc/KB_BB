---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-06_size-matters-when-capital-letters-introduce-vulnerabilities.md
original_filename: 2023-05-06_size-matters-when-capital-letters-introduce-vulnerabilities.md
title: Size matters! When capital letters introduce vulnerabilities
category: documents
detected_topics:
- xss
- api-security
- command-injection
- cloud-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- api-security
- command-injection
- cloud-security
- mobile-security
- supply-chain
language: en
raw_sha256: 15d2ef9a19cd2fc6282055ccecb69c811fc583a3b8c708440793f0529ceceb0e
text_sha256: 7528040955478fc1f15383b9ec2f5e5712166f67fc4f40c252761c37a89ea716
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Size matters! When capital letters introduce vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-06_size-matters-when-capital-letters-introduce-vulnerabilities.md
- Source Type: markdown
- Detected Topics: xss, api-security, command-injection, cloud-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `15d2ef9a19cd2fc6282055ccecb69c811fc583a3b8c708440793f0529ceceb0e`
- Text SHA256: `7528040955478fc1f15383b9ec2f5e5712166f67fc4f40c252761c37a89ea716`


## Content

---
title: "Size matters! When capital letters introduce vulnerabilities"
page_title: "SECFORCE - Security without compromise"
url: "https://www.secforce.com/blog/size-matters-when-capital-letters-introduce-vulnerabilities/"
final_url: "https://www.secforce.com/blog/size-matters-when-capital-letters-introduce-vulnerabilities/"
authors: ["Mario Stathakopoulos", "Pieter Van Schaik"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2023-05-06"
added_date: "2023-05-13"
source: "pentester.land/writeups.json"
original_index: 1181
---

[ ](https://www.secforce.com)

  * [Our Services](javascript:void\(0\))

  * Control Assurance Ensuring your security controls are effective, reliable, and consistently protecting your organisation against evolving internal and external threats.
  * Business Resilience Strengthening your business to anticipate, respond, and recover effectively from disruptions, minimising impact on operations.
  * Governance, Risk and Compliance Helping your organisation confidently navigate complex regulations, manage evolving risks, and implement robust governance for sustainable growth.

![01A-Application Security-Black](/assets/img/menu/01A-Application Security-Black.8bc03b672299.svg) Application Security Ensuring your software, web, mobile, and API applications are designed, developed, and maintained to withstand attacks and protect sensitive data.

  * [Web Application Penetration Testing](/web-application-penetration-testing)
  * [Mobile Application Penetration Testing](/mobile-application-penetration-testing)
  * [API Penetration Testing](/api-penetration-testing)
  * Thick Client Penetration Testing
  * Source Code Review

![01B-Deployment-Security-Black](/assets/img/menu/01B-Deployment-Security-Black.17fb669447d6.svg) Deployment Security Securing the environments, configurations, and deployment processes of your applications and systems to prevent vulnerabilities and misconfigurations.

  * [AI/LLM Application Testing](/ai-llm-application-testing)
  * [IoT Penetration Testing](/iot-penetration-testing)
  * [Cloud Configuration Review](/cloud-configuration-review)
  * VDI Breakout Assessment
  * Host Configuration Review
  * AD Review

![01C-Infrastructure-Security-Black](/assets/img/menu/01C-Infrastructure-Security-Black.e2c7ca64bc2f.svg) Infrastructure Security Protecting your networks, servers, endpoints, and IT infrastructure from internal and external threats while ensuring operational continuity.

  * [Internal Infrastructure Penetration Testing](/internal-infrastructure-penetration-testing)
  * [External Infrastructure Penetration Testing](/external-infrastructure-penetration-testing)
  * Wireless Infrastructure Penetration Testing

![02A-Incident-Readiness-Black](/assets/img/menu/02A-Incident-Readiness-Black.0db4a571a2fe.svg) Incident Readiness Preparing your organisation to quickly detect, respond to, and recover from security incidents, minimising impact and downtime.

  * [Malware Resilience Testing](/malware-resilience-testing)
  * Endpoint Detection and Response Testing
  * [Ransomware Readiness](/ransomware-readiness)
  * [Crisis Management (Gold Team)](/gold-teaming-exercise)
  * Stolen Laptop Review
  * Physical Breach Simulation

![02B-Advanced-Threat Resilience-Black](/assets/img/menu/02B-Advanced-Threat-Resilience-Black.8ca3d57008db.svg) Advanced Threat Resilience Simulating and testing your defences against sophisticated cyber threats to strengthen detection, response, and recovery capabilities.

  * [Red Team Exercise](/red-team)
  * [Purple Team Exercise](/purple-team)
  * [Phishing Exercise](/phishing-exercise)

![02C-Regulated-TLPT-Black](/assets/img/menu/02C-Regulated-TLPT-Black.0cfad849b89d.svg) Regulated TLPT Conducting specialised tests and exercises aligned with regulatory frameworks to ensure compliance and resilience under formal supervision.

  * CBEST, TBEST, TIBER
  * iCast, Feer, Corie

![03A-Advisory-Services-Black](/assets/img/menu/03A-Advisory-Services-Black.824130d779c2.svg) Advisory Services Providing strategic guidance, risk assessments, and expert recommendations to optimise your cybersecurity posture and decision-making.

  * Virtual CISO
  * [Cybersecurity Strategy](/cybersecurity-strategy)
  * [Remediation Companion](/cybersecurity-remediation-companion)
  * Attack Path Mapping
  * Gap Analysis

![03B-Compliance-Black](/assets/img/menu/03B-Compliance-Black.c469ad4bf328.svg) Compliance Helping your organisation meet industry standards and regulatory requirements while embedding security best practices into daily operations.

  * [Compliance and Audit Readiness](/compliance-and-audit-readiness)

  * [Resources](javascript:void\(0\))

  * [ The Lab ](/blog)
  * [ The Blog ](/the-blog)
  * [ Case Studies ](/case-studies)
  * [ LLMGoat ](/llm-goat)

  * [About Us](javascript:void\(0\))

  * [ Why Secforce ](/why-secforce)
  * [ Join ](/join-the-force)

  * [![comment](/assets/img/testing_services/comment.67d2c688ef24.svg)Contact us](/contact-us)

[ ](https://www.secforce.com)

  * [Our Services]()
  * Control Assurance
  * [ ![01A-Application Security-Black](/assets/img/menu/01A-Application Security-Black.8bc03b672299.svg) Application Security ]()
  * [Web Application Penetration Testing](/web-application-penetration-testing)
  * [Mobile Application Penetration Testing](/mobile-application-penetration-testing)
  * [API Penetration Testing](/api-penetration-testing)
  * Thick Client Penetration Testing
  * Source Code Review
  * [ ![01B-Deployment-Security-Black](/assets/img/menu/01B-Deployment-Security-Black.17fb669447d6.svg) Deployment Security ]()
  * [AI/LLM Application Testing](/ai-llm-application-testing)
  * [IoT Penetration Testing](/iot-penetration-testing)
  * [Cloud Configuration Review](/cloud-configuration-review)
  * VDI Breakout Assessment
  * Host Configuration Review
  * AD Review
  * [ ![01C-Infrastructure-Security-Black](/assets/img/menu/01C-Infrastructure-Security-Black.e2c7ca64bc2f.svg) Infrastructure Security ]()
  * [Internal Infrastructure Penetration Testing](/internal-infrastructure-penetration-testing)
  * [External Infrastructure Penetration Testing](/external-infrastructure-penetration-testing)
  * Wireless Infrastructure Penetration Testing
  * Business Resilience
  * ![02A-Incident-Readiness-Black](/assets/img/menu/02A-Incident-Readiness-Black.0db4a571a2fe.svg) Incident Readiness
  * [Malware Resilience Testing](/malware-resilience-testing)
  * Endpoint Detection and Response Testing
  * [Ransomware Readiness](/ransomware-readiness/)
  * [Crisis Management (Gold Team)](/gold-teaming-exercise)
  * Stolen Laptop Review
  * Physical Breach Simulation
  * [ ![02B-Advanced-Threat Resilience-Black](/assets/img/menu/02B-Advanced-Threat-Resilience-Black.8ca3d57008db.svg) Advanced Threat Resilience ]()
  * [Red Team Exercise](/red-team)
  * [Purple Team Exercise](/purple-team)
  * [Phishing Exercise](/phishing-exercise)
  * [ ![02C-Regulated-TLPT-Black](/assets/img/menu/02C-Regulated-TLPT-Black.0cfad849b89d.svg) Regulated TLPT ]()
  * CBEST, TBEST, TIBER
  * iCast, Feer, Corie
  * Governance, Risk and Compliance
  * [ ![03A-Advisory-Services-Black](/assets/img/menu/03A-Advisory-Services-Black.824130d779c2.svg) Advisory Services ]()
  * Virtual CISO
  * [Cybersecurity Strategy](/cybersecurity-strategy)
  * [Remediation Companion](/cybersecurity-remediation-companion)
  * Attack Path Mapping
  * Gap Analysis
  * [ ![03B-Compliance-Black](/assets/img/menu/03B-Compliance-Black.c469ad4bf328.svg) Compliance ]()
  * [Compliance and Audit Readiness](/compliance-and-audit-readiness)
  * [Resources]()
  * [ The Lab ](/blog)
  * [ The Blog ](/the-blog)
  * [ Case Studies ](/case-studies)
  * [ LLMGoat ](/llm-goat)
  *  * [About Us]()
  * [ Why Secforce ](/why-secforce)
  * [ Join ](/join-the-force)

[![comment](/assets/img/testing_services/comment.67d2c688ef24.svg)Contact us](/contact-us)

# Size matters! When capital letters introduce vulnerabilities

![Blogpost Image](/media/images/MicrosoftTeams-image_1.width-1000.png)

One aspect to always keep in mind when introducing third-party software in your organisation is security. Any third-party application should ideally undergo an independent security assessment before adaptation, to ensure that no misconfigurations and vulnerabilities are inadvertently introduced in the security ecosystem. If, during this process, a vulnerability is identified, it should then be promptly and responsibly disclosed to the relevant vendor, whose responsibility is to apply proper mitigation actions and roll out fixes for their customer base.

Microsoft Dynamics 365 is a CRM software solution, which has gained a lot of traction recently as it helps organisations efficiently maintain customer information under a centralised platform. During a recent engagement whose focus was to assess the security of a Microsoft Dynamics 365 application, SECFORCE consultants identified several instances where the application was susceptible to Cross-Site-Scripting attacks.

Upon discovery, the established policies were followed, and the issue was shared with Microsoft’s security team through their responsible disclosure program. The vulnerability was confirmed by Microsoft’s engineers and a fix was deployed shortly after.

**But what was the issue?**

Microsoft Dynamics offers a rich text editor in various parts of the application, which allows users to include notes within certain areas, such as the _Opportunities_ section. When performing a security assessment, such functionalities are of great interest as they can allow the inclusion and rendering of HTML content by design. Therefore, they are often a good candidate for mounting Cross Site Scripting attacks.

**What is Cross-site scripting (XSS)?**

Cross-site scripting (XSS) occurs when an attacker is able to inject malicious code (usually in the form of a script) into a webpage viewed by other users. This code can then be executed in the context of the victim's browser, allowing the attacker to steal sensitive information, manipulate the victim's session, or perform other malicious actions. XSS attacks can be prevented through a combination of input validation, output encoding, and other security measures.

It is common practice for off-the-shelf products to have defense mechanisms in place, such as validation of user input to prevent code injection attacks (e.g. XSS).

In this instance, while reviewing the functionality of the Rich Text Editor, it was identified that it was possible to include links and URLs in user content, via the **< a href>** HTML tag. Additionally, the editor allowed the user to select a protocol for the URL, through a list of options or even set a custom one as can be observed in the evidence below.

![Arbitrary protocols supported for URLs](/media/images/new-image_nAnYoXz.width-800.png)

A common vector for XSS is to use the "**javascript** :" protocol when crafting a link. This can allow JavaScript execution once a user clicks on the included link. While attempting to do so, it was identified that the application had taken this attack vector into consideration, as there was a client-side check to disallow the usage of this protocol as can be observed below.

![Client-side validation for javascript: protocol](/media/images/image2.width-800.png)

The next step was to validate whether there was also a server-side check for the same attack vector. To that end, the client-side check was trivially bypassed by intercepting the request and injecting the payload in the _notetext_ parameter, and the request was subsequently submitted to the server.

![Injection of javascript: protocol within the intercepted request](/media/images/image3.width-800.png)

As demonstrated here, the request appeared to have been accepted, however when trying to load the new note entry, it was observed that the malicious payload had been removed and replaced with the ‘#’ character. Therefore, it was concluded that there was also server-side validation that removed such malicious content.

![Server-side validation removes injected javascript: protocol](/media/images/image4.width-800.png)

The challenge was to identify if there was a way to bypass the validations performed by the application which could allow us to conduct an XSS attack. There are a few ways to do this, and most of them involve trying to identify if a regex pattern check is being used for the filtering and if it can be bypassed. One of the first things to do in these cases, is to verify if the filtering can distinguish between case sensitive input. In other words, what if our payload used a combination of lower and uppercase characters – e.g. **JaVaSCrIpT:**. Will the filtering mechanism in place still be able to detect and remove our injection?

Having this in mind, the following payload was submitted `JaVaScRiPt:alert()` through the application’s UI, as shown below. The client-side check was bypassed and the application accepted the new entry without errors.

![Injecting case sensitive javascript: protocol to bypass validations](/media/images/bypass-filtering-2.width-800.png)

The next step was to identify whether our malicious entry had bypassed the existing server-side validation. Checking the source code for our new note entry, confirmed that the payload had also bypassed any server-side checks and was stored in the application’s page. This means that if a victim:

  * visited that page  

  * attempted to use the Rich Text Editor  

  * and clicked on the provided URL  

The stored malicious JavaScript code would be executed under the context of the victim user.

![Injected payload bypasses client-side and server-side validations](/media/images/bypassed-filtering-injetion-present.width-800.png)

Upon clicking on the malicious link, the alert popup will get triggered in a new page within the same domain’s context. This attack method can be leveraged in multiple ways, and if a user with appropriate privileges is targeted, it can allow escalation of privileges via calling the relevant API endpoints that Dynamics utilizes.

![XSS Executed](/media/images/image7_UjGcpoG.width-800.png)

As per Microsoft’s engineer team review, the issue is considered of “ _Important”_ status.

**Timeline**

04/04/2023 - Issue reported

19/04/2023 - Issue verified and report state changed to a fix being developed

20/04/2023 - Severity set to Important

26/05/2023 - Fix released

**TLDR**

It was possible to bypass the implemented client-side and server-side filters of the Dynamics 365 Rich Text editor and achieve XSS by using a combination of lowercase and uppercase letters. The main reason that allowed such an attack was the fact that there wasn’t an effective regex mechanism implemented to take into consideration case sensitive input.

### Share on

[![](/assets/img/post/share-linkedin.bbf3bfe683c7.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https://www.secforce.com/blog/size-matters-when-capital-letters-introduce-vulnerabilities/)

[![](/assets/img/post/share-twitter.be2cd0ba0dc1.svg)](https://twitter.com/intent/tweet?url=https://www.secforce.com/blog/size-matters-when-capital-letters-introduce-vulnerabilities/)

[![](/assets/img/post/share-facebook.e2eb401c1f6b.svg)](https://www.facebook.com/sharer.php?u=https://www.secforce.com/blog/size-matters-when-capital-letters-introduce-vulnerabilities/)

### You may also be interested in...

[![imagensecforcepost.png](/media/images/imagensecforcepost.original.png)](/blog/holistic-penetration-testing-when-1-1-does-not-always-equal-2/)

Oct. 21, 2012

### [Holistic penetration testing – when 1 + 1 does not always equal 2](/blog/holistic-penetration-testing-when-1-1-does-not-always-equal-2/)

Our view about the correct approach to penetration testing.

[See more](/blog/holistic-penetration-testing-when-1-1-does-not-always-equal-2/)

[![imagensecforcepost.png](/media/images/imagensecforcepost.original.png)](/blog/cve-2011-3368-poc-apache-proxy-scanner/)

Oct. 10, 2011

### [CVE-2011-3368 PoC - Apache Proxy Scanner](/blog/cve-2011-3368-poc-apache-proxy-scanner/)

ECFORCE has developed a proof of concept for this vulnerability. The script exploits the vulnerability and allows the user to retrieve arbitrary known files from the DMZ.

[See more](/blog/cve-2011-3368-poc-apache-proxy-scanner/)

##### Contact

[+44 (0) 845 056 8694](tel:+44 \(0\) 845 056 8694) [info@secforce.com](mailto:info@secforce.com)

##### Social

  * [Linkedin](https://www.linkedin.com/company/secforce-ltd/)
  * [Youtube](https://www.youtube.com/channel/UCuN3JqLlbwmk02G37Q2ba4Q)
  * [Twitter](https://twitter.com/secforce_ltd)
  * [Github](https://github.com/SECFORCE)

[![](/assets/img/logos/secforce.011a81db89c9.svg)](https://www.secforce.com)

![Crest](/assets/img/logos/Crest-White.c86cfe88dfec.svg) ![VA](/assets/img/logos/Crest-VA-White.b0d4236905dd.png) ![Pen Test](/assets/img/logos/Pen-Test-White.c7ad54e39937.svg) ![Star](/assets/img/logos/cert-crest-star.0097b63c50d8.png) ![Cbest](/assets/img/logos/CBEST-White.47a37b071bc6.svg) ![ISO27001](/assets/img/logos/ISO_27001_White.3f0f29c234e1.svg) ![ISO9001](/assets/img/logos/B-ISO9001.9215c083a36f.png) ![Tiber](/assets/img/logos/TIBER-White.fe33a7e8fdb3.svg) ![Cyber Essentials Certified](/assets/img/logos/log_Cyberessentials.1074e6de93a2.svg) ![AICPA SOC 2](/assets/img/logos/SOC_logo_white.b20f6cc7e407.svg)

Thank you!

All done, my friend. The information reached SECFORCE goblins safely.

Please try again later.

Oops... Something went wrong. Please check that the form fields are correct.
