---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-24_remote-command-execution-in-visual-studio-code-remote-development-extension.md
original_filename: 2021-09-24_remote-command-execution-in-visual-studio-code-remote-development-extension.md
title: Remote Command Execution in Visual Studio Code Remote Development Extension
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: b335285f1e433194d62a4d00232a47de3539c3113a4fe2c86b22cf6abc8198ed
text_sha256: b9b6993158d5e68be16e3528e9b014076fdda8c1490380a1b4699d6330a2df51
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Command Execution in Visual Studio Code Remote Development Extension

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-24_remote-command-execution-in-visual-studio-code-remote-development-extension.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `b335285f1e433194d62a4d00232a47de3539c3113a4fe2c86b22cf6abc8198ed`
- Text SHA256: `b9b6993158d5e68be16e3528e9b014076fdda8c1490380a1b4699d6330a2df51`


## Content

---
title: "Remote Command Execution in Visual Studio Code Remote Development Extension"
page_title: "Shielder - Remote Command Execution in Visual Studio Code Remote Development Extension 1.50"
url: "https://www.shielder.it/advisories/remote-command-execution-in-visual-studio-code-remote-development-extension/"
final_url: "https://www.shielder.com/advisories/remote-command-execution-in-visual-studio-code-remote-development-extension/"
authors: ["Abdel Adim `smaury` Oisfi (@smaury92)"]
programs: ["Microsoft"]
bugs: ["RCE"]
publication_date: "2021-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3286
---

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage") __

  * [Home](https://www.shielder.com/ "Home")
  * [Company](https://www.shielder.com/company "Company")
  * [Services](https://www.shielder.com/services "Services")
  * [Advisories](https://www.shielder.com/advisories "Advisories")
  * [Blog](https://www.shielder.com/blog "Blog")
  * [Careers](https://www.shielder.com/careers "Careers")
  * [Contacts](https://www.shielder.com/contacts "Contacts")
  * ENG

[ENG](https://www.shielder.com/advisories/remote-command-execution-in-visual-studio-code-remote-development-extension/ "ENG") [ITA](https://www.shielder.com/it/advisories/remote-command-execution-in-visual-studio-code-remote-development-extension/ "ITA")

# Remote Command Execution in Visual Studio Code Remote Development Extension

Visual Studio Code Remote Development Extension 1.50 failed to sanitize the host field before using it as an argument of the `ssh` command, allowing to inject a `ProxyCommand` option which could be used to run arbitray commands.

## Product Description (from vendor)

Visual Studio Code Remote Development allows you to use a container, remote machine, or the Windows Subsystem for Linux (WSL) as a full-featured development environment.  
You can:

  * Develop on the same operating system you deploy to or use larger or more specialized hardware.
  * Separate your development environment to avoid impacting your local machine configuration.
  * Make it easy for new contributors to get started and keep everyone on a consistent environment.
  * Use tools or runtimes not available on your local OS or manage multiple versions of them.
  * Develop your Linux-deployed applications using the Windows Subsystem for Linux.
  * Access an existing development environment from multiple machines or locations.
  * Debug an application running somewhere else such as a customer site or in the cloud.

No source code needs to be on your local machine to get these benefits. Each extension in the Remote Development extension pack can run commands and other extensions directly inside a container, in WSL, or on a remote machine so that everything feels like it does when you run locally.

### CVE

  * [CVE-2020-17148](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-17148)

### Root Cause Analysis

An argument injection is present in the “Remote - SSH” extension, which is used and installed by the “Remote Development” one.

This extension uses the SSH binary of the host to setup the connection with the remote host.

One of the ways to trigger the SSH connection is to use the `vscode://` URI scheme. Specifically, the format is the following: `vscode://vscode-remote/ssh-remote+$REMOTE_HOST+$PATH_OF_PROJECT_ON_THE_REMOTE_HOST`

Once a user browses an URI as the previous one, VSCode is opened and the extension tries to connect to the `$REMOTE_HOST`.

While connecting the following command is executed: `ssh -T -D $RANDOM_PORT "$REMOTE_HOST" bash`

As no sanitization is performed on the `$REMOTE_HOST` user-supplied input it is possible to inject arbitrary arguments to the SSH binary.

SSH has an option called `ProxyCommand`, which specifies a command which is executed before performing the actual SSH connection.

Combining all together it is possible to execute arbitrary system commands on the host of a victim by forcing them into opening a malicious link.

### Proof of Concept

  1. Install Visual Studio Code
  2. Install the “Remote Development” extension (<https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack>)
  3. Open a browser
  4. Visit the following URL: `vscode://vscode-remote/ssh-remote+-oProxyCommand=C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -c msg %username% command_injection" "a@127.0.0.1+/a`
  5. Confirm to open VSCode
  6. Select a random OS (Linux / Windows / MacOS)
  7. Notice the pop-up executed by Powershell with the message “command_injection”

![](/img/blog/rce-vscode-remote-development.png)

 _The same attack can be reproduced on Linux and MacOS by editing the ProxyCommand._

### Impact

An attacker able to force a victim into visiting a malicious link could execute arbitrary commands on their system.

### Remediation

Upgrade the Visual Studio Code Remote Development Extension to version 1.51 or higher.

## Disclosure Timeline

  * 17/08/2020: The vulnerability was found and reported to Microsoft
  * 20/08/2020: Microsoft acknowledged the vulnerability
  * 02/11/2020: Microsoft released the fix
  * 24/09/2021: Shielder’s advisory is made public

## Credits

Abdel Adim `[smaury](https://twitter.com/smaury92)` Oisfi of Shielder

This advisory was first published on https://www.shielder.com/advisories/remote-command-execution-in-visual-studio-code-remote-development-extension/

__[Advisory](/types/advisory)

Date

24 September 2021

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 €

[Via Palestro, 1/C  
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/@44.8833849,7.3303863,17z/data=!3m1!4b1!4m5!3m4!1s0x4788250440849fa5:0x74cf10f2092abc85!8m2!3d44.8833849!4d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

[info@shielder.com](mailto:info@shielder.com "email Shielder")

Landline: [(+39) 0121 - 39 36 42](tel:+390121393642 "Landline")

Commercial: [(+39) 345 - 57 18 634](tel:+393455718634 "Commercial")

Technical: [(+39) 393 - 16 66 814](tel:+393931666814 "Technical")

[ __](https://twitter.com/ShielderSec "Shielder Twitter profile")[__](https://bsky.app/profile/shielder.com "Shielder Bluesky profile")[__](https://infosec.exchange/@Shielder "Shielder Mastodon profile")[__](https://www.linkedin.com/company/shielder "Shielder LinkedIn profile")[__](https://github.com/shieldersec "Shielder Github profile")

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")

[Services](https://www.shielder.com/services "Services")

[Advisories](https://www.shielder.com/advisories "Advisories")

[Blog](https://www.shielder.com/blog "Blog")

[Careers](https://www.shielder.com/careers "Careers")

[Contacts](https://www.shielder.com/contacts "Contacts")

Copyright © Shielder 2014 - 2026 [Disclosure policy](/disclosure-policy "Disclosure Policy") [Privacy policy](/privacy-policy "Privacy Policy")
