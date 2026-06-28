---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-14_youve-crossed-the-line-disturbing-a-hosts-rest.md
original_filename: 2022-12-14_youve-crossed-the-line-disturbing-a-hosts-rest.md
title: You’ve Crossed the Line — Disturbing a Host’s Rest
category: documents
detected_topics:
- sqli
- api-security
- command-injection
- automation-abuse
- supply-chain
tags:
- imported
- documents
- sqli
- api-security
- command-injection
- automation-abuse
- supply-chain
language: en
raw_sha256: 50bdc289adcff66ab32ad8f6e398503cede5fffff9f03a01235c1d99f08dc0b1
text_sha256: 4b9ec4a2982b331227f9476f749911724a078984b11fa2f0f2ef9e475ece54a3
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# You’ve Crossed the Line — Disturbing a Host’s Rest

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-14_youve-crossed-the-line-disturbing-a-hosts-rest.md
- Source Type: markdown
- Detected Topics: sqli, api-security, command-injection, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `50bdc289adcff66ab32ad8f6e398503cede5fffff9f03a01235c1d99f08dc0b1`
- Text SHA256: `4b9ec4a2982b331227f9476f749911724a078984b11fa2f0f2ef9e475ece54a3`


## Content

---
title: "You’ve Crossed the Line — Disturbing a Host’s Rest"
url: "https://www.akamai.com/blog/security-research/msrpc-lsm-cve-disturbing-hosts-rest"
authors: ["Ben Barnea (@nachoskrnl)"]
programs: ["Microsoft"]
bugs: ["Windows", "MS-RPC", "DoS"]
publication_date: "2022-12-14"
added_date: "2022-12-15"
source: "pentester.land/writeups.json"
original_index: 1779
scraped_via: "browseros"
---

# You’ve Crossed the Line — Disturbing a Host’s Rest

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
Blog Security Research You’ve Crossed the Line — Disturbing a Host’s Rest
You’ve Crossed the Line — Disturbing a Host’s Rest

Ben Barnea

December 14, 2022

Share

MS-RPC is largely under-researched, and it can have real-world effects. One of those effects is that vulnerabilities in an RPC interface become exposed.
Executive summary

Akamai researcher Ben Barnea found two important vulnerabilities in a Microsoft Windows RPC service that were assigned CVE-2022-37998 and CVE-2022-37973 with a base score of 7.7.
The vulnerabilities take advantage of several bugs in the Local Session Manager RPC interface.
The vulnerabilities lead to denial-of-service attacks that prevent container and session services (such as Microsoft Defender Application Guard, Sandbox, Docker, and Windows Terminal Server) from working.
The vulnerability exists in unpatched Windows 10, Windows 11, and Windows Server 2022 machines.
The vulnerabilities were responsibly disclosed to Microsoft and addressed in October 2022 Patch Tuesday.
We provide a proof of concept of the vulnerabilities in our research repository.
See our MS-RPC GitHub Repository
Introduction

Akamai Security Intelligence Group dove deeply into MS-RPC research this past year. For a protocol that does so much, MS-RPC is largely under-researched, and it can have real-world effects. One of those effects is that vulnerabilities in an RPC interface become exposed. This is what we are focusing on in this blog post: vulnerabilities within the Local Session Manager (LSM) RPC interface. 

LSM is a service that is part of the Session Manager Subsystem. It’s responsible for the management of local sessions related to terminal server sessions on a Windows machine. It communicates with other related Windows components, such as Winlogon and Csrss. 

LSM is implemented in lsm.dll and contains both client and server logic. LSM exposes several RPC interfaces, with one interesting interface related to the management of sessions of containers that are run inside a Hyper-V virtual machine. The vulnerabilities lie inside this interface.

What is this interface?

The new RPC interface is assigned the UUID c938b419-5092-4385-8360-7cdc9625976a. This interface exposes exactly two functions: ContainerCom_AskForSession and ContainerCom_SessionLoggedOff. The interface is also registered with a security callback that always returns RPC_S_OK, thus allowing access to everyone. The LSM server registers a Hyper-V socket (hvsocket) endpoint that is only accessible to Hyper-V containers.

Fig. 1: Client setting up RPC connection over hvsocket vs server setting up a hvsocket endpoint

When a session is created inside the container (e.g., because of an RDP connection) the LSM client first calls RpcGetRequestForWinlogon inside the container’s LSM. This function arbitrates the session creation, and when it’s running inside a container it first asks for permission from the host. This is done by invoking the RPC call ContainerCom_AskForSession to the host using an hvsocket to the parent. The RPC interface limits the number of sessions to the containers. It does so by keeping track of the newly created sessions. 

How does LSM keep track of sessions?

The answer is simple. There’s a global object called ContainerSessionServer that holds two variables to keep track of sessions:

Counter of total sessions created. This is limited to one, meaning only one session is allowed at any given moment.
A map between a container’s GUID, and its container’s session count. This is limited to two for each container.

Each time a container asks for a session, ContainerSessionServer::AskForSession first checks whether the total session counter is less than one. If so, it increments the total session count and also increments the container’s session counter in the map.

When ContainerSessionServer::OnSessionLoggedOff is called (upon container exit or directly as an RPC call), the function decrements both the total session count and the container’s session count by one. 

Auditing RPC functions for vulnerabilities

Although this interface sounds simple and easy to implement, we found four bugs that we managed to chain into two vulnerabilities.

Chain #1 — DoS through a critical section — CVE-2022-37998
Bug #1 — Failure to exit a critical section

