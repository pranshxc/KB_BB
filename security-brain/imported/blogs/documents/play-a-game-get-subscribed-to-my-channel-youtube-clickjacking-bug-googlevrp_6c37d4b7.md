---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-02_play-a-game-get-subscribed-to-my-channel-youtube-clickjacking-bug-googlevrp.md
original_filename: 2021-04-02_play-a-game-get-subscribed-to-my-channel-youtube-clickjacking-bug-googlevrp.md
title: 'Play a game, get Subscribed to my channel - YouTube Clickjacking Bug \| #GoogleVRP'
category: documents
detected_topics:
- command-injection
- clickjacking
tags:
- imported
- documents
- command-injection
- clickjacking
language: en
raw_sha256: 6c37d4b796badec6b5960dc4fae7b74b9f1aa05b9cfecb68d1323fff4f891a4c
text_sha256: ed9c3f892ae01c0710435c458d5097e5d02f6004a3dce5ba48e20ea662658be0
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Play a game, get Subscribed to my channel - YouTube Clickjacking Bug \| #GoogleVRP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-02_play-a-game-get-subscribed-to-my-channel-youtube-clickjacking-bug-googlevrp.md
- Source Type: markdown
- Detected Topics: command-injection, clickjacking
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `6c37d4b796badec6b5960dc4fae7b74b9f1aa05b9cfecb68d1323fff4f891a4c`
- Text SHA256: `ed9c3f892ae01c0710435c458d5097e5d02f6004a3dce5ba48e20ea662658be0`


## Content

---
title: "Play a game, get Subscribed to my channel - YouTube Clickjacking Bug \| #GoogleVRP"
url: "https://sriram-offcl.medium.com/play-a-game-get-subscribed-to-my-channel-youtube-clickjacking-bug-googlevrp-6ce1d15542d3"
authors: ["Sriram Kesavan (@sriramoffcl)"]
programs: ["Google"]
bugs: ["Clickjacking"]
bounty: "100"
publication_date: "2021-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3772
scraped_via: "browseros"
---

# Play a game, get Subscribed to my channel - YouTube Clickjacking Bug \| #GoogleVRP

Play a game, get Subscribed to my channel - YouTube Clickjacking Bug | #GoogleVRP
Sriram Kesavan
Follow
4 min read
·
Apr 2, 2021

205

2

Press enter or click to view image in full size

NOTE: Not gonna publish some of my best bugs :) Sorry !!!

Well, it was a amazing Sunday ( We are a Startup ). I reached my office approximately at 10:30AM and had my colleague with me in office. He had a long night journey that day, so he decided to have a 5 hour nap in our office :)

I was reviewing my previously reported bugs in Google VRP and I was listening to a song on YouTube.

When I was listening to the song, I noticed the share function in YouTube that I never used before.

The Share function has more options like “Share to Facebook”, “Share to Twitter”, “Share to Email” and more. And this time Embed option got my attention.

Press enter or click to view image in full size

The Embed option allows user to embed a YouTube Video in their site in a iframe by a small HTML code like below:

Well, everything was fine until I decided to embed a video in my own site. So, I copied the code and pasted it in my own site. I refreshed my site and found the YouTube video embedded in my site.

And when before playing the video I found the YouTube Video had the Channel Image. And hovering the mouse above the Image allowed users to directly Subscribe or Unsubscribe to a channel without sending the user to the main channel page to confirm the Subscription. Hmmmm ;)

Press enter or click to view image in full size

I was wondering if I can convert this to a potential Clickjacking attack that allows an attacker to trick a victim to Subscribe or Unsubscribe to a channel then it would be cool…

I jumped in to my Sublime Editor and started creating a small HTML code that can be convincing for a victim to go for it. And like in 5 minutes I came up with a toooo simple HTML code and built a POC. That works like this:

Press enter or click to view image in full size

It was a very simple game ( Not a game though ) The victim has to hover his mouse over the RED color and has to follow the path and click on it when it turns to GREEN color. I agree this isn’t super cool POC script but with 5–10 mins of time…That was OK :)

And this also has a function to add a video to Watch Later that can be also used to add a video in Victim’s Watch later list by again creating a fake button.

Without any delays even before reporting this issue:

Get Sriram Kesavan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

All I had in my mind was, what could be the Google VRP reply be ?

Duplicate
Intended Behavior
Won’t Fix & more…

And I was also wondering how it didn’t get on the eyes of other top researchers which was just there. Like Literally there !!

I reported this to Google VRP and after two days I received a mail like this:

Press enter or click to view image in full size

At first glace, this might not severe enough to qualify for a reward

I was almost broke but still it was Accepted and the panel will take a look.

And after around 2 weeks I received a mail like this:

Reward Snip

Yes, the panel decided to reward me $100. I was literally laughing because I never thought this will be even rewarded and even my friend said “It was something, than nothing”

But still it wasn’t totally satisfying for me and asked them for a explanation and GVRP team replied me, that the reward was issued based on the impact and also we found unusual user interaction on this scenario, which I also seriously agree. And also added me that if I can and decrease the user interaction, we will reconsider this issue again.

And on Feb 2, 2021

Started working on this and it’s been almost 2 months and decided to give up :(

yah, but still I am happy with the panel decision:

Hide the Pain :)

Need a Video for better understanding — Here you go:

Youtube Video

Thanks for reading:

Well if you love this write up drop a clap 👏, let’s connect then:

Twitter: sriramoffcl

Instagram: sriram_offcl

LinkedIn: sriramkesavan

Peace ✌️ !!!
