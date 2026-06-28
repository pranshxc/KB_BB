---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-01_hdiff-a-semi-automatic-framework-for-discovering-semantic-gap-attack-in-http-imp.md
original_filename: 2022-03-01_hdiff-a-semi-automatic-framework-for-discovering-semantic-gap-attack-in-http-imp.md
title: 'HDiff: A Semi-automatic Framework for Discovering Semantic Gap Attack in HTTP
  Implementations'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 41c2657df79a8af4045483d45b613d43a197126c7969686bd9cae4cb14bcf7ec
text_sha256: 22175ce2f8c4925a8ed3e91b6f077834a1d52f17cf3f3edeffccdf45aff7c5b3
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# HDiff: A Semi-automatic Framework for Discovering Semantic Gap Attack in HTTP Implementations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-01_hdiff-a-semi-automatic-framework-for-discovering-semantic-gap-attack-in-http-imp.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `41c2657df79a8af4045483d45b613d43a197126c7969686bd9cae4cb14bcf7ec`
- Text SHA256: `22175ce2f8c4925a8ed3e91b6f077834a1d52f17cf3f3edeffccdf45aff7c5b3`


## Content

---
title: "HDiff: A Semi-automatic Framework for Discovering Semantic Gap Attack in HTTP Implementations"
page_title: "HDiff: A Semi-automatic Framework for Discovering Semantic Gap Attack in HTTP Implementations | Kaiwen Shen"
url: "https://shenkaiwen.com/publication/2022-hdiff/"
final_url: "https://shenkaiwen.com/publication/2022-hdiff/"
authors: ["Kaiwen Shen (@m0xiaoxi)", "Jianyu Lu", "Yaru Yang", "Jianjun Chen", "Mingming Zhang", "Haixin Duan", "Jia Zhang", "Xiaofeng Zheng"]
bugs: ["HTTP request smuggling", "DoS", "Semantic gap attacks"]
publication_date: "2022-03-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2862
---

# Search

 __

[Kaiwen Shen](/)

__

