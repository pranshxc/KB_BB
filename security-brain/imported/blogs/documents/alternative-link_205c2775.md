---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-23_alternative-link.md
original_filename: 2022-01-23_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- path-traversal
- command-injection
tags:
- imported
- documents
- path-traversal
- command-injection
language: en
raw_sha256: 205c27752b1ceb5f6a650f3ca70d15ebd376dd5fbc49def48dca83f4edbaa648
text_sha256: 3bcc0a9606afceb719ad59c8a7539049e11ca1344d7026314924395bf1329ad4
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-23_alternative-link.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `205c27752b1ceb5f6a650f3ca70d15ebd376dd5fbc49def48dca83f4edbaa648`
- Text SHA256: `3bcc0a9606afceb719ad59c8a7539049e11ca1344d7026314924395bf1329ad4`


## Content

---
title: "Alternative link"
page_title: "Path Traversal Paradise | Synack"
url: "https://www.synack.com/blog/path-traversal-paradise/"
final_url: "https://www.synack.com/exploits-explained/path-traversal-paradise/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)"]
bugs: ["Path traversal", "LFI"]
publication_date: "2022-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2988
---

Although this was enough for PoC, I decided to dig deeper with this path traversal.

When I was fuzzing the application, I encountered an error that disclosed the full path to the webroot.

I ran ffuf again but now in the webroot of the server using the path traversal that I had found. This way, I was able to enumerate a file named LICENSE that had license keys of the application.

I reported the issue with all my findings and my report was selected during the Initial Launch Period.

Thanks for the read. 🙂

![Kuldeep Pandya](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2022/02/Kuldeep-Pandya-130-circle.png)

You can reach out to me at [@kuldeepdotexe](https://twitter.com/kuldeepdotexe).
