---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-19_logging-passwords-in-plaintext-in-azure-arc.md
original_filename: 2022-07-19_logging-passwords-in-plaintext-in-azure-arc.md
title: Logging Passwords in Plaintext in Azure Arc
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
- cloud-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
- cloud-security
- supply-chain
language: en
raw_sha256: 57bc768f1f52ade9d77615db7efd4be016b3e2aa3d66be4f1fe6731ce19af43e
text_sha256: 43a20951a595734962cd32b160e6a01b5b569807ee932ffe4bff3529c525b0aa
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Logging Passwords in Plaintext in Azure Arc

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-19_logging-passwords-in-plaintext-in-azure-arc.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `57bc768f1f52ade9d77615db7efd4be016b3e2aa3d66be4f1fe6731ce19af43e`
- Text SHA256: `43a20951a595734962cd32b160e6a01b5b569807ee932ffe4bff3529c525b0aa`


## Content

---
title: "Logging Passwords in Plaintext in Azure Arc"
url: "https://medium.com/tenable-techblog/logging-passwords-in-plaintext-in-azure-arc-2f94cb046a"
authors: ["Jimi Sebree (@DinoBytes)"]
programs: ["Microsoft"]
bugs: ["Information disclosure", "Local Privilege Escalation", "Cloud"]
publication_date: "2022-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2429
scraped_via: "browseros"
---

# Logging Passwords in Plaintext in Azure Arc

Logging Passwords in Plaintext in Azure Arc
James Sebree
Follow
2 min read
·
Jul 19, 2022

61

Microsoft’s Azure Arc is a management platform designed to bridge multi-cloud and similarly mixed environments together in a convenient way.

Tenable Research has discovered that the Jumpstart environments for Arc do not properly use logging utilities common amongst other Azure services. This leads to potentially sensitive information, such as service principal credentials and Arc database credentials, being logged in plaintext. The log files that these credentials are stored in are accessible by any user on the system. Based on this finding, it may be possible that other services are also affected by a similar issue.

Microsoft has patched this issue and updated their documentation to warn users of credential reuse within the Jumpstart environment. Tenable’s advisory can be found here. No bounty was provided for this finding.

The Flaw

The testing environment this issue was discovered in is the ArcBox Fullbox Jumpstart environment. No additional configurations are necessary beyond the defaults.

When ArcBox-Client provisions during first-boot, it runs a PowerShell script that is sent to it via the `Microsoft.Compute.CustomScriptExtension (version 1.10.12) plugin.

Get James Sebree’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Most scripts we’ve come across on other services tend to write ***REDACTED*** in place of anything sensitive when writing to a log file. For example:

<PluginSettings>
  <Plugin name="Microsoft.CPlat.Core.RunCommandLinux" version="1.0.3">
  <RuntimeSettings seqNo="0">{
  "runtimeSettings": [
  {
  "handlerSettings": {
  "protectedSettingsCertThumbprint": "7AF139E055555FAKEINFO555558EC374DAD46370",
  "protectedSettings": "*** REDACTED ***",
  "publicSettings": {}
  }
  }
  ]
}</RuntimeSettings>

In the provisioning script for this host, however, this sanitizing is not done. For example, in “C:\Packages\Plugins\Microsoft.Compute.CustomScriptExtension\1.10.12\Status\0.status”, our secrets and credentials are plainly visible to everyone, including low privileged users.

Press enter or click to view image in full size
Press enter or click to view image in full size

This allows a malicious actor to disclose potentially sensitive information if they were to gain access to this machine. The accounts revealed could allow the attacker to further compromise a customer’s Azure environment if these credentials or accounts are re-used elsewhere.

Conclusion

Obviously, the Arc Jumpstart environment is intended to be used as a demo environment, which ideally lessens the impact of the revealed credentials — provided that users haven’t reused the service principal elsewhere in their environment. That said, it isn’t uncommon for customers to use these types of Jumpstart environments as a starting point to build out their actual production infrastructure.

We do, however, feel it’s worth being aware of this issue in the event that other logging mechanisms exist elsewhere in the Azure ecosystem, which could have more dire consequences if present in a production environment.
