---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-11-29_authentication-bypass-on-ubiquitys-single-sign-on-via-subdomain-takeover.md
original_filename: 2016-11-29_authentication-bypass-on-ubiquitys-single-sign-on-via-subdomain-takeover.md
title: Authentication bypass on Ubiquity’s Single Sign-On via subdomain takeover
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
raw_sha256: 84650895334eb49b4c3b54d3cefb037318d6d1b1006f88abfe6fbedbd3b67316
text_sha256: c201dd053ebe66c578b664f0bfa8972f8f1ab41183b8f22d067d529998fcbb89
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Authentication bypass on Ubiquity’s Single Sign-On via subdomain takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-11-29_authentication-bypass-on-ubiquitys-single-sign-on-via-subdomain-takeover.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `84650895334eb49b4c3b54d3cefb037318d6d1b1006f88abfe6fbedbd3b67316`
- Text SHA256: `c201dd053ebe66c578b664f0bfa8972f8f1ab41183b8f22d067d529998fcbb89`


## Content

---
title: "Authentication bypass on Ubiquity’s Single Sign-On via subdomain takeover"
page_title: "Authentication bypass on Ubiquity’s Single Sign-On via subdomain takeover – Arne Swinnen"
url: "https://www.arneswinnen.net/2016/11/authentication-bypass-on-sso-ubnt-com-via-subdomain-takeover-of-ping-ubnt-com/"
final_url: "https://www.arneswinnen.net/2016/11/authentication-bypass-on-sso-ubnt-com-via-subdomain-takeover-of-ping-ubnt-com/"
authors: ["Arne Swinnen (@ArneSwinnen)"]
programs: ["Ubiquity Networks"]
bugs: ["Subdomain takeover", "Authentication bypass"]
bounty: "500"
publication_date: "2016-11-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6241
---

[0](https://www.arneswinnen.net/2016/11/authentication-bypass-on-sso-ubnt-com-via-subdomain-takeover-of-ping-ubnt-com/#respond)

# Authentication bypass on Ubiquity’s Single Sign-On via subdomain takeover

Posted on [November 29, 2016](https://www.arneswinnen.net/2016/11/authentication-bypass-on-sso-ubnt-com-via-subdomain-takeover-of-ping-ubnt-com/ "8:42 am") by [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "View all posts by Arne Swinnen")

I publicly disclosed a vulnerability that I responsibly disclosed to Ubiquity via the HackerOne platform. It concerned a subdomain takeover issue via Amazon Cloudfront (ping.ubnt.com) in combination with shared session cookies between subdomains on *.ubnt.com, which ultimately lead to a complete Authentication Bypass of their SSO system (sso.ubnt.com). It can be found [here](https://hackerone.com/reports/172137).

### [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "All posts by Arne Swinnen")

![](https://secure.gravatar.com/avatar/85c6e3f06dfe5994e9c112f745d801f39266bc0c77c1deadbfed337f3aa5da49?s=70&d=mm&r=g)

[](https://www.twitter.com/ArneSwinnen)[](https://www.linkedin.com/in/arneswinnen)

Belgian. IT Security. Bug Bounty Hunter.

__[Web Security](https://www.arneswinnen.net/category/research/websec/)
