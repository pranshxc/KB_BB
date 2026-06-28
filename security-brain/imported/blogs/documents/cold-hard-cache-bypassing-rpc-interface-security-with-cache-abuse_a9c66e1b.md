---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-11_cold-hard-cache-bypassing-rpc-interface-security-with-cache-abuse.md
original_filename: 2022-10-11_cold-hard-cache-bypassing-rpc-interface-security-with-cache-abuse.md
title: Cold Hard Cache — Bypassing RPC Interface Security with Cache Abuse
category: documents
detected_topics:
- automation-abuse
- api-security
- supply-chain
- access-control
- command-injection
- otp
tags:
- imported
- documents
- automation-abuse
- api-security
- supply-chain
- access-control
- command-injection
- otp
language: en
raw_sha256: a9c66e1b5303438958efcb1a42a3f657c7c888a61fc4bd19796657f823edd0cf
text_sha256: fb990887af51555a0c4186668bba12edc5be1fcef7ca7f2ec7a036c628707ecf
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Cold Hard Cache — Bypassing RPC Interface Security with Cache Abuse

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-11_cold-hard-cache-bypassing-rpc-interface-security-with-cache-abuse.md
- Source Type: markdown
- Detected Topics: automation-abuse, api-security, supply-chain, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `a9c66e1b5303438958efcb1a42a3f657c7c888a61fc4bd19796657f823edd0cf`
- Text SHA256: `fb990887af51555a0c4186668bba12edc5be1fcef7ca7f2ec7a036c628707ecf`


## Content

---
title: "Cold Hard Cache — Bypassing RPC Interface Security with Cache Abuse"
page_title: "Message from Akamai"
url: "https://www.akamai.com/blog/security-research/cold-hard-cache-bypassing-rpc-with-cache-abuse"
authors: ["-"]
programs: ["Microsoft"]
bugs: ["Privilege escalation", "Windows"]
publication_date: "2022-10-11"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2061
scraped_via: "browseros"
---

# Cold Hard Cache — Bypassing RPC Interface Security with Cache Abuse

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
Blog Security Research Cold Hard Cache — Bypassing RPC Interface Security with Cache Abuse
Cold Hard Cache — Bypassing RPC Interface Security with Cache Abuse

Ben Barnea and Stiv Kupchik

October 11, 2022

Share

In this blog post, we will focus on the security callback mechanism of RPC servers, how it can be bypassed by caching, and how we automated our research to flag Windows services as potentially vulnerable.

 

Executive summary

Akamai researchers found two important vulnerabilities in Microsoft Windows RPC services that were assigned CVE-2022-38034 and CVE-2022-38045 with base scores of 4.3 and 8.8,  respectively.

The vulnerabilities take advantage of a design flaw that allows the bypass of MS-RPC security callbacks through caching.

We confirmed that the vulnerability exists in unpatched Windows 10 and Windows 11 machines.

The vulnerabilities were responsibly disclosed to Microsoft and addressed in October’s Patch Tuesday.

The vulnerability discovery process is assisted by an automation tool and methodology developed by Akamai researchers.

We provide a proof of concept of the vulnerabilities and tools used in our research in the RPC toolkit repository.

Introduction

MS-RPC is one of the cornerstones of the Windows operating system. Released back in the 1990s, it has since become rooted in most parts of the system. The service manager? RPC. Lsass? RPC. COM? RPC. Even some domain operations against the domain controller use RPC. Given how commonplace MS-RPC has become, you’d expect it to have been heavily scrutinized, documented, and researched.

Well, not really. Although Microsoft’s documentation about using RPC is quite good, not much more has been written about the subject, and even less has been written by researchers looking into RPC — specifically, about its security. This could probably be attributed to the fact that RPC (not just MS-RPC, though Microsoft certainly added to the mix) is majorly complex, making research and understanding a daunting task.

