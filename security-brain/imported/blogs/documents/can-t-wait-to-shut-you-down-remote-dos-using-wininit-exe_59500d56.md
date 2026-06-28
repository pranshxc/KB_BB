---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-31_cant-wait-to-shut-you-down-remote-dos-using-wininitexe.md
original_filename: 2023-01-31_cant-wait-to-shut-you-down-remote-dos-using-wininitexe.md
title: Can't Wait to Shut You Down — Remote DoS Using Wininit.exe
category: documents
detected_topics:
- sqli
- api-security
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- sqli
- api-security
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 59500d5666ff675ce59fc2fed4998e9cef91bc296919d44b7aa2a8b1d341b355
text_sha256: 51ab3b0d25c0c28834a8797b1656d32507ddecd3e0310d2849cf4c07b7a2822d
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Can't Wait to Shut You Down — Remote DoS Using Wininit.exe

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-31_cant-wait-to-shut-you-down-remote-dos-using-wininitexe.md
- Source Type: markdown
- Detected Topics: sqli, api-security, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `59500d5666ff675ce59fc2fed4998e9cef91bc296919d44b7aa2a8b1d341b355`
- Text SHA256: `51ab3b0d25c0c28834a8797b1656d32507ddecd3e0310d2849cf4c07b7a2822d`


## Content

---
title: "Can't Wait to Shut You Down — Remote DoS Using Wininit.exe"
page_title: "Message from Akamai"
url: "https://www.akamai.com/blog/security-research/cant-wait-to-shut-you-down-msrpc-wininit"
authors: ["Stiv Kupchik (@kupsul)"]
programs: ["Microsoft"]
bugs: ["DoS", "MS-RPC", "Windows"]
publication_date: "2023-01-31"
added_date: "2023-02-07"
source: "pentester.land/writeups.json"
original_index: 1602
scraped_via: "browseros"
---

# Can't Wait to Shut You Down — Remote DoS Using Wininit.exe

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
Blog Security Research Can't Wait to Shut You Down — Remote DoS Using Wininit.exe
Can't Wait to Shut You Down — Remote DoS Using Wininit.exe

Stiv Kupchik

January 31, 2023

Share

Editorial and additional contributions by Tricia Howard

Executive summary

Akamai researcher Stiv Kupchik found a new denial-of-service (DoS) vulnerability in Microsoft’s Wininit.exe, CVE-2022-44707, with a CVSS score of 6.5.

The vulnerability was responsibly disclosed to MSRC in August, and was patched as part of December’s Patch Tuesday 2022.

The vulnerability abuses the RPC caching mechanism, on which we have done extensive research. We provide a proof of concept of the attack in our RPC toolkit.

By exploiting this vulnerability, an attacker can bypass a security check thanks to the caching mechanism, and interact with the shutdown mechanism on a remote Windows machine — gaining control to stop or initiate shutdowns.

The vulnerability affects all unpatched Windows versions, starting with Windows 8/Server 2012, reinforcing the importance of patching in a timely manner.

See the attack flow
Introduction

In our previous post, Cold Hard Cache, we teased the reveal of some more RPC vulnerabilities we found using our RPC toolkit, and the time has finally come. Today, in another episode of RPC shenanigans, we have Wininit.  

Wininit is a critical Windows process, playing a crucial role in both the start up and shut down of the Windows operating system (to the tune of — if it crashes, the whole system crashes). As such, it exposes multiple RPC interfaces that implement shutdown functionality — some of them are even documented. The vulnerability we found is in the WindowsShutdown interface.

What is the WindowsShutdown interface?

WindowsShutdown is one of the few RPC interfaces exposed by Wininit. It is responsible for the shutdown process (just like the rest of Wininit’s RPC interfaces; surprising, right?). The interface’s UUID is d95afe70-a6d5-4259-822e-2c84da1ddb0d. It is part of MS-RSP (Remote Shutdown Protocol) and has the following capabilities: 

Fig. 1: The capabilities of of the WindowsShutdown interface

Looking at the public IDL file, we can see that only WsdrInitiateShutdown and WsdrAbortShutdown are documented. Should we care about an undocumented function (asked no researcher ever)? To answer that, let’s take a look at the security callback for this interface.

The security callback

The callback first checks the transport protocol, and allows only ALPC or TCP. Then, the authentication level is checked and only RPC_C_AUTHN_LEVEL_PKT_PRIVACY is allowed. If the called function isn’t WsdrCheckForHiberboot, the remote calling user’s token is checked. It is done by comparing the token with a well-known SID (saved in a global variable, created during WinInit’s initialization) — SECURITY_NETWORK_RID. Calls to WsdrCheckForHiberboot are not restricted at all by the security callback.

Fig. 2: The security callback for WindowsShutdown

The RPC interface is registered with the default cache behavior; so, theoretically, if we can successfully call WsdrCheckForHiberboot, the cached successful result would allow us to bypass the SID check on subsequent calls to WsdrInitiateShutdown and WsdrAbortShutdown.

So, what do we need to do to call WsdrCheckForHiberboot?

WsdrCheckForHiberboot

We don’t really care about what the function does, or what hiberboot is (it’s Windows fast startup, for those wondering), but we do need to know how to call it correctly. We want to define the function correctly in an IDL file to compile a client for it. Although the function is undocumented, we can try to look at the advapi CheckForHiberboot, the only documented RPC client we found for WsdrCheckForHiberboot. It only requires two arguments: a Boolean pointer and a Boolean.

