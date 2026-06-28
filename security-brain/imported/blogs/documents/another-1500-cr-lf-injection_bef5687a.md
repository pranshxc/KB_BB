---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-18_another-1500-crlf-injection.md
original_filename: 2024-08-18_another-1500-crlf-injection.md
title: 'Another 1500$: CR/LF Injection'
category: documents
detected_topics:
- command-injection
- file-upload
tags:
- imported
- documents
- command-injection
- file-upload
language: en
raw_sha256: bef5687adc8c2e5e67db9dd9b556161fcc0020912dc2caecb77031c5979402e4
text_sha256: cd597c56d6ec197249ab481483328384138b426894aa421d436a1d774cec9b75
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Another 1500$: CR/LF Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-18_another-1500-crlf-injection.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `bef5687adc8c2e5e67db9dd9b556161fcc0020912dc2caecb77031c5979402e4`
- Text SHA256: `cd597c56d6ec197249ab481483328384138b426894aa421d436a1d774cec9b75`


## Content

---
title: "Another 1500$: CR/LF Injection"
url: "https://medium.com/@a13h1/1500-cr-lf-injection-59152daaf413"
authors: ["Abhi Sharma (@a13h1_)"]
bugs: ["CRLF injection"]
bounty: "1,500"
publication_date: "2024-08-18"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 62
scraped_via: "browseros"
---

# Another 1500$: CR/LF Injection

Member-only story

Another 1500$: CR/LF Injection
Abhi Sharma
Follow
4 min read
·
Aug 17, 2024

203

Hi Everyone, How you all doing. Recently, while assessing the security of HuliaHub(Pseudonym of a private bbp), I found a critical CR/LF vulnerability. This marks my second CR/LF injection vulnerability found in this particular program within a month, highlighting the importance of rigorous security testing and patching.

Press enter or click to view image in full size

Understanding CR/LF (Carriage Return/Line Feed) Injection

CR/LF (Carriage Return/Line Feed) injection is a type of security vulnerability. CR/LF refers to a sequence of two ASCII control characters: Carriage Return (CR, ASCII code 13) and Line Feed (LF, ASCII code 10). CR/LF injection vulnerabilities occur when attackers insert CR/LF characters into input fields, parameters, file extensions or file uploads to manipulate application behavior. This can lead to exploits such as altering headers, injecting malicious code, or manipulating file content.

Discovery of the Vulnerability

The CR/LF vulnerability found in HuliaHub’s authentication mechanism allows attackers to manipulate the redirect URL parameter during user authentication. This manipulation involves injecting special characters (%0D%0A), commonly used to denote new lines in HTTP headers. This vulnerability enables attackers to perform malicious actions post-authentication.

Reconnaissance and Testing
