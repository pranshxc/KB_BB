---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-17_dropbox-escalation-of-privileges-to-system-on-windows.md
original_filename: 2020-09-17_dropbox-escalation-of-privileges-to-system-on-windows.md
title: Dropbox Escalation of Privileges to SYSTEM on Windows
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 3103034679907763f4982278fbed607eebdce7134f3663cb31f7c09697888f08
text_sha256: e36a90d50d6729600ddd6884a8ae0c0f5d4978b8135d4c55d762775600b35654
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Dropbox Escalation of Privileges to SYSTEM on Windows

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-17_dropbox-escalation-of-privileges-to-system-on-windows.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `3103034679907763f4982278fbed607eebdce7134f3663cb31f7c09697888f08`
- Text SHA256: `e36a90d50d6729600ddd6884a8ae0c0f5d4978b8135d4c55d762775600b35654`


## Content

---
title: "Dropbox Escalation of Privileges to SYSTEM on Windows"
page_title: "Dropbox Escalation of Privileges to SYSTEM on Windows - Dreamlab Technologies"
url: "https://dreamlab.net/en/blog/post/dropbox-escalation-of-privileges-to-system-on-windows-1/"
final_url: "https://dreamlab.net/en/blog/post/dropbox-escalation-of-privileges-to-system-on-windows-1/"
authors: ["Teresa Alberto"]
programs: ["Dropbox"]
bugs: ["Local Privilege Escalation"]
publication_date: "2020-09-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4259
---

###### _By Teresa Alberto, Security Researcher at Dreamlab Technologies_

In January of this year we found an EoP (Escalation of Privileges) or LPE (Local Privilege Escalation) in the **Dropbox** Windows application. The bug was already patched in the last Dropbox update. This vulnerability allowed an attacker with low privilege access on a machine to escalate to SYSTEM (highest administrator privileges).

As soon as we found this vulnerability, we reported it to Dropbox through their Bug Bounty Program. They informed us that they were already aware of the vulnerability and had been working on a fix since another researcher (name not disclosed) had recently reported it as well. However, no patch was yet available to the customers.

### Local Privilege Escalation

In general a **local privilege escalation** attack allows privileges to be escalated on a compromised machine from a low privilege user to SYSTEM. More specifically, a **file privilege escalation** attack -such as the one found in Dropbox- relies on the abuse of file operations performed by privileged processes to achieve this goal.

[An interesting aspect of this vulnerability is that it’s considered a “logical vulnerability” because it relies on subverting the programmer’s original logic rather than abusing unintended behaviour.](https://conference.hitb.org/hitbsecconf2017ams/materials/D2T3%20-%20James%20Forshaw%20-%20Introduction%20to%20Logical%20Privilege%20Escalation%20on%20Windows.pdf "Opens internal link in current window")

[As this vulnerability relies on the logic of file manipulation it usually survives code refactoring and becomes very stable to exploit, without the pitfalls involved in memory corruption issues.](https://offsec.almond.consulting/intro-to-file-operation-abuse-on-Windows.html "Opens internal link in current window")

### An automatic Dropbox update from low privileges to SYSTEM

By analysing the Dropbox client for Windows, we realized that the _update component_ was running with system privileges. Oh! What can go wrong?

With the aid of Procmon tool (as part of [SysInternals toolkit](https://docs.microsoft.com/en-us/sysinternals/downloads/)) we were able to monitor the updater process behaviour and discover that this high privilege process was writing log files in the folder `C:\ProgramData\Dropbox\Update\Log`.

![](/wp-content/uploads/2024/11/Dropbox-LPE1.png)

This behaviour caught our attention and we investigated further.

The permissions of that Log directory were actually set by default as writeable by non-privileged users. The privileged process then set permissions on the log files that allowed any user to modify them.

![](/wp-content/uploads/2024/11/Dropbox-LPE2.png)

#### **Exploiting the vulnerability**

In order to leverage this vulnerability, the writing of a file by the privilege process needs to be redirected to a more interesting folder, for example `C:\Windows\System32`. If this can be achieved, then the _DropboxUpdate_ process would write a file to the new target directory and set the permissions to allow a low privilege user to have write access on the files.

To achieve the redirection, the _CreateMountPoint_ tool can be used, one of the amazing [“Symbolic link testing tools”](https://github.com/googleprojectzero/symboliclink-testing-tools) created by James Forshaw. By using CreateMountPoint an NTFS junction can be created. As Clément Lavoillotte states: [“Junctions are an NTFS feature that allows directories to be set as mount points for a filesystem, like a mount point in Unix, but can also be set up to resolve to another directory (on the same or another filesystem)”](https://offsec.almond.consulting/intro-to-file-operation-abuse-on-Windows.html "Opens internal link in current window").

Simply, when using junctions, a sort of directory symbolic link to another target directory is created and -the most important thing- junctions can be created by low privileged users.

![](/wp-content/uploads/2024/11/Dropbox-LPE3.png)

By using CreateMountPoint tool it was possible to turn `C:\ProgramData\Dropbox\Update\Log` into a junction to `C:\Windows\System32` and redirect the privilege writing into an arbitrary and definitely more interesting directory.

To create the junction the following line was run on the Windows console:

`.\CreateMountPoint.exe C:\ProgramData\Dropbox\Update\Log C:\Windows\System32`  
---  
  
Once the symlink is triggered by the DropboxUpdate process, the log files can be seen being written to the `System32` folder:

![](/wp-content/uploads/2024/11/Dropbox-LPE4.png)

Due to the weak permissions setting, the log file can then be replaced with malicious content. From here, there are then several ways in which an attacker can achieve privilege escalation.

Since the report to Dropbox has not been fully disclosed, we will not give details of the exploitation. However, it is possible to develop a working exploit using this vulnerability. The following video shows how a non-privileged user escalates to SYSTEM by abusing this bug: [WATCH VIDEO ](https://dreamlab.net/media/img/blog/2020-09-17-Dropbox-Escalation/dropbox-LPE-final.mp4 "Opens internal link in current window")

To protect yourself from this vulnerability, remember to update Dropbox to the latest version.

#### **Conclusion**

The EoP vulnerability we found in Dropbox client for Windows allows an attacker with low privilege access on a compromised machine to escalate their privileges to SYSTEM.

We want to acknowledge the role of SandboxEscaper’s [blog](http://sandboxescaper.blogspot.com/2019/12/chasing-polar-bears-part-one.html) as an inspiration for this finding and highlight the valuable toolkit developed by James Forshaw for exploiting these kinds of vulnerabilities.

#### **Timeline**

January 12, 2020 – Initial discovery.

January 13, 2020 – Report sent to Dropbox via Hackerone.

January 13, 2020 – Report is triaged and considered duplicated.

July 31, 2020 – A fix resolved the vulnerability.

September 3, 2020 – Our report is disclosed.

![](/wp-content/uploads/2024/11/Dropbox-escalation_09.03.35.png)

[Back __](/en/latest)
