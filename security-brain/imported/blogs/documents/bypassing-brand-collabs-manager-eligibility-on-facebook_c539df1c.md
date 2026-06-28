---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-26_bypassing-brand-collabs-manager-eligibility-on-facebook.md
original_filename: 2019-12-26_bypassing-brand-collabs-manager-eligibility-on-facebook.md
title: Bypassing Brand Collabs Manager Eligibility on Facebook
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: c539df1c037de320a1514326a442b42bec3050cd9edf3a2c4a4ca32692392ded
text_sha256: 960d7319c661e9a1e67a265821d87d1bab82b55c690120cd6eb6ab18c72fea3f
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Brand Collabs Manager Eligibility on Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-26_bypassing-brand-collabs-manager-eligibility-on-facebook.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `c539df1c037de320a1514326a442b42bec3050cd9edf3a2c4a4ca32692392ded`
- Text SHA256: `960d7319c661e9a1e67a265821d87d1bab82b55c690120cd6eb6ab18c72fea3f`


## Content

---
title: "Bypassing Brand Collabs Manager Eligibility on Facebook"
url: "https://medium.com/nassec-cybersecurity-writeups/bypassing-brand-collabs-manager-eligibility-7d26523da816"
authors: ["Ajay Gautam (@evilboyajay)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-12-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4860
scraped_via: "browseros"
---

# Bypassing Brand Collabs Manager Eligibility on Facebook

Member-only story

Bypassing Brand Collabs Manager Eligibility on Facebook
Ajay Gautam
Follow
3 min read
·
Dec 26, 2019

115

In this week’s blog, I am writing about how I was able to bypass the eligibility criteria for the Brand Collabs Manager and register my page without meeting the criteria and policy. I wasn’t awarded any bounty for this as Facebook’s production team deemed it unqualified for monetary reward.

If you are not familiar with what Brand Collabs Manager is on Facebook, it is the monetization of Facebook videos where brands can reach to their creators for branded content partnerships.

To be eligible to register in brand collabs one needs to meet the following conditions-

Your Facebook page must have a minimum of 1,000 followers.
In 60 days, your posts must have reached 15000 engagement.
In 60 days, your videos must have 180,000 minutes views.
In the last 60 days, your page must have 30,000 views along with a minimum of one minute watch time for videos over 3 minutes long.

Let me take you through what I found -

When I went to the Brand Collabs Manager application form, I saw that I am was not eligible to apply for the brand collabs manager as Nassec.io as my page didn’t meet the above-mentioned criteria.

Press enter or click to view image in full size
