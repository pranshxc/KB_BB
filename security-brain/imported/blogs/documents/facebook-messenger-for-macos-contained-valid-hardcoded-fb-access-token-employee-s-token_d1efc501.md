---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-23_facebook-messenger-for-macos-contained-valid-hardcoded-fb-access-token-employees.md
original_filename: 2021-09-23_facebook-messenger-for-macos-contained-valid-hardcoded-fb-access-token-employees.md
title: Facebook Messenger for MacOS contained valid hardcoded FB access token (employee's
  token?)
category: documents
detected_topics:
- command-injection
- otp
- api-security
tags:
- imported
- documents
- command-injection
- otp
- api-security
language: en
raw_sha256: d1efc5018fc672773598ae09b231cc1aa151d76635c94e0a09fc156ed015d55b
text_sha256: 3939fd7b83a78baa75fda84519d9e2b1d12d9ae76e317957a8ab6a1ef23b44b0
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Messenger for MacOS contained valid hardcoded FB access token (employee's token?)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-23_facebook-messenger-for-macos-contained-valid-hardcoded-fb-access-token-employees.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d1efc5018fc672773598ae09b231cc1aa151d76635c94e0a09fc156ed015d55b`
- Text SHA256: `3939fd7b83a78baa75fda84519d9e2b1d12d9ae76e317957a8ab6a1ef23b44b0`


## Content

---
title: "Facebook Messenger for MacOS contained valid hardcoded FB access token (employee's token?)"
url: "https://www.vulnano.com/2021/09/facebook-messenger-for-macos-contained.html"
final_url: "https://www.vulnano.com/2021/09/facebook-messenger-for-macos-contained.html"
authors: ["Dzmitry Lukyanenka (@vulnano)"]
programs: ["Meta / Facebook"]
bugs: ["Hardcoded credentials"]
bounty: "625"
publication_date: "2021-09-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3291
---

###  Facebook Messenger for MacOS contained valid hardcoded FB access token (employee's token?) 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

By  [ Dzmitry ](https://www.blogger.com/profile/06784930502399670573 "author profile") \-  [ September 23, 2021  ](https://www.vulnano.com/2021/09/facebook-messenger-for-macos-contained.html "permanent link")

At summer I decided to test Facebook Messenger for MacOS. Grepped all urls from code and started to analyze them. Quickly I noticed few urls on image with "access_token" value:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-T7pdNx2pdGyw_IDcWI11VSUuanca7_JRMJC-dkr0yZz7Wf6lHxmkzxJj_CzJ6CDNvDwUDev6LVNZ_1e_dcP6XHlm_9PoYGf-i0TomW-KhjbhQZHMrX85nrsjfYNb2nKD9_tIifRghyphenhyphenlV/w640-h180/facebook_messenger_macos_token_check_public2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-T7pdNx2pdGyw_IDcWI11VSUuanca7_JRMJC-dkr0yZz7Wf6lHxmkzxJj_CzJ6CDNvDwUDev6LVNZ_1e_dcP6XHlm_9PoYGf-i0TomW-KhjbhQZHMrX85nrsjfYNb2nKD9_tIifRghyphenhyphenlV/s1096/facebook_messenger_macos_token_check_public2.png)

  

Cool! Interesting is this token still valid?

I opened https://developers.facebook.com/tools/debug/accesstoken/?access_token= and got confirmation: the token is valid!

I stopped experiments and rapidly sent report to Facebook Team.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgE81Vs3igpKccWlQ4jUPldDNIp2PU1y4iurCMbnL7Q_9-saLZ_qzOjQwW5IwnLa0qB2Z9mcKtJu_2P4xxrutR-uJGJaG9BvTVgCdFt_m0jrU2r8lmwZzjyjDjITLAsBWvsZCE7ecFQnKn/w640-h365/facebook_messenger_macos_token_check_public.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgE81Vs3igpKccWlQ4jUPldDNIp2PU1y4iurCMbnL7Q_9-saLZ_qzOjQwW5IwnLa0qB2Z9mcKtJu_2P4xxrutR-uJGJaG9BvTVgCdFt_m0jrU2r8lmwZzjyjDjITLAsBWvsZCE7ecFQnKn/s1646/facebook_messenger_macos_token_check_public.png)

  

  

All time before bounty decision I hoped that this token had some extra internal permissions. Unfortunately for me looks like it was just normal token, probably from Facebook employee, without any extra access. I think some software developer placed such link by mistake inside the app and it went over whole world))

So, be careful and attentive when you investigate hardcoded data inside apps ;)  

  * Facebook Messenger v. 97.11.116 (97.11.116.283083801) for MacOS
  * Submitted: 27.07.2021 10:08AM
  * Triaged: 27.07.2021 12:36AM
  * Fixed: 27.07.2021 12:45AM (token became invalid, may be system automatically invalidated the token or Facebook team did it)
  * Fix notification: 04.08.2021
  * Reward: $500 (+$125 bonus) 08.09.2021

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps
