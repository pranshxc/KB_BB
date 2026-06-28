---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-15_technical-advisory-azure-b2c-crypto-misuse-and-account-compromise.md
original_filename: 2023-02-15_technical-advisory-azure-b2c-crypto-misuse-and-account-compromise.md
title: Technical Advisory – Azure B2C – Crypto Misuse and Account Compromise
category: documents
detected_topics:
- oauth
- jwt
- cloud-security
- api-security
- sso
- idor
tags:
- imported
- documents
- oauth
- jwt
- cloud-security
- api-security
- sso
- idor
language: en
raw_sha256: 865f15a1bcb5b035064b637774bb28c198f4a93f980ce9d544fa4f2af0c1fb19
text_sha256: 8cc481b5637fae85b240fa792ca9e9d2997991129d2f7e905ecaa8f1c9940430
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Technical Advisory – Azure B2C – Crypto Misuse and Account Compromise

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-15_technical-advisory-azure-b2c-crypto-misuse-and-account-compromise.md
- Source Type: markdown
- Detected Topics: oauth, jwt, cloud-security, api-security, sso, idor
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `865f15a1bcb5b035064b637774bb28c198f4a93f980ce9d544fa4f2af0c1fb19`
- Text SHA256: `8cc481b5637fae85b240fa792ca9e9d2997991129d2f7e905ecaa8f1c9940430`


## Content

---
title: "Technical Advisory – Azure B2C – Crypto Misuse and Account Compromise"
page_title: "Technical Advisory - Azure B2C - Crypto Misuse and Account Compromise | Praetorian"
url: "https://www.praetorian.com/blog/azure-b2c-crypto-misuse-and-account-compromise/"
final_url: "https://www.praetorian.com/blog/azure-b2c-crypto-misuse-and-account-compromise/"
authors: ["John Novak"]
programs: ["Microsoft (Azure)"]
bugs: ["Cryptographic issues", "JWT", "Account takeover", "Authentication bypass"]
publication_date: "2023-02-15"
added_date: "2023-02-22"
source: "pentester.land/writeups.json"
original_index: 1523
---

Skip to content

**Meet Constantine – Find Mythos-level vulnerabilities in your code. It proves them, patches them, PRs them back. Autonomously.**

[ Download Datasheet ](/resources/constantine-datasheet/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

  * Platform  Close Platform Open Platform

#### [Praetorian Guard Platform](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Services  Close Services Open Services

#### [Penetration Testing Services](/penetration-testing/)

  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)
  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)

#### [Advanced Offensive Security](/advanced-penetration-testing/)

  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)
  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)

#### [Continuous Offensive Security](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Why Praetorian  Close Why Praetorian Open Why Praetorian

#### [Customer Case Studies](/customer-success-in-cybersecurity/)

  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)
  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)

#### Resources

  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)
  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)

#### Use Cases

  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)
  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)

  * About  Close About Open About

#### [About Praetorian](/praetorian-offensive-cybersecurity-company/)

  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)
  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)

