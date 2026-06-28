---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-26_subdomain-takeover-via-pantheon.md
original_filename: 2019-12-26_subdomain-takeover-via-pantheon.md
title: Subdomain takeover via pantheon
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 821a9e2182706dddd2738e63b5d3815729b9333f3b497c95be7b36cfa7ac3990
text_sha256: 6c2b5f348bc0e07e161c59f0163ab25b8fce89741449f3b09044e6f400034566
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain takeover via pantheon

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-26_subdomain-takeover-via-pantheon.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `821a9e2182706dddd2738e63b5d3815729b9333f3b497c95be7b36cfa7ac3990`
- Text SHA256: `6c2b5f348bc0e07e161c59f0163ab25b8fce89741449f3b09044e6f400034566`


## Content

---
title: "Subdomain takeover via pantheon"
page_title: "Subdomain takeover via pantheon – Smaran Chand"
url: "https://smaranchand.com.np/2019/12/subdomain-takeover-via-pantheon/"
final_url: "https://smaranchand.com.np/2019/12/subdomain-takeover-via-pantheon/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["Subdomain takeover"]
publication_date: "2019-12-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4861
---

[December 26, 2019](https://smaranchand.com.np/2019/12/subdomain-takeover-via-pantheon/)

# Subdomain takeover via pantheon

I hope you are having a great time, I would like to share an issue which i discovered in less than 10 minutes and got rewarded $XXXX bounty within 24 hours of the submission. 

So the story begins when I visited a scope, one of the subdomains and I received a certificate error. I removed SSL from the protocol and used HTTP only and the site opened without any certificate error.

The Site was giving 404 errors in the index page with pantheon stating “Unknown Site”, I felt it might be vulnerable to subdomain takeover issue.

![](https://smaranchand.com.np/wp-content/uploads/2019/12/unclaimed_subdomain.png)

Without wasting any time I signed up for pantheon, added payment details and created a sandbox domain, installed WordPress and added simple Title on the homepage as ” Subdomain Takeover”. The sandbox domain provided by pantheon looked like http://dev-subdomaintakeover[.]patheonsite.io/

![](https://smaranchand.com.np/wp-content/uploads/2019/12/sandbox_domain.png)

And then I added the vulnerable domain to my pantheon account or routed the sandbox domain to vulnerable subdomain.

![](https://smaranchand.com.np/wp-content/uploads/2019/12/records.png)

and within few seconds the site was updated with my sandbox domain content.

![](https://smaranchand.com.np/wp-content/uploads/2019/12/takeover-700x420.png)

The same method was used to hack the website belonging to the current president of the United States Of America Donald J Trump.

**References:**

<https://github.com/EdOverflow/can-i-take-over-xyz/issues/24>

<https://medium.com/@hussain_0x3c/hostile-subdomain-takeover-using-pantheon-ebf4ab813111>

<https://thehackernews.com/2017/02/donald-trump-website-hacked.html>

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/)
