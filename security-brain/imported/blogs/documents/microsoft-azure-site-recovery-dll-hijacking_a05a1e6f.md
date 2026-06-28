---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-12_microsoft-azure-site-recovery-dll-hijacking.md
original_filename: 2022-07-12_microsoft-azure-site-recovery-dll-hijacking.md
title: Microsoft Azure Site Recovery DLL Hijacking
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: a05a1e6fbcca3b76f53d37c2fc2b002e4d9504534f7b2c58adc1017569325e82
text_sha256: 4bce2803ab7d46f2942d9cbb42385f4b1df9826d7f11f1477ff525124d313d22
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Azure Site Recovery DLL Hijacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-12_microsoft-azure-site-recovery-dll-hijacking.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `a05a1e6fbcca3b76f53d37c2fc2b002e4d9504534f7b2c58adc1017569325e82`
- Text SHA256: `4bce2803ab7d46f2942d9cbb42385f4b1df9826d7f11f1477ff525124d313d22`


## Content

---
title: "Microsoft Azure Site Recovery DLL Hijacking"
url: "https://medium.com/tenable-techblog/microsoft-azure-site-recovery-dll-hijacking-cd8cc34ef80c"
authors: ["Jimi Sebree (@DinoBytes)"]
programs: ["Microsoft"]
bugs: ["DLL Hijacking", "Privilege escalation"]
bounty: "10,000"
publication_date: "2022-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2464
scraped_via: "browseros"
---

# Microsoft Azure Site Recovery DLL Hijacking

Microsoft Azure Site Recovery DLL Hijacking
James Sebree
Follow
3 min read
·
Jul 12, 2022

226

1

Azure Site Recovery is a suite of tools aimed at providing disaster recovery services for cloud resources. It provides utilities for replication, data recovery, and failover services during outages.

Tenable Research has discovered that this service is vulnerable to a DLL hijacking attack due to incorrect directory permissions. This allows any low-privileged user to escalate to SYSTEM level privileges on hosts where this service is installed.

Microsoft has assigned this issue CVE-2022–33675 and rated it a severity of Important with a CVSSv3 score 7.8. Tenable’s advisory can be found here. Microsoft’s post regarding this issue can be found here. Additionally, Microsoft is expected to award a $10,000 bug bounty for this finding.

The Flaw

The cxprocessserver service runs automatically and with SYSTEM level privileges. This is the primary service for Azure Site Recovery.

Incorrect permissions on the service’s executable directory (“E:\Program Files (x86)\Microsoft Azure Site Recovery\home\svsystems\transport\”) allow new files to be created by normal users. Please note that while the basic permissions show that “write” access is disabled, the “Special Permissions” still incorrectly grant write access to this directory. This can be verified by viewing the “Effective Access” granted to a given user for the directory in question, as demonstrated in the following screenshot.

Press enter or click to view image in full size

This permissions snafu allows for a DLL hijacking/planting attack via several libraries used by the service binary.

Proof of Concept

For brevity, we’ve chosen to leave full exploitation steps out of this post since DLL hijacking techniques are extremely well documented elsewhere.

Get James Sebree’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

A malicious DLL was created to demonstrate the successful hijack via procmon.

Under normal circumstances, the loading of ktmw32.dll looks like the following:

Press enter or click to view image in full size

With our planted DLL, the following can be observed:

Press enter or click to view image in full size

This allows an attacker to elevate from an arbitrary, low-privileged user to SYSTEM. During the disclosure process, Microsoft confirmed this behavior and has created patches accordingly.

Conclusion

DLL hijacking is quite an antiquated technique that we don’t often come across these days. When we do, impact is often quite limited due to lack of security boundaries being crossed. MSRC lists several examples in their blog post discussing how they triage issues that make use of this technique.

In this case, however, we were able to cross a clear security boundary and demonstrated the ability to escalate a user to SYSTEM level permissions, which shows the growing trend of even dated techniques finding a new home in the cloud space due to added complexities in these sorts of environments.

As this vulnerability was discovered in an application used for disaster recovery, we are reminded that had this been discovered by malicious actors, most notably ransomware groups, the impact could have been much wider reaching. Ransomware groups have been known to target backup files and servers to ensure that a victim is forced into paying their ransom and unable to restore from clean backups. We strongly recommend applying the Microsoft supplied patches as soon as possible to ensure your existing deployments are properly secured. Microsoft has taken action to correct this issue, so any new deployments should not be affected by this flaw.
