---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-14_neighbourhood-watch-hikvision-intercom-eavesdropping.md
original_filename: 2023-09-14_neighbourhood-watch-hikvision-intercom-eavesdropping.md
title: Neighbourhood Watch - Hikvision Intercom Eavesdropping
category: documents
detected_topics:
- rate-limit
- supply-chain
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- rate-limit
- supply-chain
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: a5326ba6d079d2f19b4bd9ff473c6d958b429a47b8911e5ead51380e2a30dcf0
text_sha256: 9c257d0a19bd99dab553eb0573d66226d4e0f32ed44f8b0ac70bf8af4ed1c13b
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Neighbourhood Watch - Hikvision Intercom Eavesdropping

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-14_neighbourhood-watch-hikvision-intercom-eavesdropping.md
- Source Type: markdown
- Detected Topics: rate-limit, supply-chain, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `a5326ba6d079d2f19b4bd9ff473c6d958b429a47b8911e5ead51380e2a30dcf0`
- Text SHA256: `9c257d0a19bd99dab553eb0573d66226d4e0f32ed44f8b0ac70bf8af4ed1c13b`


## Content

---
title: "Neighbourhood Watch - Hikvision Intercom Eavesdropping"
page_title: "Skylight Cyber | Neighbourhood Watch - Hikvision Intercom Eavesdropping"
url: "https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/"
final_url: "https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/"
authors: ["Peter Szot"]
programs: ["Hikvision"]
bugs: ["IoT", "UDP", "SIP", "DoS", "Authentication bypass", "Bruteforce", "Restricted shell escape"]
publication_date: "2023-09-14"
added_date: "2023-09-22"
source: "pentester.land/writeups.json"
original_index: 778
---

[![](/images/logo.svg)](/)

[Home](/)

[About](/about-us/ "About")

[Services](/services/ "Services")

[Blog](/blog/ "Blog")

[Careers](/careers/ "Careers")

[Contact Us](/contact-us/ "Contact Us")

# Neighbourhood Watch - Hikvision Intercom Eavesdropping

14 September 2023

![clock-image](/images/clock-eight.svg)

15

minute read

by

Peter Szot

# TL;DR

Ever wanted to get back at that nosy neighbour or become the boss of your neighbourhood gossip game? We have your back! A series of vulnerabilities we discovered in Hikvision intercoms allows you to gain full control of devices on the same network, open the microphone and turn your neighbour’s intercom into a spying device. 

