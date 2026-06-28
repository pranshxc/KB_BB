---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-18_mute-the-sound-chaining-vulnerabilities-to-achieve-rce-on-outlook-pt-1.md
original_filename: 2023-12-18_mute-the-sound-chaining-vulnerabilities-to-achieve-rce-on-outlook-pt-1.md
title: 'Mute the Sound: Chaining Vulnerabilities to Achieve RCE on Outlook: Pt 1'
category: documents
detected_topics:
- sqli
- command-injection
- api-security
- automation-abuse
- supply-chain
tags:
- imported
- documents
- sqli
- command-injection
- api-security
- automation-abuse
- supply-chain
language: en
raw_sha256: ea8d39f0d7cd31aee4abbe117cfc3a6237becba5befd5ea3ba0065c64a5b4d21
text_sha256: 1db7fa59598534e6fd1fb159cc91b9206ba32e3e055babe9c01b328d5fd74488
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Mute the Sound: Chaining Vulnerabilities to Achieve RCE on Outlook: Pt 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-18_mute-the-sound-chaining-vulnerabilities-to-achieve-rce-on-outlook-pt-1.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `ea8d39f0d7cd31aee4abbe117cfc3a6237becba5befd5ea3ba0065c64a5b4d21`
- Text SHA256: `1db7fa59598534e6fd1fb159cc91b9206ba32e3e055babe9c01b328d5fd74488`


## Content

---
title: "Mute the Sound: Chaining Vulnerabilities to Achieve RCE on Outlook: Pt 1"
page_title: "Message from Akamai"
url: "https://www.akamai.com/blog/security-research/2023/dec/chaining-vulnerabilities-to-achieve-rce-part-one"
authors: ["Ben Barnea (@nachoskrnl)"]
programs: ["Microsoft (Outlook)"]
bugs: ["RCE"]
publication_date: "2023-12-18"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 614
scraped_via: "browseros"
---

# Mute the Sound: Chaining Vulnerabilities to Achieve RCE on Outlook: Pt 1

Akamai to acquire LayerX to enforce AI usage control on any browser. Get details
 Close
English
Docs
Sales
Support
Under Attack ?
Log in
Cloud Manager
Manage your cloud computing services
Control Center
Manage your security and delivery services
Products
Solutions
Pricing
Developers
Resources
Create account
Blog Security Research Mute the Sound: Chaining Vulnerabilities to Achieve RCE on Outlook: Pt 1
Mute the Sound: Chaining Vulnerabilities to Achieve RCE on Outlook: Pt 1

Ben Barnea

December 18, 2023

Share

Executive summary

Akamai researcher Ben Barnea found two vulnerabilities in Microsoft Windows, which were assigned CVE-2023-35384 and CVE-2023-36710.

An attacker on the internet can chain the vulnerabilities together to create a full, zero-click remote code execution (RCE) exploit against Outlook clients.

The first vulnerability lies in the parsing of a path by the MapUrlToZone function. Exploiting this vulnerability requires sending a crafted email to an Outlook client, which in turn will download a special sound file from an attacker-controlled server.

The second vulnerability lies in the Audio Compression Manager (ACM). This vulnerability is exploited when the downloaded sound file is autoplayed, and it can lead to code execution on the victim machine. This vulnerability is described in detail in part 2 of this blog post.

The vulnerabilities were responsibly disclosed to Microsoft and addressed on the August 2023 and October 2023 Patch Tuesdays.

Windows machines with the October 2023 software update installed are protected from these vulnerabilities. Additionally, Outlook clients that use Exchange servers patched with March 2023 software update are protected against the abused feature.

Read the origin story
Overview

Among the vulnerabilities addressed as part of the March 2023 Patch Tuesday was a critical Outlook vulnerability assigned CVE-2023-23397, which was exploited in the wild by Forest Blizzard, which Microsoft has identified as a Russian state-sponsored threat actor. In December 2023, Microsoft, along with the Polish Cyber Command (DKWOC), published that they had seen recent exploitation attempts of the vulnerability by the same threat actor. The vulnerability allowed an attacker to coerce an Outlook client to connect to the attacker’s server. As part of this connection, the client sends their NTLM credentials to the attacker, who can then crack them offline, or use them in a relay attack. This vulnerability could be exploited remotely over the internet without any user interaction (zero click).

After the patch for this vulnerability was released, we found a bypass that we described in a previous blog post. This bypass was fixed on the May 2023 Patch Tuesday. In that publication, we recommended that Microsoft remove the abused feature, as it introduces a vast and complex attack surface. Since the feature remains in Outlook, we decided to investigate it further.

