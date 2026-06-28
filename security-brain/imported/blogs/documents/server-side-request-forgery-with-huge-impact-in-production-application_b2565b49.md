---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-23_server-side-request-forgery-with-huge-impact-in-production-application.md
original_filename: 2021-08-23_server-side-request-forgery-with-huge-impact-in-production-application.md
title: Server Side Request Forgery with huge impact in production application
category: documents
detected_topics:
- ssrf
- command-injection
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- supply-chain
language: en
raw_sha256: b2565b49514b57a8c4c2ce607694ee51765333c869bbd3afe55e6ba2d92de960
text_sha256: fb8152c17e4061194103423fe63f73d21050c564e5e5ce4da5bcf10091bd0b22
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Server Side Request Forgery with huge impact in production application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-23_server-side-request-forgery-with-huge-impact-in-production-application.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `b2565b49514b57a8c4c2ce607694ee51765333c869bbd3afe55e6ba2d92de960`
- Text SHA256: `fb8152c17e4061194103423fe63f73d21050c564e5e5ce4da5bcf10091bd0b22`


## Content

---
title: "Server Side Request Forgery with huge impact in production application"
url: "https://medium.com/@gguzelkokar.mdbf15/huge-impact-server-side-request-forgery-in-production-app-20bf0cc5731"
authors: ["Gökhan Güzelkokar (@gkhck_)"]
bugs: ["SSRF"]
publication_date: "2021-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3399
scraped_via: "browseros"
---

# Server Side Request Forgery with huge impact in production application

Member-only story

Server Side Request Forgery with huge impact in production application
Gökhan Güzelkokar
Follow
3 min read
·
Aug 23, 2021

271

1

Hi all, I hope all is well. I’m going to talk about the SSRF I found a long time ago. That was really easy finding. Let’s get started 🐱‍💻

Now, I’ll talk about my recon process for programs which have big scopes. Let’s talk about for *.anywebsite.com. Listen, of course recon is important but if you focus on your target you can find more juicy things. I’ll use 5 tools for my all recon process.

GitHub - projectdiscovery/subfinder: Subfinder is a subdomain discovery tool that discovers valid…
Subfinder is a subdomain discovery tool that discovers valid subdomains for websites. Designed as a passive framework…

github.com

GitHub - lc/gau: Fetch known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and…
getallurls (gau) fetches known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl for…

github.com

GitHub - projectdiscovery/httpx: httpx is a fast and multi-purpose HTTP toolkit allows to run…
httpx is a fast and multi-purpose HTTP toolkit allows to run multiple probers using retryablehttp library, it is…

github.com

GitHub - GerbenJavado/LinkFinder: A python script that finds endpoints in JavaScript files
A python script that finds endpoints in JavaScript files - GitHub - GerbenJavado/LinkFinder: A python script that finds…

github.com
