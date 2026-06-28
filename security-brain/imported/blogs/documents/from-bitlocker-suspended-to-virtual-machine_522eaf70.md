---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-21_from-bitlocker-suspended-to-virtual-machine.md
original_filename: 2023-04-21_from-bitlocker-suspended-to-virtual-machine.md
title: From BitLocker-Suspended to Virtual Machine
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 522eaf7080822405524df4fb2dc653c260bfe085c9a63867f7489f36be787d0a
text_sha256: 7fbedc06591c7b8a50af73168391737e2fd947b16b578e68815eeef503184d24
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# From BitLocker-Suspended to Virtual Machine

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-21_from-bitlocker-suspended-to-virtual-machine.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `522eaf7080822405524df4fb2dc653c260bfe085c9a63867f7489f36be787d0a`
- Text SHA256: `7fbedc06591c7b8a50af73168391737e2fd947b16b578e68815eeef503184d24`


## Content

---
title: "From BitLocker-Suspended to Virtual Machine"
page_title: "SensePost | From BitLocker-Suspended to Virtual Machine"
url: "https://sensepost.com/blog/2023/from-bitlocker-suspended-to-virtual-machine/"
final_url: "https://sensepost.com/blog/2023/from-bitlocker-suspended-to-virtual-machine/"
authors: ["Reino Mostert"]
bugs: ["Internal pentest"]
publication_date: "2023-04-21"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1234
---

On a recent red-team I was given a client laptop from which I was expected to simulate an insider-threat/employee laptop compromise scenario over their VPN. 

I was given a normal employee user account and did **not** have local administrator privileges. The laptop itself was riddled with security products and snitchware, threatening to report back every action taken on the system to the SOC/SIEM. My first objective was to obtain local administrative access, so that I could disable these security products. 

After I manually enumerated the system’s setup, I found that while **_BitLocker_** was configured, it was in a **_Suspended_** state. 

I didn’t really know what this meant, and initially ignored it for far more interesting rabbit holes.

When I finally started looking into the **_Bitlocker_** configuration properly, and what the **_Suspended_** state meant, I found [this](https://learn.microsoft.com/en-us/powershell/module/bitlocker/suspend-bitlocker?view=windowsserver2022-ps) description from Microsoft:

[![](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/ed6deb79d8e07995d0f9e1ad14a884f2.png)](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/ed6deb79d8e07995d0f9e1ad14a884f2.png)

Basically, this means that when **_BitLocker_** is in a **_Suspended_** state, the drive is encrypted, but the key used to encrypt it is stored on the drive in the clear, and not protected by say a TPM or so forth.

I spent some time searching for where the encryption key would be stored, and found unhelpful posts such as [this one](https://www.reddit.com/r/AskNetsec/comments/8qvwvv/when_suspending_bitlocker_protection_where_is_the/) which didn’t really reveal anything.

I also booted the system into a Linux live system, but it refused to mount the drive.

Finally, I came across the following [blog](https://community.spiceworks.com/how_to/150987-access-windows-partition-in-linux-bitlocker-suspended), which indicated that when **_BitLocker_** is in **_Suspended_** mode, you can simply boot the system using a Windows Setup USB, and then decrypt the drive using this command:
  
  
  manage-bde -off c:

You can check if it is done decrypting using this command:
  
  
  manage-bde -status

Following these steps, I was able to decrypt the hard drive.

[![](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/68ddf7e07bd8df69d22146c7284c1463.jpg)](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/68ddf7e07bd8df69d22146c7284c1463.jpg)

Afterwards, I booted the laptop into a Linux live system and was able to mount the hard drive.

From here, I could do several things, like obtain SYSTEM access by backdooring/replacing an executable that runs as SYSTEM on boot, clear log files, or disable the **_CrowdStrike Falcon Agent EDR_**.

I instead decided to see if I could virtualize the laptop, that is, see if I could run the client laptop as a virtual machine. 

There are a number of benefits to doing this, beyond not having to lug around yet another laptop everywhere. 

First and foremost on the list of benefits, would be the ability to take snapshots and revert back to a prior state. This means that if you break the system while trying to remove its security software, you can just revert back to a previous snapshot and try again. 

It also means you can run malicious software such as **_mimikatz_** , get the output, and then revert back to a prior snapshot to remove all traces of it ever happening. 

Its often also easier to proxy traffic from your system to the client’s VPN via a virtual machine, than via a client laptop, since you don’t need to setup an actual network for the laptop to connect to.

Copy and pasting and taking screenshots also become much easier when using a virtual machine, instead of a laptop. Similarly, capturing a virtual machine’s network traffic is also much easier to do.

To virtualise the laptop, I first ran the **_dd_** command to clone the laptop’s hard drive.
  
  
  dd if=/dev/sda of=laptop.img bs=4096 conv=noerror,sync

After waiting for the command to complete, I used the following command to convert the raw **_dd_** image into a **_VMDK_** image that VirtualBox could understand.
  
  
  VBoxManage convertfromraw laptop.img laptop.vmdk --format VMDK

At this point, I simply created a Windows 10 virtual machine within VirtualBox, and specified **_laptop.vmdk_** as the hard drive. 

Once created, I immediately took a snapshot, to preserve the system’s state.

  
Unfortunately, my initial start up attempts failed. 

To check if the hard drive image was in working order, I booted the virtual machine into a live Linux system and mounted the hard drive. After confirming that everything was in order, I realised that the laptop had UEFI/ Secure Boot enabled. I enabled UEFI on my virtual machine – and viola – it booted.

[![](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/0e70e48d17e5e9d9f57b9b00af3c6131.png)](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/0e70e48d17e5e9d9f57b9b00af3c6131.png) [![](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/bdfbb49f818ebdb94a0f43791ffc821c.png)](/img/pages/blog/2023/from-bitlocker-suspended-to-virtual-machine/bdfbb49f818ebdb94a0f43791ffc821c.png)

To my surprise, the system and user certificates were intact on the virtual machine, allowing me to connect to the WiFi and VPN. I suspect the laptop did not have the TPM configured for storing certificates.

At this point, you could uninstall the security software on the virtual machine and use it to conduct your attacks, while reverting the laptop back to its original state (with BitLocker encrypted and so forth). This would allow you to connect the laptop to the Internet so that the security software/snitchware keeps sending “everything is alright/nothing to report” signals to the SOC/SIEM.

While this setup worked really well for me, there are some things to keep in mind:

  * Virtual machines often boot with their network adapter set to NAT. This means that your virtual machine will likely have Internet access, and the security products will start snitching to the cloud. Until you are able to uninstall the security products, make sure to configure it so that its **_Not Attached,_** to prevent leaks.
  * If you connect to the client network, your virtual machine may automatically update its machine account’s password on the DCs. If you then revert to a prior snapshot, you won’t have the new machine account’s password, effectively removing your system from the domain. To avoid this, make sure to keep all your snapshots so that you can get the new password via Mimikatz, or much easier, configure your machine [not to update its Machine password](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/disable-machine-account-password).

Hope you found this useful!
