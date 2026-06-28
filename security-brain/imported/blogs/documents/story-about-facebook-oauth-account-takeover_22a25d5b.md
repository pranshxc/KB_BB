---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-26_story-about-facebook-oauth-account-takeover.md
original_filename: 2019-07-26_story-about-facebook-oauth-account-takeover.md
title: Story about Facebook Oauth Account Takeover
category: documents
detected_topics:
- oauth
- command-injection
- otp
- api-security
- mobile-security
tags:
- imported
- documents
- oauth
- command-injection
- otp
- api-security
- mobile-security
language: en
raw_sha256: 22a25d5bbd2385d093e91532d16f4243311309f5ada0d6dbb3df95d8eeb87ace
text_sha256: cbcfd1a4fb7c618a6535a4d0ac703823e30a192c4e46d3dee080393bead40553
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Story about Facebook Oauth Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-26_story-about-facebook-oauth-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `22a25d5bbd2385d093e91532d16f4243311309f5ada0d6dbb3df95d8eeb87ace`
- Text SHA256: `cbcfd1a4fb7c618a6535a4d0ac703823e30a192c4e46d3dee080393bead40553`


## Content

---
title: "Story about Facebook Oauth Account Takeover"
url: "https://medium.com/@androgaming1912/story-about-facebook-oauth-account-takeover-6537ff32281b"
authors: ["Zerb0a"]
programs: ["iLOTTE"]
bugs: ["Account takeover", "OAuth"]
bounty: "150"
publication_date: "2019-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5120
scraped_via: "browseros"
---

# Story about Facebook Oauth Account Takeover

zer
Follow
2 min read
·
Jul 26, 2019

51

Story about Facebook Oauth Account Takeover

Hi, My name is Rafli pasya. My hacker name is Zerb0a. On this Story im gonna tell you guys an Account Takeover on iLOTTE. For your information iLOTTE is an eCommerce from South Korea. I found this bug on Facebook Oauth Function. Okay let me explain you the story.

That day, my father just bought something for my grandma. He told me to check the order status ( he paid it ). then my hacker brain began to think of looking for something interesting bug, so i opened burp suite and intercept the Request.

When im trying to login With Facebook, i found a POST request to /loginProccess.do with body :
sometokenparamter=&andiforgotittoo=&id=[myfacebookemail]

it’s look’s interesting right ? i changed the id to victim email address and booom ! i logged in as victim account :) so this is working on any Account, you just need an email to login.

Get zer’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Video PoC:

PoC Video From my Channel

After that i contacted the Customer Service, but they did’nt take it seriosly. then when I told her the impact of this bug could cause a loss, the iLOTTE IT team contacted me via WhatsApp. I Gave him a video PoC and after 2 weeks i got my reward , not much but enough for a Student like me :D.

Press enter or click to view image in full size

Reward : IDR 2.000.000 ( around $150–160 )

Status : Fixed & Rewarded ( Accepted For Public Disclosure )
