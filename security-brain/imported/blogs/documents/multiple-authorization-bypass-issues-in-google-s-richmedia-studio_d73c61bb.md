---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-24_multiple-authorization-bypass-issues-in-googles-richmedia-studio.md
original_filename: 2021-03-24_multiple-authorization-bypass-issues-in-googles-richmedia-studio.md
title: Multiple Authorization bypass issues in Google's Richmedia Studio
category: documents
detected_topics:
- sso
- idor
- access-control
- xss
- command-injection
- file-upload
tags:
- imported
- documents
- sso
- idor
- access-control
- xss
- command-injection
- file-upload
language: en
raw_sha256: d73c61bb6c7fb07a6a89d7c28ec29ec5cfdb5cb7153e6132b6b6627128634b53
text_sha256: f1692313e6d0dfad1099349cc4f6add472a91c0e140d3ab5214c8fafc544c9bd
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Authorization bypass issues in Google's Richmedia Studio

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-24_multiple-authorization-bypass-issues-in-googles-richmedia-studio.md
- Source Type: markdown
- Detected Topics: sso, idor, access-control, xss, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `d73c61bb6c7fb07a6a89d7c28ec29ec5cfdb5cb7153e6132b6b6627128634b53`
- Text SHA256: `f1692313e6d0dfad1099349cc4f6add472a91c0e140d3ab5214c8fafc544c9bd`


## Content

---
title: "Multiple Authorization bypass issues in Google's Richmedia Studio"
url: "https://www.ehpus.com/post/multiple-authorization-bypass-issues-in-google-s-richmedia-studio"
final_url: "https://www.ehpus.com/post/multiple-authorization-bypass-issues-in-google-s-richmedia-studio"
authors: ["Zohar Shachar"]
programs: ["Google"]
bugs: ["Broken authorization"]
bounty: "6,000"
publication_date: "2021-03-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3793
---

# Multiple Authorization bypass issues in Google's Richmedia Studio

  * zohar shachar
  * Mar 24, 2021
  * 5 min read

