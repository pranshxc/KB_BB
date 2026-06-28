---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-05_multiple-plone-cross-site-scripting-vulnerabilities.md
original_filename: 2017-12-05_multiple-plone-cross-site-scripting-vulnerabilities.md
title: Multiple Plone Cross-Site Scripting Vulnerabilities
category: documents
detected_topics:
- xss
- csrf
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- csrf
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 25aae50e7a090ee1c3e462e393748d2a5de988b9f720fa5a6c13adeeab96cdcd
text_sha256: cd602a22f3595ce0b5f65064a3e6a3650f785c19780ce30baf672a9f6733965b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Plone Cross-Site Scripting Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-05_multiple-plone-cross-site-scripting-vulnerabilities.md
- Source Type: markdown
- Detected Topics: xss, csrf, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `25aae50e7a090ee1c3e462e393748d2a5de988b9f720fa5a6c13adeeab96cdcd`
- Text SHA256: `cd602a22f3595ce0b5f65064a3e6a3650f785c19780ce30baf672a9f6733965b`


## Content

---
title: "Multiple Plone Cross-Site Scripting Vulnerabilities"
url: "https://www.fortinet.com/blog/threat-research/multiple-plone-cross-site-scripting-vulnerabilities"
final_url: "https://www.fortinet.com/blog/threat-research/multiple-plone-cross-site-scripting-vulnerabilities"
authors: ["Zhouyuan Yang"]
programs: ["Plone"]
bugs: ["XSS", "CSRF"]
publication_date: "2017-12-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6035
---

