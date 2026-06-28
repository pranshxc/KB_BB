---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-23_electronizing-macos-privacy.md
original_filename: 2024-01-23_electronizing-macos-privacy.md
title: ELECTRONizing macOS privacy
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 63ae047f38ff1fe178ea08f9098bd846b725e5431a20d7f0fc12b272eea8b942
text_sha256: ac29ee6f455d810eeadca176fab99a1c1930beaa48f1b3d15049496ce9f33e63
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# ELECTRONizing macOS privacy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-23_electronizing-macos-privacy.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `63ae047f38ff1fe178ea08f9098bd846b725e5431a20d7f0fc12b272eea8b942`
- Text SHA256: `ac29ee6f455d810eeadca176fab99a1c1930beaa48f1b3d15049496ce9f33e63`


## Content

---
title: "ELECTRONizing macOS privacy"
url: "https://wojciechregula.blog/post/electroniz3r/"
final_url: "https://wojciechregula.blog/post/electroniz3r/"
authors: ["Wojciech Reguła (@_r3ggi)"]
programs: ["Apple (macOS)"]
bugs: ["TCC bypass", "Electron", "Local Privilege Escalation"]
publication_date: "2024-01-23"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 509
---

### Publications

This research has been presented at:

  * DEF CON 31 - [ELECTRONizing macOS privacy](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/Wojciech%20Regu%C5%82a%20-%20ELECTRONizing%20macOS%20privacy%20-%20a%20new%20weapon%20in%20your%20red%20teaming%20armory.pdf)
  * Objective By the Sea - [ELECTRONizing macOS Privacy - a New Weapon in Your Red Teaming Armory](https://objectivebythesea.org/v6/talks/OBTS_v6_wRegula.pdf)

### The backstory

In 2019 I wrote a blog post about injecting code to Electron apps to impersonate their TCC permissions. The trick was really simple because at that time the only thing an attacker had to do was to modify one of the Electron app’s HTML files or the whole ASAR. In macOS Ventura, this trick stopped working as the app protection mechanism has been introduced.

![app protection](/images/2024/01/privacy-security.png)

This mechanism broke my simple Electron injection technique so it was time to figure out something new…

### TCC inheritance problem

TCC is now a much bigger mechanism than it was before. As we all know, complicity usually indicates vulnerabilities. One such example is the inheritance of privacy privileges (look at: [CVE-2020-10008](https://wojciechregula.blog/post/bypass-tcc-via-privileged-helpers-aka-cve-2020-10008/)). What happens when an entitled process spawns a child that wants to access something? Or if a process has a completely separate privileged helper that wants to access your desktop for example? Who should be then responsible for that action - the parent or the child?

As I’m not going to update this post in the future, please keep in mind that the TCC inheritance may change in the future. On macOS Sonoma, generally speaking, situation looks as follows:

  * When an app has private TCC entitlements – its permissions are not inherited by other apps they spawn
  * When an app has TCC permission granted by the user (User clicked “OK” in the prompt) - its permissions are inherited

Electron apps are in the second group so if we make our target Electron app spawn a malicious process - we would be able to inherit its TCC permissions.

### `--inspect` flag for the rescue

Turns out that Electron has a debugging feature that we may trigger by setting a `--inspect` flag. Before we do so it’s important to verify if the targeted app respects it:
  
  
  $ npx @electron/fuses read --app /Applications/Test.app
  Analyzing app: Test.app
  Fuse Version: v1
  RunAsNode is Enabled
  EnableCookieEncryption is Disabled
  EnableNodeOptionsEnvironmentVariable is Enabled
  EnableNodeCliInspectArguments is Enabled
  EnableEmbeddedAsarIntegrityValidation is Disabled
  OnlyLoadAppFromAsar is Disabled
  LoadBrowserProcessSpecificV8Snapshot is Disabled
  

If `EnableNodeCliInspectArguments` is enabled it means that we can use the `--inspect` flag to turn on DevTools API available on a local web socket. Accessing this API with a chromium-based browser allows us to execute arbitrary JavaScript code in the context of the targeted Electron app. Using the following JavaScript code we can spawn a child process that will inherit our Electron’s app TCC permissions:
  
  
  const exec = require('child_process').exec;
  exec("/System/Applications/Calculator.app/Contents/MacOS/Calculator");
  

You may ask what if `EnableNodeCliInspectArguments` is disabled? - Well, [injecting to old vulnerable versions](https://wojciechregula.blog/post/macos-red-teaming-bypass-tcc-with-old-apps/) still works.

### electroniz3r

![electroniz3r](/images/2024/01/electroniz3r.png)

I decided to write a tool that automates the above-mentioned steps and has some predefined JavaScript scripts embedded to make exploitation even easier. It’s called electroniz3r and it is available on my Github - <https://github.com/r3ggi/electroniz3r>.

Take a look at the demos below.

**Teams vs electroniz3r**

**Visual Studio Code vs electroniz3r**