Eventually, we were able to achieve a full RCE vulnerability chain on Outlook. We found another bypass to the original Outlook vulnerability — a bypass that once again allowed us to coerce the client to connect to an attacker-controlled server and download a malicious sound file. Then, we managed to find a vulnerability in the Windows media parsing library that is used to process and play any audio file in general and Outlook’s notification sounds in particular. An attacker chaining these vulnerabilities together can achieve a zero-click RCE on vulnerable Outlook clients.

This two-part blog post series will present the research we conducted to find the two vulnerabilities. This first part will focus on the previous bypass and a new one. In part 2, we will describe the media parsing vulnerability we found.

The original vulnerability

The Outlook vulnerability that was patched in March is triggered when an attacker sends an email containing a reminder with a custom notification sound. This custom sound is specified by the attacker as a path, using the extended MAPI property PidLidReminderFileParameter. An attacker can specify a UNC path that would cause the client to retrieve the sound file from any SMB server. As part of the connection to the remote SMB server, the Net-NTLMv2 hash is sent in a negotiation message (Figure 1). 

Fig. 1: Coercion of NTLM credentials

To fix the issue, the code now calls MapUrlToZone to classify the path as intranet, local, or internet. If the URL points to a resource on the internet, the default reminder sound is used instead of the custom one.

Finding a bypass

After the mitigation was put in place, we asked ourselves whether it was possible to bypass it.

In this context, a bypass means a path that will both pass the locality test and be used by Outlook to download the sound file from a remote location. In other words, we need to find a path that MapUrlToZone would consider as non-internet, but that CreateFile would treat as an internet domain.

To find such a bypass, we needed to fully understand the inner workings of the functions, and the operations done as part of the path parsing.

Windows paths and URLs

There are many different types of DOS paths in Windows, and much research has been conducted on them and their conversion to NT paths. We will not cover the different Windows path types here; James Forshaw's blog post thoroughly covers this topic.

Let’s go back to our functions of interest. CreateFile receives a Windows path; MapUrlToZone (as hinted by its name) can be passed either a URL or a path. To find a bypass, we first need to understand what path types are supported by each function (or both).

Note: CreateFile and MapUrlToZone do not process paths themselves; instead, they use other WinAPI functions for this purpose. For the sake of brevity, we’ll use CreateFile and MapUrlToZone to refer to their underlying path-parsing functions.

 
	

CreateFile

	

MapUrlToZone

RtlPathTypeUncAbsolute

	

✔

	

✔

RtlPathTypeDriveAbsolute

	

✔

	

✔

RtlPathTypeDriveRelative

	

✔

	

✔

RtlPathTypeRooted

	

✔

	

✘

RtlPathTypeRelative

	

✔

	

✘

RtlPathTypeLocalDevice

	

✔

	

✔

RtlPathTypeRootLocalDevice

	

✔

	

✘

