---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-02_cloud-firewall-management-api-snafu-put-500k-sonicwall-customers-at-risk.md
original_filename: 2020-09-02_cloud-firewall-management-api-snafu-put-500k-sonicwall-customers-at-risk.md
title: Cloud firewall management API SNAFU put 500k SonicWall customers at risk
category: documents
detected_topics:
- idor
- mobile-security
- sso
- jwt
- access-control
- ssrf
tags:
- imported
- documents
- idor
- mobile-security
- sso
- jwt
- access-control
- ssrf
language: en
raw_sha256: d968cc55c8fe8481fa90f649b5d5917cfd2c376d36448aca6e6624e3dc41804f
text_sha256: d11e46d6c81fff73758f1077bd6659a9bc9f3dc7dfe1ac6d9ded9513c683ecbb
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# Cloud firewall management API SNAFU put 500k SonicWall customers at risk

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-02_cloud-firewall-management-api-snafu-put-500k-sonicwall-customers-at-risk.md
- Source Type: markdown
- Detected Topics: idor, mobile-security, sso, jwt, access-control, ssrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `d968cc55c8fe8481fa90f649b5d5917cfd2c376d36448aca6e6624e3dc41804f`
- Text SHA256: `d11e46d6c81fff73758f1077bd6659a9bc9f3dc7dfe1ac6d9ded9513c683ecbb`


## Content

---
title: "Cloud firewall management API SNAFU put 500k SonicWall customers at risk"
page_title: "Cloud firewall management API SNAFU put 500k SonicWall customers at risk | Pen Test Partners"
url: "https://www.pentestpartners.com/security-blog/cloud-firewall-management-api-snafu-put-500k-sonicwall-customers-at-risk/"
final_url: "https://www.pentestpartners.com/security-blog/cloud-firewall-management-api-snafu-put-500k-sonicwall-customers-at-risk/"
authors: ["Vangelis Stykas (@evstykas)"]
programs: ["SonicWall"]
bugs: ["IDOR"]
publication_date: "2020-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4283
---

[Home](/)

Services ▾

Test and Simulate ▾

