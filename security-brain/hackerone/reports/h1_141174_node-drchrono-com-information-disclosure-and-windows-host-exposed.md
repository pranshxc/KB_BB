---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141174'
original_report_id: '141174'
title: node.drchrono.com - Information Disclosure and Windows Host Exposed
team_handle: drchrono
created_at: '2016-05-26T12:34:52.294Z'
disclosed_at: '2016-06-13T19:02:13.909Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# node.drchrono.com - Information Disclosure and Windows Host Exposed

## Metadata

- HackerOne Report ID: 141174
- Weakness: 
- Program: drchrono
- Disclosed At: 2016-06-13T19:02:13.909Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This host has the following TCP ports open;
* 21 - FTP
* 22 - SSH
* 135 - Windows RPC Dynamic
* 445 - Microsoft DS
* 3389 - Remote Desktop
* 5986 - PowerShell Remoting
* 47001 - WinRM

The server appears to be secured well on the whole.
However the services SSH and FTP do all give out some information.
Please see attached images for the versions given out.
This information could be used by a malicious attacker, to create a targeted attack vector, on the underlying server.

To remove the FileZilla ftp server version go to the options and ensure the **%v** is removed from the welcome message. See the screenshot named **Remove FileZilla version.PNG**.

To remove the banner version from the SSH service locate the SSH configuration file and open it up in notepad, find the line with the option named **banner** and set it to **none**. The default location for Windows is **C:\Program Files\OpenSSH\etc\ssh_config**.

The remote desktop is widely open and does not require any form of authentication to connect. As you will see in the screenshot named **Remote Desktop.png** it clearly states the OS version running, which again all helps a malicious attacker. You can not remove this information however you can protect against it. It is highly recommended that you enable network level authentication (NLA), this means that you are not able to connect to remote desktop unless you are authenticated first. Also ensure that you have set the remote desktop to use high encryption. More information about this can be found here https://technet.microsoft.com/en-us/library/cc770833(v=ws.11).aspx.

With Microsoft DS (445 SMB) open, ensure you have disabled the local administrator account or at least renamed it from default. This account can not be locked out, allowing for unlimited password guesses against it. This would facilitate an attacker, as they could use this service to brute force the password until obtained. As remote desktop is open they could simply login to the server with full administrative privileges once the password has been revealed.

I would highly recommend ensuring that you have had a build review completed on the server by an experienced security professional as the server is very open to the internet. If money is an issue then ask your administration team to follow the guidance from the CIS benchmarks, available at https://benchmarks.cisecurity.org/downloads/benchmarks/.

Final general advice is to not open the ports to the world when there is no need and to ensure that the FTP/SSH service installed is always fully patched.
The ports identified are useful for internal administration only, I would recommend limiting their availability to your trusted subnets or IP addresses. This can be done using the windows firewall or a hardware firewall such as checkpoint.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
