---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-13_how-oauth-implicit-flow-led-to-hundreds-of-user-accounts-being-accessed.md
original_filename: 2023-12-13_how-oauth-implicit-flow-led-to-hundreds-of-user-accounts-being-accessed.md
title: 'How OAuth Implicit Flow Led To Hundreds Of User Accounts Being Accessed? '
category: documents
detected_topics:
- rate-limit
- mobile-security
- oauth
- idor
- access-control
- command-injection
tags:
- imported
- documents
- rate-limit
- mobile-security
- oauth
- idor
- access-control
- command-injection
language: en
raw_sha256: 1e1ed4df175ebd0215faf375008aa2cf61045b04576fd2f41ed7893ee3b17a45
text_sha256: 7263f1bc450ac97f73c46f76572c700a8fba27aafd88063dd5bb338fb7a37be2
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# How OAuth Implicit Flow Led To Hundreds Of User Accounts Being Accessed? 

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-13_how-oauth-implicit-flow-led-to-hundreds-of-user-accounts-being-accessed.md
- Source Type: markdown
- Detected Topics: rate-limit, mobile-security, oauth, idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `1e1ed4df175ebd0215faf375008aa2cf61045b04576fd2f41ed7893ee3b17a45`
- Text SHA256: `7263f1bc450ac97f73c46f76572c700a8fba27aafd88063dd5bb338fb7a37be2`


## Content

---
title: "How OAuth Implicit Flow Led To Hundreds Of User Accounts Being Accessed? "
page_title: "How OAuth Implicit Flow led to mass unauthorized access"
url: "https://payatu.com/blog/how-oauth-implicit-flow-led-to-hundreds-of-user-accounts-being-accessed/"
final_url: "https://payatu.com/blog/how-oauth-implicit-flow-led-to-hundreds-of-user-accounts-being-accessed/"
authors: ["Sufiyan Gouri (@gouri_sufyan)"]
bugs: ["OAuth"]
publication_date: "2023-12-13"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 630
---

Skip to content

