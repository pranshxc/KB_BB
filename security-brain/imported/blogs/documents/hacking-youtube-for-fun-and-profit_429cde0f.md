---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-12_hacking-youtube-for-fun-and-profit.md
original_filename: 2019-02-12_hacking-youtube-for-fun-and-profit.md
title: 'Hacking YouTube for #fun and #profit'
category: documents
detected_topics:
- sso
- idor
- command-injection
- business-logic
- api-security
- cloud-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- business-logic
- api-security
- cloud-security
language: en
raw_sha256: 429cde0f1c839f069ce3ed04342541a586c5dba363308a290b4cfecf35f62f37
text_sha256: 93a3c94b25e251cb4d9a80e545bcbe6afb16cb227112ac19f4f500e322ee0f69
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking YouTube for #fun and #profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-12_hacking-youtube-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, business-logic, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `429cde0f1c839f069ce3ed04342541a586c5dba363308a290b4cfecf35f62f37`
- Text SHA256: `93a3c94b25e251cb4d9a80e545bcbe6afb16cb227112ac19f4f500e322ee0f69`


## Content

---
title: "Hacking YouTube for #fun and #profit"
url: "https://www.linkedin.com/pulse/hacking-youtube-fun-profit-alexandru-coltuneac/"
final_url: "https://www.linkedin.com/pulse/hacking-youtube-fun-profit-alexandru-coltuneac/"
authors: ["Alexandru Coltuneac (@dekeeu)"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2019-02-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5419
---

![Hacking YouTube for #fun and #profit](https://media.licdn.com/dms/image/v2/C4D12AQHhCFh2KMZs3w/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1549841204530?e=2147483647&v=beta&t=Z9eFh2ZiGa_mtF2wVW7AVpOdyQ-nCVcA-9pqtHjV4iE)

# Hacking YouTube for #fun and #profit

  * [ Report this article ](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fhacking-youtube-fun-profit-alexandru-coltuneac&trk=article-ssr-frontend-pulse_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=PONCHO_ARTICLE&_f=guest-reporting)

[ 🚀 Alexandru Coltuneac  ](https://ro.linkedin.com/in/alexandrucoltuneac)

###  🚀 Alexandru Coltuneac 

####  Lead Security Engineer | AppSec & Cloud Security | Security Consulting and Delivery | OSCP • CISSP 

Published Feb 12, 2019 

[ \+ Follow ](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fhacking-youtube-fun-profit-alexandru-coltuneac%2F&trk=article-ssr-frontend-pulse_publisher-author-card)

Hi there,

While I was cleaning up some folders from my Desktop today, I accidentally found one of them called "PoCs", full of text files and images. They were from my previous reported security bugs, 99% of them for the Google Vulnerability Reward Program. These experiences, all these hours spent looking for bugs, trying different methods and understanding how Google services work taught me many lessons which are very helpful now, at work or at home, hacking for bounties. I hope that, through this article, I can share my experience and help hackers to discover new interesting and cool bugs.

This article will be about a two vulnerabilities that I found in YouTube web application, more exactly in the Studio platform. YouTube Studio (<https://studio.youtube.com/>) is a new dashboard created by Google for the content creators which makes their lives easier and speeds up the process of editing and publishing videos. This tool has a lot of cool features, including here the possibility to view the Analytics data for your videos, changing community and channel related settings and also updating all your videos at once, feature called [Update In Bulk](https://support.google.com/youtube/answer/6085540?hl=en).

## Bug #1 (Change any YouTube video settings)

If you go to the YT Studio homepage, you will see that in the left menu, there is a tab called Videos, which once clicked will redirect you to a new page, where you can see all your videos:

![](//:0)

If you are a content creator and want to change all your videos at once (to put a new partner link in the description, add a tag in the title, or shut down your channel by setting all your videos on private) there is a functionality which allows you to do that. By selecting the videos you want to update, a new toolbar will appear in the context of the application. Then, you will be able to select which part(s) of the videos you want to change (title, description, tags, visibility, comments, etc) and a new update button will be shown in the page:

![](//:0)

That blue Update button, once clicked will trigger a POST request to the YouTube servers (**https://studio.youtube.com/youtubei/v1/creator/enqueue_creator_bulk_action**) and will have as a body, a JSON formatted code. That JSON object includes various attributes and configuration parameters, but among them, only one caught my attention: a parameter called **videos** , represented by **videoIds** object which has an array with the ids of the videos I've just selected for update:

![](//:0)

After playing a bit with it, I discovered that there was no protection or access-right checks to verify if the videos behind those id values are **really owned by the user who initiated the update process**. This way, I could have changed any YouTube video's settings just by setting its video ID.

The impact of this vulnerability was pretty big, since I could (for example) to **shut down** **any YouTube channel** just be setting its videos on private. The regular viewer won't be able to find those videos anymore and then, many views will be lost. Also, if someone wanted to promote a website or a product, this flaw could help him a lot since the only thing he had to do, was to **update the title and the video of some of the most popular YouTube videos** , like Despacito or Shape of you by Ed Sheeran. Also, if someone wanted to gain some pocket-money, he could **add a "Donation" PayPal account in the description of some high-ranked videos** , as many YouTubers do these days.

Below, there is a **PoC** video which I've created for this bug. Thinking better, maybe I should make it shorter, but it captures all technical aspects and all the reproduction steps of this bug.

Timeline:

**11.11.2018 - Bug reported**

**12.11.2018 - Bug triaged & "Nice catch"**

**13.11.2018 - Bug rewarded**

**13.12.2018 - Bug fixed**

## Bug #2 (Get the Unlisted Playlists of any YouTube user)

The second bug was a logic flaw by which an attacker could have seen any unlisted playlist of any YouTube user. 

Any time a user opens the Studio dashboard and wants to edit a specific video, he has to click on it first and then he will be redirected to a new page.

![](//:0)

Once this page opens, a new POST request is sent in the background to the **https://studio.youtube.com/youtubei/v1/creator/list_creator_playlists** endpoint, which as the name suggests, will retrieve all the playlist of the current logged-in user. The role of this request was to populate the **Playlists** section, from Video Edit page.

Once again, the body of that request was JSON formatted and contained an attribute called **channelId** , representing the value of the channel being currently edited. After several tests, I discovered that the backend scripts did not verify if the value supplied by the user for the **channelId** parameter was actually his channel ID.

![](//:0)

In the response sent back by the ap plication there were all the playlists associated with that specific **channelId** with only one condition: the channel should have had only PUBLIC and UNLISTED playlists:

![](//:0)

If that condition was met, an attacker could have get any unlisted playlist of a YouTube user. This was more like a privacy bug since an unlisted playlist (as an unlisted video) can't be found in the platform, until shared by the person who owns it.

**Timeline:**

**12.11.2018 - Bug reported**

**13.11.2018 - Bug triaged**

**14.11.2018 - "Nice catch"**

**30.11.2018 - Bug rewarded**

**12.12.2018 - Bug fixed**

## **Conclusion**

Hacking Google is a always fun and it's also a good way to improve your pentesting skills. I recommend you to have a look on [Google VRP program](https://www.google.com/about/appsecurity/reward-program/) and start hacking for good :)

Anyways, I want to thank you for reading and of course if you have any questions just drop me an [email](http://dekeeu@gmail.com) or send me a DM on Twitter([@dekeeu](https://twitter.com/dekeeu)). See ya !
