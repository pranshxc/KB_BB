---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-05_analyzing-the-sonicwall-custom-grub-luks-encryption-modifications.md
original_filename: 2023-12-05_analyzing-the-sonicwall-custom-grub-luks-encryption-modifications.md
title: Analyzing the SonicWall Custom Grub LUKS Encryption Modifications
category: documents
detected_topics:
- command-injection
- supply-chain
- race-condition
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- supply-chain
- race-condition
- api-security
- mobile-security
language: en
raw_sha256: d12eacf4a9cd41e4b063391ebda7161ef1b0584544adc7c44b25f3f0f81185d5
text_sha256: a23b77b84e97a5c2e6fab9b59aa8d6b13ec711fbb59b5bae0e34fd224feb54f1
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Analyzing the SonicWall Custom Grub LUKS Encryption Modifications

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-05_analyzing-the-sonicwall-custom-grub-luks-encryption-modifications.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, race-condition, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `d12eacf4a9cd41e4b063391ebda7161ef1b0584544adc7c44b25f3f0f81185d5`
- Text SHA256: `a23b77b84e97a5c2e6fab9b59aa8d6b13ec711fbb59b5bae0e34fd224feb54f1`


## Content

---
title: "Analyzing the SonicWall Custom Grub LUKS Encryption Modifications"
page_title: "Analyzing the SonicWall Custom Grub LUKS Encryption Modifications | Praetorian"
url: "https://www.praetorian.com/blog/sonicwall-custom-grub-luks-encryption/"
final_url: "https://www.praetorian.com/blog/sonicwall-custom-grub-luks-encryption/"
authors: ["Adam Crosser", "Michael Weber (@BouncyHat)"]
programs: ["SonicWall"]
bugs: ["Reverse engineering"]
publication_date: "2023-12-05"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 649
---

Skip to content

**Meet Constantine – Find Mythos-level vulnerabilities in your code. It proves them, patches them, PRs them back. Autonomously.**

[ Download Datasheet ](/resources/constantine-datasheet/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

  * Platform  Close Platform Open Platform

#### [Praetorian Guard Platform](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Services  Close Services Open Services

#### [Penetration Testing Services](/penetration-testing/)

  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)
  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)

#### [Advanced Offensive Security](/advanced-penetration-testing/)

  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)
  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)

#### [Continuous Offensive Security](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Why Praetorian  Close Why Praetorian Open Why Praetorian

#### [Customer Case Studies](/customer-success-in-cybersecurity/)

  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)
  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)

#### Resources

  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)
  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)

#### Use Cases

  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)
  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)

  * About  Close About Open About

#### [About Praetorian](/praetorian-offensive-cybersecurity-company/)

  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)
  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)

