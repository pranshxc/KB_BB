---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-05_csrf-in-youtube-leanback-api.md
original_filename: 2021-04-05_csrf-in-youtube-leanback-api.md
title: CSRF in YouTube Leanback API
category: documents
detected_topics:
- command-injection
- otp
- csrf
tags:
- imported
- documents
- command-injection
- otp
- csrf
language: en
raw_sha256: 0d51c2b417e06ff62d3c12c877c4d14d400db23bbcb58f97896ac1ed761210d1
text_sha256: 6c4dd589a14807e28177593215e353ce2488d2818538c048ffe61ccc56acade6
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF in YouTube Leanback API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-05_csrf-in-youtube-leanback-api.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `0d51c2b417e06ff62d3c12c877c4d14d400db23bbcb58f97896ac1ed761210d1`
- Text SHA256: `6c4dd589a14807e28177593215e353ce2488d2818538c048ffe61ccc56acade6`


## Content

---
title: "CSRF in YouTube Leanback API"
page_title: "[#0001] CSRF in YouTube Leanback API | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0001"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0001"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["CSRF"]
publication_date: "2021-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3761
---

#0001  
Vendor: Google  
Status: fixed  
Reported: Jul 24, 2020  
Disclosed: Apr 05, 2021 (255 days) 

# CSRF in YouTube Leanback API

**_Short Impact:_**

All **private/unlisted videos** of a victim can be stolen if the victim visits a malicious link.  
Using the same technique, the victim’s **liked videos** , **watch later** and any **private playlist** ’s content can be stolen.

**_Short Summay:_**

Due to the lack of CSRF protection, a malicious website can play any video/playlist on a YouTube TV via the `lounge` API in the name of the victim.

**_POC Video:_**

<https://youtu.be/HmdyzRH67ac> \- length: 1:46  
_Source code of the POC shown in the video is attached to this report._  
_Stealing liked videos, watch later and private playlist content is not shown in the POC._

**_Core Issue:_**

There is no CSRF protection on the `https://www.youtube.com/api/lounge/bc/bind` endpoint. A malicious website can send a `POST` request to this enpoint to request a video/playlist to be played on a YouTube TV. The malicious website can specify which TV to send the video to using the `loungeIdToken` parameter.

**_POC Flow:_**

This sections describes how, using this CSRF, the attacker can steal _all_ of the victim’s private/unlisted videos. More specifically, here I describe how the POC code works.

  1. POC starts a Flask webserver, to serve the victim opening the malicious page. Let’s call the POC python script backend.
  2. Victim opens the malicious webpage. Let’s call the victim’s page frontend.
  3. Backend requests the attacker to enter the victim’s channel ID.
  4. The channel ID’s second character is changed to a `U`. The resulting string is the playlist ID of the playlist `Uploads from [Channel Name]`, which contains all private/unlisted uploads. Only the owner can see the private/unlisted videos in this playlist. Other users don’t even see the private/unlisted video IDs.
  5. The POC sets up a fake TV, and starts to poll the events for the new malicious TV.
  6. The frontend is instructed to execute the CSRF request, and play the playlist generated in `Step 4.` on the malicious TV.
  7. When the CSRF request is sent by the frontend, the backend recieves the TV play event, containing the IDs of all of the victim’s videos, including private/unlisted video IDs.
  8. The backend queries the YouTube Data API with all of the video IDs, to find out the which videos are private/unlisted.
  9. The unlisted videos are ready, the backend prints the IDs out for the attacker. The unlisted videos only require knowing the video ID to watch.
  10. Backend instructs the frontend to play the victim’s private videos on the malicious TV one by one. For every video, the backend sets up a new malicious TV, tells the frontend to play the specific video, listens for play events, and recieves the play event for the TV with a special `ctt` parameter. Using the `ctt`, the backend queries the `get_video_info` YouTube endpoint for the specific private video, authenticates itself with the `ctt`, and greps the private video’s title and direct video URl from the response.
  11. After every private video is played by the frontend, the backend prints the details of all of the private videos for the attacker.
  12. The POC script is done.

_The specific technical details of how the backend/frontend constructs/sends the requests can be found in the attached POC script._

_The`poc.py` and the `frontend.html` files have to be in the same directory for the script to run._

**Stealing WL/Likes/Private Playlists:**

Similarly to `Step 6.` of the POC, any other private playlists can be played just as the `Uploads from [Channel Name]` playlist. And listening for the play event on the backend, the attacker can get the list of video ID’s the given private playlist contains.

All channels have a few special private playlists:

  * `WL` -> The victim’s `Watch Later` playlist
  * `LL` -> The victim’s `Liked videos` playlist

These two can also be stolen using the same method.

_`HL` used to point to the victim’s `Watch History`, but as of my testing, that playlist is not available anymore._

**Aditional Infos:**

This attack works with not only private, but “draft”, “scheduled” and “removed” videos as well. (These videos are just “private” internally.)

### Extras:

_This section was not included in the original report._

The POC Python script and the frontend JavaScript:  
<https://gist.github.com/xdavidhu/b264ee21d8586e580adc7f821ddfbfc9>

Q: _Is the`/bind` request giving you a `400`?_  
A: That’s “normal”. I stripped off so many parameters that it returns an error, but the video/playlist still gets played on the TV.
