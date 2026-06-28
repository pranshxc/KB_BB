---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-11_how-i-was-able-to-find-pagepersonal-account-disclosure-on-instagram.md
original_filename: 2020-08-11_how-i-was-able-to-find-pagepersonal-account-disclosure-on-instagram.md
title: How I was able to find page/personal account disclosure on Instagram
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: f77d860670235db4c5167fe423a55d981d8e638c097b4816d07b8245976c61a0
text_sha256: 05853436a2c0dbb076eefea4c3e6c8aae0bca1afee736c1cdf887a1bdae061f0
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to find page/personal account disclosure on Instagram

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-11_how-i-was-able-to-find-pagepersonal-account-disclosure-on-instagram.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `f77d860670235db4c5167fe423a55d981d8e638c097b4816d07b8245976c61a0`
- Text SHA256: `05853436a2c0dbb076eefea4c3e6c8aae0bca1afee736c1cdf887a1bdae061f0`


## Content

---
title: "How I was able to find page/personal account disclosure on Instagram"
url: "https://medium.com/nassec-cybersecurity-writeups/how-i-was-able-to-find-page-personal-account-disclosure-on-instagram-d9607de4883f"
authors: ["Ajay Gautam (@evilboyajay)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "2,000"
publication_date: "2020-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4333
scraped_via: "browseros"
---

# How I was able to find page/personal account disclosure on Instagram

Member-only story

How I was able to find page/personal account disclosure on Instagram
Ajay Gautam
Follow
3 min read
·
Aug 11, 2020

324

This write-up is about how I was able to find page/personal account disclosure on Instagram. In my previous blog, I had written about Page admin disclosure and I had got much positive feedback on that blog. Since a lot of people were interested in such vulnerability exposures, I thought why not cover my new discoveries on a blog and share it with you people.

I was testing Instagram and Facebook integration features. If you are familiar with Instagram and Facebook page integration then I am sure you know that we can link our Instagram account to the Facebook page. We can also receive and send messages to Instagram users from the Facebook page. We are also familiar that the Facebook page assigned role in the message looks like below.

Press enter or click to view image in full size
Facebook assigns conversation

While I was testing this Facebook message feature from Facebook, I was not able to get admin id in any way, but when I tried this from Instagram I was able to get admin id in the WebSocket response. When an Instagram message thread is assigned to a page admin from Facebook page inbox then a WebSocket message is sent to the Instagram account which discloses the ID of the assigned Facebook Page admin.

Going deep into this vulnerability. At first, I sent a message to the Instagram id where my Facebook page was linked.