#### [Join Praetorian](/careers/#job-opening)

  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)
  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)

  * [ Platform Demo  ](/praetorian-guard-demo/)

  * [ Contact Us  ](/contact-us/)

  * [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

# Analyzing the SonicWall Custom Grub LUKS Encryption Modifications

  * [Adam Crosser](https://www.praetorian.com/author/adam-crosser/), [Michael Weber](https://www.praetorian.com/author/michael-weber/)
  * [ December 5, 2023 ](https://www.praetorian.com/blog/2023/12/05/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/SonicWall-LUKS-7.png)

## Overview

Recently, we decided to perform some reverse engineering of the SonicWall NSv appliance to identify any potential remote code execution vulnerabilities within the appliance. During our initial analysis of a virtual machine image for the application, we discovered a customized LUKS encryption mechanism meant to hinder reverse engineering of the application.

We were able to recover the LUKS decryption key by leveraging Qemu with dynamic analysis/debugging within GDB, however, we still didn’t understand how this decryption mechanism actually worked, as it appeared to be a modified version of LUKS. After performing some reverse engineering, we discovered some modifications made to the GRUB LUKS module that included a custom key-derivation algorithm. It derived the key to decrypt the LUKS partition based on the LUKS header of the partition being decrypted.

We analyzed this key-derivation algorithm and developed a utility named [sonicwall-nsv-decrypter ](https://github.com/praetorian-inc/sonicwall-nsv-decrypter)that calculates the decryption key to decrypt a SonicWall NSv partition based on the LUKS file header. This key can then be used with standard LUKS utilities such as cryptsetup to decrypt and analyze SonicWall NSv partitions containing the core filesystem and application code.

## Attempting to Jailbreak the Appliance

We initially attempted to analyze the SonicWall NSv appliance by SSHing into the appliance as the management user. However, the management user account did not have any shell access to the system which hindered reverse engineering of the application. At this point, we were unable to access the underlying filesystem of the application and analyze the application binaries used for the web interface component of the application.

### Hurdle One: LUKS Encryption

Normally, to get around these restrictions we could simply boot into a LiveCD and mount the hard disk partitions containing the root filesystem. This would then allow us to modify the /etc/passwd file to run the bash shell when accessing the appliance. We could then either modify sudoers or add a new SUID binary to the system to achieve root access to the image for analysis purposes.

However, when we attempted this with the SonicWall NSv appliance we observed that the core partitions containing the application code and root filesystem were encrypted with LUKS encryption. Figure 1 shows the output of the lsblk command when analyzing the virtual hard disk of the appliance which indicates the ROOT, OEM-CONFIG, OEM, and USR-A partitions were all encrypted with LUKS encryption.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20762%20343'%3E%3C/svg%3E)

_Figure 1: An analysis of the virtual hard disk image containing the SonicWall NSv appliance indicated that all of the core partitions containing application code were encrypted using LUKS encryption._

We were quite perplexed by this as we knew that the appliance booted successfully, meaning at some point it used the correct decryption key to decrypt the filesystem and mount the relevant partitions.

### Hurdle Two: GRUB Binaries

Presuming that the decryption key was stored somewhere on the unencrypted EFI-SYSTEM partition, we searched for any LUKS decryption key material. Unfortunately our initial investigation to find explicit decryption keys in the binaries on the partition yielded nothing useful. The EFI-SYSTEM partition was almost entirely GRUB binaries and libraries with no obvious hardcoded keys. However, we were able to find the following grub.cfg file embedded in several different GRUB kernel files:
  
  
  # 1 "/dev/stdin"
  
  # 1 "<built-in>"
  
  # 1 "<command-line>"
  
  # 1 "/usr/include/stdc-predef.h" 1 3 4
  
  # 1 "<command-line>" 2
  
  # 1 "/dev/stdin"
  
  insmod luks
  
  insmod crypto
  
  
  set prefix=($root)/coreos/grub
  
  if search --no-floppy --set oem_config_partition --part-label OEM-CONFIG --hint "$root"
  
  then if cryptomount $oem_config_partition
  
       then configfile (crypto0)/grub.cfg
  
            echo "System failed to boot, halt in 10 seconds"
  
            sleep 10
  
            halt
  
       else
  
            echo "System configuration locked, halt in 10 seconds"
  
           sleep 10
  
           halt
  
       fi
  
  else echo "System configuration missing, halt in 10 seconds"
  
       sleep 10
  
       halt
  
  fi
  
  echo "System loader failed, halt in 10 seconds"
  
  sleep 10
  
  halt

The use of cryptomount was encouraging to see, since that was obviously how the next partition (labeled as OEM-CONFIG) would be decrypted, but frustratingly the system didn’t appear to provide any passphrase to cryptomount. We scoured the online documentation trying to figure out the default password, and the most frequent comment on “default” LUKS passwords was that there is no such thing as default LUKS passwords.

### Hurdle Three: Partition Decryption with Concurrent GRUB Debugging

As a quick sanity check, we attempted to use cryptsetup to decrypt the OEM-CONFIG partition using a blank passphrase, but it was rejected. Clearly some kind of passphrase was in use, but we had no idea where it was. The only way to determine the key would be to debug the GRUB bootloader as it decrypted the partition.

Before doing that we had to identify code where we could drop a breakpoint. We found the code responsible for LUKS decryption unsurprisingly in [GRUB’s luks.mod module](https://gitlab.com/kalilinux/packages/grub2/-/blob/kali/master/grub-core/disk/luks.c). In the disk partition we examined, there was a binary explicitly compiled containing only the LUKS decryption logic. Examining the disassembly for this binary helped identify the area where we wanted to drop a breakpoint–right before invoking grub_crypto_pbkdf2 (see Figure 2). Luckily for us, the code performed a check for a unique LUKS macro value, LUKS_KEY_ENABLED (0x00AC71F3), right before invoking this decryption, which simplified building a binary search pattern for finding the code at runtime.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20721%20250'%3E%3C/svg%3E)

_Figure 2: Disassembly of the luks.mod file where it invokes grub_crypto_pbkdf2_

## Recovering the LUKS Decryption Keys with Qemu

During our research into this peculiar behavior, we identified a [blog post](https://www.anquanke.com/post/id/266078) written by a user named CataLpa that describes their method of recovering the LUKS keys to decrypt the partitions of the SonicWall NSv appliance. At a high level, this method involves running the appliance in Qemu and leveraging GDB to set a breakpoint on the grub_crypto_pbkdfv2 function that the LUKS module invokes. Below is the qemu-system-x86_64 command we leveraged to run the SonicWall NSv appliance in Qemu which instructed Qemu to start with a GDB debugging listener enabled:
  
  
  qemu-system-x86_64 
  
    -smp 2 
  
    -m 4G 
  
    -usb 
  
    -device usb-tablet 
  
    -vga virtio 
  
    -display default,show-cursor=on 
  
    -device virtio-net,netdev=vmnic -netdev user,id=vmnic 
  
    -device ich9-intel-hda 
  
    -drive file=sonciwall-snapshot.qcow2,if=virtio 
  
    -bios ./OVMF.fd 
  
    -s -S

After configuring GDB with Qemu we followed the steps from the previously mentioned blog post to boot into the Grub recovery shell and load the luks, crypto, gcry_rajndael, and gcry_sha256 modules with the recovery shell. However, we performed a slightly different step after performing these actions. Instead of searching for the “Trying keyslot %dn” string in memory as they did in the post, we searched for a block of code we identified within the luks_recover_key function itself. This signature is based on the LUKS_KEY_ENABLED constant shown in Figure 2 of the previous section “Attempting to Jailbreak the Appliance” _._ We searched for this block of code using the following GDB command:
  
  
  find /b 0xB0000000, 0xD0000000, 0x41, 0x81, 0x7C, 0x24, 0xF8, 0x00, 0xAC, 0x71, 0xF3, 0x0F, 0x85, 0xE0, 0x02, 0x00, 0x00

The result of that command’s execution is the following snippet:
  
  
  (gdb) find /b 0xB0000000, 0xD0000000, 0x41, 0x81, 0x7C, 0x24, 0xF8, 0x00, 0xAC, 0x71, 0xF3, 0x0F, 0x85, 0xE0, 0x02, 0x00, 0x00
  
  0xbbe7d0f9
  
  0xbe0ef6d1
  
  0xbe34f6e9
  
  warning: Unable to access 16000 bytes of target memory at 0xc07fe0f8, halting search.
  
  3 patterns found.
  
  (gdb)

### Identifying the Correct Address

At this point, we had three potential addresses for the luks_recover_key function, which were 0xBBE7D0F9, 0xBE0EF6D1, and 0xBE34F6E9. However, after disassembling the code at all three of these addresses, it became obvious that 0xBBE7D0F9 was the correct address as this was the only code block with the proper relocations applied to the code (see Figure 3).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20729'%3E%3C/svg%3E)

_Figure 3: An analysis of the disassembly of each of the three discovered addresses indicated that the first address_ 0xBBE7D0F9 was the correct address of the luks_recover_key function.

At this point we analyzed the disassembly of the luks_recover_key function and identified the address of the grub_crypto_pbkdf2 function as being 0xBBE88320 (See Figure 4). We placed a breakpoint on the grub_crypto_pbkdf2 function and then triggered decryption of the LUKS encrypted partitions using the grub recovery shell with the cryptomount command.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20744%20855'%3E%3C/svg%3E)

_Figure 4: We then analyzed the luks_recover_key function and identified the address of the grub_crypto_pbkdf2 function at 0xBBE7D162, which moves the address of the grub_crypto_pbkdf2 function into the rax register (0xBBE88320)._

### Recovering a Passed Key

We hit our breakpoint on the grub_crypto_pbkdf2 function and we examined the current register state to obtain the arguments passed to the function. After observing that a 52 byte key was passed to the function to calculate the LUKS decryption key for the partition (See Figure 5), we recovered the passed key by leveraging the RSI register that pointed to the key in memory (See Figure 6).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20774%20516'%3E%3C/svg%3E)

_Figure 5: We observed that the passphrase size (rdx) was 52 bytes with a pointer to the passphrase passed to the grub_crypto_pbkdf2 function via the RSI register._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20797%20239'%3E%3C/svg%3E)

_Figure 6: A recovered LUKS passphrase passed to the grub_crypto_pbkdf2 function to derive a decryption key to decrypt a LUKS partition used by SonicWall NSv._

## Analyzing the SonicWall NSv GRUB LUKS Module

While we technically had the keys necessary to decrypt the partitions, we still didn’t have an answer to the mystery of WHERE these keys were coming from. Binary searches of the entire unencrypted partition didn’t match any files. How was GRUB just pulling these keys out of nowhere? We’d been nerd-sniped (see Figure 7).

![](https://www.praetorian.com/wp-content/uploads/2024/06/SonicWall-LUKS-7.png)

_Figure 7: At this point, even though we had recovered the LUKS decryption keys, we were deeply curious as to the origin of the LUKS decryption keys and how they were calculated. Credit:[xkcd](https://xkcd.com/356/#:~:text=Hat%20Guy%3A%20There's%20a%20certain,a%20new%20sport%3A%20nerd%20sniping.)_

### Decompiling the Code

Clearly something was not “default” about the LUKS implementation this GRUB bootloader was using. Going back into IDA we looked for logic that didn’t seem to match the source code we’d found online for the module. While most of the code was identical, there was an additional chunk of decompilation which didn’t seem to map back to the source, which we have highlighted in Figure 8.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20797%20630'%3E%3C/svg%3E)

_Figure 8: This code didn’t have anything matching in the original LUKS module source code_

The code was nearly identical, however, there was an additional chunk of decompiled code that didn’t seem to map back to the original GRUB source code. Decompiled code is unreliable ground truth so this wasn’t unusual to see, but what immediately set off alarm bells was the use of the XOR operator on line 138. The original source code never performed an XOR operation, and XOR outside of traditional cryptography implementations is also the hallmark of someone attempting to roll their own obfuscation.

While clearly something was amiss in this part of the code, we needed to clean the decompiled code to get a better understanding of what was happening. We knew that the memory we were iterating over derived from the LUKS partition header (see Figure 9), but we were unsure how this played into the key derivation.

_ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20902'%3E%3C/svg%3E) _

_Figure 9: The format of the LUKS partition header_

### Cleaning the Code

Fortunately the LUKS header had a [formal specification](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/LUKS-standard/on-disk-format.pdf) which made it straightforward to enter into IDA’s struct window, as in Figure 10. While the UI for defining structs in IDA can be a pain to use, it was crucial for forcing the decompiler into a much more readable format.

_ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20758%20687'%3E%3C/svg%3E) _

_Figure 10: The LUKS_HEADER manually entered into an IDA struct, struct handling in IDA is a great source of joy and pain for reverse engineers_

After defining the struct, and telling IDA’s decompiler to use it by defining the appropriate stack variables as a LUKS_HEADER, we had much cleaner code to examine (see Figure 11).

_![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20805%20357'%3E%3C/svg%3E)_

_Figure 11: A decompilation of the key derivation algorithm used to generate the LUKS decryption key we identified through reverse engineering._

### Eureka!

We now understand that the developers had modified the LUKS module to read the LUKS header of the partition it was decrypting and then derive a decryption passphrase (see Figure 12). The derivation function was to concatenate mk-digest and mk-digest-salt from the header, and then XOR each byte against its “mirrored” position on the opposite end of the byte array. For example, the first byte would be XORed against the last byte, the second byte would be XORed against the second to last byte, and so on. For unknown reasons, they also made sure that each key byte value was always at least 0x20 with an additional check.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20733%20396'%3E%3C/svg%3E)

_Figure 12: A custom implementation of the key derivation algorithm that the SonicWall NSv appliance’s modified LUKS encryption module used.___

We compiled the above code, ran it against the headers for every encrypted partition, and were able to derive each LUKS decryption key (see Figure 13). Interestingly as a side effect of the obfuscation mechanism, every encryption key is a palindrome.

_![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20537'%3E%3C/svg%3E)_

_Figure 13: An analysis of the four extracted LUKS decryption keys indicated that all of the extracted keys exactly mirrored each other between the first and last bytes._

## (Ab)Using the Keys

Now that we had the decryption keys, we were able to mount each drive by running the following commands:
  
  
  cat p9-luks.key | sudo cryptsetup luksOpen /dev/nvme1n1p9 decryptedp9
  
  mkdir /tmp/p9
  
  sudo mount /dev/mapper/decryptedp9 /tmp/p9

This decrypted the ROOT partition and mounted it to /tmp/p9, where we could browse around the file system and modify it as desired.

For Sonicwall appliances, a default management user normally runs a very restricted shell. We wanted our full root shell, so we modified the partition’s /etc/passwd at /tmp/p9/etc/passwd to have the management user access /bin/bash as its default shell.

We rebooted the NSv appliance and then were able to ssh into the NSv as the management user while receiving a bash shell. The moment we tried to poke around, however, we received permission denied messages. Management didn’t have root access or sudo privileges. With raw file system access though, this was easy to fix. We logged in as management, copied the local /bin/bash file to /home/management/localbash, and then stopped the machine. Next we re-mounted the ROOT partition using the previously specified commands and ran the following command:
  
  
  sudo chown root:root /tmp/p9/home/management/localbash
  
  sudo chmod u+s /tmp/p9/home/management/localbash

After rebooting the NSv appliance once more we could login and run ./localbash -p (with -p added to make sure we didn’t drop our root privileges), after which we enjoyed full root access to the NSv appliance as Figure 14 shows.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20206'%3E%3C/svg%3E)

_Figure 14: The final fruits of our reverse engineering labor – unrestricted root access to the NSv appliance_

## Conclusion

Thanks to some overkill reverse engineering, we now have a general solution to decrypt LUKS partitions for all SonicWall NSv appliances that use this custom GRUB module. The decryption tool is available at [sonicwall-nsv-decrypter](https://github.com/praetorian-inc/sonicwall-nsv-decrypter).

While we could have used the keys we obtained from debugging, taking this path helped us better understand the LUKS decryption process and will help us identify other “bespoke” key derivation algorithms in the future. Also we REALLY wanted to know where that key was coming from and now we can sleep better at night.

## About the Authors

![Adam Crosser](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Adam Crosser](https://www.praetorian.com/author/adam-crosser/)

Adam is an operator on the red team at Praetorian. He is currently focused on conducting red team operations and capabilities development.

[ ](https://www.linkedin.com/in/adam-crosser-366263265)

![Michael Weber](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Michael Weber](https://www.praetorian.com/author/michael-weber/)

Michael has worked in security as a malware reverse engineer, penetration tester, and offensive security developer for over a decade.

## Catch the Latest

Catch our latest exploits, news, articles, and events.

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 19, 2026

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

## [GhostPack Necromancy: Reforging C# Tools with WasmForge](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[ Read More ](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 17, 2026

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

## [FreeBSoD: Leveraging Language Models to Find and Exploit Kernel Bugs (Part 1 of 2)](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[ Read More ](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

  * [Uncategorized](https://www.praetorian.com/category/uncategorized/)

  * June 16, 2026

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## [Sharing is Caring: SMB Secret Scanning with Sulla](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

[ Read More ](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## Ready to Discuss Your Next Continuous Threat Exposure Management Initiative?

Praetorian’s Offense Security Experts are Ready to Answer Your Questions

[ Get Started ](/contact-us/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

##### [Praetorian Guard Platform](https://www.praetorian.com/guard)

  * [ Continuous Threat Exposure Management ](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [ Attack Surface Management ](https://www.praetorian.com/guard/attack-surface-management/)
  * [ Vulnerability Management ](/chariot/vulnerability-management/)
  * [ Cyber Threat Intelligence ](/chariot/threat-intelligence/)
  * [ Continuous Penetration Testing ](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [ Breach and Attack Simulation ](https://www.praetorian.com/guard/breach-attack-simulation/)

##### Professional Services

  * [ AI/ML Penetration Testing ](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [ Application Penetration Testing ](/services/application-penetration-testing/)
  * [ Assumed Breached Exercise ](/services/assumed-breached-exercise/)
  * [ Attack Path Mapping ](https://www.praetorian.com/resources/attack-path-mapping/)
  * [ Automotive Penetration Testing ](/services/automotive-penetration-testing/#)
  * [ CI/CD Security Engagement ](/services/ci-cd-security-engagement/)
  * [ Cloud Penetration Testing ](/services/cloud-penetration-testing/)
  * [ IoT Penetration Testing ](/services/iot-penetration-testing/)
  * [ Network Penetration Testing ](/services/network-penetration-testing/)
  * [ NIST CSF Benchmark ](/services/nist-csf-benchmark/)
  * [ Purple Team ](/services/purple-team/)
  * [ Red Team ](/services/red-team/)

##### Use Cases

  * [ Bug Bounty Cost Reduction ](/services/bug-bounty-cost-reduction/)
  * [ FDA Testing and Monitoring ](/services/fda-testing-monitoring/)
  * [ Mergers and Acquisitions ](/services/mergers-acquisitions/)
  * [ Ransomware Prevention ](/services/ransomware-prevention/)
  * [ Rogue IT Identification ](/services/rogue-it-identification/)
  * [ Tool and Vendor Consolidation ](/services/tool-vendor-consolidation/)
  * [ Vendor Risk Management ](https://www.praetorian.com/services/vendor-risk-management/)

##### Company

  * [ About Us ](https://www.praetorian.com/about-us/)
  * [ Leadership Team ](https://www.praetorian.com/leadership-team/)
  * [ Press Releases ](/news/press-release/)
  * [ In the News ](/news/news)
  * [ Contact Us ](https://www.praetorian.com/contact-us/)
  * [ Resource Library ](https://www.praetorian.com/resources/)
  * [ Security Blog ](/blog/)
  * [ People Ops Blog ](/people-ops/)
  * [ Careers ](https://www.praetorian.com/careers/)
  * [ Culture ](https://www.praetorian.com/work-at-praetorian/)
  * [ Survival Kit ](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)

### Subscribe to our Newsletter

Catch our latest exploits, news, articles, and events.

[Privacy Policy](/privacy-policy/) | [Responsible Disclosure Policy](/responsible-disclosure-policy/) | [Terms of Service](/terms-of-service/) | [Terms and Conditions](/terms/)

Copyright © 2025. All Rights Reserved.

[ Linkedin-in ](https://www.linkedin.com/company/praetorian/) [ X-twitter ](https://twitter.com/praetorianlabs) [ Facebook-f ](https://www.facebook.com/praetorianlabs) [ Github ](https://github.com/praetorian-inc) [ Youtube ](https://www.youtube.com/user/PraetorianLabs)
