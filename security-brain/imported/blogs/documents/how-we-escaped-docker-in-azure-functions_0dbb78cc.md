---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-27_how-we-escaped-docker-in-azure-functions.md
original_filename: 2021-01-27_how-we-escaped-docker-in-azure-functions.md
title: How We Escaped Docker in Azure Functions
category: documents
detected_topics:
- cloud-security
- supply-chain
- sso
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- cloud-security
- supply-chain
- sso
- access-control
- command-injection
- api-security
language: en
raw_sha256: 0dbb78cc3f82c8df10d39d376704f21d11c06f526ab78903d6e54eaa9e51fd27
text_sha256: df61e699ddc29bcb0ac180394ac3481e8ade9c783756f7d3a6aad9275fe18c77
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How We Escaped Docker in Azure Functions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-27_how-we-escaped-docker-in-azure-functions.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, sso, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `0dbb78cc3f82c8df10d39d376704f21d11c06f526ab78903d6e54eaa9e51fd27`
- Text SHA256: `df61e699ddc29bcb0ac180394ac3481e8ade9c783756f7d3a6aad9275fe18c77`


## Content

---
title: "How We Escaped Docker in Azure Functions"
page_title: "How We Escaped Docker in Azure Functions - Intezer"
url: "https://www.intezer.com/blog/research/how-we-escaped-docker-in-azure-functions/"
final_url: "https://intezer.com/blog/how-we-escaped-docker-in-azure-functions/"
authors: ["Intezer"]
programs: ["Microsoft"]
bugs: ["Privilege escalation", "Cloud"]
publication_date: "2021-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3960
---

_Summary of Findings_  
_What is Azure Functions?_  
_Technical Analysis_  
_Proof of Concept_  
_Why Does this Matter?_

## Summary of Findings

In previous months we identified vulnerabilities in [Microsoft Azure Network Watcher](https://intezer.com/blog/cloud-security/cve-2020-16995-microsoft-azure-network-watcher-linux-extension/) and [Azure App Services](https://intezer.com/blog/cloud-security/kud-i-enter-your-server-new-vulnerabilities-in-microsoft-azure/), leading us to investigate other types of Azure compute infrastructure. We found a new vulnerability in [Azure Functions](https://azure.microsoft.com/en-us/services/functions/), which would **allow an attacker to escalate privileges and escape the Azure Functions Docker container to the****Docker host**. 

We reported the vulnerability to Microsoft’s security team. They have determined the issue has no security impact on Azure Functions users. Although it is possible to escape from the function to the host, the Docker host itself is protected by a Hyper-V boundary. Based on our findings Microsoft has made changes to block /etc and /sys directories since this change has already been deployed. 

Instances like this underscore that vulnerabilities are sometimes out of the cloud user’s control. Attackers can find a way inside through vulnerable third-party software. While you should focus on reducing the attack surface as much as possible, you also need to prioritize the runtime environment to make sure you don’t have any malicious code lurking in your systems. 

## What is Azure Functions?

Azure Functions is a serverless compute service that allows users to run code without having to provision or manage infrastructure. Azure Functions is Microsoft’s equivalent to Amazon Web Services’ well-known [Lambda](https://aws.amazon.com/lambda/) service. 

Azure Functions can be triggered by HTTP requests and are meant to run for only a few minutes in order to handle the event. Behind the scenes, the user’s code is run on an Azure-managed container and served without requiring the user to manage their own infrastructure. In other words, if the user wants to take a shortcut they can, since it’s expected that Microsoft will do it for them. This code is segmented securely and is not intended to escape from its confined environment. However, we will soon demonstrate why this is not the case.

We created a demonstration of the vulnerability—mimicking an attacker having execution on Azure Functions and escalating privileges to achieve a full escape to the Docker host. Check it out below.  

## Technical Analysis

An Azure function requires no infrastructure management. It’s triggered by a user merely uploading their code, which enables seamlessly calling the Function. In our example, it’s invoked via HTTP: <https://test11114117.azurewebsites.net> ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-16-3.png)_Figure 1: Example Azure Function handler code_  

As the user can upload any code of their choice, we abused this to gain a foothold over the Function container and further understand its internals. We wrote a reverse shell to connect to our control server once the Function was executed, so that we could operate an interactive shell.![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-17-3.png) _Figure 2: Azure Function reverse shell_  

Once the shell was on our Function we noticed that we were running as a unprivileged ‘app’ user in an endpoint with a ‘SandboxHost’ hostname: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-22-3.png) _Figure 3: Connecting to the Function reverse shell_  

The environment was mostly sterile from utilities, so we added several useful tools—most notably nmap—to our Function directory and then reuploaded the new Function package. 

Using nmap, we scanned localhost to familiarize ourselves with the server. As a result we spotted multiple open ports: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-25-2.png) _Figure 4: Running nmap on an Azure Function_  

