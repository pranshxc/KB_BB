---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-27_site-isolation-bypass-via-chrome-extension.md
original_filename: 2019-11-27_site-isolation-bypass-via-chrome-extension.md
title: Site Isolation bypass via Chrome extension
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 214c5a0564e5c5a7b1fb75eeeda19d00f0cf27ea2c7e7dcb99bc9ae928119b7c
text_sha256: 5deac3909adbfbfb6917f7bbe9762ec4d2b40b769a9ac695231de9da3bb1d5d3
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Site Isolation bypass via Chrome extension

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-27_site-isolation-bypass-via-chrome-extension.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `214c5a0564e5c5a7b1fb75eeeda19d00f0cf27ea2c7e7dcb99bc9ae928119b7c`
- Text SHA256: `5deac3909adbfbfb6917f7bbe9762ec4d2b40b769a9ac695231de9da3bb1d5d3`


## Content

---
title: "Site Isolation bypass via Chrome extension"
page_title: "Site Isolation bypass via Chrome extension | Anthony Weems"
url: "https://lf.lc/vrp/145304705/"
final_url: "https://amlw.dev/vrp/145304705/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["Site Isolation bypass", "Browser hacking"]
bounty: "3,133.70"
publication_date: "2019-11-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4915
---

#  Site Isolation bypass via Chrome extension 

November 27, 2019

### Vulnerability Details#

This vulnerability assumes a compromise of the renderer process as described in this post:

<https://groups.google.com/a/chromium.org/forum/#!msg/chromium-extensions/0ei-UCHNm34/IDaXwQhzBAAJ>

From a compromised renderer process, we can send a message to the extension background script (`chext_backgroundpage.js`) and break site isolation by triggering a POST request with credentials to an arbitrary origin, with arbitrary headers, and the ability to read the response.

Steps to reproduce:

  1. Install the Google Input Tools extension: <https://chrome.google.com/webstore/detail/google-input-tools/mclfklkfljcocdinagocijmpgbhab>
  2. Visit an “attacker” domain (e.g. <https://example.org>) and open DevTools
  3. Simulate compromise of renderer process and select the Google Input Tools content script from the scope dropdown.
  4. Execute the following JavaScript from the content script (part of the renderer) and observe the response logged:

  
  
  chrome.runtime.sendMessage({
  sq: true,
  url: "@mail.google.com/mail/u/0/",
  hd: {
  "x-arbitrary": "header"
  }
  }, function(x) { console.log(x); })
  

**Content script showing cross-origin response reading:** ![Content script showing cross-origin response reading](/assets/vrp/145304705-content-script.png)

**HTTP request sent by extension:** ![HTTP request sent by extension](/assets/vrp/145304705-http-request.png)

Browser: Google Chrome 78.0.3904.108  
Extension version: 5.9.0.0

### Attack Scenario#

An attacker that compromises the renderer process can abuse this vulnerability to break site isolation and read cross-origin responses. The request must be a POST request to an HTTPS resource, but the attacker can set any headers they like, and cookies are sent by default.

### Timeline#

  * 2019-11-27: Issue reported to Google VRP
  * 2019-11-28: Issue triaged
  * 2019-11-28: Discussed reproducibility with Google
  * 2019-12-15: Internal bug report filed
  * 2019-12-28: Issue fixed
  * 2020-01-07: VRP issued reward ($3133.70)
