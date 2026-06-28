---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-12_microsoft-windows-msi-installer-repair-to-system-a-detailed-journey.md
original_filename: 2024-09-12_microsoft-windows-msi-installer-repair-to-system-a-detailed-journey.md
title: Microsoft Windows MSI Installer - Repair to SYSTEM - A detailed journey
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: 6377b32c6f63e69b421cfeb4b5b5aa657a66948c346fd76a9edb03ac2513d8cb
text_sha256: 8b931fb016fe2d82ad426add83d17ba610f86892d0b5866488b52c52e568ffdd
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Windows MSI Installer - Repair to SYSTEM - A detailed journey

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-12_microsoft-windows-msi-installer-repair-to-system-a-detailed-journey.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `6377b32c6f63e69b421cfeb4b5b5aa657a66948c346fd76a9edb03ac2513d8cb`
- Text SHA256: `8b931fb016fe2d82ad426add83d17ba610f86892d0b5866488b52c52e568ffdd`


## Content

---
title: "Microsoft Windows MSI Installer - Repair to SYSTEM - A detailed journey"
page_title: "Microsoft Windows MSI Installer - Repair to SYSTEM - A detailed journey - SEC Consult"
url: "https://sec-consult.com/blog/detail/msi-installer-repair-to-system-a-detailed-journey/"
final_url: "https://sec-consult.com/blog/detail/msi-installer-repair-to-system-a-detailed-journey/"
authors: ["Michael Baer"]
programs: ["Microsoft (Windows)"]
bugs: ["Local Privilege Escalation"]
publication_date: "2024-09-12"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 8
---

1. [ Home ](/)
  2. [ Blog ](/blog/)
  3. Microsoft Windows MSI Installer - Repair to SYSTEM - A detailed journey

# Microsoft Windows MSI Installer - Repair to SYSTEM - A detailed journey

12.09.2024  research 

Repair functions of Microsoft Windows MSI installers can be vulnerable in several ways, for instance allowing local attackers to escalate their privileges to SYSTEM rights. This vulnerability is referenced as CVE-2024-38014.

![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/image__3_.png)

_This article by our researcher Michael Baer for the SEC Consult Vulnerability Lab will explain different attacks against MSI installers and present an open-source analyzer tool named "msiscan" in order to automatically detect potential security issues. The main focus lies on an attack that abuses briefly opened command Windows during program execution of the MSI installer in the GUI. While most available public research on this topic tries to slow down the system in order to have enough time for the attack, we will describe a technique to completely pause the program execution. This simplifies the attack and makes it a lot more reliable._

