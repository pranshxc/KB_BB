---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-15_microsoft-azure-portal-persistent-cross-site-scripting.md
original_filename: 2021-09-15_microsoft-azure-portal-persistent-cross-site-scripting.md
title: Microsoft Azure Portal – Persistent Cross-Site Scripting
category: documents
detected_topics:
- xss
- access-control
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- access-control
- command-injection
- cloud-security
language: en
raw_sha256: 7c7b71cd31c55681b3481a54e386817e91c22848737ecfaf78b0a6b9d5686b03
text_sha256: bf3f2b4a64fb0ef8b77fc902b8957f1898c3cd8519d5bacba4ed8c216999568b
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Azure Portal – Persistent Cross-Site Scripting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-15_microsoft-azure-portal-persistent-cross-site-scripting.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `7c7b71cd31c55681b3481a54e386817e91c22848737ecfaf78b0a6b9d5686b03`
- Text SHA256: `bf3f2b4a64fb0ef8b77fc902b8957f1898c3cd8519d5bacba4ed8c216999568b`


## Content

---
title: "Microsoft Azure Portal – Persistent Cross-Site Scripting"
page_title: "Microsoft Azure Portal - Persistent Cross-Site Scripting - Y-Security GmbH"
url: "https://www.y-security.de/news-en/microsoft-azure-portal-persistent-cross-site-scripting/index.html"
final_url: "https://www.y-security.de/news-en/microsoft-azure-portal-persistent-cross-site-scripting/index.html"
authors: ["Christian Becker (@0xchrisb)", "Sven Schlüter (@secsven)"]
programs: ["Microsoft"]
bugs: ["Stored XSS"]
publication_date: "2021-09-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3316
---

##  Microsoft Azure Portal – Persistent Cross-Site Scripting 

