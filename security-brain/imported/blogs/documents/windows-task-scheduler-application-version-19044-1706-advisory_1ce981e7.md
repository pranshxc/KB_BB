---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-04_windows-task-scheduler-application-version-190441706-advisory.md
original_filename: 2023-04-04_windows-task-scheduler-application-version-190441706-advisory.md
title: Windows Task Scheduler Application, Version 19044.1706 Advisory
category: documents
detected_topics:
- sso
- access-control
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- sso
- access-control
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 1ce981e7bbd0586b8185b9e2eb4f9b4a611bd83eb51767accec69a45ac2a3419
text_sha256: 678a36ebaef40f6ff8717eaa81911844efe33ad45988adddac3bf00a138ef4a3
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Windows Task Scheduler Application, Version 19044.1706 Advisory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-04_windows-task-scheduler-application-version-190441706-advisory.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `1ce981e7bbd0586b8185b9e2eb4f9b4a611bd83eb51767accec69a45ac2a3419`
- Text SHA256: `678a36ebaef40f6ff8717eaa81911844efe33ad45988adddac3bf00a138ef4a3`


## Content

---
title: "Windows Task Scheduler Application, Version 19044.1706 Advisory"
page_title: "Windows Task Scheduler Application, Version 19044.1706… | Bishop Fox"
url: "https://bishopfox.com/blog/windows-task-scheduler-19044-advisory"
final_url: "https://bishopfox.com/blog/windows-task-scheduler-19044-advisory"
authors: ["Ben Lincoln (@0x00C651E0)"]
programs: ["Microsoft (Windows)"]
bugs: ["Unquoted search path", "Local Privilege Escalation"]
publication_date: "2023-04-04"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1300
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/windows-task-scheduler-19044-advisory&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/windows-task-scheduler-19044-advisory&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/windows-task-scheduler-19044-advisory&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

## Summary

The following document describes identified vulnerabilities in the Windows Task Scheduler application version 19044.1706.

### Product Vendor

Microsoft Corporation

### Product Description

Windows Task Scheduler is the built-in Windows component that manages scheduled tasks. The project’s official website is <https://www.microsoft.com/en-us/windows>.

### Vulnerabilities List

One vulnerability was identified within the Windows Task Scheduler application:

  * Unquoted search path

The vulnerability is described in the following sections.

### Affected Version

Version 19044.1706

### Summary of Findings

The Microsoft Windows Task Scheduler component does not properly quote executable paths when calling external programs whose paths contain an environment variable, if the environment variable’s value contains spaces and the remainder of the program’s path does not. This can result in an unquoted search path vulnerability even if the path appears to be quoted correctly in the scheduled task configuration.

### Impact

A local user may be able to execute programs in the context of another user, or the `SYSTEM` account, resulting in horizontal or vertical privilege escalation. At the time this vulnerability was reported to Microsoft, Windows Update included a vulnerable scheduled task named `PLUGScheduler`, but the issue may occur with scheduled tasks registered by third parties as well.

### Solution

Automatic Windows update available after January 10, 2023. 

  

## Vulnerabilities

### Unquoted Search Path

