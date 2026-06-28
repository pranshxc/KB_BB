---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-10_taking-over-the-medium-subdomain-using-medium.md
original_filename: 2022-10-10_taking-over-the-medium-subdomain-using-medium.md
title: Taking over the Medium subdomain using Medium
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 7759bb0b6a5d3c282d2547bacd1567dc4a42e8c7aafd5e9437d774cf7af691c9
text_sha256: 23fe29e3a784ee61c62f1d0fecb227d1da9e69dbc7c352d37705ee4596871818
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Taking over the Medium subdomain using Medium

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-10_taking-over-the-medium-subdomain-using-medium.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `7759bb0b6a5d3c282d2547bacd1567dc4a42e8c7aafd5e9437d774cf7af691c9`
- Text SHA256: `23fe29e3a784ee61c62f1d0fecb227d1da9e69dbc7c352d37705ee4596871818`


## Content

---
title: "Taking over the Medium subdomain using Medium"
page_title: "Taking over the Medium subdomain using Medium – Smaran Chand"
url: "https://smaranchand.com.np/2022/10/taking-over-the-medium-subdomain-using-medium/"
final_url: "https://smaranchand.com.np/2022/10/taking-over-the-medium-subdomain-using-medium/"
authors: ["Smaran Chand (@smaranchand)"]
programs: ["Medium"]
bugs: ["Subdomain takeover"]
publication_date: "2022-10-10"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 2063
---

[October 10, 2022](https://smaranchand.com.np/2022/10/taking-over-the-medium-subdomain-using-medium/)

# Taking over the Medium subdomain using Medium

Medium is a blog hosting platform where a user can write their ideas and share them with a mass number of people. The great thing about medium is “Simplicity” everything is made easier whether it is User Interface/Experience, system, or functions.

After discovering my first critical server-side issue in the medium platform, I chose to help secure the medium by further exploring the vulnerabilities and did explore almost every feature, and every functionality.

While gathering information about the Medium assets, something draw my attention which was medium.engineering. The subdomain platform.medium.engineering had DNS entry pointed to but the medium blog was not active.

![](https://smaranchand.com.np/wp-content/uploads/2021/06/Screen-Shot-2021-06-03-at-9.47.34-AM.png)Image: DNS records for platforms.medium.engineering

In order to point our blog to the vulnerable subdomain medium membership is required. The process is simple to go to the medium account and add the domain.

![](https://smaranchand.com.np/wp-content/uploads/2022/10/A-records.png)_Image: A record required to link a domain which is already done by Medium Engineering Team_

![](https://smaranchand.com.np/wp-content/uploads/2022/10/ponted_to_my_medium-blog-700x273.png)_Image: Subdomain linked._ ![](https://smaranchand.com.np/wp-content/uploads/2022/10/Configuration-700x221.png)

And here we go.

![](https://smaranchand.com.np/wp-content/uploads/2022/10/Takeover-700x369.png)_Image: Subdomain Takeover_

Sad Part: The Subdomain takeover issue is not eligible for a bounty cash reward according to the Medium Bug Bounty policy.

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/)
