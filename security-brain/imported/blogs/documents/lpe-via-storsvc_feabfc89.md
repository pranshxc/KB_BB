---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-13_lpe-via-storsvc.md
original_filename: 2023-02-13_lpe-via-storsvc.md
title: LPE via StorSvc
category: documents
detected_topics:
- access-control
- xss
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- api-security
language: en
raw_sha256: feabfc89ba1b20dbce9eb90406bd4539e942a5628e7b0cebdb715987c77d0dee
text_sha256: 3442ca77614f7c03ed932fc630015739bc4b6a80b127dca3988741302d66b6a5
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# LPE via StorSvc

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-13_lpe-via-storsvc.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `feabfc89ba1b20dbce9eb90406bd4539e942a5628e7b0cebdb715987c77d0dee`
- Text SHA256: `3442ca77614f7c03ed932fc630015739bc4b6a80b127dca3988741302d66b6a5`


## Content

---
title: "LPE via StorSvc"
page_title: "redteam-research/LPE via StorSvc at master · blackarrowsec/redteam-research · GitHub"
url: "https://github.com/blackarrowsec/redteam-research/tree/master/LPE%20via%20StorSvc"
final_url: "https://github.com/blackarrowsec/redteam-research/tree/master/LPE%20via%20StorSvc"
authors: ["Antón Ortigueira (@antuache)", "Kurosh Dabbagh (@_Kudaes_)"]
programs: ["Microsoft (Windows)"]
bugs: ["Local Privilege Escalation", "DLL Hijacking"]
publication_date: "2023-02-13"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1532
---

# LPE via StorSvc

Windows Local Privilege Escalation via StorSvc service (writable SYSTEM path DLL Hijacking)

## Summary

StorSvc is a service which runs as `NT AUTHORITY\SYSTEM` and tries to load the missing **SprintCSP.dll** DLL when triggering the `SvcRebootToFlashingMode` RPC method locally.

## Description

The `StorSvc.dll!SvcRebootToFlashingMode` RPC method, calls `StorSvc.dll!InitResetPhone` which also calls `StorSvc.dll!ResetPhoneWorkerCallback`, that tries to load **SprintCSP.dll** as shown in the image below:

[![FactoryResetUICC.png](/blackarrowsec/redteam-research/raw/master/LPE%20via%20StorSvc/FactoryResetUICC.png)](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/FactoryResetUICC.png)

As this DLL is missing, it is loaded following the **DLL Search Order** flow and we can take advantage of this behaviour by placing a malicious DLL in a writable folder contained in the SYSTEM `%PATH%`. Then, the malicious DLL should be executed with **SYSTEM privileges**.

It is worth noting that the service is launched as `NT AUTHORITY\SYSTEM` in the service group `LocalSystemNetworkRestricted` which has the following privileges:
  
  
  Privilege Name  Description  State  
  ============================ =================================================== =============
  SeTcbPrivilege  Act as part of the operating system  Enabled  
  SeLoadDriverPrivilege  Load and unload device drivers  Disabled
  SeBackupPrivilege  Back up files and directories  Disabled
  SeRestorePrivilege  Restore files and directories  Disabled
  SeSystemEnvironmentPrivilege Modify firmware environment values  Disabled
  SeChangeNotifyPrivilege  Bypass traverse checking  Enabled  
  SeManageVolumePrivilege  Perform volume maintenance tasks  Enabled  
  

The command line that corresponds to this service is `C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p -s StorSvc`.

## Proof of Concept

In this repo we provide 2 different source codes:

  * [**RpcClient.exe**](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/RpcClient): that triggers the RPC call.
  * [**SprintCSP.dll**](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/SprintCSP): which can be placed to exploit the DLL Hijacking. This PoC runs a `whoami` command and writes the output to `C:\ProgramData\whoamiall.txt`. If you want to expand the functionality of this PoC you can edit the `DoStuff()` function at [main.c](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/SprintCSP/SprintCSP/main.c#L7).

The provided exploit should work by default and has been tested on **Windows 10** , **Windows 11** , **Windows Server 2019** and **Windows Server 2022**. **In order to make it work, the`#define` macro at [storsvc_c.c](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/RpcClient/RpcClient/storsvc_c.c#L3) must be changed so the exploit is adapted to the target machine's operative system.**

After triggering the exploit it is necessary to **stop** or **reboot** the service, which [SprintCSP.dll](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/SprintCSP) already does.

### Steps

  1. Find writable SYSTEM path with `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" -v Path`
  2. Copy [SprintCSP.dll](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/SprintCSP) to the writable path
  3. Execute [RpcClient.exe](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/RpcClient)
  4. Check `C:\ProgramData\whoamiall.txt`

[![PoC.gif](/blackarrowsec/redteam-research/raw/master/LPE%20via%20StorSvc/PoC.gif)](/blackarrowsec/redteam-research/blob/master/LPE%20via%20StorSvc/PoC.gif)

## References

  * [Fuzzing Windows RPC with RpcView](https://itm4n.github.io/fuzzing-windows-rpc-rpcview/)
  * [CdpSvcLPE](https://github.com/sailay1996/CdpSvcLPE/blob/main/README.md)
  * [CDPSvc DLL Hijacking - From LOCAL SERVICE to SYSTEM](https://itm4n.github.io/cdpsvc-dll-hijacking/)

# 

[![](https://camo.githubusercontent.com/476c0c909f3bd61169f79ff692936d52aad0c86f36d627e05a010bdb7ab5a05c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7777772d626c61636b6172726f772e6e65742d4535413530353f7374796c653d666c61742d737175617265)](https://www.blackarrow.net) [![](https://camo.githubusercontent.com/3ce059269fbaff69a4de964635713522752d46dd36de0ff2258699f58476fb34/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f747769747465722d40426c61636b4172726f775365632d3030616365643f7374796c653d666c61742d737175617265266c6f676f3d74776974746572266c6f676f436f6c6f723d7768697465)](https://twitter.com/BlackArrowSec) [![](https://camo.githubusercontent.com/273f6af793ea5ab35b27e613578de5bce118450171390cb83ca71e94af7135a5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d40426c61636b4172726f775365632d3030383462343f7374796c653d666c61742d737175617265266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/company/blackarrowsec/)
