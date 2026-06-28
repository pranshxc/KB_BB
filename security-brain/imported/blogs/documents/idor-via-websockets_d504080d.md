---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-23_idor-via-websockets.md
original_filename: 2019-11-23_idor-via-websockets.md
title: IDOR via Websockets
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: d504080d8631a8f12c7a0f00cba3d1beaf9cc677259a68ebd71348f7cf8873a1
text_sha256: 7fa9091af18b9b058dff7adbaaf5ae328153ed2efded3f7966cff884979bd333
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR via Websockets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-23_idor-via-websockets.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `d504080d8631a8f12c7a0f00cba3d1beaf9cc677259a68ebd71348f7cf8873a1`
- Text SHA256: `7fa9091af18b9b058dff7adbaaf5ae328153ed2efded3f7966cff884979bd333`


## Content

---
title: "IDOR via Websockets"
page_title: "cat ~/footstep.ninja/blog.txt"
url: "https://footstep.ninja/posts/idor-via-websockets/"
final_url: "https://footstep.ninja/posts/idor-via-websockets/"
authors: ["Shuaib Oladigbolu (@_sawzeeyy)"]
bugs: ["IDOR"]
publication_date: "2019-11-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4922
---

# IDOR via Websockets

  * Nov 23, 2019
  * 2 min read

In my previous post, I shared my love for testing Insecure Direct Object Reference (IDOR) vulnerability. This time I’ll be sharing the situation where I found an IDOR in Websockets. You may want to read [this write-up](https://footstep.ninja/posts/websockets-testing/) before you continue. But in short, I shared how I approach testing Websockets.

The target allows commenting on slides in which a user who has access to a slide can share their views about it. Knowing this, I couldn’t resist the urge to test it out. So I made a comment on a slide while also logging the requests via Burp Suite. I noticed 2 requests:

  1. A HTTP PUT request was first sent which notifies the other users of the comment (this was also vulnerable and I would write about it in an upcomming post!).
  2. And a WebSocket request with the following body.

`{ "command": { "operation": [ { "p": [ "slides", 0, "comments", 12 ], "li": { "author": "authorID", "content": " My Comment", "createdAt": "creationDate" } } ], "uuid": "commentUUID", "version": 1 }, "type": "operation", "channel": { "type": "Presentation", "uuid": "slideUUID" } }`

Haha! There is a lot of ID/UUIDs and I was so excited to continue testing.

![Let's do this!](https://media.giphy.com/media/8YHmc8luwmJJjFY7zh/giphy.gif)

I immediately sent this over to Burp Repeater and replaced the authorID with that of another account I have control over. But that didn’t work 😩.

On a closer look, I realized the `commentUUID` could only be used once. So, I improvised and found ways I could obtain another. The easiest way was to make another comment, but this time with “intercept on” while logging requests with Burp Suite.

Then I copied the `commentUUID` from the HTTP PUT request and dropped both the HTTP PUT request and the Websocket request. Afterwards, I replaced the `commentUUID` in Burp Repeater with the one copied and sent the request. This worked and I was able to make comment as another user whether they belong to the team or not.

![Let's do this!](https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif)

Someone would ask, what about the other UUIDs? They were somehow not vulnerable when I tested.

Thank you for your time. And I hope you enjoyed reading this.

### Timeline

##### Dec 7, 2018 - Report Sent

##### Dec 7, 2018 - Comment from Triager and downgraded severity from Medium to Low

##### Dec 7, 2018 - Flagged the downgrade as a misunderstanding

##### Dec 10, 2018 - Comment from the team and report mistakenly flagged as duplicate

##### Dec 12, 2018 - Report state changed and severity upgraded from Low to Medium

##### Dec 20, 2018 - Bounty Awarded

##### June 13, 2019 - Fix Requested and Confirmed

Share on [](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f)[](https://twitter.com/intent/tweet/?text=I%20just%20read%20"IDOR%20via%20Websockets"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f)[](mailto:?subject=I%20just%20read%20"IDOR%20via%20Websockets"&body=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f&title=I%20just%20read%20"IDOR%20via%20Websockets"&summary=I%20just%20read%20"IDOR%20via%20Websockets"&source=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f)[](https://reddit.com/submit/?url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f&resubmit=true&title=I%20just%20read%20"IDOR%20via%20Websockets")[](whatsapp://send?text=I%20just%20read%20"IDOR%20via%20Websockets"%20https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f)[](https://news.ycombinator.com/submitlink?u=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f&t=I%20just%20read%20"IDOR%20via%20Websockets")[](https://telegram.me/share/url?text=I%20just%20read%20"IDOR%20via%20Websockets"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-websockets%2f)
