---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-19_escalating-privileges-via-third-party-windows-installers.md
original_filename: 2023-07-19_escalating-privileges-via-third-party-windows-installers.md
title: Escalating Privileges via Third-Party Windows Installers
category: documents
detected_topics:
- cloud-security
- supply-chain
- sso
- access-control
- automation-abuse
- command-injection
tags:
- imported
- documents
- cloud-security
- supply-chain
- sso
- access-control
- automation-abuse
- command-injection
language: en
raw_sha256: 2bc8ee6dca813c5f7acef9fff119a4a40fb333b67541425f7573d9bf9996016d
text_sha256: 6ff90eb8354703aaf85749e4f375c55399e75239c8c6db2d133734c18eb71fa6
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating Privileges via Third-Party Windows Installers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-19_escalating-privileges-via-third-party-windows-installers.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, sso, access-control, automation-abuse, command-injection
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `2bc8ee6dca813c5f7acef9fff119a4a40fb333b67541425f7573d9bf9996016d`
- Text SHA256: `6ff90eb8354703aaf85749e4f375c55399e75239c8c6db2d133734c18eb71fa6`


## Content

---
title: "Escalating Privileges via Third-Party Windows Installers"
page_title: "Mandiant Cybersecurity Consulting | Google Cloud"
url: "https://www.mandiant.com/resources/blog/privileges-third-party-windows-installers"
final_url: "https://cloud.google.com/security/mandiant"
authors: ["Andrew Oliveau (@AndrewOliveau)"]
programs: ["Atera"]
bugs: ["Local Privilege Escalation", "DLL Hijacking"]
publication_date: "2023-07-19"
added_date: "2023-07-31"
source: "pentester.land/writeups.json"
original_index: 916
---