[ ![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/06/Payatu_logo.png?fit=320%2C89&ssl=1) ](https://payatu.com)

![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/06/hamburger_logo.png?fit=35%2C28&ssl=1)

![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/06/hamburger_logo.png?fit=35%2C28&ssl=1)

  * Services
  * [Product Security Assessment](https://payatu.com/product-security-assessment/)
  * [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  * [Red Team Assessment](https://payatu.com/red-team-assessment/)
  * [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  * [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  * [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  * [Code Review Service](https://payatu.com/code-review-service/)
  * [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  * [SOC Service](https://payatu.com/soc-service/)
  * [Web Application Security Testing](https://payatu.com/web-security-testing/)
  * [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  * [Certification Body](https://payatu.com/certification-body/)
  * [Inspection Body](https://payatu.com/inspection-body/)
  * Industries
  * [Automotive](https://payatu.com/automotive-security/)
  * [IT/SaaS](https://payatu.com/it-saas-security/)
  * [FinTech/BFSI](https://payatu.com/fintech-bfsi-security/)
  * [MedTech](https://payatu.com/medtech-security/)
  * [Telecom](https://payatu.com/telecom-security/)
  * Products
  * [EXPLIoT](https://expliot.io/)
  * [Cloudfuzz](https://cloudfuzz.io/)
  * Who we are
  * [About Us](https://payatu.com/about-us/)
  * [Payatu Bandits](https://payatu.com/bandits/)
  * Resources
  * [Advisory](https://payatu.com/advisory/)
  * [Blog](https://payatu.com/blog/)
  * [BugBazaar](https://payatu.com/bugbazaar/)
  * [Case Studies](https://payatu.com/case-studies/)
  * [Checklist](https://payatu.com/checklist/)
  * [CISO Corner](https://payatu.com/ciso-corner/)
  * [Datasheet](https://payatu.com/datasheet/)
  * [DVAPI](https://payatu.com/dvapi/)
  * [Ebooks](https://payatu.com/ebooks/)
  * [Infographics](https://payatu.com/infographics/)
  * [Masterclass](https://payatu.com/masterclass-series/)
  * [Media](https://payatu.com/media/)
  * [Securecodewiki](https://securecode.wiki/)
  * [Telegram Community](https://payatu.com/community/)
  * [Contact Us](https://payatu.com/contact-us/)
  * [CISO Corner](https://payatu.com/ciso-corner/)

____

  * Services
  * [Product Security Assessment](https://payatu.com/product-security-assessment/)
  * [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  * [Red Team Assessment](https://payatu.com/red-team-assessment/)
  * [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  * [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  * [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  * [Code Review Service](https://payatu.com/code-review-service/)
  * [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  * [SOC Service](https://payatu.com/soc-service/)
  * [Web Application Security Testing](https://payatu.com/web-security-testing/)
  * [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  * [Certification Body](https://payatu.com/certification-body/)
  * [Inspection Body](https://payatu.com/inspection-body/)
  * Industries
  * [Automotive](https://payatu.com/automotive-security/)
  * [IT/SaaS](https://payatu.com/it-saas-security/)
  * [FinTech/BFSI](https://payatu.com/fintech-bfsi-security/)
  * [MedTech](https://payatu.com/medtech-security/)
  * [Telecom](https://payatu.com/telecom-security/)
  * Products
  * [EXPLIoT](https://expliot.io/)
  * [Cloudfuzz](https://cloudfuzz.io/)
  * Who we are
  * [About Us](https://payatu.com/about-us/)
  * [Payatu Bandits](https://payatu.com/bandits/)
  * Resources
  * [Advisory](https://payatu.com/advisory/)
  * [Blog](https://payatu.com/blog/)
  * [BugBazaar](https://payatu.com/bugbazaar/)
  * [Case Studies](https://payatu.com/case-studies/)
  * [Checklist](https://payatu.com/checklist/)
  * [CISO Corner](https://payatu.com/ciso-corner/)
  * [Datasheet](https://payatu.com/datasheet/)
  * [DVAPI](https://payatu.com/dvapi/)
  * [Ebooks](https://payatu.com/ebooks/)
  * [Infographics](https://payatu.com/infographics/)
  * [Masterclass](https://payatu.com/masterclass-series/)
  * [Media](https://payatu.com/media/)
  * [Securecodewiki](https://securecode.wiki/)
  * [Telegram Community](https://payatu.com/community/)
  * [Contact Us](https://payatu.com/contact-us/)
  * [CISO Corner](https://payatu.com/ciso-corner/)

  * Services
  * [Product Security Assessment](https://payatu.com/product-security-assessment/)
  * [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  * [Red Team Assessment](https://payatu.com/red-team-assessment/)
  * [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  * [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  * [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  * [Code Review Service](https://payatu.com/code-review-service/)
  * [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  * [SOC Service](https://payatu.com/soc-service/)
  * [Web Application Security Testing](https://payatu.com/web-security-testing/)
  * [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  * [Certification Body](https://payatu.com/certification-body/)
  * [Inspection Body](https://payatu.com/inspection-body/)
  * Industries
  * [Automotive](https://payatu.com/automotive-security/)
  * [IT/SaaS](https://payatu.com/it-saas-security/)
  * [FinTech/BFSI](https://payatu.com/fintech-bfsi-security/)
  * [MedTech](https://payatu.com/medtech-security/)
  * [Telecom](https://payatu.com/telecom-security/)
  * Products
  * [EXPLIoT](https://expliot.io/)
  * [Cloudfuzz](https://cloudfuzz.io/)
  * EXPLIoT is framework for IoT security testing and exploitation.

  * CloudFuzz is platform that lets you code for bugs by running your software with millions of test cases.

  * Who we are
  * [About Us](https://payatu.com/about-us/)
  * [Payatu Bandits](https://payatu.com/bandits/)
  * Resources
  *  *  * #### Resources

  * [Advisory](https://payatu.com/advisory/)
  * [Blog](https://payatu.com/blog/)
  * [Case Studies](https://payatu.com/case-studies/)
  * [Checklist](https://payatu.com/checklist/)
  * [CISO Corner](https://payatu.com/ciso-corner/)
  * [Datasheet](https://payatu.com/datasheet/)
  * [Ebooks](https://payatu.com/ebooks/)
  * [Masterclass](https://payatu.com/masterclass-series/)
  * [Media](https://payatu.com/media/)
  *  * #### Tools

  * [BugBazaar](https://payatu.com/bugbazaar/)
  * [Securecodewiki](https://securecode.wiki/)
  * [DVAPI](https://payatu.com/dvapi/)
  * #### Community

  * [Telegram Community](https://payatu.com/community/)
  *  *  * [Infographics](https://payatu.com/infographics/)
  * [Contact Us](https://payatu.com/contact-us/)
  * [CISO Corner](https://payatu.com/ciso-corner/)

# How OAuth Implicit Flow led to Hundreds of User Accounts Being Accessed? 

![](https://secure.gravatar.com/avatar/71ea8ac8cf9b3774942967596f0e1b802626eaa6be84b3faebe1aebeae034a69?s=96&d=mm&r=g)

  * [ Sufiyan Gouri  ](https://payatu.com/author/sufiyan-gouri/)
  * [ December 13, 2023 ](https://payatu.com/2023/12/13/)

![](https://i0.wp.com/payatu.com/wp-content/uploads/2023/12/MicrosoftTeams-image.png?fit=2880%2C1440&ssl=1)

__

__

__

__

__

__

Table of Contents

Toggle

  * Introduction
  * What is OAuth Implicit Flow? 
  * The OAuth Implicit Flow follows these steps: 
  * Exploiting OAuth Implicit Flow: A Step-by-Step Guide 
  * How Did I Discover OAuth-enabled Users and Employees Through Email Enumeration? 
  * Mitigation: 
  * Impact
  * For Practice and Learning

## Introduction

In this article, I delve into the potential vulnerabilities of OAuth Implicit Flow, specifically in gaining unauthorized access to user accounts due to a misconfiguration in OAuth Setup. I will examine how this flaw allowed me to access the accounts of hundreds of users, including administrators and employees. 

## **What is OAuth Implicit Flow?**

OAuth Implicit Flow is one of the four authentication and authorization flows used across different platforms and applications. This flow is designed for mobile applications or single-page applications (SPAs), wherein the client-side JavaScript code directly communicates with the authorization server of the OAuth provider. 

The Implicit Flow allows access tokens to be obtained without exchanging client secrets. After the user has granted authorization, the authorization server directly returns the access token to the client application. The access token is then sent directly to the client-side JavaScript code without the need for a temporary code exchange for the access token. 

## **The OAuth Implicit Flow follows these steps:**

The client-side JavaScript code initiates the authorization request by redirecting the user to the authorization endpoint of the OAuth provider. 

The user authenticates and authorizes the client application. 

The authorization server sends the access token directly to the client-side JavaScript code. 

The client-side JavaScript code can then access the protected resources on behalf of the user using the access token. 

For more information about OAuth grant types, you can visit this link: <https://payatu.com/blog/oauth-grant-types/>

## **Exploiting OAuth Implicit Flow: A Step-by-Step Guide**

I performed a simple attack on an application that used Google OAuth for login to demonstrate how the OAuth Implicit Flow vulnerability can be exploited. 

![](https://i0.wp.com/payatu.com/wp-content/uploads/2023/12/Image-08-12-23-at-3.53-PM.jpeg?resize=800%2C394&ssl=1)

1\. Captured the OAuth login request in Burp.  
2\. It was observed that the application received basic user information from the Google OAuth service. It then logged the user in by sending a POST request containing this information to its authentication endpoint, along with the access token. 

**POST /api/dashboard/login/google HTTP/1.1**  
**Host: oauth.domain.com**  
User-Agent:  
Cookie: 

{“googleId”:”1234″, “imageUrl”:”[https://abc.com&#8221](https://abc.com&#8221);,  
“email”:”**[[email protected]](/cdn-cgi/l/email-protection)** “,  
“name”:”Attacker”,  
“givenName”:”Attacker”,  
“familyName”:”K”} 

![](https://i0.wp.com/payatu.com/wp-content/uploads/2023/12/Image-08-12-23-at-3.54-PM.jpeg?resize=800%2C411&ssl=1)

3: Modified the request by changing the attacker’s email to the victim’s email. 

**POST /api/dashboard/login/google HTTP/1.1  
Host: app.domain.com **  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0)  
Cookie:  
{“googleId”:”1234″, “imageUrl”:”[https://abc.com&#8221](https://abc.com&#8221);,  
[**email”:”[email protected]**](/cdn-cgi/l/email-protection#e98c84888085ccdbdbd3ccdbdb888d848087a98d8684888087c78a8684),// Changed email to admin’s email  
“name”:”Attacker”,  
“givenName”:”Attacker”,  
“familyName”:”K”} 

![](https://i0.wp.com/payatu.com/wp-content/uploads/2023/12/Image-08-12-23-at-3.54-PM-1.jpeg?resize=800%2C454&ssl=1)

5: Forward the request. Observe that it redirected to the admin’s account. 

![](https://i0.wp.com/payatu.com/wp-content/uploads/2023/12/Image-08-12-23-at-3.54-PM-2.jpeg?resize=800%2C350&ssl=1)

## **How Did I Discover OAuth-enabled Users and Employees Through Email Enumeration?**

To find out which users and employees had OAuth-enabled accounts, I started by looking for endpoints where I could fuzz email addresses and usernames in the app. After some testing, I was fortunate to find an endpoint using tools like [Paramspider](https://github.com/devanshbatham/ParamSpider) or [waybackurls](https://github.com/tomnomnom/waybackurls). 

The endpoint I discovered was <https://sub.domain.com/xxx/check/?email>=**{email to fuzz}**

**The response from this endpoint was disclosing information about OAuth, 2FA, and passwords.**

{“status”:”success”,”data”:{“email”:”[[email protected]](/cdn-cgi/l/email-protection#54203c3b39352714303b39353d3a7a373b39)“,”status”:{“isExist”:true,”**service”:”auth”** ,”havePassword”:true,”is2FAEnabled”:false,”haveWidData”:true,”userOrigin”:”wid”}}} 

**Screenshot**

![](https://i0.wp.com/payatu.com/wp-content/uploads/2023/12/Image-08-12-23-at-3.55-PM.jpeg?resize=800%2C125&ssl=1)

This endpoint helped me enumerate users with OAuth-enabled accounts. I captured this request in Burp and used Intruder to enumerate usernames using a payload list of usernames from [Seclists](https://github.com/danielmiessler/SecLists) and Employee names in the following format: 

**$user$** @domain.com and **$user$** @gmail.com 

![](https://i0.wp.com/payatu.com/wp-content/uploads/2023/12/Image-08-12-23-at-3.55-PM-1.jpeg?resize=800%2C460&ssl=1)

After Successful execution, we received the “200 OK” response on existing email addresses. 

After getting a list of all the users, I could access over 100 accounts using the OAuth flow. 

### **Mitigation:**

  * Implement strict validation and verification mechanisms for OAuth tokens, ensure proper token expiration, use short-lived tokens, and regularly audit authorized applications. 
  * Implement the rate limit protection to avoid email enumeration. 

### Impact

  * Attackers can identify valid email addresses for targeted phishing and social engineering attacks. 
  * Attackers gain complete control over user or employee accounts, potentially leading to data manipulation and unauthorized actions. 
  * The vulnerability could lead to severe business disruptions, financial losses, and reputational damage.  

### **For Practice and Learning**

  * <https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow>
  * <https://portswigger.net/web-security/oauth/grant-types>
  * <https://infosecwriteups.com/write-up-authentication-bypass-via-oauth-implicit-flow-portswigger-academy-c98b841d3d3d>

Subscribe to our Newsletter

Subscription Form

Δ

Subscribe

![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/06/payatu_logo_red_white.png?fit=800%2C222&ssl=1)

Research Powered Cybersecurity Services and Training. Eliminate security threats through our innovative and extensive security assessments.

###  Subscribe to our newsletter 

Subscription Form

Δ

Subscribe

#### Services

  * [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  * [Red Team Assessment](https://payatu.com/red-team-assessment/)
  * [Product Security Assessment](https://payatu.com/product-security-assessment/)
  * [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  * [Web Application Security Testing](https://payatu.com/web-security-testing/)
  * [SOC Service](https://payatu.com/soc-service/)

Hamburger Toggle Menu __

  * [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  * [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  * [Code Review Service](https://payatu.com/code-review-service/)
  * [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  * [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)

Hamburger Toggle Menu __

#### Products

  * [ExPLIoT](https://expliot.io/)
  * [CloudFuzz](https://cloudfuzz.io/)

Hamburger Toggle Menu __

#### Conference

  * [Nullcon](https://nullcon.net/)
  * [Hardwear.io](https://hardwear.io/)

Hamburger Toggle Menu __

#### Resources

  * [Blog](https://payatu.com/blog/)
  * [Masterclass](https://payatu.com/masterclass-series/)
  * [Case Studies](https://payatu.com/case-studies/)
  * [Ebooks](https://payatu.com/ebooks/)
  * [Advisory](https://payatu.com/advisory/)
  * [Media](https://payatu.com/media/)
  * [Checklist](https://payatu.com/checklist/)
  * [Reports](https://payatu.com/reports/)
  * [Datasheet](https://payatu.com/datasheet/)
  * [CISO Corner](https://payatu.com/ciso-corner/)
  * [Infographics](https://payatu.com/infographics/)

Hamburger Toggle Menu __

#### About

  * [Career](https://payatu.com/career/)
  * [About Us](https://payatu.com/about-us/)
  * [News](https://payatu.com/news/)
  * [Contact-Us](https://payatu.com/contact-us/)
  * [Payatu Bandits](https://payatu.com/bandits/)
  * [WhatsApp Community](https://payatu.com/whatsapp-community/)
  * [Hardware-Lab](https://payatu.com/hardware/)
  * [Disclosure Policy](https://payatu.com/payatu-disclosure-policy/)
  * [Corporate Partners](https://payatu.com/corporate-partners/)

Hamburger Toggle Menu __

[ Youtube __](https://www.youtube.com/@payatu) [ Linkedin __](https://www.linkedin.com/company/payatu/) [ Facebook __](https://www.facebook.com/payatutechnologies) [ Twitter __](https://twitter.com/payatulabs) [ Instagram __](https://www.instagram.com/payatubandit/) [ Whatsapp __](https://payatu.com/whatsapp-community/)

All rights reserved © 2026 Payatu

  * [Home](https://payatu.com/)
  * [News](https://payatu.com/news/)
  * [Advisory](https://payatu.com/advisory/)
  * [Hardware-Lab](https://payatu.com/hardware/)
  * [Contact-Us](https://payatu.com/contact-us/)
  * [Career](https://payatu.com/career/)
  * [Telegram Community](https://payatu.com/community/)

____

  * [Home](https://payatu.com/)
  * [News](https://payatu.com/news/)
  * [Advisory](https://payatu.com/advisory/)
  * [Hardware-Lab](https://payatu.com/hardware/)
  * [Contact-Us](https://payatu.com/contact-us/)
  * [Career](https://payatu.com/career/)
  * [Telegram Community](https://payatu.com/community/)

[ Youtube __](https://www.youtube.com/@payatu5031) [ Linkedin __](https://www.linkedin.com/company/payatu/) [ Facebook __](https://www.facebook.com/payatutechnologies) [ Twitter __](https://twitter.com/payatulabs) [ Instagram __](https://www.instagram.com/payatubandit/) [ Telegram __](https://payatu.com/community/)

  * Services
  * [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  * [Red Team Assessment](https://payatu.com/red-team-assessment/)
  * [Product Security Assessment](https://payatu.com/product-security-assessment/)
  * [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  * [Web Application Security Testing](https://payatu.com/web-security-testing/)
  * [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  * [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  * [Code Review Service](https://payatu.com/code-review-service/)
  * [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  * [SOC Service](https://payatu.com/soc-service/)
  * [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  * Industries
  * [Automotive-Security](https://payatu.com/automotive-security/)
  * [IT/SaaS Security](https://payatu.com/it-saas-security/)
  * [FinTech Security](https://payatu.com/fintech-bfsi-security/)
  * [MedTech Security](https://payatu.com/medtech-security/)
  * [Telecom Security](https://payatu.com/telecom-security/)
  * Products
  * [EXPLIoT](https://expliot.io/)
  * [CloudFuzz](https://cloudfuzz.io/)
  * Who we are
  * [About Us](https://payatu.com/about-us/)
  * [Payatu Bandits](https://payatu.com/bandits/)
  * Resources
  * [Blog](https://payatu.com/blog/)
  * [Masterclass Series](https://payatu.com/master-class-security-series/)
  * [Ebooks](https://payatu.com/ebooks/)
  * [Advisory](https://payatu.com/advisory/)
  * [Media](https://payatu.com/media/)
  * [Checklist](https://payatu.com/checklist/)
  * [BugBazaar](https://payatu.com/bugbazaar/)
  * [securecode.wiki](http://securecode.wiki)
  * [Telegram Community](https://payatu.com/community/)
  * [News](https://payatu.com/news/)
  * [Advisory](https://payatu.com/advisory/)
  * [Hardware-Lab](https://payatu.com/hardware/)
  * [Career](https://payatu.com/career/)
  * [Contact-Us](https://payatu.com/contact-us/)
  * [Pune Location](https://payatu.com/contact-us/#pune-location)
  * [Europe Location](https://payatu.com/contact-us/#europe-location)
  * [Australia Location](https://payatu.com/contact-us/#australia-location)
  * [USA Location](https://payatu.com/contact-us/#usa-location)

  * Services
  * [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  * [Red Team Assessment](https://payatu.com/red-team-assessment/)
  * [Product Security Assessment](https://payatu.com/product-security-assessment/)
  * [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  * [Web Application Security Testing](https://payatu.com/web-security-testing/)
  * [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  * [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  * [Code Review Service](https://payatu.com/code-review-service/)
  * [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  * [SOC Service](https://payatu.com/soc-service/)
  * [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  * Industries
  * [Automotive-Security](https://payatu.com/automotive-security/)
  * [IT/SaaS Security](https://payatu.com/it-saas-security/)
  * [FinTech Security](https://payatu.com/fintech-bfsi-security/)
  * [MedTech Security](https://payatu.com/medtech-security/)
  * [Telecom Security](https://payatu.com/telecom-security/)
  * Products
  * [EXPLIoT](https://expliot.io/)
  * [CloudFuzz](https://cloudfuzz.io/)
  * Who we are
  * [About Us](https://payatu.com/about-us/)
  * [Payatu Bandits](https://payatu.com/bandits/)
  * Resources
  * [Blog](https://payatu.com/blog/)
  * [Masterclass Series](https://payatu.com/master-class-security-series/)
  * [Ebooks](https://payatu.com/ebooks/)
  * [Advisory](https://payatu.com/advisory/)
  * [Media](https://payatu.com/media/)
  * [Checklist](https://payatu.com/checklist/)
  * [BugBazaar](https://payatu.com/bugbazaar/)
  * [securecode.wiki](http://securecode.wiki)
  * [Telegram Community](https://payatu.com/community/)
  * [News](https://payatu.com/news/)
  * [Advisory](https://payatu.com/advisory/)
  * [Hardware-Lab](https://payatu.com/hardware/)
  * [Career](https://payatu.com/career/)
  * [Contact-Us](https://payatu.com/contact-us/)
  * [Pune Location](https://payatu.com/contact-us/#pune-location)
  * [Europe Location](https://payatu.com/contact-us/#europe-location)
  * [Australia Location](https://payatu.com/contact-us/#australia-location)
  * [USA Location](https://payatu.com/contact-us/#usa-location)

DOWNLOAD THE DATASHEET

Fill in your details and get your copy of the datasheet in few seconds

DOWNLOAD THE EBOOK

Fill in your details and get your copy of the ebook in your **inbox**

Ebook Download

Δ

Your Name

Company Email

How did you hear about Payatu?

Contact Number

Checkbox Field

We're committed to your privacy. Payatu uses the information you provide to us to contact you about our relevant content, products, and services. You may unsubscribe from these communications at any time.

Download Now 

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download ICS Sample Report

Δ

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download Cloud Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download IoT Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download Code Review Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download Red Team Assessment Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download AI/ML Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download DevSecOps Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download Product Security Assessment Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download Mobile Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

DOWNLOAD A SAMPLE REPORT

Fill in your details and get your copy of sample report in few seconds

Download Web App Sample Report

Δ

Contact Number

How did you hear about Payatu?

Download

Let’s make cyberspace secure together!

Requirements

Connect Now Form

Δ

I am Interested in:

Cybersecurity Services

Cybersecurity Training

Select Service

Web Application Security

Mobile application Security

IoT Product Ecosystem Security

Red Team Assessment

Cloud Application and Infrastructure Security

Code Review

Threat Modeling and Architecture Review

Product Security Assurance Programme

Cyber Investigation and Forensic

Critical Infrastructure Security Assessment

Blockchain Security Audit

Other Cyber Security Services

Select the reason for an assessment.

Regulatory Compliance

Pass a vendor assessment

Product release

Find vulnerabilities (Proactiveness)

Select a tentative start time.

Right Away (ASAP)

Within 2 weeks

Within 4 weeks

I am flexible

Select Training

Practical IoT Hacking

Web Security

Mobile Security

Exploitation

Machine Learning Security

Cloud Security

Network Infrastructure Security

Red Team Assessment

Practical DevSecOps

Attack Monitoring for SOC

Any Other

Contact information

Organization

Designation 

Select DesignationDirectorCXOSenior LeaderSecurity ConsultantCISOAny other

Offical Email ID

Contact Number 

How did you hear about Payatu?

Lets Connect

What our clients are saying!

Trade Ledger takes privacy and security of it’s customers and system very seriously. We needed an independent audit to check our systems, and wanted to partner with a team that understands the compliance environment of banks. 

![MARTIN MECCAN](https://i0.wp.com/payatu.com/wp-content/uploads/2022/11/image-3.png?fit=68%2C68&ssl=1)

MARTIN MECCANCEO - TradeLedger Australia

Trusted by

![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/11/Group-60.png?fit=420%2C215&ssl=1)
