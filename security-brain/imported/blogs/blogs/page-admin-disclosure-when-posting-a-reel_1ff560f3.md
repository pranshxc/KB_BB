---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-30_page-admin-disclosure-when-posting-a-reel.md
original_filename: 2022-04-30_page-admin-disclosure-when-posting-a-reel.md
title: Page Admin Disclosure when Posting a Reel
category: blogs
detected_topics:
- command-injection
- api-security
- mobile-security
tags:
- imported
- blogs
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 1ff560f3129cdea535c1dfd33ef7f65d22186d8b74eb9f1851e5f6b8db32f338
text_sha256: 4838860590a6ed323894eab4065508a1a4c656fd28f619224cfe922d508f87b4
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Page Admin Disclosure when Posting a Reel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-30_page-admin-disclosure-when-posting-a-reel.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `1ff560f3129cdea535c1dfd33ef7f65d22186d8b74eb9f1851e5f6b8db32f338`
- Text SHA256: `4838860590a6ed323894eab4065508a1a4c656fd28f619224cfe922d508f87b4`


## Content

---
title: "Page Admin Disclosure when Posting a Reel"
url: "https://zerocode-ph.medium.com/page-admin-disclosure-when-posting-a-reel-1bfac9bd7f71"
authors: ["Syd Ricafort (@devsyd11)"]
programs: ["Meta / Facebook"]
bugs: ["Spoofing"]
bounty: "1,000"
publication_date: "2022-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2674
scraped_via: "browseros"
---

# Page Admin Disclosure when Posting a Reel

Page Admin Disclosure when Posting a Reel
Syd Ricafort (0cod3)
Follow
3 min read
·
Apr 30, 2022

56

1

Hello , I’m Syd from the Philippines. Today I would like to share one of my findings in Meta Bug Bounty Program. The bug that I found is pretty simple and help me earn 1000 USD.

It was just a normal day and I was checking in on my Facebook account watching random videos. It came up on my mind to check if there is a new feature in FB4A (Facebook for Android). So I noticed, that there is a new feature called Reels.

Reels were first introduce by Facebook (now Meta) in September 29 2021 in the US Alone. Reels on Facebook can consist of music, audio, effects and more. You can find them in News Feed or in Groups, and when viewing a reel on Facebook, you can easily follow the creator directly from the video, like and comment on it, or share it with friends.

However, in this current year it was launched globally in 150 countries. So after seeing this feature, I quickly open my laptop and fire up my burpsuite and checking if there is an endpoint that would leak the admin id of the page. Unfortunately I have found nothing, but I did not give up. I remember that Facebook will pay you if you found a Voice Confusion issue(where the identity under which the admin is acting is unclear). Luckily I noticed that one of my test group has the Reels feature (I also checked with other account but the reels is not present there, seems it is limited on small market).

Now, here is the interesting part, I use the voice switcher to act as page and then quickly create a sample reel. After publishing the reel, it was posted as admin instead of page. Then I quickly made a report and Meta Team triaged my report.

Description/Impact
In a Facebook group member with linked pages can choose how to interact its either admin or page profile. The vulnerability is on the Facebook Reel, whenever the user switch the voice as page using the voice switcher in a FB group and publish a Reel, it will be posted as admin personal voice.

Get Syd Ricafort (0cod3)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to reproduce:

1. Navigate to your group
2. Switch your voice as page using the voice switcher floating button
3. Open the composer then reel
4. Create a 3 seconds reel or more then click “share reel”
5. You will notice that the reel is posted as admin profile instead of page (even you set the voice as page in the first place)

Press enter or click to view image in full size
Sweet message from Meta Team 😍

Voice Related Issue is eligible at that time of the report. Today, Meta will no longer reward such issue.

Found multiple voice related issues but Meta closed it as informative since its no longer eligible.

Press enter or click to view image in full size

Make sure to follow me on my Twitter Account.

Thanks and Enjoy Hacking😊
