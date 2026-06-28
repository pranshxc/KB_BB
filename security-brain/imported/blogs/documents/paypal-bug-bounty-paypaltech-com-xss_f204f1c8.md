---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-04-13_paypal-bug-bounty-paypaltechcom-xss.md
original_filename: 2013-04-13_paypal-bug-bounty-paypaltechcom-xss.md
title: 'PayPal Bug Bounty: PayPaltech.com XSS'
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
raw_sha256: f204f1c847322d4205b8b27e4d7106abee23d8fa269f8b5b5f17ce3c8965c6e1
text_sha256: 5dff08ba7d6b8cf7f8b79dc6e9375a4d3024b67aa1a71ca62195b7ed2f20a344
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# PayPal Bug Bounty: PayPaltech.com XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-04-13_paypal-bug-bounty-paypaltechcom-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `f204f1c847322d4205b8b27e4d7106abee23d8fa269f8b5b5f17ce3c8965c6e1`
- Text SHA256: `5dff08ba7d6b8cf7f8b79dc6e9375a4d3024b67aa1a71ca62195b7ed2f20a344`


## Content

---
title: "PayPal Bug Bounty: PayPaltech.com XSS"
page_title: "PayPal Bug Bounty: PayPaltech.com XSS | RCE Security"
url: "https://www.rcesecurity.com/2013/04/paypal-bug-bounty-paypaltech-com-xss/"
final_url: "https://www.rcesecurity.com/2013/04/paypal-bug-bounty-paypaltech-com-xss/"
authors: ["Julien Ahrens (@MrTuxracer)"]
programs: ["Paypal"]
bugs: ["XSS"]
publication_date: "2013-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6406
---

# PayPal Bug Bounty: PayPaltech.com XSS

Apr 13, 2013 · By [Julien Ahrens](/about/)

Great news! Today I received the second payment for another valid Cross-Site Scripting vulnerability covered by [PayPal’s bug bounty](https://www.paypal.com/us/webapps/mpp/security/reporting-security-issues) program. This time the domain [www.paypaltech.com](https://www.paypaltech.com) was affected, which provides scripts and samples used for Instant Payment Notifications (IPNs). **Sometimes** … being on the ethical side of hacking feels good … :-)

![ia41](/2013/04/paypal-bug-bounty-paypaltech-com-xss/images/ia41.d9204e908ccc842e5cee32d6a27af40f5ae478c0a1614f2de6250c00687b43ef.png)
