---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-02_filezilla-fzsftp-untrusted-search-path.md
original_filename: 2019-04-02_filezilla-fzsftp-untrusted-search-path.md
title: FileZilla 'fzsftp' Untrusted Search Path
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 986d494ff0ac54e22597415218a2a95ca88fe8a7344bec3cb84c1bc247a44986
text_sha256: c82c5d4eae5bd2079126972d8dfb65997d3f462514f4477e4861ba7d3afbbe22
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# FileZilla 'fzsftp' Untrusted Search Path

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-02_filezilla-fzsftp-untrusted-search-path.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `986d494ff0ac54e22597415218a2a95ca88fe8a7344bec3cb84c1bc247a44986`
- Text SHA256: `c82c5d4eae5bd2079126972d8dfb65997d3f462514f4477e4861ba7d3afbbe22`


## Content

---
title: "FileZilla 'fzsftp' Untrusted Search Path"
page_title: "FileZilla 'fzsftp' Untrusted Search Path - Research Advisory | Tenable®"
url: "https://www.tenable.com/security/research/tra-2019-14"
final_url: "https://www.tenable.com/security/research/tra-2019-14"
authors: ["Chris Lyne (@lynerc)"]
programs: ["FileZilla (EU-FOSSA 2)"]
bugs: ["RCE"]
publication_date: "2019-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5334
---

* [← View more research advisories](/security/research)

### Synopsis

Tenable has discovered that FileZilla is affected by an untrusted search path vulnerability. The 'fzsftp' binary, which is used to perform SFTP operations, can be loaded from one of many untrusted file paths. These paths are searched in the CFileZillaApp::CheckExistsTool method inside FileZilla.cpp. If an attacker were to convince a user to download a malicious 'fzsftp' binary to his/her home directory, this executable would be launched after FileZilla restarts and opens an SFTP connection.  

##### Proof of Concept

  1. Victim user opens FileZilla client application.
  2. Attacker has modified and compiled psftp.c to include a payload of his/her choosing.
  3. Attacker convinces victim to connect to his/her server using FileZilla. Victim is tricked into downloading the attacker's malicious 'fzsftp' binary to the victim's home directory.
  4. Victim restarts the FileZilla client.
  5. Victim opens a new SFTP connection to any server.

The attacker code would have been executed at this point.

### Solution

Upgrade to FileZilla 3.41.0 or newer.

### Disclosure Timeline

02/19/2019 - Tenable submits bug report to HackerOne

02/20/2019 - HackerOne states that the report is being reviewed

02/20/2019 - Issue is reproducible. HackerOne will check with product team to see if they intend to fix the issue.

02/21/2019 - The report was validated and submitted to the appropriate team for remediation. Issue severity is reduced to Low.

02/21/2019 - Tenable disagrees with severity change. 

02/22/2019 - HackerOne stands firm on their reasoning for dropping the severity.

02/22/2019 - HackerOne indicates that the bug was validated by the Notepad++ team and will be sent to the European Commission for final approval to pay out a bounty.

02/22/2019 - Tenable thanks HackerOne for the update. 

02/23/2019 - HackerOne indicates that the bug was validated by the FileZilla team and will be sent to the European Commission for final approval to pay out a bounty. 

03/14/2019 - Tenable asks for an update.

03/15/2019 - HackerOne indicates that the bug was validated and is now pending bounty by the European Commission. Could take up to 90 days.

03/19/2019 - FileZilla thanks Tenable for the report. Vulnerability has been confirmed. Bounty is sent out. 

03/20/2019 - Tenable asks when a patch is planned. 

03/20/2019 - HackerOne indicates that a fix was released two weeks prior. 

03/20/2019 - Tenable sends a reminder about our disclosure policy and our intent to disclose the bug.

03/21/2019 - HackerOne asks to be kept up to date about an advisory. 

03/27/2019 - Tenable indicates that an advisory will be released 3/28.

04/26/2019 - HackerOne notifies Tenable that CVE-2019-5429 was assigned.

_All information within TRA advisories is provided “as is”, without warranty of any kind, including the implied warranties of merchantability and fitness for a particular purpose, and with no guarantee of completeness, accuracy, or timeliness. Individuals and organizations are responsible for assessing the impact of any actual or potential security vulnerability._

_Tenable takes product security very seriously. If you believe you have found a vulnerability in one of our products, we ask that you please work with us to quickly resolve it in order to protect customers. Tenable believes in responding quickly to such reports, maintaining communication with researchers, and providing a solution in short order._

_For more details on submitting vulnerability information, please see our[Vulnerability Reporting Guidelines](/security/report) page._

_If you have questions or corrections about this advisory, please email[[email protected]](/cdn-cgi/l/email-protection#ea889f8d829f849e8f9899aa9e8f848b88868fc4898587)_

### Risk Information

**CVE ID:** [CVE-2019-5429](https://www.tenable.com/cve/CVE-2019-5429)  

**Tenable Advisory ID:** TRA-2019-14 

**Credit:**  
Chris Lyne 

**CVSSv2 Base / Temporal Score:**  
6.8 / 5.6 

**CVSSv2 Vector:**  
(AV:N/AC:M/Au:N/C:P/I:P/A:P) 

**Affected Products:**  
FileZilla 3.40.0 and prior 

**Risk Factor:**  
Medium 

### Advisory Timeline

03-28-2019 - [R1] Initial Release

04-29-2019 - [R2] CVE added and timeline updated.
