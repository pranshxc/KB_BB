---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-26_exploring-three-remote-code-execution-vulnerabilities-in-rpc-runtime.md
original_filename: 2023-05-26_exploring-three-remote-code-execution-vulnerabilities-in-rpc-runtime.md
title: Exploring Three Remote Code Execution Vulnerabilities in RPC Runtime
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
raw_sha256: 855edbd939346f234fdd6af7e2cee6e9ba520dc855203e15fcf52d374e8144e1
text_sha256: 18d720b1bae1966b4cb103174b69f76f8c54bad195c51741429c3f2e4b7322d5
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Exploring Three Remote Code Execution Vulnerabilities in RPC Runtime

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-26_exploring-three-remote-code-execution-vulnerabilities-in-rpc-runtime.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `855edbd939346f234fdd6af7e2cee6e9ba520dc855203e15fcf52d374e8144e1`
- Text SHA256: `18d720b1bae1966b4cb103174b69f76f8c54bad195c51741429c3f2e4b7322d5`


## Content

---
title: "Exploring Three Remote Code Execution Vulnerabilities in RPC Runtime"
url: "https://www.akamai.com/blog/security-research/rpc-runtime-exploring-three-vulnerabilities"
authors: ["Ben Barnea (@nachoskrnl)"]
programs: ["Microsoft (Windows)"]
bugs: ["RCE", "MS-RPC", "Integer overflow", "Memory corruption"]
publication_date: "2023-05-26"
added_date: "2023-05-29"
source: "pentester.land/writeups.json"
original_index: 1113
scraped_via: "browseros"
---

# Exploring Three Remote Code Execution Vulnerabilities in RPC Runtime

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
Blog Security Research Exploring Three Remote Code Execution Vulnerabilities in RPC Runtime
Exploring Three Remote Code Execution Vulnerabilities in RPC Runtime

Ben Barnea

May 26, 2023

Share

Executive summary

Akamai researcher Ben Barnea found three important vulnerabilities in Microsoft Windows RPC runtime that were assigned CVE-2023-24869, CVE-2023-24908, and CVE-2023-23405, all with a base score of 8.1.

The vulnerabilities can lead to remote code execution. Since the RPC runtime library is loaded into all RPC servers, and these are commonly used by Windows services, all Windows versions (Desktop and Server) are affected.

The vulnerabilities are integer overflows in three data structures used by the RPC runtime.

The vulnerabilities were responsibly disclosed to Microsoft and addressed in March 2023 Patch Tuesday.

See our MS-RPC GitHub repository
Introduction

MS-RPC is a highly used protocol in Windows networks, and it is relied upon by many services and applications. As such, vulnerabilities in MS-RPC can lead to harsh consequences. The Akamai Security Intelligence Group has been engaging in MS-RPC research for the past year. We’ve found and exploited vulnerabilities, built research tools, and wrote up some of the undocumented internals of the protocol. 

While previous blog posts focused on vulnerabilities in services, this post will examine vulnerabilities in the RPC runtime — the "engine" of MS-RPC. These vulnerabilities are similar to a vulnerability we discovered in May 2022.

A pattern of integer overflow

The three new vulnerabilities have a common theme — they all exist because of an integer overflow in the insertion into three data structures:

SIMPLE_DICT (a dictionary that only saves values)

SIMPLE_DICT2 (a dictionary that saves both keys and values)

Queue 

All these data structures are implemented using a dynamic array that grows each time the array gets full. This happens by allocating twice the memory allocated for the current array. This allocation is susceptible to integer overflow.

Figure 1 presents decompiled code from RPC runtime. It shows the insertion process into the SIMPLE_DICT structure and the vulnerable line of code (highlighted) where integer overflow can be triggered.

Fig. 1: An integer overflow in the expansion of the SIMPLE_DICT struct
Exploring a vulnerability

To trigger a vulnerability, we need to understand its underlying cause, figure out whether a flow to the vulnerable function exists, and how much time it takes to trigger.

For the sake of brevity, we’ll describe one of the three vulnerabilities: the one in the Queue data structure. Since the other integer overflows are similar in nature, the analysis done in the following sections can be conducted interchangeably.

Understanding the integer overflow

A queue is a simple FIFO (first in, first out) data structure. A queue in the RPC runtime is implemented using a struct that contains an array of queue entries, current capacity, and the position of the last item in the queue. 

When a new entry is added to the queue (given that there’s an available slot), all the items are moved forward in the array, and the new item is added to the beginning of the array. The position of the last item in the queue is then incremented.

When a dequeue happens, the last item is pulled out, and the last item’s position is decremented (Figure 2). 

Fig. 2: A queue structure during queue and dequeue operations

