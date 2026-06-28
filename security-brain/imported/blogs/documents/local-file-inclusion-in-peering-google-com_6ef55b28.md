---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-21_local-file-inclusion-in-peeringgooglecom.md
original_filename: 2019-05-21_local-file-inclusion-in-peeringgooglecom.md
title: Local File Inclusion in peering.google.com
category: documents
detected_topics:
- path-traversal
- ssrf
- command-injection
- information-disclosure
tags:
- imported
- documents
- path-traversal
- ssrf
- command-injection
- information-disclosure
language: en
raw_sha256: 6ef55b2810787f77965b215d8a2d391888e487549f22856b0533d776406f29da
text_sha256: a2584143df9f1d148f2e2da647e3007bace7b7af3c2cd3fa93dcd554b2124aba
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Local File Inclusion in peering.google.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-21_local-file-inclusion-in-peeringgooglecom.md
- Source Type: markdown
- Detected Topics: path-traversal, ssrf, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `6ef55b2810787f77965b215d8a2d391888e487549f22856b0533d776406f29da`
- Text SHA256: `a2584143df9f1d148f2e2da647e3007bace7b7af3c2cd3fa93dcd554b2124aba`


## Content

---
title: "Local File Inclusion in peering.google.com"
page_title: "Local File Inclusion in peering.google.com - Update - أب ديت"
url: "https://www.updatelap.com/2019/05/local-file-inclusion-in-peeringgooglecom.html"
final_url: "https://www.updatelap.com/2019/05/local-file-inclusion-in-peeringgooglecom.html"
authors: ["Jafar Abo Nada (@Jafar_Abo_Nada)"]
programs: ["Google"]
bugs: ["LFI"]
bounty: "3,133.7"
publication_date: "2019-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5252
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqA21ve_tVmgELVQh8dhOOVs9o7RUDHn7QCGcbzq4BxsG4KxeeXu8XI23dvML-wgWPXlk24Ifp5WGmCTzpCDBnjcNDKYG-18v9RvS8W0MQWkoM4optC7ozSurAO8fd5P1eWWZMfMd6lx0g/s640/local-file-inclusion-vulnerability-sm.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqA21ve_tVmgELVQh8dhOOVs9o7RUDHn7QCGcbzq4BxsG4KxeeXu8XI23dvML-wgWPXlk24Ifp5WGmCTzpCDBnjcNDKYG-18v9RvS8W0MQWkoM4optC7ozSurAO8fd5P1eWWZMfMd6lx0g/s1600/local-file-inclusion-vulnerability-sm.jpg)  

### 

##  I found an Local File Inclusion 'LFI' Vulnerability in "Google's Edge Network".

#####  Description

  

As it is known, the impacts of exploiting a Local File Inclusion (LFI) vulnerability vary from information disclosure to complete compromise of the system. Even in cases where the included code is not executed, it can still give an attacker enough valuable information to be able to compromise the system,As is the case of the security vulnerability we are reporting. 

#####  Impact

disclosed Local server information 

  

  

#####  Reproduction Steps

  1. Go to "<https://peering.google.com/>".

  2. Open any picture in another window for example: "<https://peering.google.com/static/images/couch-ipad.png>".

  3. Add one of this value at the end of the link: ("../../../../../../../etc/passwd") OR ("../../../../../../../proc/self/cmdline") OR ("../../../../../../../proc/self/stat") OR ("../../../../../../../proc/self/status").

  4. .In this way: "https://peering.google.com/static/images/couch-ipad.png../../../../../../../proc/self/cmdline".

  5. Now you are viewing sensitive information about the server.

  

####  Example Leak Data:

1.The attacker gets information about the server and Kernel data. PoC: "/proc/version" OR "/proc/cpuinfo" OR "proc/meminfo") Example leak data: "Linux version 3.*.* #1 SMP"  
  
2.The attacker gets information about the files on the server. PoC:"proc/self/cmdline") Example: "server_software=Google App Engine/1.*.*  
  
3.The attacker gets information about the internal network. PoC:"proc/self/cmdline") Example:"apihost_address=169.*.*.253:* /server_address=169.*.*.2:*"  
  
4.The attacker gets information about the operations and the time they run on the server. PoC: "proc/self/stat") Example: "(python27g_runti)"  
  
5.The attacker gets sensitive information about the operation processes and the ability of the system that can contribute well in measuring the size of denial of service attacks. PoC: "proc/self/status"). Example: "FDSize: 11, VmSize: 1134532 kB, VmRSS: 134860 kB, Threads: 17" 

  

and More...