[![Openbrowser](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_openbrowser_01.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_openbrowser_01.png) Figure 1: Legacy console mode, open with browser 

[MSI installers](https://en.wikipedia.org/wiki/Windows_Installer) are a common way to install applications on Windows systems. The MSI file format allows to create standardized installers that can install, remove and repair software. While the installation and removal of software usually requires elevated permissions, the repair function for already installed software can be performed by a low-privileged user. The issued repair functions can, however, be executed under the context of NT AUTHORITY\SYSTEM, a very high access right in Windows. If an attacker is able to maliciously interfere with those functions, a privilege escalation attack is possible.

This blog post mainly focuses on the vulnerability of visible elevated windows during program execution. However, various other vulnerabilities can arise by an insecurely developed installer. Our provided open-source tool "msiscan" tries to give some more insights into an installer that can help identifying further vulnerabilities:

**Open-source tool "msiscan":** <https://github.com/sec-consult/msiscan>

SEC Consult encountered various MSI installers in the past that allowed privilege escalation because of the unsafe usage of repair functions. The following advisories with technical exploit information have been published:

  * [Local Privilege Escalation via MSI installer in PDF24 Creator - CVE-2023-49147](https://r.sec-consult.com/pdf24) (found by Lukas Donaubauer & Mario Keck; Lukas Donaubauer who developed the new approach set the basis for this research, blog post and tool release!)
  * [Local Privilege Escalation via MSI installer in SoftMaker Office 2024 / NX, FreeOffice - CVE-2023-7270](https://r.sec-consult.com/softmaker) (found by Michael Baer)
  * [Local Privilege Escalation via MSI Installer in Nitro PDF Pro CVE-2024-35288](https://sec-consult.com/vulnerability-lab/advisory/local-privilege-escalation-via-msi-installer-in-nitro-pdf-pro/) (added 20240930; found by Sandro Einfeldt & Michael Baer)
  * [Perimeter 81](https://www.perimeter81.com/) software, a Check Point company - we identified that version 9 is vulnerable, but version 10 is unaffected. As there is a patch available, we didn't notify the vendor specifically on this issue.
  * Another security product vendor was notified about the MSI installer issue in one of their products back in November 2023. They recognized the issue, but are still unable to provide a timeline for a fix as of June 2024. Edit 2024-10-09: The advisory has been released now, a patch has been provided by the vendor: [Local Privilege Escalation via MSI installer in Palo Alto Networks GlobalProtect (CVE-2024-9473)](https://sec-consult.com/vulnerability-lab/advisory/local-privilege-escalation-via-msi-installer-in-palo-alto-networks-globalprotect/) (found by Michael Baer)
  * A customer modified Keepass to install a certificate with the windows executable certutil.exe. This modification was vulnerable as well.

We have contacted Microsoft via their Researcher Portal about this issue through our CVD process ([coordinated vulnerability disclosure](https://sec-consult.com/vulnerability-lab/responsible-disclosure-policy/)) regarding this vulnerability and the release of this blog post and the tool. **Microsoft** decided to implement a remediation for the **September 2024 patch day.** Microsoft also issued a bounty to us via the Intigriti platform, which we are going to donate to a good cause in the security community.

**Microsoft vendor advisory** ([CVE-2024-38014](https://www.cve.org/CVERecord?id=CVE-2024-38014)): [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38014 ](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38014)(CVSS Score 7.8 - HIGH - CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:F/RL:O/RC:C)

Several other articles and CVEs have been published about this topic by other researchers in the past. The goal of this blog post is to build upon those and add further details about detecting and exploiting and releasing our "msiscan" tool.

  * [A similar vulnerability](https://www.mandiant.com/resources/blog/privileges-third-party-windows-installers)
  * [Another use of OpLocks](https://www.mandiant.com/resources/blog/arbitrary-file-deletion-vulnerabilities)
  * [Other attacks on MSI installers](https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks)

## The MSI repair exploit - repeat the known exploit and improve it

The exploit requires GUI access and a supported browser (e.g. Firefox or Chrome). This attack does not work using a recent version of the Edge browser or Internet Explorer. Also make sure, that Edge or IE have not been set as default browser for the system user and that Firefox or Chrome are not running before attempting to exploit it. Otherwise, the spawned process would be running with your own permissions and the installer will just add a new tab to the browser, instead of spawning a new process with SYSTEM privileges.

We will also make use of another tool called "[SetOpLock.exe](https://github.com/googleprojectzero/symboliclink-testing-tools/tree/main/SetOpLock)".

On a high level, we repair an already installed application (which can be done by low-privileged users). The installer runs as SYSTEM. Some installers will spawn a console window with those elevated privileges. We can navigate the GUI of this window to spawn an interactive console window with elevated privileges then.

We will first explain the main process and then our improvement using SetOpLock.

  1. Close your browser.
  2. Start the repair process as low-privileged user. This can be done by either normal windows GUI functionality or by executing `msiexec.exe /fa <path/to/installer.msi>`
  3. When a black console window pops up, quickly right click on the window bar and select `properties`, or select an area inside the window. This will stop the window from closing.
  4. Click on "legacy console mode", a dialog to select a browser should open, see the following figure 1:

[![CMD](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_cmd_02.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_cmd_02.png) Figure 2: New command window with SYSTEM privileges opens 

5\. Select your browser, preferably Firefox.  
6\. Press Ctrl+O in Firefox, then a file dialog should open.  
7\. Type `cmd.exe` in the top bar and press ENTER, a new command window should open. See the following figure 2:

[![Not found](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_notfound_03.PNG)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_notfound_03.PNG) Figure 3: File not found, place installer in your chosen directory 

8\. You have a command window with elevated SYSTEM privileges.

**Detailed notes about the steps:**

  1. If a browser is already open, the link will be opened in your current browser window with your current privileges and privilege escalation won't work in this case.
  2. Starting the repair process 
  1. The installer can be found in `C:\Windows\Installer`. This folder is hidden, the path must be explicitly specified in the file explorer. The name will be a random name varying between every system.
  2. We observed a slight difference between double-clicking the file and the `msiexec.exe` command from above. As of our knowledge, this is caused by the following:  
During the repair process, several actions of the installation will be repeated to fix the system. There is a level, how much will be repaired, `/fa` is the strongest mode, while a normal GUI repair does not repeat every step. Therefore, we suggest to use `/fa` to be on the safe side, but normally both will work.
  3. If you encounter the following message (figure 3), simply place the installer with the mentioned name in a directory of your choice.

[![SetOpLock.exe](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_22-28-23_04.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_22-28-23_04.png) Figure 4: SetOpLock.exe loop 

3\. If this black window closes too fast, we have a trick for you:

a) SetOpLock.exe is a small tool that locks a file. Other programs accessing the file have to wait for SetOpLock to release the lock.

b) Identify a file that is accessed by the installation while the window is visible and lock this file. In practice, we run it once with ProcMon (on a different machine, where we are administrator) and try all accessed files (not every file will be working).

c) The window will now be kept open forever.

d) We use a loop in case the file is accessed several times before the window is opened (see figure 4): `while ($true) { .\SetOpLock.exe "C:\Program Files\<xxx>.exe" x }`

[![msiexec.exe](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_22-47-15_05.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_22-47-15_05.png) Figure 5: ProcMon excerpt 

4\. No browser should be open before clicking the link.  
5\. Untick "Always open with this app". Otherwise you will configure the SYSTEM user's configuration and cannot go back.

Now, we will dive deeper into this vulnerability.

## Identifying the vulnerability

We will show two ways of identifying this vulnerability: Manual and Automatic. Depending on the context, one is preferable over the other.

### Identify Manually

This step assumes that you already have administrator privileges on the system.

1\. Check whether the application is vulnerable

a. Start ProcMon64.exe from the [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite).  
b. Start the repair process. It is advised to use the command line version `msiexec.exe /fa <path/to/installer.msi>`  
c. Go to ProcMon and open the Thread-View (Ctrl+T).  
d. Here, we can look for the following pattern: `msiexec.exe` → <some binary> → `conhost.exe` . The binary should be executed as SYSTEM, see figure 5.  
e. We have now identified a target binary that is likely to be vulnerable.

[![MSI example](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_example_annot_06.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_example_annot_06.png) Figure 6: msiscan example output 

2\. Find a suitable file to pause the execution.  
a. Filter the ProcMon events to only include the identified binary `SCHTASKS.exe` and only show file operations.  
b. Try each accessed file whether it blocks the process (run the exploit and see whether the window stays open.

  * Files that are written are a good target (e.g. logfiles)
  * Sometimes the loaded DLLs do work
  * Sometimes even the binary itself does work

**Pros** of the manual approach

  * Step 1 is quickly performed, only ProcMon as external tool is required
  * Very few false-negatives
  * Good for client assessments or checking a single application

**Cons** of the manual approach

  * Tedious work, especially for more than one application
  * Only useful to identify exactly this vulnerability

### Identify Automatically

We have implemented a python tool called "[msiscan](https://github.com/sec-consult/msiscan)" to analyze MSI files offline. Administrator privileges on the system are not needed to identify potential vulnerabilities, however they can be helpful to identify a suitable file for the locking part.

  1. Check whether the application is vulnerable  
a. Copy the MSI installer to the analysis machine  
b. Run `python msiscan.py`  
c. Analyse the results. Look out especially for red entries.
  2. Do step 2 from the manual approach. There is no support for this yet.

**Pros** of the automatic approach

  * Scales well to quickly identify potential targets for thousands of applications
  * Can indicate other interesting behavior
  * Identification is offline → No noise on the system

**Cons** of the automatic approach

  * Need to copy installers to analysis machine
  * More false-negatives

Repeatedly observed working binaries:

  * If certutil.exe is invoked → lock the certificate file
  * If powershell.exe is invoked → lock the powershell.exe executable

## How does this vulnerability occur?

Executables in Windows normally come in two forms: GUI applications and console applications. The Linux tool `file` can be used to easily determine the type of the executable:

`PE32 executable (**GUI**) Intel 80386` versus `PE32 executable (**console**) Intel 80386.`

If a console application is executed, a console window is automatically created. This is the black window `conhost.exe` we use to interact with.

The vulnerability therefore is:  _Executing a console application in an elevated repair context without taking precautions to hide the window._

We show some precautions at the end of the article.

## When is an installer vulnerable?

### Quick Introduction to MSI installer files

An MSI installer is basically only a database bundled with the files of the application. The database contains several tables to configure the installation. E.g., one table with properties (`Properties`) and one with all the steps performed during an installation (`InstallExecuteSequence`). The tables can be displayed with the Microsoft tool [Orca](https://learn.microsoft.com/en-us/windows/win32/msi/orca-exe). The InstallExecuteSequence table contains different actions, most of which are standard actions provided by the MSI service. But this table can also reference `CustomActions`. Those are actions that execute custom scripts, binaries or DLLs if non-standard features are needed for the application. A custom action can be configured to be executed with elevated privileges. This is where it gets interesting for an attacker, because the function is self-implemented by the vendor and the implementation must be safe against privilege escalations.

### A vulnerable installer

Two base conditions need to be fulfilled:

  * The custom action is executed during a repair (actions can be conditionally executed).
  * The action is configured to run in an elevated context.

Apart from this, the actions themselves need to perform unsafe operations. One of the following must be true:

  * A custom action invokes directly or indirectly a PE console application. This allows the exploit path from above, as a "conhost" window is opened. The invocation often happens in various ways: 
  * Invoking a binary provided by the installer that is itself a console application
  * Invoking a binary provided by the installer that calls a console application
  * Invoking system applications that are console applications, e.g. executing `certutil.exe <...>` or `cmd /c del xyz`
  * Invoking a DLL function that calls a console application
  * A custom action executes scripts or executables that are unsafe.

Additionally, the software can be vulnerable, but exploiting is not possible. The following conditions need to be fulfilled on the system for an exploit to be feasible:

  * A browser is installed on the system, that can be run as SYSTEM User 
  * Newer versions of Edge do not work (Windows 11 and current versions of Windows 10 always start Edge as a normal user)
  * Internet Explorer is often configured to launch Edge and therefore is not exploitable
  * As the browser is invoked from a SYSTEM context, all settings are taken from the SYSTEM user → it is not possible to reconfigure the settings or use portable browsers
  * Firefox and Chromium are known to work to the date of our analysis
  * The process can be slowed down: Normally the windows just pops up for a very short time, often not even visible. The SetOpLock trick can pause the execution of the command. However, we need a file that will be read by the process and blocks the closing of the window. We encountered applications where we did not find a way to block the window.

## Tooling support

We created a python script to analyze MSI files. [It can be downloaded from here.](https://github.com/sec-consult/msiscan)

  * It is a python script using `msitools` (Linux) to quickly identify vulnerable or potentially vulnerable installers
  * Analysis is fully offline, and does not execute the installer (but has false-negatives, e.g. missing vulnerable installers)
  * Analyses MSI files outside of the target environment 
  * Checks all custom actions for elevated actions
  * Checks binaries and calls to detect those that spawn a terminal (static analysis)
  * Shows JS/VB scripts that are executed as they often contain process invocations
  * Shows the InstallerCondition when this action is run
  * Detects potential CVE-2024-29188 (WiX Toolset) vulnerabilities

The tool unpacks the installer, queries all CustomActions and analyses the executed scripts or binaries. For each custom action that is invoked as a privileged user, it prints some basic information. The following screenshot in figure 6 shows one for a very likely exploitation (red).

You can read the output as follows:

  * _EXE (commandline)_ : There is a CustomAction that invokes an executable using a command line
  *  _name='CopyLog':_ Name of the CustomAction
  *  _Rating.VERYLIKELY:_ The heuristic assumes that this action is very likely to be vulnerable (executing a console application). Commands from Installer Frameworks are unlikely, custom written code is a medium likelihood.
  * _InvestigateDifficulty.EASY_ : It is very easy to further investigate this (follow the steps described above in this blog post). Scripts are considered medium as they can be easily read, but still some source code reading is needed. Compiled binaries are hard to analyse.
  * Then some information about this particular CustomAction is shown and the exploit follows.
  * _Command ..._ : This is the command that will be invoked.
  * A green line following this snippet indicates the condition used to decide whether the action is executed. Normally it references variables that indicate whether the software is currently installed or removed.

[![uacfail](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/uacfail.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/uacfail.png) Figure 7: UAC popup denying the attack 

The colors give a quick overview whether it might be worthy to look deeper into this action.

  * Red: Yes, very likely exploitable.
  * Orange: Probably scripting code is involved that can be analyzed with low effort.
  * Cyan: Most common color. These are normal GUI binaries. The window exploit is not working and analyzing further takes a lot of effort.
  * Blue: Those actions invoke commands from the WiX Toolset used to build installers. We assume they are safe (but check the next chapter "Further MSI exploitation ideas").

## Further MSI exploitation ideas

  * The WiX Toolset is often used to build installers. This can introduce vulnerabilities as well. An example is [CVE-2024-29188](https://www.cve.org/CVERecord?id=CVE-2024-29188). Our tool detects installers using the vulnerable RemoveFolderEx function.
  * Basically every CustomAction that is executed in an elevated context is at risk to cause a privilege escalation. It must be ensured that users cannot interfere with it.
  * We focused on the repair function, because this can be invoked as a low-privileged user. However, we also encountered an installer, that was vulnerable only during the installation process. Yet, because the company uses a software portal, where any user can request the installation of this software, we could perform the same exploit.
  * We also used the repair function of a software to trigger a restart of its privileged service. This allowed us to trigger an exploit without restarting the device.

## Microsoft's patch

After our communication with Microsoft, they implemented a patch for the issue that was released on 10th September 2024 (<https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014>). They also assigned CVE-2024-38014 for this vulnerability. The fix now activates a User Account Control (UAC) prompt when the installer executes an action with elevated privileges. This prompt asks for the authentication of a user with extended privileges. When the prompt is denied, the installation is aborted (figure 7):

[![information MSI installer](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-8-46_07.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-8-46_07.png) Figure 8: Four events triggered 

To disable this security measure and return to the original insecure behavior, the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer\DisableLUAInRepair could be set to 1. In this case it must be ensured that no installer in use is vulnerable to a privilege escalation.

## Mitigation (for MSI package authors)

The underlying vulnerability is the usage of console applications that automatically open such a command window that can be interacted with. To write a secure installer that is safe from this exploit, those programs must be started without a visible window. The new patch by Microsoft mitigates this issue, nevertheless writing secure code is always recommended!

  * As mentioned in the blog posts from Mandiant (part of Google Cloud), one option is the usage of <https://wixtoolset.org/docs/v3/customactions/qtexec/>. This will execute the program without the window being visible.
  * The WiX Toolset approach can be reimplemented as well: Write a wrapper (e.g., a DLL) that will launch the program with a hidden window.
  * If the program is self-developed, it can be changed from a console application to a window application (with hidden window). Non-intuitive on the first sight, but it will not show a window.
  * Disable repairing with the property ARPNOREPAIR.

Unrelated to this particular vulnerability, Microsoft offers several guidelines for securing MSI installers:

  * <https://learn.microsoft.com/en-us/windows/win32/msi/guidelines-for-authoring-secure-installations>
  * <https://learn.microsoft.com/en-us/windows/win32/msi/custom-action-security>
  * <https://learn.microsoft.com/en-us/windows/win32/msi/guidelines-for-securing-custom-actions>

## Mitigation (for IT administrators)

We are not aware of any good solution apart from applying the new patch (CVE-2024-38014) and updating Windows and all software. However, we know of two additional possibilities:

  * Customize the MSI package and disable repairing with the property ARPNOREPAIR.
  * Disable installation via a registry key. However, this completely prevents installation of software.

## Detection

Mandiant suggest in their [article](https://www.mandiant.com/resources/blog/privileges-third-party-windows-installers) to observe the Event ID 11728. A successful installation generated the following four events, including this 11728 (see figure 8):

The following sigma rule can be used to detect this event:

**win_application_msi_repair.yml**
  
  
  title: MSI repair process completed
  id: 6cfd7bbd-201f-4fc6-ab23-b485c6d38af1
  status: test
  description: Event signaling the completion of a repair for an application installed through an MSI file; might indicate abuse of this functionality to elevate privileges using the repair process of a vulnerable MSI file
  references:
  - [r.sec-consult.com/msi](https://r.sec-consult.com/msi)
  - [msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014)
  author: Herbert Bärschneider @SEC Consult
  date: 2024-07-12
  tags:
  - attack.t1068
  - cve.2024-38014
  logsource:
  product: windows
  service: application
  detection:
  selection:
  Provider_Name: 'MsiInstaller'
  EventID:
  - 11728 # Product Configuration completed successfully
  condition: selection
  fields:
  - SecurityUserID
  falsepositives:
  - legitimate use of MSI files to repair installed applications by users or administrators
  # level is low, as one needs further context to identify, if this is part of malicious activity; moreover, the event can be evaded by an attacker
  level: low

[![Windows installer](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-4-4_08.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-4-4_08.png) Figure 9: Task manager - ending the process 

However, after we successfully exploited the vulnerability, we are SYSTEM, allowing us to tamper with the installation. For example, we could spawn the Taskmanager (`taskmgr.exe`), and choose the **background** process "Windows installer". We can simply end this process (see figure 9):

[![Windows installer](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-4-37_09.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-4-37_09.png) Figure 10: Ongoing installation fails 

This lets the current ongoing installation fail (figure 10):

[![MSI Installer](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-5-16_10.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2024_09/MSI_image-2024-1-23_23-5-16_10.png) Figure 11: Only the very first event was generated 

As a result, only the very first event (Starting of the Installation) was generated (figure 11):

An event with Event ID 11728 is evaded. Detecting the event itself is not sufficient.

While tracing the process creations of an example exploit of this vulnerability, we noticed that there is no clear parent child relationship between the `msiexec `process at the start and the elevated system shell at the end. At the step of choosing a browser in the properties windows, a new process tree starts from an instance of `svchost`, running `OpenWith `and then the chosen browser.

An investigation of an example exploit of the vulnerability showed multiple aspects of interest:

  * Execution of msiexec with the repair flags
  * Execution of msiexec with SYSTEM privileges
  * Execution of OpenWith with SYSTEM privileges
  * A system shell with SYSTEM privileges being started by a browser process

We created detection rules as Sigma rules for each of these and suggest combining them to identify suspicious behavior.

The first sigma rule matches on the use of msiexec with the command line flag for the repair functionality. A likely exploit of this vulnerability involves an attacker identifying a locally installed application, which used an MSI file. In this situation, the attacker likely utilizes the repair function to trigger the MSI install process and exploits the vulnerability in it. As such, the execution of the repair functionality through msiexec is a possible indicator of an exploit happening.

**process_creation_windows_msiexec_repair.yml**
  
  
  title: Process Execution of Repair Functionality of msiexec.exe
  id: a83342d8-272a-43e3-b7c1-24e6c439f735
  status: test
  description: Execution of the repair functionality of msiexec.exe through the command line. While not malicious itself, it might be part of a chain of actions leading to privilege escalation due vulnerabilities in the used MSI installer.
  references:
  - [r.sec-consult.com/msi](https://r.sec-consult.com/msi)
  - [msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014)
  author: Herbert Bärschneider @SEC Consult
  date: 2024-07-15
  tags:
  - attack.t1068
  - cve.2024-38014
  logsource:
  product: windows
  category: process_creation
  detection:
  selection_msiexec_repair:
  Image|endswith: '\msiexec.exe'
  CommandLine|contains: '/f'
  condition: selection_msiexec_repair
  falsepositives:
  - legitimate use of MSI files to repair installed applications by users or administrators
  level: medium

After the repair functionality was initiated, a new process of msiexec is spawned with an undocumented command line flag. This process has the elevated privileges, which are passed through, until the system shell is executed at the end of the exploit. 

**process_creation_windows_elevated_msiexec.yml**
  
  
  title: Process Execution of Elevated msiexec.exe
  id: 3e1ce5a2-6c4e-473b-8e55-dffcdd1ffc25
  status: test
  description: Execution of elevated msiexec.exe. While not malicious itself, it might be part of a chain of actions leading to privilege escalation due vulnerabilities in the used MSI installer.
  references:
  - [r.sec-consult.com/msi](https://r.sec-consult.com/msi)
  - [msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014)
  author: Herbert Bärschneider @SEC Consult
  date: 2024-07-15
  tags:
  - attack.t1068
  - cve.2024-38014
  logsource:
  product: windows
  category: process_creation
  detection:
  selection_msiexec:
  Image|endswith: '\msiexec.exe'
  CommandLine|contains: '/V' # this is an undocumented parameter, used by the msiexec process that actually runs the MSI actions
  selection_user:
  User|contains:
  - 'AUTHORI'
  - 'AUTORI'
  LogonId: '0x3e7'
  condition: selection_msiexec and selection_user
  falsepositives:
  - legitimate use of MSI files to repair installed applications by users or administrators
  level: low

The choice of browser is given by the program OpenWith. The program normally runs with the privileges of a user account. For exploits of this vulnerability, the program runs with SYSTEM privileges.

**process_creation_windows_elevated_openwith.yml**
  
  
  title: Process Execution of Elevated OpenWith.exe
  id: bd759006-f077-429e-819c-1cba0b3a13bb
  status: test
  description: Detects the use of OpenWith.exe with elevated privileges. While not malicious itself, it might be part of a chain of actions leading to privilege escalation, as subsequent process executions might lead to an interactive shell with elevated privileges.
  references:
  - [r.sec-consult.com/msi](https://r.sec-consult.com/msi)
  - [msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014)
  author: Herbert Bärschneider @SEC Consult
  date: 2024-07-15
  tags:
  - cve.2024-38014
  logsource:
  product: windows
  category: process_creation
  detection:
  selection_openwith:
  Image|endswith: '\OpenWith.exe'
  selection_user:
  User|contains:
  - 'AUTHORI'
  - 'AUTORI'
  LogonId: '0x3e7'
  condition: selection_openwith and selection_user
  level: medium

The last step of the exploit spawns a system shell from the chosen browser. This is generally unusual. Combined with the SYSTEM privileges, it becomes a strong signal for suspicious activity.

**process_creation_windows_elevated_system_shell_browser_parent.yml**
  
  
  title: Elevated System Shell Spawned From Browser
  id: d3c850ab-f715-4a72-a8b0-3223f51c0773
  status: test
  description: Detects elevated system shells spawned through a browser process. This might be part of a local privilege escalation using vulnerable MSI packages.
  references:
  - [r.sec-consult.com/msi](https://r.sec-consult.com/msi)
  - [msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014)
  author: Herbert Bärschneider @SEC Consult
  date: 2024-07-15
  tags:
  - attack.t1068
  - cve.2024-38014
  logsource:
  product: windows
  category: process_creation
  detection:
  selection_shell:
  - Image|endswith:
  - '\powershell.exe'
  - '\pwsh.exe'
  - '\cmd.exe'
  - OriginalFileName:
  - 'PowerShell.EXE'
  - 'pwsh.dll'
  - 'Cmd.Exe'
  selection_user:
  User|contains:
  - 'AUTHORI'
  - 'AUTORI'
  LogonId: '0x3e7'
  selection_browser_parent:
  ParentImage|contains:
  - '\brave.exe'
  - '\chrome.exe'
  - '\chromium.exe'
  - '\firefox.exe'
  - '\iexplore.exe'
  - '\msedge.exe'
  - '\opera.exe'
  - '\safari.exe'
  - '\tor.exe'
  - '\vivaldi.exe'
  condition: selection_shell and selection_user and selection_browser_parent
  level: high

The following Sigma rule combines the detection of an elevated msiexec process with an elevated system shell. These aspects show the start and the end of an exploit of the vulnerability. Matching both in time-wise proximity highlights possible exploit usage. 

**correlation_msi_privesc.yml**
  
  
  title: Privilege Escalation to System using MSI installers
  id: f1cee536-f60a-4e4f-93a6-20766ef27158
  status: test
  description: Detects privilege escalation using vulnerabilities in MSI installers by correlating the use of msiexec with elevated privileges with spawning of an elevated system shell.
  references:
  - [r.sec-consult.com/msi](https://r.sec-consult.com/msi)
  - [github.com/SigmaHQ/sigma/blob/master/rules-threat-hunting/windows/process_creation/proc_creation_win_susp_elevated_system_shell.yml](https://github.com/SigmaHQ/sigma/blob/master/rules-threat-hunting/windows/process_creation/proc_creation_win_susp_elevated_system_shell.yml)
  - [msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38014)
  author: Herbert Bärschneider @SEC Consult
  date: 2024-07-15
  tags:
  - attack.t1068
  - cve.2024-38014
  correlation:
  type: temporal
  rules:
  - 3e1ce5a2-6c4e-473b-8e55-dffcdd1ffc25 # elevated msiexec spawned
  - 61065c72-5d7d-44ef-bf41-6a36684b545f # elevated system shell spawned
  timespan: 30m
  level: high

## Timeline

We have contacted Microsoft about the issue in the MSI installers affecting multiple vendors early 2024 through our CVD process (coordinated vulnerability disclosure) and if there was a more global solution feasible.

  * 2024-01-24: Issue reported to Microsoft Researcher portal, case 85165
  * 2024-02-08: Issue confirmed by Microsoft, investigation continued, determining how to address the issue
  * 2024-03-06: Fix is going to be implemented at May 2024 patch day
  * 2024-03-28: Fix is rescheduled to July 2024 patch day given the complexity and potential impact of regressions.
  * 2024-06-28: Microsoft delays patch because of issues during regression testing until September patch day, more time to fix is needed
  * 2024-09-10: Microsoft publishes fix, assigned CVE-2024-38014
  * 2024-09-12: Release of technical blog post

 _This research has been performed by Michael Baer and published on behalf of the[SEC Consult Vulnerability Lab](/vulnerability-lab/#c1699)._

###  Are you interested in working at SEC Consult? 

SEC Consult is always searching for talented security professionals to work in our team. 

[ More Information ](/career/#c2854)

[ Back ](/blog/)
