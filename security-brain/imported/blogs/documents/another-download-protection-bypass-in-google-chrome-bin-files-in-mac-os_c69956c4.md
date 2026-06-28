---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-02_another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os.md
original_filename: 2019-07-02_another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os.md
title: Another Download Protection Bypass in Google Chrome – BIN files in Mac OS
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: c69956c4df0cf8e9f2bacc3c005e66c4065da774550582cb48074dc33c625eef
text_sha256: 6f8c76c132d278eb9e1c923cd3ab15365d9c284e3d99a4ec510b2a0c1dbd4b17
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Another Download Protection Bypass in Google Chrome – BIN files in Mac OS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-02_another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c69956c4df0cf8e9f2bacc3c005e66c4065da774550582cb48074dc33c625eef`
- Text SHA256: `6f8c76c132d278eb9e1c923cd3ab15365d9c284e3d99a4ec510b2a0c1dbd4b17`


## Content

---
title: "Another Download Protection Bypass in Google Chrome – BIN files in Mac OS"
page_title: "Another Download Protection Bypass in Google Chrome – BIN files in Mac OS | Nightwatch Cybersecurity"
url: "https://wwws.nightwatchcybersecurity.com/2019/07/02/another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os/"
final_url: "https://wwws.nightwatchcybersecurity.com/2019/07/02/another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os/"
authors: ["Nightwatch Cybersecurity (@nightwatchcyber)"]
programs: ["Google"]
bugs: ["Browser hacking"]
bounty: "1,000"
publication_date: "2019-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5172
---

# Another Download Protection Bypass in Google Chrome – BIN files in Mac OS

[July 2, 2019](https://wwws.nightwatchcybersecurity.com/2019/07/02/another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os/) [nightwatchcyber](https://wwws.nightwatchcybersecurity.com/author/nightwatchcyber/) [Advisories](https://wwws.nightwatchcybersecurity.com/category/advisories/)[chrome](https://wwws.nightwatchcybersecurity.com/tag/chrome/), [google](https://wwws.nightwatchcybersecurity.com/tag/google/)

## Summary

BIN files on Mac OS bypass the download protection mechanism offered by Google’s Chrome browser. This was reported and fixed by the vendor, then pushed via a component update to users in March 2019.

## Background

The Chrome and Chromium browsers are an open-source based web browser offered by Google. Among it’s features it includes a safety feature that detects unsafe downloads to protect the user. This feature works in multiple ways but is controlled via a file in Chrome’s source code ([“download_file_types.asciipb”](https://cs.chromium.org/chromium/src/chrome/browser/resources/safe_browsing/download_file_types.asciipb)). Additional background details can be found [in our earlier post](https://wwws.nightwatchcybersecurity.com/2018/02/26/multiple-instances-of-download-protection-bypass-in-googles-chrome/). [We had previously reported](https://wwws.nightwatchcybersecurity.com/2018/02/26/multiple-instances-of-download-protection-bypass-in-googles-chrome/) multiple instances of download protection bypass in Chrome to the vendor – this post describes another one that was found more recently.

## Details

The BIN file extension on Mac OS is opened by default via the Archive Mounter utility. That means that you can take a compressed file such as ZIP and rename it as a BIN file. When downloaded via Chrome, the browser will not do safety checks on this file yet the file can carry dangerous content. The root cause is the fact that the BIN file type is whitelisted as being not dangerous. This issue only affects users on Mac OS.

The vendor fixed the issue and pushed it via a component update. Users do not need to update the actual browser – as long as connectivity exists for component updates, this should be fixed automatically.

## References

Chrome Bug Report: [933637](https://bugs.chromium.org/p/chromium/issues/detail?id=933637)

## Bounty Information

This issue qualified for the Chrome Rewards security bounty program and a bounty has been paid.

## Credits

Advisory written by Y. Shafranovich.

## Timeline Summary

2019-02-19: Report submitted  
2019-02-27: Vendor fix is committed  
2019-03-25: Vendor fix is released to users  
2019-07-02: Public disclosure

### Share this:

  * [ Share on X (Opens in new window) X ](https://wwws.nightwatchcybersecurity.com/2019/07/02/another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://wwws.nightwatchcybersecurity.com/2019/07/02/another-download-protection-bypass-in-google-chrome-bin-files-in-mac-os/?share=facebook)
  * 

Like Loading...