[Penetration Testing (CHECK)](https://www.pentestpartners.com/service/penetration-testing/)

[Pen Testing as a Service (PTaaS)](https://www.pentestpartners.com/service/pen-testing-as-a-service-ptaas/)

[Artificial Intelligence Testing](https://www.pentestpartners.com/service/artificial-intelligence-testing/)

[Red Teaming (CBEST, GBEST, STAR-FS, TIBER)](https://www.pentestpartners.com/service/red-teaming-cbest-gbest-star-fs-tiber/)

[Purple Teaming](https://www.pentestpartners.com/service/purple-teaming/)

[Attack Surface Assessment](https://www.pentestpartners.com/service/attack-surface-assessment/)

[Attack Surface Management](https://www.pentestpartners.com/service/attack-surface-management-asm/)

[Cloud Testing Services](https://www.pentestpartners.com/service/cloud-testing-services/)

[Physical Security Testing](https://www.pentestpartners.com/service/physical-security-testing/)

[OT, ICS, IIot Security Testing](https://www.pentestpartners.com/service/ot-ics-iiot-security-testing/)

[Transport Systems Testing ](https://www.pentestpartners.com/service/transport-systems-testing/)

Detect and Respond ▾

[Incident Response](https://www.pentestpartners.com/service/incident-response/)

[ Incident Response Maturity Assessment](https://www.pentestpartners.com/service/incident-response-maturity-assessment/)

[Digital Forensic Investigations](https://www.pentestpartners.com/service/digital-forensic-investigations/)

[Digital Forensics Expert Witness](https://www.pentestpartners.com/service/digital-forensics-expert-witness/)

[Dark Web Annual OSINT Assessment](https://www.pentestpartners.com/service/dark-web-annual-monitoring-osint-assessment/)

[Exposure and Identity Risk Assessment](https://www.pentestpartners.com/service/exposure-and-identity-risk-assessment/)

[Managed Detection & Response](https://www.pentestpartners.com/service/managed-detection-response/)

[Compromise Assessments and Forensic Sweep](https://www.pentestpartners.com/service/compromise-assessment/)

Improve and Protect ▾

[Security Architecture](https://www.pentestpartners.com/service/security-architecture/)

[Secure Software Development (SDLC)](https://www.pentestpartners.com/service/secure-software-development-sdlc/)

[Cloud Configuration and Best Practice](https://www.pentestpartners.com/service/cloud-configuration-and-best-practice/)

[Cyber Security Gap Analysis](https://www.pentestpartners.com/service/cyber-security-gap-analysis/)

[Cyber Security Maturity Assessment (CSMA)](https://www.pentestpartners.com/service/cyber-security-maturity-assessment-csma/)

[Security Training](https://www.pentestpartners.com/service/security-training/)

[Third-party Vendors Selection and Assurance](https://www.pentestpartners.com/service/third-party-vendors-selection-and-assurance/)

[Virtual CISO](https://www.pentestpartners.com/service/virtual-ciso/)

[Proactive Advanced Password Auditor (Papa)](https://www.pentestpartners.com/service/proactive-advanced-password-auditor-papa/)

Comply ▾

[Cyber Essentials and Cyber Essentials Plus](https://www.pentestpartners.com/service/cyber-essentials-cyber-essentials-plus/)

[Formal Certification Preparation](https://www.pentestpartners.com/service/formal-certification-preparation/)

[PCI ROC Level 1 Assessment](https://www.pentestpartners.com/service/pci-roc-level-1-assessment/)

[PCI SAQ Assessment](https://www.pentestpartners.com/service/pci-saq-assessment/)

[PCI Scoping Workshop](https://www.pentestpartners.com/service/pci-scoping-workshop/)

Industries ▾

[Finance](https://www.pentestpartners.com/security-blog/industries/finance/)

[Healthcare](https://www.pentestpartners.com/security-blog/industries/healthcare/)

[Retail & Consumer](https://www.pentestpartners.com/security-blog/industries/retail-and-consumer/)

[Transport](https://www.pentestpartners.com/security-blog/industries/transport/)

About Us ▾

[About Us](https://www.pentestpartners.com/about-us/)

[In the News](https://www.pentestpartners.com/about-us/in-the-news/)

[Our Team](https://www.pentestpartners.com/about-us/meet-the-team/)

[Careers](https://www.pentestpartners.com/about-us/careers/)

[Vulnerability Disclosure Policy](https://www.pentestpartners.com/about-us/vulnerability-disclosure-policy/)

[Our Vision & Values](https://www.pentestpartners.com/our-vision-and-values/)

[Blog](/security-blog/)

[Videos](/hack-demo-videos/)

[Events](/events-and-speaking/)

[Contact Us](/contact-us/)

![Cloud firewall management API SNAFU put 500k SonicWall customers at risk](https://www.pentestpartners.com/wp-content/uploads/2024/09/swall-headline-captioned.png)

  * Security Blog 
  * Vulnerabilities and Disclosures 

# Cloud firewall management API SNAFU put 500k SonicWall customers at risk

###  Vangelis Stykas 

**02 Sep 2020** 65 Min Read 

  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/linkedin-icon-footer.svg) ](https://www.linkedin.com/company/pen-test-partners/)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/x-icon-footer.svg) ](https://x.com/PentestPartners)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/youtube-icon-footer.svg) ](https://www.youtube.com/channel/UC2HCAhj6JiOsV_PcMFrjykw)

Also on this page ▾

  * Related services
  * Related blogs

### TL;DR

  * I found an IDOR in SonicWall’s cloud management platform API
  * **Any** user could add themselves to **any** account at **any** organisation using it
  * Anyone could create a user account to exploit the issue, from the public internet
  * Can be used to change firewall rules, or add rogue VPN users, for example
  * Results in **trivial compromise** of ~500K orgs, ~2 million user groups and ~10 million devices
  * Where SonicWall is used for SSO, results in compromise of 3rd party systems too
  * Not clear how long it was vulnerable for, but took SonicWall 14 days to fix the issue…  
…during which time they left the offending API request available, exposing all customers

Potential for injecting ransomware was significant.

Irony of a security vendor making clients more vulnerable is not lost on us!

### Let’s begin

SonicWall is a significant provider of security appliances, primarily firewalls, UTM, VPNs and content control.

During a recent test, I was investigating the cloud management functionality of a client firewall and other SonicWall devices through the mysonicwall.com cloud.

I found a security issue so serious that we then spent £££ on our own SonicWall products in order to independently validate the issue, to be certain it wasn’t just our client that was affected.

What I discovered was a trivial method to compromise every single cloud managed device attached to mysonicwall.com, affecting around 1.9 million user groups across hundreds of thousands of organisations. At least 10 million individual devices were affected.

The vulnerability, an insecure direct object reference in the ‘partyGroupID’ API request, allowed any user to be added to _any_ group at _any_ organization. All I needed was my own account and I could add it to anyone else’s group through the public cloud service.

Using this degree of access, one could modify firewall rules and/or VPN access, giving oneself remote access in to any organization. One could inject ransomware, or any manner of other attacks should one so wish. That’s a breach of customer networks directly as a result of their security products. The irony is not lost on me!

Disclosure was initially very positive, then went rapidly downhill as SonicWall procrastinated with a fix and refused to take down the vulnerable functionality in the meantime, knowingly leaving their customers exposed for a full 17 days.

### The vulnerability

An insecure direct object reference vulnerability was found in the users/add-user API endpoint for the SonicWall GMS application. This could allow a normal authenticated user to manipulate a parameter and gain access to any user group in any tenant.

When inviting a new user, a call is made to the api/users/add-user endpoint. Amongst other parameters, this call includes a partyGroupId parameter. This number appears to be a sequential integer which is unique to any group in any tenant.

This parameter will add the user in the request to the resultant group. A check is made whether the emailAddress parameter is allowed, but this only works if the emailAddress is the same as that in the JWT used for authorisation. If the emailAddress is changed to a new or existing user, but is not the same as in the JWT then the user will be added to the partyGroupId group.

As the partyGroupId parameter is a 7-digit integer it is possible to perform a brute force attack and gain access to other groups.

The partyGroupId parameter appears to be unique globally and can reference groups in any tenant. This could give access to all devices of another tenant.

An example request can be seen below where a throw-away user is created to have very basic access:

Request:
  
  
  Request:
  POST /api/users/add-user?emailAddress=[[email protected]](/cdn-cgi/l/email-protection)&firstName=Vangelis&lastName=Stykas1&partyGroupId=1644147&contactTypeId=10001&bskipResellerCustomerValidation=false HTTP/1.1
  Host: api.mysonicwall.com
  Connection: close
  Content-Length: 2
  Accept: application/json, text/plain, */*
  Origin: https://www.mysonicwall.com
  Authorization: Bearer ***REDACTED***
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36
  Content-Type: application/json
  Referer: https://www.mysonicwall.com/workspace/m/feature/user-groups?mode=APP
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9
  
  {}

The highlighted parameters can be tampered with. This attack could easily be scripted and run from a simple curl script.

As noted, the emailAddress in the parameters is egw**12** @mailinator.com whereas the email address in the JWT is “egw**11** @mailinator.com”.

This will respond with:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc1.png)

This can be run through a simple curl command:
  
  
  curl -i -s -k -X

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  POST' \
  -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Host: api.mysonicwall.com' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Accept: application/json, text/plain, */*' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Accept-Language: en-GB,en;q=0.5' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Accept-Encoding: gzip, deflate' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Authorization: Bearer ***REDACTED*** -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Origin: https://www.mysonicwall.com' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Connection: close' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Referer: https://www.mysonicwall.com/workspace/m/feature/user-group?mode=APP' -H

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  Content-Length: 2' \
  --data-binary

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  {}' \

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

  
  
  https://api.mysonicwall.com/api/users/add-user?emailAddress=sonicwall1@█████████.org.uk&firstName=David&lastName=█████&partyGroupId=1644147&contactTypeId=10001&bskipResellerCustomerValidation=false'

This will make it possible to simply script an attack

Once the user has been added then they will have access to that usergroup; in the examples above, this has given access to the following:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc2.png)

From here it is possible to perform user administration, including removing valid users:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc3.png)

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc4.png)

As permissions have been obtained it should be possible to access all licensed options for that tenant.

This includes obtaining the list of users for that company:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc5.png)

(the same page allows deleting of current users)

And the company’s details. This is our own account:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc6-1.png)

Through services it is possible to control the company’s devices, including the firewall rules and logs:

![](https://www.pentestpartners.com/wp-content/uploads/2020/08/swallvulndisc7.png)

Compromise is now complete. Depending on the features the client has paid for, one would have access to configure:

  * Routers
  * Firewalls
  * VPN (adding a VPN user and having access to the internal network)
  * Security reports
  * Traffic analytics
  * VoIP and potentially toll fraud
  * Internal wireless networks
  * Web application firewalls
  * Cloud app security controls
  * Anti-spam and content filters

### Disclosure

Following the vulnerability disclosure process at <https://psirt.global.sonicwall.com/vuln-policy>, we emailed a report to [[email protected]](/cdn-cgi/l/email-protection) on the morning of **August 13th**.

This was acknowledged about **45 minutes later** with a personal reply. We strongly urged SonicWall to take down the affected service whilst a fix was implemented, given the degree of customer exposure

About **12 hours later** we had an update, confirming the vulnerability existed. **This is good!**

“We have validated your report and submitted to our remediation team to fix the issue.  
And if you keep it confidential until we patch it, you and Pentest Partners will be credited on our vulnerabilities Hall of Fame page.”

But no reference to a timeline to fix. After hearing **nothing for 6 days** , I asked the question directly:

“Could you please urgently confirm when you intend to fix this issue, given it exposes every one of your customers using the SonicWall cloud service and should be straightforward to resolve?”

And received this reply:

“Please be patient, our team is still working on fixing the issue. We will let you know once the issue is patched.”

This is a trivial IDOR in an API, not a complex RCE in the firewall OS. Other API requests were correctly authorized, so the fix should be straightforward. Also, why wasn’t the service taken down in the meantime?

I waited **another four days** and asked again for a timeline:

“Can you please give me a timeline estimate on fixing this issue ?  
To my understanding you have knowingly left vulnerable every user of the cloud platform.”

Finally a timeline:

“Again thanks for you report and follow up, the fix is in QA and it will be deployed by end of the month.”

That would make a **total of 17 days** during which SonicWall knowingly exposed their entire customer base.

Most of the other API IDOR issues we’ve disclosed to other organisations have been fixed within 48 hours. Even car alarm vendors have fixed similar issues inside 3 days of us reporting. This is a security vendor though, who really should know better and do better.

My colleague Ken helped me escalate this to the SonicWall CEO.

Ken reached out to message the CEO Bill Conner privately on LinkedIn. He replied within two hours, which was impressive given the time difference.

The head of global support was introduced to us and we were then passed to a VP of support who took our report and assured us that it would be raised urgently.

Whilst it still took **another 48 hours** , the vulnerability was resolved overnight on the **26-27th August**.

It was a shame that we had to go around the PSIRT team to get the priority raised, but good that it did accelerate the fix.

Even so, we still don’t understand why the service wasn’t taken down immediately. We’re realists – we know that keeping the service running is important, but in the face of risks this significant? Taking down the API request function to add a user wouldn’t have been particularly impactful for a short period whilst the fix was worked on either.

### Conclusion

Having a vulnerability this serious in a security product and cloud service isn’t great, but that isn’t our issue here. Vulnerabilities happen. It’s OK.

What makes the difference between a cool vendor and an uncool vendor is how they deal with the report. In our opinion SonicWall didn’t deal with this well and then knowingly exposed every single one of their cloud-connected customers to remote pwnage for 14 days.

### ***UPDATE***

SonicWall issued a statement to a journalist in which they said:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

Any exploitation of the vulnerability would first require a hacker to obtain an account owner’s specific tenant ID (which are fully protected and not publicly available) and then associate a new user with that tenant ID.

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

This is inaccurate and misleading for two reasons:

  * Firstly the tenant IDs were both unprotected and publicly available, otherwise we couldn’t have found them.
  * Secondly they use sequential numbers, meaning that if a hacker can count they could have obtained a valid tenant ID.

### API Penetration Testing

Test your APIs for authentication, injection, and data exposure risks that could compromise your services.

[Learn more](https://www.pentestpartners.com/service/api-penetration-testing/)

[ ![Decoding Rust strings ](https://www.pentestpartners.com/wp-content/uploads/2026/06/headline-rust-strings.png) __ ](https://www.pentestpartners.com/security-blog/decoding-rust-strings/)

  * Hardware Hacking 

##### Decoding Rust strings 

7 Min Read 

Jun 23, 2026

[ ![PTP Cyber Fest 2026. Built for people to get involved ](https://www.pentestpartners.com/wp-content/uploads/2026/06/ptp-cyber-fest-blog-shameless-headline.png) __ ](https://www.pentestpartners.com/security-blog/ptp-cyber-fest-2026-built-for-people-to-get-involved/)

  * Shameless Self Promotion 

##### PTP Cyber Fest 2026. Built for people to get involved 

6 Min Read 

Jun 12, 2026

[ ![ClickFix, CrashFix and the growing family of copy and paste attacks ](https://www.pentestpartners.com/wp-content/uploads/2026/06/Clickfix-headline-joew2.png) __ ](https://www.pentestpartners.com/security-blog/clickfix-crashfix-and-the-growing-family-of-copy-and-paste-attacks/)

  * Digital Forensics and Incident Response 

##### ClickFix, CrashFix and the growing family of copy and paste attacks 

13 Min Read 

Jun 10, 2026