**Item** |  **Comment**  
---|---  
Software  |  Microsoft Azure Portal  
URL  |  [**https://portal.azure.com**](https://portal.azure.com)  
Type of Issue  |  Persistent Cross-Site Scripting  
CWE  |  [**https://cwe.mitre.org/data/definitions/79.html**](https://cwe.mitre.org/data/definitions/79.html)  
OWASP  |  [**https://owasp.org/www-community/attacks/xss/**](https://owasp.org/www-community/attacks/xss/)  
Roles affected  |  All  
Privilege Escalation  |  User to Administrator  
CVSS  |  [**High – 7.7**](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:N&version=3.1)  
Credits  |  [**Christian Becker**](https://twitter.com/0xchrisb) & [**Sven Schlüter**](https://www.twitter.com/secsven) from Y-Security  
  
##  Summary 

The notification widget of the Microsoft Azure Portal does not encode certain HTML characters. This allows to inject HTML and JavaScript code into the Azure Portal, which is reflected for other users (of the same Azure Active Directory Tenant). 

![](../../y-content/uploads/2021/09/AzureXSS-Preview-small.png)

The Persistent Cross-Site Scripting attack would allow to read and modify the content of the logged in user and provide a possibility to escalate privilege to those of a Portal Administrator. 

###  Video 

##  Steps to reproduce 

Multiple ways to inject JavaScript code exists and we will show as an example how a standard user can attack an administrator in a Cross-Site Scripting attack: 

###  **1st: Steps for the Attacker (low privileged user)**

  * Open **<https://portal.azure.com>**
  * Browse to “Azure Active Directory” 
  * Go to “Groups” 
  * Select “New Group” 
  * Provide a “Group name” of “Y<a target=”_parent” href=”javascript:alert(document.domain)//mailto:”>Y-Security“ and hit “Create” 

###  **2nd: Steps for the Administrator to trigger the attack**

  * Open **<https://portal.azure.com>**
  * Browse to “Azure Active Directory” 
  * Go to “Users” and click any user 
  * Under “Manage –> Groups” click “Add memberships” 
  * Add the previous created group “Y<a target=”_parent” href=”javascript:alert(document.domain)//mailto:”>Y-Security“ by clicking on it and hit “Select” 

The Microsoft Azure Portal automatically confirms the action with a notification on the upper right, which was found to render certain HTML tag: 

![](../../y-content/uploads/2021/08/U32oX7dbrBo4WNUOJZtScOqyKwYNpUOH-notification1.png) Automatic notification of added group membership 

The malicious code is also displayed in the Notifications panel (bell) and placed persistent in the notification widget: 

![](../../y-content/uploads/2021/08/U32oX7dbrBo4WNUOJZtScOqyKwYNpUOH-notification2.png) Rendered payload in Notifications widget 

The JavaScript code entered as part of the payload is executed whenever the text is clicked: 

![](../../y-content/uploads/2021/08/U32oX7dbrBo4WNUOJZtScOqyKwYNpUOH-portal-1920x520.png) Executed JavaScript payload on portal.azure.com 

The JavaScript code is executed every time the group is used and gets displayed in the notification bar – making it a persistent issue. 

###  **Details of the attack vector**

In the below we have split up the attack vector to explain it in more detail: 
  
  
  Y<a target="_parent" href="javascript:alert(document.domain)//mailto:">Y-Security
  

**Injection** |  **Description**  
---|---  
Y  |  A single character is needed before an HTML element can be used  
<a  |  Opening for the a element  
target=”_parent”  |  By default the _target would be “_blank” and hence not executing our code  
href=”  |  Opening for the a href attribut  
javascript:alert(document.domain)  |  JavaScript code to display the current domain in an alert box  
//mailto:  |  The double slash is required to end the JavaScript command/comment out all further code. The **mailto:** is required to bypass the filter  
href=”  |  Closing href attribute value  
>Y-Security  |  Closing the A Element and appending a String  
  
####  **Root Cause – Bypass of Allowed URL handlers**

We have bypassed the allowed URL handlers by appending a **mailto:**. The following code snippet is from [**https://portal.azure.com/Content/Dynamic/jLscZOlMp2-g.js**](https://portal.azure.com/Content/Dynamic/jLscZOlMp2-g.js): 
  
  
  var d = MsPortalFx.Base.Diagnostics, f = /^(vstfs:|ftp:|ftps:|sftp:|storageexplorer:|adlalink:|adl:|asalink:|vscode:|vsweb:|azuredatastudio:|bfcomposer:|)\/\/|mailto:/, l = /^#(allservices|asset|blade|create|dashboard|home|menu|resource)\b/, e = /^#/, a = /^(data:image)\//;
  

The regular expression for all allowed protocol handlers requires “to start with one of the defined URL handlers followed by a double slash”, for example “ftp://”. **mailto:** is the only protocol handler which does not require a double slash and therefore is shown in an extra list. The “starts-with” (`^`) regular expression is missing: **|mailto:**. That allowed us to place the **mailto:** anywhere in the URI scheme and still get a valid response from the filter/regular expression. 

###  Variants 

We believe the URL handler bypass for **mailto:** is generic and could be abused in other places as well. The root issue relies in the notification widget, but can be triggered also when: 

  * Adding a new Administrative unit with a malicious name (like the above **a** Element) and assigning that unit to a group 
  * Adding a new user with a malicious display name (like the above **a** Element) and adding that user to a group 

Another example of this generic injection can be found under [**https://portal.azure.com/#create/Microsoft.KeyVault**](https://portal.azure.com/#create/Microsoft.KeyVault) using the **Create Key Vault** option with the payload in the **Key vault name**. The injection is reflected in the error message. 

###  Recommendation 

The **mailto:** filter should be changed to make sure it needs to be at the start of the string. This would already remediate the injection of JavaScript code in this instance. To mitigate against HTML injection it is recommended to perform HTML encoding. 

###  Fix (10.09.2021) 

The single character fix to mitigate the issue has been rolled out on the 9th of September 2021: 
  
  
  var d = MsPortalFx.Base.Diagnostics, f = /^(vstfs:|ftp:|ftps:|sftp:|storageexplorer:|adlalink:|adl:|asalink:|vscode:|vsweb:|azuredatastudio:|bfcomposer:|ms-quick-assist:|ms-remote-assist:|)\/\/|^mailto:/, l = /^#(allservices|asset|blade|create|dashboard|home|menu|resource)\b/, e = /^#/, a = /^(data:image)\//;
  

Now, it is verified that **mailto** is at the start of the URL scheme which prevents the above payload from being executed. It is still possible to inject some HTML characters but we couldn’t identify another vector to bypass the security controls and inject JavaScript within the time spend on the application. 

##  Timeline 

We have disclosed the issue to Microsoft MSRC and the public with the following timeline: 

**Date** |  **Comment**  
---|---  
19.08.2021  |  Issue discovered  
20.08.2021  |  Issue exploitability verified  
20.08.2021  |  Issue opened with Microsoft MSRC  
08.09.2021  |  Behavior confirmed & Investigation Started  
09.09.2021  |  Issue remediated  
10.09.2021  |  Added mitigation description & internal release  
15.09.2021  |  Coordinated Public Disclosure  
  
##  Disclosure Policy 

Please note: The vulnerability is subjected under the Y-Security Disclosure policy that be found here: [**https://www.y-security.de/disclosure-policy/index.html**](../../disclosure-policy/index.html)

##  Read more articles 

[__# Previous Post All You Need To Know About Threat Intelligence-Based Ethical Red-Teaming](../all-you-need-to-know-about-threat-intelligence-based-ethical-red-teaming/index.html)

[__# Next Post Threat Simulation – Mimicking an APT](../threat-simulation-mimicking-an-apt/index.html)