#### [Join Praetorian](/careers/#job-opening)

  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)
  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)

  * [ Platform Demo  ](/praetorian-guard-demo/)

  * [ Contact Us  ](/contact-us/)

  * [Cloud Security](https://www.praetorian.com/category/cloud-security/), [Uncategorized](https://www.praetorian.com/category/uncategorized/)

# Technical Advisory – Azure B2C – Crypto Misuse and Account Compromise

  * [John Novak](https://www.praetorian.com/author/john-novak/)
  * [ February 15, 2023 ](https://www.praetorian.com/blog/2023/02/15/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/AzureB2C1.png)

Microsoft’s Azure Active Directory B2C service contained a cryptographic flaw which allowed an attacker to craft an OAuth refresh token with the contents for any user account. An attacker could redeem this refresh token for a session token, thereby gaining access to a victim account as if the attacker had logged in through a legitimate login flow. Praetorian reported this security vulnerability to Microsoft in two parts in March 2021 & July 2022 and Microsoft applied two changes in December 2022 and February 2023. Based on our examination of Microsoft’s fixes, however, previously exploited Azure B2C environments may remain vulnerable to attackers until the rollout of Microsoft’s second fix is complete on Feb 15, 2023.

### Impact: Potential range of effect

Azure B2C environments with the following configuration were likely to be susceptible to the vulnerability :

  * Used [ Azure AD B2C custom policies](https://learn.microsoft.com/en-us/azure/active-directory-b2c/custom-policy-overview)
  * Configured an application with the OAuth [ Authorization code flow (with PKCE)](https://learn.microsoft.com/en-us/azure/active-directory-b2c/application-types#authorization-code-flow-with-pkce)
  * Configured the environment as described in [ Microsoft’s tutorial documentation](https://learn.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-user-flows?pivots=b2c-custom-policy) without any modifications to the cryptographic guidance therein

These conditions are common for most single page applications (SPAs) or mobile applications. Performing a [ subdomain lookup](https://subdomains.whoisxmlapi.com/lookup-report/d95pvV9dRp) for *.b2clogin.com shows that Microsoft’s customers have configured at least a thousand B2C environments, but we have not rigorously probed these environments to determine which meet the criteria above. Microsoft also has [ dogfooded](https://en.wikipedia.org/wiki/Eating_your_own_dog_food) this service for the Microsoft Security Response Center (MSRC) Researcher Portal where security researchers can submit vulnerabilities in exchange for bug bounties or leaderboard notoriety. In the case of MSRC, an attacker could use this vulnerability to target the accounts of security researchers and enumerate the details of Microsoft zero-day vulnerabilities as they are submitted through the portal.

### Implications: Risk rating and remediation

Given the potential for the compromise of any account in a B2C environment from an unauthenticated attacker using only account identifiers (such as an email address or account UUID), Praetorian rated this vulnerability as a critical risk elevation of privilege issue. Following disclosure, Microsoft rated this issue as an Important Information Disclosure issue. After a lengthy discussion with Microsoft we reached a middle-ground of agreement that we will explain in the disclosure section. Given the disconnect between our researcher and Microsoft, the reader will need to determine the potential impact to their own Azure B2C environment.

Microsoft resolved the issue behind-the-scenes with a narrow fix in December 2022 that addresses the “information disclosure” portion of the issue and end users do not need to take any action to apply this fix. Microsoft applied another change to the contents of refresh tokens in February 2023 which addresses the underlying “crypto misuse” portion of the issue. Microsoft’s fixes are designed to ensure backward compatibility and “no action required” on the part of tenant administrators. For these reasons, this advisory also provides our remediation guidance for Azure administrators to strengthen their environment with a key rotation and/or configuration change.

## Details

Figure 1 shows an abbreviated Azure B2C OAuth Authorization code flow (with PKCE) . The OAuth flow itself and redemption of a token matches the standard flow, but the generation of a refresh_token deviates from convention.

![](https://www.praetorian.com/wp-content/uploads/2024/06/AzureB2C1.png)

_Figure 1: Abbreviated OAuth flow meets expectations, but refresh token generation does not._

In particular, Microsoft’s [ tutorial](https://learn.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-user-flows?pivots=b2c-custom-policy) for generating keys recommends generating an encryption key of type “RSA” which corresponds to RSA public key cryptography (see figure 2).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20996%20973'%3E%3C/svg%3E)

_Figure 2: A snippet of the tutorial and the corresponding UI in the Azure portal._

The cryptographic flaw here is that encryption with RSA uses the _public_ portion of the RSA public/private key pair. As the name implies, the public key is not a secret value and in common implementations multiple parties share it when interacting with the RSA cryptographic primitive (such as in a X.509 certificate). If an attacker were to know the public part of the “TokenEncryptionKeyContainer” RSA key, then that attacker could generate and encrypt their own refresh_token, resulting in a shortcut to the OAuth flow as figure 3 demonstrates.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201003%20789'%3E%3C/svg%3E)

_Figure 3: Encryption via the public key allows an attacker to shortcut to the OAuth flow._

This advisory does not provide the attack that recovers the public portion of this RSA key, but suffice to say that it was possible by a determined attacker. We also do not give the format of the encrypted refresh_token contents but that, too, can be recovered with additional effort. Disclosing these details or exploit code before or soon after remediation by Microsoft might put Azure B2C environments at unnecessary risk. Luckily, since this is a cryptographic attack, we can prove our claims by providing signed tokens not under the attacker’s control. We may choose to disclose the additional details at a future time, as in the author’s opinion they are the most interesting technical pieces of this vulnerability.

## Proof of Work

As we mentioned in the introduction, the MSRC web portal uses Azure B2C as its login method of choice and is susceptible to the vulnerability described in this blog post. We obtained the RSA public key for the msrcweb.b2clogin.com domain and used it to craft a refresh_token. We then submitted this refresh_token to the appropriate [ /token endpoint](https://msrcweb.b2clogin.com/9f449d34-93e9-437f-8082-7127fc8ab474/oauth2/v2.0/token?p=b2c_1a_multitenant_signupsignin) and retrieved an id_token (see figure 4). For demonstration purposes, this token was acquired for a user with an email address of [[email protected]](/cdn-cgi/l/email-protection) and an additional claim of “isAdmin”:true.
  
  
  eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imtjb19tY20tUDc3UjZnSVpwOVBLLWxqdkhfVlVMNkltdjRDdF9ncWpnMGsifQ.eyJleHAiOjE2NjMyNTAxNDcsIm5iZiI6MTY2MzI0NjU0NywidmVyIjoiMS4wIiwiaXNzIjoiaHR0cHM6Ly9tc3Jjd2ViLmIyY2xvZ2luLmNvbS85ZjQ0OWQzNC05M2U5LTQzN2YtODA4Mi03MTI3ZmM4YWI0NzQvdjIuMC8iLCJzdWIiOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJhdWQiOiIxZDEzZTUyOS05OWI4LTQ4ZmUtYTc3ZC04NDQ4NTNhZTI1YmYiLCJhY3IiOiJiMmNfMWFfbXVsdGl0ZW5hbnRfc2lnbnVwc2lnbmluIiwiaWF0IjoxNjYzMjQ2NTQ3LCJhdXRoX3RpbWUiOjE2NjMyNDI5NDMsImVtYWlsIjoiYWxpY2UuYm9iQGV4YW1wbGUuY29tIiwib2lkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwidGlkIjoiOWY0NDlkMzQtOTNlOS00MzdmLTgwODItNzEyN2ZjOGFiNDc0IiwiaXNBZG1pbiI6dHJ1ZX0.HpyntiW6C6uw4ZrHr1yVTSdz4FSbmRw_BveGslupHktfhK8PbELW9UVs36rxNj-0Y3C-OSBp505HJpQOUro6bfmA0xGLxjLyAcQHFOmaomEuZHlWEjhSPgO42YelV3nW2Cp74NxiejzWWgogS5z8qjk6VgxHI1-4chaahtYW2kF1DbSFad0NtskhdYkM4be-RoXYD5mJofK0gG0tyxIpp3AiptoVehp039Jjvlcfc93RqSsrEdoNPGlMGWM1pwgEvnPlatYAlaHHmpST801OEhudwwgw5TfSh4mHbxsljVtIv7mUYfkW7tCL_ErOqgQgA529KBDOvak-dukveKiFnw

_Figure 4: The id_token we retrieved using this method._

OpenID Key for validation:[ https://msrcweb.b2clogin.com/9f449d34-93e9-437f-8082-7127fc8ab474/discovery/v2.0/keys?p=b2c_1a_multitenant_signupsignin](https://msrcweb.b2clogin.com/9f449d34-93e9-437f-8082-7127fc8ab474/discovery/v2.0/keys?p=b2c_1a_multitenant_signupsignin) ([ web archive link](https://web.archive.org/web/20220812172056/https://msrcweb.b2clogin.com/9f449d34-93e9-437f-8082-7127fc8ab474/discovery/v2.0/keys?p=b2c_1a_multitenant_signupsignin) )

Using the public key corresponding to this token, any reader of this post can independently verify the validity of this token with several lines of code. We have provided an example in Python in figure 5. Note that validation will require the “check_claims=False” parameter since the token in figure 4 has expired (it was short-lived and created months ago). Should you omit that option you will get a “JWTExpired” error, and if the signature on the token does not match then you will get a “InvalidJWSSignature” error.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201009%20148'%3E%3C/svg%3E)

_Figure 5: Python example of code verifying our id_token._

The JWT given above with the script should provide proof that attackers can create arbitrary JWT claims for any user account on the msrcweb.b2clogin.com domain. To further demonstrate that this ability could compromise any user account, we also found a minimal set of claims in the JWT that still allowed access to sensitive API endpoints for the MSRC web application API. Using the JWT with this minimal set of claims, an attacker could request a list of vulnerability reports for a victim account using an email address alone. We captured this request in a Burp proxy window (see figure 6).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201004%20686'%3E%3C/svg%3E)

_Figure 6: A list of vulnerability reports we captured using only an email address in the JWT._

Keen observers will notice that the minimal set of claims does have two values that appear random and non-guessable–a “tid” or tenant id, and an “aud” or audience. However, the [ OpenID configuration](https://msrcweb.b2clogin.com/msrcweb.onmicrosoft.com/v2.0/.well-known/openid-configuration?p=b2c_1a_multitenant_signupsignin) and client-side [ JavaScript code](https://msrc.microsoft.com/report/vulnerability/static/js/main.201b4c4a.js) from the [ web application](https://msrc.microsoft.com/report/vulnerability) serve up both of these to external users. Note that the JavaScript loaded changes from time to time so the link provided may 404.

## MSRC Business Impact

In summary, using an email alone, an attacker could view vulnerability reports that researchers had submitted to the MSRC web portal for any victim account. Depending on the victim, this could include details of zero-day vulnerabilities for any number of Microsoft products (Windows, Azure, Exchange, etc.). This type of information would be highly valuable to nation state attackers looking to exploit Microsoft products or services before they are patched.

We specifically chose the MSRC web portal as a demonstration of impact since it was not developed by an unsuspecting Microsoft customer of Azure B2C. However, the business impact could vary widely depending on the design of an application associated with other Azure B2C environments. Praetorian recommends that Azure B2C customers perform their own risk assessment and consider the guidance below.

## Remediation Guidance

Microsoft resolved the information disclosure portion of this vulnerability in a way that does not require an update or configuration change by end users. Microsoft’s remediation is for the Azure B2C /token endpoint to return no response (error or otherwise) when an invalid refresh token is submitted. This implementation is a narrow fix of the information disclosure vulnerability and remediates the specific attack to recover the RSA public key.

Microsoft addressed the “crypto misuse” of this vulnerability by adding a new element to the refresh token contents signed with a key owned and controlled by Microsoft. This implementation means that even if an attacker recovers the RSA public key, they cannot construct all of the contents of a refresh token. This will prevent an attacker from constructing a complete refresh token. Microsoft seems to have chosen this design to maintain some backward compatibility and keep B2C tenant administrators from having to take any action to apply a fix.

While Microsoft’s fixes are technically effective, they sidestep the underlying crypto misuse issue and Praetorian cannot find an easy method of configuring Azure B2C with that in mind. Praetorian recommends that Azure customers rotate keys at the very least to stop an attacker who has already exposed a RSA public key. However, we further recommend all users change to a secret key type for AES encryption for a more robust fix that resolves the issues around cryptographic misuse. A [ previous blog article](https://www.praetorian.com/blog/signing-and-encrypting-with-json-web-tokens/) provides reasoning for using each key type.

### Option 1: Key Rotation.

Cryptographic key rotation is an industry standard and follows security best practices. The simple act of deleting the “TokenEncryptionKey” and then generating a new one (see [ Microsoft tutorial](https://learn.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-user-flows?pivots=b2c-custom-policy) ) will perform a key rotation. We recommend users take this action on a regular basis. In the event of a security vulnerability that leaks keys, users should prioritize key rotation among their first actions in response. This will invalidate compromised keys or evict attackers, but this action is not as crucial given that Microsoft’s second fix for this vulnerability changes the format for refresh tokens. In fact, users should consider as compromised any RSA key in place while the environment was vulnerable.

A key rotation will necessarily invalidate the refresh token for all users, requiring each to re-login, so security teams should consider this business impact before undertaking this action. Security teams also should take note that keeping the RSA key type and choosing a rotation solution will leave environments configured this way vulnerable in the event of any future discoveries of “information disclosure” issues with the RSA public key.

### Option 2: Key Type Change.

From a cryptographic perspective, using symmetric encryption is a preferred method for JWEs in a refresh token. At first glance, end users should be able to easily configure this option by choosing “Secret” instead of “RSA” keys within the key generation menu pictured in figure 2. However, choosing this option and then logging in with any user account results in an error message indicating that the “Secret” key generation method makes a key which is not 256-bits in size (see Figure 7).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201000%20867'%3E%3C/svg%3E)

_Figure 7: An error message indicating the “Secret” encryption key is not the correct length._

At the time of writing (Feb 11, 2023), the only way for an end user to configure a Secret key properly for refresh token encryption is to generate a key on their own system and then upload it instead of using the “generate” method. Figure 8 provides the format for such a key.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201007%20171'%3E%3C/svg%3E)

_Figure 8: The format for a Secret key an engineer would generate locally and upload to Azure._

The downside for this approach is that the secret key will necessarily exist outside of the Azure B2C environment and must be protected on external systems beyond Microsoft’s control. If engineers choose this method, they should securely delete and discard the key from their local system after generating and uploading it. Changing the key type will also necessarily invalidate all refresh tokens for users of the system just as with a key rotation action and therefore will have a business impact that bears consideration.

**Incident Response** : While Praetorian has no indication that this is a known vulnerability, it is possible that attackers have exploited this vulnerability and not disclosed having done so. A worst case scenario is that an attacker masqueraded as another user on the affected application and performed some sensitive action or disclosed information from that account. If an Azure B2C application is of particularly high-value to an organization, then their security team should consider undertaking blue team or incident response activities, depending on the business risk. If these activities provide any indication of compromise in a B2C application, then the organization must undertake one of the remediation options we suggested above.

**Recommendation to Microsoft** : For a robust solution for JWTs, use a nested JWT as other experts have described in the [ JWT RFC](https://www.rfc-editor.org/rfc/rfc7519.html#section-11.2) and the [ OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) specification. However, to minimize design changes, altering the tutorial and fixing the “Secret” key generation function as we described in the Key Type Change option above may suffice.

## Disclosure

We initially disclosed this vulnerability to the MSRC in March 2021. That submission included details of how an attacker could use a compromised RSA public key to craft a refresh token and compromise any victim account. However, at that time we had not discovered the means to recover the RSA public key as an unauthenticated attacker so the vulnerability was largely theoretical. Microsoft reviewed the submission and noted that the RSA public key was available in the Azure Portal “Identity Experience Framework | Policy keys” tab, but the public portion of that key is only available to users with the “Global Administrator” or “IEF Key Set Administrator” role in the Azure environment. Since these are already highly privileged users, the functionality was working as they expected and they took no action.

Through a series of unrelated events in July 2022 we discovered and exploited an attack which can recover the RSA public key for refresh tokens. We provided the full details of this attack in a new submission to the MSRC on July 27, 2022. A long series of interaction through the MSRC web portal, email, and a call followed this submission as summarized in the figure 9 timeline.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20994%20590'%3E%3C/svg%3E)

_Figure 9: A timeline reflecting the interactions between Microsoft and Praetorian between July 2022 and February 2023._

For approximately three months, the vulnerability sat in the “Review” stage which [ Microsoft stated should take “up to one or two weeks”](https://msrc-blog.microsoft.com/2020/09/21/what-to-expect-when-reporting-vulnerabilities-to-microsoft/) . During the review period they provided no substantive information in response to our follow up inquiries. We can attribute the lag to the fact that we reported a complex vulnerability that does take some understanding of cryptographic concepts above and beyond standard vulnerability categories (ex. XSS, CSRF, IDOR). It most likely warranted additional review time. Once the submission moved to the Develop stage, Microsoft was more forthcoming with updates and feedback and remediated the information disclosure vulnerability in December 2022. Early in 2023 we engaged with Microsoft to publicly disclose this vulnerability but mutually agreed to hold off disclosure until they could complete some new architectural changes in mid-February.

### Microsoft’s Response

The first remediation Microsoft implemented for this vulnerability does narrowly address the information disclosure issue, but it does not automatically perform any key rotation or otherwise invalidate encryption keys for refresh tokens in any Azure B2C environment. We observed that the same RSA public key we used in our demonstration was valid for creating new refresh tokens in the msrcweb.b2clogin.com domain following Microsoft’s fix in mid-December 2022. After sharing an early draft of this technical advisory and regularly probing that environment, we observed that on or around January 6, 2023 the keys for that domain were rotated in line with the remediation guidance we provided in this advisory.

Microsoft rated this issue with a severity rating of “Important”. Praetorian believes that the severity rating for this vulnerability is much higher for reasons described in the MSRC Impact section above. We recommend that each application using Azure B2C assess the potential severity of this issue for their own environment.

Microsoft assigned the vulnerability a security impact of “Information Disclosure” and surely does disclose an RSA public key so by definition this categorization makes sense. However, the vulnerability ultimately arises because the security of the Azure B2C authentication system relies on keeping secret a RSA public key–something that neither RSA nor any other asymmetric cryptosystem was designed to do. Microsoft seems to categorize vulnerabilities based on how they intend to remediate them, and indeed their first fix only addresses the disclosure issue and not the underlying cryptographic misuse.

While the categorization of this vulnerability might have financial implications for a [ bug bounty](https://www.microsoft.com/en-us/msrc/bounty) , Microsoft did not award one. Microsoft does have several bug bounty programs, including ones for [ Microsoft Azure](https://www.microsoft.com/en-us/msrc/bounty-microsoft-azure) and [ Microsoft Identity](https://www.microsoft.com/en-us/msrc/bounty-microsoft-identity) , but this particular vulnerability does not qualify. Azure B2C is an Azure service, but since it directly relates to authentication it falls under the Identity bounty program. However, b2clogin.com is not an “in-scope domain” for that bounty program so it is ineligible. This is an unfortunate circumstance not just for the submitter, but for the security of the Azure B2C service itself. Since Microsoft does not include Azure B2C identity flaws under any program at this time, researchers have no incentive to find and, more importantly, disclose vulnerabilities to Microsoft.

## About the Authors

![John Novak](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [John Novak](https://www.praetorian.com/author/john-novak/)

John is in Praetorian's Architecture and Engineering practice. His specialties include IoT assessments, cryptography, & other advanced service offerings.

[ ](http://linkedin.com/in/john-novak-823a267a)[ ](https://twitter.com/jwnovak)

## Catch the Latest

Catch our latest exploits, news, articles, and events.

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 19, 2026

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

## [GhostPack Necromancy: Reforging C# Tools with WasmForge](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[ Read More ](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 17, 2026

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

## [FreeBSoD: Leveraging Language Models to Find and Exploit Kernel Bugs (Part 1 of 2)](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[ Read More ](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

  * [Uncategorized](https://www.praetorian.com/category/uncategorized/)

  * June 16, 2026

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## [Sharing is Caring: SMB Secret Scanning with Sulla](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

[ Read More ](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## Ready to Discuss Your Next Continuous Threat Exposure Management Initiative?

Praetorian’s Offense Security Experts are Ready to Answer Your Questions

[ Get Started ](/contact-us/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

##### [Praetorian Guard Platform](https://www.praetorian.com/guard)

  * [ Continuous Threat Exposure Management ](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [ Attack Surface Management ](https://www.praetorian.com/guard/attack-surface-management/)
  * [ Vulnerability Management ](/chariot/vulnerability-management/)
  * [ Cyber Threat Intelligence ](/chariot/threat-intelligence/)
  * [ Continuous Penetration Testing ](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [ Breach and Attack Simulation ](https://www.praetorian.com/guard/breach-attack-simulation/)

##### Professional Services

  * [ AI/ML Penetration Testing ](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [ Application Penetration Testing ](/services/application-penetration-testing/)
  * [ Assumed Breached Exercise ](/services/assumed-breached-exercise/)
  * [ Attack Path Mapping ](https://www.praetorian.com/resources/attack-path-mapping/)
  * [ Automotive Penetration Testing ](/services/automotive-penetration-testing/#)
  * [ CI/CD Security Engagement ](/services/ci-cd-security-engagement/)
  * [ Cloud Penetration Testing ](/services/cloud-penetration-testing/)
  * [ IoT Penetration Testing ](/services/iot-penetration-testing/)
  * [ Network Penetration Testing ](/services/network-penetration-testing/)
  * [ NIST CSF Benchmark ](/services/nist-csf-benchmark/)
  * [ Purple Team ](/services/purple-team/)
  * [ Red Team ](/services/red-team/)

##### Use Cases

  * [ Bug Bounty Cost Reduction ](/services/bug-bounty-cost-reduction/)
  * [ FDA Testing and Monitoring ](/services/fda-testing-monitoring/)
  * [ Mergers and Acquisitions ](/services/mergers-acquisitions/)
  * [ Ransomware Prevention ](/services/ransomware-prevention/)
  * [ Rogue IT Identification ](/services/rogue-it-identification/)
  * [ Tool and Vendor Consolidation ](/services/tool-vendor-consolidation/)
  * [ Vendor Risk Management ](https://www.praetorian.com/services/vendor-risk-management/)

##### Company

  * [ About Us ](https://www.praetorian.com/about-us/)
  * [ Leadership Team ](https://www.praetorian.com/leadership-team/)
  * [ Press Releases ](/news/press-release/)
  * [ In the News ](/news/news)
  * [ Contact Us ](https://www.praetorian.com/contact-us/)
  * [ Resource Library ](https://www.praetorian.com/resources/)
  * [ Security Blog ](/blog/)
  * [ People Ops Blog ](/people-ops/)
  * [ Careers ](https://www.praetorian.com/careers/)
  * [ Culture ](https://www.praetorian.com/work-at-praetorian/)
  * [ Survival Kit ](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)

### Subscribe to our Newsletter

Catch our latest exploits, news, articles, and events.

[Privacy Policy](/privacy-policy/) | [Responsible Disclosure Policy](/responsible-disclosure-policy/) | [Terms of Service](/terms-of-service/) | [Terms and Conditions](/terms/)

Copyright © 2025. All Rights Reserved.

[ Linkedin-in ](https://www.linkedin.com/company/praetorian/) [ X-twitter ](https://twitter.com/praetorianlabs) [ Facebook-f ](https://www.facebook.com/praetorianlabs) [ Github ](https://github.com/praetorian-inc) [ Youtube ](https://www.youtube.com/user/PraetorianLabs)
