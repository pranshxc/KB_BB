---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-04_galactical-bug-hunting-how-we-discovered-new-issues-in-cd-projekt-reds-gaming-pl.md
original_filename: 2024-04-04_galactical-bug-hunting-how-we-discovered-new-issues-in-cd-projekt-reds-gaming-pl.md
title: 'Galactical Bug Hunting: How we discovered new issues in CD Projekt Red’s Gaming
  Platform'
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: e78706a432bf3a2ca13ff3610df6b6c1d66c8b31dab2381815edf19cacf119d4
text_sha256: a05eb447f646bfe28de972a92bcfb08df6c4c0401f236675d99e11aa708f5af7
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Galactical Bug Hunting: How we discovered new issues in CD Projekt Red’s Gaming Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-04_galactical-bug-hunting-how-we-discovered-new-issues-in-cd-projekt-reds-gaming-pl.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `e78706a432bf3a2ca13ff3610df6b6c1d66c8b31dab2381815edf19cacf119d4`
- Text SHA256: `a05eb447f646bfe28de972a92bcfb08df6c4c0401f236675d99e11aa708f5af7`


## Content

---
title: "Galactical Bug Hunting: How we discovered new issues in CD Projekt Red’s Gaming Platform"
page_title: "Galactical Bug Hunting: How we discovered new issues in CD Projekt Red's Gaming Platform - Anvil Secure"
url: "https://www.anvilsecure.com/blog/galactical-bug-hunting-how-we-discovered-new-issues-in-cd-projekt-reds-gaming-platform.html"
final_url: "https://www.anvilsecure.com/blog/galactical-bug-hunting-how-we-discovered-new-issues-in-cd-projekt-reds-gaming-platform.html"
authors: ["Lautaro Fain (@LautaroFain)"]
programs: ["GOG"]
bugs: ["Local Privilege Escalation", "DoS", "Arbitrary file overwrite"]
publication_date: "2024-04-04"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 353
---

# Galactical Bug Hunting: How we discovered new issues in CD Projekt Red’s Gaming Platform

![Galactical Bug Hunting: How we discovered new issues in CD Projekt Red’s Gaming Platform](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==) By Anvil SecureOn April 4, 2024May 8, 2024 __0 Comments

**_TL;DR:_** We analyzed the way on which GOG Galaxy 2.0 (a gaming platform owned by CD Projekt Red, creators of world-wide known games such as Cyberpunk 2077 and The Witcher Saga) interacts with the underlying filesystem and the Inter-Process Communication (IPC) between its client process and its privileged service. This resulted in the discovery of two new security issues: a Denial-of-Service, assigned _CVE-2023-50915_ , and a Local Privilege Escalation, assigned _CVE-2023-50914_ , which we will detail in this blog post.

The original analysis was started by myself, as part of a broader on-going research project, resulting in _CVE-2023-50915_. Later on, my colleague Alex Popovici joined me to evaluate if the vulnerability could be exploited beyond a DoS, and helped discover _CVE-2023-50914_ along the way.

## Why GOG Galaxy?

The main purpose behind starting this research project was to get further understanding on how to review and exploit both Windows Applications and Environments in the search of security issues. What a better approach to look for consistent motivation than merging both of my passions? Offensive Security and Gaming ❤️.

The process started right away, as I did not have much prior experience with this kind of targets I started going through publicly available vulnerability reports and posts that would match my expectations to learn new techniques I was not familiar with. I learned different ways to abuse inter-process communication, filesystem manipulation, commonly-used frameworks (like Electron or Chromium Embedded Framework), and other common Windows related misconfigurations, among others.

As I read through each of the resources I could find, I started a list of potential targets that included all the currently existent Windows supported Gaming Platforms I could think of, so basically, the first approach was to fire a shotgun shell over all of the targets at the same time and see what would come afterwards. At that moment, this list looked as follows:

  * **Steam** (from _Valve_)
  * **Origin** (from _Electronic Arts_)
  * **Connect** (from _Ubisoft_)
  * **GOG Galaxy** (from _CD Projekt Red_)
  * **Battle.net** (from _Activision Blizzard_ , now owned by _Microsoft_)
  * **Epic Games** (from _Epic Games Publishing_)