[ ![Fortinet home](/content/dam/fortinet-blog/fortinet-logo-white.svg) ![Fortinet home](/content/dam/fortinet-blog/fortinet-logo-white.svg) ](https://www.fortinet.com/.html)

[ Blog ](https://www.fortinet.com/blog.html)

  * Products & Solutions

  * [ Secure Networking ](http://www.fortinet.com/blog/secure-networking)
  * [ Unified SASE ](http://www.fortinet.com/blog/unified-sase)
  * [ Cloud Security ](http://www.fortinet.com/blog/cloud-security)
  * [ Security Operations ](http://www.fortinet.com/blog/security-operations)
  * [ Operational Technology ](http://www.fortinet.com/blog/operational-technology)
  * Threat Research

  * [ Threat Research ](http://www.fortinet.com/blog/threat-research)
  * [ PSIRT ](http://www.fortinet.com/blog/psirt-blogs)
  * Thought Leadership

  * [ CISO Collective ](http://www.fortinet.com/blog/ciso-collective)
  * [ Industry Trends ](http://www.fortinet.com/blog/industry-trends)
  * [ Security Architecture ](http://www.fortinet.com/blog/security-architecture)
  * Corporate

  * [ Fortinet News & Updates ](http://www.fortinet.com/blog/business-and-technology)
  * [ Partners ](http://www.fortinet.com/blog/partners)
  * [ Customer Success Stories ](http://www.fortinet.com/blog/customer-stories)
  * [ Life at Fortinet ](http://www.fortinet.com/blog/life-at-fortinet)

![Multiple Plone Cross-Site Scripting Vulnerabilities](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=)

[FortiGuard Labs Threat Research](http://www.fortinet.com/blog/threat-research)

# Multiple Plone Cross-Site Scripting Vulnerabilities

By  [Zhouyuan Yang](http://www.fortinet.com/blog/search?author=Zhouyuan+Yang) | December 05, 2017

Plone is a free and open source content management system, and is ranked among the top 2% of all open source projects worldwide. More than 350 solution providers in more than 100 countries currently support it. The project has been actively developed since 2001, is available in more than 40 languages, and has the best security track record of any major CMS. The users (<https://plone.com/about/they-use-plone>) include the Federal Bureau of Investigation (FBI), the Central Intelligence Agency (CIA), the Intellectual Property Rights Center, and so on.

Earlier this year, FortiGuard Labs discovered two cross-site scripting (XSS) vulnerabilities and one cross-site request forgery (CSRF) vulnerability affecting Plone versions from 2.5.5 to 5.1rc1. The first cross-site scripting (XSS) vulnerability exists in the Plone login process and only works in conjunction with the CSRF issue, so Plone has addressed them together in their recent update. The second XSS vulnerability is caused by the home page member property.

## [Plone Login Form XSS & CSRF Vulnerability](https://plone.org/security/hotfix/20171128/open-redirection-on-login-form)

The first XSS vulnerability is caused because the Plone login function incorrectly processes user requests. Combined with a CSRF issue in the login process, remote attackers could run malicious code in a victim’s browser and trigger a XSS attack. This could allow the remote attacker to gain control of the victim’s Plone account. If the victim has higher permission, like system administrator, the attacker could conceivably gain full control of the web server.

### Analysis

When a user logs into Plone with a valid account (any permission), there are 9 parameters in the login request. The server then responds with a 302 redirection containing the value taken from the “came_from” params found in the request response. This is shown in figure 1.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1796.png)

Figure 1. Plone login payload

The issue here is that that attacker can control the value in the param “came_from”, and Plone doesn’t sterilize it in the response.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1797.png)

Figure 2. Param “came_from”

For example, when setting the “came_from” value to![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1798.PNG)Plone will output the HTML tags in the response, as shown below.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1799.png)

Figure 3. Insert HTML tags

Modern browsers will not execute the body part in a 302 response. However, in Firefox (Windows version) we can bypass it by setting the value starts to [mailto:](mailto:) \-- for example, setting the “came_from” value to ![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1800.PNG) Firefox will then load this 302 response, try to open the default email program, and execute the HTML elements in the body.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1801.png)

Figure 4. Bypassing the 302 redirect in Firefox I

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1802.png)

Figure 5. Bypassing the 302 redirect in Firefox II

Finally, there is no CSRF protection in the login process. So with this XSS vulnerability, a valid account (any permission), combined with the CSRF vulnerability and bypass issue in Firefox, an attacker could successfully trigger a XSS attack. The PoC codes are shown in figure 6, and the result is shown in figure 7.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1803.png)

Figure 6. PoC

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1804.jpg)

Figure 7. XSS attack triggered

## [Plone Personal Homepage XSS Vulnerability](https://plone.org/security/hotfix/20171128/xss-using-the-home_page-member-property)

The second XSS vulnerability is caused because the Plone Personal Information Home page function incorrectly processes user requests. Just as with the first XSS vulnerability, remote attackers could run malicious code in a victim’s browser, gain control of the victim’s Plone account, and even gain full control of the web server.

### Analysis

In the Plone Personal Information page, users can set their own information, such as name, email address, home page, and so on.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1805.png)

Figure 8. Personal Information page

The issue is that Plone doesn’t sterilize the home page value before sending it to the server. For example, attackers could set their home page value to “javascript:alert(1)”.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1806.png)

Figure 9. PoC

When the victim accesses the attacker’s personal information page, Plone will then display the home page value (the XSS codes) with![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1807.PNG) If the victim then clicks the home page link, the XSS codes will be triggered.

![](/content/dam/fortinet-blog/new-images/uploads/multiple-plone-cross-site-scripting-vulnerabilities-1808.png)

Figure 10. XSS attack triggered

### Solution

All users of Plone should upgrade to the latest version immediately. Additionally, organizations that have deployed a Fortinet IPS solution are already protected from these vulnerabilities with the signature Plone.Login.Form.XSS and Plone.Personal.Homepage.XSS that were issued as part of our zero day practice once the vulnerabilities were confirmed.

### Reference

<https://plone.org/security/hotfix/20171128>

<https://plone.org/security/hotfix/20171128/open-redirection-on-login-form>

<https://plone.org/security/hotfix/20171128/xss-using-the-home_page-member-property>

<https://fortiguard.com/zeroday/FG-VD-17-006>

<https://fortiguard.com/zeroday/FG-VD-17-007>

_Sign up for our weekly FortiGuard Labs[intel briefs](https://www.fortinet.com/fortiguard/threat-intelligence/threat-research.html) or to be a part of our [open beta](https://www.fortinet.com/fortiguard/threat-intelligence/threat-research.html) of Fortinet’s FortiGuard Threat Intelligence Service._

Tags:

[vulnerabilities](https://www.fortinet.com/blog/tags-search.html?tag=vulnerabilities), [Plone](https://www.fortinet.com/blog/tags-search.html?tag=plone), [firefox](https://www.fortinet.com/blog/tags-search.html?tag=firefox), [csrf](https://www.fortinet.com/blog/tags-search.html?tag=csrf), [fortiguard](https://www.fortinet.com/blog/tags-search.html?tag=fortiguard), [html](https://www.fortinet.com/blog/tags-search.html?tag=html), [xss](https://www.fortinet.com/blog/tags-search.html?tag=xss)

### Related Posts

[ ![Seven Critical Vulnerabilities Discovered in Portainer](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=) Threat Research  Seven Critical Vulnerabilities Discovered in Portainer ](http://www.fortinet.com/blog/threat-research/seven-critical-vulnerabilities-portainer) [ ![Incomplete Patch: More Joomla! Core XSS Vulnerabilities Are Found](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=) Threat Research  Incomplete Patch: More Joomla! Core XSS Vulnerabilities Are Found ](http://www.fortinet.com/blog/threat-research/incomplete-patch-more-joomla-core-xss-vulnerabilities-are-found) [ ![Bindweed: Digging Down to a Root of a Hidden Phishing Network](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=) Threat Research  Bindweed: Digging Down to a Root of a Hidden Phishing Network ](http://www.fortinet.com/blog/threat-research/bindweed--digging-down-to-a-root-of-a-hidden-phishing-network)

[ ![Fortinet](/content/dam/fortinet-blog/fortinet-logo-white.svg) ](https://www.fortinet.com/.html)

  * [ ](https://www.linkedin.com/company/fortinet)
  * [ ](https://www.x.com/Fortinet)
  * [ ](https://www.youtube.com/channel/UCJHo4AuVomwMRzgkA5DQEOA?sub_confirmation=1)
  * [ ](https://www.instagram.com/fortinet/)
  * [ ](https://www.facebook.com/fortinet)
  * [ ](https://www.fortinet.com/rss-feeds.html)

#### News & Articles

  * [News Releases](http://www.fortinet.com/corporate/about-us/newsroom/press-releases)
  * [News Articles](http://www.fortinet.com/corporate/about-us/newsroom/news)

#### Security Research

  * [Threat Research](http://www.fortinet.com/fortiguard/threat-intelligence/threat-research)
  * [FortiGuard Labs](https://fortiguard.com/)
  * [Threat Map](http://www.fortinet.com/fortiguard/threat-intelligence/threat-map)
  * [Ransomware Prevention](http://www.fortinet.com/solutions/ransomware)

#### Connect With Us

  * [Fortinet Community](https://community.fortinet.com/)
  * [Partner Portal](http://www.fortinet.com/partners/partner-program/become-a-fortinet-partner)
  * [Investor Relations](https://investor.fortinet.com/)
  * [Product Certifications](http://www.fortinet.com/corporate/about-us/product-certifications)

#### Company

  * [About Us](http://www.fortinet.com/corporate/about-us/about-us)
  * [Exec Mgmt](http://www.fortinet.com/corporate/about-us/executive-management)
  * [Careers](http://www.fortinet.com/corporate/careers)
  * [Training](http://www.fortinet.com/nse-training)
  * [Events](http://www.fortinet.com/corporate/about-us/events)
  * [Industry Awards](http://www.fortinet.com/corporate/about-us/industry-awards)
  * [Social Responsibility](http://www.fortinet.com/corporate/about-us/corporate-social-responsibility)
  * [CyberGlossary](http://www.fortinet.com/resources/cyberglossary)
  * [Sitemap](http://www.fortinet.com/sitemap)
  * [Blog Sitemap](http://www.fortinet.com/sitemap/blog)

#### 

Copyright © 2026 Fortinet, Inc. All Rights Reserved

[Terms of Services](http://www.fortinet.com/corporate/about-us/legal) [Privacy Policy](http://www.fortinet.com/corporate/about-us/privacy) | Cookie Settings

FORTINET: Cybersecurity everywhere you need it

Also of Interest:

  * [The Analysis of Apache Struts 1 Form Field...](https://www.fortinet.com/blog/threat-research/the-analysis-of-apache-struts-1-form-field-input-validation-bypass-cve-2015-0899)
  * [WordPress WooCommerce XSS Vulnerability –...](https://www.fortinet.com/blog/threat-research/wordpress-woocommerce-xss-vulnerability----hijacking-a-customer-)
  * [WooCommerce Tax Rates Cross-Site Scripting...](https://www.fortinet.com/blog/threat-research/woocommerce-tax-rates-cross-site-scripting-vulnerability2)
  * [Magento Commerce Widget Form (Core) XSS Vulnerability](https://www.fortinet.com/blog/threat-research/magento-commerce-widget-form--core--xss-vulnerability)
