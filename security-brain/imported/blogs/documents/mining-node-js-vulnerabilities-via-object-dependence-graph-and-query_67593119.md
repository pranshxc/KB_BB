---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-10_mining-nodejs-vulnerabilities-via-object-dependence-graph-and-query.md
original_filename: 2022-08-10_mining-nodejs-vulnerabilities-via-object-dependence-graph-and-query.md
title: Mining Node.js Vulnerabilities via Object Dependence Graph and Query
category: documents
detected_topics:
- command-injection
- sso
- path-traversal
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- path-traversal
- supply-chain
language: en
raw_sha256: 675931198d3996530ce00c43a0bc5bc622a1a83dd795fbf5ecd5576881453417
text_sha256: f65a3e2d270305025a27b129fbf1048316e8d53c171800ca989e58cc44e6e228
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Mining Node.js Vulnerabilities via Object Dependence Graph and Query

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-10_mining-nodejs-vulnerabilities-via-object-dependence-graph-and-query.md
- Source Type: markdown
- Detected Topics: command-injection, sso, path-traversal, supply-chain
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `675931198d3996530ce00c43a0bc5bc622a1a83dd795fbf5ecd5576881453417`
- Text SHA256: `f65a3e2d270305025a27b129fbf1048316e8d53c171800ca989e58cc44e6e228`


## Content

---
title: "Mining Node.js Vulnerabilities via Object Dependence Graph and Query"
page_title: "Mining Node.js Vulnerabilities via Object Dependence Graph and Query | USENIX"
url: "https://www.usenix.org/conference/usenixsecurity22/presentation/li-song"
final_url: "https://www.usenix.org/conference/usenixsecurity22/presentation/li-song"
authors: ["Song Li", "Mingqing Kang", "Jianwei Hou", "Yinzhi Cao"]
bugs: ["RCE", "OS command injection", "Prototype pollution", "Path traversal"]
publication_date: "2022-08-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2337
---

Song Li and Mingqing Kang, _Johns Hopkins University;_ Jianwei Hou, _Johns Hopkins University/Renmin University of China;_ Yinzhi Cao, _Johns Hopkins University_

Node.js is a popular non-browser JavaScript platform that provides useful but sometimes also vulnerable packages. On one hand, prior works have proposed many program analysis-based approaches to detect Node.js vulnerabilities, such as command injection and prototype pollution, but they are specific to individual vulnerability and do not generalize to a wide range of vulnerabilities on Node.js. On the other hand, prior works on C/C++ and PHP have proposed graph query-based approaches, such as Code Property Graph (CPG), to efficiently mine vulnerabilities, but they are not directly applicable to JavaScript due to the language's extensive use of dynamic features.

In the paper, we propose flow- and context-sensitive static analysis with hybrid branch-sensitivity and points-to information to generate a novel graph structure, called Object Dependence Graph (ODG), using abstract interpretation. ODG represents JavaScript objects as nodes and their relations with Abstract Syntax Tree (AST) as edges, and accepts graph queries—especially on object lookups and definitions—for detecting Node.js vulnerabilities.

We implemented an open-source prototype system, called ODGEN, to generate ODG for Node.js programs via abstract interpretation and detect vulnerabilities. Our evaluation of recent Node.js vulnerabilities shows that ODG together with AST and Control Flow Graph (CFG) is capable of modeling 13 out of 16 vulnerability types. We applied ODGEN to detect six types of vulnerabilities using graph queries: ODGEN correctly reported 180 zero-day vulnerabilities, among which we have received 70 Common Vulnerabilities and Exposures (CVE) identifiers so far.

## Open Access Media

USENIX is committed to Open Access to the research presented at our events. Papers and proceedings are freely available to everyone once the event begins. Any video, audio, and/or slides that are posted after the event are also free and open to everyone. [Support USENIX](/annual-fund) and our commitment to Open Access.

BibTeX

@inproceedings {277128,  
author = {Song Li and Mingqing Kang and Jianwei Hou and Yinzhi Cao},  
title = {Mining Node.js Vulnerabilities via Object Dependence Graph and Query},  
booktitle = {31st USENIX Security Symposium (USENIX Security 22)},  
year = {2022},  
isbn = {978-1-939133-31-1},  
address = {Boston, MA},  
pages = {143--160},  
url = {https://www.usenix.org/conference/usenixsecurity22/presentation/li-song},  
publisher = {USENIX Association},  
month = aug  
}  

[Download](/biblio/export/bibtex/277128)

![PDF icon](/core/modules/file/icons/application-pdf.png) [Li PDF](https://www.usenix.org/system/files/sec22-li-song.pdf "sec22-li-song.pdf")

![PDF icon](/core/modules/file/icons/application-pdf.png) [Li Appendix PDF](https://www.usenix.org/system/files/usenixsecurity22-li-song.pdf "usenixsecurity22-li-song.pdf")

![PDF icon](/core/modules/file/icons/application-pdf.png) [Li Paper (Prepublication) PDF](https://www.usenix.org/system/files/sec22summer_li-song.pdf "sec22summer_li-song.pdf")

![](https://www.usenix.org/sites/default/files/usenix_artifact_evaluation_available_125_update.png)

![](https://www.usenix.org/sites/default/files/usenix_artifact_evaluation_functional_125.png)

![](https://www.usenix.org/sites/default/files/usenix_artifact_evaluation_reproduced_125.png)

## Presentation Video
