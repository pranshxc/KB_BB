---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-15_admin-panel-bypass-without-the-credentials.md
original_filename: 2023-06-15_admin-panel-bypass-without-the-credentials.md
title: Admin Panel Bypass without the credentials
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: de60d38f41a19d6d3a27613618cb8fa98fc4d89cc87cc7c0dac3be20a674f852
text_sha256: 41345f625e72e2323fd04440a92cae4527a579c70c111b5ed4e37b919feeb8d3
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Admin Panel Bypass without the credentials

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-15_admin-panel-bypass-without-the-credentials.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `de60d38f41a19d6d3a27613618cb8fa98fc4d89cc87cc7c0dac3be20a674f852`
- Text SHA256: `41345f625e72e2323fd04440a92cae4527a579c70c111b5ed4e37b919feeb8d3`


## Content

---
title: "Admin Panel Bypass without the credentials"
url: "https://medium.com/@sayim0x3105/admin-panel-bypass-without-the-credentials-e867eee7c81b"
authors: ["Sayim0x (@sayim0x)"]
programs: ["Pfizer"]
bugs: ["Authentication bypass"]
publication_date: "2023-06-15"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1043
scraped_via: "browseros"
---

# Admin Panel Bypass without the credentials

Admin Panel Bypass without the credentials
Sayim0x
Follow
2 min read
·
Jun 16, 2023

579

7

Assalamu Alaikum, peace be upon you

I am Sayim0x. I’m a bug bounty hunter from Bangladesh. This is my first article/write-up, Today I will share how I find my first critical bug on HackerOne.

I started doing my recon on a HackerOne public program named Pfizer. I found lots of IPs on this organization by Shodan and picked one. Then I start crawling on this IP. Suddenly I noticed this endpoint ( https://x.x.x.x/PurchaseOrder/MyDashboard.aspx ). Then I try to access the page but it redirects me to this page ( https://x.x.x.x/LogOut.aspx?action=logout )

s

After some time my mind says Wait Wait Wait……

Get Sayim0x’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am not logged in, why does it auto-redirect and log out me? Then I used the No Redirect extension for capture redirection. After capturing redirection, I can access the full admin panel.

Press enter or click to view image in full size

Then I report it on HackerOne. But I don’t receive any Bounty because it is VDP Program.

Thank you for reading my short write-up. ❤
