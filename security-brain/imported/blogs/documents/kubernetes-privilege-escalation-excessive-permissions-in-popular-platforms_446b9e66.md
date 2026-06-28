---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-17_kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms.md
original_filename: 2022-05-17_kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms.md
title: 'Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms'
category: documents
detected_topics:
- access-control
- cloud-security
- command-injection
- supply-chain
tags:
- imported
- documents
- access-control
- cloud-security
- command-injection
- supply-chain
language: en
raw_sha256: 446b9e667751d538b4cff85226431eed00c5b9228b00feaca5017993266dbd08
text_sha256: a7b6f39b7676a93a9a4dc1e1113090189c0b15b4b5e60ede6aec066549c01cc8
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-17_kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms.md
- Source Type: markdown
- Detected Topics: access-control, cloud-security, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `446b9e667751d538b4cff85226431eed00c5b9228b00feaca5017993266dbd08`
- Text SHA256: `a7b6f39b7676a93a9a4dc1e1113090189c0b15b4b5e60ede6aec066549c01cc8`


## Content

---
title: "Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms"
page_title: "Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms - Palo Alto Networks"
url: "https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms"
final_url: "https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms"
authors: ["Yuval Avrahami (@yuval_avrahami)", "Shaul Ben Hai"]
programs: ["Google", "AWS", "Microsoft", "Red Hat"]
bugs: ["Privilege escalation", "Broken Access Control", "Kubernetes"]
bounty: "13,022"
publication_date: "2022-05-17"
added_date: "2023-01-27"
source: "pentester.land/writeups.json"
original_index: 2635
---

[ Introducing Idira, the next-generation identity security platform.  ](/idira)

[](/)

  * Sign In
  * Customer
  * Partner
  * Employee
  * [Login to download](/login)
  * [Join us to become a member](/login?screenToRender=traditionalRegistration)

  * EN

  * ![magnifying glass search icon to open search field](/etc/clientlibs/clean/imgs/search-black.svg)

  * [ Contact Us](/company/contact-sales)
  * [ What's New](/resources)
  * [ Get Support](https://support.paloaltonetworks.com/SupportAccount/MyAccount)
  * [ Under Attack?](https://start.paloaltonetworks.com/contact-unit42.html)

[ ![Palo Alto Networks logo](/etc/clientlibs/clean/imgs/pan-logo-dark.svg) ](/) ![magnifying glass search icon](/etc/clientlibs/clean/imgs/search-black.svg)

  * [](/)
  * Products
  * Solutions
  * Services
  * Partners
  * Company
  * More

  * Sign In

Sign In

  * Customer
  * Partner
  * Employee
  * [Login to download](/login)
  * [Join us to become a member](/login?screenToRender=traditionalRegistration)

  * EN

Language

  * [Contact Us](/company/contact-sales)
  * [What's New](/resources)
  * [Get support](https://support.paloaltonetworks.com/SupportAccount/MyAccount)
  * [Under Attack?](https://start.paloaltonetworks.com/contact-unit42.html)

  * [Demos and Trials](/get-started)

* * *

![asset thumbnail](/content/dam/pan/en_US/assets/pdf/white-papers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms.pdf.transform/resourceRedesign/image.png)

Whitepaper

May 17, 2022

#  Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms

Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms

[ English ](javascript:;)

[Show me the research __](/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms)

[Show me the research __](/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms)

Kubernetes threat actors are growing more sophisticated, and are beginning to target excessive permissions and Role-Based Access Control (RBAC) misconfigurations. To understand the real-world impact of excessive permissions, Prisma Cloud researchers analyzed popular Kubernetes platforms - distributions, managed services, and common add-ons - to identify widespread infrastructure components that run with powerful permissions. In 62.5% of the Kubernetes platforms reviewed, privileged credentials were distributed across every node in the cluster. As a result, in half of the platforms examined, a single container escape was enough to take over the entire cluster.­­

Get your copy of the whitepaper to learn about:­

  * Privilege escalation attacks in Kubernetes.
  * The real blast radius of container escapes.
  * How to evaluate and strengthen your RBAC posture.
  * A newly released open-source tool that can identify risky permissions and privilege escalation paths in your clusters.

[ ](mailto:?subject=Kubernetes%20Privilege%20Escalation%3A%20Excessive%20Permissions%20in%20Popular%20Platforms&body=Kubernetes%20threat%20actors%20are%20growing%20more%20sophisticated%20with%20their%20attack%20techniques%2C%20including%20beginning%20to%20target%20Role-Based%20Access%20Control%20%28RBAC%29%20misconfigurations.%20at%20https%3A//www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms)

Related Resources

Access a wealth of educational materials, such as datasheets, whitepapers, critical threat reports, informative cybersecurity topics, and top research analyst reports 

[See all resources __](/resources)

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
  * [ Product Certifications ](/legal-notices/trust-center/certifications)
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
