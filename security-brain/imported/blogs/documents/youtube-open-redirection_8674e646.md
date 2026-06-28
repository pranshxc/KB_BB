---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-19_youtube-open-redirection.md
original_filename: 2018-11-19_youtube-open-redirection.md
title: Youtube - Open redirection
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 8674e6467373a79610c57d0ff7953dbc3479ec1442e0249e138b943027cc4963
text_sha256: f145cb6d0058f326d2a3e0c324e9a838d481c00a82ce3e948bac25108fe632b8
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Youtube - Open redirection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-19_youtube-open-redirection.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `8674e6467373a79610c57d0ff7953dbc3479ec1442e0249e138b943027cc4963`
- Text SHA256: `f145cb6d0058f326d2a3e0c324e9a838d481c00a82ce3e948bac25108fe632b8`


## Content

---
title: "Youtube - Open redirection"
page_title: "Youtube - Open redirection – Barak Tawily – Security Researcher"
url: "https://quitten.github.io/Youtube/"
final_url: "https://quitten.github.io/Youtube/"
authors: ["Barak Tawily (@quitten11)"]
programs: ["Google"]
bugs: ["Open redirect"]
publication_date: "2018-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5574
---

# Youtube - Open redirection

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIB_tsms02Zl1N_OA03VN76uyqGdeS5MD398UshCUsX_P1mMecbw)

  
Google fixed this a year after I reported this bug and yet refused to accept this as a vulnerability, got no luck with bug-bounties haha

Attack Scenario:

  1. Attacker send youtube link and lure the victim click on it

  2. The link redirects the victim to the attacker’s malicious phishing website requires youtube’s credentials

  3. The victim enters his youtube credentials because he thinks he is still on youtube domain.

  4. The attacker take over the victim’s youtube account (which is actually google account, so he can actually take over gmail drive, etc.)

PoC Video: <https://www.youtube.com/watch?v=CcsJ8EXUIvA>

Written on November 19, 2018