To my surprise, GOG Galaxy showed interesting, potentially insecure behaviors during the very first analysis phases, where we analyzed with [Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon), [Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer) and [Wireshark](https://www.wireshark.org/) which files from the system were being manipulated by the Service and what was being sent over the IPC link. This is when I noticed the existence of the first issue, explained in-depth in the sections to-come.

## The Architecture

Before jumping right into the findings, I would like to share some insights on the target architecture we were faced against. This might give you enough tools to understand what kind of attack surface was available to us and, to also familiarize with the logical process we followed to create a mental threat model that would prioritize the available assets accordingly.

Similar to the other platforms that aim to satisfy the same audience, GOG Galaxy is built on top of a `Client - Service` model composed by the following assets:

  * The Client Process
  * The Privileged Process (acting as a Service)

Please follow me through the incoming sub-sections to get more insights on each of the above listed components.

### The Client Process

The Client Process, in this case called `GalaxyClient.exe`, is responsible for handling tasks and features that are related to the front-end side of things. This basically involves taking care of tasks like:

  * **_Site Renderization_** , using an engine to inherit the main web application logic and display it back to the user (tied to features like the game store, community forums and support).
  * Handling the logic for **_Friends Management_** tasks.
  * Manipulating the **_In-Game Overlay_**.
  * Integrating with **_Cloud Storage_** to save game progress.
  * Taking care of some really basic **_Game Library Management_** tasks (only triggering game installs or updates, filesystem interactions and tasks that do not require further elevation).

It is worth noting that this process runs in behalf of the user that executed the program, therefore, it is unprivileged. This means that if the user `PC\Lautaro` executes `GOG Galaxy`, then the `GalaxyClient.exe` process will start under its name, and also, its attached privileges.

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

### The Privileged Process

The Privileged Process, on the other hand, named `GalaxyClientService.exe`, handles all of the tasks that require any kind of elevation, you name it. Some of the tasks tied to this privileges are enumerated down below:

  * Managing **_Game Installs and Updates_** after users prompt them through the Client Process
  * Manipulating the underlying **_Operative System Configuration Components_** (like playing around with the Privilege Descriptors for several different assets in the FileSystem)
  * Taking care of **_Updating the Client Process_** component.

This component is triggered whenever `GOG Galaxy`is executed or the `GalaxyClient.exe` process sends a a new instruction. After startup, `GalaxyClientService.exe` searches and validates if updates are available for the binaries located inside the program's main install directory (`C:\Program Files (x86)\GOG Galaxy`) and also exposes an IPC channel for handling privileged operations initiated by `GalaxyClient.exe`.

Did I mention that this service is running as `NT AUTHORITY\SYSTEM`? The most privileged user on Local Windows Host Installations? Given that context, it’s not really a surprise to handle privileged operations, this also makes it an interesting target when it comes to finding vulnerabilities, if we wanted to find impactful bugs, then this was the way to go.

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

### Inter-Process Communication

If we were to recreate a really high-level, abstract diagram of `GOG Galaxy`'s architecture, it would look like the following:

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

As mentioned before, both `GalaxyClient.exe` and `GalaxyClientService.exe` communicate through an IPC Channel which we presume acts as a zero capacity bi-directional link (in this type of link channels, the sender waits until the receiver informs the sender that it has received the message).

Both of these assets also interact with the underlying filesystem in different ways, such as:

  * Creating, modifying or deleting certain given files
  * Modifying folder structures
  * Modifying asset privileges

When interacting with the Windows filesystem, they will be using different privileges that correspond to what was already mentioned in previous sections.

## CVE-2023-50915: Denial of Service through Arbitrary File Overwrite

### The Issue

So, to recap, both the `GalaxyClient.exe` and the `GalaxyClientService.exe` processes write data on the main GOG Galaxy installation directory (`C:\Program Files (x86)\GOG Galaxy`)

One of the things that is written in equal fashion by both of them are the logs files that get created in the `C:\Program Files (x86)\GOG Galaxy\logs` directory, each of the processes write into its own log file. Because of the inherited privileges of the user who ran `GalaxyClient.exe`, this process will write into the `GalaxyClient.log` on their behalf and, on the opposite hand, `GalaxyClientService.exe` runs as `NT AUTHORITY\SYSTEM` and it does not drop privileges when writing contents into `GalaxyClientService.log`, this means that this file is written by this very same user, as can be evidences in the following screenshot taken from Process Monitor:

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

This might not really sound like an issue so far, but what if I tell you that the Windows `Users`group has Read, Write and Execute privileges over `C:\Program Files (x86)\GOG Galaxy\logs`?

This instantly caught my eye when investigating which kind of access people had over GOG Galaxy's subdirectory structure because given this scenario, we have a privileged process writing a file into a folder that everyone has multiple kinds of access to.

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

### The Theoretical Abuse

Well, after facing the above scenario, some questions popped-up into my mind to validate if I, as an attacker, could somehow take advantage of it! Next steps properly summarize my line of thinking:

  * Can we control where `GalaxyClientService.exe` writes or what it writes?

Despite we cannot control what the service writes into the `GalaxyClientService.log` file (it is just the way on which it works by design) I can definitely try to manipulate the destination file on which this content gets written.

On a first line of thinking, I thought about creating a SymLink using the `CreateSymlink` binary from James Forshaw [Symboliclink Testing Tools Repository](https://github.com/googleprojectzero/symboliclink-testing-tools).

As stated by the instructions of this very same toolkit:

> You can only create symlinks in directories which are empty, this is a limitation on the processing of the junction points, so you can't just drop into %TEMP%. However if you can at least delete the files from the directory you should still be able to do it.

Looks like I will need to delete the whole `logs` directory first and then try to recreate it, but there is no actual issue with this as I (who am within the Windows `Users` Group) can definitely do that!

  * Can we leverage any harm?

This might be a tricky one, how can you turn a plain potential file overwrite without any actual content manipulation into something that would be impactful? Well, if we can point the privileged service to write anywhere from within the Windows Host Installation, why not forcing it into writing over a Critical Windows Driver?

Doing that will actually corrupt the whole Windows Installation, forcing the user to rollback to an old back-up snapshot or either reinstall the Operating System from scratch!

Great, so now that the path is more clear, I can target `C:\Windows\System32\drivers\pci.sys` as it plays a crucial role in handling the interaction between the machine's hardware and the underlying Operating System.

Finally, the overall visual flow of the exploit should look something like this:

![Exploit Visual Flow](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

### The Exploit

After a first manual attempt to trigger this driver overwrite vector worked, I was committed to weaponize my way out through a PowerShell Script that would make the exploitation process much more reliable and scalable.

The code for this exploit can be found on the following repository section: [https://github.com/anvilsecure/gog-galaxy-app-research/tree/main/poc/CVE-2023-50915 - Host Denial-of-Service through Arbitrary File Overwrite](https://github.com/anvilsecure/gog-galaxy-app-research/tree/main/poc/CVE-2023-50915%20-%20Host%20Denial-of-Service%20through%20Arbitrary%20File%20Overwrite)

## CVE-2023-50914: Privilege Escalation via Insecure Inter-Process Communication

### The Issue

Right after I found the Denial-of-Service vector we just talked about, I was prompted to challenge myself and see if I could somehow achieve even more impact with it. Like, could I manipulate anything in any magic way to elevate our own privileges as users within the host machine?

By this point Alex jumped into the research, and again, we committed to that task and dived right into each of the log file contents (`GalaxyClient.log` along with `GalaxyClientService.log`) to see what could be done with them.

At some point, we just noticed that `GalaxyClient.exe` was issuing some interesting instructions to `GalaxyClientService.exe` and that the latter was executing it accordingly with the information provided as parameters, the log entries looked as follows:

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Apparently, whenever a user installs a game the following process takes place:

`GalaxyClient.exe` sends a new packet to the `GalaxyClientService.exe` process through the IPC Channel, asking the service to create a new child directory in the path the users asked to install the game at.

Then, `GalaxyClientService.exe` validates that the packet is signed with the cryptographic key of `GalaxyClient.exe`, acknowledges the reception and proceeds to execute the tasks it was prompted with.

Once the game files are downloaded, installed and located into the appropriate directory, `GalaxyClient.exe` once again sends another packet, asking `GalaxyClientService.exe` to drop the privileges over the created folder so everyone has access to it in the future, mostly so the actual game can write stuff within its own directory without the need to run as an elevated process. And yes, YES, you read it right, this directive called `FixDirectoryPrivileges` is responsible for giving the Windows `Everyone` group full access over the indicated folder.

This behavior was instantly confirmed after manually inspecting the target folder:

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

### The Theoretical Abuse

Once again, immediately after evidencing the above scenario, our mind gets filled up with questions. Questions that we addressed with the following line of thinking:

  * Can we control which directory gets set with those privileges?

We can try forging our own packets but this would definitely be a complex approach due to the in-place integrity checks. Is there any simpler solution to this scenario? Well, we can inject a Custom DLL into `GalaxyClient.exe` and hook the function that calls `FixDirPrivileges` to manipulate the `Directory` parameter value that gets sent to `GalaxyClientService.exe` and replace it with our own `Target Path`instead.

  * Can we leverage any harm?

So, what is the whole point behind modifying the access to a given directory if we cannot take advantage of that? If we can abuse the `Everyone` group permissions to write into `C:\Program Files (x86)\GOG Galaxy\` we will be able to plant a Malicious DLL.

We can then use that planting approach to actually replace a DLL that the privileged `GalaxyClientService.exe` process loads, in this case scenario, `profapi.dll` (a widely known DLL that is used for profiling) seems like a good fit. We certainly know that the affected process uses it because it validates its existence with the `CreateFile` Operation, as can be seen in the following screenshot:

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

We can try to forge our own `profapi.dll` and make it spawn a new shell when loaded by the `NT AUTHORITY\SYSTEM` service!

Finally, the overall visual flow of the exploit should look similar to this, please note that each of the steps is enumerated with a blue number next to it:

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

### The Exploit

We immediately proceeded to manually confirm our thoughts by creating the necessary DLLs (one for hooking purposes, the other one to spawn a system shell) and deep-dived into the manual execution of the steps.

This last process took some hours from our time though, as we also needed to track some implementation issues back and forth. It's always interesting to deal with low-level code and debug different components until you finally get things to work as expected.

The code for this exploit can be found on the following repository section: [https://github.com/anvilsecure/gog-galaxy-app-research/tree/main/poc/CVE-2023-50914 - Privilege Escalation via Insecure Inter-Process Communication](https://github.com/anvilsecure/gog-galaxy-app-research/tree/main/poc/CVE-2023-50914%20-%20Privilege%20Escalation%20via%20Insecure%20Inter-Process%20Communication)

## Conclusions

This blogpost serves as a technical introduction to testing Windows Applications, specifically GOG Galaxy. It explains the different steps that we followed to assess the security standpoint of the target and discover two new vulnerabilities. It also goes into detail on how we were able to exploit those to leverage impact.

We discussed about filesystem interactions as well as IPC Mechanisms, and commented how those could be abused given this specific context scenario. Obviously, there are still other vectors to iterate over that we consider can yield interesting results in the future.

Further technical details of each finding, along with the corresponding proof-of-concept scripts and the demos are available on our [GitHub repository](https://github.com/anvilsecure/gog-galaxy-app-research) and YouTube channel.

## Responsible Disclosure Timeline

  * **2023-09-07:** _Anvil contacted GOG via their support web page with a link containing the advisory with the findings and our 90-day disclosure policy._
  * **2023-09-28:** _After multiple follow-up emails, GOG confirms that they received Anvil's message and that they are forwarding it to their internal security team. Anvil asked if it was possible to be put in direct contact with their security team._
  * **2023-10-10:** _GOG replies that there is no actual ETA and that is not possible to establish a direct communication with their security team._
  * **2023-10-31:** _Anvil requested updates._
  * **2023-11-07:** _GOG replies that there is no update and asks for a new link pointing to the initial advisory as the previous one expired. Anvil provides a new link to the advisory._
  * **2023-12-06:** _Anvil requests an update and reminds GOG that the 90-day disclosure period has already expired. Anvil asks if GOG is requesting an extension._
  * **2023-12-14:** _Anvil requests CVE IDs to MITRE._
  * **2023-12-15** : _MITRE answers with the following assigned CVE IDs: CVE-2023-50914 and CVE-2023-50915_
  * **2024-01-04:** _GOG replies that they are still investigating the issues and that they have no actual ETA to provide. Anvil responds with the CVE IDs assigned by MITRE, and explains that we'll be publishing details about the issues in the upcoming months_
  * **2024-02-20:** _GOG sends an email explaining that the security team is still investigating the issues. Anvil replies that the publication of our blog post is coming soon._

### About the Author

Lautaro Fain is a Security Engineer at Anvil Secure who started his career in the Offensive Security field almost 7 years ago when joining Immunity Inc. in 2017. Since then, he has performed different tasks related to: Reverse Engineering, Exploit Development, Research and Consulting over different technology stacks.

Always eager to learn new things, Lautaro tries to find a way to mix both of his passions while still accomplishing progress in both the Offensive Security and Gaming fields. If not working, you will probably find him either reviewing games for his spanish-based podcast or playing CTF.

Previous research projects covered some other targets within the Game Industry, Reversing Public Cheats and Malicious APKs for a Mobile Game Studio Company, and Creating Hardware Implants.

[ __](https://www.linkedin.com/company/anvil-secure/)
