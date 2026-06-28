---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-30_reposted-2019-hacking-youtube-for-fun-and-profit.md
original_filename: 2019-07-30_reposted-2019-hacking-youtube-for-fun-and-profit.md
title: 'Reposted [2019]: Hacking YouTube for #fun and #profit'
category: blogs
detected_topics:
- sso
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- blogs
- sso
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: db8ebd075e4f547db0682300451744db4bb07ea2f4e51a738b3120c274a989a4
text_sha256: 9070df21abc6ce47c6989186ec7beafa2497d398bfdce7f18dde830e8c435c93
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Reposted [2019]: Hacking YouTube for #fun and #profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-30_reposted-2019-hacking-youtube-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `db8ebd075e4f547db0682300451744db4bb07ea2f4e51a738b3120c274a989a4`
- Text SHA256: `9070df21abc6ce47c6989186ec7beafa2497d398bfdce7f18dde830e8c435c93`


## Content

---
title: "Reposted [2019]: Hacking YouTube for #fun and #profit"
url: "https://medium.com/@dekeeu/reposted-2019-hacking-youtube-for-fun-and-profit-8685dd475e30"
authors: ["Alexandru Coltuneac (@dekeeu)"]
programs: ["Google"]
bugs: ["Broken authorization"]
publication_date: "2019-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5112
scraped_via: "browseros"
---

# Reposted [2019]: Hacking YouTube for #fun and #profit

Reposted [2019]: Hacking YouTube for #fun and #profit
Alexandru Coltuneac
Follow
5 min read
·
Jul 31, 2019

39

1

Hi there,

While I was cleaning up some folders from my Desktop today, I accidentally found one of them called “PoCs”, full of text files and images. They were from my previous reported security bugs, 99% of them for the Google Vulnerability Reward Program. These experiences, all these hours spent looking for bugs, trying different methods and understanding how Google services work taught me many lessons which are very helpful now, at work or at home, hacking for bounties. I hope that, through this article, I can share my experience and help hackers to discover new interesting and cool bugs.

This article will be about a two vulnerabilities that I found in YouTube web application, more exactly in the Studio platform. YouTube Studio (https://studio.youtube.com/) is a new dashboard created by Google for the content creators which makes their lives easier and speeds up the process of editing and publishing videos. This tool has a lot of cool features, including here the possibility to view the Analytics data for your videos, changing community and channel related settings and also updating all your videos at once, feature called Update In Bulk.

Bug #1 (Change any YouTube video settings)

If you go to the YT Studio homepage, you will see that in the left menu, there is a tab called Videos, which once clicked will redirect you to a new page, where you can see all your videos:

Press enter or click to view image in full size

If you are a content creator and want to change all your videos at once (to put a new partner link in the description, add a tag in the title, or shut down your channel by setting all your videos on private) there is a functionality which allows you to do that. By selecting the videos you want to update, a new toolbar will appear in the context of the application. Then, you will be able to select which part(s) of the videos you want to change (title, description, tags, visibility, comments, etc) and a new update button will be shown in the page:

Press enter or click to view image in full size

That blue Update button, once clicked will trigger a POST request to the YouTube servers (https://studio.youtube.com/youtubei/v1/creator/enqueue_creator_bulk_action) and will have as a body, a JSON formatted code. That JSON object includes various attributes and configuration parameters, but among them, only one caught my attention: a parameter called videos, represented by videoIds object which has an array with the ids of the videos I’ve just selected for update:

Press enter or click to view image in full size

After playing a bit with it, I discovered that there was no protection or access-right checks to verify if the videos behind those id values are really owned by the user who initiated the update process. This way, I could have changed any YouTube video’s settings just by setting its video ID.

The impact of this vulnerability was pretty big, since I could (for example) to shut downany YouTube channel just be setting its videos on private. The regular viewer won’t be able to find those videos anymore and then, many views will be lost. Also, if someone wanted to promote a website or a product, this flaw could help him a lot since the only thing he had to do, was to update the title and the video of some of the most popular YouTube videos, like Despacito or Shape of you by Ed Sheeran. Also, if someone wanted to gain some pocket-money, he could add a “Donation” PayPal account in the description of some high-ranked videos, as many YouTubers do these days.

Below, there is a PoC video which I’ve created for this bug. Thinking better, maybe I should make it shorter, but it captures all technical aspects and all the reproduction steps of this bug.

Timeline:

11.11.2018 — Bug reported

12.11.2018 — Bug triaged & “Nice catch”

13.11.2018 — Bug rewarded

Get Alexandru Coltuneac’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

13.12.2018 — Bug fixed

Bug #2 (Get the Unlisted Playlists of any YouTube user)

The second bug was a logic flaw by which an attacker could have seen any unlisted playlist of any YouTube user.

Any time a user opens the Studio dashboard and wants to edit a specific video, he has to click on it first and then he will be redirected to a new page.

Press enter or click to view image in full size

Once this page opens, a new POST request is sent in the background to the https://studio.youtube.com/youtubei/v1/creator/list_creator_playlists endpoint, which as the name suggests, will retrieve all the playlist of the current logged-in user. The role of this request was to populate the Playlists section, from Video Edit page.

Once again, the body of that request was JSON formatted and contained an attribute called channelId, representing the value of the channel being currently edited. After several tests, I discovered that the backend scripts did not verify if the value supplied by the user for the channelId parameter was actually his channel ID.

Press enter or click to view image in full size

In the response sent back by the ap plication there were all the playlists associated with that specific channelId with only one condition: the channel should have had only PUBLIC and UNLISTED playlists:

Press enter or click to view image in full size

If that condition was met, an attacker could have get any unlisted playlist of a YouTube user. This was more like a privacy bug since an unlisted playlist (as an unlisted video) can’t be found in the platform, until shared by the person who owns it.

Timeline:

12.11.2018 — Bug reported

13.11.2018 — Bug triaged

14.11.2018 — “Nice catch”

30.11.2018 — Bug rewarded

12.12.2018 — Bug fixed

Conclusion

Hacking Google is a always fun and it’s also a good way to improve your pentesting skills. I recommend you to have a look on Google VRP program and start hacking for good :)

Anyways, I want to thank you for reading and of course if you have any questions just drop me an email or send me a DM on Twitter(@dekeeu). See ya !
