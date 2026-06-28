---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-17_bypassing-instagrams-stories-restriction.md
original_filename: 2019-05-17_bypassing-instagrams-stories-restriction.md
title: Bypassing Instagram’s stories restriction
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: 0d2a152ac18f230706a043ff189e3dd935873c4804489b9e980bf1be9bc668a0
text_sha256: 6d85bd172f992c016838429a575293ed2be5f03b046ebce58576b53118460532
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Bypassing Instagram’s stories restriction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-17_bypassing-instagrams-stories-restriction.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `0d2a152ac18f230706a043ff189e3dd935873c4804489b9e980bf1be9bc668a0`
- Text SHA256: `6d85bd172f992c016838429a575293ed2be5f03b046ebce58576b53118460532`


## Content

---
title: "Bypassing Instagram’s stories restriction"
url: "https://medium.com/@baibhavanandjha/bypassing-instagrams-stories-restriction-5936f8a4f079"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2019-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5259
scraped_via: "browseros"
---

# Bypassing Instagram’s stories restriction

Baibhav Anand
 highlighted

Baibhav Anand
Follow
2 min read
·
May 17, 2019

219

3

Bypassing Instagram’s stories restriction

Hello readers, Today I will be telling you how I managed to bypass Instagram’s story restriction and got $500 awarded by Facebook.

One fine day while I was watching some Instagram stories of the people I follow and while watching the story of Unbox Therapy I realized that he had disabled story replies and I couldn’t find the reply option and suddenly one of my friend messaged me on WhatsApp and a pop up of that message came on top of the Instagram story and upon clicking on the reply button of that pop up message that I received on WhatsApp suddenly reply option also showed in Instagram that was when I realized that popping up keyboard while viewing a story with replies disabled can bring back the reply option in the story.

Get Baibhav Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I then created a video report on February 3rd stating this issue and also I attached a video POC with it, here is what I sent them : https://drive.google.com/file/d/17WZvdGKvzeBz5OPq4PlEUPXF35XaziHv/view?fbclid=IwAR2EEdEPCmR75-Mvcga***REDACTED-SUSPECT-TOKEN***Facebook then replied that they have sent it to the product team for further investigation meaning that it was then triaged and it almost took around 2.5 months for them to fix it and then they sent me a fixed message where they stated that the bug has been fixed and after around a week I got a message that I have been awarded $500 for finding an issue where a user could reply to stories when the reply was disabled and then after around 3 days they had put me in the Facebook’s Hall of Fame 2019.

Thank you for reading. Follow me for more such stories as I progress with my journey as a security researcher.