ContainerSessionServer::AskForSession uses a critical section to synchronize access to the global object ContainerSessionServer. 

Fig. 2: Decompiled code of the vulnerability. The function exits without releasing the critical section

As seen above, the critical section is entered at line 112. Later on, at lines 114–116, there’s a check to see if the container’s session counter is at its limit (two). If so, the LSM will not keep track of this session and it immediately exits the function (line 125). Unfortunately, the code does not exit the critical section that was entered. Therefore, further calls to this interface will be stuck waiting for this critical section to be released. 

But, if you recall, there’s a limit of one to the total session counter, so how can we get to a point where a container’s session counter is two? Well, logically it’s not possible. But, then comes the second bug!

Bug #2 — Incorrect tracking of counter

When a session to the container is logged off, an RPC call is made to ContainerSessionServer::OnSessionLoggedOff in the host. This function first decreases the total session counter by calling DecreaseTotalSessionCount. It does so regardless of whether the container is being tracked. If it finds out that the container is not being tracked, it exits without incrementing back the total session counter. 

This can lead to a total session counter with the value of a negative number (as it is a signed integer). We can simply send many OnSessionLoggedOff requests before we send any AskForSession requests, and thus keep decrementing the total session counter to an arbitrary negative number. 

Chaining the first and second bugs

We can use bug #2 to decrease the total sessions counter a few times until it’s a negative number. Then, we can exploit bug #1 by sending two requests to AskForSession. The second time this function is called, it will check that the total session counter is less than 1— and because of the second bug, it is. Then, it will see that the container session counter is 2, and it will return without exiting the critical section.

Fig. 3: An outline of the exploitation process

The DoS depends on whether the new incoming RPC calls are dispatched to the same thread that created the critical section deadlock. If the RPC runtime dispatched the new call to the same thread, then the DoS wouldn’t happen since EnterCriticalSection allows nested ownership; that is, the same thread can call EnterCriticalSection twice. If the RPC call was dispatched to any thread other than the one holding the critical section, then it’d wait forever.

Chain #2 — DoS through memory leak — CVE-2022-37973
Bug #3 — Memory leak

ContainerSessionServer::AskForSession also tracks containers’ events like container exit/pause/resume. This is done by calling HcsOpenComputeSystem with the GUID of the container and then registering a callback with HcsRegisterComputeSystemCallback. 

The registered callback receives a context object. The context is allocated inside ContainerSessionServer::AskForSession. Unfortunately, in many cases in which an error occurs, the function exits without freeing the memory allocated for the context. This leads to a memory leak that an attacker can trigger multiple times. After enough calls, there’s memory exhaustion for the LSM process and the process crashes. 

In our testing, sending RPC requests in an endless loop yielded approximately 3 MB of allocation every second. In our case, after 24 GB of memory was allocated, the LSM service crashed. The time it took to exhaust 24 GB is about two hours. The service is not automatically re-spawned.

Bug #4 — Remote access

Endpoints in MS-RPC are multiplexed. If a server registers multiple interfaces and multiple endpoints, each interface is accessible through each endpoint. Endpoints and interfaces are not bound to each other.

This interface is supposed to be only accessible through the hvsocket to containers. In our case, LSM registers a named pipe endpoint “\pipe\LSM_API_service”, which is remotely accessible. Because of endpoint multiplexing, a remote attacker can connect to the named pipe endpoint and send a request to the container's interface. The fix is simple — the security callback should check what endpoint the client has used, and if it’s not hvsocket, deny access.

Chaining the third and fourth bugs

The container tracking functionality is based on the client identifier property. This means that for an hvsocket the client identifier will be the container’s GUID. For a named pipe, this will be the client’s machine name.

To trigger the first exploit, the client needs to have a client identifier that is an actual GUID of a running container. As such, a remote client would not be able to trigger those bugs unless they successfully ascertain a running container’s GUID and change their machine name — an improbable scenario.

Unfortunately, the third bug (memory leak) allocates the objects before any checks are done on the requested container. This means that a remote attacker (using bug #4) can remotely trigger the memory leak. By calling it multiple times, an attacker can cause memory exhaustion and crash the process.

Impact

While these vulnerabilities are categorized as denial-of-service (DoS) vulnerabilities, they do have a security impact as they allow an attacker to bypass security features.

With the first exploit (critical section), there’s a DoS to the specific new interface. This issue would prevent the creation of new sandbox instances.

With the second exploit, which can be triggered both remotely and from a container, the whole process crashes. Thus, all dependencies on LSM wouldn’t work. Security features such as Microsoft Defender Application Guard and Sandbox also would not work. Additionally, RDP and Docker would not work.

Fig. 4: MDAG error as shown in Microsoft Edge

Summary

These vulnerabilities are a great example of how something that seems simple or insignificant can have truly negative impacts. This interface may seem minor: It has presented us with a few bugs that are easy to trigger and have an interesting impact. 

The reality of the situation is that malicious actors are utilizing these attack chains in the wild. The more insignificant something seems, the more easily it is ignored, and that is prime real estate to be exploited. 

In conjunction with the continuous work we are doing in RPC, we encourage other researchers to look for similar bugs in other RPC interfaces.

If you're interested in RPC research topics such as this, check out our RPC toolkit for more write-ups and tools. You can also follow us on Twitter for real-time updates on this and the other research we are doing here at Akamai.

Want to see more security research?
Security Research
Cyber Security
DDoS
Research

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
