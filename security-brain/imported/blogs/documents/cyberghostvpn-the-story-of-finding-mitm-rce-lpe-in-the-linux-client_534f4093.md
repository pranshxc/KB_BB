---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-03_cyberghostvpn-the-story-of-finding-mitm-rce-lpe-in-the-linux-client.md
original_filename: 2023-04-03_cyberghostvpn-the-story-of-finding-mitm-rce-lpe-in-the-linux-client.md
title: CyberGhostVPN - the story of finding MITM, RCE, LPE in the Linux client
category: documents
detected_topics:
- command-injection
- supply-chain
- access-control
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- access-control
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 534f4093b174f93e8de381bd2952a6c9dc6c629c1570266cc26b7770ce8bd74e
text_sha256: 9b7544741c5e9c5048cf69cddc920934f14792c7c9a9d5c207b926c94e33d142
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# CyberGhostVPN - the story of finding MITM, RCE, LPE in the Linux client

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-03_cyberghostvpn-the-story-of-finding-mitm-rce-lpe-in-the-linux-client.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, access-control, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `534f4093b174f93e8de381bd2952a6c9dc6c629c1570266cc26b7770ce8bd74e`
- Text SHA256: `9b7544741c5e9c5048cf69cddc920934f14792c7c9a9d5c207b926c94e33d142`


## Content

---
title: "CyberGhostVPN - the story of finding MITM, RCE, LPE in the Linux client"
page_title: "CyberGhostVPN - the story of finding MITM, RCE, LPE in the Linux client – mmmds's blog"
url: "https://mmmds.pl/cyberghostvpn-mitm-rce-lpe/"
final_url: "https://mmmds.pl/cyberghostvpn-mitm-rce-lpe/"
authors: ["mmmds"]
programs: ["CyberGhost"]
bugs: ["RCE", "MiTM", "Local Privilege Escalation"]
publication_date: "2023-04-03"
added_date: "2023-04-07"
source: "pentester.land/writeups.json"
original_index: 1305
---

# CyberGhostVPN - the story of finding MITM, RCE, LPE in the Linux client

2023-04-03

CyberGhost is a company that provides VPN services to individual users. They support many popular platforms, including Windows, macOS, and Linux. As a Linux user, I was particularly interested in their Linux application and decided to take a closer look at this version of their software. During my analysis, I discovered vulnerabilities that could be exploited to achieve local privilege escalation, remote code execution on the user’s machine, or to control the victim’s network traffic.

This article discloses the vulnerabilities that were present in the CyberGhostVPN Linux 1.3.5 client (and versions below). The latest version of the CyberGhostVPN Linux client is now free from these vulnerabilities.

## Introduction

Before we delve into the details of specific vulnerabilities, it may be useful to briefly explain how the CyberGhost VPN Linux client works.

Every CyberGhost user has an account that is used to log in to the management web panel to manage their subscription and download the client for their desired platform. Once the client is installed, the same account is used to log in to the client.

users can select their desired VPN server by specifying criteria such as service type (OpenVPN or Wireguard), country, city, and server type (traffic, streaming, or torrent). Depending on the service type selected, a different underlying protocol is used, and different paths in the code are executed.

When a user decides to connect to the VPN, two important things happen:

  1. The client sends an authenticated request to the CyberGhost API to fetch the VPN configuration.
  2. The client executes the locally installed VPN software (OpenVPN or Wireguard) with the downloaded configuration.

After these two steps, the user’s machine is connected to one of the CyberGhost VPN servers, and all network traffic is routed through it.

Here’s an example command to connect:
  
  
  $ sudo cyberghostvpn --connect --wireguard --country-code CZ
  Prepare Wireguard connection ...
  Select server ... prague-s402-i11
  Connecting ... 
  VPN connection established.
  

## Dissecting the client

The client is delivered as an ELF executable, so there is no source code available. Fortunately, it is written in Python, which can be decompiled to a form that, in many cases, resembles the original source code.

