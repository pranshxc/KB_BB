---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-31_microsoft-accidentally-exposed-their-private-xbox-game-developer-forums.md
original_filename: 2022-01-31_microsoft-accidentally-exposed-their-private-xbox-game-developer-forums.md
title: Microsoft accidentally exposed their private Xbox game developer forums
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: c2ba69a8e387c338e7c807427eec42f952ff48149afa215e40c2f49f20436ff0
text_sha256: ec9459c8db99830ccc0f016fc24069681222279a740dda22063ccba638c43c09
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft accidentally exposed their private Xbox game developer forums

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-31_microsoft-accidentally-exposed-their-private-xbox-game-developer-forums.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `c2ba69a8e387c338e7c807427eec42f952ff48149afa215e40c2f49f20436ff0`
- Text SHA256: `ec9459c8db99830ccc0f016fc24069681222279a740dda22063ccba638c43c09`


## Content

---
title: "Microsoft accidentally exposed their private Xbox game developer forums"
url: "https://eaton-works.com/2022/01/31/microsoft-accidentally-exposed-their-private-xbox-game-developer-forums/"
final_url: "https://eaton-works.com/2022/01/31/microsoft-accidentally-exposed-their-private-xbox-game-developer-forums/"
authors: ["Eaton Z. (@XeEaton)"]
programs: ["Microsoft (Xbox)"]
bugs: ["Missing authentication"]
publication_date: "2022-01-31"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 2956
---

# Microsoft accidentally exposed their private Xbox game developer forums

![](/assets/images/ew-logo-4circle-48.png?cb=64e21a35) Eaton • Jan 31, 2022

Copy Link Share 

**Note:** This occurred in 2015 and was published January 31, 2022 as part of the recent [Eaton Works website revamp](/2021/11/15/building-the-new-eaton-works-website/).

Ever since the very beginning of Xbox development there have been private forums hosted by Microsoft where game studio employees can discuss topics with each other and Microsoft Xbox staff. These forums are confidential and no one outside of Microsoft and Microsoft-approved game studios can access them.

In May 2015 Microsoft was working on an updated forum. After Google-searching an error code I was getting on my Xbox One console, I stumbled upon an interesting cloudapp.net (Azure) website result. It was a forum topic from a game developer asking about the same error code.

After looking around the forum, I realized this was the fabled game developer forums. It was a staging site with several years worth of topics imported into a seemingly new design. **The forums had no authentication.** 🚨 All the forum sections could be browsed without getting a login prompt, which was why the site was being indexed/crawled by Google. I also had full access to private forums that were made specifically for AAA studios such as Ubisoft, Bethesda, and Bungie:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/841ba879-1cfe-4bd5-fe6f-5d5ba2440000/full)

Fortunately, there was a support email in the footer of the site. I promptly sent an email describing the issue. I got in touch with the right person and just about 24 hours after I sent the first email, the forums were taken offline. I was very impressed how quickly Microsoft/Xbox addressed the issue.

My report did not qualify for a bug bounty since the website didn’t fall in the list of eligible Microsoft domains. The Microsoft/Xbox staff were very thankful for the responsible disclosure, however.

_Enjoyed this post?_[Like or repost it on X!](https://x.com/XeEaton/status/1488242872902168576)
