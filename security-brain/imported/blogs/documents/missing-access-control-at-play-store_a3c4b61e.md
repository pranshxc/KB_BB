---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-03_missing-access-control-at-play-store.md
original_filename: 2019-06-03_missing-access-control-at-play-store.md
title: Missing access control at play store
category: documents
detected_topics:
- access-control
- xss
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- xss
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: a3c4b61e9927bda7f3ab8bf8da4ba89cd65a9aa017308c1b06c7c21ebb97e507
text_sha256: cccdea5c40cb62321509cdfc1c21a94ff4bfb766a0824dd731f26e6021bf53c9
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Missing access control at play store

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-03_missing-access-control-at-play-store.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `a3c4b61e9927bda7f3ab8bf8da4ba89cd65a9aa017308c1b06c7c21ebb97e507`
- Text SHA256: `cccdea5c40cb62321509cdfc1c21a94ff4bfb766a0824dd731f26e6021bf53c9`


## Content

---
title: "Missing access control at play store"
page_title: "Missing access control at play store – Vishwaraj Bhattrai"
url: "https://vishwarajbhattrai.wordpress.com/2019/06/03/missing-access-control-at-play-store/"
final_url: "https://vishwarajbhattrai.wordpress.com/2019/06/03/missing-access-control-at-play-store/"
authors: ["Vishwaraj Bhattrai (@vishwaraj101)"]
programs: ["Google"]
bugs: ["Broken authorization"]
publication_date: "2019-06-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5234
---

**Summary:**

Google play store developer account has an invite feature which allows admin user to invite other colleagues/developers for managing the account as well as app releases. With this issue, an invited user with limited permissions was able to see the information of other apps as well, which was not permitted by the account owner.  
**  
Steps to reproduce:**

1.) Login to <https://play.google.com/apps/publish/> as owner A using chrome.  
2.) Now from A account visit Settings > Developer account > Users & Permissions.  
3.) Now send an invite to user B with read-only permissions.  
4.) Click on invited link and login to B account using Firefox.  
5.) Now from A account change the user B permissions and restrict its visibility to one app with read-only permissions.  
6.) Now from B account hit refresh he will only be able to see one app which is permitted by user A from dashboard he cannot see the other listed apps.  
7.) To bypass this check just visit this URL from B account  
<https://play.google.com/apps/publish/?account=5765075562513459389#StatisticsPlace:p=com.dummiesguideto.indiantrain>  
8.) Where 5765075562513459389 is account id which will be there by default and com.dummiesguideto.indiantrain is the package name of the app.  
9.) Now user B is able to watch the information of other apps which are present in A account despite A has applied the restrictive view of apps for user B.  
**  
[Video Poc](https://www.youtube.com/watch?v=Bu9XKyDrybI&feature=youtu.be)**

**Timeline:  
**6-April-2018-Reported.  
6-April-2018-Triaged.  
17-April-2018-Fixed and 5k bounty was rewarded.  
5-Sept-2018-Granted permission for public disclosure.

Thank you for reading 🙂

### Share this:

  * [ Share on X (Opens in new window) X ](https://vishwarajbhattrai.wordpress.com/2019/06/03/missing-access-control-at-play-store/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://vishwarajbhattrai.wordpress.com/2019/06/03/missing-access-control-at-play-store/?share=facebook)
  * 

Like Loading…

Published by

vishwaraj bhattrai

Security enthusiast
