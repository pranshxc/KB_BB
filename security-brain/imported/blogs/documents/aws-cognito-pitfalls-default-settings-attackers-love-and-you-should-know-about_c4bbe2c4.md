---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-19_aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about.md
original_filename: 2023-01-19_aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about.md
title: 'AWS Cognito pitfalls: Default settings attackers love (and you should know
  about)'
category: documents
detected_topics:
- sso
- mobile-security
- saml
- jwt
- access-control
- command-injection
tags:
- imported
- documents
- sso
- mobile-security
- saml
- jwt
- access-control
- command-injection
language: en
raw_sha256: c4bbe2c427bb84ae94dbf8ae41a24953e63146a4309932a84022c5a561279ec3
text_sha256: 364109fcae21dcc0c70b6c26b49eb3ea7e7a2c5e0d0d2ad2a170097d610c0921
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# AWS Cognito pitfalls: Default settings attackers love (and you should know about)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-19_aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about.md
- Source Type: markdown
- Detected Topics: sso, mobile-security, saml, jwt, access-control, command-injection
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `c4bbe2c427bb84ae94dbf8ae41a24953e63146a4309932a84022c5a561279ec3`
- Text SHA256: `364109fcae21dcc0c70b6c26b49eb3ea7e7a2c5e0d0d2ad2a170097d610c0921`


## Content

---
title: "AWS Cognito pitfalls: Default settings attackers love (and you should know about)"
url: "https://www.secforce.com/blog/aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about/"
final_url: "https://www.secforce.com/blog/aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about/"
authors: ["Lorenzo Vogelsang (@ptrac3)"]
bugs: ["Amazon cognito misconfiguration"]
publication_date: "2023-01-19"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1647
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

# AWS Cognito pitfalls: Default settings attackers love (and you should know about)

![AWS Cognito](/media/images/AWS-Cognito.width-1000.png)

In recent years, there has been a significant rise in the adoption of cloud services as they are being perceived as convenient, powerful, and relatively secure.

