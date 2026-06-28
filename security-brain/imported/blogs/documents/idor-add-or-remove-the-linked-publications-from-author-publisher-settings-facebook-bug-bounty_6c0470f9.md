---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-29_idor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebo.md
original_filename: 2021-12-29_idor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebo.md
title: '[IDOR] add or remove the linked publications from Author Publisher settings
  — Facebook Bug Bounty'
category: documents
detected_topics:
- idor
- command-injection
- otp
- graphql
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- graphql
- mobile-security
language: en
raw_sha256: 6c0470f9f32a3e6ca9a2580e2eb7e10933b8d22065a32b215b55995a9b60cab7
text_sha256: 31d3a91ad3361272d434ed4fe11c22eeb677368b4107a65ec383c880a75415ad
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# [IDOR] add or remove the linked publications from Author Publisher settings — Facebook Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-29_idor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebo.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `6c0470f9f32a3e6ca9a2580e2eb7e10933b8d22065a32b215b55995a9b60cab7`
- Text SHA256: `31d3a91ad3361272d434ed4fe11c22eeb677368b4107a65ec383c880a75415ad`


## Content

---
title: "[IDOR] add or remove the linked publications from Author Publisher settings — Facebook Bug Bounty"
page_title: "[IDOR] add or remove the linked publications from Author Publisher settings — Facebook Bug Bounty | SERVICENGER"
url: "https://servicenger.com/mobile/idor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebook-bug-bounty/"
final_url: "https://servicenger.com/mobile/idor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebook-bug-bounty/"
authors: ["Rahul Kankrale (@RahulKankrale)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "863"
publication_date: "2021-12-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3051
---

# [IDOR] add or remove the linked publications from Author Publisher settings — Facebook Bug Bounty

Posted  Dec 29, 2021 

[![Preview Image](/assets/uploads/2021/12/linkedfb-e1640625131954.png)](/assets/uploads/2021/12/linkedfb-e1640625131954.png)

By _Rahul Kankrale_

_1 min_ read

Facebook Linked Publications ( [Authorship or Author Tag](https://www.facebook.com/formedia/blog/using-author-tags-to-grow-your-audience) ) feature was designed to give journalists more credit and visibility for the articles they were writing, regardless of where they were being published and it resulted in the byline that you saw in many posts, as well as the ability to easily follow that journalist and see when they shared new articles publicly.

To use that feature authors were needed to give permission for a publication or a website (and specifically the FB page of that site) in order to be cited as the author in Facebook’s byline feature.

As such, the _authors_ were needed to login to their own Facebook profile and in Settings (for their own profile) required to click “[Linked Publications](https://www.facebook.com/formedia/blog/using-author-tags-to-grow-your-audience)” (Or just send them to this link: <https://www.facebook.com/settings?tab=author_publisher> )

There, they were needed to add/remove the publication’s (or site’s) Facebook page as a “linked publication.”

This feature was vulnerable to Indirect object reference (IDOR) which could have led attacker to add or remove the approved publications from Author Publisher settings.

* * *

To reproduce follow graphQL request:  
Vulnerable parameter: `author_id` and `publisher_id`  
Access Token: First party token (Android)

  1. **Add publication in victim’s setting:**  
`author_id` was victims profile id and `publisher_id` was any media/news page id. [![Add publication](/assets/uploads/2021/12/fbadd1-1024x169.png)](/assets/uploads/2021/12/fbadd1-1024x169.png)[![Add Publication Response](/assets/uploads/2021/12/fbresponnnse-e1640714448799-1024x226.png)](/assets/uploads/2021/12/fbresponnnse-e1640714448799-1024x226.png)

  2. **Remove publication from victim’s setting:**[![](/assets/uploads/2021/12/removeFacebookPublication-1024x189.png)](/assets/uploads/2021/12/removeFacebookPublication-1024x189.png)[![Remove Facebook Author Publication Response](/assets/uploads/2021/12/removeFacebookPublicationResponse-1024x290.png)](/assets/uploads/2021/12/removeFacebookPublicationResponse-1024x290.png)

* * *

**Timeline:**

  * 27/05/2021: Report submitted.
  * 27/05/2021: Triaged.
  * 07/06/2021: Fixed (Add/Remove vulnerability patched but I was able to see previously approved publications of any page)
  * 21/07/2021: Bounty -> $750 + $75 (Gold league Bonus) + $38 (Delay bonus)
  * 28/09/2021: FB replied: _The product team decided to remove the add and remove functionality for this feature and cleanup for this feature is still going on, since add/remove functionality is not available now and you are only able to see the previously added settings_.
  * 07/12/2021: Feature completely removed and the clean of this issue is completed.

__[Mobile](/categories/mobile/), [Android](/categories/android/), [Web](/categories/web/)

__[author-tag](/tags/author-tag/) [bugbounty](/tags/bugbounty/) [facebook](/tags/facebook/) [facebook-publications](/tags/facebook-publications/) [idor](/tags/idor/)

This post is licensed under [ CC BY 4.0 ](https://creativecommons.org/licenses/by/4.0/) by the author.

Share [ __](https://twitter.com/intent/tweet?text=\[IDOR\]%20add%20or%20remove%20the%20linked%20publications%20from%20Author%20Publisher%20settings%20%E2%80%94%20Facebook%20Bug%20Bounty%20-%20SERVICENGER&url=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fidor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebook-bug-bounty%2F "Twitter") [ __](https://www.facebook.com/sharer/sharer.php?title=\[IDOR\]%20add%20or%20remove%20the%20linked%20publications%20from%20Author%20Publisher%20settings%20%E2%80%94%20Facebook%20Bug%20Bounty%20-%20SERVICENGER&u=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fidor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebook-bug-bounty%2F "Facebook") [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fidor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebook-bug-bounty%2F "Linkedin") [ __](https://t.me/share/url?url=https%3A%2F%2Fwww.servicenger.com%2Fmobile%2Fidor-add-or-remove-the-linked-publications-from-author-publisher-settings-facebook-bug-bounty%2F&text=\[IDOR\]%20add%20or%20remove%20the%20linked%20publications%20from%20Author%20Publisher%20settings%20%E2%80%94%20Facebook%20Bug%20Bounty%20-%20SERVICENGER "Telegram") __
