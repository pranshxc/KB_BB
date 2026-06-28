---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-21_clamav-critical-patch-review.md
original_filename: 2023-02-21_clamav-critical-patch-review.md
title: ClamAV Critical Patch Review
category: documents
detected_topics:
- command-injection
- supply-chain
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: d2e8ffc0bd5a78cdad4f5f31a564aaa8b08d531ba1f930845e32e2401ffb307f
text_sha256: a2206506468d97ed1dc09dfd5de019dfb958ebd1fe5dddb36cc31421f128f3a5
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# ClamAV Critical Patch Review

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-21_clamav-critical-patch-review.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `d2e8ffc0bd5a78cdad4f5f31a564aaa8b08d531ba1f930845e32e2401ffb307f`
- Text SHA256: `a2206506468d97ed1dc09dfd5de019dfb958ebd1fe5dddb36cc31421f128f3a5`


## Content

---
title: "ClamAV Critical Patch Review"
page_title: "ClamAV Critical Patch Review | ONEKEY Research | Research | ONEKEY"
url: "https://onekey.com/blog/clamav-critical-patch-review/"
final_url: "https://www.onekey.com/resource/clamav-critical-patch-review"
authors: ["ONEKEY (@onekey_sec)"]
programs: ["ClamAV"]
bugs: ["RCE", "Memory corruption", "Buffer Overflow", "XXE", "Security code review"]
publication_date: "2023-02-21"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1502
---

[Resources](/resources)

>

[Research](/resources/research)

>

ClamAV Critical Patch Review

# ClamAV Critical Patch Review

