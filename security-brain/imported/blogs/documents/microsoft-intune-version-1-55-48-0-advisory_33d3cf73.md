---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-04_microsoft-intune-version-155480-advisory.md
original_filename: 2023-04-04_microsoft-intune-version-155480-advisory.md
title: Microsoft Intune, Version 1.55.48.0 Advisory
category: documents
detected_topics:
- access-control
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 33d3cf73b84376213243890c6a4a701249c2b75a86c90cfdb781b0b74e5007a9
text_sha256: 071aeedd5405bff2b67dc2d4279a45d056a9cb6772ae107df91dbfc610f19fa9
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Intune, Version 1.55.48.0 Advisory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-04_microsoft-intune-version-155480-advisory.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `33d3cf73b84376213243890c6a4a701249c2b75a86c90cfdb781b0b74e5007a9`
- Text SHA256: `071aeedd5405bff2b67dc2d4279a45d056a9cb6772ae107df91dbfc610f19fa9`


## Content

---
title: "Microsoft Intune, Version 1.55.48.0 Advisory"
page_title: "Microsoft Intune, Version 1.55.48.0 Advisory | Bishop Fox"
url: "https://bishopfox.com/blog/microsoft-intune-version-1-55-48-0-advisory"
final_url: "https://bishopfox.com/blog/microsoft-intune-version-1-55-48-0-advisory"
authors: ["Ben Lincoln (@0x00C651E0)"]
programs: ["Microsoft (Intune)"]
bugs: ["Unquoted search path", "Local Privilege Escalation"]
publication_date: "2023-04-04"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1299
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/microsoft-intune-version-1-55-48-0-advisory&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/microsoft-intune-version-1-55-48-0-advisory&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/microsoft-intune-version-1-55-48-0-advisory&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

## Summary

The following document describes identified vulnerabilities in the Microsoft Intune application, version 1.55.48.0.

### Product Vendor

Microsoft

### Product Description

Microsoft Intune is an endpoint-management suite. The project’s official website is [https://partner.microsoft.com/...](https://partner.microsoft.com/en-us/solutions/microsoft-intune).

### Vulnerabilities List

One vulnerability was identified within the Windows Task Scheduler application:

  * Unquoted search path

The vulnerability is described in the following sections.

### Affected Version

Version 1.55.48.0

### Summary of Findings

At least one function in Microsoft Intune calls an external executable on a recurring basis without quoting the full path to the executable.

### Impact

If a local user has write access to the root of the `C:\ drive or the C:\Program Files (x86)` directory, they may be able to execute programs as another user, resulting in horizontal or vertical privilege escalation.

### Solution

There is no update available to address this vulnerability. Security defenders can monitor for the presence of files with paths such as `C:\Program.exe and C:\Program Files (x86)\Microsoft.exe` as indicators of potential compromise.

## Vulnerabilities

### Unquoted Search Path

The Microsoft Intune Management Extension does not quote one or more calls to the following utility program: 

`C:\Program Files (x86)\Microsoft Intune Management Extension\agentexecutor.exe`

An attacker with write access to the root of the `C:\ drive or the C:\Program Files (x86)` directory could execute code in the context of another user by creating a malicious executable named `C:\Program.exe or C:\Program Files (x86)\Microsoft.exe`, and then wait for Intune to call the agentexecutor.exe utility program. In the default Windows configuration, only local administrators have write access to the affected locations, but a malicious administrator could exploit the issue to move laterally into the accounts of other users who logged on to the same system. Additionally, a malicious user could exploit the issue to prevent execution of PowerShell scripts assigned by the Intune administrator for their organization.

### Vulnerability Details

Vulnerability Type: Unquoted search path

Access Vector: ☐ Remote, ☒ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☒☐ Escalation of privileges, ☐ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☐ Critical, ☐ High, ☐ Medium, ☒☐ Low

Vulnerability: CWE- 428

The presence of the vulnerability was confirmed by copying `C:\Windows\SysWOW64\cmd.exe to C:\Program.exe`, then waiting for Intune to execute PowerShell scripts. For example, the following list was present in Task Manager after leaving a laptop locked but powered on overnight:

![Task Manager entries for the Program.exe process](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Intune-Image-1.png)

**FIGURE 1** \- Task Manager entries for the `Program.exe` process

A custom 32-bit x86 executable that logged environmental data was created, and a copy was named `C:\Program.exe`. When executed via the unquoted search path, the following details were logged:
  
  
  Date/time: 2022-07-06.14:00:20
  Process ID: 23620
  Parent Process ID: 23620
  Parent Process Executable: Microsoft.Management.Services.IntuneWindowsAgent.exe
  
  Arguments:
  C:\Program
  Files
  (x86)\Microsoft
  Intune
  Management
  Extension\agentexecutor.exe
  -proxy
  TXXX-PF2X5Q1N\blincoln
  https://fef.msua06.manage.microsoft.com/TrafficGateway/TrafficRoutingService/SideCar/StatelessSideCarGatewayService
  
  Environment variables:
  …omitted for brevity…
  LOCALAPPDATA=C:\Windows\system32\config\systemprofile\AppData\Local
  …omitted for brevity…
  USERNAME=TXXX-PF2X5Q1N$
  USERPROFILE=C:\Windows\system32\config\systemprofile

**FIGURE 2** \- Relevant details logged by custom executable

These details indicated that the process that launched the unquoted command was the Intune Windows Agent, and that it executed in the context of the computer account. However, Task Manager showed the owning user was instead the currently logged-on user, indicating that Intune potentially used the elevated permissions of the computer account to change the context of the process after launching it. An attacker could therefore potentially exploit this vulnerability to not only execute commands as the computer account, but also as any user who logged on to the device.

The following Intune .NET DLL was decompiled to disclose at least two potential locations for this issue: `Microsoft.Management.Services.IntuneWindowsAgent.AgentCommon.dll`

The first instance of an unquoted search path was found in the source code file `Microsoft.Management.Services.IntuneWindowsAgent.AgentCommon\Services\IntuneWindowsAgent\AgentCommon\ProxyHelper.cs`, as shown below:
  
  
  string str1 = string.Format((IFormatProvider) CultureInfo.InvariantCulture, "{0}\\{1}", (object) Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), (object) "agentexecutor.exe");
  …omitted for brevity…
  string str4 = string.Format((IFormatProvider) CultureInfo.InvariantCulture, "{0} {1} {2} {3}", (object) str1, (object) " -proxy ", (object) str2, (object) str3);
  Log.TraceInformation(str4);
  Log.TraceInformation("[Proxy Poller] Launch agent executor in user session");
  if (!NativeMethods.CreateProcessAsUser(tokenHandle, (string) null, str4, ref structure, ref structure, true, dwCreationFlags, IntPtr.Zero, (string) null, ref lpStartupInfo, out lpProcessInformation))