But we’re always up for the challenge, so we decided to dive head first into the deep sea of MS-RPC. Not just because it’s an interesting research topic, but also because of its security implications — even now, common attack techniques rely on RPC (T1021.003 happens through MS-COM, T1053.005 is MS-TSCH, T1543.003 is MS-SCMR, to name a few). There are security mechanisms built into MS-RPC, but what if there are vulnerabilities there that can allow them to be bypassed or abused, or allow  an exposed RPC service to be abused to impact machines in an undesired way?

In fact, we managed to find a way to bypass one security mechanism through caching. Through it, we found a few services that we could abuse to escalate privileges on remote servers, without many required conditions (which we will dig into later in the post). At the moment, we can share information on two real-life examples of potential exploitation, WksSvc and SrvSvc.   We will publish updates on the other vulnerabilities we found once their disclosure process is finished.

In this blog post, we will focus on the security callback mechanism of RPC servers, how it can be bypassed by caching, and how we automated our research to flag Windows services as potentially vulnerable. Our automation tools, as well as their raw output, can also be found in our RPC toolkit, which is shared in our GitHub repository. Our repository also includes links to other useful references and work done by other researchers that we relied on.

Security callbacks

Before we discuss the vulnerabilities themselves, it’s important to shed some light on one of the most fundamental security mechanisms that MS-RPC implements: security callbacks. Security callbacks allow RPC server developers to restrict access to an RPC interface. It allows them to apply their own logic to allow access to specific users, enforce authentication or transport types, or prevent access to specific opnums (functions exposed by the server are represented using opnums; that is, operation numbers). 

This callback is fired by the RPC runtime each time the client invokes an exposed function on the server.

In our research, we focused on remote client-server interaction. We mention this since the implementations of the RPC runtime server-side code differ between an ALPC endpoint versus a remote endpoint such as a named pipe.

Caching

The RPC runtime implements caching of the security callback’s result for better performance and utilization. That basically means that the runtime will try to use a cached entry before calling the security callback each time. Let's dive into the implementation. 

Before RPC_INTERFACE::DoSyncSecurityCallback invokes the security callback, it first checks to see if a cache entry exists. It does so by calling OSF_SCALL::FindOrCreateCacheEntry. 

OSF_SCALL::FindOrCreateCacheEntry does the following operations:

It fetches the client’s security context from the SCALL (an object that represents a client call).

It fetches the caching dictionary from the client’s security context.

It uses the interface pointer as a key to the dictionary. The value is the cache entry.

If no cache entry exists, it creates one.

A cache entry has three important fields: the number of procedures in the interface, a bitmap, and the interface generation.

During the lifetime of an RPC server, the interface can be changed — for example, if the server calls RpcServerRegisterIf3 on an existing interface. This in turn calls RPC_INTERFACE::UpdateRpcInterfaceInformation, which updates the interface and increments the interface generation. This way the caching knows it needs to “reset” as the cache entries might be from the old interface. 

The caching mechanism can work in two modes: on an interface basis (which is the default behavior) and on a call basis. 

Interface-based caching

In this mode, the caching works on an interface basis. This means that from a caching point of view, there’s no difference between two calls to two different functions as long as they’re on the same interface.

In order to know if the cache entry can be used instead of calling the security callback, the RPC runtime compares the interface generation that is saved in the cache entry with the actual interface generation.  Since the initialization of the cache entry zeroes the interface generation, the first time the comparison is performed, the interface generations will be different and therefore the security callback will be called. If the callback returned successfully, the RPC runtime will update the cache entry’s interface generation (and therefore it’ll be “marked” as a successful cache entry — one that allows access to the interface without calling the security callback again). The next time the client calls a function on the same interface, the cache entry will be used.

Call-based caching

This mode is used when the RPC interface is registered with the RPC_IF_SEC_CACHE_PER_PROC flag.  In this mode, the caching is based on a bitmap that tracks to which procedures the security callback allowed access. Therefore, if the client invoked function Foo and the security callback returned successfully, we’ll have a cache entry for Foo. If the client invokes Bar, the security callback will be called again.

Caching requirements

So, what do we need to have for caching to work? First, we need to clarify some terminology. MS-RPC represents a logical connection between a client and a server using a binding handle. The client and server can manipulate the binding data using designated functions. 

