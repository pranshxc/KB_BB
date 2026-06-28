---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-04_poc.md
original_filename: 2022-04-04_poc.md
title: PoC
category: documents
detected_topics:
- access-control
- command-injection
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- supply-chain
language: en
raw_sha256: 3b8af35a0c3a0da7a6697dcd477eed6631785621857e2f2414a090a6891ba69d
text_sha256: 8714534c370f4a11253df93a11db41b824d3bdbf1796401d426b9cad31f65ac9
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# PoC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-04_poc.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `3b8af35a0c3a0da7a6697dcd477eed6631785621857e2f2414a090a6891ba69d`
- Text SHA256: `8714534c370f4a11253df93a11db41b824d3bdbf1796401d426b9cad31f65ac9`


## Content

---
title: "PoC"
page_title: "GitHub - jhftss/CVE-2022-22639: CVE-2022-22639: Get a Root Shell on macOS Monterey · GitHub"
url: "https://github.com/jhftss/CVE-2022-22639"
final_url: "https://github.com/jhftss/CVE-2022-22639"
authors: ["Mickey Jin (@patch1t)"]
programs: ["Apple"]
bugs: ["Local Privilege Escalation"]
publication_date: "2022-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2751
---

# Details

See Blog:

<https://www.trendmicro.com/en_us/research/22/d/macos-suhelper-root-privilege-escalation-vulnerability-a-deep-di.html>

# Exploitation of CVE-2022-22639

  1. Compile with command: `clang exploit.m -o /tmp/exploit -framework Foundation -fobjc-arc -fobjc-link-runtime /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate.tbd`
  2. Unzip **InstallAssistant.gz** to `/tmp` folder
  3. run `/tmp/exploit`

# Demo

<https://www.youtube.com/watch?v=-vbkTLHh874>