As mentioned before, the vulnerability happens in the insertion of a new entry. If the dynamic array is full, the code does the following:

Allocate a new array with the following size:
CurrentCapacity * 2 * sizeof(QueueEntry)

Copy old items to the new array

Free the array of old items

Double the capacity

For a 32-bit system, the overflow will happen in the calculation of the new array size:

We fill the queue with 0x10000000 (!) items. 

An expansion happens. The size of the new allocation is calculated: 0x10000000 * 16.  As this overflows, the new allocation size is 0. 

A zero-length array is allocated.

The code copies the old items array into the new small array. This will lead to a wild copy (a linear large copy).

On a 64-bit system, this vulnerability is not exploitable because there’s a huge allocation that fails. This leads the code to gracefully exit without triggering any out-of-bounds writes. Despite 64-bit systems being invulnerable to this issue, they are vulnerable to the other integer overflows (in SIMPLE_DICT and SIMPLE_DICT2).

Code flow

An RPC connection is represented using the OSF_SCONNECTION class. Each connection can handle multiple client calls (OSF_SCALL), but at every given time only one call is allowed to run on the connection, while others are queued. 

Thus, an interesting function that uses a queue is OSF_SCONNECTION::MaybeQueueThisCall.  It is called as part of dispatching a new call that has arrived on the connection. In this case, the queue is used to "put on hold" incoming calls while another call is being processed.

So, we have a user-controlled way to fill a queue (by sending client calls one after the other), but this function imposes a requirement: A call is currently processed by the connection. That means that if we want to fill the queue, we need to have a call that takes time to complete. While the call is processed, we will send multiple new calls that will fill up the dispatch queue. 

What kind of function call takes the longest to complete? 

The best candidate is a function in which we can cause an infinite loop.

The second best option is an authentication coercion vulnerability because then the server connects to us — thus, we have control over the response time.

A last resort would be a complex function with complicated logic or a function that processes lots of data and therefore takes a lot of time to complete.

We decided to use our own authentication coercion vulnerability.

The time it takes to trigger

So far we understand what it takes to fill the queue and how it can be done. But one important question arises — Is it practical?

We have minimal control over the variable in which the integer overflow happens — we can only increment it one at a time — similar to refcount (reference count) overflows. This kind of integer overflow is marginally worse than integer overflows where two variables we fully control are added or multiplied, or when the size added can be somewhat controlled (e.g., packet size).

As mentioned previously, we must allocate 0x10000000 (~268M) items. This is a lot.

Trying to trigger the vulnerability on my machine yielded a rate of approximately 15 to 20 queued calls per second. This means it would take about 155 days to trigger it on an average machine! We expected to cause a higher number of queued calls per second. Is there a reason why the RPC runtime is so slow? Isn't it multithreaded? 

Our assumption was that multiple threads process and queue different calls for the same connection simultaneously. After some reversing, we found that in practice the flow is a little bit different.

MS-RPC packet handling

Just before a call is dispatched, the code spins a new thread (if needed) and calls OSF_SCONNECTION::TransAsyncReceive. TransAsyncReceive tries to receive a request on the same connection. It then submits the request to the new thread (by calling CO_SubmitRead). 

The other thread picks the request from TppWorkerThread, and it eventually leads to  ProcessReceiveComplete, which calls MaybeQueueThisCall to queue the SCALL to the dispatch queue. Then, it propagates up and tries to receive a new request for this connection. 

Therefore, although we might have multiple threads running, in practice only one is being used for the connection. This means we can’t simultaneously add calls to the queue from multiple threads.

Packet “leftovers”

We tried to find ways to make more calls per second to minimize the time it takes to trigger the vulnerability. While reversing the receiving code, we noticed that if a packet's length is larger than the actual RPC request in the packet, the RPC runtime saves the remainder. Later, when it checks for new requests, it doesn't immediately use the socket. It first checks if it has packet “leftovers” and if so, it serves a new request from the leftovers.

That allowed us to send many fewer packets, each of which contains the maximum number of requests. The number of queued calls per second remained relatively unchanged when we tried to do exactly that, so that did not seem to help.

Summary

Despite the expected low likelihood of exploiting these vulnerabilities, we’ve added them to the list of important vulnerabilities we’ve found in our last year of research on MS-RPC. It’s important to remember that even hard-to-exploit vulnerabilities are an opportunity for a competent (and patient) attacker. 

While MS-RPC has existed for several decades, it still has vulnerabilities waiting to be discovered. 

It is our hope that this research will encourage other researchers to look into MS-RPC and the attack surface it presents. We would like to thank Microsoft for responding quickly and fixing the issues.

Our GitHub repository is full of tools and techniques to help you get started.

See more research
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
