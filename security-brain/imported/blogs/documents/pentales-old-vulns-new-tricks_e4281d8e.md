---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-14_pentales-old-vulns-new-tricks.md
original_filename: 2023-07-14_pentales-old-vulns-new-tricks.md
title: 'PenTales: Old Vulns, New Tricks'
category: documents
detected_topics:
- mfa
- sso
- idor
- access-control
- ssrf
- command-injection
tags:
- imported
- documents
- mfa
- sso
- idor
- access-control
- ssrf
- command-injection
language: en
raw_sha256: e4281d8e1e53da11fb2116ae70ae3ef149c624b642a6e5ac24234a92a071eb46
text_sha256: 784bde25bcbd27b665b0fd9ec3fc3b11647e3c44d4bea5aa3fc744f3627aa59e
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# PenTales: Old Vulns, New Tricks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-14_pentales-old-vulns-new-tricks.md
- Source Type: markdown
- Detected Topics: mfa, sso, idor, access-control, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `e4281d8e1e53da11fb2116ae70ae3ef149c624b642a6e5ac24234a92a071eb46`
- Text SHA256: `784bde25bcbd27b665b0fd9ec3fc3b11647e3c44d4bea5aa3fc744f3627aa59e`


## Content

---
title: "PenTales: Old Vulns, New Tricks"
page_title: "Pentesting Story: Old Vulns, New Tricks | Rapid7 Blog"
url: "https://www.rapid7.com/blog/post/2023/07/13/pentales-old-vulns-new-tricks/"
final_url: "https://www.rapid7.com/blog/post/2023/07/13/pentales-old-vulns-new-tricks/"
authors: ["Austin Guidry"]
bugs: ["Internal pentest"]
publication_date: "2023-07-14"
added_date: "2023-07-17"
source: "pentester.land/writeups.json"
original_index: 926
---

_At Rapid7 we love a good pentest story. So often they show the cleverness, skill, resilience, and dedication to our customer’s security that can only come from actively trying to break it! In this series, we’re going to share some of our favorite tales from the pen test desk and hopefully highlight some ways you can improve your own organization’s security._

This engagement began like any other [Internal Network Penetration test](/fundamentals/penetration-testing/). I followed a systematic methodology to enumerate the internal domain. The target organization was a financial institution, but their internal domain was administered _via_ Active Directory (AD) like most organizations with more than a handful of computers. AD is a Microsoft product that provides centralized control of the whole gamut of networking devices that an organization may have. This may include workstations, servers, switches, routers, printers, and IoT devices. Additionally, AD can be used for localized, global, or cloud-based networks.