## Escalating Privileges

Since our goal was to find an elevation of privilege vulnerability, it was important that we find sockets belonging to processes associated with root. After interrogating network-related /proc files, we were able to map the ports to their corresponding processes: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-23-3.png) _Figure 5: Mapping each open port to the process that owns it_  

We found three privileged processes with an open port. The first was [NGINX](https://www.nginx.com/), a thoroughly tested open-source project. The local NGINX version had no known vulnerabilities so this wouldn’t have helped us. 

The MSI and Mesh processes offered better chances at finding potential problems as they are close-sourced, undocumented Microsoft processes. As such, we were confident that they had been less thoroughly tested. 

MSI, Managed Service Identity, a feature of the serverless model, eliminates the user’s need to manage identities, easing development by letting Azure handle it instead. 

As for the Mesh binary, we couldn’t find much information (it’s unrelated to [Azure’s Fabric Mesh](https://docs.microsoft.com/en-us/azure/service-fabric-mesh/service-fabric-mesh-overview) service which has a similar name). 

Unfortunately, the binaries belonging to the two processes reside in root-owned directories (e.g. /root/mesh/init) and we didn’t have access to them. 

The Mesh process seemed to be less documented and also very relevant for our purposes, so we focused our efforts on finding out what this component does. 

After searching for references to the Mesh binary in Google, we found the questioned “/root/mesh/init” path in the build log of a public Docker image in [Docker Hub](https://hub.docker.com/layers/balag0/km/2/images/sha256-69b1fa875e4e67232364c8b25b3f803633fc82226a1ae65b61a5ce3530dc0625?context=explore) belonging to a Microsoft employee (we deduced this was public on purpose because it’s used internally somehow). 

We downloaded the image, created a container with it and extracted the Mesh Init binary. The binary was compiled from a Go codebase and conveniently for our purposes wasn’t stripped.

Immediately as we opened the binary in IDA we noticed some interesting functions: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-21-3.png) _Figure 6: Mesh binary mount functions_  

Performing a mount is a privileged operation and should our unprivileged user access this functionality through the HTTP server, it could result in privilege escalation. 

With this goal in mind and after some reverse engineering, we found the HTTP paths and variables that would allow us to invoke these functions. The server expected an HTTP variable to specify an operation to invoke:![](https://intezer.com/wp-content/uploads/2025/03/imageforblogpostinte.png)  

At first we attempted to use the mount_RunCifs and mount_RunZip commands, however, we had no success as the system was lacking binaries for these functions to actually work. We had hoped that the third time would be the charm as we looked at mount_RunSquash: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-15-4.png) _Figure 7: mount_RunSquash function disassembly_  

The RunSquash function would simply invoke [squashfuse_ll](https://github.com/vasi/squashfuse) (in the init_server_pkg_mount_runSquashInternal function) to mount the given squashfs image in the path supplied by “filePath” HTTP variable onto the path specified by the “targetPath” HTTP variable. 

With this information, we built our own [squashfs filesystem](https://tldp.org/HOWTO/SquashFS-HOWTO/whatis.html) containing only a single file that would grant our unprivileged app user root permissions using the [sudoers](https://linux.die.net/man/5/sudoers) mechanism.![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-19-3.png) _Figure 8: Creating the sudoers file on our own server_  
![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-24-2.png) _Figure 9: Creating the squashfs image on our own server for the exploit_  

We included this file in our new Function image and instructed the server to mount our evil squashfs image over _/etc/sudoers.d_. This granted root to our unprivileged user: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-20-3.png) _Figure 10: Escalating to root_  

## Escaping Docker

We were able to escalate to root! However, we were still confined to our container. This new freedom was still somewhat limiting but nonetheless an upgrade to a bigger “cage.” 

Escalating to root within a container is a remarkable achievement, yet escalating privileges within containers is not the final destination for an attacker. Compromising the Docker host would give them much more control, allowing them to break away from the container which might be monitored and moving to the Docker host which is often neglected in terms of security. Containers are often scraped for unnecessary items which the attacker might find interesting, so escalating to the Docker host could allow them to gather more compromising leads to incite further damage.

It’s a known [bad practice](https://containerjournal.com/topics/container-security/why-running-a-privileged-container-is-not-a-good-idea/) to host containers with the _**–****–** privileged_ flag, or to grant them non-default capabilities, since this nullifies Docker’s security features. Seeing as Azure Functions’ core is its container, the first thing we did once we had execution over the Function was to check what capabilities our container had been granted. This can be achieved by reading a process’s status file in the _/proc_ directory:  

![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-14-5.png) _Figure 11: Azure Function process capabilities_  

The Cap fields relate to a Linux capability mechanism. We won’t go into detail but decoding the Cap bitmap allows us to list the process’s capabilities, which all processes in the container share: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-26-2.png) _Figure 12: Decoding Function process capabilities_  

We were very surprised to discover that Azure Functions ran with several extra capabilities. With these extra capabilities it was clear that the container was run with the **–****–** privileged flag. 

This by itself would not have helped us initially, since we only had access to an unprivileged user, and the Docker escape techniques available in this scenario required root. This all changed once we found the Privilege Escalation vulnerability. 

Using a [known](https://blog.trailofbits.com/2019/07/19/understanding-docker-container-escapes/) Docker escape technique we ran ‘ps’ on the Docker host: ![](https://intezer.com/wp-content/uploads/2025/03/pasted-image-0-18-3.png) _Figure 13: Running `ps` on the Docker Host_  

In a nutshell, the technique we used—discovered by [Felix Wilhem](https://twitter.com/_fel1x/status/1151487051986087936)—abuses a feature within cgroups and allows calling a binary on the Docker host (only with the SYS_ADMIN capability as given by the **–****–** privileged flag). In our PoC, we instructed the system to run the ‘ps’ command and redirect its output to our containerized filesystem. 

Once we have achieved execution on the Docker host we reported our findings to Microsoft. After assessment they have decided not to fix the bug, as they claim it does not impact security. The reason for this is because the Docker host is not the final host by itself. This “host” was managed by HyperV (Virtual Machine Manager) and protected by its sandbox, therefore our container was essentially a box within a box. This Docker host only contains our own Docker container, and it’s this real host that manages shared infrastructure between different Azure Functions belonging to various Azure customers, which we were not able to access. 

## Proof of Concept

To make reproduction easier for those who would like to probe the Docker host environment, we’ve created an easy to run PoC. It contains instructions on how to upload an Azure Function with a reverse shell so that you can probe the Docker host yourself and perhaps find some use out of it. It’s available on [GitHub](https://github.com/tsarpaul/Azure-Functions-EoP-PoC). 

## Why Does this Matter?

No matter how hard you work to secure your own code, sometimes vulnerabilities are out of your control. It’s critical that you have protection measures in place to detect and terminate when the attacker executes unauthorized code in your production environment. This [Zero Trust mentality](https://thehackernews.com/2021/01/heres-how-solarwinds-hackers-stayed.html) is even echoed by Microsoft. 

## Try our Free Community Edition

Cloud Workload Protection Platforms (CWPP) like [Intezer Protect](https://intezer.com/) monitor the runtime environment to detect and terminate any unauthorized code execution following a vulnerability exploitation or other attack vector. 

Intezer Protect defends the cloud-native stack—including VMs, containers and container orchestration platforms—against the latest threats. You’ll want to know what code is running in your production environments at all times. The [community edition](http://protect.intezer.com/signup) is a quick way to get this visibility. 

[Get Started for Free](http://protect.intezer.com/signup)

If you’re not ready to deploy, we also have a lab environment where you can simulate attacks such as backdoors, malware, and Living off the Land (LotL) threats. [Contact us](https://intezer.com/contact-us/) to access this environment. 

![Paul Litvak](https://intezer.com/wp-content/uploads/2025/03/Paul.png)

######  Paul Litvak 

[ ](https://il.linkedin.com/in/paul-litvak-7b35a7133) [ ](https://twitter.com/polarply)

Paul is a malware analyst and reverse engineer at Intezer. He previously served as a developer in the Israel Defense Force (IDF) Intelligence Corps for three years.