The security of cloud services will always need to follow the [Shared Responsibility model](https://cloudsecurityalliance.org/blog/2020/08/26/shared-responsibility-model-explained/) whereby it is the customer's responsibility to ensure that their cloud environment is properly configured.

In this article, we will be exploring two misconfigurations of AWS Cognito which, sometimes, may be overlooked by both customers and pentesters alike. You will learn not only how attackers can exploit them but also how to remediate them.

Before we dive into the vulnerabilities, what is exactly AWS Cognito and what role does it have in the AWS Cloud ecosystem?

* * *

## **AWS Cognito**

According to the vendor, "Amazon Cognito provides authentication, authorisation, and user management for your web and mobile apps" but what does that mean exactly? Let’s see it in practice to understand it better.

The following diagram, taken from [Amazon](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html), represents a typical scenario for Amazon Cognito where the goal is to authenticate a user and to grant them access to a specific web resource. For authentication and authorisation purposes, AWS Cognito offers two different methods for different scenarios which are the use of _User_ and _Identity Pools_.

![AWS User Pool Diagram](/media/images/AWS_Cognito.width-800.png)

### **User Pools**

A user pool can be imagined as a user directory in Amazon Cognito. Users and groups can be onboarded to a User Pool in order to give them access to a bespoke web application either directly (with the credentials defined in the user pool) or via social identity providers like Apple, Google, etc through the use of the SAML protocol.

![User Pool example](/media/images/UserPool_Example.width-800.png)

During a recent web application test, a misconfiguration was identified in the permission configuration of a custom attribute which allowed us to successfully perform a privilege escalation attack. Based on further investigation in our AWS lab, it was possible to determine that the misconfiguration was due to AWS default settings and for this reason, it is believed that many other companies and services may be affected by the same issue. Let’s start by understanding what the attributes are and why they are important.

During the onboarding of a user in a User Pool, it is possible to specify which attributes should be enabled for that user and what their permissions should be (e.g. read/write permissions). The only attributes for which it is not possible to set Write permissions are the ones related to MFA policies and those involving the sign-up and verification process for a given user. For example, the “email_verified” attribute, which can have a “yes” or “no” value, cannot be modified as to allow write access for security reasons:

![AWS Cognito attributes](/media/images/AWS_Cognito_attributes.width-800.png)

It is important to notice that, whilst the attribute's name/type are defined on a User Pool level, their permissions can be configured on App Client level meaning that different applications can be configured with a different set of permissions regarding attributes. This is also very important to know as all users belonging to the same App Client, which is the most common scenario, will have the same set of attribute permissions.

Most importantly, the AWS Cognito User Pool allows users to add custom attributes. This is performed by AWS prepending “custom:” to the name that was chosen for the attribute. Let’s consider the following as an example of a vulnerable web application.

Let’s suppose that a fictitious Trading web application was configured in a way to allow certain actions based on a user-role setting. As such option is not natively supported in User Pools, it would be possible to define a custom attribute that will include the details of the user’s role and some backend code responsible for parsing the token and the role associated to a specific user. Let’s suppose that the roles available in the web application are only the following:

  1. Read only - The user only has read recent trading transactions
  2. Admin - The user has admin rights and can read but also issue new trading transactions

A viable option would be adding a custom attribute to a user containing the name of the user role. What could possibly go wrong, right?

According to our research, the permissions set for any custom attribute during the creation of a _User Pool_ is Read and Write by **default**.

For this reason, we have reached out to the AWS Security Team which recognized our submission and proposed a change in their document to better reflect the Cognito behaviour.

![AWS acknowledges a change in their documentation](/media/images/AWS_Documentation_Change.width-800.png)

Please refer to the following videos for a quick overview of AWS Console’s new/old UI default settings when creating a user pool:

However, if a custom role is added **after** a User Pool has been created, it would have neither Read or Write permissions by default:

![AWS Cognito custom attributes](/media/images/AWS_Cognito_custom_attributes.width-800.png)

In this example, let’s suppose that the user John was given read-only access to the Trading platform. This is the type of information the user will be able to get about the current AWS Cognito context by issuing the following AWS CLI command:

`aws cognito-idp get-user --region us-east-1 --access-token <TOKEN>`

![AWS Cognito custom "role" attribute](/media/images/AWS_Cognito_custom_attribute_CLI.width-800.png)

Although in our example the name of the custom role is already known, in real-life scenarios it might not be possible to correctly guess the name of a role or more generally of a user attribute that the attacker intends to update.

In a vulnerable scenario, this would translate to any _read-only_ user being able to successfully update their own role by issuing a command like the following:

`aws cognito-idp update-user-attributes --region us-east-1 --access-token <TOKEN> --user-attributes Name="custom:role",Value="admin-role"`

If successful, the custom user attribute would now reflect the change with the updated role:

![Custom attribute successful update](/media/images/AWS_Cognito_custom_attribute_update.width-800.png)

_Edit - 27 Mar 2023:_

#### Since AWS Cognito tokens can sometimes be overlooked and mistaken for generic JWT Tokens, we have developed a simple yet effective passive Burp Suite Pro extension to detect whether a JWT token is actually a Cognito session token. To download the extension and for more additional information please refer to the following link:

  * <https://github.com/SECFORCE/AWS-Cognito-Finder>

#### 

#### **Mitigation**

To mitigate the issue, it would be recommended to ensure that the permissions being set on Cognito users are matching both business and security requirements.

In particular, to update a custom attribute permission’s setting it is possible to follow this procedure (in the new AWS web UI):

  1. Browse to the Cognito section of AWS
  2. Select the current User Pool and click on the App client section
  3. Expand the Edit attribute read and write permission and proceed to change them as shown in the following screenshot

![Editing AWS Cognito Attribute permissions](/media/images/AWS_Cognito_attributes_editing.width-800.png)

### 

* * *

### Identity Pools

In contrast to _User Pools_ ,_Cognito Identity Pool IDs_ are utilised to allow users to fetch temporary AWS credentials. If the AWS Credentials obtained have excessive AWS permissions, it might be possible for an unauthenticated user to access sensitive AWS services.

In reality though, how commonly could this be exploited? I would argue that it would not be uncommon for a web application to leak its pool id which should look like the following:

![AWS Cognito Identity Pool](/media/images/IdentityPool.width-800.png)

Although the leakage of such information may not be an issue in itself, it would be recommended to avoid it since it may introduce unnecessary risk especially if the AWS credentials’ permissions are not following the principle of least privilege.

To derive the set of AWS credentials from a _PoolID_ , an attacker would only need a simple Boto3 script to generate them. For readers that are not experts in AWS, Boto3 is the official Python SDK for interacting with an AWS environment.

![Generating AWS Credentials from an Identity Pool](/media/images/AWS_creds_from_Pool.width-800.png)

Once the credentials have been generated, they can be stored under the ~/.aws/credentials folder as shown in the following screenshot:

![AWS Config credentials](/media/images/AWS_Creds_Config.width-800.png)

After this last step, an attacker would face no constraints apart from restrictive permissions from interacting with the AWS environment via the AWS CLI SDK:

![AWS "whoami" command](/media/images/AWS_whoami.width-800.png)

### 

* * *

### Final Remarks

The acceleration of adoption of Cloud environments as the industry’s “gold standard” for handling companies’ most sensitive assets is just getting started and it does not hint at stopping any time soon. On-premise migrations to PaaS services, the ever-availability of services such as corporate emails, cloud-managed security services such as EDR, zero trust and conditional policies are redefining the current landscape in what can be considered a "threat" and how the modern threat actor operates. In the current Cloud multi-verse, it may sometimes be a daunting task to be prepared to new emerging threats that do not follow the "on-premise" paradigm.

Even if it was for only a fraction of this, we wanted to raise awareness about some of the emerging threats that attackers are nowadays taking advantage of and with a simple but practical approach. This way, whether it is for your next offensive Security Assessment or to better defend against new attacks, we hope you found something you didn't know about. If that is the case, it means it has served its purpose as awareness is sometimes the invisible ingredient for better tackling new threats.

#### References

<https://infosecwriteups.com/hacking-aws-cognito-misconfiguration-to-zero-click-account-takeover-36a209a0bd8a?gi=3d6083295f1f>

<https://notsosecure.com/hacking-aws-cognito-misconfigurations>

<https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>

#### Downloads

<https://github.com/SECFORCE/AWS-Cognito-Finder>

### Share on

[![](/assets/img/post/share-linkedin.bbf3bfe683c7.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https://www.secforce.com/blog/aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about/)

[![](/assets/img/post/share-twitter.be2cd0ba0dc1.svg)](https://twitter.com/intent/tweet?url=https://www.secforce.com/blog/aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about/)

[![](/assets/img/post/share-facebook.e2eb401c1f6b.svg)](https://www.facebook.com/sharer.php?u=https://www.secforce.com/blog/aws-cognito-pitfalls-default-settings-attackers-love-and-you-should-know-about/)

### You may also be interested in...

[![A03 LLM GOAT](/media/images/A03_LLM_GOAT.original.png)](/blog/llmgoat-a03-supply-chain/)

March 25, 2026

### [LLMGoat - A03 Supply Chain](/blog/llmgoat-a03-supply-chain/)

This post is the third in a series of 10 blog posts and it covers the solution to the Supply Chain challenge from LLMGoat.

[See more](/blog/llmgoat-a03-supply-chain/)

[![imagensecforcepost.png](/media/images/imagensecforcepost.original.png)](/blog/secforce-will-be-presenting-at-owasp/)

March 17, 2014

### [SECFORCE will be presenting at OWASP](/blog/secforce-will-be-presenting-at-owasp/)

SECFORCE will present Tunna framework and a number of techniques penetration testers can benefit from to bypass network firewalls.

[See more](/blog/secforce-will-be-presenting-at-owasp/)

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