A binding can be authenticated. This happens when the server registers authentication info (by calling RpcServerRegisterAuthInfo), and then the client sets authentication info on the binding. This allows the server to retrieve information about the client’s identity. The output of this authentication process is a security context object created for the client.

The whole caching mechanism is based on this security context. This means that if the binding is not authenticated, then a security context is not created for the client, and thus caching is not enabled. For caching to work, both the server and client need to register and set authentication info. 

But what if the server did not register authentication info? Can we still have caching enabled? Introducing: multiplexing.

Multiplexing

Until Windows 10, version 1703, a service could share the same svchost process with other services. This behavior affects MS-RPC security as some of the RPC runtime objects are shared between all interfaces. For example, when registering an endpoint (such as TCP port 7777), this endpoint can be used to access all of the interfaces that are running under the same process. Therefore, other services that expect to be accessed locally can now also be accessed remotely. This is also described on this page by Microsoft. 

Although the fact that endpoints are multiplexed is already somewhat known and documented,  we would like to present another similar behavior — SSPI multiplexing. As part of registering authentication info, the server must specify the authentication service to be used. The authentication service is a Security Support Provider (SSP), which is a package that processes the authentication info received from the client. In most cases, this will be the NTLM SSP, Kerberos SSP, or the Microsoft Negotiate SSP, which chooses the best available option between Kerberos and NTLM.

The RPC runtime saves the authentication info globally. This means that if two RPC servers share the same process, and one of them registers authentication info, the other server will also have authentication info. A client can now authenticate the binding when accessing each one of the servers. From a security perspective, servers that did not register authentication info, and therefore might not have expected clients to authenticate the binding or for caching to take place, can have those forced upon them.

CVE-2022-38045 — srvsvc

Armed with our new knowledge about RPC security callbacks and caching, we set out to see if we can actually abuse the mechanism in real life. We returned to srvsvc, in which we already found an off-by-one vulnerability in the past.

Srvsvc exposes the MS-SRVS interface. The Server service (also called LanmanServer) is a Windows service that is responsible for the management of SMB shares. Shares are resources — files, printers, and directory trees — that are made accessible over the network by a Common Internet File System (CIFS) server. Essentially, network shares allow users to utilize other devices on the network to perform various daily tasks.

When we looked at the security callback of Srvsvc, we noticed that the function might have another vulnerability, different from the one we’d already found. Let's take a look at the security callback logic:

As seen above, srvsvc’s security callback has the following logic:

If a remote client tries to access a function in the range of 64–73 (inclusive) — deny access

If a remote client that is not a cluster account tries to access a function in the range of 58–63 (inclusive) — deny access

So, in essence, remote clients are prevented from accessing these particular functions of the interface. This range check hints that the restricted functions are sensitive and should be invoked by only expected (local) processes.

Although this check tries to prevent remote access to these functions, a remote attacker can bypass this check by abusing caching. First, a remote attacker invokes a function that is not in this range — a remotely available function. Since the security callback function returns RPC_S_OK, the RPC runtime is going to cache the result as a successful one. Since the interface is not registered with the RPC_IF_SEC_CACHE_PER_PROC flag, the caching is going to be on an interface basis. As a result, the next time the attacker calls any function on the same interface, the cache entry will be used and access will be granted. This means that the attacker can now invoke the local functions to which they shouldn’t have access, and the security callback will not be called at all. 

Srvsvc does not register authentication info, and therefore under normal circumstances, clients can not authenticate the binding, and thus caching is not enabled. As it turns out, Srvsvc shares the same svchost process with other services when the server machine has less than 3.5 GB of RAM. The services “AD Harvest Sites and Subnets Service” and “Remote Desktop Configuration service”   register authentication info, and, therefore, srvsvc is now vulnerable to cache attacks. 

In this specific scenario, an attacker can access restricted functions with the opnums 58–74. One of the things an attacker can do with those functions is to coerce the authentication of the remote machine.

Going on a treasure hunt

After understanding that abusing the security callback’s caching mechanism can yield actual vulnerabilities,  we decided to try to find other interfaces that could be vulnerable to a caching attack. But to find all interfaces manually would be a long and arduous task, so we wanted to find a way to automate it.

