---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-11_identity-confusion-in-webview-based-mobile-app-in-app-ecosystems.md
original_filename: 2022-08-11_identity-confusion-in-webview-based-mobile-app-in-app-ecosystems.md
title: Identity Confusion in WebView-based Mobile App-in-app Ecosystems
category: documents
detected_topics:
- mobile-security
- sso
- command-injection
- supply-chain
tags:
- imported
- documents
- mobile-security
- sso
- command-injection
- supply-chain
language: en
raw_sha256: 6c503a36b1d370823905d3a7cc359c850702d4bdbed23f1af4ff503d6492a3c7
text_sha256: c5ed373c914ca0dc2f8a137d37d0fe6986e74fbbdf00f656aa592b5a3a90c7a6
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Identity Confusion in WebView-based Mobile App-in-app Ecosystems

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-11_identity-confusion-in-webview-based-mobile-app-in-app-ecosystems.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `6c503a36b1d370823905d3a7cc359c850702d4bdbed23f1af4ff503d6492a3c7`
- Text SHA256: `c5ed373c914ca0dc2f8a137d37d0fe6986e74fbbdf00f656aa592b5a3a90c7a6`


## Content

---
title: "Identity Confusion in WebView-based Mobile App-in-app Ecosystems"
page_title: "Identity Confusion in WebView-based Mobile App-in-app Ecosystems | USENIX"
url: "https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-lei"
final_url: "https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-lei"
authors: ["Lei Zhang, Zhibo Zhang, Ancong Liu, Yinzhi Cao, Xiaohan Zhang, Yanjun Chen, Yuan Zhang, Guangliang Yang & Min Yang"]
programs: ["Alipay"]
bugs: ["Android", "iOS"]
bounty: "2,500"
publication_date: "2022-08-11"
added_date: "2022-10-02"
source: "pentester.land/writeups.json"
original_index: 2336
---

Lei Zhang, Zhibo Zhang, and Ancong Liu, _Fudan University;_ Yinzhi Cao, _Johns Hopkins University;_ Xiaohan Zhang, Yanjun Chen, Yuan Zhang, Guangliang Yang, and Min Yang, _Fudan University_

Distinguished Paper Award Winner

Mobile applications (apps) often delegate their own functions to other parties, which makes them become a super ecosystem hosting these parties. Therefore, such mobile apps are being called super-apps, and the delegated parties are subsequently called sub-apps, behaving like "app-in-app". Sub-apps not only load (third-party) resources like a normal app, but also have access to the privileged APIs provided by the super-app. This leads to an important research question—determining who can access these privileged APIs.

Real-world super-apps, according to our study, adopt three types of identities—namely web domains, sub-app IDs, and capabilities—to determine privileged API access. However, existing identity checks of these three types are often not well designed, leading to a disobey of the least privilege principle. That is, the granted recipient of a privileged API is broader than intended, thus defined as an "identity confusion" in this paper. To the best of our knowledge, no prior works have studied this type of identity confusion vulnerability.

In this paper, we perform the first systematic study of identity confusion in real-world app-in-app ecosystems. We find that confusions of the aforementioned three types of identities are widespread among all 47 studied super-apps. More importantly, such confusions lead to severe consequences such as manipulating users' financial accounts and installing malware on a smartphone. We responsibly reported all of our findings to developers of affected super-apps, and helped them to fix their vulnerabilities.

## Open Access Media

USENIX is committed to Open Access to the research presented at our events. Papers and proceedings are freely available to everyone once the event begins. Any video, audio, and/or slides that are posted after the event are also free and open to everyone. [Support USENIX](/annual-fund) and our commitment to Open Access.

![](https://www.usenix.org/modules/custom/usenix_files/images/usenix-locked.png)

BibTeX

@inproceedings {280044,  
author = {Lei Zhang and Zhibo Zhang and Ancong Liu and Yinzhi Cao and Xiaohan Zhang and Yanjun Chen and Yuan Zhang and Guangliang Yang and Min Yang},  
title = {Identity Confusion in {WebView-based} Mobile App-in-app Ecosystems},  
booktitle = {31st USENIX Security Symposium (USENIX Security 22)},  
year = {2022},  
isbn = {978-1-939133-31-1},  
address = {Boston, MA},  
pages = {1597--1613},  
url = {https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-lei},  
publisher = {USENIX Association},  
month = aug  
}  

[Download](/biblio/export/bibtex/280044)

![PDF icon](/core/modules/file/icons/application-pdf.png) [Zhang PDF](https://www.usenix.org/system/files/sec22-zhang-lei.pdf "sec22-zhang-lei.pdf")

![](https://www.usenix.org/modules/custom/usenix_files/images/usenix-unlocked.png)

[View the slides](https://www.usenix.org/system/files/sec22_slides-zhang_lei.pdf)

## Presentation Video
