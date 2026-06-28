---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-14_unremovable-tags-in-facebook-page-reviews.md
original_filename: 2018-12-14_unremovable-tags-in-facebook-page-reviews.md
title: Unremovable Tags In Facebook Page Reviews
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 32b33b73c2e387797df3a07c31962b96617aa82107a4984061dbbd71b0fddae2
text_sha256: 1325ef810b82e84d29f82c9d50555ef71aa57645cb89189ed4d2cc3baf9fa13d
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Unremovable Tags In Facebook Page Reviews

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-14_unremovable-tags-in-facebook-page-reviews.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `32b33b73c2e387797df3a07c31962b96617aa82107a4984061dbbd71b0fddae2`
- Text SHA256: `1325ef810b82e84d29f82c9d50555ef71aa57645cb89189ed4d2cc3baf9fa13d`


## Content

---
title: "Unremovable Tags In Facebook Page Reviews"
url: "https://medium.com/@maxpasqua/unremovable-tags-in-facebook-page-reviews-656e095e69aa"
authors: ["Max Pasqua"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2018-12-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5525
scraped_via: "browseros"
---

# Unremovable Tags In Facebook Page Reviews

Max Pasqua
 highlighted

Unremovable Tags In Facebook Page Reviews
Max Pasqua
Follow
1 min read
·
Dec 15, 2018

130

Facebook pages have a feature to leave reviews on them. When making a review a malicious user could tag a victim and it would render the tag unremovable. Upon trying to remove it would give the victim an error. The impact behind this is that the victim is permanently stuck tagged. Attackers could leverage this with massive spam posts or embarrassing information against the victim and he will not be able to remove himself from the post.

Proof of Concept

1) Browse to the page that you want the tag to be stuck on (Preferably owned by the attacker so the owner of the page wont remove the post)

2) Create a review and tag the victim

3) The victim will now no longer be able to remove the tag

Get Max Pasqua’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Video

Timeline

Submitted- October 13th, 2018

Triaged- October 18th, 2018

Bounty Awarded($500)- December 14th, 2018
