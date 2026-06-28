---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_bugtales-unziploc-from-0-click-to-platform-compromise.md
original_filename: 2022-06-14_bugtales-unziploc-from-0-click-to-platform-compromise.md
title: '[BugTales] UnZiploc: From 0-click To Platform Compromise'
category: documents
detected_topics:
- command-injection
- access-control
- business-logic
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- access-control
- business-logic
- api-security
- mobile-security
language: en
raw_sha256: 6390b487baeb2747db2b0231f1acae55c76364c06002b3f8f006f460e22cacdd
text_sha256: 916adc9ff380b31c2a3fad4ac77de6abc061555a1c9bbb2dbd3c4cc25a38c9bc
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# [BugTales] UnZiploc: From 0-click To Platform Compromise

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_bugtales-unziploc-from-0-click-to-platform-compromise.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, business-logic, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `6390b487baeb2747db2b0231f1acae55c76364c06002b3f8f006f460e22cacdd`
- Text SHA256: `916adc9ff380b31c2a3fad4ac77de6abc061555a1c9bbb2dbd3c4cc25a38c9bc`


## Content

---
title: "[BugTales] UnZiploc: From 0-click To Platform Compromise"
page_title: "[BugTales] UnZiploc: From 0-click To Platform Compromise - taszk.io labs"
url: "https://labs.taszk.io/articles/post/unziploc/"
final_url: "https://labs.taszk.io/articles/post/unziploc/"
authors: ["Daniel Komaromy (@kutyacica)", "Lorant Szabo (@szabolor)", "Gyorgy Miru (@gymiru)"]
programs: ["Huawei"]
bugs: ["Memory corruption", "Logic flaw", "RCE", "Local Privilege Escalation"]
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2550
---

##  [[BugTales] UnZiploc: From 0-click To Platform Compromise](https://labs.taszk.io/articles/post/unziploc/)

__2022-06-14 __by Lorant Szabo __[Huawei](/articles/tags/huawei) [ota](/articles/tags/ota) [baseband](/articles/tags/baseband) [dma](/articles/tags/dma)

Recently we have disclosed new advisories related to the remote exploitation of Huawei smartphones.

The research that led to these findings was motivated by analyzing new interfaces for remote code execution on a mobile platform. After our work on exploiting Huawei’s Kirin via its baseband interface, we wanted to explore the possibilities of logic bugs as RCE vectors in a modern smartphone chipset, as opposed to memory corruption scenarios that are more common in public research. Logic bugs can be the most powerful because they have the potential to bypass almost all the exploit mitigations that are the typical focus these days, like ASLR, N^X, sandboxing parser code, etc.

Our research resulted in a 0-click remote code execution exploit. Demonstrating the usefulness of an exploit using only logic bugs, it worked without modification even on Huawei devices with Qualcomm Snapdragon chipsets! In addition, we chained together a few more logical bugs for further escalation, including getting code execution at TEE level.

The vulnerabilities we disclosed have all been reported to and patched by Huawei (see the advisories for the disclosure timelines).

The interested reader may find all the vulnerability details in our advisories:

[CVE-2021-40045: Huawei Recovery Update Zip Signature Verification Bypass](https://labs.taszk.io/blog/post/75_hw_eocd_sig/)

[CVE-2021-40055: Huawei OTA Insecure SSL Configuration Man-In-The-Middle Vulnerability](https://labs.taszk.io/blog/post/76_hw_hota_ssl/)

[CVE-2021-37107: Huawei Peripheral DMA Memory Access Permission Bypass](https://labs.taszk.io/blog/post/69_hw_peridma_tee/)

[CVE-2021-37109: Huawei Baseband MPU Security Protection Bypass via EDMA](https://labs.taszk.io/blog/post/73_hw_edma_mpu/)

[CVE-2021-37115: Huawei DMSS Memory Access Management Configuration Unathorized Rewrite Via ASP DMA](https://labs.taszk.io/blog/post/71_hw_aspdma_dmss/)

[CVE-2021-39986: Huawei Baseband Memory Access Permission Bypass And DMSS Memory Access Management Configuration Unathorized Rewrite Via LPMCU](https://labs.taszk.io/blog/post/72_hw_lpmcu_dmss/)

[CVE-2021-39991: Huawei DMSS Memory Access Management Configuration Unathorized Rewrite Via Peripheral DMA](https://labs.taszk.io/blog/post/70_hw_peridma_dmss/)

[CVE-2021-39992: Huawei Kernel Memory Access Permission Bypass via EDMA](https://labs.taszk.io/blog/post/74_hw_edma_modem/)

In addition, you can find a slidedeck of the UnZiploc research presentation on our [github](https://github.com/TaszkSecLabs/presentations/blob/main/unziploc.pdf). Last month we also had the opportunity to present this research at the [QSS](https://qct-qualcomm.secure.force.com/QCTConference/GenericSitePage?eventname=SecuritySummit&page=Presentations).

A video recording of the talk that we delivered is available [here](https://youtu.be/geqc6xQuy_o).