[![soundwave.png](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/soundwave.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/soundwave.png)

# Introduction

Have you ever answered your ringing intercom and thought, “I wonder if this thing can be hacked?”. No? Just me? Well, if you answered yes, look no further, because it can, and we’ve done most of the legwork for you. 

Physical security devices, i.e., IP cameras/intercoms/etc, are an interesting target since the security of these devices often relies on them being inaccessible e.g., being embedded into a wall, and/or being part of an air-gapped network. This is just a nice way to say that the security of the communication stack is often treated as an afterthought. However, the impact can be quite interesting, as these devices serve a security function that can be a double-edged sword.

We’ve focused on attacks which are possible given just network-level access to an intercom, as this level of access is quite trivial to achieve. Hikvision devices were chosen specifically, partly because it’s what I already had access to in my own apartment, and because they are one of the biggest players in the security-product sector. 

# Targets

All testing was conducted on the following 2 intercom products:

  * DS-KH6210-L - firmware version: V1.5.0build 181114
  * DS-KH6320-WTE1 - firmware version: V2.1.46build 220607

  
[![DS-KH6320-WTE1](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/device.jpg)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/device.jpg) DS-KH6320-WTE1

# Test Environment Setup and Background

Both intercom products we looked at were PoE capable and could be powered by a PoE enabled switch (802.3af). The switch we used supplied automatic sensing on PoE enabled ports, however the KH6210 did not support this, necessitating the use of a PoE adapter (e.g., Ubiquiti Instant 802.3AF Outdoor Gigabit). 

Once the devices could be successfully powered up while connected to the switch, port mirroring was configured to allow us to capture all traffic entering and leaving the device. One of the devices was tested on-premises inside an actual apartment building network so that it was able to communicate with the door controller, cameras, SIP servers, and other intercoms.

# Denial of Sleep

Intercoms on a network configured to communicate with a SIP server will periodically register their existence with the controller. They also listen on port 5060/udp to receive incoming calls from the primary intercom/door controller. Most notably, the traffic is neither encrypted nor authenticated in any way.

An attacker able to connect to an intercom on port 5060/UDP (trivial with physical access) can send an SIP “INVITE” message to the device, causing it to start ringing. This can be abused to cause nuisance, or act as a constant denial of service, preventing residents from accepting legitimate calls. 

Furthermore, it is not possible to prevent or otherwise block the spam call on an affected intercom, without either turning it off, or configuring do-not-disturb hours. 

Talk about elevating your ding dong ditch game…

The following python code can be used to execute this attack, connecting to an intercom with IP address 192.0.0.30 and sending the SIP invitation. 

<https://github.com/skylightcyber/CVE-2023-28810/blob/0a827dd0c94fa94e9ecc965b43026fb22a6eb08d/SIP-ghost-caller.py>

# Putting the B in Bypass

Hikvision is kind enough to offer a suite of tools for performing remote management of their devices for free, the most comprehensive of which is [IVMS-4200](https://www.hikvision.com/au-en/support/download/software/ivms4200-series/). The tool can communicate with the intercoms over Hikvision’s proprietary “camera management” protocol (port 8000/tcp) using logic implemented in the “HCNetSDK.dll” library. 

Usage of the software revealed that the devices also listen for XML messages on port 32070/UDP on the IPv4 multicast address 239.255.255.250. These messages are primarily used as a means of device discovery enabling the IVMS software to identify Hikvision devices on the local network. This is done via the _inquiry_ message, per the following example:
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <Probe>
  <Uuid>7621A503-49E6-4FBA-B3F8-CBE1F18E55F4</Uuid>
  <Types>inquiry</Types>
  </Probe>

Each device will respond with the following message, broadcasting some basic diagnostic information:
  
  
  <?xml version="1.0" encoding="UTF-8" ?>
  <ProbeMatch>
  <Uuid>7621A503-49E6-4FBA-B3F8-CBE1F18E55F4</Uuid>
  <Types>inquiry</Types>
  <DeviceType>57397</DeviceType>
  <DeviceDescription>DS-KH6210-L</DeviceDescription>
  <DeviceSN>DS-KH6210-serial_number</DeviceSN>
  <CommandPort>8000</CommandPort>
  <HttpPort>80</HttpPort>
  <MAC>AA-BB-CC-AA-BB-CC</MAC>
  <IPv4Address>192.0.0.60</IPv4Address>
  <IPv4SubnetMask>255.255.0.0</IPv4SubnetMask>
  <IPv4Gateway>192.0.0.1</IPv4Gateway>
  <DHCP>false</DHCP>
  <AnalogChannelNum>1</AnalogChannelNum>
  <DigitalChannelNum>0</DigitalChannelNum>
  <SoftwareVersion>V1.5.0build 181114</SoftwareVersion>
  <DSPVersion>V1.0, build 180613</DSPVersion>
  <BootTime>2023-01-16 11:06:06</BootTime>
  <OEMInfo>N/A</OEMInfo>
  <Activated>true</Activated>
  <PasswordResetAbility>true</PasswordResetAbility>
  <DeviceLock>true</DeviceLock>
  </ProbeMatch>

Further investigation into supported message types identified the _update_ command, which can be issued to modify various device network settings remotely. The body of the message is as follows:
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <Probe>
  <Uuid>44037D7F-7D48-4DB0-8893-05705C4AE965</Uuid>
  <Types>update</Types>
  <PWErrorParse>true</PWErrorParse>
  <MAC>18-68-cb-aa-bb-cc</MAC>
  <Password>X03MO1qnZdYdgyfeuILPmQ==</Password>
  <IPv4Address>192.0.0.60</IPv4Address>
  <CommandPort>8000</CommandPort>
  <IPv4SubnetMask>255.255.0.0</IPv4SubnetMask>
  <IPv4Gateway>192.0.0.1</IPv4Gateway>
  <IPv6Address>::</IPv6Address>
  <IPv6Gateway>::</IPv6Gateway>
  <IPv6MaskLen>0</IPv6MaskLen>
  <DHCP>false</DHCP>
  <HttpPort>80</HttpPort>
  </Probe>

This is an authenticated command which requires the admin password to the target intercom. It’s submitted in the _Password_ field which contains the MD5 hash of the password, but in base64 encoding instead of hex. While this request is multicast to all devices in the network, only the one with the matching MAC address will process it. This device will verify the supplied password matches its own and will then apply the provided network configuration. If an incorrect password is specified, the device returns an error and decreases an account lockout counter. After 6 failed attempts, the device will stop accepting update requests and begin a 30-minute lockout timer, though resetting/power-cycling the device will clear this state.

To bypass this well-designed security mechanism, we had to come up with something truly exceptional and complex, requiring advanced AI, super computers and never seen before algorithms – omitting the password field completely. Yep, no password, no problem! The following message demonstrates this “authentication bypass”:
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <Probe>
  <Uuid>44037D7F-7D48-4DB0-8893-05705C4AE965</Uuid>
  <Types>update</Types>
  <PWErrorParse>true</PWErrorParse>
  <MAC>18-68-cb-aa-bb-cc</MAC>
  <IPv4Address>192.0.0.60</IPv4Address>
  <CommandPort>8000</CommandPort>
  <IPv4SubnetMask>255.255.0.0</IPv4SubnetMask>
  <IPv4Gateway>192.0.0.1</IPv4Gateway>
  <IPv6Address>::</IPv6Address>
  <IPv6Gateway>::</IPv6Gateway>
  <IPv6MaskLen>0</IPv6MaskLen>
  <DHCP>false</DHCP>
  <HttpPort>80</HttpPort>
  </Probe>

The following proof-of-concept script can be used to modify the network configuration of an arbitrary Hikvision device. Note that modifying the config of devices in an arbitrary way, or introducing IP address conflicts into an intercom network may cause them to stop operating as expected. Use it at your own peril!  
<https://github.com/skylightcyber/CVE-2023-28810/blob/0a827dd0c94fa94e9ecc965b43026fb22a6eb08d/udp-config-changer.py>

# Brute-forcing – Achievement Unlocked

The discovery of the UDP authentication bypass vulnerability led to an interesting revelation: the lockout attempt counter resets back to 6 on “successful” authentication. We can therefore guess 5 different passwords for the device by issuing update requests including the password field, then on the 6th request, drop the field and complete authentication without a password. In this way we can carry out an online brute-force of the admin password, without worrying about getting locked out and waiting a long time or resetting the device.

As a proof-of-concept we’ve provided the following script to guess the password of a Hikvision intercom based on a supplied word list:

<https://github.com/skylightcyber/CVE-2023-28810/blob/0a827dd0c94fa94e9ecc965b43026fb22a6eb08d/udp-password-brute.py>

# “Protected” Shell

Assuming you’ve managed to successfully brute force the admin password for your Hikvision intercom and are wondering what to do next (or even if you haven’t), the following section is for you.

Using the device’s admin password, we can now leverage the Hikvision IVMS software to enable SSH on the device:

  
[![Using Hikvision IVMS to configure the device and enable SSH](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/enable_ssh.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/enable_ssh.png) Using Hikvision IVMS to configure the device and enable SSH

Once it’s enabled, connect to it as root using the admin password for the device. This will drop us into Hikvision’s PSH or “protected” shell:

  
[![Connecting to the device via SSH as the root user.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/restricted_shell.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/restricted_shell.png) Connecting to the device via SSH as the root user.

The help command shows us the limited set of commands we can execute. Some of which do not appear to work on every type of device:

  
[![Not all commands are available on every type of device.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/sandbox_command.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/sandbox_command.png) Not all commands are available on every type of device.

From the publicly available firmware for our intercom, we were able to extract the PSH binary and perform some static analysis on it using everyone’s favourite NSA totally-not-spyware reverse engineering tool (Ghidra). The following screenshot shows a snippet of the decompiled function which handles all user input passed into the binary:

  
[![Snippet of the decompilation of the main user-input processing loop](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/shell_user_input_processing_loop.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/shell_user_input_processing_loop.png) Snippet of the decompilation of the main user-input processing loop

From this we can infer that any user input provided to the function, assuming it matches one of the supported commands (pictured above), is passed directly through to a system call unless it is the literal string “Debug”. This is a special command handled by the psh binary which then prompts the user with a challenge-response token, expecting an encrypted blob which is verified using an embedded Hikvision public key (stored in /etc/psh_rsa.conf). Since breaking asymmetric encryption is no trivial feat, we decided to explore alternative avenues.

Commands are able to take arguments, but some filtering is performed on the input to check for special characters, as seen below:

  
[![Decompilation of the input sanitization function.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/input-sanitization.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/input-sanitization.png) Decompilation of the input sanitization function.

If the user input contains any one of these characters, the application prints an error and returns.

We did note that the ‘\n’ or newline character is not specifically prohibited. But supplying it through the prompt in a fashion like “sandbox\necho aaa” did not yield the expected result – the escape sequence was simply being interpreted as a literal ‘backslash n’ and any multi-line inputs were being tokenised and correctly parsed line-by-line.  
Instead, we switched to piping a string containing the newline character directly via SSH i.e.:
  
  
  echo -n 'sandbox\nid' | ssh root@device

And voila! It works:

  
[![Attempting to execute a pair of commands separated via a new-line.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/escape_restricted_shell.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/escape_restricted_shell.png) Attempting to execute a pair of commands separated via a new-line.

But then again, so does this:

  
[![Directly executing an arbitrary command via SSH through STDIN.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/directly_executing_arbitrary_commands.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/directly_executing_arbitrary_commands.png) Directly executing an arbitrary command via SSH through STDIN.

So, what is really going on here? This is clearly not an issue with PSH inappropriately parsing STDIN, but rather an unexpected behaviour of the dropbear SSH server executing commands via sh instead of psh when passed via stdin.

If we look at the shell configuration of the root user on the device (after breaking out or from analysing the firmware), we see the following:

  
[![Snippet of the device /etc/passwd showing the root user's shell config.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/shell_config.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/shell_config.png) Snippet of the device /etc/passwd showing the root user's shell config.

The shell is clearly set to /bin/sh (which is just a symlink to the busybox binary on the device). Why are we still executing psh on login? The answer lies in the /etc/profile file:

  
[![Contents of the system profile file showing executing of psh.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/shell_profile.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/shell_profile.png) Contents of the system profile file showing executing of psh.

The last line of the file executes the /bin/psh binary after it is processed.  
Breaking down the login flow:

  1. User authenticates to the device
  2. SSH Server executes the user’s passwd-defined shell
  3. sh executes the system profile file (/etc/profile)
  4. User meets the psh prompt

When passing input to the device via standard input, the following happens:

  1. User authenticates to the device
  2. SSH Server executes the user’s passwd-defined shell
  3. STDIN is passed to the shell (/bin/sh) and executed

Linux sysadmins can attest that **/etc/profile** is not a good place to change a user’s login shell.

Bypassing psh on the device can therefore be done in many ways, replacing the psh binary with ash is one such example:

  
[![Bypassing the restricted shell by overwriting it with /bin/ash.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/bypass_restricted_shell.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/bypass_restricted_shell.png) Bypassing the restricted shell by overwriting it with /bin/ash.

The next time the root user logs in, they have access to an unrestricted shell:

  
[![/bin/ash executing instead of /bin/psh](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/unrestricted_shell.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/unrestricted_shell.png) /bin/ash executing instead of /bin/psh

# Bonus Round – Decrypting Config

Now that we have unrestricted access to the device, we can poke around in the filesystem to try to figure out more about how it works. Of particular interest is the device configuration, which when exported from the device via IVMS, produces a 256kb file which looks a little like this:

  
[![Hexdump view of the exported device configuration file.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/hexdump_device_config.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/hexdump_device_config.png) Hexdump view of the exported device configuration file.

Ignoring the very peculiar file size for now, we can compare it against the same file extracted directly from the device via our shell:

  
[![Hexdump view of the same configuration file pulled from the device.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/hexdump_device_config2.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/hexdump_device_config2.png) Hexdump view of the same configuration file pulled from the device.

A clear and interesting pattern emerges.

If we XOR the two files together we can recover the ‘encryption’ key ‘20DC1E0C’ which conveniently enough is the first 4 bytes of the encrypted file (1st screenshot). However, there are still no plaintext strings visible in the second file, indicating that there is a second layer of encryption in use - which is also a short XOR key due to the observable lack of entropy in the file and the repeated occurrences of the 4-letter string ‘SWKH’.

If we convert this string into another XOR key (‘53574b48’) and apply it to the file again (treating it as Big Endian or reversing the byte order to ‘484b5753’):

  
[![Result of successfully decrypting the file and reading its contents.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/decrypted_config.png)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/decrypted_config.png) Result of successfully decrypting the file and reading its contents.

We now have a fully decrypted device config file!

If you want to modify the file, simply re-encrypt it, applying both XOR keys in the reverse order. The code to perform this has been left as an exercise for the reader.

# Nosy Neighbours

Just to quickly recap – we showed how, by merely having network level access, we can deny our neighbours of sleep, brute-force our way to an admin password and break out of the not-so-protected shell to have full, unrestricted control of another device. But as much as we like the electric feeling of power that comes with admin level access to a device, what does that actually enable us to do?

As you may have guessed from the headline of this blog post, the ultimate reward is having the ability to covertly open the microphone on a device, turning it into a privacy nightmare. Is it theoretically possible? Of course, that is an innate ability of the device. Did we prove that it is indeed possible by going ahead and creating a proof of concept? Of course we did. Are we going to share it with you? Not a chance. 

The problem is that as much as we would like to believe that this blog post will be the talk of the day for every Hikvision installer out there, there’s a very slight possibility that it won’t. In that case, and given that building security systems are usually not connected to and updated from the Internet automatically, it will take a lot of time to patch, leaving too many people exposed. 

  
[![Definitely not us eavesdropping on the neighbours.](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/nosy_neighboor.jpg)](https://skylightcyber.com/2023/09/14/neighbourhood-watch-hikvision-intercom-eavesdropping/nosy_neighboor.jpg) Definitely not us eavesdropping on the neighbours.

# Conclusion

There is a lot of interesting (and vulnerable!) hardware that we interact with in our everyday lives without much second thought. Unfortunately, despite the vendors of these appliances releasing relatively frequent security updates, we often find that they go without patching for the majority, if not all, of their lifespans. 

In most cases, these devices are often found in air-gapped networks, disconnected from the internet. It is also often difficult to for users to update their devices manually since they are often locked with a unique admin password prior to their deployment. If you, as reader of this blog, find your intercom ringing at strange times of the night, consider pushing your building manager to update the intercoms in your building!

# Vendor Response

Hikvision has been prompt in addressing our security disclosure, and at the time of this blog release had issued a patch for the majority of concerns we identified. Their announcement can be found at:  
<https://www.hikvision.com/en/support/cybersecurity/security-advisory/security-vulnerability-in-some-hikvision-access-control-intercom/>

A CVE for the unauthenticated UDP protocol attack was also raised:  
<https://nvd.nist.gov/vuln/detail/CVE-2023-28810>

# Timeline

  * 3 January 2023
  * Skylight begins security testing of Hikvision intercom products with latest available firmware versions
  * 15 March 2023
  * Report detailing research findings provided to Hikvision security (HSRC)
  * HSRC acknowledges receipt
  * 29 May 2023
  * Update from HSRC on submission of CVE
  * Remediation for SIP protocol exploits fixed in Firmware version 2.2.8_build230219 (released 2023-03-02)
  * 14 June 2023
  * HSRC releases security advisory for latest firmware patch (See vendor response)
  * 14 September 2023
  * Skylight blog post published

share

![](/images/skylight-logo-big.svg)

![](/images/logomark.svg)

Level 30, 201 Elizabeth St

Sydney

NSW 2000

Australia

## SKYLIGHT CYBER

[ Home ![](/images/vector_7.svg) ](/) [ About ![](/images/vector_7.svg) ](/about-us/) [ Services ![](/images/vector_7.svg) ](/services/) [ Blog ![](/images/vector_7.svg) ](/blog/) [ Careers ![](/images/vector_7.svg) ](/careers/) [ Contact Us ![](/images/vector_7.svg) ](/contact-us/)

## find us

[ ](https://twitter.com/SkylightCyber) [ ](https://www.linkedin.com/company/skylight-cyber-security/)

Copyright © 2025 Skylight Cyber All rights reserved.

[ Privacy Policy ](/privacy-policy/)
