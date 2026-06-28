---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-01_a-large-scale-and-longitudinal-measurement-study-of-dkim-deployment.md
original_filename: 2022-04-01_a-large-scale-and-longitudinal-measurement-study-of-dkim-deployment.md
title: A Large-scale and Longitudinal Measurement Study of DKIM Deployment
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
raw_sha256: 4d25921d90b9b17ca3bad7673d19a99fa4aeed781d7b029ee9e82e243b378f07
text_sha256: 02035d4f518142361ccf09607f26c4d0cb3894f6233fe13c04f7f2ee769e1a42
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# A Large-scale and Longitudinal Measurement Study of DKIM Deployment

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-01_a-large-scale-and-longitudinal-measurement-study-of-dkim-deployment.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `4d25921d90b9b17ca3bad7673d19a99fa4aeed781d7b029ee9e82e243b378f07`
- Text SHA256: `02035d4f518142361ccf09607f26c4d0cb3894f6233fe13c04f7f2ee769e1a42`


## Content

---
title: "A Large-scale and Longitudinal Measurement Study of DKIM Deployment"
page_title: "A Large-scale and Longitudinal Measurement Study of DKIM Deployment | Kaiwen Shen"
url: "https://shenkaiwen.com/publication/2022-dkim/"
final_url: "https://shenkaiwen.com/publication/2022-dkim/"
authors: ["Chuhan Wang", "Kaiwen Shen (@m0xiaoxi)", "Minglei Guo", "Yuxuan Zhao", "Mingming Zhang", "Jianjun Chen", "Baojun Liu", "Xiaofeng Zheng", "Haixin Duan", "Yanzhong Lin", "Qingfeng Pan"]
programs: ["Google", "Mailchimp", "Sendgrid", "Salesforce"]
bugs: ["Email spoofing", "Phishing"]
publication_date: "2022-04-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2765
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

[中文 (简体)](https://shenkaiwen.com/zh/publication/2022-dkim/)

# A Large-scale and Longitudinal Measurement Study of DKIM Deployment

[Chuhan Wang](/author/chuhan-wang/), [Kaiwen Shen](/author/kaiwen-shen/), [Minglei Guo](/author/minglei-guo/), [Yuxuan Zhao](/author/yuxuan-zhao/), [Mingming Zhang](/author/mingming-zhang/), [Jianjun Chen](/author/jianjun-chen/), [Baojun Liu](/author/baojun-liu/), [Xiaofeng Zheng](/author/xiaofeng-zheng/), [Haixin Duan](/author/haixin-duan/), [Yanzhong Lin](/author/yanzhong-lin/), [Qingfeng Pan](/author/qingfeng-pan/)

April 2022 [](/publication/2022-dkim/#disqus_thread)__[email](/category/email/), [DKIM](/category/dkim/)

[PDF](/files/papers/DKIM.pdf)

![](/publication/2022-dkim/featured_huff72ab5ebca0ed8a20711e21126f2857_145467_720x0_resize_lanczos_2.png)

### Abstract

DomainKeys Identified Mail (DKIM) is an email authentication protocol to protect the integrity of email contents. It has been proposed and standardized for over a decade and adopted by Yahoo!, Google, and other leading email service providers. However, little has been done to understand the adoption rate and potential security issues of DKIM due to the challenges of measuring DKIM deployment at scale. In this paper, we provide a large-scale and longitudinal measurement study on how well DKIM is deployed and managed. Our study was made possible by a broad collection of datasets, including 9.5 million DKIM records from passive DNS datasets over five years and 460 million DKIM signatures from real-world email headers. Moreover, we conduct an active measurement on Alexa Top 1 million domains. Our measurement results show that 28.1% of Alexa Top 1 million domains have enabled DKIM, of which 2.9% are misconfigured. We demonstrate that the issues of DKIM key management and DKIM signatures are prevalent in the real world, even for well-known email providers (eg, Gmail and Mail. ru). We recommend the security community should pay more attention to the systemic problems of DKIM deployment and mitigate these issues from the perspective of protocol design.

Type

[Conference paper](/publication/#1)

Publication

In _the 31th USENIX Security Symposium, Vancouver, BC, Canada, August 2022_

* * *

[Email Security](/tag/email-security/) [DKIM Deployment](/tag/dkim-deployment/)

  * [ __](https://twitter.com/intent/tweet?url=https://shenkaiwen.com/publication/2022-dkim/&text=A%20Large-scale%20and%20Longitudinal%20Measurement%20Study%20of%20DKIM%20Deployment)
  * [__](https://www.facebook.com/sharer.php?u=https://shenkaiwen.com/publication/2022-dkim/&t=A%20Large-scale%20and%20Longitudinal%20Measurement%20Study%20of%20DKIM%20Deployment)
  * [__](mailto:?subject=A%20Large-scale%20and%20Longitudinal%20Measurement%20Study%20of%20DKIM%20Deployment&body=https://shenkaiwen.com/publication/2022-dkim/)
  * [__](https://www.linkedin.com/shareArticle?url=https://shenkaiwen.com/publication/2022-dkim/&title=A%20Large-scale%20and%20Longitudinal%20Measurement%20Study%20of%20DKIM%20Deployment)
  * [__](whatsapp://send?text=A%20Large-scale%20and%20Longitudinal%20Measurement%20Study%20of%20DKIM%20Deployment%20https://shenkaiwen.com/publication/2022-dkim/)
  * [__](https://service.weibo.com/share/share.php?url=https://shenkaiwen.com/publication/2022-dkim/&title=A%20Large-scale%20and%20Longitudinal%20Measurement%20Study%20of%20DKIM%20Deployment)

[comments powered by Disqus](https://disqus.com)

Previous

[HDiff: A Semi-automatic Framework for Discovering Semantic Gap Attack in HTTP Implementations](/publication/2022-hdiff/)

### Related

  * [Weak Links in Authentication Chains: A Large-scale Analysis of Email Sender Spoofing Attacks](/publication/2021-email/)
  * [HDiff: A Semi-automatic Framework for Discovering Semantic Gap Attack in HTTP Implementations](/publication/2022-hdiff/)
  * [CDN judo: Breaking the cdn dos protection with itself](/publication/2020-cdn-judo/)
  * [CDN Backfired: Amplification Attacks Based on HTTP Range Requests](/publication/2020-cdn-backfired/)
  * [Talking with Familiar Strangers: An Empirical Study on HTTPS Context Confusion Attacks](/publication/2020-tls/)

Copyright © Academic Blog of Kaiwen Shen 2024

Published with [Wowchemy](https://wowchemy.com) — the free, [open source](https://github.com/wowchemy/wowchemy-hugo-modules) website builder that empowers creators.

##### Cite

×

 __Copy __Download
