---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-02_journey-of-my-first-bug-bounty-nov-2018.md
original_filename: 2020-10-02_journey-of-my-first-bug-bounty-nov-2018.md
title: Journey Of My First Bug Bounty (Nov 2018)
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: b197fc2dff43e0f445857dfd4462f83a8a87d13e0eac32c786b8d66c3f007524
text_sha256: 3637c86a285f1986ba2a8078975952fccacba6eb2fd5ce1f72df5399880ef741
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Journey Of My First Bug Bounty (Nov 2018)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-02_journey-of-my-first-bug-bounty-nov-2018.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `b197fc2dff43e0f445857dfd4462f83a8a87d13e0eac32c786b8d66c3f007524`
- Text SHA256: `3637c86a285f1986ba2a8078975952fccacba6eb2fd5ce1f72df5399880ef741`


## Content

---
title: "Journey Of My First Bug Bounty (Nov 2018)"
url: "https://medium.com/@harshtya9i/journey-of-my-first-bug-bounty-nov-2018-af471c21efc0"
authors: ["Harsh Tyagi (@harshtya9i)"]
programs: ["Samsung"]
bugs: ["Authentication bypass"]
bounty: "200"
publication_date: "2020-10-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4223
scraped_via: "browseros"
---

# Journey Of My First Bug Bounty (Nov 2018)

Journey Of My First Bug Bounty (Nov 2018)
Harsh Tyagi
Follow
2 min read
·
Oct 2, 2020

71

Hello everyone,

This is my first writeup

To people who don’t know me I Harsh, a 4th year Engineering student in Information technology and a bug bounty hunter.

This is the story when i’m in a 2nd year and summer holidays going on, as a daily routine i'm sitting in my room and scrolling my phone, and suddenly i noticed that there is some misconfiguration in my phone then i tried the same procedure 2–3 times and notice the same and i came to a conclusion that this is a bug but as a noob that time i don’t know where to report this so i search on google and i saw official Samsung Mobile Security vulnerability reporting website https://security.samsungmobile.com/main.smsb

After this i create an account on a website and started looking for instructions how to report a bug to samsung and you won’t believe it guys that time i even don’t know about Poc, report making, but i keep things simple that time so i made a simple report and as you all know this is my first report so forget about professional report writing skills but anyway i make a Poc video and send it to the samsung.

Get Harsh Tyagi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next morning, I received an email

Press enter or click to view image in full size
Vulnerability
Press enter or click to view image in full size
Attack Scenario
User locked their Whatsapp with S Secure application
User add second whatsapp from dual apps feature by samsung it as a parallel space application does
When we open second whatsapp sometimes it open without any authentication means without pin, fingerprint and this bug unlock our first whatsapp also. So anybody can enter in our locked apps.
Bounty Reward

After waiting 90 Days, Samsung rewarded me $200 😍 through bugcrowd and that moment my excitement level 🎉

Press enter or click to view image in full size
Tips

Sometimes you don’t need to do reverse engineering or read application source code. Always try to abuse manually first.

Thanks for reading😎

Sorry for my bad english..

More writeups coming soon…

Linkedin: https://www.linkedin.com/in/harsh-tyagi-1468b3193/

Twitter: https://twitter.com/harshtya9i

Instagram: https://instagram.com/harsh_tya9i