Schemes (file://, http://)

	

✘

	

✔

Table 1: Comparison chart of CreateFile and MapUrlToZone path capabilities

As seen in Table 1, only four path types are supported by both functions: RtlPathTypeUncAbsolute, RtlPathTypeDriveAbsolute, RtlPathTypeDriveRelative, and RtlPathTypeLocalDevice.

First attempt

The first attempt to find a bypass was with an absolute UNC path (RtlPathTypeUncAbsolute). Figure 2 details the structure of the path.

Fig. 2: An absolute UNC path and its components

How does Windows know where the path component begins? Table 2 shows the relevant code (RtlGetFullPathName_Ustr).

  case RtlPathTypeUncAbsolute:
  SeperatorsFound = 0;
  for ( CurrentIndex = 2; CurrentIndex < InputPathLength; ++CurrentIndex )
  {
  CurrentChar = InputPathString->Buffer[CurrentIndex];
  if ( CurrentChar == '\\' || CurrentChar == '/' )
  {
  SeperatorsFound++;
  if ( SeperatorsFound == 2 )
  break;
  }
  }

Copy

Table 2: RtlGetFullPathName_Ustr code snippet that is handling the UNC path

We can see that the code skips the absolute UNC prefix (“\\”), and then assumes that the path component begins one character after the second path separator (‘\’ or ‘/’).

But what happens if we provide a path such as “\\\\localhost\..\Akamai.com\dir\file.txt”?
The path will be processed as follows:

“\\\\” is interpreted as the UNC prefix and the root path component

The path component is “localhost\..\Akamai.com\dir\file.txt”

Normally, no amount of “..” could go above the root path. For example,  “\\localhost\directory\..\file.txt” would result in “\\localhost\directory\file.txt”. However, since in our example the “..” is not part of the root path, the path is converted to “\\\Akamai.com\dir\file.txt”.

This means we found a way to tamper with the path by dropping parts of it.

That is how CreateFile processes this path; how does MapUrlToZone handle it (Table 3)? It first removes the extra backslashes, and thus it interprets the path in a different way:

\\localhost is the server name

\..\ is ignored (as we can’t go above the server name)

Akamai.com\dir\file.txt comprises the path component

Input path: \\\\localhost\..\Akamai.com\dir\file.txt

CreateFile

	

MapUrlToZone

\\\Akamai.com\dir\file.txt

	

\\localhost\Akamai.com\dir\file.txt

Table 3: Input paths for CreateFile and MapUrlToZone and the result of their parsing

MapUrlToZone returns 0 (Local) for the output path seen above.

Although this seems like we found a bypass, unfortunately, the path cannot be used to trigger a UNC request. Notice the extra slash at the beginning of the path processed by CreateFile — this marks the server name as empty. When the multiple UNC provider (MUP) queries the different network providers whether they can handle this (empty) server name, they all return false — therefore, no request is made.

Abusing the difference between how MapUrlToZone  and CreateFile handle this path might require a more complicated solution — perhaps such as finding a way to omit the additional backslash, or finding a parsing mismatch in the MUP code. This is a suggestion for future research.

Second attempt: Bypass #1 (CVE-2023-29324)

As playing with absolute UNC paths did not really work, we continued to the next path type that supports UNC — RtlPathTypeLocalDevice. “\\.\UNC\Akamai.com\test.wav” is an example for a local device path. Specifically, it points to the UNC device name, which will be redirected to the MUP driver.

As we said before, to find a bypass we need to look at the different operations done as part of the parsing of the paths. Table 4 shows that difference.

CreateFile

	

MapUrlToZone

if RtlPathTypeLocalDevice → Advance 4 characters

	

if RtlPathTypeLocalDevice → Advance 4 characters

Skip trailing spaces

	 

Convert ‘/’ to ‘\’

Collapse repeated ‘\’

Remove ‘.’ and ‘..’ components

	

Remove ‘.’ and ‘..’ components

Table 4: Different operations completed as part of path parsing

We can see that CreateFile does extra operations, such as converting forward slashes to backslashes and collapsing repeated backslashes.

Let's take a look at a path that takes advantage of one of these differences  — using an extra path separator. Table 5 shows the resulting paths after the code skips the “UNC\” prefix.

Input path: \\.\UNC\\Akamai.com\test.wav

CreateFile

	

MapUrlToZone

Akamai.com\test.wav

	

\Akamai.com\test.wav

Table 5: Resulting paths after skipping UNC/ prefix

Notice the path in the right column. A path that begins with a path separator followed by a character that is not a path separator is called a rooted path. MapUrlToZone uses the functions IsRootedPath or IsDrivePath to determine if the root path component is local. In our case, the path is rooted and therefore MapUrlToZone returns local.

CreateFile does not have the extra path separator after the UNC prefix, so it knows to extract the domain name correctly, and now accesses the Akamai.com SMB server to retrieve the test.wav file. We found a path that MapUrlToZone considers local, but CreateFile doesn’t. This bypass reenabled exploitation of the Outlook vulnerability CVE-2023-23397.

To mitigate this issue, Microsoft attempted to make the two flows more similar; the operations of converting forward slashes to backslashes and collapsing repeated path separators were now added to the MapUrlToZone path parsing flow.

A thought …

In the previous section, we noted that MapUrlToZone checks whether the path component after “\\.\UNC\” is a drive or a rooted path. We can’t make this path component a rooted path after the fix because repeated path separators are collapsed. However, we can still provide a drive path; for example, “\\.\UNC\C:Akamai.com/test.wav”.

Doing so indeed causes MapUrlToZone to return 0. Unfortunately, no network provider is able to handle a path with a colon in it, so this confusion is not helpful for us. As with our first (failed) attempt, finding a confusion with MUP parsing code can lead to a new vulnerability.

Third attempt: Bypass #2 (CVE-2023-35384)

After the fix, the operations carried out by the two functions are nearly the same (Table 6).

CreateFile

	

MapUrlToZone

if RtlPathTypeLocalDevice → Advance 4 characters

	

If RtlPathTypeLocalDevice → Advance 4 characters

Skip trailing spaces

	 

Convert ‘/’ to ‘\’

	

Convert ‘/’ to ‘\’

Collapse repeated ‘\’

	

Collapse repeated ‘\’

Remove ‘.’ and ‘..’ components

	

Remove ‘.’ and ‘..’ components

Table 6: Operations carried out by CreateFile and MapUrlToZone postfix

However, if we go into deeper detail, we can ask ourselves: How does each function decide that the path is a local device path? Table 7 illustrates code snippets from each function that help determine the path type.

CreateFile

  if (IS_PATH_SEPARATOR(Path[0])  &&
  IS_PATH_SEPARATOR(Path[1])  &&
  (Path[2] == '.' || Path[2] == '?') &&
  IS_PATH_SEPERATOR(Path[3])
		return RtlPathTypeLocalDevice;

Copy

MapUrlToZone

  !strncmp(path, "\\.\", 4) || !strncmp(path, "\\?\", 4)

Copy

Table 7: Code snippets that determine path type

With CreateFile, a path separator can be either a forward slash or a backslash; for example, “\\./” is considered a local device path. With MapUrlToZone, only the exact “\\.\” or “\\?\” paths are considered local device paths. This is a path type confusion — we can make CreateFile recognize the component “\\./” as a local device path while MapUrlToZone won’t. This confusion entails different handling of the path by the two functions.

With this in mind, let’s use a path that contains the “confusing” component: \\./UNC/Akamai.com/file.wav.

When analyzing the decision-making for this path’s type, this is MapUrlToZone’s flow:

Is the path a local drive or a rooted path? No

IsLocalDeviceUNC? No

PathIsUNCW? Yes

PathIsUNCW returns true, and thus the function marks it as an absolute UNC path and advances two characters to skip the UNC prefix “\\”. The output for each function is shown in Table 8.

Input path: \\./UNC/Akamai.com/file.wav

CreateFile

	

MapUrlToZone

UNC\Akamai.com\file.wav

	

./UNC/Akamai.com/file.wav

Table 8: Paths outputs for CreateFile and MapUrlToZone functions

At this point, CreateFile concludes that its output is a UNC path and that Akamai.com is the hostname.

Conversely, MapUrlToZone concludes the following information:

Scheme: file://

Host: .  (dot)

Path: /UNC/Akamai.com/file.wav

Absolute URI: file://./UNC/Akamai.com/file.wav

It turns out that when the absolute URI begins with “file://./” (with the host being “.”), the code interprets the sharename as part of the DOS devices namespace (Figure 3). Thus, “file://./UNC/” refers to the UNC namespace.

Fig. 3: URL with a dot hostname (https://en.wikipedia.org/wiki/File_URI_scheme)

To clarify, both functions consider our input path a UNC path, but of a different type: CreateFile treats it as a Windows local device path, whereas MapUrlToZone sees it as a URL.

At this point, we can trigger confusion between the two functions. Unfortunately, if we don’t perform any tricks, MapUrlToZone would still interpret Akamai.com as the hostname — and since this hostname is an internet domain, the function will return 3, so this is not a bypass.  We need to find another way to abuse the parsing process.

Down the line, MapUrlToZone uses an inner function named SetPath to operate on the path component (Table 9).

CreateFile

	

SetPath

if RtlPathTypeLocalDevice → Advance 4 characters

	 

Skip trailing spaces

Convert ‘/’ to ‘\’

Collapse repeated ‘\’

Remove ‘.’ and ‘..’ components

	

Remove ‘.’ and ‘..’ components

Table 9:  Comparison of operations completed between CreateFile and SetPath

Once again we can take advantage of the difference between the operations carried by the two functions. We know from our previous vulnerability that adding an extra slash can lead to a bypass, so it makes sense to try it again. CreateFile will simply remove the extra slash. 

With MapUrlToZone, CreateUri returns the absolute URI “file://./UNC//Akamai.com/file.wav”. This URI is passed to GetZoneFromUriInternal, which internally leads to another CreateUri call.

And why is that a problem? Since CreateUri received a URL, it converts it back to a Windows path using PathCreateFromUrlW. The returned Windows path is “\\.\UNC\\Akamai.com\test.wav”. The fixed version now knows to remove the extra slash and thus correctly understands Akamai.com is the hostname.

That means we need a more complicated abuse of the difference between CreateFile and SetPath. This time, we will abuse two differences:

CreateFile collapses repeated path separators.

CreateFile removes the ‘.’ and ‘..’ components after the collapse of the repeated path separators.

A path that abuses both differences is \\./UNC/C://../Akamai.com/file.wav. Its processing is detailed in the flow chart in Figure 4.

Fig. 4: Flow chart of the path being parsed by the two functions

We already know that CreateFile’s final path is going to be treated as a UNC path. As for SetPath’s output, MapUrlToZone is going to call GetZoneFromUriInternal with the absolute URI file://./UNC/C:/Akamai.com/file.wav. This time PathCreateFromUrlW converts this URL to the Windows path “\\.\UNC\C:\Akamai.com\file.wav”. This is a local path, and thus MapUrlToZone returns 0 (local). We have once again found a neat bypass!

To fix the issue, the code now calls NormalizeDosDevicePrefix to convert slashes to backslashes, preventing confusion in the detection of a local device path.

Detection and mitigation

Microsoft published comprehensive guidance for the detection and mitigation of the original Outlook vulnerability. From our observation, all the methods specified are applicable to the new vulnerability as they are not dependent on the URL specified in the PidLidReminderFileParameter property.

We recommend that organizations use microsegmentation to block outgoing SMB connections to remote public IP addresses. Furthermore, we recommend that you either disable NTLM in your environment, or add users to the Protected Users group, which prevents the use of NTLM as an authentication mechanism.

Blocking outgoing SMB connections and disabling NTLM can help prevent credentials theft. Yet, when SMB requests fail, Windows falls through to WebDAV if it is enabled. Credentials theft can not be abused through WebDAV, yet downloading the sound file is still possible, which is the second step in our RCE chain.

Why stop now?

In this post, we have detailed the research process that led to the discovery of the two bypasses, including their root-cause analysis. As we’ve shown, Windows path parsing code is complex and often can lead to vulnerabilities. Security researchers who encounter path handling code are encouraged to think about the attack surface it presents.

Other than the bypass of MapUrlToZone in the context of Outlook, we can not rule out the possibility that those vulnerabilities can also lead to Mark-of-the-Web (MotW) bypasses.

Other than the ability to leak NTLM credentials, we also have the ability to download and play an arbitrary sound file. Now you can read part 2 of this blog series, which  details the sound-parsing vulnerability.

Keep reading
Cyber Security
Research
Threat Intelligence
Security Research

Share

Written by

Ben Barnea

Ben Barnea is a Security Researcher at Akamai with interest and experience in conducting low-level security research and vulnerability research across various architectures, including Windows, Linux, IoT, and mobile. He enjoys learning how complex mechanisms work and, more important, how they fail.

Related Blog Posts
Navigating this shift requires a proactive defense architecture that blocks exploits before they ever reach your back-end infrastructure.
SECURITY RESEARCH
The New MCP Specification: What Security Teams Must Prepare For
June 25, 2026
As MCP evolves with a new stateless architecture, security responsibility shifts to developers. Learn how Akamai is threat modeling the new specification.
by Maxim Zavodchik, Segev Fogel, and Gal Meiri
Read more
You are at risk if your Drupal site uses a PostgreSQL database and relies on the JSON:API, Views, or related routing modules.
BLOGS
Decentralized Threat: Stealthy P2P Cryptominer Targeting Ollama Endpoints
May 21, 2026
The Akamai SIRT uncovered a custom P2P Trojan masquerading as system activity. Learn how to detect and mitigate this stealthy Go-based cryptominer.
by Larry Cashdollar
Read more
You are at risk if your Drupal site uses a PostgreSQL database and relies on the JSON:API, Views, or related routing modules.
SECURITY RESEARCH
CVE-2026-9082: Mitigating a Critical SQL Injection Vulnerability in Drupal
May 21, 2026
Learn how the complex Drupal SQLi vulnerability (CVE-2026-9082) exploits PostgreSQL environments and its data theft risks — and how to ensure you’re protected.
by Akamai Security Research
Read more

Rate the helpfulness of this page

PRODUCTS
Cloud Computing
Security
Content Delivery
All Products and Trials
Global Services
COMPANY
About Us
History
Leadership
Awards
Board of Directors
Infrastructure for Innovation
Investor Relations
Corporate Responsibility
Ethics
Locations
Vulnerability Reporting
Accessibility Statement
CAREERS
Careers
Working at Akamai
Students and Recent Grads
Inclusive Workplace
Search Jobs
Culture Blog
NEWSROOM
Newsroom
Press Releases
In the News
Media Resources
LEGAL & COMPLIANCE
Legal
Information Security Compliance
Privacy Trust Center
Privacy Statement
Cookie Settings
EU Digital Services Act (DSA)
GLOSSARY
What Is API Security?
What Is a CDN?
What Is Cloud Computing?
What Is Cybersecurity?
What Is a DDoS attack?
What Is Microsegmentation?
What Is WAAP?
What Is Zero Trust?
See all
EMEA Legal Notice
Service Status
Contact Us
English
English
Deutsch
Español
Français
Italiano
Português
中文
日本語
한국어

© 2026 Akamai Technologies