[**Download Rapid7's Annual Vulnerability Intelligence Report**](/info/vulnerability-intelligence-report-2022-edition/) ▶︎

After enumeration, I identified high value targets and a wide range of open ports and services. I used a Metasploit RC file containing instructions and settings to configure Metasploit modules. This allowed me to scan the open ports and services for common/default credentials, vulnerabilities, misconfigurations, software types, version numbers, and other accessible information in the background while I covered more ground manually.  

I began operations to understand the state of several types of combinable networking vulnerabilities, checking for broadcast name services (BNS) and poisoning capabilities, Server Message Block (SMB) Signing statuses for hosts using SMB visible to my attack box (PTK), and for Internet Protocol version 6 (IPv6) traffic. These are some of the more common ways to begin a successful attack path. I checked all of these options on this organization’s network, but I found that I could not leverage BNS poisoning, SMB Signing not required, or IPv6-based attacks.  

Luckily, the Metasploit RC file found default credentials for Intelligent Platform Management Interface (IPMI) assets. The IPMI protocol’s design introduced a vulnerability that provides a hash to someone attempting authentication. A user would attempt to authenticate with a specific username, and the IPMI device would provide the hash for that account. The Metasploit module for dumping IPMI hashes does this exactly for a wordlist full of common usernames and checks the provided hashes against a partial rainbow table of common passwords like “admin” and “root.” In this case, several devices were using credentials such as “admin:admin” and “root:root.”  

This is exciting because IPMI is used to control servers, and more often these days server virtualization is such that several server virtual machines (VMs) are hosted on one physical server computer. I logged into the web interfaces associated with these IPMIs and found within the remote consoles that three of these IPMI assets were hosting VMware ESXi instances. VMware ESXi is, in fact, used to host and manage multiple VMs. The remote consoles provided the IP and website addresses for the VMware ESXi administrative login interfaces. I navigated to these interfaces and typed in the default credentials used on the IPMI hosts… and they were valid!  

At this point, I was quite shocked that default credentials were in use, some 4+ decades after “admin:admin” became an official vulnerability. Not to mention, default credentials to valuable assets is probably the simplest and easiest vulnerability to exploit.  

So, I got into the VMware ESXi consoles and I quickly identified which of the three assets contained the primary Domain Controller (DC) and Exchange Server. As an administrator to the VMware ESXi console, I had a lot of flexibility in what I was able to do with the virtual machines. First, I checked to see if there were sessions still open with these two assets. Both were locked and would require valid credentials to access _via_ (Remote Desktop Protocol) RDP or similar remote access control.  

I could conduct other attacks such as [Denial of Service (DoS)](/fundamentals/denial-of-service-attacks/), deleting the machine or turning it off, but this would immediately be noticed by organization personnel, and most importantly these types of attacks were out of scope. DoS is out of scope for pentesters by default. This type of attack is extremely harmful to business operations, and has the potential to cause irreversible harm.  

I needed to find an interface with which I had administrative control to view data on these VMs vs. trying to use the underlying Operating Systems (OS) within the VMs. I tried to download the VMs, but they would have taken 10 + days for the DC and multiple weeks for the Exchange Server. I tried to create a snapshot of the memory of the DC to attempt to filter credentials from it, but this was also too large and I could not acquire the file during the engagement.  

I asked for help from the consulting team. At Rapid7, we have a deep bench of talented and knowledgeable people and a healthy culture of teamwork and support.  

One of my teammates hopped on a call to help me investigate the potential options. Upon further review of the accessible ports and services in use by the VMware ESXi host, we found that Secure Shell (SSH) was open and accessible. There is a tool called SSHFS, which stands for SSH File System. This tool uses an SSH connection to mount and interact with the files on a remote device. This is similar to Network File Share (NFS) where a user can create a directory and mount it to the directory of a remote device. With administrative credentials to the VMware ESXi device, this provided me administrative control over the remote system’s file system and allowed me to interact with it in the same way as local files.  

From here, I simply navigated to the directory within the DC that contained the NTDS.DIT file. This file is present on all Windows hosts running Active Directory Domain Services (AD DS) and, when it is contained by a Domain Controller this file contains all of the New Technology LAN Manager (NTLM) hashes for all of the accounts on the domain, including users, workstation machine accounts, and service accounts.  

Sometimes, for environments that have or once had devices older than Windows Vista or Server 2008, there are also LM hashes which are incredibly weak. The entire keyspace for LM can be cracked in minutes to hours depending on the hardware, and the entire 8 character keyspace for NTLM can be cracked within several hours on enterprise-grade hardware.  

This does not even cover the most valuable feature of NTLM authentication. NTLM hashes can be used _as passwords_ , making it irrelevant to know the cleartext password that created the hash. This is called a “pass-the-hash” attack. Upon successfully dumping the NTDS.DIT file for the organization’s domain, I now controlled every domain-joined account and device.  

With this control, I switched gears to post-exploitation and demonstrating impact for the organization's stakeholders. I logged into several email accounts, looking for and finding sensitive information such as Social Security Numbers (SSNs) and Account Numbers. I sent emails from organizational personnel’s email accounts to the point-of-contact and myself, demonstrating the impersonation potential. I used cracked account credentials to locate accounts for which Multi-factor Authentication (MFA) had not been configured and enrolled in MFA for one account. I perused several organization-wide network file share servers finding sensitive documents, PII, account numbers, bank and loan statements, and network information. I found multiple PDFs identifying the organization’s ATMs, their names, locations, makes and models, support information from supporting third-parties, and IP addresses.  

I used these ATM IP addresses to conduct additional enumeration attempting to discover attack paths to gain control of ATMs. I found several open ports but was unable to gain access or control to the ATMs. However, within the directories containing ATM information were Excel spreadsheet logs of ATM activity. These non-password-protected spreadsheets held cardholder data, their links to bank customer account numbers, and historical information such as timestamps, locations, transaction amounts, and transaction types.  

The customer’s environment had a lot of time and effort dedicated to security, and the security team covered many of the “low-hanging-fruit.” Sometimes older technology like IPMI is necessary for business. It is vital to understand the risks and to work with the technology we have to secure it against well-documented attacks. Why allow anyone internally to see an administrative resource? Access controls and closing unnecessary ports could minimize the attack surface on exploitable systems. Finally, one of the best defenses continues to be a strong, unique password for all logins, local or domain.  

We, the pentesters at Rapid7 put our experience and knowledge together to reveal the weaknesses in the customer’s environment and give them the opportunities to fix them. Sometimes hacking is like finding a needle in the haystack, but we hackers have automated needle-finding, haystack-searching machines. Do your research, do the best you can, and when in doubt, get a pentest!

[![LinkedIn](/linkedin-logo.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F07%2F13%2Fpentales-old-vulns-new-tricks&title=PenTales%3A%20Old%20Vulnerabilities%2C%20New%20Tricks)[![Facebook](/facebook-logo.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F07%2F13%2Fpentales-old-vulns-new-tricks)[![X](/x-logo.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F07%2F13%2Fpentales-old-vulns-new-tricks&text=PenTales%3A%20Old%20Vulnerabilities%2C%20New%20Tricks)[![Bluesky](/bluesky-dark-logo.svg)](https://bsky.app/intent/compose?text=PenTales%3A%20Old%20Vulnerabilities%2C%20New%20Tricks%20https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F07%2F13%2Fpentales-old-vulns-new-tricks)

#### Article Tags

  * [Penetration Testing](/blog/tag/penetration-testing/)

[![Austin Guidry](/default-author-image.svg)Austin GuidryAuthor Posts](/blog/author/austin/)
