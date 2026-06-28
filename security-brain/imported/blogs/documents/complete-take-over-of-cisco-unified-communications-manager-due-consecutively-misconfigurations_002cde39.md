---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-24_complete-take-over-of-cisco-unified-communications-manager-due-consecutively-mis.md
original_filename: 2022-09-24_complete-take-over-of-cisco-unified-communications-manager-due-consecutively-mis.md
title: Complete take-over of Cisco Unified Communications Manager due consecutively
  misconfigurations
category: documents
detected_topics:
- api-security
- ssrf
- command-injection
- automation-abuse
tags:
- imported
- documents
- api-security
- ssrf
- command-injection
- automation-abuse
language: en
raw_sha256: 002cde394875a821358027e674097fc92abeafe68d06e27948f068e7b3748152
text_sha256: 16c882615c647008b34f23d6c6cd9303352ab0aba54028fb67e3757c24a2251d
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Complete take-over of Cisco Unified Communications Manager due consecutively misconfigurations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-24_complete-take-over-of-cisco-unified-communications-manager-due-consecutively-mis.md
- Source Type: markdown
- Detected Topics: api-security, ssrf, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `002cde394875a821358027e674097fc92abeafe68d06e27948f068e7b3748152`
- Text SHA256: `16c882615c647008b34f23d6c6cd9303352ab0aba54028fb67e3757c24a2251d`


## Content

---
title: "Complete take-over of Cisco Unified Communications Manager due consecutively misconfigurations"
url: "https://infosecwriteups.com/complete-take-over-of-cisco-unified-communications-manager-due-consecutively-misconfigurations-2a1b5ce8bd9a"
authors: ["hackthebox"]
bugs: ["Security misconfiguration", "VoIP hacking"]
publication_date: "2022-09-24"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2124
scraped_via: "browseros"
---

# Complete take-over of Cisco Unified Communications Manager due consecutively misconfigurations

Complete take-over of Cisco Unified Communications Manager due consecutively misconfigurations
hackthebox
Follow
5 min read
·
Sep 24, 2022

7

Press enter or click to view image in full size

Hi there, this roadmap is developed to show that exploiting misconfigurations in devices an individual can get a complete take-over of a management control system. In this article we will cover Cisco VOIP Phones and Unified CM.

Product Overview: Cisco Unified Communications Manager (CallManager)

During the internal recon stage in ranges identified on internal network, and after getting all hosts alive, a good start is look for webapps on ports 80 and 443, I was able to identify by grepping the results of http-title nmap nse script all VOIP Phone devices that were exposed to internal network.

The exposed web interfaces of Cisco VOIP Phones looks like the following:

Some of the models were prone to public disclosed vulnerabilties with known exploits, but all of them were patched.

After spend a lot of time reading the documentation of all devices that I can reach I figured out that if the VOIP Phone configuration was left from default values and it was not hardened to increase its security, it might leak some interesting information.

For example, just to enter in the web portal, I was able to read phone logs, inside that logs, I can find phone calls with debug information, that allowed me to add more targets in the lists by parsing that logs. Also I was able to download the entire phone configuration file from the device and unencrypted configuration file of Cisco UCM.

Focusing on reading a lot of documentation when we perform a security audit (and I encourage you to do the same, because it’s make life easier), I found the following article from the manufacturer:

Two Ways to Obtain a Phone’s Configuration File from CUCM.

Press enter or click to view image in full size

Now the question is, where do we get the IP of the call manager?

Inside the exposed web panels of VOIP Phones, many IP addresses were disclosed, I just scraped all addresses from all devices in the target list, and scaned all these IP’s searching for opened port 6970 as the documentation says.

After few tests, I confirm that I found the API endpoint address that will provide us the configuration files. Inside that files we can obtain SSH and LDAP credentials.

I just build a script to get a nice terminal print with the gold data described above.

Spider all web VOIP Phone portals.
Extract MAC Address.
Craft the links to get configuration file.
Download and parse the configuration files.
Print important data in a nice way.

Just run python3 ciscophonecfg.py -iL voip-phone-addr.txt

The script is going to read from the target voip phones file (one phone per
line), then will do a little scraping on the exposed portals, and then
will build the links based on the information detailed above. The script is going to extract the critical data from the config file. It will then show a summary of each device.

Get hackthebox’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The code’s output I developed prints information as full name of owner of the phone, SSH credentials, and a “key file”. The last parameter is very interesting, becouse it’s the same link in all devices. That is the configuration manager file.

Press enter or click to view image in full size

That key file contains LDAP credentials of the Cisco UCM and other very interesting information. According to the official documentation, this file can be encrypted from the Cisco UCM configuration, but due to misconfigurations, this option was not enabled, and allowed us to read the file in cleartext. The syntax to obtain that configuration file is:

http://ip_callmanager:6970/@serviceProfileFile_value

Where @serviceProfileFile_Value is a filename like SPd95f326b-655f-2a44-d529–78e891d75b26.cnf.xml

At this point we have SSH and LDAP credentials used by Cisco Phone and Management System. Just in case I tried to login with the information scraped in the Cisco Unified Communications Manager portal, and by my fortune I was able to login as administrator due to rehused credentials:

Press enter or click to view image in full size

Other actions were conducted by this misconfigurations, like dump all telephone directory with a custom script developed on the go:

Press enter or click to view image in full size

Rehuse SSH credentials in other hosts:

And read-write access to Samba Share with LDAP credentials of Cisco UCM extracted from unencrypted key file:

Press enter or click to view image in full size
References
Cisco IP Phone 8800 Series Multiplatform Phone Administration Guide for Release 11.3(1) and Later …
If the parameter is enabled, the phone GUI honors the user access attribute of the relevant parameters when the GUI…

www.cisco.com

Two Ways to Obtain a Phone's Configuration File from CUCM
This document describes two ways to obtain a phone's configuration file. It is not uncommon to require the phone's…

www.cisco.com

Security Guide for Cisco Unified Communications Manager, Release 11.5(1) - Phone Security Profile…
Unified Communications Manager Administration groups security-related settings for a phone type and protocol into…

www.cisco.com

Reset or Change CUCM OS Admin and Security Password
This document describes how to reset or change OS admin password and security password. Cisco recommends that you have…

www.cisco.com

Enable the Encrypted Configuration Feature on the CUCM
This document describes the use of encrypted configuration phone files on the Cisco Unified Communications Manager…

www.cisco.com

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
