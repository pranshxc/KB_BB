---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-18_path-traversal-in-mobilesafari.md
original_filename: 2021-05-18_path-traversal-in-mobilesafari.md
title: Path Traversal in MobileSafari
category: documents
detected_topics:
- command-injection
- path-traversal
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- path-traversal
- mobile-security
- supply-chain
language: en
raw_sha256: 9a5cfd454dd9ae842f3c64dc5cd9fb00494556e6e52ab13c6578e8debd73a5d0
text_sha256: 8321352234121a4201b5a18f7bd32a8318d000eedaa9b4a1bc66cfdd2ae3c852
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Path Traversal in MobileSafari

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-18_path-traversal-in-mobilesafari.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `9a5cfd454dd9ae842f3c64dc5cd9fb00494556e6e52ab13c6578e8debd73a5d0`
- Text SHA256: `8321352234121a4201b5a18f7bd32a8318d000eedaa9b4a1bc66cfdd2ae3c852`


## Content

---
title: "Path Traversal in MobileSafari"
page_title: "[#0006] Path Traversal in MobileSafari | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0006"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0006"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Apple"]
bugs: ["Path traversal"]
publication_date: "2021-05-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3644
---

#0006  
Vendor: Apple  
Status: fixed  
Reported: Sep 20, 2020  
Disclosed: May 18, 2021 (240 days) 

# Path Traversal in MobileSafari

**Summary:**

I have found a path traversal issue in Safari, present in iOS 14.0. When saving a web page as PDF into Files, Safari uses the page’s `<title>` tag as a file name, without sanitising it first, leading to path traversal.

**Steps to reproduce:**

  1. Set up a webserver hosting this HTML file:

  
  
  <title>/../../Library/Preferences/</title>
  <h1>Hello world!</h1>
  

  2. Open the page in Safari
  3. Tap `Share`
  4. Tap `Options` -> Set `Send As` to `PDF` -> Tap the back arrow
  5. Tap `Save to Files`
  6. An extension-less file named `pdf` was created at `/private/var/mobile/Containers/Data/Application/[safari's UUID]/Library/Preferences/pdf`

This file was created by the `MobileSafari` process.

**Extras / limitations:**

  * If the `<title>` tag ends with a `/`, a file named `pdf` will be created.
  * If the `<title>` tag doesn’t end with a `/`, `.pdf` is always appended at the end of the file.
  * If the file to create already exists, a `-1` or `-2` (incremental number) will be added to the filename, before the first dot. (example: if `/Library/Preferences/com.apple.mobilesafari.plist.pdf` already exists, pressing `Save to Files` will create `/Library/Preferences/com-1.apple.mobilesafari.plist.pdf`)
  * If a file path outside the app folder is provided, a warning in the Console from the `kernel` process will show. e.g.: `Sandbox: MobileSafari(1756) deny(1) file-write-create /private/var/pdf`.

A malicious attack could may use this vulnerability to permanently crash Safari by creating a file which Safari is unable to parse.

As far as I know Safari can’t be deleted/reinstalled, so I’m not sure how to remove these test/malicious files from Safari’s filesystem.

Thank you,  
David

_This issue was fixed in[iOS/iPadOS 14.5](https://support.apple.com/en-us/HT212317) and in [watchOS 7.4](https://support.apple.com/en-us/HT212324)._
