---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-25_the-logging-dead-two-event-log-vulnerabilities-haunting-windows.md
original_filename: 2022-10-25_the-logging-dead-two-event-log-vulnerabilities-haunting-windows.md
title: 'The Logging Dead: Two Event Log Vulnerabilities Haunting Windows'
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 9a0211be0a6ddf4ffcadb5ed5bab0198de4a79d1242cfade91010b90c517085c
text_sha256: d9296bd419809d918e7c6abaeffd66345b7b91ea3e094ad69da041620cd00192
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# The Logging Dead: Two Event Log Vulnerabilities Haunting Windows

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-25_the-logging-dead-two-event-log-vulnerabilities-haunting-windows.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `9a0211be0a6ddf4ffcadb5ed5bab0198de4a79d1242cfade91010b90c517085c`
- Text SHA256: `d9296bd419809d918e7c6abaeffd66345b7b91ea3e094ad69da041620cd00192`


## Content

---
title: "The Logging Dead: Two Event Log Vulnerabilities Haunting Windows"
url: "https://www.varonis.com/blog/the-logging-dead-two-windows-event-log-vulnerabilities"
final_url: "https://www.varonis.com/blog/the-logging-dead-two-windows-event-log-vulnerabilities"
authors: ["Dolev Taler"]
programs: ["Microsoft"]
bugs: ["DoS"]
publication_date: "2022-10-25"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1996
---

You don't have to use Internet Explorer for its legacy to have left you vulnerable to LogCrusher and OverLog, a pair of Windows vulnerabilities discovered by the Varonis Threat Labs team.

Microsoft ended support for Internet Explorer on June 15, 2022.  However, IE’s deep integration into the Windows ecosystem impacts the security and stability of current Windows operating systems.

One feature of the IE and Windows integration is an Internet Explorer-specific Event Log that is present on all current Windows operating systems. This IE-specific Event Log has a distinct set of permissions that enable two exploits against Windows systems:

LogCrusher, which allowed any domain user to remotely crash the Event Log application of any Windows machine on the domain.

OverLog, which causes a remote denial-of-service (DoS) attack by filling the hard drive space of any Windows machine on the domain. ([CVE-2022-37981](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-37981))

In this article, we'll explain how both exploits work and detail their respective attack flows. As part of our research, we promptly disclosed these vulnerabilities to Microsoft, which released a partial [patch](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-37981) on October 11, 2022. We urge everyone to patch their systems.

## Enter MS-EVEN

### Microsoft Event Log Remoting Protocol

These exploits (LogCrusher and OverLog) both use functions of the [Microsoft Event Log Remoting Protocol (MS-EVEN)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-even/55b13664-f739-4e4e-bd8d-04eeda59d09f), which allows for remote manipulation of a machine's event logs.

From Microsoft:

The Event Log Remoting Protocol is an RPC-based protocol that exposes remote procedure call (RPC) methods for reading events in both live event logs and backup event logs on remote computers.

### Internet Explorer log handle

[OpenEventLogW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-openeventlogw) is a Windows API function that allows a user to open a handle for a specific event log on a local or remote machine.

This function is useful for services that can use it to read, write, and clear event logs for remote machines without the need to connect manually to the machines themselves.

The function takes two parameters:

**lpUNCServerName** — The remote machine name, or NULL for a local connection

**lpSourceName** — The specific Event Log to get the handle to

By default, low-privilege, non-administrative users cannot get a handle for event logs of other machines. The one exception to this is the legacy “Internet Explorer” log — which exists in every Windows version and has its own security descriptor that overrides the default permissions.

The Internet Explorer Event Log security descriptor can be found under the registry hive: HKLM\SYSTEM\CurrentControlSet\Services\EventLog\Internet Explorer

