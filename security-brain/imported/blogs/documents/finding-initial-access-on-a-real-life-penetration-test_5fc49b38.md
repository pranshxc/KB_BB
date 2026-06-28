---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-23_finding-initial-access-on-a-real-life-penetration-test.md
original_filename: 2023-03-23_finding-initial-access-on-a-real-life-penetration-test.md
title: Finding Initial Access on a real life Penetration Test
category: documents
detected_topics:
- saml
- command-injection
- file-upload
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- saml
- command-injection
- file-upload
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 5fc49b384112b62e5e3370dfdb0c5c4606bc4b254cc416c7277085fb88302293
text_sha256: b95dbff90617d8713cc01f48274c57cd68d83f8faef3671069ad0b3a57a77810
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Finding Initial Access on a real life Penetration Test

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-23_finding-initial-access-on-a-real-life-penetration-test.md
- Source Type: markdown
- Detected Topics: saml, command-injection, file-upload, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `5fc49b384112b62e5e3370dfdb0c5c4606bc4b254cc416c7277085fb88302293`
- Text SHA256: `b95dbff90617d8713cc01f48274c57cd68d83f8faef3671069ad0b3a57a77810`


## Content

---
title: "Finding Initial Access on a real life Penetration Test"
url: "https://medium.com/@warrenbutterworth/finding-initial-access-on-a-real-life-penetration-test-86ed5503ae48"
authors: ["Warren Butterworth (@w88ugs)"]
bugs: ["Old components with known vulnerabilities", "Internal pentest", "RCE"]
publication_date: "2023-03-23"
added_date: "2023-03-28"
source: "pentester.land/writeups.json"
original_index: 1344
scraped_via: "browseros"
---

# Finding Initial Access on a real life Penetration Test

Finding Initial Access on a real life Penetration Test
Warren Butterworth
Follow
4 min read
·
Mar 23, 2023

7

On a recent internal Penetration Test I was faced with the above scenario and had to work a little harder for Domain Admin. So finding initial access. What do we need to do.. as a rule we will need one of 2 things:

a) Something vulnerable
b) Credentials

Press enter or click to view image in full size

Putting Red team tactics to one side (so that means no phishing etc) one of the above is often our only route to gaining intital access. Basically we need to steal , sniff or crack some credentials or we find something vulnerable (a juicy CVE will do nicely) to enable us to get a beacon/session on our initial target.

Often the first thing that comes to mind is responder/mitm6 or some sort of MITM attack to steal creds and relay/crack them. This is often a great step and usually finds some weak passwords, but in this case the client had been tested multiple times including by ourselves and had worked hard to push a new password policy. Even with an AWS hashcat instance these credentials were tough to crack.

Relaying credentials also didnt produce any joy. So we are only left with finding something vulnerable.

Enter Vcenter. A version of Vcenter was found that was vulnerable to
CVE-2021–22005 which exploits a file upload in VMware vCenter Server’s analytics/telemetry (CEIP) service to write a system crontab and execute shell commands as the root user. Great we can get a shell.

CVE-2021–22005 Root Shell

Gaining access to vCenter as root we can retrieve the data.mdb file which contains certificates which are stored in cleartext and can be used to sign any SAML authentication request for any user including the builtin Administrator. Gaining a root shell allows us to download this file.

Press enter or click to view image in full size
Data.mdb file

With this file there is a tool created by horizon3ai found here that allows us to create a cookie for the vCenter ui.

Cookie Created

With this cookie injected into a browser session on the vCenter /ui url we are authenticated onto the vsphere gui administrator.

Get Warren Butterworth’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Once on Vsphere I looked at 2 different scenarios.
1.) Dump vmdks and mount the locally, grab SYSTEM,SAM,SECURITY and dump hashes.
2.) Open all vm’s to see if any gave me some sort of access

I started with download dumps. This has to be done on VM backups or VMs that have been stopped. Fortunately there was a few available but the download size was often quite large.

Downloading vmdks

The process involved downloading the vmdk file, using kpartx to create device maps from the VMDK partition tables, mount the partition, copy the SAM, SECURITY and SYSTEM files and then run secretsdump on them. This for me gave me access to some RID 500 accounts hashes and Domain Cached Credentials (DCC) (Pretty slow to crack these!) The RID 500s didnt have any access on the rest of the domain but it was a useful exercise. You can find a great writeup on this here.

Next I opened every single VM to see if any didn’t need passwords to login. To my suprise I found one VM that dumped me straight on the desktop with no password prompt. After an initial look around Sophos was found to be running so I wanted to get something running quickly. I set up Responder and ntlmrelay. Using the VM I navigated to my Kali VM, captured and relayed the hash. This was a privileged account so succesfully dumped creds from 2 x Management Servers. Quite a lot of hashes were in here including LSA secrets in cleartext for an account that was configured to start a service. This account was a domain admin.

Always wanting to go the extra mile as I love getting a CobaltStrike Beacon I wmiexec’d to the Domain Controller. Again Sophos was running. Before dumping any file on disk I ran Hook Detector to see what Windows APIs were being hooked.

Press enter or click to view image in full size
Windows APIS hooked

Seems there are a few Windows APIs hooked but a few that are not including NTQueueApcThread. Utilising a little C# I created a process inject executable that downloaded a bin file and injected a payload (my CS Beacon) into memory. After hosting the bin file, uploading and running the exe I was presented with a High integrity beacon for CobaltStrike. From here a DCSYNC of the krbtgt NTLM/AES hash gave me domain dominance.

I hope you find this writeup helpful.

Feel free to connect on linkedin
