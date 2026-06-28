---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-07_server-side-request-forgery-on-vanilla-forums.md
original_filename: 2018-07-07_server-side-request-forgery-on-vanilla-forums.md
title: Server Side Request Forgery on Vanilla Forums
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 79bf7904ee370dc2867b2cf167d826155f2e2a3c2c29062b7ed75467dc959cfe
text_sha256: 993af4e732f388abac070238cd9b1576ee77c8d7e673c415a1f1cae06f1eeb62
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Server Side Request Forgery on Vanilla Forums

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-07_server-side-request-forgery-on-vanilla-forums.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `79bf7904ee370dc2867b2cf167d826155f2e2a3c2c29062b7ed75467dc959cfe`
- Text SHA256: `993af4e732f388abac070238cd9b1576ee77c8d7e673c415a1f1cae06f1eeb62`


## Content

---
title: "Server Side Request Forgery on Vanilla Forums"
page_title: "Server Side Request Forgery| #Vulnerability | Reported a Few Days Ago | Its Fixed Now | BugBounty Duplicate | #SSRF | #POC | Learn from the Error Please | Sorry for the Background Noise | 

Get… | Vikash Chaudhary | 32 comments"
url: "https://www.linkedin.com/feed/update/urn:li:activity:6421357227923337216"
final_url: "https://www.linkedin.com/feed/update/urn:li:activity:6421357227923337216"
authors: ["Vikash Chaudhary (@OffensiveHunter)"]
programs: ["Vanilla Forums"]
bugs: ["SSRF"]
publication_date: "2018-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5815
---

[ ](https://in.linkedin.com/in/offensivehunter?trk=public_post_feed-actor-image)

[ Vikash Chaudhary ](https://in.linkedin.com/in/offensivehunter?trk=public_post_feed-actor-name)

7y  Edited 

  * [ Report this post ](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)

Server Side Request Forgery| #Vulnerability | Reported a Few Days Ago | Its Fixed Now | BugBounty Duplicate | #SSRF | #POC | Learn from the Error Please | Sorry for the Background Noise | Get online Training by me for Penetration Testing | Bug Bounty Hunting. Regards! Vikash Chaudhary CEO & Founder (HackersEra Cyber Security Consultancy & Training PVT LTD) mail: [founder@hackersera.com](mailto:founder@hackersera.com?trk=public_post-text) cell : +91 9921910319 #BugHunting #BugBounty

…more 

`` ``

[ 181  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [ 32 Comments ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_social-actions-comments)

[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_like-cta) [ Comment  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment-cta) `` ``

Share 

  * Copy
  * LinkedIn
  * Facebook
  * X

[ ](https://uk.linkedin.com/in/mrr3boot?trk=public_post_comment_actor-image)

[ Suresh Narvaneni ](https://uk.linkedin.com/in/mrr3boot?trk=public_post_comment_actor-name) 7y 

  * [ Report this comment ](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Not a Vulnerability. It's functioning as per their design - Firing GET request to given URL. What else ? Any XSPA or LFR ?

[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_like) [ Reply  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_reply) [ 3 Reactions ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_reactions) 4 Reactions 

[ ](https://pk.linkedin.com/in/protector47?trk=public_post_comment_actor-image)

[ Muhammad Asim Shahzad ](https://pk.linkedin.com/in/protector47?trk=public_post_comment_actor-name) 7y 

  * [ Report this comment ](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Very informative!

[ Like  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_like) [ Reply  ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_reply) [ 1 Reaction ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_comment_reactions) 2 Reactions 

[ See more comments ](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_see-more-comments)

To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Foffensivehunter_server-side-request-forgery-vulnerability-activity-6421357227923337216-q9OF&trk=public_post_feed-cta-banner-cta)