![ClamAV Critical Patch Review](https://cdn.prod.website-files.com/66e0617dd66a9d24cea2d0d8/671b8234692550f5d60744cd_6712aeab38ffa37f04df5ba4_16.jpeg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

February 20, 2023

7

min read

TablE of contents

Example H2

## READY TO UPGRADE YOUR RISK MANAGEMENT?

Make cybersecurity and compliance efficient and effective with ONEKEY.

[See it in Action](/book-a-demo)

## Introduction

[ClamAV](https://www.clamav.net/) released a [critical patch](https://blog.clamav.net/2023/02/clamav-01038-01052-and-101-patch.html) a few days ago with fixes for two vulnerabilities reported by [Simon Scannell](https://twitter.com/scannell_simon):

  * **[CVE-2023-20032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20032)** : Fixed a possible remote code execution vulnerability in the HFS+ file parser. The issue affects versions 1.0.0 and earlier, 0.105.1 and earlier, and 0.103.7 and earlier.

  * **[CVE-2023-20052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20052)** : Fixed a possible remote information leak vulnerability in the DMG file parser. The issue affects versions 1.0.0 and earlier, 0.105.1 and earlier, and 0.103.7 and earlier.

The description of those bugs got our attention since we have format handlers in [unblob](https://unblob.org/) for both [DMG](https://github.com/onekey-sec/unblob/blob/main/unblob/handlers/archive/dmg.py) and HFS+. We therefore decided to spend some time trying to understand them and learn if we may be affected by similar bugs.

To do so, we performed patch diffing by comparing ClamAV version 1.0.0 and 1.0.1, downloaded from their [release page](https://github.com/Cisco-Talos/clamav/releases) on Github. The fix is not yet visible on their git history so we had to do it manually.

## CVE-2023-20052

The first bug, CVE-2023-20052, is fixed with this patch:
  
  
  210,211c210
  < /* XML_PARSE_NOENT | XML_PARSE_NONET | XML_PARSE_COMPACT */
  < #define DMG_XML_PARSE_OPTS ((1 << 1 | 1 << 11 | 1 << 16) | CLAMAV_MIN_XMLREADER_FLAGS)
  ---
  > #define DMG_XML_PARSE_OPTS ((XML_PARSE_NONET | XML_PARSE_COMPACT) | CLAMAV_MIN_XMLREADER_FLAGS)

The fix simply removes the `XML_PARSE_NOENT` flag from the libxml2 parsing options. This flag controls whether or not the parser is allowed to perform entity substitutions and can lead to XML External Entity Injection (XXE) if left enabled.

This is a very common mistake, especially with a counter-intuitive name like "NOENT" [introduced in 2016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-9318).

### Exploitation Strategy

DMG files are composed of a "Data fork" containing disk blocks, followed by a [Property List](https://en.wikipedia.org/wiki/Property_list) and a trailer. Here's an excerpt from our DMG handler in unblob with some nice ASCII art:
  
  
  # NOTE: the koly block is a trailer
  # ┌─────────────┐ │
  # │Data fork  │ │DataForkLength
  # │contains  │ │
  # │disk blocks  │ │
  # │  │ │
  # │  │ ▼
  # ├─────────────┤ │
  # │XML plist  │ │XMLLength
  # ├─────────────┤ ▼
  # │koly trailer │
  # └─────────────┘
  #

To exploit this vulnerability, you would need to place your malicious XXE payload within the property list to make libxml2 substitute and resolve external entities.

### Exploitation Limitations

Since the `XML_PARSE_NONET` flag is set, the parser will not be able to establish outbound connections. This means that exfiltrating local file content with this bug is not possible. This is the error message that you get when you try anyway:
  
  
  clamscan ../../samples/malicious.dmg 
  Loading:  16s, ETA:  0s [========================>]  8.65M/8.65M sigs  
  Compiling:  3s, ETA:  0s [========================>]  41/41 tasks 
  
  I/O error : Attempt to load network entity http://10.0.2.15/malicious.dtd
  /home/quentin/research/clamav/samples/malicious.dmg: OK
  
  ----------- SCAN SUMMARY -----------
  Known viruses: 8653236
  Engine version: 1.0.0
  Scanned directories: 0
  Scanned files: 1
  Infected files: 0
  Data scanned: 2.00 MB
  Data read: 0.02 MB (ratio 127.75:1)
  Time: 21.642 sec (0 m 21 s)
  Start Date: 2023:02:20 17:14:15
  End Date:  2023:02:20 17:14:36

At this point, it is still unclear how one can leak content remotely with this bug, but the investigation is ongoing. We're exploring two ideas at the moment: verbose logging and substituted XML content being written to temporary files.

Edit 21/02/2023: it's possible to leak local files if the binary runs with `--debug` enabled. In the excerpt below we make it dump the content of `/etc/passwd` through XXE:
  
  
  clamscan --debug malicious.dmg
  --snip--
  LibClamAV debug: clean_cache_add: f7e8ac0c33c257d878344560fcc78d40 (level 0)
  LibClamAV debug: cli_scandmg: Matched blkx
  LibClamAV debug: cli_scandmg: wanted blkx, text value is root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  bin:x:2:2:bin:/bin:/usr/sbin/nologin
  sys:x:3:3:sys:/dev:/usr/sbin/nologin
  sync:x:4:65534:sync:/bin:/bin/sync
  --snip--

## CVE-2023-20032

This bug is a heap buffer overflow affecting the `hfsplus_fetch_node` function. CalmAV fixed it by expanding the function signature with a `buffSize` integer value, which is used later in the code to perform a size check.
  
  
  // BEFORE
  static cl_error_t hfsplus_fetch_node(cli_ctx *ctx, hfsPlusVolumeHeader *volHeader, hfsHeaderRecord *catHeader,
  hfsHeaderRecord *extHeader, hfsPlusForkData *catFork, uint32_t node, uint8_t *buff)
  
  // AFTER
  static cl_error_t hfsplus_fetch_node(cli_ctx *ctx, hfsPlusVolumeHeader *volHeader, hfsHeaderRecord *catHeader,
  hfsHeaderRecord *extHeader, hfsPlusForkData *catFork, uint32_t node, uint8_t *buff, size_t buffSize);

Additionally, a size check within the function body (line 89 to 92) was included:
  
  
  /* Fetch a node's contents into the buffer */
  static cl_error_t hfsplus_fetch_node(cli_ctx *ctx, hfsPlusVolumeHeader *volHeader, hfsHeaderRecord *catHeader,
  hfsHeaderRecord *extHeader, hfsPlusForkData *catFork, uint32_t node, uint8_t *buff,
  size_t buffSize)
  {
  bool foundBlock = false;
  uint64_t catalogOffset;
  uint32_t startBlock, startOffset;
  uint32_t endBlock, endSize;
  uint32_t curBlock;
  uint32_t extentNum = 0, realFileBlock;
  uint32_t readSize;
  size_t fileOffset = 0;
  uint32_t searchBlock;
  uint32_t buffOffset = 0;
  
  UNUSEDPARAM(extHeader);
  
  /* Make sure node is in range */
  if (node >= catHeader->totalNodes) {
  cli_dbgmsg("hfsplus_fetch_node: invalid node number " STDu32 "\n", node);
  return CL_EFORMAT;
  }
  
  /* Need one block */
  /* First, calculate the node's offset within the catalog */
  catalogOffset = (uint64_t)node * catHeader->nodeSize;
  /* Determine which block of the catalog we need */
  startBlock  = (uint32_t)(catalogOffset / volHeader->blockSize);
  startOffset = (uint32_t)(catalogOffset % volHeader->blockSize);
  endBlock  = (uint32_t)((catalogOffset + catHeader->nodeSize - 1) / volHeader->blockSize);
  endSize  = (uint32_t)(((catalogOffset + catHeader->nodeSize - 1) % volHeader->blockSize) + 1);
  cli_dbgmsg("hfsplus_fetch_node: need catalog block " STDu32 "\n", startBlock);
  if (startBlock >= catFork->totalBlocks || endBlock >= catFork->totalBlocks) {
  cli_dbgmsg("hfsplus_fetch_node: block number invalid!\n");
  return CL_EFORMAT;
  }
  
  for (curBlock = startBlock; curBlock <= endBlock; ++curBlock) {
  
  foundBlock  = false;
  searchBlock = curBlock;
  /* Find which extent has that block */
  for (extentNum = 0; extentNum < 8; extentNum++) {
  hfsPlusExtentDescriptor *currExt = &(catFork->extents[extentNum]);
  
  /* Beware empty extent */
  if ((currExt->startBlock == 0) || (currExt->blockCount == 0)) {
  cli_dbgmsg("hfsplus_fetch_node: extent " STDu32 " empty!\n", extentNum);
  return CL_EFORMAT;
  }
  /* Beware too long extent */
  if ((currExt->startBlock & 0x10000000) && (currExt->blockCount & 0x10000000)) {
  cli_dbgmsg("hfsplus_fetch_node: extent " STDu32 " illegal!\n", extentNum);
  return CL_EFORMAT;
  }
  /* Check if block found in current extent */
  if (searchBlock < currExt->blockCount) {
  cli_dbgmsg("hfsplus_fetch_node: found block in extent " STDu32 "\n", extentNum);
  realFileBlock = currExt->startBlock + searchBlock;
  foundBlock  = true;
  break;
  } else {
  cli_dbgmsg("hfsplus_fetch_node: not in extent " STDu32 "\n", extentNum);
  searchBlock -= currExt->blockCount;
  }
  }
  
  if (foundBlock == false) {
  cli_dbgmsg("hfsplus_fetch_node: not in first 8 extents\n");
  cli_dbgmsg("hfsplus_fetch_node: finding this node requires extent overflow support\n");
  return CL_EFORMAT;
  }
  
  /* Block found */
  if (realFileBlock >= volHeader->totalBlocks) {
  cli_dbgmsg("hfsplus_fetch_node: block past end of volume\n");
  return CL_EFORMAT;
  }
  fileOffset = realFileBlock * volHeader->blockSize;
  readSize  = volHeader->blockSize;
  
  if (curBlock == startBlock) {
  fileOffset += startOffset;
  } else if (curBlock == endBlock) {
  readSize = endSize;
  }
  
  if ((buffOffset + readSize) > buffSize) {
  cli_dbgmsg("hfsplus_fetch_node: Not enough space for read\n");
  return CL_EFORMAT;
  }
  
  if (fmap_readn(ctx->fmap, buff + buffOffset, fileOffset, readSize) != readSize) {
  cli_dbgmsg("hfsplus_fetch_node: not all bytes read\n");
  return CL_EFORMAT;
  }
  buffOffset += readSize;
  }
  
  return CL_CLEAN;
  }
  

Without this protection, the call to `fmap_readn` on line 94 could lead to a heap buffer overflow. The function simply reads (`readSize`) bytes from (`ctx->fmap`) fmap at (`fileOffset`) offset into (`buff+buffOffset`) destination buffer.

The destination buffer is a node allocated in `hfsplus_walk_catalog` like this:
  
  
  static cl_error_t hfsplus_walk_catalog(cli_ctx *ctx, hfsPlusVolumeHeader *volHeader, hfsHeaderRecord *catHeader,  
  hfsHeaderRecord *extHeader, hfsHeaderRecord *attrHeader, const char *dirname)  
  {
  // ---snip---
  uint8_t *nodeBuf  = NULL;
  nodeLimit = MIN(catHeader->totalNodes, HFSPLUS_NODE_LIMIT);
  thisNode  = catHeader->firstLeafNode;
  nodeSize  = catHeader->nodeSize;
  nodeBuf = cli_malloc(nodeSize);
  // --snip--

`cli_malloc` is a simple wrapper around `malloc `with some sanity checks:
  
  
  void *cli_malloc(size_t size)
  {
  void *alloc;
  
  
  if(!size || size > CLI_MAX_ALLOCATION) {
  cli_errmsg("cli_malloc(): Attempt to allocate %lu bytes. Please report to http://bugs.clamav.net\n", (unsigned long int) size);
  return NULL;
  }
  
  alloc = malloc(size);
  
  if(!alloc) {
  cli_errmsg("cli_malloc(): Can't allocate memory (%lu bytes).\n", (unsigned long int) size);
  perror("malloc_problem");
  return NULL;
  } else return alloc;
  }

This vulnerability provides rather strong exploitation primitive as it allows the attacker to control:

  * the **size of the allocation** via the `nodeSize` value of headers within the Catalog or Attribute file structures;
  * the **source of the copied chunk** is controllable through the `blockSize` value of the HFS+ volume header, which is used to calculate `fileOffset`;
  * the **size of the copied chunk** (`readSize`) is controllable through the `blockSize` value of the HFS+ volume header

More details about the HFS+ format can be found on Apple's website at <https://developer.apple.com/library/archive/technotes/tn/tn1150.html>

### Exploitation Strategy

We have yet to explore the actual exploitation on a default installation of ClamAV. Please note that `clamscan `and `libclamav `are hardened on modern Linux distros (NX, stack canary, PIE, fortify, partial RELRO). An attacker would - at the very least - need to find an information leak (maybe by exploiting the XXE ?) on top of finding interesting objects to overwrite on the heap in order to take control of process execution.

Folks at Qualys recently [demonstrated](https://seclists.org/oss-sec/2023/q1/92) they could exploit a double free vulnerability affecting OpenSSH on OpenBSD, so I'm betting someone out there can definitely write an exploit for this ClamAV vuln.

## Key Takeaways

As already demonstrated in [our previous blog posts](https://b1eyc.myrdbx.io/blog/security-advisory-remote-command-execution-in-binwalk/), file format parsing is a difficult and complex endeavor. The R&D team at ONEKEY always keeps an eye on recently published vulnerabilities and looks into them to check if there are new things to learn and adopt in our own products such as unblob.

Speaking of unblob, we do not parse the DMG property list XML structure and we default to `defusedxml` for any XML parsing needs. So, we're safe on that side - at least for now. Additionally, we rely on 7zip to perform extraction of DMG and HFS, which does not seem to be affected by similar memory corruption in the HFS catalog parsing code. 

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
