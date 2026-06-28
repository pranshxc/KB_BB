---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-12_weaponizing-middleboxes-for-tcp-reflected-amplification.md
original_filename: 2021-08-12_weaponizing-middleboxes-for-tcp-reflected-amplification.md
title: Weaponizing Middleboxes for TCP Reflected Amplification
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
raw_sha256: e1b637c76a0a99cc1051e72acb64d31130323eda945af1a08a381720e4b6c6b2
text_sha256: 172c68c8a7445a742c4635e2125ac916173888460df01534d6c77f0465178d99
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Weaponizing Middleboxes for TCP Reflected Amplification

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-12_weaponizing-middleboxes-for-tcp-reflected-amplification.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `e1b637c76a0a99cc1051e72acb64d31130323eda945af1a08a381720e4b6c6b2`
- Text SHA256: `172c68c8a7445a742c4635e2125ac916173888460df01534d6c77f0465178d99`


## Content

---
title: "Weaponizing Middleboxes for TCP Reflected Amplification"
page_title: "Weaponizing Middleboxes for TCP Reflected Amplification | USENIX"
url: "https://www.usenix.org/conference/usenixsecurity21/presentation/bock"
final_url: "https://www.usenix.org/conference/usenixsecurity21/presentation/bock"
authors: ["Kevin Bock", "Abdulrahman Alaraj", "Yair Fax", "Kyle Hurley", "Eric Wustrow", "Dave Levin"]
programs: ["Check Point", "Cisco", "F5", "Fortinet", "Juniper", "Netscout", "Palo Alto", "SonicWall", "Sucuri"]
bugs: ["DoS"]
publication_date: "2021-08-12"
added_date: "2022-10-02"
source: "pentester.land/writeups.json"
original_index: 3427
---

Kevin Bock, _University of Maryland;_ Abdulrahman Alaraj, _University of Colorado Boulder;_ Yair Fax and Kyle Hurley, _University of Maryland;_ Eric Wustrow, _University of Colorado Boulder;_ Dave Levin, _University of Maryland_

Distinguished Paper Award Winner and Third Prize winner of the 2021 Internet Defense Prize

Reflective amplification attacks are a powerful tool in the arsenal of a DDoS attacker, but to date have almost exclusively targeted UDP-based protocols. In this paper, we demonstrate that non-trivial TCP-based amplification is possible and can be orders of magnitude more effective than well-known UDP-based amplification. By taking advantage of TCP-noncompliance in network middleboxes, we show that attackers can induce middleboxes to respond and amplify network traffic. With the novel application of a recent genetic algorithm, we discover and maximize the efficacy of new TCP-based reflective amplification attacks, and present several packet sequences that cause network middleboxes to respond with substantially more packets than we send.

We scanned the entire IPv4 Internet to measure how many IP addresses permit reflected amplification. We find hundreds of thousands of IP addresses that offer amplification factors greater than 100×. Through our Internet-wide measurements, we explore several open questions regarding DoS attacks, including the root cause of so-called "mega amplifiers". We also report on network phenomena that causes some of the TCP-based attacks to be so effective as to technically have infinite amplification factor (after the attacker sends a constant number of bytes, the reflector generates traffic indefinitely). We have made our code publicly available.

## Open Access Media

USENIX is committed to Open Access to the research presented at our events. Papers and proceedings are freely available to everyone once the event begins. Any video, audio, and/or slides that are posted after the event are also free and open to everyone. [Support USENIX](/annual-fund) and our commitment to Open Access.

BibTeX

@inproceedings {272318,  
author = {Kevin Bock and Abdulrahman Alaraj and Yair Fax and Kyle Hurley and Eric Wustrow and Dave Levin},  
title = {Weaponizing Middleboxes for {TCP} Reflected Amplification},  
booktitle = {30th USENIX Security Symposium (USENIX Security 21)},  
year = {2021},  
isbn = {978-1-939133-24-3},  
pages = {3345--3361},  
url = {https://www.usenix.org/conference/usenixsecurity21/presentation/bock},  
publisher = {USENIX Association},  
month = aug  
}  

[Download](/biblio/export/bibtex/272318)

![PDF icon](/core/modules/file/icons/application-pdf.png) [Bock PDF](https://www.usenix.org/system/files/sec21-bock.pdf "sec21-bock.pdf")

![PDF icon](/core/modules/file/icons/application-pdf.png) [Bock Paper (Prepublication) PDF](https://www.usenix.org/system/files/sec21fall-bock.pdf "sec21fall-bock.pdf")

![](https://www.usenix.org/modules/custom/usenix_files/images/usenix-unlocked.png)

[View the slides](https://www.usenix.org/system/files/sec21_slides_bock.pdf)

## Presentation Video
