---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-12_eset-endpoint-security-credentials-theft.md
original_filename: 2021-10-12_eset-endpoint-security-credentials-theft.md
title: ESET Endpoint Security credentials theft
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 2c8c5fef5385eba7a00fdafcc9c6896c1f9963bfa85cfc1e4864410272b46346
text_sha256: c168d8bf2158cc6707b0c49b5dd659c3497658466966a5724eaf08234e1df5e2
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# ESET Endpoint Security credentials theft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-12_eset-endpoint-security-credentials-theft.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `2c8c5fef5385eba7a00fdafcc9c6896c1f9963bfa85cfc1e4864410272b46346`
- Text SHA256: `c168d8bf2158cc6707b0c49b5dd659c3497658466966a5724eaf08234e1df5e2`


## Content

---
title: "ESET Endpoint Security credentials theft"
url: "https://medium.com/@mehdi.alouache/eset-endpoint-security-credentials-theft-90082dfdf474"
authors: ["Mehdi Alouache"]
programs: ["ESET"]
bugs: ["Credentials sent over unencrypted channel"]
publication_date: "2021-10-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3242
scraped_via: "browseros"
---

# ESET Endpoint Security credentials theft

ESET Endpoint Security credentials theft
Mehdi Alouache
Follow
3 min read
·
Oct 12, 2021

16

1

The title should have been Improper check of definitions updates in ESET Endpoint security leads to enterprise credentials theft, but this seemed a bit long, isn’t it ?

I submitted what I believe to be a vulnerability in a confidential report to ESET first, but finally received an answer mentioning this was not eligible for a bug bounty.

A vulnerability leveraging quite similar behaviours was reported back on 2016 on a different perimeter : https://www.cvedetails.com/cve/CVE-2016-9892/

TL;DR

The vulnerability reported here allows an attacker who has a foothold in an organization using ESET to passively steal the ESET license as well as ESET License Administrator credentials (https://ela.eset.com/LicenseOwner/Converter)

Presentation

The test was conducted on a Windows 10 21h1 computer, running a ESET Endpoint Security 7.32.2041.0

At the moment, I have all the reasons to believe this behaviour can be reproduced against any version of ESET Endpoint Security.

Get Mehdi Alouache’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

During a security audit of an internal infrastructure, I was trying to hijack DNS traffic through a rogue IPv6 DNS beside Responder waiting for some employees to log-in somewhere. However, what happened was one instance of ESET Endpoint Security on the network tried to update its database by contacting pico.eset.com, sending me some plain-text credentials. The site seems to have an SSL certificate with an invalid Common Name (update.eset.com instead of pico.eset.com).

Press enter or click to view image in full size

Take note in the meantime that this website seems to be accessible as well on plain-text HTTP. I believe it to be an issue in itself.

Press enter or click to view image in full size
nmap scan of pico.eset.com showing http support

For the following, I have not been able to determine if I was able to capture the credentials because ESET tried to connect to pico.eset.com on port 80 or if it tried port 443 and did not perform a TLS/SSL check before, leading to the MITM attack success.
When presented a basic auth form by Responder following the DNS IPv6 spoofing, ESET sent the plaintext credentials with the username of the syntax “EAV-XXXXXXXXXX” as well as the password.

These credentials can be reused to manually on the License Manager URL available here: https://ela.eset.com/LicenseOwner/Converter. Then, licenses can be generated as follows:

“Use this license key to active ESET products”
Summary

Prerequisites
- A computer in the same network than your target on which you have administrator rights to use tools such as Responder or Wireshark
- Nothing else (but it is easier if your target responds to Netbios/LLMNR or has no static IPv6 DNS setup, otherwise a simple packet sniffer could do the job).
Impact
The target (individual or company) will get its licensing information stolen and the attacker can issue licenses for himself. Perhaps is there some other usage for the credentials that I didn’t identify yet. No impact for ESET company, only an impact for customers ==> Additional costs on the licenses or licenses expiration by over-usage.
Easiness
Definitely not rocket science…
