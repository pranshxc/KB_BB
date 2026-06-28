---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-13_how-a-simple-bug-in-facebook-lite-let-me-win-my-first-bug-bounty-from-facebook.md
original_filename: 2020-11-13_how-a-simple-bug-in-facebook-lite-let-me-win-my-first-bug-bounty-from-facebook.md
title: How a simple bug in Facebook Lite let me win my first bug bounty from Facebook
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 350775582ff5b7121e4d048920c511c4704508ed1c67d4b5c0f6a3e0db085e3c
text_sha256: 5421059abb1a6493bc32a5eef833dfe4b262e86fa31cd681728b7a7ca48e69c5
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How a simple bug in Facebook Lite let me win my first bug bounty from Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-13_how-a-simple-bug-in-facebook-lite-let-me-win-my-first-bug-bounty-from-facebook.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `350775582ff5b7121e4d048920c511c4704508ed1c67d4b5c0f6a3e0db085e3c`
- Text SHA256: `5421059abb1a6493bc32a5eef833dfe4b262e86fa31cd681728b7a7ca48e69c5`


## Content

---
title: "How a simple bug in Facebook Lite let me win my first bug bounty from Facebook"
url: "https://samiparyal.medium.com/commenting-on-a-post-by-opening-it-via-pages-news-feed-goes-from-a-wrong-actor-i-e-56fab4cf5a91"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2020-11-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4140
scraped_via: "browseros"
---

# How a simple bug in Facebook Lite let me win my first bug bounty from Facebook

How a simple bug in Facebook Lite let me win my first bug bounty from Facebook
Samip Aryal
Follow
3 min read
·
Nov 13, 2020

215

This writeup is about an easy catch in Facebook Lite that led me to win a bug bounty from Facebook unexpectedly for the first time.

[Edit(2021): This actually became my 3rd valid bug report at the present according to the date of reporting because two previous reports before this got recognized as valid later on this year]

There’s a separate Newsfeed available for pages to interact with other pages and their posts independently. However, this option might not be available for all the users but it can be accessed anytime through this URL: ‘https://www.facebook.com/pageusername/news_feed’.

But the vulnerability is on the mobile platform of the same section. So, moving to mobile; Pages still get the separate section ‘Pages Newsfeed’ in the top bar or from the ‘more’ option inside the page in FB4A and FBLite too.

Now, At first, I began to look for admin disclosure vulnerability in the page news_feed on the Facebook app. Everything went smooth, I couldn’t find anything suspicious. But then I remembered that ‘Oh! Facebook Lite has that same Page News Feed option too’ so, I started looking it there. Suddenly; when I opened a photo from any one of the posts on the page news_feed and then commented in the post; then the comment went from the admin’s personal account instead of the page. (However, when commenting just from the outer interface without opening the media, the comment went from the page itself). This vulnerability was practically most effective with the posts containing multiple media (photos/videos) where pages can view the photos/videos one by one by clicking on it and then when they commented back, it used to go from Admin’s account. So, without any hesitation, I immediately reported it to Facebook with the title ‘Commenting on a post by opening it via page’s news-feed goes from a wrong actor (i.e. admin’s personal account)’ along with a short POC video (←click to see the video).

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After several conversations, they replied claiming it to be fixed but it wasn’t properly fixed for the first time. I informed them about the remains. After some days, they rewarded me the bounty before a complete fix. So, they refrained me from disclosing any details of the report before it was fully resolved. Now, as the bug is patched already; here I am disclosing it under the responsible disclosure policy.

Timeline

Reported — Sunday, July 12, 2020

Pre-Triaged — Thursday, July 16, 2020

Triaged — Friday, 17 July 2020

Fix claim from their side — Saturday, 25 July 2020

Informed about incomplete fix— Saturday, 25 July 2020

Reply of Acknowledgement — Wednesday, 5 August 2020

Asked for an update — Sunday, 16 August 2020

Informed about the ongoing process — Wednesday, 19 August 2020

Bounty Rewarded without the fix — Friday, 28 August 2020

Refrained additionally for non-disclosure — Friday, 28 August 2020

Agreed, thanked & requested to update the hall-of-fame page — Friday, 28 August 2020

Listed in the Facebook hall of fame — Wednesday, 2 September 2020

Asked permission to disclose the bug as it got completely fixed — Monday, 28 September 2020

Permission granted with a final patch message — Wednesday, 7 October 2020

Bounty Reward Message from Facebook

Thank you for reading this write-up about the simple vulnerability. If you have any suggestions/queries, I’m available on Facebook/ Instagram :)