To accomplish this, a few tools will come in handy:

  * [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) \- to extract Python bytecode (.pyc files) from the binary. When running the tool, it is important to use the same Python version that was used to compile the binary.
  * Decompiler - to translate bytecode into Python code (.pyc to .py). Depending on the Python version, one of these two tools will give better results. \- [uncompyle6](https://pypi.org/project/uncompyle6/) for Python 3.6 and below. \- [decompyle3](https://pypi.org/project/decompyle3) for Python 3.7 and 3.8.

So, how do we determine the Python version?
  
  
  $ strings cyberghostvpn | grep python3
  blibpython3.8.so.1.0
  4libpython3.8.so.1.0
  

With this information, the two steps will give us the code.
  
  
  $ python3.8 ~/pyinstxtractor/pyinstxtractor.py cyberghostvpn
  [+] Processing cyberghostvpn
  [+] Pyinstaller version: 2.1+
  [+] Python version: 3.8
  [+] Length of package: 8255126 bytes
  [+] Found 60 files in CArchive
  [+] Beginning extraction...please standby
  [+] Possible entry point: pyiboot01_bootstrap.pyc
  [+] Possible entry point: pyi_rth_multiprocessing.pyc
  [+] Possible entry point: pyi_rth_certifi.pyc
  [+] Possible entry point: cyberghostvpn.pyc
  [+] Found 470 files in PYZ archive
  [+] Successfully extracted pyinstaller archive: cyberghostvpn
  $ decompyle3 -o out -r cyberghostvpn_extracted 
  

## MITM + RCE

This case is based on two vulnerabilities that can be chained together to achieve code execution by a man-in-the-middle attacker. It has been agreed with the vendor that technical details that could be used to reproduce the exploit will be omitted to protect users who have not yet patched their clients. Despite these limitations, I would like to present a high-level overview of the issues and possible ways of exploitation.

### Issue 1 - Lack of certificate validation.

The client always connects to the API over HTTPS. However, in one specific case, the communication had certificate validation disabled. The affected endpoint happened to be responsible for fetching connection details (hostname, port, key) of a chosen Wireguard server.

This alone is enough to make the client trust an illegitimate server imitating the API. The server could return connection details to a malicious Wireguard server, and the client would connect to it. The user would think that they’re connected to the legitimate CyberGhost Wireguard VPN server, but in fact, their entire traffic would be routed through the malicious server. Such traffic could be analyzed or modified by the threat actor conducting the attack.

The only prerequisite to conduct the attack is to make the client connect to the illegitimate API. This prerequisite requires an attacker to have the ability to successfully conduct a DNS cache poisoning attack, or to perform ARP spoofing if they’re on the same local network. Malicious ISPs and hackers exploiting intermediate network devices or DNS servers are also in a perfect position to redirect the traffic.

### Issue 2 - Command injection

The client parses a response from the endpoint mentioned above and prepares a Wireguard configuration file. The file was generated by issuing a shell command that was filled with connection details without proper sanitization.

In a typical scenario, it’s not a problem because connection details are controlled by CyberGhost and could be trusted. It becomes a problem when we consider the first issue. The illegitimate API instead of providing details of its own Wireguard server could respond with a command injection payload. The payload would be executed on the user’s machine with root privileges. It would give the threat actor full control over the machine.

### Demo

Below I present two videos demonstrating exploitation. A victim on the left, an attacker on the right. For simplicity, the described prerequisite condition is already met and is not covered in the videos.

1\. Exploitation of issue 1. The client communicates with a malicious API and then connects to a malicious VPN server.

2\. Exploitation of issues 1 and 2. The client communicates with a malicious API. The API serves a payload that is executed on the victim’s machine and sets up a reverse shell connection.

## Local Privilege Escalation

In this case, I can provide more technical details. As I didn’t know what to expect from the code, I decided to find out how the client interacts with the operating system. By searching for occurrences of `os.system` and `subprocess.Popen`, I came across a helper function used throughout the entire client.
  
  
  $ grep -C 5 -r 'os\.system\|subprocess\.Popen'
  [...]
  PYZ-00.pyz_extracted/libs/helpers.py:  def executeCommand(self, command: str):
  PYZ-00.pyz_extracted/libs/helpers.py-  try:
  PYZ-00.pyz_extracted/libs/helpers.py-  ps = subprocess.Popen(command, shell=True, stdout=(subprocess.PIPE), stderr=(subprocess.PIPE))
  PYZ-00.pyz_extracted/libs/helpers.py-  output, errors = ps.communicate(timeout=60)
  PYZ-00.pyz_extracted/libs/helpers.py-  except subprocess.TimeoutExpired:
  PYZ-00.pyz_extracted/libs/helpers.py-  ps.kill()
  [...]
  

From there, I easily navigated to the first suspicious line of code in the wireguard-related function:
  
  
  def __addKey(self, publicKey, hostname):
  token = self.getConfig('device', 'token')
  secret = self.getConfig('device', 'secret')
  command = 'curl [...] --user "' + token + ':' + secret + [...] + '" "https://' + hostname + ':1337/addKey"'
  proc = Helpers().executeCommand(command)
  

By looking at the command, it was obvious that if either `token` or `secret` could be controlled, they would allow the injection of additional commands to execute. Both of them are read from a user-specific configuration file: `$HOME/.cyberghost/config.ini`, which is created during installation.
  
  
  $ ls -la ~/.cyberghost/config.ini 
  -rwx------ 1 user user 207 Dec 20 19:03 /home/user/.cyberghost/config.ini
  

A user has permissions to modify the file and inject their own commands. However, what is the point since the code will be executed locally, and the client has to be executed with sudo? In the standard configuration, it doesn’t make much sense, but in the case of non-standard configuration, this injection could be used to locally escalate privileges.

### Demo

Let’s say we have an unprivileged user in our system who should be allowed to initiate a connection to the VPN. Sudo could be configured in a way that the unprivileged user could run only the CyberGhostvpn command with elevated privileges. Attempts to run any other command would be prevented.

In such a scenario, the unprivileged user modifies their configuration file `.cyberghost/config.ini` and puts a payload in `token`, and then tries to initiate a connection. The connection fails because the injected command breaks the original `curl` invocation. But at this point, the “unprivileged” user has root privileges in the system.

## Summary

The vulnerabilities were found in the CyberGhostVPN Linux client version 1.3.5 (and versions below) and were reported to the vendor through the BugCrowd platform. The issues are fixed in the newest version of the client (1.4.1). The client does not have an auto-update feature, so users must manually download and install it.

If, for some reason, it is impossible to update the client, the exploitation of MITM and RCE issues could be mitigated by using the OpenVPN service type, for example, `sudo cyberghostvpn --connect --openvpn --country-code CZ`.

I worked closely with the CyberGhostVPN team to report and remediate the vulnerabilities identified, and the CyberGhostVPN team had the following to say:

> We are delighted with the research performed by mmmds into our Linux application, and thank him for his efforts. Collaboration in the cybersecurity community is critical for keeping our users safe from all and any potential attack vectors. In this spirit, we are committed to continued transparency and partnership with all researchers on our bug bounty platform, and will continue providing our customers with world class protection. 

## Timeline

  * 01.12.2022: vulnerabilities reported
  * 02.12.2022: the report acknowledged by the vendor
  * 07.12.2022: vulnerabilities confirmed by the vendor
  * 24.12.2022: CyberGhostVPN Linux 1.4.0 released with a fix for remote code execution and privilege escalation
  * 22.02.2023: CyberGhostVPN Linux 1.4.1 released with certificate pinning
  * 06.03.2023: vendor notifies me that the issues have been fully addressed
  * 03.04.2023: vulnerabilities disclosed in coordination with the vendor

## References

  * <https://bugcrowd.com/disclosures/98117b52-679b-4745-8719-d8771be3d3f6/linux-client-lack-of-certificate-validation-leading-to-rce>
  * <https://bugcrowd.com/disclosures/93d4a008-31dc-441c-a160-ab81d217e288/linux-client-command-injection-local-privilege-escalation>
