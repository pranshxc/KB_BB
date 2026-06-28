---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-03_leaking-browser-urlprotocol-handlers.md
original_filename: 2020-12-03_leaking-browser-urlprotocol-handlers.md
title: Leaking Browser URL/Protocol Handlers
category: documents
detected_topics:
- rate-limit
- cloud-security
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- rate-limit
- cloud-security
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 3617ef566a3bdadda7b14ab7493f78ec20139817d2a13c546f3929b5df5ff21b
text_sha256: a4e806180a8e096421dbb17e71ca0c0b53133442a50c57a8fce4179a7617888b
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Leaking Browser URL/Protocol Handlers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-03_leaking-browser-urlprotocol-handlers.md
- Source Type: markdown
- Detected Topics: rate-limit, cloud-security, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `3617ef566a3bdadda7b14ab7493f78ec20139817d2a13c546f3929b5df5ff21b`
- Text SHA256: `a4e806180a8e096421dbb17e71ca0c0b53133442a50c57a8fce4179a7617888b`


## Content

---
title: "Leaking Browser URL/Protocol Handlers"
page_title: "Leaking Browser URL/Protocol Handlers | FortiGuard Labs"
url: "https://www.fortinet.com/blog/threat-research/leaking-browser-url-protocol-handlers"
final_url: "https://www.fortinet.com/blog/threat-research/leaking-browser-url-protocol-handlers"
authors: ["Tabahi (@_tabahi)"]
programs: ["Google", "Microsoft", "Mozilla"]
bugs: ["Information disclosure"]
publication_date: "2020-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4094
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

![Leaking Browser URL/Protocol Handlers | FortiGuard Labs](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=)

