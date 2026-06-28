---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-06_90-days-16-bugs-and-an-azure-sphere-challenge.md
original_filename: 2020-10-06_90-days-16-bugs-and-an-azure-sphere-challenge.md
title: 90 days, 16 bugs, and an Azure Sphere Challenge
category: documents
detected_topics:
- access-control
- cloud-security
- command-injection
- automation-abuse
- information-disclosure
- supply-chain
tags:
- imported
- documents
- access-control
- cloud-security
- command-injection
- automation-abuse
- information-disclosure
- supply-chain
language: en
raw_sha256: 5bee9b68f04b56c227eb8e1800a00c64ff07b1e6e36fd5a70617f09d85b4ad69
text_sha256: 91c652087e37a5b856a695b50996fecc4c26f8ec4846f5bd4ea2e5916a13acfd
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# 90 days, 16 bugs, and an Azure Sphere Challenge

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-06_90-days-16-bugs-and-an-azure-sphere-challenge.md
- Source Type: markdown
- Detected Topics: access-control, cloud-security, command-injection, automation-abuse, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `5bee9b68f04b56c227eb8e1800a00c64ff07b1e6e36fd5a70617f09d85b4ad69`
- Text SHA256: `91c652087e37a5b856a695b50996fecc4c26f8ec4846f5bd4ea2e5916a13acfd`


## Content

---
title: "90 days, 16 bugs, and an Azure Sphere Challenge"
url: "https://blog.talosintelligence.com/2020/10/Azure-Sphere-Challenge.html"
final_url: "https://blog.talosintelligence.com/azure-sphere-challenge/"
authors: ["Cisco Talos"]
programs: ["Microsoft"]
bugs: ["Local Privilege Escalation", "RCE", "DoS", "Information disclosure"]
publication_date: "2020-10-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4217
---

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/-xNjCixJ_QJY/Xyq3IamiJxI/AAAAAAAAAOg/ILd_okgk750m_S2IbALbUa8hJ7iblfNUQCPcBGAYYCw/w1200-h630-p-k-no-nu/recurring-2Bblog-2Bimages_vuln-2Bspotlight.jpg)

# 90 days, 16 bugs, and an Azure Sphere Challenge

