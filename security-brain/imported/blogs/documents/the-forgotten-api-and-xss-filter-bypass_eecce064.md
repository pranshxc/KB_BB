---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-14_the-forgotten-api-and-xss-filter-bypass.md
original_filename: 2022-08-14_the-forgotten-api-and-xss-filter-bypass.md
title: The forgotten API and XSS filter bypass
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: eecce064f618c8a7e9aec37559bb60cb94ad90cf9e6da2f9da4224a668e3e1bd
text_sha256: facdc29e66914144a029ca8274266e840214fa493b81787f7c9e01d5a43760dc
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# The forgotten API and XSS filter bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-14_the-forgotten-api-and-xss-filter-bypass.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `eecce064f618c8a7e9aec37559bb60cb94ad90cf9e6da2f9da4224a668e3e1bd`
- Text SHA256: `facdc29e66914144a029ca8274266e840214fa493b81787f7c9e01d5a43760dc`


## Content

---
title: "The forgotten API and XSS filter bypass"
page_title: "The forgotten API and XSS filter bypass - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/the-forgotten-api-and-xss-filter-bypass/"
final_url: "https://bergee.it/blog/the-forgotten-api-and-xss-filter-bypass/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["XSS"]
publication_date: "2022-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2310
---

# The forgotten API and XSS filter bypass

Posted on [2022-08-142022-09-07](https://bergee.it/blog/the-forgotten-api-and-xss-filter-bypass/) by [bergee](https://bergee.it/blog/author/bergee/)

On one site I found the forum section. There was an option to join some groups and then create posts in the group. I created an account, joined some opened group, and then created the post with the payload:

> <img src=x onerror=alert(1)>

Nothing happened the user input was properly sanitized. I tried URL encoding, double URL encoding, and HTML entity encoding however nothing worked :(. The group URL was like:

> https://www.redacted.com/members/modules/groupsV3/

I thought – what if I change the _groupsV3_ to _groupsV2_ or _groupsV1?_ I didn’t expect much, however, I changed V3 to V2, and… it worked, the URL was valid but no alert box :(. There was some other filter in action – quotes, double quotes, and parenthesis were cut. Hmmm, there must be a way to bypass it. By googling for some time I found this payload:

> <img src=x onerror=setTimeout`alert\x28document.domain\x29`>

It is based on template literal expressions. You can read about it [here](https://css-tricks.com/template-literals/). I used it in a forum post and.. it worked like a charm :). The alert box popped up.

See you next bug :).

Reward: 👕
