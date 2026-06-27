# Security Blogs & Articles

This directory stores curated summaries, notes, and excerpts from security blogs and articles.

## Structure

```
blogs/
├── medium/              # Medium articles
├── portswigger/         # PortSwigger Research blog
├── assetnote/           # Assetnote blog
├── project-zero/        # Google Project Zero
├── trail-of-bits/       # Trail of Bits blog
└── personal-notes/      # Your own notes and summaries
```

## How to Add Content

### Recommended Format (Markdown with YAML frontmatter)

```yaml
---
source: medium
url: "https://medium.com/..."
title: "Article Title"
author: "Author Name"
published: "2024-01-01"
tags:
  - ssrf
  - cloud
summary: "Brief summary of the article"
---
```

### Copyright Notice

- For blogs and Medium articles, **prefer storing**:
  - URL and metadata
  - Your own summary and key takeaways
  - Short excerpts for context (fair use)
- **Do not redistribute** full copyrighted article text unless you have explicit rights.
- When in doubt, store a link + your notes.

### Adding via knowledge-rag MCP

You can also add documents directly via the MCP tools:

```
add_from_url(url="https://example.com/article", category="blogs/medium", title="Title")
```