[FortiGuard Labs Threat Research](http://www.fortinet.com/blog/threat-research)

# Leaking Browser URL/Protocol Handlers

By  [Rotem Kerner](http://www.fortinet.com/blog/search?author=Rotem+Kerner) | December 03, 2020

**[FortiGuard Labs](https://www.fortinet.com/fortiguard/labs.html?utm_source=blog&utm_medium=campaign&utm_campaign=FortiGuardLabs) Threat Research Report  
**

**Affected platforms:** Windows, Linux  
**Impacted parties:** Chrome, Firefox and Edge  
**Impact:** Leaking sensitive data  
**Severity level:** Medium  
**Assigned CVEs:** CVE-2020-15680

An important step in any targeted attack is reconnaissance. The more information an attacker can obtain on the victim the greater the chances for a successful exploitation and infiltration. Recently, we uncovered two information disclosure vulnerabilities affecting three of the major web browsers which can be leveraged to leak out a vast range of installed applications, including the presence of security products, allowing a threat actor to gain critical insights on the target. 

In this post we will discuss what are protocol handlers and disclose two information disclosure vulnerabilities affecting three major browsers (namely - Firefox, Edge and Chrome). Exploiting these vulnerabilities will enable a remote attacker to identify the presence of a vast amount of applications that may be installed on a targeted system.

## Overview - What Are Protocol Handlers?  

Generally speaking when talking about Protocol Handlers we are referring to a mechanism which allows applications to register their own URI scheme. This enables the execution of processes through the use of URI formatted strings. 

The Windows OS manages custom URL handlers under the following key- 

  * HKEY_CURRENT_USER\SOFTWARE\Classes\\*
  * HKEY_LOCAL_MACHINE\SOFTWARE\Classes\\*
  * HKEY_CLASSES_ROOT\\*

When a URL Handler is invoked the OS is searching within those locations for keys containing values with the name  _“URL Protocol”_. 

For instance, we can use  _regedit_ to inspect the path at  _HKEY_CLASSES_ROOT\msteams_ and see that it contains the special Value of  _“URL Protocol”_.

Figure 1

Looking further into  _HKEY_CLASSES_ROOT\msteams\shell\open\command\_ we can see the actual command that gets invoked - 

Figure 2

Figure 3

In this example the browser will launch Teams.exe when a url that starts with “msteams” is clicked.

Web browsers will enable their users to click on links with non-http schemes which will result in prompting the user with a message box asking them if they want to let another application handle this URL. 

Figure 4

Though it requires user interaction and thus poses a limited risk, it expands the attack surface beyond the browser borders. An attacker could craft a special web page which triggers another potentially vulnerable application. In some cases, such attacks may bypass protection measures such as Smart Screen and other security products.

While exploring the potential of attacking the browsers through the different protocol handlers I got curious as to whether web browsers somehow disclose what protocols handlers exist on a targeted system. The short answer is yes. 

## Leaking Protocol Handlers  

In this section we disclose how both Chrome, Edge and Firefox were circumvented in order to disclose which protocol handlers exist on a targeted system. It's worth mentioning that these findings are the result of manually playing with HTML/CSS components with the emphasis on finding a difference in behavior when referring (using some elements) to existing and non-existing URL handlers.

The environment I’ve been testing on is Windows 10 but it is fair to assume that the same vulnerabilities exist on other platforms (such as Linux and Mac).

## Leaking Firefox protocol handlers (CVE-2020-15680)

This vulnerability has been tested on Firefox 78.0.1 (64-bit) under Windows 10. To leak the protocol handlers in Firefox we leverage differences in the way firefox renders images sourced from existing and non-existing protocol handlers.

For example, if we will try to load a web page containing the following element - 

And observe the elements styling using developer tools we would see that the default styling for broken images generate element with size of 24x24 as can be seen in Figure-5.

Figure 5

Unlike the example above, if we try and create an image element and set source to some non-existent handler like the following.

This will result with an element with different sizing of 0x0 as can be seen in Figure-6.  

Figure 6

This difference can be measured using a simple JS script Basing on this a malicious actor may perform a brute-force attack to disclose the different protocol handlers on a targeted system.

The following example code will print whether a handlers exists or not on a targeted system.

## Leaking Chrome and Edge protocol handlers  

This vulnerability has been tested on Chrome 83.0.4103.116 under Windows 10. The exploitability of this vulnerability may be less stealthy but still yields equivalent results as the Firefox vulnerability. 

The mechanism here was different than the one in Firefox, here we leverage the fact that the window lose focus whenever the user is challenged with the message box as can be seen in figure-7.

Figure 7

So, in order to detect if a given handler exists on the victim we take the following steps.

First, we dynamically generate a link that is made of the scheme we would like to detect like such -

Then we trigger the link and detect whether the document has focus:

That will work for a one time check however if we would like to brute force an entire list of handlers we would have to get rid of the message box every time it pops up or else the  _document_.hasFocus() will always return true. 

Figure 8

The technique we came up with was to redirect the user to an entirely different domain/ip which will eliminate any previously opened message box. 

Figure-8 draws the general idea of how the flow should be carried out in order to work.  _Protocol Handler Test page_ performs the actual test and saves the results to the back-end. In case the handler exists, it will redirect to “ _Redirect-Back Page_ ” which exists on domain2.com. The redirection will get rid of the message box. Finally, back to the _Protocol Handler Test Page_ for the next handler test.

## Vulnerabilities Impact

Such information disclosure vulnerability could be exploited in several different ways. Here are some examples:

  * **Identifying communication channels** : By listing the handlers an attacker can get a hint to what platforms he may use for reaching the targeted user. For instance, detecting social applications such as Slack, Skype, WhatsApp or Telegram may be used for communicating with the target. 
  * **General reconnaissance:** A wide range of applications nowadays uses custom URL handlers and can be detected using this vulnerability. Some examples: music players, IDE, office applications, crypto-mining, browsers, mail applications, antivirus, video conferencing, virtualizations, database clients, version control clients, chat clients, voice conference apps, shared storages****
  * **Pre-exploitation detection** : Exploit kits may leverage this information in order to identify if a potentially vulnerable application is present without exposing the vulnerability itself. 
  * **Detecting Security solutions** : Many security solutions such as AV products register protocol handlers whose presence can be exposed by leveraging the vulnerabilities because they have custom protocol handlers installed. Attackers may use this to further customize their attack to be able to circumvent any protection mechanism set by those security solutions.
  * **User Fingerprinting** : reading what protocol handlers exist on a system may also be used in order to improve browser/user fingerprinting algorithms.****

## Vendor Response  

Below is a table specifying the vendor responses:

**Vendor** |  **Vendor Response**  
---|---  
**Mozilla** |  The security team at mozilla were quick to respond and have issued a fix for the bug. - CVE-2020-15680  
**Microsoft** |  The vendor decided not to fix the issue due to the following explanation -  _“This is by design (and not a security issue) - if we want to support registered protocol handler links from the browser, it seems like there'll be various ways to detect whether a link for a particular protocol handler worked or not”_  
**Google** |  The vendor decided to treat this as a “user fingerprinting issue” rather than a security issue and are working on a patch. _“The general consensus on the security team is that none of the concerns here relate to leaking user data, and that this is best handled as a fingerprinting bug”_  
  
## Summary

In this post we uncovered a new type of information disclosure vulnerabilities in Chrome, Edge and Firefox and identified how attackers can leverage them to gain valuable insights which could assist them in compromising their targets. When browsers are enabling the interaction with other applications through URL handlers, they may be easing the engagement with third party software, but they also enable a wider attack surface by giving the attacker a chance to attack the user through other applications.

While Microsoft and Google currently don't consider it a security issue, we believe that being able to expose the presence of other software, including security software, on targeted devices should be prevented.

With that being said, we anticipate that in the near future we shall see an increase in the number of attacks which exploit the different URL handlers through the user's web browser.

[FortiEDR](https://www.fortinet.com/products/endpoint-security/fortiedr.html?utm_source=blog&utm_campaign=2020-q1-fortiedr) can detect and block these browser-based exploits and provide visibility into such attempts. 

_Learn more about[FortiGuard Labs](https://www.fortinet.com/fortiguard/labs.html?utm_source=blog&utm_medium=campaign&utm_campaign=FortiGuardLabs) threat research and the FortiGuard Security Subscriptions and Services [portfolio](https://www.fortinet.com/support/support-services/fortiguard-security-subscriptions?utm_source=blog&utm_campaign=2020-q2-security-subscriptions). [Sign up](https://secure.fortinet.com/FortiGuard) for the weekly Threat Brief from FortiGuard Labs. _

_Learn more about Fortinet’s[free cybersecurity training initiative](https://www.fortinet.com/blog/business-and-technology/why-cybersecurity-training-is-more-important-than-ever.html) or about the Fortinet [Network Security Expert program](https://training.fortinet.com/?utm_source=blog&utm_campaign=2019-q3-nse-institute), [Network Security Academy program](https://training.fortinet.com/local/staticpage/view.php?page=fnsa&utm_source=blog&utm_campaign=2019-q3-fnsa), and [FortiVet program](https://www.fortinet.com/corporate/careers/vets.html?utm_source=blog&utm_campaign=2018-q2-fortivet)._

Tags:

[FortiGuard Labs](https://www.fortinet.com/blog/tags-search.html?tag=fortiguard-labs), [AI-Driven Security Operations](https://www.fortinet.com/blog/tags-search.html?tag=ai-driven-security-operations), [Cybersecurity Architect](https://www.fortinet.com/blog/tags-search.html?tag=cybersecurity-architect)

### Related Posts

[ ![Scammers Using COVID-19/Coronavirus Lure to Target Medical Suppliers](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=) Threat Research  Scammers Using COVID-19/Coronavirus Lure to Target Medical Suppliers ](http://www.fortinet.com/blog/threat-research/scammers-using-covid-19-coronavirus-lure-to-target-medical-suppliers) [ ![EKANS Ransomware: A Malware Targeting OT ICS Systems](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=) Threat Research  EKANS Ransomware: A Malware Targeting OT ICS Systems ](http://www.fortinet.com/blog/threat-research/ekans-ransomware-targeting-ot-ics-systems) [ ![Leveraging the Darknet for Threat Intelligence](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAQAAAAe/WZNAAAADklEQVR42mNkgAJGDAYAAFEABCaLYqoAAAAASUVORK5CYII=) Threat Research  Leveraging the Darknet for Threat Intelligence ](http://www.fortinet.com/blog/threat-research/how-threat-researchers-leverage-darknet-to-stay-ahead-of-cyber-threats)

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

  * [FortiGuard Labs Discovers Multiple Critical...](https://www.fortinet.com/blog/threat-research/fortiguard-lab-researcher-discovers-multiple-critical-vulnerabilities-in-adob-illustrator-cc-2020)
  * [Analysis of CVE-2016-0059 - Microsoft IE...](https://www.fortinet.com/blog/threat-research/analysis-of-cve-2016-0059-microsoft-ie-information-disclosure-vulnerability-discovered-by-fortinet)
  * [Multiple Critical Vulnerabilities in Adobe...](https://www.fortinet.com/blog/threat-research/multiple-critical-vulnerabilities-in-adobe-illustrator-and-effects-products)
  * [Burning Zero Days: Suspected Nation-State...](https://www.fortinet.com/blog/threat-research/burning-zero-days-suspected-nation-state-adversary-targets-ivanti-csa)
