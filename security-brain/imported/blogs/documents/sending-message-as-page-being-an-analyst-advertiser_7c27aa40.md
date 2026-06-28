---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-21_sending-message-as-page-being-an-analyst-advertiser.md
original_filename: 2019-08-21_sending-message-as-page-being-an-analyst-advertiser.md
title: Sending Message as page being an analyst/ advertiser?
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 7c27aa405d063e175777091f90b7b54c4ca57984db7643ca7058005037e6600b
text_sha256: 8cbe84ef4d4241f3528359545cf167f1802ade7dcfe17574d9b764917098125f
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Sending Message as page being an analyst/ advertiser?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-21_sending-message-as-page-being-an-analyst-advertiser.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7c27aa405d063e175777091f90b7b54c4ca57984db7643ca7058005037e6600b`
- Text SHA256: `8cbe84ef4d4241f3528359545cf167f1802ade7dcfe17574d9b764917098125f`


## Content

---
title: "Sending Message as page being an analyst/ advertiser?"
url: "https://medium.com/@baibhavanandjha/sending-message-as-page-being-an-analyst-advertiser-eb0317376f43"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-08-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5070
scraped_via: "browseros"
---

# Sending Message as page being an analyst/ advertiser?

Sending Message as page being an analyst/ advertiser?
Baibhav Anand
Follow
2 min read
·
Aug 21, 2019

174

Press enter or click to view image in full size

Hello readers,

Today I will be telling you how I was able to send messages as a page being a page analyst/ advertiser.

According to this article from Facebook https://www.facebook.com/help/pageroles Analysts and Advertisers cannot send messages as page.

Here is how I managed to bypass it :

Setup : 3 Facebook accounts, Where User A should be the admin, User B is the attacker account here and User C is any random Facebook account.

Get Baibhav Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps :

Make User B an editor.
User B must be using Facebook lite.
Send the page a message from User C's account.
User B in Facebook lite app will get a notification saying user C messaged to the page.
User B will open the message.
User A will now change user B's page role to Analyst.
While User B is still in the inbox with user C, he/she will be able to send messages as page despite being page analyst or advertiser.

Here is a video POC :https://drive.google.com/file/d/1-tcGdGtDPUTBtLn57iAKeFer_wGuBhzB/view?usp=drivesdk

As unfortunate as it could be for me, it got an internal fix.

Thank you for making it to the end of the article. Here is a Facebook bug bounty tip : While being in the session when you had privileges try changing your privilege and see if you can still perform certain tasks while still in that session.

Find me on Twitter : https://www.twitter.com/spongebhav

Find me on Facebook : https://www.facebook.com/ibaibhav