[**_Get help now_** for a security breach or possible incident.](https://cloud.google.com/security/report-incident)

![Mandiant Logo](https://www.gstatic.com/bricks/image/58777d3f-ec3a-4151-984c-ec37ae1a3f8f.png)

# 

Mandiant Cybersecurity Consulting

Elevate your cyber defense, from incident response to business resilience.

Talk to an expert[](https://cloud.google.com/security/contact/mandiant-consulting)

Explore all services[](https://cloud.google.com/security/consulting/mandiant-consulting-all)

![Mandiant Logo](https://www.gstatic.com/bricks/image/58777d3f-ec3a-4151-984c-ec37ae1a3f8f.png)

# 

Mandiant Cybersecurity Consulting

Elevate your cyber defense, from incident response to business resilience.

Talk to an expert[](https://cloud.google.com/security/contact/mandiant-consulting)

Explore all services[](https://cloud.google.com/security/consulting/mandiant-consulting-all)

  * [![Cyber Defense Summit 2026, Google Cloud Security](https://www.gstatic.com/bricks/image/7c353749-b5cb-40b2-bf0a-26ac0334f0b9.png)Cyber Defense Summit 2026Register today to reserve your spot](https://cyberdefensesummit.mandiant.com)
  * [![M-Trends 2026](https://www.gstatic.com/bricks/image/8a79a498-a5c0-4d08-9405-60b2a4651c76.png)M-Trends 2026Stay ahead of the latest cyber threats](https://cloud.google.com/security/resources/m-trends)
  * [![The Defender's Advantage](https://www.gstatic.com/bricks/image/920579f1-040b-4a6a-9242-8dd97d1044bb.png) The Defender's Advantage A guide to activating cyber defense](https://cloud.google.com/security/resources/defenders-advantage)

  * Consulting
  * Threat intel services
  * AI security
  * Cyber risk partners
  * Customers & Analysts
  * Resources
  * Get started

Page Contents

  * Consulting
  * Threat intel services
  * AI security
  * Cyber risk partners
  * Customers & Analysts
  * Resources
  * Get started

## 

Tackle breaches confidently

Partner with world-renowned experts. Our team combines a deep understanding of global attacker behavior with over two decades of frontline experience to provide comprehensive [incident response services](https://cloud.google.com/security/consulting/mandiant-incident-response-services), including preparedness, technical response, and crisis management.

[![A good incident response plan turns chaos into clarity. Best practices for incident response planning](https://www.gstatic.com/bricks/image/a4b140c4-6bbe-4ef4-b3b0-e63b9af15015.png)Read the guide](https://cloud.google.com/security/best-practices-for-incident-response-plans)

#### 

Get flexible access to experts with a Mandiant Retainer

Adapt to changing priorities and access the services you need, without reworking contracts. The [Mandiant Retainer](https://cloud.google.com/security/consulting/mandiant-retainer) is a flexible incident response retainer that gives organizations immediate access to cybersecurity experts with pre-negotiated terms, 2-hour response times, and proactive services to strengthen your defenses.

#### 

Protect your brand with strategic crisis communications

Don't let a cyberattack define your brand. [Mandiant crisis communication services](https://cloud.google.com/security/solutions/crisis-communications) provide the strategic readiness you need to respond effectively to modern, multifaceted attacks. Partner with us to safeguard your stakeholders, mitigate reputational risk, and preserve the brand you've worked hard to build.

#### 

Uncover past and present threats in your network

Run a [c](https://services.google.com/fh/files/misc/ds-compromise-assessment-en.pdf)[ompromise assessment](https://services.google.com/fh/files/misc/ds-compromise-assessment-en.pdf) to discover if you've been breached and proactively hunt for hidden attackers. Our experts combine extensive incident response experience with real-time threat intelligence to find evidence of past or ongoing intrusions across your enterprise environment.

## 

Increase business resilience and strategic readiness

Outmaneuver today’s threats. [Secure your operations by proactively enhancing your security capabilities.](https://cloud.google.com/security/consulting/mandiant-strategic-readiness) Our experts can help you advance your approach to cyber risk management and be ready for complex challenges, from M&A due diligence to supply chain attacks and insider threats.

#### 

Manage cyber risk, make better business decisions

[Pinpoint the cyber risks most relevant to your organization](https://cloud.google.com/security/consulting/mandiant-cyber-risk-management) and understand their potential business impact. Translate critical findings and recommendations for executive leadership and stakeholders through [tabletop exercises](https://services.google.com/fh/files/misc/ds-tabletop-exercises-en.pdf), empowering you to make smarter security investments and mitigate future risks.

#### 

Assess and strengthen your defense capabilities

Run a [cyber defense assessment](https://services.google.com/fh/files/misc/ds-cyber-defense-assessment-en.pdf) to gain a clear understanding of your defensive capabilities and receive a prioritized roadmap to build a stronger, more resilient security program, prepared for any challenge. Harden your technical controls, and improve the performance of every critical defense function—from initial threat detection to [full environment recovery.](https://services.google.com/fh/files/misc/mandiant_cyber_resiliency_cire_whitepaper_en.pdf)

#### 

Build frontline skills with Mandiant Academy

Prepare your team to combat real-world threats with reality-based case studies and training on the latest attacker TTPs from frontline incident response and threat intelligence experts. Choose from a [full range of learning formats](https://cloud.google.com/learn/security/mandiant-academy) that fit your needs, including on-demand courses, instructor-led classes, certification programs, and [immersive, hands-on exercises in the ThreatSpace™ cyber range](https://cloud.google.com/learn/security/mandiant-academy-threatspace).

[![How ThreatSpace prepares customers for real-world threats with Google Cloud Security](https://www.gstatic.com/bricks/image/367cb407-76eb-44c2-a1e2-3ec70f07c573.png)2:45](https://www.youtube.com/watch?v=tougo8159t8)

## 

Test and strengthen your security program with real-world attacks

Pressure-test your security program with [realistic, objective-based assessments](https://cloud.google.com/security/consulting/mandiant-technical-assurance). Our experts mimic genuine threat actor behavior—using the latest TTPs from the frontlines—to help you understand your weaknesses from an adversary’s perspective and build a truly resilient defense.

[![Watch Mandiant Red Teamers in Action: Pushing the Limits of Red Teaming](https://www.gstatic.com/bricks/image/54b4cc48-08ee-43bb-a8e3-9b215b0519e1.png)1:41](https://www.youtube.com/watch?v=cbuMxSfNV3c)

Watch Mandiant red teamers in action: Pushing the limits of red teaming

#### 

Push the boundaries of red team assessments

See how your defenses perform against a sophisticated, goal-oriented adversary. Pushing beyond standard testing, our [red team assessments](https://services.google.com/fh/files/misc/ds-red-team-operations-en.pdf) emulate a real attacker pursuing custom objectives, revealing complex attack paths that conventional assessments often miss. This unique engagement provides an unparalleled opportunity to harden your defenses by combatting a realistic threat before it happens.

#### 

Harden your cloud with an architecture assessment

Secure your assets and data across any cloud environment with a [cloud architecture assessment](https://services.google.com/fh/files/misc/ds-cloud-architecture-assessment-000236-03.pdf)—from AWS and Azure to Google Cloud. Identify and mitigate commonly exploited misconfigurations, reduce your attack surface, and gain the visibility needed to effectively detect and respond to threats across your entire cloud estate.

#### 

Expose risks with offensive security and penetration testing

Improve your security team’s detection and response capabilities against realistic attack scenarios with a full range of [offensive security services](https://cloud.google.com/security/consulting/mandiant-technical-assurance), from collaborative assessments to testing specific assets and capabilities across technologies.

## 

Elevate your cyber defense capabilities across all critical functions

[Transform your core security processes and technologies. ](https://cloud.google.com/security/consulting/mandiant-cybersecurity-transformation)Our experts help you up-level threat detection, containment, and remediation capabilities while optimizing your security operations and functions for a more mature and resilient defense.

#### 

Integrate and optimize Google SecOps with Mandiant

Realize the full transformative potential of the [Google SecOps](https://cloud.google.com/security/products/security-operations) platform by operationalizing it within your organization. [Plan, optimize, and validate your Google SecOps deployment](https://services.google.com/fh/files/misc/mandiant_secops_transformation_services_ds.pdf) with guidance from Mandiant experts to ensure you achieve its full potential.

#### 

Balance cyber risk with rapid business innovation

Enable business innovation by translating complex security topics into the language of risk and value for executive leadership and the board. Bridge the gap between security and business objectives with [executive cybersecurity services](https://services.google.com/fh/files/misc/mandiant-executive-cybersecurity-services-000490-02.pdf) to establish security as a strategic enabler, helping the business achieve its innovation goals securely.

#### 

Build a resilient cyber defense center

Improve your overall defense posture and [transition from a reactive incident response methodology to a predictive, mission-focused cyber defense center](https://services.google.com/fh/files/misc/ds-cyber-defense-center-dev-000045-05.pdf). Identify and close gaps in your security monitoring and response capabilities by building and implementing core processes aligned with an adaptive defense strategy.

[![Discover the 6 critical functions of cyber defense. The Defender's Advantage: Guide to activating cyber defense](https://www.gstatic.com/bricks/image/b5f2fd5d-007a-4c63-af48-8f759296ccc6.png)Download the ebook](https://cloud.google.com/security/resources/defenders-advantage)

## 

Turn threat intelligence into confident decisions

[Operationalize and maximize your threat intelligence sources with Mandiant](https://cloud.google.com/security/consulting/threat-intelligence-services). Build a program tailored to your specific environment, delivered through custom research, embedded expertise, and comprehensive skills development.

[![M-Trends 2026 Report](https://www.gstatic.com/bricks/image/0e9b9660-47e4-4bf2-92db-f99adf13a17f.png)Download the report](https://cloud.google.com/security/resources/m-trends)

#### 

Accelerate decisions with custom Mandiant insights

Inform and accelerate your security decisions with [customized cyber risk research and analysis](https://services.google.com/fh/files/misc/threat_diagnostic_datasheet.pdf), personalized for your specific environment, use cases, and stakeholder needs. Use these tailored insights to enhance your security posture, drive effective hunt missions, and strengthen your vulnerability management for a more resilient security program.

#### 

Embed frontline intelligence experts into your team

Get access to world-class experts for [personalized reporting and part-time expertise](https://services.google.com/fh/files/misc/security_essential_intel_access_ds.pdf), providing timely, analyst-compiled responses from curated intelligence holdings. For deeper integration, get a [dedicated expert embedded with your team](https://services.google.com/fh/files/misc/advanced-intelligence-access-ds-en.pdf), providing early access to raw intelligence and a direct line to world-class tooling.

#### 

Build best-in-class cyber threat intelligence capabilities

[Apply best practices for the consumption, analysis, and practical application of threat intelligence](https://services.google.com/fh/files/misc/intelligence-capability-development-ds-en.pdf) to operationalize insights and maximize the value of your cyber threat intelligence (CTI) sources. Train your team with [a full range of CTI training, on-demand certifications, expert coaching, and immersive, real-world exercises](https://cloud.google.com/learn/security/mandiant-academy-courses).

## 

Secure your AI systems and leverage AI to strengthen your cyber defenses

AI technologies are transforming the way organizations operate. Mandiant experts can help you [utilize AI to enhance cyber defenses while safeguarding the use of your AI systems.](https://cloud.google.com/security/solutions/mandiant-ai-consulting)

#### 

Secure your use of AI, end-to-end

[Evaluate the end-to-end security of your AI systems](https://cloud.google.com/security/solutions/mandiant-ai-consulting) and implementation to assess and safeguard your training data, models, and custom applications before attackers can exploit them. Build upon the extensive, combined, real-world experience of Mandiant and Google in protecting production AI systems.

#### 

Battle-test your AI systems and defenses

[Identify the critical insights needed to proactively harden your AI systems](https://cloud.google.com/security/solutions/mandiant-ai-consulting) and overall security posture. Measure the effectiveness of your controls against the latest AI-specific threats and assess your security team’s ability to detect and respond to a live attack in a controlled environment.

#### 

Pave the path towards an agentic defense future

[Understand how to augment your cyber defense capabilities and prepare for the future by leveraging the power of AI](https://cloud.google.com/security/solutions/mandiant-ai-consulting). Develop a strategic plan to integrate AI into your processes to reduce defender toil and increase investigation efficiency. Explore how to create AI-based detections and [practice AI-assisted incident response in a realistic, virtual cyber range with ThreatSpace™](https://cloud.google.com/learn/security/mandiant-academy-threatspace).

[![Stay ahead of threats by harnessing the power of AI, securely](https://www.gstatic.com/bricks/image/a0ffb899-f73d-46cf-a62c-9c173e81cb2f.png)Read the report](https://cloud.google.com/security/resources/ai-risk-and-resilience)

## 

Tap specialists across a range of services that fit your business challenges

Address your most unique and complex security challenges, from [ransomware and multifaceted extortion defense](https://cloud.google.com/security/solutions/ransomware?hl=en) to securing mission-critical [operational technology (OT) and industrial control systems (ICS)](https://cloud.google.com/security/solutions/mandiant-operational-technology), with a wide range of specialized consulting services. All of our engagements are delivered by experienced specialists and backed by real-time frontline threat intelligence, ensuring targeted guidance to build a stronger defense.

Explore all services[](https://cloud.google.com/security/consulting/mandiant-consulting-all)

Download our services overview[](https://services.google.com/fh/files/misc/mandiant_consulting_overview_datasheet.pdf)

## Mandiant cyber risk partners

Mandiant collaborates with a global network of leading law firms, insurance providers and brokers, ransomware negotiators, and other specialized firms to help you mitigate risk and minimize liability from cyberattacks. This integrated ecosystem simplifies the cyber risk management process for executives and security teams by improving threat visibility, accelerating incident response, and preparing your organization for a crisis before it occurs.

Explore our partners[](https://cloud.google.com/security/partners/cybersecurity-risk-partners)

### 

Trusted by leading organizations

[![How UC Riverside aces digital safety for students, staff, and researchers](https://www.gstatic.com/bricks/image/56ee8d00-057f-4cf9-b330-c06ac6fdd470.jpg)The CIO of the University of California, Riverside describes how Mandiant delivers industry-leading expertise that combined with Google SecOps has transformed their security.See the video](https://www.youtube.com/watch?v=Wv81ntozeBs)

[![The UK's largest homewares retailer lands a one-two punch against cyber threats](https://www.gstatic.com/bricks/image/e6d8a8a1-3c53-4b43-967a-da540efc4826.jpg)The UK’s largest homewares retailer, Dunelm talks about landing a one-two punch against cyber threats with Google SecOps and a Mandiant Retainer.See the video](https://www.youtube.com/watch?v=MUQGfgoJ7VY)

[![Trends from the seat of a CISO](https://www.gstatic.com/bricks/image/82aefa63-409f-4b8a-aa2c-21b1acc311b4.jpg)CISOs from AT&T and Coinbase join Mandiant's CTO to share and discuss firsthand experiences and insights from the frontlines on responding to nation-state actors and complex insider risk.See the video](https://www.youtube.com/watch?v=VVzJq74Zyuw)

[![How the UK's biggest digital bank hunts threats faster with Google SecOps](https://www.gstatic.com/bricks/image/6d972f4c-6ff1-4259-ba4c-1ac447c453d1.jpg)Lloyds Banking Group is confident in its ability to detect sophisticated attacks and can now focus on what matters most — staying ahead of the next generation of threats.See the video](https://www.youtube.com/watch?v=7gNyN3fBn00)

### 

**Recognized by industry analysts**

  * [![IDC](https://www.gstatic.com/bricks/image/33b16f76-a391-44be-ac2b-915f977fca00.png) Google is a Leader in the IDC MarketScape: Worldwide Incident Response 2025 Vendor Assessment  
Read the report](https://cloud.google.com/resources/content/security-idc-marketscape-2025-incident-response)
  * [![Forrester](https://www.gstatic.com/bricks/image/9abe6d21-25d4-4abb-860c-e7cf77460960.png)Google is a Leader in the Forrester Wave™: Cybersecurity Incident Response Services, Q2 2024Read the report](https://cloud.google.com/resources/content/security/forrester-wave-incident-response-2024)
  * [![IDC](https://www.gstatic.com/bricks/image/992564c5-a33c-432a-9699-b2a7774ae4cb.png)Google is a Leader in the IDC MarketScape: Worldwide Cybersecurity Consulting Services 2024 Vendor AssessmentRead the report](https://services.google.com/fh/files/misc/idc-marketscape-ww-cybersecurity-consulting-vendor-assessment-2024.pdf)

### 

Browse resources

#### Events

#### Reports

#### Blogs

#### Podcasts

#### For the CISO

  * [![Cyber Defense Summit 26, Google Cloud Security](https://www.gstatic.com/bricks/image/4da88ef5-8e54-4eb4-9c89-c1806b2d06aa.png)Cyber Defense Summit 2026Crafted to equip elite security professionals with the strategies, tools, and insights needed to outmaneuver increasingly sophisticated, AI-enabled adversaries and build resilient cyber ecosystems.Register now](https://cyberdefensesummit.mandiant.com/)
  * [![Next iconography in vivid colors](https://www.gstatic.com/bricks/image/fe9c6aeb-3ea9-4a70-abc9-16b3eb0f350b.png)Google Cloud Next 2026Catch-up sessions on the keynotes and select sessions are now available on demand.Explore content on-demand](https://www.googlecloudevents.com/next-vegas)
  * [![Yellow security lock ](https://www.gstatic.com/bricks/image/fc120bbf-c7b0-4ce8-9e04-df8f13e3b913.png)Security TalksJoin our security experts in this ongoing series as they explore the latest AI innovations across our security product portfolio, threat intelligence best practices, and more.Watch on-demand](https://cloudonair.withgoogle.com/events/google-cloud-security-talks-june-2026)

View More

  * [![M-Trends 2026](https://www.gstatic.com/bricks/image/12b8b9ae-e444-42d8-a6ca-e7431b884953.png)Mandiant M-Trends 2026Stay ahead of the latest cyber threatsRead the report](https://cloud.google.com/security/resources/m-trends)
  * [![Cybersecurity Forecast 2026](https://www.gstatic.com/bricks/image/e1580b44-7dfe-473e-8739-c9df09f54914.png)Cybersecurity Forecast 2026Forward-looking insights to plan for the year ahead.Read the report](https://cloud.google.com/security/resources/cybersecurity-forecast)
  * [![Defender shield in white grid lines](https://www.gstatic.com/bricks/image/ee3f2220-52fb-4e61-bb94-38d1d56d0d6e.png)The Defender's AdvantageA guide to activating cyber defense.Read the eBook](https://cloud.google.com/security/resources/defenders-advantage)

View More

  * [![TI blog](https://www.gstatic.com/bricks/image/091a2f69-2cc9-4142-a8c7-f25930177d83.png)Google Threat Intelligence blogThe latest frontline investigations, analysis, and in-depth security research from Mandiant experts.Read the blog](https://cloud.google.com/blog/topics/threat-intelligence)
  * [![GCS Blog](https://www.gstatic.com/bricks/image/94693feb-eb8f-46dd-ad07-370a40590342.png)Google Cloud Security blogNews, tips, and inspiration to accelerate your security and AI transformation. Read the blog](https://cloud.google.com/blog/products/identity-security)
  * [![Community blog](https://www.gstatic.com/bricks/image/2ac43e6e-9e9d-400e-a381-60cbd16c96c9.png)Google Cloud Security Community blogInsights, answers, and expert perspectives to optimize your security tools, from Googlers and seasoned users.Read the blog](https://security.googlecloudcommunity.com/p/blog)

View More

  * [![TDA podcast](https://www.gstatic.com/bricks/image/02c03a94-f8aa-4cf1-941c-4fdacc1efec5.png)The Defender’s Advantage PodcastLuke McNamara is joined by fellow cybersecurity experts providing frontline insights into the latest attacks, threat research, and trends. Dive deep on nation-state activity, malware, and more. Listen now](https://podcasts.apple.com/us/podcast/the-defenders-advantage-podcast/id1073779629)
  * [![binary podcast](https://www.gstatic.com/bricks/image/e52553ab-76bf-46cf-96d0-dd03394dea7a.png)Behind the Binary PodcastGoogle FLARE team member Josh Stroschein uncovers the human stories and unique perspectives of the experts who secure our digital world through reverse engineering.Listen now](https://open.spotify.com/show/3yWgmIuhWPtmTDFWDovtlc)
  * [![cloud sec podcast](https://www.gstatic.com/bricks/image/6c3171c3-db93-4b5b-a66b-db31d01e24da.png)Cloud Security PodcastAnton Chuvakin and Timothy Peacock tackle today’s most interesting cloud security stories, including what we’re doing at Google Cloud. Come for the no-nonsense insights; stay for the threat model questioning and bad puns.Listen now ](https://cloud.withgoogle.com/cloudsecurity/podcast/)

View More

  * [![Team in discussion](https://www.gstatic.com/bricks/image/d0a5c773-911b-4526-be25-ee849769116a.png)CISO Insights HubExpert perspectives, reports, and frameworks to help security leaders navigate today’s evolving threat landscape, with insights from Google Cloud’s Office of the CISO.Learn more](https://cloud.google.com/solutions/security/leaders)
  * [![Man discussing with the team in conference room](https://www.gstatic.com/bricks/image/b429460d-2231-4d0e-a712-59ec25ad865c.png)Board of Directors Insights HubInsights and best practices designed for boards to lead security decisions and ensure resilient, secure operations.Learn more](https://cloud.google.com/solutions/security/board-of-directors)
  * [![Blue color Mike and earphone illustration](https://www.gstatic.com/bricks/image/ae39710b-31a8-41ab-aaf6-7ef600af255f.png)The Cyber Savvy Boardroom From Google Cloud's Office of the CISO, get monthly strategic insights from security leaders, executives, and board members to help you confidently shape your organization's security posture and future. Listen now](https://www.youtube.com/playlist?list=PLkdSRxA6DyHt7kbj0wUuatxF9eYOFro7k)

View More

#### Events

  * [![Cyber Defense Summit 26, Google Cloud Security](https://www.gstatic.com/bricks/image/4da88ef5-8e54-4eb4-9c89-c1806b2d06aa.png)Cyber Defense Summit 2026Crafted to equip elite security professionals with the strategies, tools, and insights needed to outmaneuver increasingly sophisticated, AI-enabled adversaries and build resilient cyber ecosystems.Register now](https://cyberdefensesummit.mandiant.com/)
  * [![Next iconography in vivid colors](https://www.gstatic.com/bricks/image/fe9c6aeb-3ea9-4a70-abc9-16b3eb0f350b.png)Google Cloud Next 2026Catch-up sessions on the keynotes and select sessions are now available on demand.Explore content on-demand](https://www.googlecloudevents.com/next-vegas)
  * [![Yellow security lock ](https://www.gstatic.com/bricks/image/fc120bbf-c7b0-4ce8-9e04-df8f13e3b913.png)Security TalksJoin our security experts in this ongoing series as they explore the latest AI innovations across our security product portfolio, threat intelligence best practices, and more.Watch on-demand](https://cloudonair.withgoogle.com/events/google-cloud-security-talks-june-2026)

View More

#### Reports

  * [![M-Trends 2026](https://www.gstatic.com/bricks/image/12b8b9ae-e444-42d8-a6ca-e7431b884953.png)Mandiant M-Trends 2026Stay ahead of the latest cyber threatsRead the report](https://cloud.google.com/security/resources/m-trends)
  * [![Cybersecurity Forecast 2026](https://www.gstatic.com/bricks/image/e1580b44-7dfe-473e-8739-c9df09f54914.png)Cybersecurity Forecast 2026Forward-looking insights to plan for the year ahead.Read the report](https://cloud.google.com/security/resources/cybersecurity-forecast)
  * [![Defender shield in white grid lines](https://www.gstatic.com/bricks/image/ee3f2220-52fb-4e61-bb94-38d1d56d0d6e.png)The Defender's AdvantageA guide to activating cyber defense.Read the eBook](https://cloud.google.com/security/resources/defenders-advantage)

View More

#### Blogs

  * [![TI blog](https://www.gstatic.com/bricks/image/091a2f69-2cc9-4142-a8c7-f25930177d83.png)Google Threat Intelligence blogThe latest frontline investigations, analysis, and in-depth security research from Mandiant experts.Read the blog](https://cloud.google.com/blog/topics/threat-intelligence)
  * [![GCS Blog](https://www.gstatic.com/bricks/image/94693feb-eb8f-46dd-ad07-370a40590342.png)Google Cloud Security blogNews, tips, and inspiration to accelerate your security and AI transformation. Read the blog](https://cloud.google.com/blog/products/identity-security)
  * [![Community blog](https://www.gstatic.com/bricks/image/2ac43e6e-9e9d-400e-a381-60cbd16c96c9.png)Google Cloud Security Community blogInsights, answers, and expert perspectives to optimize your security tools, from Googlers and seasoned users.Read the blog](https://security.googlecloudcommunity.com/p/blog)

View More

#### Podcasts

  * [![TDA podcast](https://www.gstatic.com/bricks/image/02c03a94-f8aa-4cf1-941c-4fdacc1efec5.png)The Defender’s Advantage PodcastLuke McNamara is joined by fellow cybersecurity experts providing frontline insights into the latest attacks, threat research, and trends. Dive deep on nation-state activity, malware, and more. Listen now](https://podcasts.apple.com/us/podcast/the-defenders-advantage-podcast/id1073779629)
  * [![binary podcast](https://www.gstatic.com/bricks/image/e52553ab-76bf-46cf-96d0-dd03394dea7a.png)Behind the Binary PodcastGoogle FLARE team member Josh Stroschein uncovers the human stories and unique perspectives of the experts who secure our digital world through reverse engineering.Listen now](https://open.spotify.com/show/3yWgmIuhWPtmTDFWDovtlc)
  * [![cloud sec podcast](https://www.gstatic.com/bricks/image/6c3171c3-db93-4b5b-a66b-db31d01e24da.png)Cloud Security PodcastAnton Chuvakin and Timothy Peacock tackle today’s most interesting cloud security stories, including what we’re doing at Google Cloud. Come for the no-nonsense insights; stay for the threat model questioning and bad puns.Listen now ](https://cloud.withgoogle.com/cloudsecurity/podcast/)

View More

#### For the CISO

  * [![Team in discussion](https://www.gstatic.com/bricks/image/d0a5c773-911b-4526-be25-ee849769116a.png)CISO Insights HubExpert perspectives, reports, and frameworks to help security leaders navigate today’s evolving threat landscape, with insights from Google Cloud’s Office of the CISO.Learn more](https://cloud.google.com/solutions/security/leaders)
  * [![Man discussing with the team in conference room](https://www.gstatic.com/bricks/image/b429460d-2231-4d0e-a712-59ec25ad865c.png)Board of Directors Insights HubInsights and best practices designed for boards to lead security decisions and ensure resilient, secure operations.Learn more](https://cloud.google.com/solutions/security/board-of-directors)
  * [![Blue color Mike and earphone illustration](https://www.gstatic.com/bricks/image/ae39710b-31a8-41ab-aaf6-7ef600af255f.png)The Cyber Savvy Boardroom From Google Cloud's Office of the CISO, get monthly strategic insights from security leaders, executives, and board members to help you confidently shape your organization's security posture and future. Listen now](https://www.youtube.com/playlist?list=PLkdSRxA6DyHt7kbj0wUuatxF9eYOFro7k)

View More

## 

Have cybersecurity questions? Contact us.

Mandiant experts are ready to answer your cybersecurity consulting questions.

Request a cybersecurity consult[](https://cloud.google.com/security/contact/mandiant-consulting)

Incident response assistance[](https://cloud.google.com/security/report-incident)

![](https://www.gstatic.com/cgc/renaissance/image/MultiPath_Bottom_2X_Centered_static.png)

menu

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

[Overview](https://cloud.google.com/why-google-cloud)[Solutions](https://cloud.google.com/solutions)[Products](https://cloud.google.com/products)[Pricing](https://cloud.google.com/pricing)[Resources](https://cloud.google.com/docs/get-started)[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)[Contact us](https://cloud.google.com/contact/security)



 _search_ _send_

[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)

[Console](https://console.cloud.google.com/)

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/security/mandiant&hl=en-US&prompt=select_account&service=cloudconsole)

Incident Response Assistance[](https://cloud.google.com/security/report-incident)

[Security](https://cloud.google.com/security)

[Threat Intel](https://cloud.google.com/security/products/threat-intelligence)[SecOps](https://cloud.google.com/security/products/security-operations)[Consulting](https://cloud.google.com/security/consulting/mandiant-services)[Security resources](https://cloud.google.com/security/resources)

Incident Response Assistance[](https://cloud.google.com/security/report-incident)

Contact us[](https://cloud.google.com/contact/security)

close

  * Accelerate your digital transformation
  * Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
  * [Learn more](https://cloud.google.com/transform)

  * Key benefits
  * [Why Google CloudTop reasons businesses choose us.](https://cloud.google.com/why-google-cloud)

  * [AI and AgentsGet enterprise-ready AI.](https://cloud.google.com/ai)

  * [MulticloudRun your apps wherever you need them.](https://cloud.google.com/multicloud)

  * [Global infrastructureBuild on the same infrastructure as Google.](https://cloud.google.com/infrastructure)

  * [Data CloudMake smarter decisions with unified data.](https://cloud.google.com/data-cloud)

  * [Modern Infrastructure CloudNext generation of cloud infrastructure.](https://cloud.google.com/solutions/modern-infrastructure)

  * [SecurityProtect your users, data, and apps.](https://cloud.google.com/security)

  * [Productivity and collaborationConnect your teams with AI-powered apps.](https://workspace.google.com)

  * Reports and insights
  * [Executive insightsCurated C-suite perspectives.](https://cloud.google.com/executive-insights)

  * [Analyst reportsRead what industry analysts say about us.](https://cloud.google.com/analyst-reports)

  * [WhitepapersBrowse and download popular whitepapers.](https://cloud.google.com/whitepapers)

  * [Customer storiesExplore case studies and videos.](https://cloud.google.com/customers)

close

  * Industry Solutions
  * Application Modernization
  * Artificial Intelligence
  * APIs and Applications
  * Data Analytics
  * Databases
  * Infrastructure
  * Productivity and Collaboration
  * Security
  * Startups and SMB

See all solutions[](https://cloud.google.com/solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.](https://cloud.google.com/solutions#industry-solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/retail.svg)RetailAnalytics and collaboration tools for the retail value chain.](https://cloud.google.com/solutions/retail)

  * [![](https://www.gstatic.com/cloud/images/navigation/cpg.svg)Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.](https://cloud.google.com/solutions/cpg)

  * [![](https://www.gstatic.com/cloud/images/navigation/finance.svg)Financial ServicesComputing, data management, and analytics tools for financial services.](https://cloud.google.com/solutions/financial-services)

  * [![](https://www.gstatic.com/cloud/images/navigation/hcls.svg)Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.](https://cloud.google.com/solutions/healthcare-life-sciences)

  * [![](https://www.gstatic.com/cloud/images/navigation/media.svg)Media and EntertainmentSolutions for content production and distribution operations.](https://cloud.google.com/solutions/media-entertainment)

  * [![](https://www.gstatic.com/cloud/images/navigation/telecommunications.svg)TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.](https://cloud.google.com/solutions/telecommunications)

  * [![](https://www.gstatic.com/cloud/images/navigation/gaming.svg)GamesAI-driven solutions to build and scale games faster.](https://cloud.google.com/solutions/games)

  * [![](https://www.gstatic.com/cloud/images/navigation/manufacturing.svg)ManufacturingMigration and AI tools to optimize the manufacturing value chain.](https://cloud.google.com/solutions/manufacturing)

  * [![](https://www.gstatic.com/cloud/images/navigation/supply-chain.svg)Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.](https://cloud.google.com/solutions/supply-chain-logistics)

  * [![](https://www.gstatic.com/cloud/images/navigation/government.svg)GovernmentData storage, AI, and analytics solutions for government agencies.](https://cloud.google.com/gov)

  * [![](https://www.gstatic.com/cloud/images/navigation/icon-sprite.svg#education)EducationTeaching tools to provide more engaging learning experiences.](https://cloud.google.com/edu/higher-education)

  * Not seeing what you're looking for?
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Application ModernizationAssess, plan, implement, and measure software practices and capabilities to modernize and simplify your organization’s business application portfolios.](https://cloud.google.com/solutions/camp)

  * [CAMPProgram that uses DORA to improve your software delivery capabilities.](https://cloud.google.com/solutions/camp)

  * [Modernize Traditional ApplicationsAnalyze, categorize, and get started with cloud migration on traditional workloads.](https://cloud.google.com/solutions/modernize-traditional-applications)

  * [Migrate from PaaS: Cloud Foundry, OpenshiftTools for moving your existing containers into Google's managed container services.](https://cloud.google.com/solutions/migrate-from-paas)

  * [Migrate from MainframeAutomated tools and prescriptive guidance for moving your mainframe apps to the cloud.](https://cloud.google.com/solutions/mainframe-modernization)

  * [Modernize Software DeliverySoftware supply chain best practices - innerloop productivity, CI/CD and S3C.](https://cloud.google.com/solutions/software-delivery)

  * [DevOps Best PracticesProcesses and resources for implementing DevOps in your org.](https://cloud.google.com/devops)

  * [SRE PrinciplesTools and resources for adopting SRE in your org.](https://cloud.google.com/sre)

  * [Platform EngineeringComprehensive suite of managed services and Golden Paths to build, manage, and scale IDPs.](https://cloud.google.com/solutions/platform-engineering)

  * [Architect for MulticloudManage workloads across multiple clouds with a consistent platform.](https://cloud.google.com/solutions/architect-multicloud)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.](https://cloud.google.com/solutions/ai)

  * [Gemini Enterprise for Customer ExperienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)

  * [Gemini EnterpriseUnified agentic portfolio for your entire organization.](https://cloud.google.com/gemini-enterprise)

  * [AI Commerce SearchGoogle-quality search and product recommendations for retailers.](https://cloud.google.com/gemini-enterprise-cx/commerce)

  * [Google Cloud with GeminiAI assistants for application development, coding, and more.](https://cloud.google.com/ai/gemini)

  * [Physical AISimulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines.](https://cloud.google.com/solutions/physical-ai)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.](https://cloud.google.com/solutions/apis-and-applications)

  * [New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.](https://cloud.google.com/solutions/new-channels-using-apis)

  * [Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.](https://cloud.google.com/solutions/unlocking-legacy-applications)

  * [Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.](https://cloud.google.com/solutions/open-banking-apix)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.](https://cloud.google.com/solutions/data-analytics-and-ai)

  * [Data MigrationMigrate and modernize your data warehouse and data lakes with AI-powered migration services.](https://cloud.google.com/solutions/data-migration)

  * [Data LakehouseUnify and govern your multimodal data with a high-performance and open data lakehouse.](https://cloud.google.com/solutions/data-lakehouse)

  * [Real-time AnalyticsInsights from ingesting, processing, and analyzing event streams.](https://cloud.google.com/solutions/stream-analytics)

  * [Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.](https://cloud.google.com/solutions/marketing-analytics)

  * [DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.](https://cloud.google.com/datasets)

  * [Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.](https://cloud.google.com/solutions/business-intelligence)

  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)

  * [Geospatial AnalyticsA comprehensive platform to solve for geospatial use cases at scale.](https://cloud.google.com/solutions/geospatial)

  * [Data ScienceManaged services and integrated workflows to build, manage, and scale data science.](https://cloud.google.com/solutions/data-science)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.](https://cloud.google.com/solutions/databases)

  * [Database MigrationGuides and tools to simplify your database migration life cycle.](https://cloud.google.com/solutions/database-migration)

  * [Database ModernizationUpgrades to modernize your operational database infrastructure.](https://cloud.google.com/solutions/database-modernization)

  * [Databases for GamesBuild global, live games with Google Cloud databases.](https://cloud.google.com/solutions/databases/games)

  * [Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.](https://cloud.google.com/products/databases)

  * [Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.](https://cloud.google.com/solutions/oracle)

  * [Open Source DatabasesFully managed open source databases with enterprise-grade support.](https://cloud.google.com/solutions/open-source-databases)

  * [SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.](https://cloud.google.com/sql-server)

  * [Gemini for DatabasesSupercharge database development and management with AI.](https://cloud.google.com/products/gemini/databases)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)InfrastructureMigrate quickly with solutions for SAP, VMware, Windows, Oracle, and other workloads.](https://cloud.google.com/solutions/infrastructure-modernization)

  * [Application MigrationDiscovery and analysis tools for moving to the cloud.](https://cloud.google.com/solutions/application-migration)

  * [SAP on Google CloudCertifications for running SAP applications and SAP HANA.](https://cloud.google.com/solutions/sap)

  * [High Performance ComputingCompute, storage, and networking options to support any workload.](https://cloud.google.com/solutions/hpc)

  * [Windows on Google CloudTools and partners for running Windows workloads.](https://cloud.google.com/windows)

  * [Data Center MigrationMigration solutions for VMs, apps, databases, and more.](https://cloud.google.com/solutions/data-center-migration)

  * [Active AssistAutomatic cloud resource optimization and increased security.](https://cloud.google.com/solutions/active-assist)

  * [Virtual DesktopsRemote work solutions for desktops and applications (VDI & DaaS).](https://cloud.google.com/solutions/virtual-desktops)

  * [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)

  * [Backup and Disaster RecoveryEnsure your business continuity needs are met.](https://cloud.google.com/solutions/backup-dr)

  * [Red Hat on Google CloudGoogle and Red Hat provide an enterprise-grade platform for traditional on-prem and custom applications.](https://cloud.google.com/solutions/redhat)

  * [Cross-Cloud NetworkSimplify hybrid and multicloud networking, and secure your workloads, data, and users.](https://cloud.google.com/solutions/cross-cloud-network)

  * [AI InfrastructureTrain, serve and operate your AI applications on the agent-native infrastructure powering Google.](https://cloud.google.com/ai-infrastructure)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.](https://workspace.google.com/enterprise/)

  * [Google WorkspaceCollaboration and productivity tools for enterprises.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)

  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)

  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)

  * [Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.](https://chromeenterprise.google)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)SecurityDetect, investigate, and respond to online threats to help protect your business.](https://cloud.google.com/solutions/security)

  * [Agentic SOCDelivering better security outcomes with AI agents.](https://cloud.google.com/solutions/agentic-soc)

  * [Web App and API ProtectionThreat and fraud protection for your web applications and APIs.](https://cloud.google.com/security/solutions/web-app-and-api-protection)

  * [Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.](https://cloud.google.com/security/solutions/security-and-resilience)

  * [Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.](https://cloud.google.com/solutions/risk-and-compliance-as-code)

  * [Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.](https://cloud.google.com/security/solutions/software-supply-chain-security)

  * [Security FoundationRecommended products to help achieve a strong security posture.](https://cloud.google.com/security/solutions/security-foundation)

  * [Google Cloud Cybershield™Strengthen nationwide cyber defense.](https://cloud.google.com/security/solutions/secops-cybershield)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.](https://cloud.google.com/solutions#section-13)

  * [Startup ProgramGet financial, business, and technical support to take your startup to the next level.](https://cloud.google.com/startup)

  * [Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.](https://cloud.google.com/solutions/smb)

  * [Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.](https://cloud.google.com/saas)

close

  * Featured Products
  * AI and Machine Learning
  * Business Intelligence
  * Compute
  * Containers
  * Data Analytics
  * Databases
  * Developer Tools
  * Distributed Cloud
  * Hybrid and Multicloud
  * Industry Specific
  * Integration Services
  * Management Tools
  * Maps and Geospatial
  * Media Services
  * Migration
  * Networking
  * Operations
  * Productivity and Collaboration
  * Security and Identity
  * Serverless
  * Storage
  * Web3

See all products (100+)[](https://cloud.google.com/products#featured-products)

  * Featured Products

  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini Enterprise appSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)

  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Agent PlatformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)

  * [![](https://www.gstatic.com/cloud/images/navigation/compute-engine.png)Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)

  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-storage.png)Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)

  * [![](https://www.gstatic.com/cloud/images/navigation/bigquery.png)BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)

  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-run.png)Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)

  * [![](https://www.gstatic.com/cloud/images/navigation/kubernetes-engine.png)Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)

  * [![](https://www.gstatic.com/cloud/images/navigation/looker.png)LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)

  * [![](https://www.gstatic.com/cloud/images/navigation/apigee.png)Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)

  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-sql.png)Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.](https://cloud.google.com/sql)

  * [![](https://www.gstatic.com/cloud/images/navigation/networking.png)Cloud CDNContent delivery network for delivering web and video.](https://cloud.google.com/cdn)

  * Not seeing what you're looking for?
  * [See all products (100+)](https://cloud.google.com/products#featured-products)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)AI and Machine Learning](https://cloud.google.com/products/ai)

  * [Gemini Enterprise Agent PlatformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)

  * [Gemini Enterprise appSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)

  * [Gemini Enterprise for Customer ExperienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)

  * [Model GardenSingle place to discover over 200 models from Google and Google partners.](https://console.cloud.google.com/agent-platform/model-garden)

  * [Customer Experience Agent StudioBuild conversational AI with both deterministic and gen AI functionality.](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)

  * [Agent SearchBuild Google-quality search for your enterprise apps and experiences.](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)

  * [Speech-to-TextSpeech recognition and transcription across 125 languages.](https://cloud.google.com/speech-to-text)

  * [Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.](https://cloud.google.com/text-to-speech)

  * [Translation AILanguage detection, translation, and glossary support.](https://cloud.google.com/translate)

  * [Vision AICustom and pre-trained models to detect emotion, text, and more.](https://cloud.google.com/vision)

  * [Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.](https://cloud.google.com/solutions/contact-center-ai-platform)

  * Not seeing what you're looking for?
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)

  * Business Intelligence

  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)

  * [Data StudioInteractive data suite for dashboarding, reporting, and analytics.](https://cloud.google.com/data-studio)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Compute](https://cloud.google.com/products/compute)

  * [Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)

  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)

  * [Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.](https://cloud.google.com/gpu)

  * [Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)

  * [Spot VMsCompute instances for batch jobs and fault-tolerant workloads.](https://cloud.google.com/spot-vms)

  * [BatchFully managed service for scheduling batch jobs.](https://cloud.google.com/batch)

  * [Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)

  * [Bare MetalInfrastructure to run specialized workloads on Google Cloud.](https://cloud.google.com/bare-metal)

  * [RecommenderUsage recommendations for Google Cloud products and services.](https://cloud.google.com/recommender/docs/whatis-activeassist)

  * [VMware EngineFully managed, native VMware Cloud Foundation software stack.](https://cloud.google.com/vmware-engine)

  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)

  * Not seeing what you're looking for?
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Containers](https://cloud.google.com/containers)

  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)

  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)

  * [Cloud BuildSolution for running build steps in a Docker container.](https://cloud.google.com/build)

  * [Artifact RegistryPackage manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)

  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)

  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)

  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)

  * [Deep Learning ContainersContainers with data science frameworks, libraries, and tools.](https://cloud.google.com/deep-learning-containers/docs)

  * [KnativeComponents to create Kubernetes-native cloud-based software.](https://knative.dev/docs/)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)

  * [BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)

  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)

  * [DataflowReal-time analytics for stream and batch processing.](https://cloud.google.com/products/dataflow)

  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)

  * [LakehouseOpen lakehouse platform with enterprise storage and performance capabilities.](https://cloud.google.com/products/lakehouse)

  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)

  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)

  * [Knowledge CatalogAlways-on catalog for AI that provides universal context for agents.](https://cloud.google.com/products/knowledge-catalog)

  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)

  * [Data Analytics Migration ServicesFree-to-use, cloud-native and AI-powered data migration services.](https://cloud.google.com/solutions/data-migration)

  * [Managed Service for Apache KafkaManaged Kafka service to operate highly available Apache Kafka clusters.](https://cloud.google.com/products/managed-service-for-apache-kafka)

  * Not seeing what you're looking for?
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Databases](https://cloud.google.com/products/databases)

  * [AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.](https://cloud.google.com/alloydb)

  * [Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.](https://cloud.google.com/sql)

  * [FirestoreHighly scalable and serverless NoSQL document database, with MongoDB compatibility.](https://cloud.google.com/firestore)

  * [SpannerCloud-native relational database with unlimited scale and 99.999% availability.](https://cloud.google.com/spanner)

  * [BigtableCloud-native wide-column database for large-scale, low-latency workloads.](https://cloud.google.com/bigtable)

  * [DatastreamServerless change data capture and replication service.](https://cloud.google.com/datastream)

  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)

  * [Bare Metal SolutionFully managed infrastructure for your Oracle workloads.](https://cloud.google.com/bare-metal)

  * [MemorystoreFully managed Redis and Memcached for sub-millisecond data access.](https://cloud.google.com/memorystore)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Developer Tools](https://cloud.google.com/products/tools)

  * [Artifact RegistryUniversal package manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)

  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)

  * [Cloud BuildContinuous integration and continuous delivery platform.](https://cloud.google.com/build)

  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)

  * [Cloud Deployment ManagerService for creating and managing Google Cloud resources.](https://cloud.google.com/deployment-manager/docs)

  * [Cloud SDKCommand-line tools and libraries for Google Cloud.](https://cloud.google.com/sdk)

  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)

  * [Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.](https://cloud.google.com/source-repositories/docs)

  * [Infrastructure ManagerAutomate infrastructure management with Terraform.](https://cloud.google.com/infrastructure-manager/docs)

  * [Cloud WorkstationsManaged and secure development environments in the cloud.](https://cloud.google.com/workstations)

  * [Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.](https://cloud.google.com/products/gemini/code-assist)

  * Not seeing what you're looking for?
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Distributed Cloud](https://cloud.google.com/distributed-cloud)

  * [Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.](https://cloud.google.com/distributed-cloud-connected)

  * [Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.](https://cloud.google.com/distributed-cloud-air-gapped)

  * Hybrid and Multicloud

  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)

  * [Apigee API ManagementAPI management, development, and security platform.](https://cloud.google.com/apigee)

  * [Migrate to ContainersTool to move workloads and existing applications to GKE.](https://cloud.google.com/products/cloud-migration/containers)

  * [Cloud BuildService for executing builds on Google Cloud infrastructure.](https://cloud.google.com/build)

  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)

  * [Cloud Service MeshFully managed service mesh based on Envoy and Istio.](https://cloud.google.com/products/service-mesh)

  * [Google Distributed CloudFully managed solutions for the edge and data centers.](https://cloud.google.com/distributed-cloud)

  * Industry Specific

  * [Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.](https://cloud.google.com/anti-money-laundering-ai)

  * [Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.](https://cloud.google.com/healthcare-api)

  * [Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.](https://cloud.google.com/device-connect)

  * [Telecom Network AutomationReady to use cloud-native automation for telecom networks.](https://cloud.google.com/telecom-network-automation)

  * [Telecom Data FabricTelecom data management and analytics with an automated approach.](https://cloud.google.com/telecom-data-fabric)

  * [Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.](https://cloud.google.com/telecom-subscriber-insights)

  * [Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).](https://cloud.google.com/products/spectrum-access-system)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Integration Services](https://cloud.google.com/integration-services)

  * [Application IntegrationConnect to 3rd party apps and enable data consistency without code.](https://cloud.google.com/application-integration)

  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)

  * [Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)

  * [Cloud TasksTask management service for asynchronous task execution.](https://cloud.google.com/tasks/docs)

  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)

  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)

  * [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion)

  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)

  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)

  * [EventarcBuild an event-driven architecture that can connect any service.](https://cloud.google.com/eventarc/docs)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Management Tools](https://cloud.google.com/products/management)

  * [Cloud ShellInteractive shell environment with a built-in command line.](https://cloud.google.com/shell/docs)

  * [Cloud consoleWeb-based interface for managing and monitoring cloud apps.](https://cloud.google.com/cloud-console)

  * [Cloud EndpointsDeployment and development management for APIs on Google Cloud.](https://cloud.google.com/endpoints/docs)

  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)

  * [Cloud APIsProgrammatic interfaces for Google Cloud services.](https://cloud.google.com/apis)

  * [Service CatalogService catalog for admins managing internal enterprise solutions.](https://cloud.google.com/service-catalog/docs)

  * [Cost ManagementTools for monitoring, controlling, and optimizing your costs.](https://cloud.google.com/cost-management)

  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)

  * [Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.](https://cloud.google.com/carbon-footprint)

  * [Config ConnectorKubernetes add-on for managing Google Cloud resources.](https://cloud.google.com/config-connector/docs/overview)

  * [Active AssistTools for easily managing performance, security, and cost.](https://cloud.google.com/solutions/active-assist)

  * Not seeing what you're looking for?
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Maps and Geospatial](https://cloud.google.com/solutions/geospatial)

  * [Earth EngineGeospatial platform for Earth observation data and analysis.](https://cloud.google.com/earth-engine)

  * [Google Maps PlatformCreate immersive location experiences and improve business operations.](https://mapsplatform.google.com)

  * Media Services

  * [Cloud CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)

  * [Live Stream APIService to convert live video and package for streaming.](https://cloud.google.com/livestream/docs)

  * [OpenCueOpen source render manager for visual effects and animation.](https://www.opencue.io/docs/getting-started/)

  * [Transcoder APIConvert video files and package them for optimized delivery.](https://cloud.google.com/transcoder/docs)

  * [Video Stitcher APIService for dynamic or server side ad insertion.](https://cloud.google.com/video-stitcher/docs)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Migration](https://cloud.google.com/products/cloud-migration)

  * [Migration CenterUnified platform for migrating and modernizing with Google Cloud.](https://cloud.google.com/migration-center/docs)

  * [Application MigrationApp migration to the cloud for low-cost refresh cycles.](https://cloud.google.com/solutions/application-migration)

  * [Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)

  * [Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)

  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)

  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)

  * [Data Analytics Migration ServicesStreamlined data warehouse and data lake migration tooling and incentives.](https://cloud.google.com/solutions/data-migration)

  * [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)

  * [Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.](https://cloud.google.com/transfer-appliance/docs/4.0/overview)

  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)

  * [VMware EngineMigrate and run your VMware workloads natively on Google Cloud.](https://cloud.google.com/vmware-engine)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Networking](https://cloud.google.com/products/networking)

  * [Cloud ArmorSecurity policies and defense against web and DDoS attacks.](https://cloud.google.com/security/products/armor)

  * [Cloud CDN and Media CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)

  * [Cloud DNSDomain name system for reliable and low-latency name lookups.](https://cloud.google.com/dns)

  * [Cloud Load BalancingService for distributing traffic across applications and regions.](https://cloud.google.com/load-balancing)

  * [Cloud NATNAT service for giving private instances internet access.](https://cloud.google.com/nat)

  * [Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.](https://cloud.google.com/hybrid-connectivity)

  * [Network Connectivity CenterConnectivity management to help simplify and scale networks.](https://cloud.google.com/network-connectivity-center)

  * [Network Intelligence CenterNetwork monitoring, verification, and optimization platform.](https://cloud.google.com/network-intelligence-center)

  * [Network Service TiersCloud network options based on performance, availability, and cost.](https://cloud.google.com/network-tiers)

  * [Virtual Private CloudSingle VPC for an entire organization, isolated within projects.](https://cloud.google.com/vpc)

  * [Private Service ConnectSecure connection between your VPC and services.](https://cloud.google.com/private-service-connect)

  * Not seeing what you're looking for?
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Operations](https://cloud.google.com/products/operations)

  * [Cloud LoggingGoogle Cloud audit, platform, and application logs management.](https://cloud.google.com/logging)

  * [Cloud MonitoringInfrastructure and application health with rich metrics.](https://cloud.google.com/monitoring)

  * [Error ReportingApplication error identification and analysis.](https://cloud.google.com/error-reporting/docs/grouping-errors)

  * [Managed Service for PrometheusFully-managed Prometheus on Google Cloud.](https://cloud.google.com/managed-prometheus)

  * [Cloud TraceTracing system collecting latency data from applications.](https://cloud.google.com/trace/docs)

  * [Cloud ProfilerCPU and heap profiler for analyzing application performance.](https://cloud.google.com/profiler/docs)

  * [Cloud QuotasManage quotas for all Google Cloud services.](https://cloud.google.com/docs/quotas)

  * Productivity and Collaboration

  * [AppSheetNo-code development platform to build and extend applications.](https://about.appsheet.com/home/)

  * [AppSheet AutomationBuild automations and applications on a unified platform.](https://cloud.google.com/appsheet/automation)

  * [Gemini Enterprise appSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)

  * [Google WorkspaceCollaboration and productivity tools for individuals and organizations.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)

  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)

  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)

  * [Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.](https://chromeenterprise.google)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Security and Identity](https://cloud.google.com/products/security-and-identity)

  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)

  * [Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.](https://cloud.google.com/security/products/sensitive-data-protection)

  * [Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.](https://cloud.google.com/security/products/managed-defense)

  * [Google Threat IntelligenceKnow who’s targeting you.](https://cloud.google.com/security/products/threat-intelligence)

  * [Security Command CenterPlatform for defending against threats to your Google Cloud assets.](https://cloud.google.com/security/products/security-command-center)

  * [Cloud Key ManagementManage encryption keys on Google Cloud.](https://cloud.google.com/security/products/security-key-management)

  * [Mandiant Incident ResponseMinimize the impact of a breach.](https://cloud.google.com/security/consulting/mandiant-incident-response-services)

  * [Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.](https://docs.cloud.google.com/chrome-enterprise-premium/)

  * [Assured WorkloadsCompliance and security controls for sensitive workloads.](https://cloud.google.com/security/products/assured-workloads)

  * [Google Security OperationsDetect, investigate, and respond to cyber threats.](https://cloud.google.com/security/products/security-operations)

  * [Mandiant ConsultingGet expert guidance before, during, and after an incident.](https://cloud.google.com/security/consulting/mandiant-services)

  * Not seeing what you're looking for?
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Serverless](https://cloud.google.com/serverless)

  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)

  * [Cloud FunctionsPlatform for creating functions that respond to cloud events.](https://cloud.google.com/functions)

  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)

  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)

  * [API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.](https://cloud.google.com/api-gateway/docs)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Storage](https://cloud.google.com/products/storage)

  * [Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)

  * [Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.](https://cloud.google.com/products/block-storage)

  * [FilestoreFile storage that is highly scalable and secure.](https://cloud.google.com/filestore)

  * [Persistent DiskBlock storage for virtual machine instances running on Google Cloud.](https://cloud.google.com/persistent-disk)

  * [Cloud Storage for FirebaseObject storage for storing and serving user-generated content.](https://firebase.google.com/products/storage)

  * [Local SSDBlock storage that is locally attached for high-performance needs.](https://cloud.google.com/products/local-ssd)

  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)

  * [Google Cloud Managed LustreHigh performance managed parallel file service.](https://cloud.google.com/products/managed-lustre)

  * [Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.](https://cloud.google.com/netapp-volumes)

  * [Backup and DR ServiceService for centralized, application-consistent data protection.](https://cloud.google.com/backup-disaster-recovery)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Web3](https://cloud.google.com/web3)

  * [Blockchain Node EngineFully managed node hosting for developing on the blockchain.](https://cloud.google.com/blockchain-node-engine)

  * [Blockchain RPCEnterprise-grade RPC for building on the blockchain.](https://cloud.google.com/products/blockchain-rpc)

close

  * Save money with our transparent approach to pricing
  * Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)

  * Pricing overview and tools
  * [Google Cloud pricingPay only for what you use with no lock-in.](https://cloud.google.com/pricing)

  * [Pricing calculatorCalculate your cloud savings.](https://cloud.google.com/products/calculator)

  * [Google Cloud free tierExplore products with free monthly usage.](https://cloud.google.com/free)

  * [Cost optimization frameworkGet best practices to optimize workload costs.](https://cloud.google.com/architecture/framework/cost-optimization)

  * [Cost management toolsTools to monitor and control your costs.](https://cloud.google.com/cost-management)

  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)

  * [Cloud SQL](https://cloud.google.com/sql/pricing)

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)

  * [Cloud Storage](https://cloud.google.com/storage/pricing)

  * [BigQuery](https://cloud.google.com/bigquery/pricing)

  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)

close

  * Learn & build
  * [Google Cloud Free Program$300 in free credits and 20+ free products.](https://cloud.google.com/free)

  * [Solution GeneratorGet AI generated solution recommendations.](https://cloud.google.com/solution-generator)

  * [QuickstartsGet tutorials and walkthroughs.](https://cloud.google.com/docs/tutorials?doctype=quickstart)

  * [BlogRead our latest product news and stories.](https://cloud.google.com/blog)

  * [Learning HubGrow your career with role-based training.](https://cloud.google.com/learn)

  * [Google Cloud certificationPrepare and register for certifications.](https://cloud.google.com/certification)

  * [Cloud computing basicsLearn more about cloud computing basics.](https://cloud.google.com/discover)

  * [Cloud Architecture CenterGet reference architectures and best practices.](https://cloud.google.com/architecture)

  * Connect
  * [InnovatorsJoin Google Cloud's developer program.](https://cloud.google.com/innovators/innovatorsplus)

  * [Developer CenterStay in the know and stay connected.](https://cloud.google.com/developers)

  * [Events and webinarsBrowse upcoming and on demand events.](https://cloud.google.com/events)

  * [Google Cloud CommunityAsk questions, find answers, and connect.](https://discuss.google.dev/c/google-cloud/14)

  * Consulting and Partners
  * [Google Cloud ConsultingWork with our experts on cloud projects.](https://cloud.google.com/consulting)

  * [Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.](https://cloud.google.com/marketplace)

  * [Find a partnerExplore the benefits of working with a partner.](https://cloud.google.com/partners)

  * [Google Cloud partnersLearn about the ecosystem and resources.](https://partners.cloud.google.com)

close

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

  * [Overview](https://cloud.google.com/why-google-cloud)
  * arrow_forward
  * [Solutions](https://cloud.google.com/solutions)
  * arrow_forward
  * [Products](https://cloud.google.com/products)
  * arrow_forward
  * [Pricing](https://cloud.google.com/pricing)
  * arrow_forward
  * [Resources](https://cloud.google.com/docs/get-started)
  * arrow_forward
  * [Docs](https://cloud.google.com/docs)
  * [Support](https://cloud.google.com/support-hub)
  * [Console](https://console.cloud.google.com/)
  * [Security](https://cloud.google.com/security)
  * [Threat Intel](https://cloud.google.com/security/products/threat-intelligence)
  * [SecOps](https://cloud.google.com/security/products/security-operations)
  * [Consulting](https://cloud.google.com/security/consulting/mandiant-services)
  * [Security resources](https://cloud.google.com/security/resources)

  * Accelerate your digital transformation
  * [Learn more](https://cloud.google.com/transform)
  * Key benefits
  * [Why Google Cloud](https://cloud.google.com/why-google-cloud)
  * [AI and Agents](https://cloud.google.com/ai)
  * [Multicloud](https://cloud.google.com/multicloud)
  * [Global infrastructure](https://cloud.google.com/infrastructure)
  * [Data Cloud](https://cloud.google.com/data-cloud)
  * [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure)
  * [Security](https://cloud.google.com/security)
  * [Productivity and collaboration](https://workspace.google.com)
  * Reports and insights
  * [Executive insights](https://cloud.google.com/executive-insights)
  * [Analyst reports](https://cloud.google.com/analyst-reports)
  * [Whitepapers](https://cloud.google.com/whitepapers)
  * [Customer stories](https://cloud.google.com/customers)

  * [Industry Solutions](https://cloud.google.com/solutions#industry-solutions)
  * [Retail](https://cloud.google.com/solutions/retail)
  * [Consumer Packaged Goods](https://cloud.google.com/solutions/cpg)
  * [Financial Services](https://cloud.google.com/solutions/financial-services)
  * [Healthcare and Life Sciences](https://cloud.google.com/solutions/healthcare-life-sciences)
  * [Media and Entertainment](https://cloud.google.com/solutions/media-entertainment)
  * [Telecommunications](https://cloud.google.com/solutions/telecommunications)
  * [Games](https://cloud.google.com/solutions/games)
  * [Manufacturing](https://cloud.google.com/solutions/manufacturing)
  * [Supply Chain and Logistics](https://cloud.google.com/solutions/supply-chain-logistics)
  * [Government](https://cloud.google.com/gov)
  * [Education](https://cloud.google.com/edu/higher-education)
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)
  * [See all solutions](https://cloud.google.com/solutions)
  * [Application Modernization](https://cloud.google.com/solutions/camp)
  * [CAMP](https://cloud.google.com/solutions/camp)
  * [Modernize Traditional Applications](https://cloud.google.com/solutions/modernize-traditional-applications)
  * [Migrate from PaaS: Cloud Foundry, Openshift](https://cloud.google.com/solutions/migrate-from-paas)
  * [Migrate from Mainframe](https://cloud.google.com/solutions/mainframe-modernization)
  * [Modernize Software Delivery](https://cloud.google.com/solutions/software-delivery)
  * [DevOps Best Practices](https://cloud.google.com/devops)
  * [SRE Principles](https://cloud.google.com/sre)
  * [Platform Engineering](https://cloud.google.com/solutions/platform-engineering)
  * [Architect for Multicloud](https://cloud.google.com/solutions/architect-multicloud)
  * [Artificial Intelligence](https://cloud.google.com/solutions/ai)
  * [Gemini Enterprise for Customer Experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Gemini Enterprise](https://cloud.google.com/gemini-enterprise)
  * [AI Commerce Search](https://cloud.google.com/gemini-enterprise-cx/commerce)
  * [Google Cloud with Gemini](https://cloud.google.com/ai/gemini)
  * [Physical AI](https://cloud.google.com/solutions/physical-ai)
  * [APIs and Applications](https://cloud.google.com/solutions/apis-and-applications)
  * [New Business Channels Using APIs](https://cloud.google.com/solutions/new-channels-using-apis)
  * [Unlocking Legacy Applications Using APIs](https://cloud.google.com/solutions/unlocking-legacy-applications)
  * [Open Banking APIx](https://cloud.google.com/solutions/open-banking-apix)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [Data Migration](https://cloud.google.com/solutions/data-migration)
  * [Data Lakehouse](https://cloud.google.com/solutions/data-lakehouse)
  * [Real-time Analytics](https://cloud.google.com/solutions/stream-analytics)
  * [Marketing Analytics](https://cloud.google.com/solutions/marketing-analytics)
  * [Datasets](https://cloud.google.com/datasets)
  * [Business Intelligence](https://cloud.google.com/solutions/business-intelligence)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Geospatial Analytics](https://cloud.google.com/solutions/geospatial)
  * [Data Science](https://cloud.google.com/solutions/data-science)
  * [Databases](https://cloud.google.com/solutions/databases)
  * [Database Migration](https://cloud.google.com/solutions/database-migration)
  * [Database Modernization](https://cloud.google.com/solutions/database-modernization)
  * [Databases for Games](https://cloud.google.com/solutions/databases/games)
  * [Google Cloud Databases](https://cloud.google.com/products/databases)
  * [Migrate Oracle workloads to Google Cloud](https://cloud.google.com/solutions/oracle)
  * [Open Source Databases](https://cloud.google.com/solutions/open-source-databases)
  * [SQL Server on Google Cloud](https://cloud.google.com/sql-server)
  * [Gemini for Databases](https://cloud.google.com/products/gemini/databases)
  * [Infrastructure](https://cloud.google.com/solutions/infrastructure-modernization)
  * [Application Migration](https://cloud.google.com/solutions/application-migration)
  * [SAP on Google Cloud](https://cloud.google.com/solutions/sap)
  * [High Performance Computing](https://cloud.google.com/solutions/hpc)
  * [Windows on Google Cloud](https://cloud.google.com/windows)
  * [Data Center Migration](https://cloud.google.com/solutions/data-center-migration)
  * [Active Assist](https://cloud.google.com/solutions/active-assist)
  * [Virtual Desktops](https://cloud.google.com/solutions/virtual-desktops)
  * [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program)
  * [Backup and Disaster Recovery](https://cloud.google.com/solutions/backup-dr)
  * [Red Hat on Google Cloud](https://cloud.google.com/solutions/redhat)
  * [Cross-Cloud Network](https://cloud.google.com/solutions/cross-cloud-network)
  * [AI Infrastructure](https://cloud.google.com/ai-infrastructure)
  * [Productivity and Collaboration](https://workspace.google.com/enterprise/)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security](https://cloud.google.com/solutions/security)
  * [Agentic SOC](https://cloud.google.com/solutions/agentic-soc)
  * [Web App and API Protection](https://cloud.google.com/security/solutions/web-app-and-api-protection)
  * [Security and Resilience Framework](https://cloud.google.com/security/solutions/security-and-resilience)
  * [Risk and compliance as code (RCaC)](https://cloud.google.com/solutions/risk-and-compliance-as-code)
  * [Software Supply Chain Security](https://cloud.google.com/security/solutions/software-supply-chain-security)
  * [Security Foundation](https://cloud.google.com/security/solutions/security-foundation)
  * [Google Cloud Cybershield™](https://cloud.google.com/security/solutions/secops-cybershield)
  * [Startups and SMB](https://cloud.google.com/solutions#section-13)
  * [Startup Program](https://cloud.google.com/startup)
  * [Small and Medium Business](https://cloud.google.com/solutions/smb)
  * [Software as a Service](https://cloud.google.com/saas)

  * Featured Products
  * [Gemini Enterprise app](https://cloud.google.com/gemini-enterprise)
  * [Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Cloud Run](https://cloud.google.com/run)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Looker](https://cloud.google.com/looker)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [See all products (100+)](https://cloud.google.com/products#featured-products)
  * [AI and Machine Learning](https://cloud.google.com/products/ai)
  * [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Gemini Enterprise app](https://cloud.google.com/gemini-enterprise)
  * [Gemini Enterprise for Customer Experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Model Garden](https://console.cloud.google.com/agent-platform/model-garden)
  * [Customer Experience Agent Studio](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [Agent Search](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)
  * [Speech-to-Text](https://cloud.google.com/speech-to-text)
  * [Text-to-Speech](https://cloud.google.com/text-to-speech)
  * [Translation AI](https://cloud.google.com/translate)
  * [Vision AI](https://cloud.google.com/vision)
  * [Contact Center as a Service](https://cloud.google.com/solutions/contact-center-ai-platform)
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)
  * Business Intelligence
  * [Looker](https://cloud.google.com/looker)
  * [Data Studio](https://cloud.google.com/data-studio)
  * [Compute](https://cloud.google.com/products/compute)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [App Engine](https://cloud.google.com/appengine)
  * [Cloud GPUs](https://cloud.google.com/gpu)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Spot VMs](https://cloud.google.com/spot-vms)
  * [Batch](https://cloud.google.com/batch)
  * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
  * [Bare Metal](https://cloud.google.com/bare-metal)
  * [Recommender](https://cloud.google.com/recommender/docs/whatis-activeassist)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)
  * [Containers](https://cloud.google.com/containers)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Deep Learning Containers](https://cloud.google.com/deep-learning-containers/docs)
  * [Knative](https://knative.dev/docs/)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Dataflow](https://cloud.google.com/products/dataflow)
  * [Looker](https://cloud.google.com/looker)
  * [Lakehouse](https://cloud.google.com/products/lakehouse)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Managed Service for Apache Kafka](https://cloud.google.com/products/managed-service-for-apache-kafka)
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)
  * [Databases](https://cloud.google.com/products/databases)
  * [AlloyDB for PostgreSQL](https://cloud.google.com/alloydb)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Firestore](https://cloud.google.com/firestore)
  * [Spanner](https://cloud.google.com/spanner)
  * [Bigtable](https://cloud.google.com/bigtable)
  * [Datastream](https://cloud.google.com/datastream)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Bare Metal Solution](https://cloud.google.com/bare-metal)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Developer Tools](https://cloud.google.com/products/tools)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs)
  * [Cloud SDK](https://cloud.google.com/sdk)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Cloud Source Repositories](https://cloud.google.com/source-repositories/docs)
  * [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs)
  * [Cloud Workstations](https://cloud.google.com/workstations)
  * [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist)
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)
  * [Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * [Google Distributed Cloud Connected](https://cloud.google.com/distributed-cloud-connected)
  * [Google Distributed Cloud Air-gapped](https://cloud.google.com/distributed-cloud-air-gapped)
  * Hybrid and Multicloud
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Cloud Build](https://cloud.google.com/build)
  * [Observability](https://cloud.google.com/products/observability)
  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh)
  * [Google Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * Industry Specific
  * [Anti Money Laundering AI](https://cloud.google.com/anti-money-laundering-ai)
  * [Cloud Healthcare API](https://cloud.google.com/healthcare-api)
  * [Device Connect for Fitbit](https://cloud.google.com/device-connect)
  * [Telecom Network Automation](https://cloud.google.com/telecom-network-automation)
  * [Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric)
  * [Telecom Subscriber Insights](https://cloud.google.com/telecom-subscriber-insights)
  * [Spectrum Access System (SAS)](https://cloud.google.com/products/spectrum-access-system)
  * [Integration Services](https://cloud.google.com/integration-services)
  * [Application Integration](https://cloud.google.com/application-integration)
  * [Workflows](https://cloud.google.com/workflows)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud Tasks](https://cloud.google.com/tasks/docs)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Cloud Data Fusion](https://cloud.google.com/data-fusion)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Eventarc](https://cloud.google.com/eventarc/docs)
  * [Management Tools](https://cloud.google.com/products/management)
  * [Cloud Shell](https://cloud.google.com/shell/docs)
  * [Cloud console](https://cloud.google.com/cloud-console)
  * [Cloud Endpoints](https://cloud.google.com/endpoints/docs)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Cloud APIs](https://cloud.google.com/apis)
  * [Service Catalog](https://cloud.google.com/service-catalog/docs)
  * [Cost Management](https://cloud.google.com/cost-management)
  * [Observability](https://cloud.google.com/products/observability)
  * [Carbon Footprint](https://cloud.google.com/carbon-footprint)
  * [Config Connector](https://cloud.google.com/config-connector/docs/overview)
  * [Active Assist](https://cloud.google.com/solutions/active-assist)
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)
  * [Maps and Geospatial](https://cloud.google.com/solutions/geospatial)
  * [Earth Engine](https://cloud.google.com/earth-engine)
  * [Google Maps Platform](https://mapsplatform.google.com)
  * Media Services
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [Live Stream API](https://cloud.google.com/livestream/docs)
  * [OpenCue](https://www.opencue.io/docs/getting-started/)
  * [Transcoder API](https://cloud.google.com/transcoder/docs)
  * [Video Stitcher API](https://cloud.google.com/video-stitcher/docs)
  * [Migration](https://cloud.google.com/products/cloud-migration)
  * [Migration Center](https://cloud.google.com/migration-center/docs)
  * [Application Migration](https://cloud.google.com/solutions/application-migration)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Cloud Foundation Toolkit](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program)
  * [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/overview)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Networking](https://cloud.google.com/products/networking)
  * [Cloud Armor](https://cloud.google.com/security/products/armor)
  * [Cloud CDN and Media CDN](https://cloud.google.com/cdn)
  * [Cloud DNS](https://cloud.google.com/dns)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing)
  * [Cloud NAT](https://cloud.google.com/nat)
  * [Cloud Connectivity](https://cloud.google.com/hybrid-connectivity)
  * [Network Connectivity Center](https://cloud.google.com/network-connectivity-center)
  * [Network Intelligence Center](https://cloud.google.com/network-intelligence-center)
  * [Network Service Tiers](https://cloud.google.com/network-tiers)
  * [Virtual Private Cloud](https://cloud.google.com/vpc)
  * [Private Service Connect](https://cloud.google.com/private-service-connect)
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)
  * [Operations](https://cloud.google.com/products/operations)
  * [Cloud Logging](https://cloud.google.com/logging)
  * [Cloud Monitoring](https://cloud.google.com/monitoring)
  * [Error Reporting](https://cloud.google.com/error-reporting/docs/grouping-errors)
  * [Managed Service for Prometheus](https://cloud.google.com/managed-prometheus)
  * [Cloud Trace](https://cloud.google.com/trace/docs)
  * [Cloud Profiler](https://cloud.google.com/profiler/docs)
  * [Cloud Quotas](https://cloud.google.com/docs/quotas)
  * Productivity and Collaboration
  * [AppSheet](https://about.appsheet.com/home/)
  * [AppSheet Automation](https://cloud.google.com/appsheet/automation)
  * [Gemini Enterprise app](https://cloud.google.com/gemini-enterprise)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security and Identity](https://cloud.google.com/products/security-and-identity)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection)
  * [Mandiant Managed Defense](https://cloud.google.com/security/products/managed-defense)
  * [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)
  * [Security Command Center](https://cloud.google.com/security/products/security-command-center)
  * [Cloud Key Management](https://cloud.google.com/security/products/security-key-management)
  * [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
  * [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/)
  * [Assured Workloads](https://cloud.google.com/security/products/assured-workloads)
  * [Google Security Operations](https://cloud.google.com/security/products/security-operations)
  * [Mandiant Consulting](https://cloud.google.com/security/consulting/mandiant-services)
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)
  * [Serverless](https://cloud.google.com/serverless)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Functions](https://cloud.google.com/functions)
  * [App Engine](https://cloud.google.com/appengine)
  * [Workflows](https://cloud.google.com/workflows)
  * [API Gateway](https://cloud.google.com/api-gateway/docs)
  * [Storage](https://cloud.google.com/products/storage)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Block Storage](https://cloud.google.com/products/block-storage)
  * [Filestore](https://cloud.google.com/filestore)
  * [Persistent Disk](https://cloud.google.com/persistent-disk)
  * [Cloud Storage for Firebase](https://firebase.google.com/products/storage)
  * [Local SSD](https://cloud.google.com/products/local-ssd)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [Google Cloud Managed Lustre](https://cloud.google.com/products/managed-lustre)
  * [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes)
  * [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery)
  * [Web3](https://cloud.google.com/web3)
  * [Blockchain Node Engine](https://cloud.google.com/blockchain-node-engine)
  * [Blockchain RPC](https://cloud.google.com/products/blockchain-rpc)

  * Save money with our transparent approach to pricing
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)
  * Pricing overview and tools
  * [Google Cloud pricing](https://cloud.google.com/pricing)
  * [Pricing calculator](https://cloud.google.com/products/calculator)
  * [Google Cloud free tier](https://cloud.google.com/free)
  * [Cost optimization framework](https://cloud.google.com/architecture/framework/cost-optimization)
  * [Cost management tools](https://cloud.google.com/cost-management)
  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)

  * Learn & build
  * [Google Cloud Free Program](https://cloud.google.com/free)
  * [Solution Generator](https://cloud.google.com/solution-generator)
  * [Quickstarts](https://cloud.google.com/docs/tutorials?doctype=quickstart)
  * [Blog](https://cloud.google.com/blog)
  * [Learning Hub](https://cloud.google.com/learn)
  * [Google Cloud certification](https://cloud.google.com/certification)
  * [Cloud computing basics](https://cloud.google.com/discover)
  * [Cloud Architecture Center](https://cloud.google.com/architecture)
  * Connect
  * [Innovators](https://cloud.google.com/innovators/innovatorsplus)
  * [Developer Center](https://cloud.google.com/developers)
  * [Events and webinars](https://cloud.google.com/events)
  * [Google Cloud Community](https://discuss.google.dev/c/google-cloud/14)
  * Consulting and Partners
  * [Google Cloud Consulting](https://cloud.google.com/consulting)
  * [Google Cloud Marketplace](https://cloud.google.com/marketplace)
  * [Find a partner](https://cloud.google.com/partners)
  * [Google Cloud partners](https://partners.cloud.google.com)