We have two approaches we can take when looking for RPC interfaces: through current running processes or through the file system. 

With running processes, we can look at RPC servers already loaded in memory, either on a remote server by querying the remote endpoint mapper (with Impacket’s rpcmap or rpcdump, for example) or locally (using tools like RpcView or RpcEnum). There’s an issue with this approach, though:  We will miss any interface that isn’t currently loaded, and we won’t be able to look at client interfaces, since they aren’t registered.

Alternatively, we can scrape the Windows file system and look for RPC interfaces compiled inside them. For each interface, we parse its registration information by analyzing the arguments passed to RpcServerRegisterIf. This is a similar approach to what is done in RpcEnum, but we scrape the file system instead of the memory.

In our research we chose the filesystem method in order to include interfaces that  were not necessarily loaded in memory. We wrote various scripts and tools to automate the process, which are available in our RPC toolkit repository.

To find interfaces with caching enabled, we don’t really need to parse the RPC interface itself — all the required information can be extracted from the RPC server registration call. The registration function accepts the RPC interface structure, registration flags, and the security callback pointer. Still, parsing the RPC interface structure can provide useful information, like the functions exposed by the interface or whether it is used by an RPC server or client. Although we are mostly interested in RPC servers (where a vulnerability may exist), RPC clients provide good insight into calling the server, which we can reference for exploitation.

The RPC server interface structure is documented, so we don’t have to guess its fields. Also, the size field and the transfer syntax are constant (there are actually two possible transfer syntaxes — DCE NDR and NDR64 — but we have only ever stumbled upon DCE NDR).

It is a trivial matter to find all RPC interface structures by looking for those two constants (using Yara or regular expressions). Once found, we can use the interpreter info field to see what functionality the server implements.

But we’re still lacking information about the interface’s security callback (if it exists) and whether it is cached. For that, we have to turn to our trusty friends, the disassemblers. Every self-respecting disassembler will have an xref functionality, so it is trivial to find all interface registration function calls in an RPC server. From there, we just need to parse the function call arguments to extract the interface structure address (so we can cross reference that with our scraped RPC server data), the security callback address (if it exists), and the RPC interface flags.

 

We have published our scraping scripts, which do exactly that; they are available in our RPC toolkit, alongside their output from Windows Server 2012 and Server 2022. 

CVEs or it didn’t happen

All those methodologies and theories are nice, but do they actually produce results?

The answer to that is yes. There are more than 120 interfaces with both a security callback and caching, many of them undocumented. This, by itself, is no reason to panic, as most times the security callback won’t be affected much by the caching. Commonly, the checks made by the security callback are performed on values that are not cacheable, like the transport protocol sequence (e.g., TCP) or the authentication level. Any change there requires a new security context anyway, since a new connection has to be established, which resets the cache and nullifies any possible caching bypass.

We have found a few vulnerabilities through this research approach. We can only discuss one of those at the moment, since the rest are still in the disclosure process.

WksSvc

CVE-2022-38034 CVSS score: 4.3

WksSvc exposes the MS-WKST interface. The service is responsible for managing domain memberships, computer names, and connections to SMB network redirectors, like SMB printer servers. Looking at the interface’s security callback, we can see that a few functions are treated differently from the rest.

Functions whose opnum is between 8-11 are also checked to be invoked by a local client, which means remotely calling them isn’t allowed. But since we have caching, what would happen if we first call a different function, which is allowed remotely, and then call one of the restricted functions?

You guessed it: We’d be able to call the locally restricted functions remotely because of the caching of the first call’s result. The question now is: Are those functions important enough to warrant them being restricted to only local clients?

The exposed functions are NetrUseAdd, NetrUseGetInfo, NetrUseDel, and NetrUseEnum. If they sound familiar, it’s because they are accessible through netapi32.dll (see NetUseAdd, for example).

This is good, since it gives us a clue on what we can do with this attack. Namely, we can connect the remote server to a network shared folder of our choosing, and even map it to a logical drive letter of our choosing, similarly to net use. (Coincidence? Probably not.)

