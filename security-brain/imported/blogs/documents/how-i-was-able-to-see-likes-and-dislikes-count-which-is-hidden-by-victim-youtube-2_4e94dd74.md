---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-17_how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube.md
original_filename: 2022-06-17_how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube.md
title: 'How I was able to see likes and dislikes count which is hidden by victim |
  YouTube #2'
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
raw_sha256: 4e94dd7442a331912bc5ead3cb1bd5bf7a60851abbac133436ac9557611b24a0
text_sha256: 0ac0c6db224047887f5aa8a551918428af2ff2f9df43f3cb049f32ecbe08fddc
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to see likes and dislikes count which is hidden by victim | YouTube #2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-17_how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `4e94dd7442a331912bc5ead3cb1bd5bf7a60851abbac133436ac9557611b24a0`
- Text SHA256: `0ac0c6db224047887f5aa8a551918428af2ff2f9df43f3cb049f32ecbe08fddc`


## Content

---
title: "How I was able to see likes and dislikes count which is hidden by victim | YouTube #2"
url: "https://medium.com/@janijay007/how-i-was-able-to-see-likes-and-dislikes-count-which-is-hidden-by-victim-youtube-2-721d8e4686a5"
authors: ["Jay Jani (@JayJani007)"]
programs: ["Google"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2022-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2539
scraped_via: "browseros"
---

# How I was able to see likes and dislikes count which is hidden by victim | YouTube #2

Top highlight

How I was able to see likes and dislikes count which is hidden by victim | YouTube #2
Jay Jani
Follow
Jun 17, 2022

5

This one is another way by which I was able to see like/dislike count of any video even if it sets hidden by the uploader.

You might want to read before moving ahead : How I was able to see likes and dislikes count which is hidden by victim | YouTube #1

So let’s get started.

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
1. Visit this GET request

GET /shorts/<short_id> HTTP/1.1
Host: www.youtube.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Cookie: <cookies>

2. Change the shorts video id to victim’s video id
3. Attacker is able to see like/dislike count.

PoC video: https://www.youtube.com/watch?v=K1MH_cJy0Ds
