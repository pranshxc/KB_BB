---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-24_facebook-stories-disclose-facebook-friend-list.md
original_filename: 2017-08-24_facebook-stories-disclose-facebook-friend-list.md
title: Facebook stories disclose Facebook friend list
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
- business-logic
language: en
raw_sha256: b5ae984f6a018e43be490e3774665898a4e74ae163e8eff0a19f23c35df49a20
text_sha256: 6db0f233ee549221e9b8a6c08db7a2f4c0fd95b49d55be0534a91b1f8f30ede9
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook stories disclose Facebook friend list

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-24_facebook-stories-disclose-facebook-friend-list.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `b5ae984f6a018e43be490e3774665898a4e74ae163e8eff0a19f23c35df49a20`
- Text SHA256: `6db0f233ee549221e9b8a6c08db7a2f4c0fd95b49d55be0534a91b1f8f30ede9`


## Content

---
title: "Facebook stories disclose Facebook friend list"
page_title: "Facebook stories disclose Facebook friend list - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/facebook-stories-disclose-facebook-friend-list/"
final_url: "https://philippeharewood.com/facebook-stories-disclose-facebook-friend-list/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2017-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6122
---

Posted on [August 24, 2017](https://philippeharewood.com/facebook-stories-disclose-facebook-friend-list/)

# Facebook stories disclose Facebook friend list

Given a Facebook user with a friend list set to “Only me” if this user posts a Facebook story to his/her bucket with privacy set to “Friends”, this will leak the user’s friend list.  
[Facebook Stories](https://techcrunch.com/2017/01/25/facebook-stories/) are what makes the sequel to Instagram stories, short media content served via photo or video. Stories are placed into a profile bucket which can be tapped to view.  
In the camera settings for Facebook Stories, show an area for privacy selections.  
![](http://philippeharewood.com/wp-content/uploads/2017/10/cameraprivacy.png)  
If a user’s friend list was set to “Only me” changing the above to “Friends” would set the privacy option for the object to “Friends” of this user. In [GraphQL](http://facebook.com/notes/phwd/a-facebook-graphql-crash-course/1189337427822946/) there was a way to see this privacy option for any user as long as the user is a friend.
  
  
  
  node(USER_ID)
  {
  story_bucket {
  nodes {
  id,
  stories_bucket_privacy {
  preview_users {
  nodes {
  id,
  name
  }
  }
  }
  }
  }
  }
  
  

The `preview_users` field allowed the audience (in this case whoever can see the story) to see which users can see this story. Since the option was to set “Friends” it disclosed the friend list even though “Only me” was set.  
![](http://philippeharewood.com/wp-content/uploads/2017/10/Editprivacy.png)  
**Impact**  
A user’s friend list can be disclosed via a Facebook story regardless of the user’s friend list privacy setting and the bug can be exploited by the audience of the story, in this case, friends.  
**Timeline**

  * Aug 24, 2017 – Report sent
  * Aug 29, 2017 – Request for additional details by Facebook
  * Aug 29, 2017 – Additional details sent
  * Aug 30, 2017 – Further investigation by Facebook
  * Oct 11, 2017 – Patched by Facebook
  * Oct 19, 2017 – Bounty awarded by Facebook