This gives us two attack scenarios:

1. We can require authentication on our shared folder; we can then either relay it to a different server for an NTLM relay attack, or store the tokens and crack the password offline.

2. Or we can masquerade an existing file server (or pretend to be a new one) with interesting or useful files. Since those files are in our control, we can weaponize them as we see fit, hopefully allowing us to infect the target user.

Those two scenarios, and being able to remotely call locally restricted functions, were enough for Microsoft to categorize this vulnerability as EoP, with a score of 4.3.

That’s not the end of the story, though — we still have a few caveats that we need to overcome.

Security context

The RPC server under WksSvc doesn’t do any authentication registration by itself. If the service is running on its own, no client-side authentication will be possible (it will result in the error RPC_S_UNKNOWN_AUTHN_SERVICE). As such, we need to have the service running with other services to also abuse SSPI multiplexing. This limits our affected Windows versions to those before Windows 10, version 1703, or newer versions that are running with less than 3.5 GB of RAM.

Logon sessions

Another issue, which is built into how network mapped folders work, is that they are limited to the logon session of the user creating them. Because we need to logon in the first place to get security binding and caching, it means that we will always create a different logon session than the existing (interactive) session on the target machine. For all intents and purposes, it means that our vulnerability has no effect. The network mapping we create is under our short-lived logon session, and not the one created by a regular user when they logged into the machine, so it won’t be visible.

To overcome that, we had to dig a bit deeper into the code of NetrUseAdd. As it turns out, there are flags that we can pass NetrUseAdd that direct it to create the mapping in the Global namespace, which affects all users. Those flags are even found in available header file LMUse.h:

Armed with the flags, our code now successfully creates a global mapping, which will affect the interactive session, finishing our exploitation attempt.

Summary

MS-RPC is a large and complex protocol. It also serves some of the core functionality of Windows. Although it has security features that developers can use to secure their RPC servers, it is an interesting topic for security researchers precisely because it contains a vulnerability that can have a security impact.

Despite that, not much public research has been done on the topic. In this blog post, we broached a large security mechanism in MS-RPC — the security callbacks — and found a bypass in the form of callback result caching. We also detailed our research methodology for finding vulnerable RPC servers, and demonstrated some of our findings with vulnerability write-ups.

We hope that this post, and its accompanying RPC toolkit repository, can help others in researching RPC servers and security mechanisms.

Follow us on Twitter!
Cyber Security
Security Research

Share

Written by

Ben Barnea

Ben Barnea is a Security Researcher at Akamai with interest and experience in conducting low-level security research and vulnerability research across various architectures, including Windows, Linux, IoT, and mobile. He enjoys learning how complex mechanisms work and, more important, how they fail.

Written by

Stiv Kupchik

Stiv Kupchik is a Security Researcher Team Lead at Akamai. His research projects revolve around OS internals, vulnerability research, and malware analysis. He has presented his research at conferences such as Black Hat, Hexacon, and 44CON. In addition to being a cybersecurity professional, Stiv also has a BSc in physics.

Related Blog Posts
Attackers do not need to start by asking for secrets.
SECURITY
AI Reconnaissance: The Missing Layer in Chatbot Security
June 23, 2026
Read how Akamai threat researchers uncovered how attackers use benign-looking questions for AI reconnaissance, and why dynamic runtime guardrails are critical.
by Gal Meiri
Read more
Your DNS is a gold mine of exploitable misconfigurations.
SECURITY
DNS Is Your Most Critical — and Most Misconfigured — Security Control
June 18, 2026
DNS has evolved from a basic networking utility into a critical security control layer. Learn about the DNS misconfigurations that today’s attackers actively exploit.
by Ponith Attili
Read more
Using real-time intelligence, Akamai stops machine-speed attacks before they reach the core cloud.
SECURITY
How Akamai Defended an Indian Bank Against Record-Breaking DDoS Attacks
June 17, 2026
Learn how Akamai successfully neutralized one of the largest DDoS attacks ever recorded in the Indian banking sector before a single customer was impacted.
by Prathmesh Verma
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
