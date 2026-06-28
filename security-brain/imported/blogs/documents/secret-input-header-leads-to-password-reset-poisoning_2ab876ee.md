---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-18_secret-input-header-leads-to-password-reset-poisoning.md
original_filename: 2024-01-18_secret-input-header-leads-to-password-reset-poisoning.md
title: Secret Input Header leads to Password Reset Poisoning
category: documents
detected_topics:
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 2ab876ee52c1a09b21c516cbaa4e61d2313469fe8f69b6193b723d00725b7d87
text_sha256: c77e008a06367c38c7b576e6b70f8ecd66ce587f863a99919007475568f9a3aa
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Secret Input Header leads to Password Reset Poisoning

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-18_secret-input-header-leads-to-password-reset-poisoning.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `2ab876ee52c1a09b21c516cbaa4e61d2313469fe8f69b6193b723d00725b7d87`
- Text SHA256: `c77e008a06367c38c7b576e6b70f8ecd66ce587f863a99919007475568f9a3aa`


## Content

---
title: "Secret Input Header leads to Password Reset Poisoning"
url: "https://medium.com/@mares.viktor/secret-input-header-leads-to-password-reset-poisoning-ad3081fd8488"
authors: ["Viktor Mares"]
bugs: ["Password reset"]
publication_date: "2024-01-18"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 519
scraped_via: "browseros"
---

# Secret Input Header leads to Password Reset Poisoning

Member-only story

Secret Input Header leads to Password Reset Poisoning
Viktor Mares
Follow
5 min read
·
Jan 18, 2024

302

1

Hi
Everyone, today I want to showcase why it is important to search for unkeyed headers and what it can lead to. The vulnerability has already been patched, however due to confidentiality agreements, the vulnerable website will be anonymized (hence, we will use the usual example.com domain).

I want everyone to be able to read this story, even without a Medium Subscription. Use this friend link to access it for free and share it with others who might find it interesting :)

To start off, we simply visit the domain (https://example.com/), which straightaway redirects us to /Portal/Account/LogOn. Before we start creating an account, we want to gather as much information as possible. So, we start by bruteforcing directories at each level of the web application. When running gobuster at the /Portal directory, we stumble upon the following interesting subdirectory: /redirect

Press enter or click to view image in full size
Running gobuster for content discovery

The /redirect directory catches the eye, because it could be possible to find a client-side redirect vulnerability quite easily. So, we visit https://example.com/Portal/redirect and we get the following response:

As we can see, this is only an onsite redirect, that will make us return to the /Portal directory. There is a big difference between an onsite and client-side redirect and I recommend reading more about…
