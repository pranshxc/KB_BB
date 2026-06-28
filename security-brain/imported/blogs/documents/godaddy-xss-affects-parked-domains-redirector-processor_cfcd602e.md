---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-11_godaddy-xss-affects-parked-domains-redirectorprocessor.md
original_filename: 2017-06-11_godaddy-xss-affects-parked-domains-redirectorprocessor.md
title: Godaddy XSS affects parked domains redirector/processor!
category: documents
detected_topics:
- xss
- sso
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- mfa
- api-security
language: en
raw_sha256: cfcd602e671811b87799a4538a748655dd9273684e841fedb770eb7de0da962b
text_sha256: 3dd448de8737a39b2c1bb3aece3d74de9f0608a107e1c362ef349c15506430a8
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Godaddy XSS affects parked domains redirector/processor!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-11_godaddy-xss-affects-parked-domains-redirectorprocessor.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `cfcd602e671811b87799a4538a748655dd9273684e841fedb770eb7de0da962b`
- Text SHA256: `3dd448de8737a39b2c1bb3aece3d74de9f0608a107e1c362ef349c15506430a8`


## Content

---
title: "Godaddy XSS affects parked domains redirector/processor!"
page_title: "Godaddy XSS affects parked domains redirector/processor! – Seekurity"
url: "https://www.seekurity.com/blog/write-ups/godaddy-xss-affects-parked-domains-redirector-processor"
final_url: "https://seekurity.com/blog/2017/06/11/admin/poc-gallery/godaddy-xss-affects-parked-domains-redirector-processor"
authors: ["Mohamed A. Baset"]
programs: ["GoDaddy"]
bugs: ["Reflected XSS"]
publication_date: "2017-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6180
---

Hi Folks,

I’m not going to talk a lot about this issue because it’s a little bit trivial but it affects Godaddy’s parked domains redirector/processor.

First, What is Godaddy?  
For all of you who don’t know [Godaddy](https://www.godaddy.com)

> GoDaddy Inc. is an American publicly traded Internet domain registrar and web hosting company. As of May 2017, GoDaddy has served approximately 17 million customers and had over 6000 employees worldwide.The company is known for its advertising. It has been involved in several controversies related to censorship.

Getting directly down to the details:

Our early STaaS (Security Testing as a Service, Vulnerability and Risk Management Platform) [Sonarify](http://www.Sonarify.com) managed to find a cross site scripting vulnerability affecting mcc.godaddy.com which can be used in stealing cookies, phishing attacks and many more. (Read about the usages of XSS vulnerability)

This vulnerability could be reproduced by issuing a GET request to http://mcc.godaddy.com/park/[PARKED_DOMAIN]?72565%27%3balert(document.domain)%2f%2f146=1

For example: <http://mcc.godaddy.com/park/rUMuqUO1ozRhpTW6?72565%27%3balert(document.domain)%2f%2f146=1>

The PoC Video (shows the vulnerable redirect code along with our javascript injection):

Godaddy fixed the issue and rewarded Seekurity team with a generous bounty, Thanks Godaddy!

**Hey!**  
Building a website? Or already built a one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fadmin%2Fpoc-gallery%2Fgodaddy-xss-affects-parked-domains-redirector-processor&linkname=Godaddy%20XSS%20affects%20parked%20domains%20redirector%2Fprocessor%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fadmin%2Fpoc-gallery%2Fgodaddy-xss-affects-parked-domains-redirector-processor&linkname=Godaddy%20XSS%20affects%20parked%20domains%20redirector%2Fprocessor%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fadmin%2Fpoc-gallery%2Fgodaddy-xss-affects-parked-domains-redirector-processor&linkname=Godaddy%20XSS%20affects%20parked%20domains%20redirector%2Fprocessor%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fadmin%2Fpoc-gallery%2Fgodaddy-xss-affects-parked-domains-redirector-processor&linkname=Godaddy%20XSS%20affects%20parked%20domains%20redirector%2Fprocessor%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fadmin%2Fpoc-gallery%2Fgodaddy-xss-affects-parked-domains-redirector-processor&linkname=Godaddy%20XSS%20affects%20parked%20domains%20redirector%2Fprocessor%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fadmin%2Fpoc-gallery%2Fgodaddy-xss-affects-parked-domains-redirector-processor&linkname=Godaddy%20XSS%20affects%20parked%20domains%20redirector%2Fprocessor%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fadmin%2Fpoc-gallery%2Fgodaddy-xss-affects-parked-domains-redirector-processor&linkname=Godaddy%20XSS%20affects%20parked%20domains%20redirector%2Fprocessor%21 "Gmail")[](https://www.addtoany.com/share)

domains  Godaddy. XSS. affects  parked  processor  redirector
