---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-03_view-other-user-private-livestream-data.md
original_filename: 2021-07-03_view-other-user-private-livestream-data.md
title: View Other User Private Livestream Data
category: documents
detected_topics:
- idor
- command-injection
- graphql
tags:
- imported
- documents
- idor
- command-injection
- graphql
language: en
raw_sha256: 6c3ba7d5bc3b042a4b0afb058ebd3badcdaf64fa33a6bcf8b1a4e2b4a31eb06a
text_sha256: b6d1ffe1298b46c18856abfb093b4c10fb5f30258d4152ea8f473fc01be0d70c
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# View Other User Private Livestream Data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-03_view-other-user-private-livestream-data.md
- Source Type: markdown
- Detected Topics: idor, command-injection, graphql
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `6c3ba7d5bc3b042a4b0afb058ebd3badcdaf64fa33a6bcf8b1a4e2b4a31eb06a`
- Text SHA256: `b6d1ffe1298b46c18856abfb093b4c10fb5f30258d4152ea8f473fc01be0d70c`


## Content

---
title: "View Other User Private Livestream Data"
url: "https://gevakun.medium.com/view-other-user-private-livestream-data-e30a0acb5972"
authors: ["Geva (@Geva_7)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2021-07-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3529
scraped_via: "browseros"
---

# View Other User Private Livestream Data

View Other User Private Livestream Data
Geva-Kun
Follow
2 min read
·
Jul 3, 2021

220

بِسْمِ للَّٰهِ لرَّحْمَٰنِ لرَّحِيمِ

Hey, welcome to this write-up!

What I’ve found is only from Allah’s will, actually I’m nothing.

Note:

There’s “TL;DR” section for those who only need the main point of this write-up.
I really apologize if my write-up is bad.

Enjoy :)

I. TL;DR
Facebook has a query to fetch the Livestream data.
Surprisingly, it’s vulnerable to IDOR.
Then I was able to view private data from other user’s Livestream.
II. Introduction

There’s a query named “LiveProducerProviderRefetchQuery”, the query provide a lot of private data such as:

Blocked user list
Broadcast config
Charity data

and many more.

Get Geva-Kun’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This query should only be used for the Livestream owner.

III. The Findings

As far as I can remember, I just messing around Live Streaming feature that is located at https://www.facebook.com/live/producer/, what I do is intercepting requests when I access the page, and hope I’ll found a vulnerable query.

Then, I found a query named “LiveProducerProviderRefetchQuery” and noticed there’s a “videoID” parameter:

Press enter or click to view image in full size
“LiveProducerProviderRefetchQuery”

Immediately I messing with it by changing the “videoID” parameter to another user Livestream ID, and boom it’s shows some private data that I mentioned above. Alhamdulillah

IV. Takeaways

I strongly recommend y’all to take your time for:

Crawl a page and check your Burp “Site Map” (especially, graphql folder) or proxy history, because it may contain vulnerable query that leads to IDOR or any weird bugs.
Press enter or click to view image in full size
Turn on “Live passive crawl”
Press enter or click to view image in full size
SUSpicious query
Intercepting request when you click a button (like add friend button, delete button, etc), because the button may contain vulnerable query.
SUSpicious button
V. Timeline

July 7, 2020 — Report sent

July 16, 2020 — Triaged by Facebook team

November 12, 2020 — Bounty rewarded

April 24, 2021 — Vulnerability patched

Alhamdulillah, finally this write-up ends here.

Hit me up if you have any inquiries: https://twitter.com/Geva_7