Fig. 3: The advapi CheckForHiberboot — the only documented RPC client we found for WsdrCheckForHiberboot

We can recreate the function definition with these arguments, compiling an IDL file and program. But we’re still missing something. When calling the function remotely with our client, the RPC runtime tells us we’re calling the function incorrectly by returning an RPC stub error.

Fig. 4: The first recreation of WsdrCheckForHiberboot definition

Instead of doing more guesswork, we can do something more delicate, but cumbersome. As part of the RPC interface stub, there is a field called ProcFormatString. It’s basically a long binary string that describes the argument types and the return values for all the functions exposed by the interface. This field is used by the RPC runtime while marshaling and unmarshaling the function calls (which is the process that returned the RPC stub error during our initial attempt). Painstakingly parsing that binary string manually, we eventually found out that there is another argument that the function expects to get — of the type wchar_t*. In the next figure, you can see the section from the ProcFormatString of WsdrCheckForHiberboot, with our own comments about each part:

Fig. 5: The section of WsdrCheckForHiberboot from the ProcFormatString

After adding that “new” argument to our function definition, we have liftoff! CheckForHiberboot successfully returns, and we can proceed to call both WsdrInitiateShutdown and WsdrAbortShutdown.

Imma let you finish, but…

Our immediate want is to use the caching attack to call WsdrInitiateShutdown and achieve a remote shutdown. This time there is no guesswork involved. Not only is the function definition documented in the IDL file, but the flags that it expects to get are documented under the advapi function InitiateShutdownA. So, using the flag combination of SHUTDOWN_GRACE_OVERRIDE, SHUTDOWN_HYBRID and SHUTDOWN_FORCE_OTHERS we can force an immediate shutdown.

With this, we basically finished our attack chain, allowing us to bypass the security callback and its SID check and shut down remotely. Technically, it is an escalation of privilege (allowing any authenticated user to call WsdrInitiateShutdown remotely instead of just those allowed under the SECURITY_NETWORK_RID). Since we can only achieve a shutdown using this interface, the vulnerability was categorized as a DoS vulnerability instead.

Detection

We provide an OSQuery to detect unpatched (and therefore vulnerable) versions of Wininit.exe. Akamai Guardicore Segmentation customers can use the Insight feature together with this query to search for vulnerable assets.

  WITH product_version AS (
  WITH os_minor AS (
  WITH os_major AS (
  SELECT substr(product_version, 0, instr(product_version, ".")) as os_major, substr(product_version, instr(product_version, ".")+1) as no_os_major_substr
  FROM file
  WHERE path = "c:\windows\system32\wininit.exe"
  )
  SELECT substr(no_os_major_substr, instr(no_os_major_substr, ".")+1) as no_os_minor_substr, substr(no_os_major_substr, 0, instr(no_os_major_substr, ".")) as os_minor, os_major
  FROM os_major
  )
  SELECT
  CAST(substr(no_os_minor_substr, instr(no_os_minor_substr, ".")+1) AS INTEGER) AS product_minor,
  CAST(substr(no_os_minor_substr, 0, instr(no_os_minor_substr, ".")) AS INTEGER) AS product_major,
  CAST(os_minor AS INTEGER) AS os_minor,
  CAST(os_major AS INTEGER) AS os_major
  FROM os_minor
)
SELECT
  CASE
  WHEN NOT ((os_major = 6 AND os_minor = 3) OR (os_major = 6 AND os_minor = 2) OR (os_major = 10 AND os_minor = 0))
  THEN "not supported"
  WHEN os_major = 6 AND os_minor = 3 AND product_major = 9600 AND product_minor >= 20716 THEN "patched"
  WHEN os_major = 6 AND os_minor = 2 AND product_major = 9200 AND product_minor >= 24011 THEN "patched"
  WHEN (
  (product_major = 14393 AND product_minor >= 5582)
  OR
  (product_major = 10240 AND product_minor >= 19624)
  OR
  (product_major = 19041 AND product_minor >= 1620)
  OR
  (product_major = 22621 AND product_minor >= 963)
  OR
  (product_major = 22000 AND product_minor >= 1335)
  OR
  (product_major = 20348 AND product_minor >= 1366)
  OR
  (product_major = 17763 AND product_minor >= 3770)
  )
  THEN
  "patched"
  ELSE
  "not patched"

Copy
Summary

Although this vulnerability isn’t critical (it’s just a remote shutdown, and not even an unauthenticated one at that), it demonstrates the inherent destructive potential of MS-RPC, as it is built into even the most critical services of the Windows operating system. In addition, unlike other types of vulnerabilities, there is almost no guesswork with RPC — all of the cards are on the (binary) table; you just have to know how to read them.

Finding ways to exploit these critical functions is precisely why we continue our extensive research into MS-RPC. Despite its widespread use, it’s largely underresearched in the grand scheme of things. Vulnerabilities such as the one being discussed today showcase why this type of work is necessary, and we look forward to seeing other researchers work on MS-RPC if they so choose. 

This vulnerability was responsibly disclosed in late August and patched in the December 2022 Patch Tuesday.

Follow us on Twitter!
Cyber Security
DDoS
Research
Security Research
Threat Intelligence

Share

Written by

Stiv Kupchik

Stiv Kupchik is a Security Researcher Team Lead at Akamai. His research projects revolve around OS internals, vulnerability research, and malware analysis. He has presented his research at conferences such as Black Hat, Hexacon, and 44CON. In addition to being a cybersecurity professional, Stiv also has a BSc in physics.

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