![MicrosoftTeams-image \(1\)-3](https://www.varonis.com/hs-fs/hubfs/MicrosoftTeams-image%20\(1\)-3.png?width=772&height=201&name=MicrosoftTeams-image%20\(1\)-3.png)

Parsing the security descriptor string: CustomSD = O:BAG:SYD:(A;;0x07;;;WD)S:(ML;;0x1;;;LW)

![descriptor](https://www.varonis.com/hs-fs/hubfs/descriptor.png?width=894&height=156&name=descriptor.png)

Can you see it? The DiscretionaryACL specifies it!

This ACL allows any user to read and write logs to it. An attacker can get a log handle to every Windows machine in the domain from any domain user.

This sets the stage for our two exploits.

## LogCrusher

### An ElfClearELFW logic bug

ElfClearELFW is an MS-EVEN function that allows administrators to remotely clear and backup event logs.

The function takes two parameters:

**LogHandle** — Log handle that has an already opened OpenEventLog function.

**BackupFileName** — a pointer to a Unicode string struct that holds the location for backing up the event log before it is cleared.

Unfortunately, the ElfClearELFW function has an improper input validation bug. It expects that the BackupFileName structure will be initialized with a zero value, but when the pointer to the structure is NULL, the process crashes.

![Blog_WindowsEventLogVulnerabilities_Diagram_LogCrusherInitialization_V1](https://www.varonis.com/hs-fs/hubfs/Blog_WindowsEventLogVulnerabilities_Diagram_LogCrusherInitialization_V1.png?width=1801&height=3201&name=Blog_WindowsEventLogVulnerabilities_Diagram_LogCrusherInitialization_V1.png)

### Attack flow

Combining these two functions, it's easy to understand the LogCrusher attack flow. Call the OpenEventLog function for the Internet Explorer Event Log on the victim machine:
  
  
  Handle = OpenEventLog(<Victim Machine>, "internet explorer") 

Call the ElfClearELFW function with the handle that was returned, and NULL as the BackupFileName parameter:
  
  
  ElfClearELFW(Handle, NULL)

That's it! Just like that, we crashed the Event Log on the victim's machine.

By default, the Event Log service will try to restart itself two more times. On the third time, it will stay down for 24 hours.

![Blog_WindowsEventLogVulnerabilities_Diagram_LogCrusherAttackFlow_V4](https://www.varonis.com/hs-fs/hubfs/Blog_WindowsEventLogVulnerabilities_Diagram_LogCrusherAttackFlow_V4.png?width=463&height=768&name=Blog_WindowsEventLogVulnerabilities_Diagram_LogCrusherAttackFlow_V4.png)

A demonstration of LogCrusher repeatedly crashing the Event Log service until it stops restarting.

![Desktop_logcrusher](https://www.varonis.com/hs-fs/hubfs/Desktop_logcrusher.gif?width=619&height=544&name=Desktop_logcrusher.gif)

### That's cool. Where's the impact?

The impact lies in the fact that many security controls rely on the normal operation of the Event Log service.

  1. Without logs, security controls are blind.
  2. Security control products, in some cases, attach themselves to the service! This means that when it crashes for good, the product will also crash and burn alongside it.
  3. This in turn could allow an attacker to use any type of usually detected exploit or attack with impunity as many alerts won't trigger.

![DC_Logcrusher](https://www.varonis.com/hs-fs/hubfs/DC_Logcrusher.gif?width=581&height=327&name=DC_Logcrusher.gif)

PowerShell verification of the Event Log stopped status.

### Déjà vu?

Another interesting finding was that the bug in ElfClearELFW function was [discovered](https://limbenjamin.com/articles/crash-windows-event-logging-service.html) two years ago, and reported to Microsoft by a researcher that goes by the nickname “limbenjamin.”

At the time, it was not possible to exploit the bug from a non-admin normal user account (and Internet Explorer), so the impact was unclear and Microsoft opted not to patch it.

## OverLog

With this attack we were able to use the same methodology and Internet Explorer Event Log handle together with another vulnerability in BackupEventLogW function to cause a permanent DoS for every Windows machine.

According to [Microsoft](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-backupeventlogw), the BackupEventLogW function:

Saves the specified event log to a backup file. The function does not clear the event log.

...The BackupEventLog function fails with the ERROR_PRIVILEGE_NOT_HELD error if the user does not have the SE_BACKUP_NAME privilege.

![overlog-1](https://www.varonis.com/hs-fs/hubfs/overlog-1.gif?width=682&height=587&name=overlog-1.gif)

The bug here is even more simple, and although it says in the documentation that the backup user needs to have SE_BACKUP_NAME privilege, the code does not validate it — so every user can backup files to a remote machine if they have write access to a folder on that machine.

### ![DC_Overlog](https://www.varonis.com/hs-fs/hubfs/DC_Overlog.gif?width=1698&height=984&name=DC_Overlog.gif)Attack flow

  1. Get a handle to the Internet Explorer Event Log on the victim machine (same as before).
  2. Write some arbitrary logs to the Event Log (random strings; different lengths).
  3. Backup the log to a writeable folder on the machine (example: “c:\windows\tasks”) that every domain user has write permission to by default.
  4. Repeat the backup process until the hard drive is full and the computer ceases operation.
  5. Victim machine is unable to write “pagefile” (virtual memory), rendering it unusable.

![Blog_WindowsEventLogVulnerabilities_Diagram_OverLogAttackFlow_V2](https://www.varonis.com/hs-fs/hubfs/Blog_WindowsEventLogVulnerabilities_Diagram_OverLogAttackFlow_V2.png?width=463&height=813&name=Blog_WindowsEventLogVulnerabilities_Diagram_OverLogAttackFlow_V2.png)

## Microsoft response and recommendations

Microsoft has opted not to fully fix the LogCrusher vulnerability on Windows 10 (more recent operating systems are unaffected).

As of Microsoft's Oct. 11, 2022 Patch Tuesday update, the default permissions setting that had allowed non-administrative users access to the Internet Explorer Event Log on remote machines has been restricted to local administrators, greatly reducing the potential for harm.

While this address this particular set of Internet Explorer Event Log exploits, there remains potential for other user-accessible application Event Logs to be similarly leveraged for attacks.

We recommend that all potentially vulnerable systems apply the Microsoft-provided patch and monitor any suspicious activity.

## Timeline

The vulnerabilities report timeline that contains the relevant correspondence:

  * 5/24/2022 \- “OverLog” and “LogCrusher” vulnerabilities were submitted to Microsoft Security Response Center (MSRC).
  * **6/2/2022** \- MSRC confirmed “OverLog” and its status was changed to “develop”
  * **7/25/2022** \- MSRC closed “LogCrusher”. They stated that they rated it as moderate severity because it required an administrator privilege and manual interaction to exploit.
  * **7/26/2022** \- We sent an email back to MSRC, specifically mentioning that the initial report says the vulnerability can be exploited from domain user in default Windows configuration. We did not receive a response back from MSRC.
  * **10/11/2022** \- Patch Tuesday — the OverLog vulnerability was assigned [CVE-2022-37981](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-37981) and patched.
  * **10/25/2022** \- Blog post published.

### What should I do now?

Below are three ways you can continue your journey to reduce data risk at your company:

1

[Schedule a demo with us](https://info.varonis.com/en/demo-request?hsLang=en "https://info.varonis.com/en/demo-request") to see Varonis in action. We'll personalize the session to your org's data security needs and answer any questions.

2

[See a sample of our Data Risk Assessment](https://www.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") and learn the risks that could be lingering in your environment. [Varonis' DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=en "https://info.varonis.com/en/data-risk-assessment") is completely free and offers a clear path to automated remediation.

3

Follow us on[ LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg"), and [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis") for bite-sized insights on all things data security, including DSPM, threat detection, AI security, and more.

![Dolev Taler](https://www.varonis.com/hubfs/dolev-taler.jpg)

Dolev Taler Dolev is a Security Researcher within Varonis Threat Labs. He likes bounty hunting, Windows Internals, and finding complicated solutions to simple problems.
