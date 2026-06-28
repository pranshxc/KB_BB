---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-10_fabricio-api-permission-apocalypse-privilege-escalations.md
original_filename: 2017-07-10_fabricio-api-permission-apocalypse-privilege-escalations.md
title: Fabric.io API permission apocalypse – Privilege Escalations
category: documents
detected_topics:
- mobile-security
- access-control
- cloud-security
- xss
- command-injection
- otp
tags:
- imported
- documents
- mobile-security
- access-control
- cloud-security
- xss
- command-injection
- otp
language: en
raw_sha256: f42fd8fbf300d864ce568a836e7aef9bd1a2bbb809b20af6bc4e0e53b658a1d3
text_sha256: b314c528b4aa88c0404254c93e9955fad3b48a10e0aa7c8c9526631290746d3a
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# Fabric.io API permission apocalypse – Privilege Escalations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-10_fabricio-api-permission-apocalypse-privilege-escalations.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, cloud-security, xss, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `f42fd8fbf300d864ce568a836e7aef9bd1a2bbb809b20af6bc4e0e53b658a1d3`
- Text SHA256: `b314c528b4aa88c0404254c93e9955fad3b48a10e0aa7c8c9526631290746d3a`


## Content

---
title: "Fabric.io API permission apocalypse – Privilege Escalations"
page_title: "Fabric.io API Permission Apocalypse - Privilege Escalation - WeSecureApp"
url: "https://wesecureapp.com/blog/fabric-io-api-permission-apocalypse-privilege-escalations"
final_url: "https://wesecureapp.com/blog/fabric-io-api-permission-apocalypse-privilege-escalations/"
authors: ["WeSecureApp (@wesecureapp)"]
programs: ["Twitter"]
bugs: ["Broken authorization", "Account takeover"]
publication_date: "2017-07-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6157
---