By  [William Largent](https://blog.talosintelligence.com/author/william-largent/)

  
Tuesday, October 6, 2020 12:07 

  
  

### Cisco Talos reports 16 vulnerabilities in Microsoft Azure Sphere's sponsored research challenge.  
_By Claudio Bozzato, Lilith [-_-]; and Dave McDaniel._

On May 15, 2020, Microsoft kicked off the [Azure Sphere Security Research Challenge](https://www.microsoft.com/en-us/msrc/azure-security-lab), a three-month initiative aimed at finding bugs in [Azure Sphere](https://docs.microsoft.com/en-us/azure-sphere/product-overview/what-is-azure-sphere). Among the teams and individuals selected, Cisco Talos conducted a three-month sprint of research into the platform and reported [16 vulnerabilities](https://blog.talosintelligence.com/vuln-spotlight-microsoft-azure-aug-2020) of various severity, including a privilege escalation bug chain to acquire Azure Sphere Capabilities, the most valuable Linux normal-world permissions in the Azure Sphere context.

The Azure Sphere platform is a cloud-connected and custom SoC platform designed specifically for IoT application security. Internally, the SoC is made up of a set of several ARM cores that have different roles (e.g. running different types of applications, enforcing security, and managing encryption). Externally, the Azure Sphere platform is supported by Microsoft’s Azure Cloud, which handles secure updates, app deployment, and periodic verification of device integrity to determine if Azure Cloud access should be allowed or not. Note however, that while the Azure Sphere is updated and deploys through the Azure Cloud, customers can still interact with their own servers independently.
  
  
  app_manifest.json
  
  
  networkd

Here’s a simplified logical chart of the system:

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/-_QcMorfU_uY/X3yB7lePdoI/AAAAAAAAEyY/yhpPRXRRuHgqe318U24bfq5RRaixjwhmQCLcBGAsYHQ/w640-h526/image1.jpg)

Since the Azure Sphere platform is designed as a secure IoT environment in which customers can flash arbitrary applications (less than ~600KB in size), the most relevant question for the ASSRC was: "Assuming a customer application has been compromised and code execution gained, what can be done from there?" This is reflected in the official scope for the [challenge](https://www.microsoft.com/en-us/msrc/azure-security-lab):

  * Ability to execute code on Pluton.
  * Ability to execute code on Secure World (security-monitor).
  * Ability to execute code on NetworkD through local attack (compromised customer application) or remotely (external network).
  * Anything allowing execution of unsigned code that isn’t pure return oriented programming (ROP) under Linux.
  * Anything allowing elevation of privilege outside of the capabilities described in the application manifest (e.g. changing user ID, adding access to a binary).
  * Ability to modify software and configuration options (except full device reset) on a device in the manufacturing state [DeviceComplete](https://docs.microsoft.com/en-us/azure-sphere/hardware/factory-floor-tasks#set-the-device-manufacturing-state) when claimed to a tenant you are not signed into and have no saved capabilities for.
  * Ability to alter the firewall allowing communication out to other domains not in the app manifest (note: not DNS poisoning).For the purposes of this writeup, we will separate the 16 vulnerabilities by the above in-scope categories, and will also have a section for denial-of-service vulnerabilities which were not considered in scope (no matter the severity or if they were required for other bug chains or not).

### Unsigned code execution
  
  
  noexec
  
  
  VM_MAY*

 **Microsoft Azure Sphere Normal World application ptrace unsigned code execution vulnerability ([TALOS-2020-1090](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1090))**

**Microsoft Azure Sphere Normal World application /proc/self/mem unsigned code execution vulnerability ([TALOS-2020-1093](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1093))**
  
  
  fork()

While admittedly incredibly simple vulnerabilities, due to the amount of researchers participating in the ASSRC, we considered it important to submit these as soon as possible, an opinion later reinforced by fact that the /proc/self/mem vulnerability had been found and reported by Trail of Bits in a previous exercise, but had not been fixed in time for the ASSRC's start. These issues were fixed in 20.07.

We then discovered the following two unsigned code execution vulnerabilities in 20.06:

**Microsoft Azure Sphere Normal World application READ_IMPLIES_EXEC personality unsigned code execution vulnerability ([TALOS-2020-1128](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1128))**

**Microsoft Azure Sphere Normal World application PACKET_MMAP unsigned code execution vulnerability ([TALOS-2020-1134](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1134)/CVE-2020-35608)**
  
  
  READ_IMPLIES_EXEC
  
  
  AF_PACKET
  
  
  /proc/self/mem

**Microsoft Azure Sphere Normal World application /proc/thread-self/mem unsigned code execution vulnerability ([TALOS-2020-1138](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1138))**
  
  
  /proc/self/mem

### Denial-of-Service
  
  
  /dev/pluton

**Microsoft Azure Sphere asynchronous ioctl denial-of-service vulnerability ([TALOS-2020-1117](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1117)/CVE-2020-35609)**
  
  
  /dev/security-monitor

**Microsoft Azure Sphere Littlefs Quota denial of service vulnerability ([TALOS-2020-1129](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1129))**
  
  
  /mnt/config

**Microsoft Azure Sphere Pluton SIGN_WITH_TENANT_ATTESTATION_KEY memory corruption vulnerability ([TALOS-2020-1139](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1129))**
  
  
  /dev/pluton
  
  
  struct azure_sphere_digest

### Information Disclosure

From the information disclosure side of things, one low-hanging issue was submitted within the first couple weeks:

**Microsoft Azure Sphere kernel message ring buffer information disclosure vulnerability ([TALOS-2020-1089](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1089))**
  
  
  application-manager

In a more convoluted sequence, we were also able to dump kernel memory via the littlefs filesystem:

**Microsoft Azure Sphere Littlefs truncate information disclosure vulnerability ([TALOS-2020-1130](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1130))**
  
  
  sys_truncate()

### Privilege escalation chain

First off, it's important to note that McAfee ATR also submitted a very similar chain before us that overlapped in the following two vulnerabilities, so we won't really cover these (but there’s more info in the individual writeups).

**Microsoft Azure Sphere ASXipFS inode type privilege escalation vulnerability ([TALOS-2020-1131](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1131))**

**Microsoft Azure Sphere mtd character device driver privilege escalation vulnerability ([TALOS-2020-1132](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1132))**
  
  
  /mnt/config/uid_map

**Microsoft Azure Sphere uid_map UID uniqueness privilege escalation vulnerability ([TALOS-2020-1137](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1137))**

After this occurred, we utilized one of our many denial-of-service vulnerabilities to reboot the device, after which our application would be running as the uid of another application. This bug has been fixed in 20.08.

**Microsoft Azure Sphere Capability access control privilege escalation vulnerability ([TALOS-2020-1133](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1133))**
  
  
  AZURE_SPHERE_CAP_*

This vulnerability has been fixed in 20.09.

### Privilege escalation (non-chain)

An extra non-utilized vulnerability memory corruption was also discovered within the first month:

**Microsoft Azure Sphere AF_AZSPIO socket memory corruption vulnerability ([TALOS-2020-1118](https://talosintelligence.com/vulnerability_reports/TALOS-2020-1118))**
  
  
  AF_AZSPIO

### Researchers’ retrospective
  
  
  .imagepackage

With regard to the ASSRC itself, we felt the dual facets of monthly (but sometimes faster) updates and having around 70 people looking at the product simultaneously ended up favoring those who could work quicker and with less tooling. Going for the extremely high-value targets (pluton/security-monitor) strictly could not be done without either having an emulation setup or having a privilege escalation chain, both of which are large time-sinks in the context of a three-month competition (granted, a third option was also available, hoping that Microsoft would accept a "Assuming I have XYZ capability…" bug). And so when 20.07 rolled around, all the privilege escalation chains were broken and there's not really any way to dynamically test pluton or security-monitor anymore.

In fairness we must state that monthly updates are part of Azure Sphere’s security model which keeps the device up to date with the latest security patches. In our opinion, while this tactic works very well for fixing the known bugs promptly, it also results in a much less complete examination of the device than might have been possible, due to researchers being handicapped in ways that an attacker would never be. Lower-value reported targets got fixed periodically, repeatedly leaving researchers to find new routes to the higher level problems. We posit that this type of CTF would just result in everyone going ham on low-hanging targets, leaving the higher level and more critical attack surfaces mostly unexamined.

As a parting thought, we'd like to thank the organizers of the event and also the Azure Sphere technical staff who were all extremely helpful in this collaboration. While there were difficulties in this process regarding higher level concepts (e.g. consistency of bug submission responses, both in quality and haste), we consider the ASSRC to have been an overall positive experience and boon for the security posture of the Azure Sphere platform as a whole.

### Conclusion

During the course of the three-month Azure Sphere Security Research Challenge, Cisco Talos found and reported 16 vulnerabilities in the Azure Sphere platform, (TALOS-2020-1141 is not yet fixed so it remains unpublished). For an in-depth look into each of the vulnerabilities, please refer to the individual vulnerability writeups listed above for more information.

### Coverage

The following SNORTⓇ rules will detect exploitation attempts. Note that additional rules may be released at a future date and current rules are subject to change pending additional vulnerability information. For the most current rule information, please refer to your Firepower Management Center or Snort.org.

Snort Rules: 54501-54504, 54645-54648, 54680-54683, 54701-54702, 54729-54732, 54829-54830.

##### Share this post

  * [](https://www.facebook.com/sharer.php?u=https://blog.talosintelligence.com/azure-sphere-challenge/ "Share this on Facebook")
  * [](https://x.com/share?url=https://blog.talosintelligence.com/azure-sphere-challenge/ "Post This")
  * [](https://www.linkedin.com/sharing/share-offsite/?url=https://blog.talosintelligence.com/azure-sphere-challenge/ "Share this on LinkedIn")
  * [](https://www.reddit/submit?url=https://blog.talosintelligence.com/azure-sphere-challenge/ "Reddit This")
  * [](mailto:?body=90 days, 16 bugs, and an Azure Sphere Challengehttps://blog.talosintelligence.com/azure-sphere-challenge/ "Email This")