**FIGURE 3** \- Vulnerable code in `ProxyHelper.cs`

  

The decompiled code called the string.Format function to concatenate the path to the directory containing the `DLL (C:\Program Files (x86)\Microsoft Intune Management Extension` by default) with the string `agentexecutor.exe`. That path was then concatenated into a larger string that represented the full command line to call the `agentexecutor.exe` utility and pass it certain options. However, the path to `agentexecutor.exe` was not enclosed in quotation marks.

In contrast, the decompiled source code file `Microsoft.Management.Services.IntuneWindowsAgent.AgentCommon\Services\IntuneWindowsAgent\AgentCommon\ScriptWorker.cs` contained code that correctly quoted search paths, as shown below:
  
  
  string str6 = string.Format((IFormatProvider) CultureInfo.InvariantCulture, "{0}\\{1}", (object) Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), (object) "agentexecutor.exe");
  …omitted for brevity…
  string str7 = string.Format((IFormatProvider) CultureInfo.InvariantCulture, "\"{0}\" {1} \"{2}\" \"{3}\" \"{4}\" \"{5}\" {6} \"{7}\" {8} \"{9}\" {10} \"{11}\"", (object) str6, (object) " -remediationScript ", (object) str1, (object) str2, (object) str3, (object) str4, (object) timeOutSeconds, (object) pathFromRegistry, enforceSignatureCheck ? (object) "1" : (object) "0", (object) str5, (object) (runningMode != 1), (object) scriptParamRunString);
  …omitted for brevity…
  if (userContext)
  {
  …omitted for brevity…
  Log.TraceInformation("Launch powershell executor in user session");
  flag2 = NativeMethods.CreateProcessAsUser(userToken, (string) null, str7, ref structure, ref structure, true, dwCreationFlags, lpEnvironment, (string) null, ref lpStartupInfo, out lpProcessInformation);
  }
  else
  {
  Log.TraceInformation("Launch powershell executor in machine session");
  flag2 = NativeMethods.CreateProcess((string) null, str7, IntPtr.Zero, IntPtr.Zero, true, (uint) dwCreationFlags, IntPtr.Zero, (string) null, ref lpStartupInfo, out lpProcessInformation);

**FIGURE 4** \- Correctly quoted process path in `ScriptWorker.cs`

The code shown above was similar to the vulnerable code in `ProxyHelper.cs`, but the second call to `string.Format` wrapped the executable path in quotation marks, removing the potential for an unquoted search path vulnerability. An exhaustive audit of the Intune Management Extension was not conducted, and the same issue may be present elsewhere in the product.  

## Credits

  * Ben Lincoln, Managing Senior Security Consultant II, Bishop Fox ([[email protected]](https://bishopfox.com/authors/ben-lincoln))  

## Timeline

  * 07/06/2022: Initial discovery
  * 08/03/2022: Contact with vendor, ID VULN-071398 assigned
  * 08/10/2022: Vendor assigned case number 73717
  * 09/06/2022: Vendor acknowledged vulnerabilities
  * 10/21/2022: Bishop Fox requests status update from Vendor via the MSRC Researcher Portal
  * 10/24/2022: Bishop Fox requests status update from Vendor via email
  * 10/26/2022: Vendor indicates that the vulnerability does not meet their criteria for servicing and will not be addressed
  * 04/04/2023: Vulnerabilities publicly disclosed

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
