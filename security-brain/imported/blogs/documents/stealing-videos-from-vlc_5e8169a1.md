---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-26_stealing-videos-from-vlc.md
original_filename: 2020-03-26_stealing-videos-from-vlc.md
title: Stealing Videos From VLC
category: documents
detected_topics:
- idor
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 5e8169a1437956e8bea29034cd1558ff1af82535872c02528b78b97bd998009d
text_sha256: a55ebf71e8a7ccbab116a89a7adcceec73b6ec30483def74c013397777b081e1
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing Videos From VLC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-26_stealing-videos-from-vlc.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `5e8169a1437956e8bea29034cd1558ff1af82535872c02528b78b97bd998009d`
- Text SHA256: `a55ebf71e8a7ccbab116a89a7adcceec73b6ec30483def74c013397777b081e1`


## Content

---
title: "Stealing Videos From VLC"
page_title: "Stealing videos from vlc ~ inputzero"
url: "https://www.inputzero.io/2020/03/idor-in-vlc-ios.html"
final_url: "https://www.inputzero.io/2020/03/idor-in-vlc-ios.html"
authors: ["Dhiraj (@RandomDhiraj)"]
programs: ["Internet Bug Bounty"]
bugs: ["IDOR"]
publication_date: "2020-03-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4691
---

#  [Stealing videos from vlc](https://www.inputzero.io/2020/03/idor-in-vlc-ios.html)

Written by [Dhiraj](https://www.blogger.com/profile/17432054824339572035 "author profile") on [07:36](https://www.inputzero.io/2020/03/idor-in-vlc-ios.html "permanent link") in [IDOR](https://www.inputzero.io/search/label/IDOR), [iOS](https://www.inputzero.io/search/label/iOS), [VLC](https://www.inputzero.io/search/label/VLC) with [ No comments ](https://www.inputzero.io/2020/03/idor-in-vlc-ios.html#comment-form) [ ![](https://img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=7052034537728065557&postID=473290635397055667&from=pencil "Edit Post")

**Summary:**  
VLC for iOS was vulnerable to an unauthenticated insecure direct object reference (IDOR) which could allow a local attacker to steal media from the storage by just navigating to the source URL/IP.  
  
This was possible by abusing a functionality in the iOS application for VLC, which allows a user to share files with others over WiFi. This can be simply done by enabling "Network **>** Sharing via WiFi" and the web-server for this functionality works on port 80(http) protocol.  
  
**Technical analysis:**  
Let's assume a scenario where Bob & Alice are sharing a video over the WiFi using vlc-iOS, Eve could perform this attack by crawling the source IP address of Bob which would list the URL's of the videos shared between Bob & Alice.  
  
Having said that, navigating to those URL's Eve could simply steal the video without Bob's knowledge which successfully leads to unauthenticated IDOR.  
  
In the below image, Bob's IP is 192.168.1.135 and the hierarchy of stored videos in Bob's phone would look like,  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidVkjoWnDc-X6iRjAxRCvt5PprkdeHeLdd0DP50vkTYGSXKLzOxlflFVUcE2R-bqZGdqi5i_F3nQNQ-QJ7F4Zc5o031cONwdq2r5l8iVf67J_Dh-XUaw-LgQF501fwefSTL9yNOuwFJlc/s1600/VlC-iOS.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidVkjoWnDc-X6iRjAxRCvt5PprkdeHeLdd0DP50vkTYGSXKLzOxlflFVUcE2R-bqZGdqi5i_F3nQNQ-QJ7F4Zc5o031cONwdq2r5l8iVf67J_Dh-XUaw-LgQF501fwefSTL9yNOuwFJlc/s1600/VlC-iOS.png)

  
Such things can be crawled via burpsuite or you can use python scrapy to extract the URL's from the host and download the videos.  
  
**Mitigation from VLC Security team:**  
They implemented a user-friendly authentication mechanism on VLC iOS web server for WiFi Sharing. Passcode authentication is enabled when VLC's passcode setting is enabled and the user uses the passcode that he set in VLC's settings to log into Wifi Sharing.  
  
This was reported on 2nd Jan 2019 and patched on 10th Feb 2020 whereas fixed version was publicly released in March 2020. Post mitigation VLC published an advisory for this which you can view [here](https://code.videolan.org/videolan/vlc-ios/blob/master/Docs/NEWS#L3). Aside this issue was accepted for bounty on [The Internet](https://hackerone.com/internet/thanks).  
  
**Update** Friday, 22 May 2020: Advisory from VLC Security[[1](https://www.videolan.org/security/sb-vlc309.html)]

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://www.inputzero.io/2020/03/idor-in-vlc-ios.html&t=Stealing videos from vlc "Share this on Facebook")[__](https://twitter.com/home?status=Stealing videos from vlc -- https://www.inputzero.io/2020/03/idor-in-vlc-ios.html "Tweet This!")[__](https://plus.google.com/share?url=https://www.inputzero.io/2020/03/idor-in-vlc-ios.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=https://www.inputzero.io/2020/03/idor-in-vlc-ios.html&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidVkjoWnDc-X6iRjAxRCvt5PprkdeHeLdd0DP50vkTYGSXKLzOxlflFVUcE2R-bqZGdqi5i_F3nQNQ-QJ7F4Zc5o031cONwdq2r5l8iVf67J_Dh-XUaw-LgQF501fwefSTL9yNOuwFJlc/s1600/VlC-iOS.png&description=Stealing videos from vlc "Share on Pinterest")

[Email This](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=473290635397055667&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=473290635397055667&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=473290635397055667&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=473290635397055667&target=facebook "Share to Facebook")
