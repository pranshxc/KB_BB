---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-21_delete-any-video-or-reel-on-facebook-11250.md
original_filename: 2022-12-21_delete-any-video-or-reel-on-facebook-11250.md
title: Delete any Video or Reel on Facebook (11,250$)
category: documents
detected_topics:
- mobile-security
- idor
- command-injection
- otp
- graphql
- api-security
tags:
- imported
- documents
- mobile-security
- idor
- command-injection
- otp
- graphql
- api-security
language: en
raw_sha256: 4e0efd3bb4e8494843abc8b7aa735b858532cde485a17b28474cf11b5e33ec69
text_sha256: e332f6d0bb50fe831f0112fc4fc2068142585d12a716b15c61105e04048a8118
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Delete any Video or Reel on Facebook (11,250$)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-21_delete-any-video-or-reel-on-facebook-11250.md
- Source Type: markdown
- Detected Topics: mobile-security, idor, command-injection, otp, graphql, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `4e0efd3bb4e8494843abc8b7aa735b858532cde485a17b28474cf11b5e33ec69`
- Text SHA256: `e332f6d0bb50fe831f0112fc4fc2068142585d12a716b15c61105e04048a8118`


## Content

---
title: "Delete any Video or Reel on Facebook (11,250$)"
page_title: "Delete any Video or Reel on Facebook (11,250$) | Bugreader"
url: "https://bugreader.com/social/write-ups-general-delete-any-video-or-reel-on-facebook-11-250--100965"
final_url: "https://bugreader.com/social/write-ups-general-delete-any-video-or-reel-on-facebook-11-250--100965"
authors: ["Bassem M Bazzoun (@bassemmbazzoun)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "11,250"
publication_date: "2022-12-21"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1750
---

[Bugreader Social](./)

  * [All Posts](./)
  * [ Write ups ]()

[All](./write-ups)[General](./write-ups:general)

  * [ Tutorials ]()

[All](./tutorials)[General](./tutorials:general)[Setup](./tutorials:setup)[Reverse Engineering](./tutorials:reverse-engineering)

  * [ Hackers Spotlight  ]()

[All](./hackers-spotlight-)[General](./hackers-spotlight-:general)

  * [ Challenges  ]()

[All](./challenges-)[General](./challenges-:general)

  * [ Bug Validity ]()

[All](./bug-validity)[General](./bug-validity:general)[Best Practices](./bug-validity:best-practices)

  * [ __Home](/)
  * [ __Reports](/reports)
  * [ __Social](/social/)
  * [ __Researchers](/researchers)
  * [ __Login](/secure/?redirect=social)
  * [ __Register](/secure/register.php)

![Bugreader](/a/logosimple.png)  
Loading post ...

###  [Delete any Video or Reel on Facebook (11,250$)](https://bugreader.com/social/100965)

![](https://bugreader.com/data/profile/63a311d988ab5167163132163a311d988f5b1671631321239131.jpeg)

**[Bassem Bazzoun](/bassembazzoun_)**  
Last Update: **21 Dec 2022 . 14:29 PM** in **[Write ups](./write-ups) ** . **[General](./write-ups:general)** in **Facebook**

__Copy Link

__Share

[__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://bugreader.com/social/100965) [__Twitter](https://twitter.com/intent/tweet?url=https://bugreader.com/social/100965) [__Whatsapp](https://wa.me/?text=https://bugreader.com/social/100965) [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://bugreader.com/social/100965)

###  Setting my goal 

While I was attempting to discover more vulnerabilities as part of Facebook's bug bounty program, I spent about two weeks without success. I began to feel like there were no more bugs on Facebook, but I continued to try and eventually realized that the issue was with my approach and not necessarily the lack of vulnerabilities on the platform. I understood that **vulnerabilities never truly end** and that in order to find a bug, I needed to change my way of thinking. With this new perspective, I was confident that I would eventually discover a bug. 

The first thing I did was to start testing every endpoint in Facebook, believing that every endpoint was potentially vulnerable. My goal was to focus on finding critical bugs, as I believed that by determining my focus and sticking to it, I would be more likely to achieve my goal. With this mindset, I began testing for IDOR vulnerabilities, specifically focusing on the ability to delete photos, videos, or disclose sensitive information. 

[![](https://i.imgur.com/DlYk8nM.gif)](https://i.imgur.com/DlYk8nM.gif)

### The Full story

I began searching for critical bugs and thoroughly testing various endpoints, not underestimating any of them. Eventually, I came across a feature in the Meta business suite that allowed me to upload a "Reel" to my page. When uploading a video, I noticed that I had the option to "Crop" and "Trim" it. 

[![](https://i.imgur.com/SN7vM7i.png)](https://i.imgur.com/SN7vM7i.png)

The first thing that came to mind was to examine the request for **trimming** and attempt to trim other people's videos. For example, if someone uploaded a video on Facebook with a length of 10 minutes, I would try to trim the video from the start to the 1-second mark, which would make it appear as though the video had been deleted due to its shortened length. 

[![](https://i.imgur.com/vrYlnN3.png)](https://i.imgur.com/vrYlnN3.png)

Unfortunately, the trim function did not work. As a result, I shifted my focus to the second option, **"Cropping."** I had the idea to try cropping other people's videos and discovered that if I was able to crop them to a size of 1x1 pixel, it would make the videos appear as though they had been deleted or looks like distorted. Below is an image that explain the aspect ratio of the cropping option.

[![](https://i.imgur.com/MfZYX0z.png)](https://i.imgur.com/MfZYX0z.png)

Again! No success! After hours in trying to find a vulnerability in this feature, I wasn't able to find anything then I moved to another feature to test. The second day I wanted to start hunting again and I was trying to find a new feature in Meta business suite to test on and since I like the actions where there is cropping and trimming video I was like maybe should I give it a second try? (**Their is a daily updates and maybe now it's vulnerable**). So, I turned in Burp suite and started to dig into this features again :)

I started manipulating the requests in this features trying to delete the videos of my test account! And guess what? I noticed that one of my test account videos just disappeared! (A video of 54 mins length) I was like:

[![](https://i.imgur.com/DDbhJl9.gif)](https://i.imgur.com/DDbhJl9.gif)

I was 100% confident that there was a vulnerable endpoint among the ones I was testing. I quickly looked back at my Burp history and focused on the crop and trim request, **manipulating the crop parameters** again and sending a request to delete a video that I had uploaded to my test account! and again guess what?! 

BOOOM! The video was deleted and it took about 5 minutes for the deletion to be fully completed, which was why I hadn't noticed the vulnerability the previous day. Which indicates that the issue was with the crop parameters.

[![](https://i.imgur.com/z221atv.gif)](https://i.imgur.com/z221atv.gif)

I quickly began creating a report to send it to Facebook, knowing that the ability to delete any video on the platform would be rewarded with a **$10,000 bounty.**

[![](https://i.imgur.com/CJEKsQ1.gif)](https://i.imgur.com/CJEKsQ1.gif)

### Impact:

I was able to delete any video, live video and reels uploaded on Facebook. For example, I could have potentially deleted videos belonging to Leo Messi that have millions of views after he won the World Cup!

**_It is important to note that it is never acceptable to exploit a bug on a real user's account and that ethical hackers should always use a test account to avoid getting into trouble. It is crucial to remember that we have a responsibility to use our skills and knowledge for the greater good and not to cause harm or disruption._**

[![](https://i.imgur.com/Zc6MK5a.jpg)](https://i.imgur.com/Zc6MK5a.jpg)

### Reproduction steps:

Users setup:

\- UserAttacker

\- PageAttacker

\- UserVictim 

1\. From UserVictim upload any video on your Facebook profile.

2\. From UserAttacker get your Facebook android app access token to use it later.

3\. Perform the below graphql POST request using UserAttacker access token and manipulate the video_id to the video id of step 1 : 
  
  
  {
  "variables": {
  "videoClipsTimestamps": {
  "start_time_in_sec": 0.706,
  "end_time_in_sec": 7.721354166666667
  },
  "videoID": "VIDEO_ID_HERE",
  "reframeAspectRatios": [
  {
  "aspect_ratio_denominator": 11,
  "aspect_ratio_numerator": 1
  }
  ],
  "aggressiveness": 0
  },
  "doc_id": "8426940007331645"
  }

4\. Wait for 5 mins and BOOMMM! The video will be deleted :)

[![](https://i.imgur.com/lkV87Nn.png)](https://i.imgur.com/lkV87Nn.png)

The issue here was that the request was accepting any video ID and, when the aspect ratio parameters (**aspect_ratio_denominator** and**aspect_ratio_numerator**) were manipulated to unexpected values, the library responsible for reframing the videos would reframe the submitted video ID and return a broken video that was no longer loadable or accessible on the user's profile. 

> Timeline:

October 24, 2022- Report sent

October 25, 2022 — Triaged

November 30, 2022 — Bug Fixed (_The issue was fixed the next day after I reported it, but the confirmation fix message was sent in this day_)

December 13, 2022 - Bounty rewarded **(11,250$)** (10,000$ + 750$ Hacker Plus program bonus + 500$ bonus for delay) 

[![](https://i.imgur.com/haszHh1.png)](https://i.imgur.com/haszHh1.png)

[![](https://i.imgur.com/tTKUHwf.png)](https://i.imgur.com/tTKUHwf.png)

* * *

  
  
  
  
  

Developed by Mohammad Atwi - bugreader.com/mo

#### Notifications

×

#### Discussion: 

×

#### About Bugreader Editor

×

##### General Features:

###### 

  1. Press "Enter" to insert new text block. ![](./index_files/edoc/3.jpg)
  2. Press "Enter + Shift" so you can add multi-line text content in the same block. ![](./index_files/edoc/3.jpg)
  3. Drag and drop content reorder, so you can change any content position **using the gray right border**. ![](./index_files/edoc/1.jpg)
  4. Change content type, so you can replace the current content type with another. ![](./index_files/edoc/4.jpg)
  5. Add new content anywhere, so you can add any content after any block. The link/embed feature is coming soon. ![](./index_files/edoc/5.jpg)
  6. Inline text format: Headings, Bold, Italic and Links. ![](./index_files/edoc/2.jpg)
  7. You can also add Codes and embeded YouTube videos.
  8. Add images, with drag and drop support.
  9. Auto save feature.
  10. Draft / Published status for posts, you can change it anytime.

* * *

###### Developer's note: This's the version 1.0, I'll be happy to know your feedback about my editor, contact me at [[email protected]](/cdn-cgi/l/email-protection#1a77755a6f6a76757e6334797577)
