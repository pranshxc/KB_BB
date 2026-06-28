---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-31_remote-command-execution-in-binwalk.md
original_filename: 2023-01-31_remote-command-execution-in-binwalk.md
title: Remote Command Execution in binwalk
category: documents
detected_topics:
- command-injection
- path-traversal
- supply-chain
- automation-abuse
tags:
- imported
- documents
- command-injection
- path-traversal
- supply-chain
- automation-abuse
language: en
raw_sha256: f216616d7e50ea0e004dfc0a8e801d5de0f7ae88d08af940ea4cf923dda5dfe9
text_sha256: 929f35a4e5bd8d9033e522c070d1c5cc494b2fcf0ce6618564e8895bfa2e2278
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Command Execution in binwalk

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-31_remote-command-execution-in-binwalk.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, supply-chain, automation-abuse
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `f216616d7e50ea0e004dfc0a8e801d5de0f7ae88d08af940ea4cf923dda5dfe9`
- Text SHA256: `929f35a4e5bd8d9033e522c070d1c5cc494b2fcf0ce6618564e8895bfa2e2278`


## Content

---
title: "Remote Command Execution in binwalk"
page_title: "Security Advisory: Remote Command Execution in binwalk | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/security-advisory-remote-command-execution-in-binwalk/"
final_url: "https://www.onekey.com/resource/security-advisory-remote-command-execution-in-binwalk"
authors: ["Quentin Kaiser (@QKaiser)"]
programs: ["ReFirm Labs (binwalk)", "ubi_reader", "jefferson", "yaffshiv"]
bugs: ["RCE", "Path traversal", "Security code review"]
publication_date: "2023-01-31"
added_date: "2023-02-07"
source: "pentester.land/writeups.json"
original_index: 1601
---

[Resources](/resources)

>

[Research](/resources/research)

>

Security Advisory: Remote Command Execution in binwalk

# Security Advisory: Remote Command Execution in binwalk

