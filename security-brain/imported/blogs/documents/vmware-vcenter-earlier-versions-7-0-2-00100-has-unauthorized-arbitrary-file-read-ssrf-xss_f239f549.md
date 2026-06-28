---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-30_vmware-vcenter-earlier-versions-70200100-has-unauthorized-arbitrary-file-read-ss.md
original_filename: 2021-11-30_vmware-vcenter-earlier-versions-70200100-has-unauthorized-arbitrary-file-read-ss.md
title: VMware vCenter earlier versions (7.0.2.00100) has unauthorized arbitrary file
  read + ssrf + xss vulnerability
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- path-traversal
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- path-traversal
- api-security
- supply-chain
language: en
raw_sha256: f239f54927af9345dd54b1fce740fe437060a560370ad2db04279e87e1dd37d1
text_sha256: 13b0b433982858dcc1f197ba0a32a626dba1272e092ba83efdd251dda2e6ce02
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# VMware vCenter earlier versions (7.0.2.00100) has unauthorized arbitrary file read + ssrf + xss vulnerability

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-30_vmware-vcenter-earlier-versions-70200100-has-unauthorized-arbitrary-file-read-ss.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, path-traversal, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `f239f54927af9345dd54b1fce740fe437060a560370ad2db04279e87e1dd37d1`
- Text SHA256: `13b0b433982858dcc1f197ba0a32a626dba1272e092ba83efdd251dda2e6ce02`


## Content

---
title: "VMware vCenter earlier versions (7.0.2.00100) has unauthorized arbitrary file read + ssrf + xss vulnerability"
page_title: "GitHub - l0ggg/VMware_vCenter: VMware vCenter 7.0.2.00100 unauth Arbitrary File Read + SSRF + Reflected XSS · GitHub"
url: "https://github.com/l0ggg/VMware_vCenter"
final_url: "https://github.com/l0ggg/VMware_vCenter"
authors: ["Khoa Dinh (@_l0gg)"]
programs: ["VMware"]
bugs: ["LFI", "SSRF", "XSS", "Arbitrary file read"]
publication_date: "2021-11-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3129
---

# VMware vCenter earlier versions (7.0.2.00100) has unauthorized arbitrary file read + ssrf + xss vulnerability

## POC

https://{vCenterserver}/ui/vcav-bootstrap/rest/vcav-providers/provider-logo?url={url}

File read:

[![](/l0ggg/VMware_vCenter/raw/main/file_read.PNG)](/l0ggg/VMware_vCenter/blob/main/file_read.PNG)

SSRF + XSS:

[![](/l0ggg/VMware_vCenter/raw/main/xss.PNG)](/l0ggg/VMware_vCenter/blob/main/xss.PNG)

## vulnerable code:

/etc/vmware/vsphere-ui/cm-service-packages/com.vmware.cis.vsphereclient.plugin/com.vmware.h4.vsphere.client-0.4.1.0/plugins/h5-vcav-bootstrap-service.jar

com.vmware.h4.vsphere.ui.bootstrap.controller.ProvidersController.getProviderLogo()

[![](/l0ggg/VMware_vCenter/raw/main/code.PNG)](/l0ggg/VMware_vCenter/blob/main/code.PNG)

Tested on vCenter 7.0.2.00100, not knowing the exact affected version range or cve id