The Microsoft Windows Task Scheduler component does not properly quote executable paths when calling external programs whose paths contain an environment variable, if the environment variable’s value contains spaces and the remainder of the program’s path does not. At least one built-in component of Windows 10 (PLUGScheduler) includes a scheduled task that meets both of these requirements and is vulnerable. An attacker with write access to the root of the `C:\` drive can cause code to be executed in the context of another user by creating a malicious executable named `C:\Program.exe` and then waiting for Windows to attempt to launch the component.

In the default Windows configuration, only local administrators have write access to the root of the `C:\` drive, so this vulnerability would typically be rated low-severity. However, as the issue potentially applies to any scheduled task, the severity is increased to medium.

### Vulnerability Details

CVE ID: CVE-2023-21541

Vulnerability Type: Unquoted search path

Access Vector: ☐ Remote, ☒ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☒ Escalation of privileges, ☐ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☐ Critical, ☐ High, ☒ Medium, ☐ Low

Vulnerability: CWE-428

The Microsoft Windows Task Scheduler component does not properly quote executable paths when calling external programs whose paths contain an environment variable, if the environment variable’s value contains spaces and the remainder of the program’s path does not. At least one built-in component of Windows 10 (PLUGScheduler) includes a scheduled task that meets both of these requirements and is vulnerable. An attacker with write access to the root of the `C:\` drive can cause code to be executed in the context of another user by creating a malicious executable named `C:\Program.exe` and then waiting for Windows to attempt to launch the component.

In the default Windows configuration, only local administrators have write access to the root of the `C:\` drive, so this vulnerability would typically be rated low-severity. However, as the issue potentially applies to any scheduled task, the severity is increased to medium.

The PLUGScheduler Windows component’s default configuration includes a scheduled task that calls `%ProgramFiles%\RUXIM\PLUGScheduler.exe`, as shown below: 

![Scheduled task definition for PLUGScheduler](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Unquoted-Search-Path-Image-1.png)

**FIGURE 1** \- Scheduled task definition for PLUGScheduler

The scheduled task definition explicitly quoted the path to the executable, which would typically prevent an unquoted search path vulnerability. However, during testing of a custom utility for detecting unquoted search paths, Bishop Fox observed a call made to the utility, indicating an unquoted search path. This utility was a 32-bit x86 executable that logged environmental data, stored as `C:\Program.exe`. On a Bishop Fox laptop left powered on but locked overnight, the following log entry was created:
  
  
  Date/time: 2022-07-07.08:19:20
  Process ID: 20996
  Parent Process ID: 20996
  Parent Process Executable: svchost.exe
  Arguments:
  C:\Program
  Files\RUXIM\PLUGscheduler.exe
  Environment variables:
  …omitted for brevity…
  APPDATA=C:\Windows\system32\config\systemprofile\AppData\Roaming
  …omitted for brevity…
  LOCALAPPDATA=C:\Windows\system32\config\systemprofile\AppData\Local
  …omitted for brevity…
  USERNAME=TXXX-PF2X5Q1N$
  USERPROFILE=C:\Windows\system32\config\systemprofile

**FIGURE 2** \- Relevant details logged by custom executable

The date and time matched the Last Run Time value in the associated scheduled task. To determine why the task had an unquoted search path vulnerability despite being quoted, several test tasks were created.

In the following scheduled task, the path to the executable is quoted:

![Scheduled task definition with quoted executable path](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Unquoted-Search-Path-Image-2.png)

**FIGURE 3** \- Scheduled task definition with quoted executable path

When this example scheduled task was executed, the correct, quoted path was used, as shown below:
  
  
  Date/time: 2022-07-14.08:43:45
  Process ID: 3700
  Parent Process ID: 3700
  Parent Process Executable: svchost.exe
  Arguments:
  C:\Program Files\Test\LogEnvironmentInfo.exe

**FIGURE 4** \- Relevant details logged by scheduled task with quoted path

However, the Task Scheduler behavior changed when a scheduled task was configured to reference the `%ProgramFiles%` environment variable and the remaining path did not contain spaces (matching the configuration of the initial PLUGScheduler task). As shown below, Bishop Fox staff created another task where the explicit path did not contain any spaces but referenced the `%ProgramFiles%` environment variable:

![Task definition referencing environment variable and path without spaces](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Unquoted-Search-Path-Image-3.png)

**FIGURE 5** \- Task definition referencing environment variable and path without spaces

In this configuration, the quotes around the path were ignored, as shown below:
  
  
  Date/time: 2022-07-14.08:51:40
  Process ID: 9060
  Parent Process ID: 9060
  Parent Process Executable: svchost.exe
  Arguments:
  C:\Program
  Files\Test\LogEnvironmentInfo.exe

**FIGURE 6** \- Relevant details logged by scheduled task with quoted path

![Task definition referencing environment variable and path with spaces](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Unquoted-Search-Path-Image-4.png)

**FIGURE 7** \- Task definition referencing environment variable and path with spaces

When the `%ProgramFiles%` environment variable was used in the path and the remaining path included spaces, the unquoted search path vulnerability was not present, as shown below:
  
  
  Date/time: 2022-07-14.09:13:37
  Process ID: 2420
  Parent Process ID: 2420
  Parent Process Executable: svchost.exe
  Arguments:
  C:\Program Files\Test With Spaces\LogEnvironmentInfo.exe

**FIGURE 8** \- Relevant details logged by scheduled task with quoted path containing spaces

Bishop Fox believes that the Task Scheduler attempts to determine if a path requires quotes by checking for spaces inside the path but does not expand environment variables before performing the check. However, this specific root cause was not verified.

Because this issue appears to affect most Windows scheduled tasks referencing a path containing an environment variable, Bishop Fox increased the severity of this finding from low to medium.

## Credits

  * Ben Lincoln, Managing Senior Security Consultant II, Bishop Fox ([[email protected]](https://bishopfox.com/authors/ben-lincoln))  

### Timeline

  * 07/07/2022: Initial discovery
  * 07/27/2022: Contact with vendor, ID VULN-071097 assigned
  * 07/28/2002: Vendor assigned case number 73445
  * 08/05/2022: Vendor acknowledged vulnerabilities
  * 08/12/2022: Vendor awards bounty
  * 10/07/2022: Vendor requests delay of disclosure to 01/10/2023
  * 1/10/2023: Vendor released patched version
  * 01/10/2023: Vulnerabilities publicly disclosed

* * *

![Ben Lincoln Headshot Managing Senior Security Consultant Bishop Fox](https://assets.bishopfox.com/prod-1437/Images/author-photos/Ben-Lincoln-Headshot-Managing-Senior-Security-Consultant-Bishop-Fox.jpg)

By Ben Lincoln 

Managing Principal

Ben Lincoln is a Managing Principal at Bishop Fox and focuses on application security. He has extensive experience in network penetration testing, red team activities, white-/black-box web/native application penetration testing, and exploit development. Prior to joining Bishop Fox, Ben was a security consultant with NCC Group, a global information assurance consulting organization. He also previously worked at a major retail corporation as a senior security engineer and a senior systems engineer. Ben delivered presentations at major security conferences, including "[A Black Path Toward the Sun](https://www.blackhat.com/us-16/arsenal.html#a-black-path-toward-the-sun)" at Black Hat USA 2016. Ben is [OSCP](https://www.offensive-security.com/pwk-oscp/)-certified and has released several open-source exploit tools.

[ More by Ben Lincoln  ](https://bishopfox.com/authors/ben-lincoln)

[ ](https://twitter.com/0x00c651e0) [ ](https://www.linkedin.com/in/ben-lincoln-57b92b153/)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