![Security Advisory: Remote Command Execution in binwalk](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b823006e95c450f5618ef_6712aebc0c7fcf8155cb3fc0_18.jpeg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

January 30, 2023

7

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

## Introduction

Before we dive into the technical details, we want to raise our hats to the teams behind [binwalk](https://github.com/ReFirmLabs/binwalk/), [ubi_reader](https://github.com/jrspruitt/ubi_reader), [jefferson](https://github.com/sviehb/jefferson), and [yaffshiv](https://github.com/devttys0/yaffshiv) and express our respect and admiration for the work they put into it over the years and all their contributions towards the security community. Without them, and many other great projects, security analysis of IoT devices would not be where it is today. With the fading maintenance of binwalk, we too were inspired to contribute to the security community and open source our internal extraction framework [unblob](https://www.unblob.org). Our objective with this blog is to summarize some of the pitfalls when dealing with untrusted data and to raise awareness about path traversal security issues and the impact they may have. 

With that being out of the way, let's dive in !

As detailed in my Black Alps talk, we audited multiple third-party extractors code base that unblob relies on over the summer of 2022 and identified multiple issues ranging from logic bugs leading to extraction failures to path traversals. In the process, I learned a lot about the many different ways you can end up with a path traversal in Python.

Around October 2022, I had the realization that if all those third-party dependencies are suffering from some variation of these insecure coding patterns, binwalk may be too. So, I started looking and soon enough found a path traversal within the PFS filesystem extractor. I then found a way to gain remote code execution by abusing binwalk's plugin system over lunch at [hardwear.io](https://hardwear.io/) with [Mücahid](https://twitter.com/muc0ze).

As explained in the [pull request](https://github.com/ReFirmLabs/binwalk/pull/617) I sent on October 26th, I took the liberty to report [it] in the open since [#556](https://github.com/ReFirmLabs/binwalk/pull/556) was fixed that way and I did not find any security/coordinated disclosure policy or contact info. At the time of publication, the vulnerability has yet to be patched.

## Path Traversal in Binwalk

**Affected vendor & product**| Refirm Labs binwalk  
---|---  
**Vendor Advisory**|  None at this time.  
**Vulnerable version**|  2.1.2b through 2.3.3 included  
**Fixed version**|  None at this time.  
**CVE IDs**| [CVE-2022-4510](https://nvd.nist.gov/vuln/detail/CVE-2022-4510)  
**Impact (CVSS)**|  7.8 (high) [AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H&version=3.1)  
**Credit**|  Q. Kaiser, ONEKEY Research Lab  
  
## Summary

A path traversal vulnerability was identified in ReFirm Labs binwalk from version 2.1.2b through 2.3.3 (inclusive). This vulnerability allows remote attackers to execute arbitrary code on affected installations of binwalk. User interaction is required to exploit this vulnerability in that the target must open the malicious file with binwalk using extract mode (`-e` option).

## The bug

PFS is an obscure filesystem format found in some embedded devices. The only public documentation comes from a tool named [pfstool](https://lekensteyn.nl/files/pfs/pfs.txt) written by Peter Lekensteyn.

A PFS extractor plugin was merged into binwalk in 2017 with commit [d023454](https://github.com/ReFirmLabs/binwalk/commit/d023454), and a path traversal mitigation attempt was introduced with commit [58d1d92](https://github.com/ReFirmLabs/binwalk/commit/58d1d92) on the same day. This commit introduced the following change:
  
  
  def extractor(self, fname):
  fname = os.path.abspath(fname)
  +  out_dir = binwalk.core.common.unique_file_name(os.path.join(os.path.dirname(fname), "pfs-root"))
  +
  try:
  with PFS(fname) as fs:
  # The end of PFS meta data is the start of the actual data
  -  data = open(fname, 'rb')
  +  data = binwalk.core.common.BlockFile(fname, 'rb')
  data.seek(fs.get_end_of_meta_data())
  for entry in fs.entries():
  -  self._create_dir_from_fname(entry.fname)
  -  outfile = open(entry.fname, 'wb')
  -  outfile.write(data.read(entry.fsize))
  -  outfile.close()
  +  outfile_path = os.path.join(out_dir, entry.fname)
  +  if not outfile_path.startswith(out_dir): # this branch will never be taken
  +  binwalk.core.common.warning("Unpfs extractor detected directory traversal attempt for file: '%s'. Refusing to extract." % outfile_path)
  +  else:
  +  self._create_dir_from_fname(outfile_path)
  +  outfile = binwalk.core.common.BlockFile(outfile_path, 'wb')
  +  outfile.write(data.read(entry.fsize))
  +  outfile.close()
  data.close()
  except KeyboardInterrupt as e:
  raise e
  

The issue lies in the fact that `os.path.join` one line 16 does not fully resolve a path. Therefore, the condition on line 17 will never be true. Here's an example of that behavior:
  
  
  >>> os.path.join("/tmp", "../etc/passwd")
  '/tmp/../etc/passwd'
  >>> os.path.abspath(os.path.join("/tmp", "../etc/passwd"))
  '/etc/passwd'

By crafting a valid PFS filesystem with filenames containing the `../` traversal sequence, we can force binwalk to write files **outside** of the extraction directory.

## Our fix

Our fix simply introduce a call to `os.path.abspath` on line 8 so that the built path is fully resolved.
  
  
  --- a/src/binwalk/plugins/unpfs.py
  +++ b/src/binwalk/plugins/unpfs.py
  @@ -104,7 +104,7 @@ class PFSExtractor(binwalk.core.plugin.Plugin):
  data = binwalk.core.common.BlockFile(fname, 'rb')
  data.seek(fs.get_end_of_meta_data())
  for entry in fs.entries():
  -  outfile_path = os.path.join(out_dir, entry.fname)
  +  outfile_path = os.path.abspath(os.path.join(out_dir, entry.fname))
  if not outfile_path.startswith(out_dir):
  binwalk.core.common.warning("Unpfs extractor detected directory traversal attempt for file: '%s'. Refusing to extract." % outfile_path)
  else:
  

## Exploitation Strategy

There are plenty of ways to get remote command execution from a path traversal (e.g., by overwriting `.ssh/authorized_keys` to obtain password-less SSH access, overwrite `~/.bashrc` to execute arbitrary commands on the next login), but I wanted something that was environment agnostic and relied on what's already there. **Enter binwalk plugins**.

Since the early days of binwalk, users have the ability to define their own plugins using binwalk's API. As [indicated in the documentation](https://github.com/ReFirmLabs/binwalk/wiki/Creating-Custom-Plugins#plugin-activation):

"_Activating a plugin is as simple as dropping it in binwalk's plugin directory $HOME/.config/binwalk/plugins/. The plugin will then be loaded on all subsequent binwalk scans._ "[](https://github.com/ReFirmLabs/binwalk/wiki/_Footer/_edit)

So, if we exploit the path traversal to write a valid plugin at that location, binwalk will immediately pick it up and execute it **while it's still scanning the malicious file**. On top of that, the PFS extractor will take care of creating all required directories if they do not exist, so we don't need to expect anything from the system we're running on.

This is the plugin I ended up writing. The plugin executes two times since it does not define an explicit `MODULE` attribute that defines its purpose (e.g., signature scan, entropy calculation, compression stream identification). I take advantage of that behavior to make it clean up after itself.
  
  
  import binwalk.core.plugin
  import os
  import shutil
  
  class MaliciousExtractor(binwalk.core.plugin.Plugin):
  """
  Malicious binwalk plugin
  """
  
  def init(self):
  if not os.path.exists("/tmp/.binwalk"):
  os.system("id")
  with open("/tmp/.binwalk", "w") as f:
  f.write("1")
  else:
  os.remove("/tmp/.binwalk")
  os.remove(os.path.abspath(__file__))
  shutil.rmtree(os.path.join(os.path.dirname(os.path.abspath(__file__)), "__pycache__"))
  

Crafting malicious PFS file is left as an exercise to the reader.

## Demo

Here's a video demo of the exploit:

## Future Work

The ["D-Link RomFS" plugin](https://github.com/ReFirmLabs/binwalk/blob/master/src/binwalk/plugins/dlromfsextract.py) is probably affected by a similar vulnerability but the format, which is actually eCOS RomFS, is not parsed properly (see this [PR](https://github.com/ReFirmLabs/binwalk/pull/456) for a fix). I did not want to load two opposing format constructs in my brain just to come up with a proof-of-concept. As a former colleague of mine would have said: CBA.

## Key Takeaways

As security industry, every now and then, we need to look in the mirror and also validate the security of our own technology stack. This especially becomes critical in forensic analysis and reverse engineering where we are commonly faced with untrusted, potentially malicious files.

While the path traversals described in this article have the potential to void any reverse engineering efforts and to tamper with evidence collected, they also demonstrate the importance of sandboxing analysis environments to limit the impact of such vulnerabilities. Especially with the rise of automated extraction and analysis tools relying on tools like binwalk (e.g., FACT, ofrak, EMBA), it's important for developers and users of those solution to be aware of the risks.

## Timeline

**2022-10** -**24** \- Attempt to get in touch with Refirm Labs but no security policies and domains are down.

**2022-10-26** – Decided to send a pull request with the fix (<https://github.com/ReFirmLabs/binwalk/pull/617>) so that it could be immediately integrated.

**2022-11-17** – Live demo of the exploit during our talk at Black Alps.

**2023-01-24** – Since the CPE of the latest binwalk vulnerability states `microsoft:binwalk` and that Refirm Labs got [acquired in 2021](https://www.microsoft.com/en-us/security/blog/2021/06/02/microsoft-acquires-refirm-labs-to-enhance-iot-security/), we reported it to MSRC. Turns out MSRC does not consider it a Microsoft product and the CPE was chosen this way by [VulDB](https://vuldb.com/).

**2023-01-25** – Since we're a CNA and we're not seeing any movement on the repository, we take the decision to create a dedicated CVE so that users are aware of this. 

**2023-01-31** – ONEKEY releases its advisory

* * *

  
  

## Python Path Traversal Code Patterns

All of the code examples provided below are illustrations of the insecure code patterns observed in the affected projects. You can click on the link provided in each description to open the pull request highlighting the actual code.

### ubi_reader - **no path traversal verification at all**

**Affected vendor & product**| jrspruitt:ubi_reader  
---|---  
**Vulnerable version**|  < 0.8.5  
**Fixed version**|  0.8.5  
**CVE IDs**| [CVE-2023-0591](https://nvd.nist.gov/vuln/detail/CVE-2023-0591)  
**Impact (CVSS)**|  5.5 (medium) [AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N&version=3.1)  
**Credit**|  Q. Kaiser, ONEKEY Research Lab  
  
As seen in [ubi_reader](https://github.com/jrspruitt/ubi_reader/pull/57/files), the code does not attempt to protect against traversal.
  
  
  import os
  extraction_dir = "/tmp"
  
  for filename in filenames:
  extraction_path = os.path.join(extraction_dir, filename)

### **jefferson - no path traversal verification at all**

**Affected vendor & product**| sviehb:jefferson  
---|---  
**Vulnerable version**|  < 0.4.1  
**Fixed version**|  0.4.1  
**CVE IDs**| [CVE-2023-0592](https://nvd.nist.gov/vuln/detail/CVE-2023-0592)  
**Impact (CVSS)**|  5.5 (medium) [AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N&version=3.1)  
**Credit**|  Q. Kaiser, ONEKEY Research Lab  
  
Similar but not the same signature, observed in [Jefferson](https://github.com/sviehb/jefferson/pull/36/files).
  
  
  import os
  extraction_dir = "/tmp"
  
  for filename in filenames:
  extraction_path = os.path.join(os.getcwd(), extraction_dir, path)

### **yaffshiv - misunderstanding os.path.join's argument precedence**

**Affected vendor & product**| devttys0:yaffshiv  
---|---  
**Vulnerable version**|  <= 0.1  
**Fixed version**|  None  
**CVE IDs**| [CVE-2023-0593](https://nvd.nist.gov/vuln/detail/CVE-2023-0592)  
**Impact (CVSS)**|  5.5 (medium) [AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N&version=3.1)  
**Credit**|  Q. Kaiser, ONEKEY Research Lab  
  
The code makes the assumption that `filename` does not start with a forward slash. Observed in [yaffshiv](https://github.com/devttys0/yaffshiv/pull/3/files).
  
  
  import os
  extraction_dir = "/tmp"
  
  for filename in filenames:
  file_path = os.path.join(extraction_dir, filename)
  if b'..' in file_path:
  raise Exception("Path traversal attempt, aborting.")

The second argument of `os.path.join` always takes precedence if both of them starts with a forward slash.
  
  
  >>> os.path.join("/tmp", "home/traversal")
  '/tmp/home/traversal'
  >>> os.path.join("/tmp", "/home/traversal")
  '/home/traversal'

### **binwalk's unpfs -**misunderstanding os.path.join's lack of resolution****

The code makes the assumption that `os.path.join` returns an absolute path, which it doesn't.
  
  
  import os
  extraction_dir = "/tmp"
  
  for filename in filenames:
  outfile_path = os.path.join(extraction_dir, filename)
  if not outfile_path.startswith(extraction_dir ): # this condition will never be True
  raise Exception("Path traversal attempt, aborting.")

This is what it looks like:
  
  
  >>> os.path.join("/tmp", "../etc/passwd")
  '/tmp/../etc/passwd'
  >>> os.path.abspath(os.path.join("/tmp", "../etc/passwd"))
  '/etc/passwd'

Share

## About Onekey

[ONEKEY](/) is the leading European specialist in Product Cybersecurity & Compliance Management and part of the investment portfolio of [PricewaterhouseCoopers Germany (PwC)](https://www.pwc.de/de.html). The unique combination of the automated ONEKEY Product Cybersecurity & Compliance Platform (OCP) with expert knowledge and consulting services provides fast and comprehensive analysis, support, and management to improve product cybersecurity and compliance from product purchasing, design, development, production to end-of-life.

![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/68d39e055d1135bee5f4ee28_foto_website_careers.webp)

CONTACT:  
Sara Fortmann  
Senior Marketing Manager  
[sara.fortmann@onekey.com](mailto:sara.fortmann@onekey.com)

euromarcom public relations GmbH  
[team@euromarcom.de](mailto:team@euromarcom.de)

## RELATED RESEARCH ARTICLES

![Latest Developments in Unblob: New Formats, Smarter Extraction, and a More Hardened Release Pipeline](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/69c51b643603964355fec609_2026-03-26-ONEKEY-Unblob-Dev.-Update_Banner.png)

Research

Mar 26, 2026

10

min read

### Latest Developments in Unblob: New Formats, Smarter Extraction, and a More Hardened Release Pipeline

Discover what changed in unblob since release 25.11.25, including new firmware and filesystem format support, smarter extraction workflows, robustness fixes, performance improvements, and stronger release security.

[Read More![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/67ee4d7596311684a7a1a95a_xynrqysiccm914h50n.svg)](/resource/latest-developments-in-unblob-new-formats-smarter-extraction-and-a-more-hardened-release-pipeline)

[](/resource/latest-developments-in-unblob-new-formats-smarter-extraction-and-a-more-hardened-release-pipeline)

![How We Taught Our Platform to Understand RTOS Firmware](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/68d14bca3bf9570f12d3d2ab_HERO-RTOS-research-ONEKEY.jpg)

Research

Sep 22, 2025

15

min read

### How We Taught Our Platform to Understand RTOS Firmware

Discover how ONEKEY’s platform breaks open real-time operating system (RTOS) firmware. Learn how automated architecture detection, load address recovery, and component identification bring transparency and security to embedded devices in automotive, medical, and industrial sectors.

[Read More![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/67ee4d7596311684a7a1a95a_xynrqysiccm914h50n.svg)](/resource/how-we-taught-our-platform-to-understand-rtos-firmware)

[](/resource/how-we-taught-our-platform-to-understand-rtos-firmware)

![Security Advisory: Remote Code Execution on Diviotec IP Camera \(CVE-2025-5113\)](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/683d4ad4919020daef44c5cf_Remote-Code-Execution-on-Diviotec-IP-Camera.jpg)

Research

Jun 3, 2025

10

min read

### Security Advisory: Remote Code Execution on Diviotec IP Camera (CVE-2025-5113)

Explore ONEKEY Research Lab's security advisory detailing a critical vulnerability in Diviotec IP Cameras. Learn about the risks and recommended actions.

[Read More![](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0cd/67ee4d7596311684a7a1a95a_xynrqysiccm914h50n.svg)](/resource/security-advisory-remote-code-execution-on-diviotec-ip-camera-cve-2025-5113)

[](/resource/security-advisory-remote-code-execution-on-diviotec-ip-camera-cve-2025-5113)

## Ready to automate your Product Cybersecurity & Compliance?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)
