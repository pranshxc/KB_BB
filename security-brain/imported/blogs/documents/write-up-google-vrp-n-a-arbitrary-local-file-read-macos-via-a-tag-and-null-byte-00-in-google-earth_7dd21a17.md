---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-14_write-up-google-vrp-na-arbitrary-local-file-read-macos-via-x3cx61x3e-tag-and-nul.md
original_filename: 2021-10-14_write-up-google-vrp-na-arbitrary-local-file-read-macos-via-x3cx61x3e-tag-and-nul.md
title: 'Write Up – Google VRP N/A: Arbitrary Local File Read (Macos) Via &#x3c;&#x61;&#x3e;
  Tag And Null Byte (&#x25;&#x30;&#x30;) In Google Earth Pro Desktop App'
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 7dd21a171751b7103d4ee3a1435817dcd3b51d11c99a534a0be7164d45dcdd62
text_sha256: a0eff7da26f27190305ccc5c23ed6e666ece1f705cf7cc98727a2c263bffd705
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up – Google VRP N/A: Arbitrary Local File Read (Macos) Via &#x3c;&#x61;&#x3e; Tag And Null Byte (&#x25;&#x30;&#x30;) In Google Earth Pro Desktop App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-14_write-up-google-vrp-na-arbitrary-local-file-read-macos-via-x3cx61x3e-tag-and-nul.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `7dd21a171751b7103d4ee3a1435817dcd3b51d11c99a534a0be7164d45dcdd62`
- Text SHA256: `a0eff7da26f27190305ccc5c23ed6e666ece1f705cf7cc98727a2c263bffd705`


## Content

---
title: "Write Up – Google VRP N/A: Arbitrary Local File Read (Macos) Via &#x3c;&#x61;&#x3e; Tag And Null Byte (&#x25;&#x30;&#x30;) In Google Earth Pro Desktop App"
page_title: "GOOGLE VRP N/A – ARBITRARY LOCAL FILE READ (MACOS) VIA <A> TAG AND NULL BYTE IN GOOGLE EARTH PRO – @omespino"
url: "https://omespino.com/write-up-google-vrp-n-a-arbitrary-local-file-read-macos-via-a-tag-and-null-byte-in-google-earth-pro-desktop-app/"
final_url: "https://omespino.com/write-up-google-vrp-n-a-arbitrary-local-file-read-macos-via-a-tag-and-null-byte-in-google-earth-pro-desktop-app/"
authors: ["Omar Espino (@omespino)"]
programs: ["Google"]
bugs: ["Local File Read"]
publication_date: "2021-10-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3239
---

DESKTOPN/A[October 2021](/write-up-google-vrp-n-a-arbitrary-local-file-read-macos-via-a-tag-and-null-byte-in-google-earth-pro-desktop-app/)

# GOOGLE VRP N/A – ARBITRARY LOCAL FILE READ (MACOS) VIA <A> TAG AND NULL BYTE IN GOOGLE EARTH PRO

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a very short story about one of my last bugs, and how I managed to get an Arbitrary local macOS file read via <a> tag and null byte (%00) in Google Earth Pro Desktop app 

Extracted from Google VRP’s report: (the actual Google VRP report) 

Summary Arbitrary local file read (macOS) via <a> and null byte (%00) element in Google Earth Pro Desktop app  
  
Steps to reproduce: 

1.- Download and install the latest [ Google Earth Pro Desktop app for macOS (7.3.3.7786 64-bit)](https://www.google.com/intl/en/earth/versions/#download-pro)

2.- Open the Google Earth app and create a new Pin, add any name add click on add link, and paste this code in the white box
  
  
  <a href="file:///etc/passwd%00.html">passwd</a> 
  

and click OK button

3.- After Pin’s creation, in the left side pane Places, click in the hyperlink called **passwd** add see **/etc/passwd** file content

[![](/assets/images/2021/04/ge-lfd-macos.webp)](/assets/images/2021/04/ge-lfd-macos.webp)

4.- Profit

**PS. any attacker can read any file with file:/// schema and appending a null byte and dot HTML extension (%00.html)**

Attack scenario  
Any attacker can read arbitrary files on macOS through the Google Earth Pro Desktop app  

Report Timeline

Apr 17, 2021: Sent the report to Google VRP  
Apr 19, 2021: ![](/assets/images/2021/01/download-1.webp) Nice catch! Bug Accepted (P4 → P2)  
Apr 27, 2021: Got a message from Google that the issue does not meet the bar for a financial reward  
May 05, 2021: Got a message from Google that the issue report has been closed without providing a fix (Status Won’t fix)

Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-xss-stored-in-api-media-atlassian-com-via-doc-file-ios/)

[](/write-up-google-vrp-n-a-ssrf-bypass-with-quadzero-in-google-cloud-monitoring/)
