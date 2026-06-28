---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-10_web-cache-deception-escalates.md
original_filename: 2022-08-10_web-cache-deception-escalates.md
title: Web Cache Deception Escalates!
category: documents
detected_topics:
- sso
- command-injection
tags:
- imported
- documents
- sso
- command-injection
language: en
raw_sha256: c3ddbe2d72a4ea12e2d9ac368f8b2c86cc17d2ec459cce4582998d13e1af8242
text_sha256: 31b4fe5b92efb6093807e9d4b99efe064d364016740fa2fcdbb11c0f5b67a961
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Web Cache Deception Escalates!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-10_web-cache-deception-escalates.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `c3ddbe2d72a4ea12e2d9ac368f8b2c86cc17d2ec459cce4582998d13e1af8242`
- Text SHA256: `31b4fe5b92efb6093807e9d4b99efe064d364016740fa2fcdbb11c0f5b67a961`


## Content

---
title: "Web Cache Deception Escalates!"
page_title: "Web Cache Deception Escalates! | USENIX"
url: "https://www.usenix.org/conference/usenixsecurity22/presentation/mirheidari"
final_url: "https://www.usenix.org/conference/usenixsecurity22/presentation/mirheidari"
authors: ["Ali Mirheidari", "Matteo Golinelli", "Kaan Onarlioglu", "Engin Kirda", "Bruno Crispo"]
bugs: ["Web cache deception"]
publication_date: "2022-08-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2338
---

Seyed Ali Mirheidari, _University of Trento & Splunk Inc.;_ Matteo Golinelli, _University of Trento;_ Kaan Onarlioglu, _Akamai Technologies;_ Engin Kirda, _Northeastern University;_ Bruno Crispo, _University of Trento_

Web Cache Deception (WCD) tricks a web cache into erroneously storing sensitive content, thereby making it widely accessible on the Internet. In a USENIX Security 2020 paper titled "Cached and Confused: Web Cache Deception in the Wild", researchers presented the first systematic exploration of the attack over 340 websites. This state-of-the-art approach for WCD detection injects markers into websites and checks for leaks into caches. However, this scheme has two fundamental limitations: 1) It cannot probe websites that do not present avenues for marker injection or reflection. 2) Marker setup is a burdensome process, making large-scale measurements infeasible. More generally, all previous literature on WCD focuses solely on personal information leaks on websites protected behind authentication gates, leaving important gaps in our understanding of the full ramifications of WCD.

We expand our knowledge of WCD attacks, their spread, and implications. We propose a novel WCD detection methodology that forgoes testing prerequisites, and utilizes page identicality checks and cache header heuristics to test any website. We conduct a comparative experiment on 404 websites, and show that our scheme identifies over 100 vulnerabilities while "Cached and Confused" is capped at 18. Equipped with a technique unhindered by the limitations of the previous work, we conduct the largest WCD experiment to date on the Alexa Top 10K, and detect 1188 vulnerable websites. We present case studies showing that WCD has consequences well beyond personal information leaks, and that attacks targeting non-authenticated pages are highly damaging.

## Open Access Media

USENIX is committed to Open Access to the research presented at our events. Papers and proceedings are freely available to everyone once the event begins. Any video, audio, and/or slides that are posted after the event are also free and open to everyone. [Support USENIX](/annual-fund) and our commitment to Open Access.

BibTeX

@inproceedings {277152,  
author = {Seyed Ali Mirheidari and Matteo Golinelli and Kaan Onarlioglu and Engin Kirda and Bruno Crispo},  
title = {Web Cache Deception Escalates!},  
booktitle = {31st USENIX Security Symposium (USENIX Security 22)},  
year = {2022},  
isbn = {978-1-939133-31-1},  
address = {Boston, MA},  
pages = {179--196},  
url = {https://www.usenix.org/conference/usenixsecurity22/presentation/mirheidari},  
publisher = {USENIX Association},  
month = aug  
}  

[Download](/biblio/export/bibtex/277152)

![PDF icon](/core/modules/file/icons/application-pdf.png) [Mirheidari PDF](https://www.usenix.org/system/files/sec22-mirheidari.pdf "sec22-mirheidari.pdf")

![PDF icon](/core/modules/file/icons/application-pdf.png) [Mirheidari Paper (Prepublication) PDF](https://www.usenix.org/system/files/sec22summer_mirheidari.pdf "sec22summer_mirheidari.pdf")

![](https://www.usenix.org/modules/custom/usenix_files/images/usenix-unlocked.png)

[View the slides](https://www.usenix.org/system/files/sec22_slides-mirheidari.pdf)

## Presentation Video