[](javascript:;)

  * [Home](https://wesecureapp.com/)
  * [Services](https://wesecureapp.com/services/)
  * [Application Security](https://wesecureapp.com/services/application-security/)
  * [Web Application VAPT](https://wesecureapp.com/vulnerability-assessment-and-penetration-testing/)
  * [Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  * [Network Security](https://wesecureapp.com/services/network-security/)
  * [Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  * [Cloud Security](https://wesecureapp.com/services/cloud-security/)
  * [Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  * [Breach & Attack Simulation](https://wesecureapp.com/services/breach-attack-simulation/)
  * [Red Team Assessment](https://wesecureapp.com/services/breach-attack-simulation/red-team-assessment/)
  * [Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [Social Engineering](https://wesecureapp.com/services/breach-attack-simulation/social-engineering/)
  * [Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  * [Staffing Services](https://wesecureapp.com/services/staffing-services/)
  * [Smart Shore Sourcing](https://wesecureapp.com/services/staffing-services/smart-shore-sourcing/)
  * [Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  * [Solutions](https://wesecureapp.com/solutions/)
  * [Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [DevsecOps](https://wesecureapp.com/footer/devsecops-themepage/)
  * [Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Case studies](https://wesecureapp.com/resources/case-studies/)
  * [White Papers](https://wesecureapp.com/resources/white-papers/)
  * [Datasheets](https://wesecureapp.com/resources/datasheets/)
  * [Events](https://wesecureapp.com/resources/events/)
  * [Podcast](https://wesecureapp.com/resources/podcast/)
  * [Company](https://wesecureapp.com/company/)
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Careers](https://wesecureapp.com/?page_id=15291)
  * [Contact](https://wesecureapp.com/contact/)

[ ![WeSecureApp Logo \(2\)](https://wesecureapp.com/wp-content/uploads/2020/08/WeSecureApp-Logo-2.svg) ](https://wesecureapp.com/)

  * Services
  *  * [Application Security](/services/application-security/)
  *  * SERVICES
  * [![application security](https://wesecureapp.com/wp-content/uploads/2020/09/application.svg)Web Application Penetration Testing](https://wesecureapp.com/services/application-security/web-app-pentest/)
  * [![Mobile Application Penetration Test](https://wesecureapp.com/wp-content/uploads/2020/09/mobile_phone-1.svg)Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [![Web Services & API Assessment](https://wesecureapp.com/wp-content/uploads/2020/09/touch-1.svg)Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [![threat-modelling](https://wesecureapp.com/wp-content/uploads/2024/03/threat-modelling.svg)Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [![application security - secure code review](https://wesecureapp.com/wp-content/uploads/2020/09/code-syntax-1.svg)Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [![application architecture review](https://wesecureapp.com/wp-content/uploads/2024/03/application-architecture-review.svg)Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  *  * RESOURCES
  * [ ![cyber security measures](https://wesecureapp.com/wp-content/uploads/2018/12/Web-1920-–-11-1.png) Top 7 cyber security measures that enterprises shouldn’t neglect](https://wesecureapp.com/blog/top-7-cyber-security-measures-that-enterprises-shouldnt-neglect/)
  * [Network Security](/services/network-security/)
  *  * SERVICES
  * [![network-1](https://wesecureapp.com/wp-content/uploads/2020/09/network-1-1.svg)Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [![Group 16753 \(1\)](https://wesecureapp.com/wp-content/uploads/2024/03/Group-16753-1.svg)Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [![telephone \(1\)](https://wesecureapp.com/wp-content/uploads/2020/09/telephone-1.svg)VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [![wireless_modem \(1\)](https://wesecureapp.com/wp-content/uploads/2020/09/wireless_modem-1.svg)Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  *  * RESOURCES
  * [![penetration testing companies in the USA](https://wesecureapp.com/wp-content/uploads/2021/07/bg.png)Top 7 Penetration Testing Companies in the USA](https://wesecureapp.com/blog/top-7-penetration-testing-companies-in-the-usa/)
  * [Cloud Security](/services/cloud-security/)
  *  * SERVICES
  * [![Aws](https://wesecureapp.com/wp-content/uploads/2020/09/Aws-1.svg)Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [![cloud-pentesing-icon](https://wesecureapp.com/wp-content/uploads/2024/03/cloud-pentesing-icon.svg)Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  *  * RESOURCES
  * [ ![Cloud Security Threats](https://wesecureapp.com/wp-content/uploads/2021/02/Cloud_Security-_Threats-1.jpg) Cloud Security Threats](https://wesecureapp.com/blog/cloud-security-threats/)
  * [Breach & Attack Simulation](/services/threat-simulation/)
  *  * SERVICES
  * [![global-security](https://wesecureapp.com/wp-content/uploads/2020/09/global-security-1.svg)Red Team Assessment](/services/threat-simulation/red-team-assessment/)
  * [![dark-web](https://wesecureapp.com/wp-content/uploads/2024/03/dark-web.svg)Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [![ransomware simulation](https://wesecureapp.com/wp-content/uploads/2024/03/ransomware-simulation.svg)Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [![insights-1](https://wesecureapp.com/wp-content/uploads/2020/09/insights-1-1.svg)Social Engineering Assessment](/services/threat-simulation/social-engineering/)
  * [![assume-breach-icon](https://wesecureapp.com/wp-content/uploads/2023/06/assume-breach-icon.svg)Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  *  * RESOURCES
  * [![Hire a Red Team](https://wesecureapp.com/wp-content/uploads/2022/01/Tinted-Bg-2-1-–-2.png)7+ Major Reasons to Hire a Red Team to Harden Your App Sec](https://wesecureapp.com/blog/7-major-reasons-to-hire-a-red-team-to-harden-your-app-sec/)
  * [Staffing Services](/services/staffing-services/)
  *  * SERVICES
  * [![smart-shore-source](https://wesecureapp.com/wp-content/uploads/2023/05/smart-shore-source.svg)Smart Shore Sourcing](https://wesecureapp.com/services-staffing-services-smart-shore-sourcing/)
  * [![virtual-ciso](https://wesecureapp.com/wp-content/uploads/2024/03/virtual-ciso.svg)Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  *  * RESOURCES
  * [ ![selecting-penetrationtesting](https://wesecureapp.com/wp-content/uploads/2021/03/selecting-penetrationtesting.jpg) How to Choose a Penetration Testing Vendor Wisely?](https://wesecureapp.com/blog/selecting-a-penetration-testing-vendor/)
  * Solutions
  *  * MANAGED SECURITY
  * [![vmaas](https://wesecureapp.com/wp-content/uploads/2024/03/vmaas.svg)Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [![vraas](https://wesecureapp.com/wp-content/uploads/2024/03/vraas.svg)Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [![tiaas](https://wesecureapp.com/wp-content/uploads/2024/03/tiaas.svg)Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [![devsecops-logo](https://wesecureapp.com/wp-content/uploads/2021/04/devsecops-logo-1.svg)DevSecOps](https://wesecureapp.com/solutions/devsecops/)
  * [![SSS-logo](https://wesecureapp.com/wp-content/uploads/2021/04/SSS-logo.svg)Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  *  * RESOURCE
  * [![worst passwords](https://wesecureapp.com/wp-content/uploads/2021/06/Tinted-Bg-5-1-–-22.png)World’s Worst Passwords: Is it time to change yours?](https://wesecureapp.com/blog/worlds-worst-passwords-is-it-time-to-change-yours/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Datasheets](/resources/datasheets/)
  * [Case Studies](/resources/case-studies/)
  * [Whitepapers](/resources/white-papers/)
  * [Podcasts](https://wesecureapp.com/resources/podcast/)
  * [Events](https://wesecureapp.com/resources/events/)
  * Company
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Contact](https://wesecureapp.com/contact/)

  * [Home](https://wesecureapp.com/)
  * [Services](https://wesecureapp.com/services/)
  * [Application Security](https://wesecureapp.com/services/application-security/)
  * [Web Application VAPT](https://wesecureapp.com/vulnerability-assessment-and-penetration-testing/)
  * [Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  * [Network Security](https://wesecureapp.com/services/network-security/)
  * [Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  * [Cloud Security](https://wesecureapp.com/services/cloud-security/)
  * [Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  * [Breach & Attack Simulation](https://wesecureapp.com/services/breach-attack-simulation/)
  * [Red Team Assessment](https://wesecureapp.com/services/breach-attack-simulation/red-team-assessment/)
  * [Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [Social Engineering](https://wesecureapp.com/services/breach-attack-simulation/social-engineering/)
  * [Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  * [Staffing Services](https://wesecureapp.com/services/staffing-services/)
  * [Smart Shore Sourcing](https://wesecureapp.com/services/staffing-services/smart-shore-sourcing/)
  * [Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  * [Solutions](https://wesecureapp.com/solutions/)
  * [Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [DevsecOps](https://wesecureapp.com/footer/devsecops-themepage/)
  * [Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Case studies](https://wesecureapp.com/resources/case-studies/)
  * [White Papers](https://wesecureapp.com/resources/white-papers/)
  * [Datasheets](https://wesecureapp.com/resources/datasheets/)
  * [Events](https://wesecureapp.com/resources/events/)
  * [Podcast](https://wesecureapp.com/resources/podcast/)
  * [Company](https://wesecureapp.com/company/)
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Careers](https://wesecureapp.com/?page_id=15291)
  * [Contact](https://wesecureapp.com/contact/)

Hamburger Toggle Menu

[Schedule a Meeting](https://meetings.hubspot.com/strobes/wesecureapp)

[Application Security](https://wesecureapp.com/blog/category/application-security/) · [Web Services & API Security](https://wesecureapp.com/blog/category/web-services-api-security/) · [Write-up](https://wesecureapp.com/blog/category/write-up/)

# Fabric.io API Permission Apocalypse – Privilege Escalations

By user

### What Is Fabric.io?

The Fabric platform is made of three modular kits that address some of the most common and pervasive challenges that all app developers face: stability, distribution, revenue and identity. It combines the services of Crashlytics, MoPub, Twitter and others to help you build more stable apps, generate revenue through the world’s largest mobile ad exchange and enable you to tap into Twitter’s sign-in systems and rich streams of real-time content for greater distribution and simpler identity. And Fabric was built with ease of use in mind.

### In Short:

Using fabric SDK one could embed Crashlytics, Login with twitter into their Android/IOS application. Users can manage/track reports from their dashboard at <https://fabric.io/dashboard>.

### The Apocalypse:

We have been testing Fabric.io since it’s release. And we came across a few XSS vulnerabilities , insecure Storage vulnerabilties(**[Android App](https://wesecureapp.com/blog/a-5-step-checklist-to-securing-your-mobile-apps/)**) and many **_privilege escalations._** Using this vulnerability one could takeover any organization in fabric.io.

### Vulnerability Description:

**While in dashboard we could see two type of users:**

  * Admin – Can Delete Apps, Add members, Delete Members
  * Member- Cannot Delete Apps, Cannot Add Members, Cannot Delete Members

On logging into Fabric.io every user gets an access token, this access token along with session cookies are used to authenticate every request. So we checked if the member’s access token can be used to perform admin requests.

We intercepted a delete request from the admin’s profile , Replaced the access token ( X-CRASHLYTICS-DEVELOPER-TOKEN: ) with member’s access token along with the member’s session cookie.

The request looks like:
  
  
  DELETE /api/v2/organizations/5460d2394b793294df01104a/apps/5496f78544e4b4145000034c HTTP/1.1
  Host: www.fabric.io
  Connection: keep-alive
  Accept: application/json, text/javascript, /; q=0.01
  Origin: <https://www.fabric.io>
  X-CSRF-Token: 06MzlRvMNizNQLk9VZWk5pb3LU6PUagNLPdGFQ4HdOg=
  X-Requested-With: XMLHttpRequest
  X-CRASHLYTICS-DEVELOPER-TOKEN: ***REDACTED-SUSPECT-TOKEN***  User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
  Referer: <https://www.fabric.io/settings/apps>
  Accept-Encoding: gzip, deflate, sdch
  Accept-Language: en-US,en;q=0.8
  Cookie:
  

Upon sending the above request we got a `200` status as response and the application was successfully deleted.  
We have tried doing the same thing on few other requests :  
Adding a user, give admin permission , remove users  
Sadly all the requests were vulnerable!

Using this vulnerability a attacker with normal member privileges could have made himself an admin and could have taken over that organization.

### Root Cause:

The access tokens issued to the users are bind with scope. A normal user with access token xyz and scope: member_only shouldn’t be able to perform admin actions.  
Applications should properly check the scope of the access token before completing any of the requests sent by the user.

_*_ Fabric.io is a twitter acquisition and twitter runs a bug bounty program on <https://hackerone.com/twitter>.  
We have reported all the above mentioned vulnerabilities to twitter and they have been fixed accordingly.  
As of now we are holding the 2nd place on twitter’s hall of fame, you can check us out at <https://hackerone.com/twitter/thanks>.

  

[fabric.io](https://wesecureapp.com/blog/tag/fabric-io/)[vulnerabilities](https://wesecureapp.com/blog/tag/vulnerabilities/)[vulnerability](https://wesecureapp.com/blog/tag/vulnerability/)

  

### Related Articles

  

[](https://wesecureapp.com/blog/why-wesecureapp-rocks-at-busting-payment-tampering-vulnerabilities/) ![data breaches in december](https://wesecureapp.com/wp-content/uploads/2024/01/Tinted-Bg-1-–-2-610x610.png)

[BFSI](https://wesecureapp.com/blog/category/bfsi/) · [Cyber Security](https://wesecureapp.com/blog/category/cyber-security/) · [vulnerabilities](https://wesecureapp.com/blog/category/vulnerabilities/)

###### [Why WeSecureApp Rocks at Busting Payment Tampering Vulnerabilities](https://wesecureapp.com/blog/why-wesecureapp-rocks-at-busting-payment-tampering-vulnerabilities/ "Why WeSecureApp Rocks at Busting Payment Tampering Vulnerabilities")

### Leave A Reply [Cancel reply](/blog/fabric-io-api-permission-apocalypse-privilege-escalations/#respond)

Your email address will not be published. Required fields are marked *

Comment

Name *

Email *

Website

Save my name, email, and website in this browser for the next time I comment.

[ ![cross site scripting](https://wesecureapp.com/wp-content/uploads/2017/07/Tinted-Bg-6-1-–-30-610x610.png) XSS by Tossing Cookies Next Article  ](https://wesecureapp.com/blog/xss-by-tossing-cookies/)

  

### Industries

[BFSI](/industries/banking/)

[Healthcare](/industries/healthcare/)

[Government](/industries/government/)

[Retail & eCommerce](/industries/retail-ecommerce/)

[Information Technology](/industries/information-technology)

[Telecommunications](/industries/telecommunications)

### SERVICES

[Application Security](/services/application-security/)

[Network Security](/services/network-security/)

[Cloud Security](/services/cloud-security/)

[Staffing Services](https://wesecureapp.com/services/staffing-services/)

[Threat Simulation](/services/threat-simulation/)

[CERT-In Audit Services](https://wesecureapp.com/services/cert-in-audit/)

### SOLUTIONS

[Managed Security](/solutions/enterprise-security/managed-security/)

[Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)

[Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)

[Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)

[Strategic Security Solutions](/solutions/strategic-security-solutions/)

### resources

[Blog](/blog/)

[Datasheets](/resources/datasheets/)

[Case studies](/resources/case-studies/)

[Podcasts](/resources/podcast/)

[Events](https://wesecureapp.com/resources/events/)

### company

[About](/company/about-us/)

[Partners](/company/partners/)

[CERT-InNew](/certin/)

[White papers](/resources/white-papers/)

[Contact](/contact)

[Privacy Policy](/privacy-policy)

### WE ARE CERTIFIED

[ ![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2024/04/cert-inlogo.jpg) ](https://www.trustpilot.com/review/wesecureapp.com)

[ ![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2024/04/img-strobes-certifications.png) ](https://www.trustpilot.com/review/wesecureapp.com)

[![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2021/09/trustpilot-black.svg)](https://www.trustpilot.com/review/wesecureapp.com)

[![GoodFirms Badge](https://assets.goodfirms.co/badges/blue-button/view-profile.svg)](https://www.goodfirms.co/company/wesecureapp)

[ ![clutch_review](https://wesecureapp.com/wp-content/uploads/2021/09/clutch.png) ](https://clutch.co/review/1737852)