[Kaiwen Shen](/)

  * [ Home](/#about)
  * [Publications](/#publications)
  * [Talks](/#presentations)
  * [Activities](/#news)
  * [Awards](/#accomplishments)
  * [Blog](https://mo-xiaoxi.github.io/)
  * [Contact](/#contact)

  *  __
  * __

Light Dark Automatic

  *  __English

English

[中文 (简体)](https://shenkaiwen.com/zh/publication/2022-hdiff/)

# HDiff: A Semi-automatic Framework for Discovering Semantic Gap Attack in HTTP Implementations

[Kaiwen Shen](/author/kaiwen-shen/), [Jianyu Lu](/author/jianyu-lu/), [Yaru Yang](/author/yaru-yang/), [Jianjun Chen](/author/jianjun-chen/), [Mingming Zhang](/author/mingming-zhang/), [Haixin Duan](/author/haixin-duan/), [Jia Zhang](/author/jia-zhang/), [Xiaofeng Zheng](/author/xiaofeng-zheng/)

March 2022 [](/publication/2022-hdiff/#disqus_thread)__[Protocol Security](/category/protocol-security/), [http](/category/http/)

[PDF](/files/papers/DSN22_HDiff.pdf) [Video](https://www.youtube.com/watch?v=7FDDW9FPsYg) [Custom Link](https://dsn2022.github.io/cpaccepted.html) [Slides](/files/papers/HDiff_DSN2022_PPT.pdf)

![](/publication/2022-hdiff/featured_hubfe46e4849271c2f7f56d609b81de4d7_314385_720x0_resize_lanczos_2.png)

### Abstract

The Internet has become a complex distributed network with numerous middle-boxes, where an end-to-end HTTP request is often processed by multiple intermediate servers before it reaches its destination. However, a general problem in this distributed network is the extit{semantic gap attack}, which is defined as inconsistent semantic interpretations in the processing chain. While some studies have found individual semantic gap attacks, most of them are based on ad-hoc manual analysis, which is inadequate for fundamentally enhancing the security assurance of a system as complex as the HTTP network. In this work, we propose HDiff, a novel semi-automatic detecting framework, systematically exploring semantic gap attacks in HTTP implementations. We designed a documentation analyzer that employs natural language processing techniques to extract rules from specifications, and utilized differential testing to discover semantic gap attacks. We implemented and evaluated it to find three kinds of semantic gap attacks in 10 popular HTTP implementations. In total, HDiff found 14 vulnerabilities and 29 affected server pairs covering all three types of attacks. In particular, HDiff also discovered three new types of attack vectors. We have already duly reported all identified vulnerabilities to the involved HTTP software vendors and obtained 7 new CVEs from well-known HTTP software, including Apache, Tomcat, Weblogic, and Microsoft IIS Server.

Type

[Conference paper](/publication/#1)

Publication

In _the 52nd Annual IEEE/IFIP International Conference on Dependable Systems and Network, 2022_

This research was awarded the runner-up of the best paper at the 52nd Annual International Conference on Reliable Systems and Networks.

* * *

[Web Application Security](/tag/web-application-security/) [Semantic Gap Attack](/tag/semantic-gap-attack/) [Differential Testing](/tag/differential-testing/) [Documentation Analysis](/tag/documentation-analysis/)

  * [ __](https://twitter.com/intent/tweet?url=https://shenkaiwen.com/publication/2022-hdiff/&text=HDiff:%20A%20Semi-automatic%20Framework%20for%20Discovering%20Semantic%20Gap%20Attack%20in%20HTTP%20Implementations)
  * [__](https://www.facebook.com/sharer.php?u=https://shenkaiwen.com/publication/2022-hdiff/&t=HDiff:%20A%20Semi-automatic%20Framework%20for%20Discovering%20Semantic%20Gap%20Attack%20in%20HTTP%20Implementations)
  * [__](mailto:?subject=HDiff:%20A%20Semi-automatic%20Framework%20for%20Discovering%20Semantic%20Gap%20Attack%20in%20HTTP%20Implementations&body=https://shenkaiwen.com/publication/2022-hdiff/)
  * [__](https://www.linkedin.com/shareArticle?url=https://shenkaiwen.com/publication/2022-hdiff/&title=HDiff:%20A%20Semi-automatic%20Framework%20for%20Discovering%20Semantic%20Gap%20Attack%20in%20HTTP%20Implementations)
  * [__](whatsapp://send?text=HDiff:%20A%20Semi-automatic%20Framework%20for%20Discovering%20Semantic%20Gap%20Attack%20in%20HTTP%20Implementations%20https://shenkaiwen.com/publication/2022-hdiff/)
  * [__](https://service.weibo.com/share/share.php?url=https://shenkaiwen.com/publication/2022-hdiff/&title=HDiff:%20A%20Semi-automatic%20Framework%20for%20Discovering%20Semantic%20Gap%20Attack%20in%20HTTP%20Implementations)

[comments powered by Disqus](https://disqus.com)

Next

[A Large-scale and Longitudinal Measurement Study of DKIM Deployment](/publication/2022-dkim/)

Previous

[Weak Links in Authentication Chains: A Large-scale Analysis of Email Sender Spoofing Attacks](/publication/2021-email/)

### Related

  * [CDN judo: Breaking the cdn dos protection with itself](/publication/2020-cdn-judo/)
  * [CDN Backfired: Amplification Attacks Based on HTTP Range Requests](/publication/2020-cdn-backfired/)
  * [A Large-scale and Longitudinal Measurement Study of DKIM Deployment](/publication/2022-dkim/)
  * [Weak Links in Authentication Chains: A Large-scale Analysis of Email Sender Spoofing Attacks](/publication/2021-email/)
  * [Talking with Familiar Strangers: An Empirical Study on HTTPS Context Confusion Attacks](/publication/2020-tls/)

Copyright © Academic Blog of Kaiwen Shen 2024

Published with [Wowchemy](https://wowchemy.com) — the free, [open source](https://github.com/wowchemy/wowchemy-hugo-modules) website builder that empowers creators.

##### Cite

×

 __Copy __Download