Ah, [_Google research grants_](https://www.google.co.il/about/appsecurity/research-grants/) , how effective you are! It seems as if exactly in these times when my energy levels are low, and I just-can’t-get-motivated to sit down and do something, exactly then a new ‘research grant’ lands in my mailbox and kicks me into gear. 

And so was the case a few months ago, where after a long break from research a wonderful email arrived - a new ‘vulnerability research grant’ for October 2020. Exciting indeed! And not only that, the research target included a Google app I’ve never encountered before, “Richmedia Studio” - a marketing campaign management platform. New (for me) target & a research grant? And it’s not even my bday! Let’s see where it goes.

  

**Challenge one: Accessing the system**

This is not much of a security issue, but I still found it interesting and it sure opened my mind regarding Google’s attack surface - you cannot just ‘stumble upon’ the Richmedia studio. If your account is not configured to use it, you will not see it, not even an ‘unauthorized’ page, you will simply be navigated away (give it a go and try to access [https://www.google.com/doubleclick/studio](https://www.google.com/doubleclick/studio/#qa/campaigns)). This is probably a key factor in why I’ve never stumbled upon this app before, even though I spent (and still spending) significant efforts searching for Google’s systems.

If you want to access the system, you should first [_fill a form here_](https://support.google.com/richmedia/answer/2389093) , afterwords (if Google grants you access), you will receive an email invite which will allow you to access the system. Welcome to Richmedia!

![](https://static.wixstatic.com/media/5527e6_22184fdc57f44456ab6ac7b5705a01db~mv2.png/v1/fill/w_49,h_29,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_22184fdc57f44456ab6ac7b5705a01db~mv2.png)

**Poking around**

So what are you, Richmedia studio? From what I could understand, the platform is used to manage online advertising campaigns, and relations with advertisers. A role management system allows administrators to create new campaigns and upload media to these campaigns (media such as HTML pages, videos, images, etc.). The admin can then give different advertisers access to the campaign, as well as run it through QA (all managed via permissions), leave comments, etc. As I don’t really understand the flow of marketing campaigns I’m sure I’m not doing this platform justice in this short description, but for our purpose it will do fine. 

  

**First vulnerability: accessing other users media [500$ bounty]**

I started by looking at the media uploads. I was expecting to see the same mechanism as in most google apps, where uploaded files are stored under the user’s google Drive, and exposed via a temporary ‘googleusercontent’ link with a long, random ID. But that was not the case. In Richmedia, files are uploaded to a different domain - ‘[ _s0.2mdn.net_](http://s0.2mdn.net/) '. An example link can be seen here: 

[_https://s0.2mdn.net/preview/CgkIARCom4rX5i4SGQCkoPPIITT873VA4lA-bButtVLChPwsXnU/ads/richmedia/studio/60019864/60019864_20201004010909357_xsspng.png_](https://s0.2mdn.net/preview/CgkIARCom4rX5i4SGQCkoPPIITT873VA4lA-bButtVLChPwsXnU/ads/richmedia/studio/60019864/60019864_20201004010909357_xsspng.png)

  

Hosting the files on a separate (non ‘google’) domain raises the question of authorization, as the browser holds no cookies for this domain (of course authorization can be solved via other means), and Indeed trying to access an example uploaded file from an anonymised browser showed that no auth is required. However, that on its own is not really an issue. The link is complex and cannot be realistically brute-forced or guessed. However, looking at this link, the ‘preview’ key jumped to my eye. Is this the actual path where the file is stored, or just a link to a ‘preview’ generated from the actual source? 

I Uploaded another file and followed the network requests more closely, and found my suspicion was correct - in a separate HTTP response, a direct link to the file (and not to its ‘preview’) is returned to the browser. This link looks much simpler: 

[_http://s0.2mdn.net/ads/richmedia/studio/pv2/61580927/20201004040915088/xsspng.png_](http://s0.2mdn.net/ads/richmedia/studio/pv2/61580927/20201004040915088/xsspng.png)

  

These direct links are also accessible without auth, and can be generated by an attacker (the first 8 digits are just the merchant ID that can be enumerated from the studio app, and the later consists of the upload date and a short random number). 

  

So here we have a clear IDOR - A guessable link to another user file, without auth. 

I’ve reported this to Google, which accepted the bug and issued a 500$ bounty.

  

**Strike 2: Accessing other users campings [5000$ bounty]**

Honestly, this one was so simple I really didn’t think it would work. If you recall, I mentioned above that studio offers a role-management system. In particular, you can create an account without access to the QA dashboard. And indeed, if you create such a user, the dashboard will look different.

  

Admin dashboard:

![](https://static.wixstatic.com/media/5527e6_2df898d827e847d2b9285878242749c0~mv2.png/v1/fill/w_49,h_8,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_2df898d827e847d2b9285878242749c0~mv2.png)

Limited account dashboard: 

![](https://static.wixstatic.com/media/5527e6_5b886b4e148c4abda5ba37467959c922~mv2.png/v1/fill/w_49,h_6,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_5b886b4e148c4abda5ba37467959c922~mv2.png)

I know what you think here. Google is too good for ‘security-by-obscurity’ sort of stuff, right? I mean there is no-way that if I try to access the QA page with the limited account it will just work.. Right? 

Well, I had to try. The results were… surprising: 

![](https://static.wixstatic.com/media/5527e6_568bda18ae754129a31641dd3fa43b4f~mv2.png/v1/fill/w_49,h_26,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_568bda18ae754129a31641dd3fa43b4f~mv2.png)

Not only that I could access the QA page for the campaigns my user was associated with, I could see all campaigns, of all accounts! 

By some weird ‘fail to true’ bug, if you have permission to see nothing, you could see everything! I had to verify it a few times to believe it myself ;) I’ve reported the issue to Google which issued a 5000$ bounty.

  

**Strike 3: GWT**

Google Richmedia studio is using [_GWT_](http://www.gwtproject.org/) for it's API's. One of the [_first issues I ever found in a Google system_](https://www.komodosec.com/post/google-groups-authorization-bypass) was a GWT authorization issue, and so I have a warm place in my heart for this technology. 

  

I decided to look again in the file upload process, this time paying closer attention to the GWT requests. Specifically, I looked at the HTTP request that retrieves the file download URL (the same long complex link we saw before), and noticed some weird strings sent as part of the HTTP POST body:
  
  
  7|0|8|[https://www.google.com/doubleclick/studio/gwt/|9DB073B0A4AFE75F8679003264944EE5|com.google.ads.api.gwt.rpc.client.BatchedInvocationService|invoke|com.google.ads.api.gwt.rpc.client.BatchedInvocationRequest/2983766987|com.google.ads.richmedia.studio.ui.common.grubby.client.BatchedInvocationRequestHeaderImpl/3117963532|java.util.ArrayList/4159755760|com.google.ads.richmedia.studio.service.CreativeServiceGwt$GetDownloadArchiveUrlRequest/1562479252|1|2|3|4|1|5|5|6|0|7|1|8|DlQXE|DlQWU|](https://www.google.com/doubleclick/studio/gwt/%7C9DB073B0A4AFE75F8679003264944EE5%7Ccom.google.ads.api.gwt.rpc.client.BatchedInvocationService%7Cinvoke%7Ccom.google.ads.api.gwt.rpc.client.BatchedInvocationRequest/2983766987%7Ccom.google.ads.richmedia.studio.ui.common.grubby.client.BatchedInvocationRequestHeaderImpl/3117963532%7Cjava.util.ArrayList/4159755760%7Ccom.google.ads.richmedia.studio.service.CreativeServiceGwt$GetDownloadArchiveUrlRequest/1562479252%7C1%7C2%7C3%7C4%7C1%7C5%7C5%7C6%7C0%7C7%7C1%7C8%7CDlQXE%7CDlQWU%7C)

If you've never seen GWT before then such body might be intimidating, but if you study the protocol it's pretty easy to decipher. These two strings at the end, '[DlQXE](https://www.google.com/doubleclick/studio/gwt/%7C9DB073B0A4AFE75F8679003264944EE5%7Ccom.google.ads.api.gwt.rpc.client.BatchedInvocationService%7Cinvoke%7Ccom.google.ads.api.gwt.rpc.client.BatchedInvocationRequest/2983766987%7Ccom.google.ads.richmedia.studio.ui.common.grubby.client.BatchedInvocationRequestHeaderImpl/3117963532%7Cjava.util.ArrayList/4159755760%7Ccom.google.ads.richmedia.studio.service.CreativeServiceGwt$GetDownloadArchiveUrlRequest/1562479252%7C1%7C2%7C3%7C4%7C1%7C5%7C5%7C6%7C0%7C7%7C1%7C8%7CDlQXE%7CDlQWU%7C)' and '[DlQWU](https://www.google.com/doubleclick/studio/gwt/%7C9DB073B0A4AFE75F8679003264944EE5%7Ccom.google.ads.api.gwt.rpc.client.BatchedInvocationService%7Cinvoke%7Ccom.google.ads.api.gwt.rpc.client.BatchedInvocationRequest/2983766987%7Ccom.google.ads.richmedia.studio.ui.common.grubby.client.BatchedInvocationRequestHeaderImpl/3117963532%7Cjava.util.ArrayList/4159755760%7Ccom.google.ads.richmedia.studio.service.CreativeServiceGwt$GetDownloadArchiveUrlRequest/1562479252%7C1%7C2%7C3%7C4%7C1%7C5%7C5%7C6%7C0%7C7%7C1%7C8%7CDlQXE%7CDlQWU%7C)', caught my attention - they seemed to be the strings indicating what file I'm actually truing to access. Poking around in the system, it became clear that these strings are actually ID's representing the specific campaign in the system. 

I guess you see where this is going now - I logged in as a different user and obtained another pair of IDs. I then tried using this IDs with the first user cookies - and was able to get the URL link for the second user's files. As these strings are very short, I figured it is rather easy to guess them. I ran a quick script to guess similar-looking ID's, and quickly found more IDs that worked - that pointed to more files belonging to other users.

Reporting this bug yielded another 500$ bounty.

  

**Strikes 4 & 5**

Encouraged by these initial findings, I continued my research around the system’s authorization mechanism, feeling that it’s not ‘as tight’ as it perhaps should be. Sure enough, within few days the issue were piling up:

![](https://static.wixstatic.com/media/5527e6_46260fe75a904a2b8ef56d6dd277d2ab~mv2.png/v1/fill/w_49,h_10,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_46260fe75a904a2b8ef56d6dd277d2ab~mv2.png)

Google’s team seemed to agree with me that perhaps the authorization in Richmedia studio should perhaps be, ah, adjusted.. 

![](https://static.wixstatic.com/media/5527e6_fd27d691e425427db67a7a2d8782ce90~mv2.png/v1/fill/w_49,h_39,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_fd27d691e425427db67a7a2d8782ce90~mv2.png)

  

**Final thoughts:**

Days after the research, what occupied my brain was not the auth issues, but rather the initial app discovery. I’m sure I’ve seen the https://www.google.com/doubleclick/studio/ link before, but as I didn’t have permission to the system I just didn’t know it existed. How many more such apps are lurking in the dark? For sure some food for thought ;)
