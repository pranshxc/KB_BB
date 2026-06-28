---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-02_view-friends-list-of-any-users-using-view-as-facebook-bug-bounty.md
original_filename: 2022-04-02_view-friends-list-of-any-users-using-view-as-facebook-bug-bounty.md
title: View Friends List of any users using “View as” | Facebook Bug bounty
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: f7c706b06d5cc4453eb41815f3af75fc8f2045c9cb23070b5816432976ca8e0b
text_sha256: b854a93c9ee3e5d57173b18f2f855473c9d0091b0bbf2f8139f3e43896a84ca3
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# View Friends List of any users using “View as” | Facebook Bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-02_view-friends-list-of-any-users-using-view-as-facebook-bug-bounty.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `f7c706b06d5cc4453eb41815f3af75fc8f2045c9cb23070b5816432976ca8e0b`
- Text SHA256: `b854a93c9ee3e5d57173b18f2f855473c9d0091b0bbf2f8139f3e43896a84ca3`


## Content

---
title: "View Friends List of any users using “View as” | Facebook Bug bounty"
url: "https://ph-hitachi.medium.com/view-friends-list-of-any-users-using-view-as-facebook-bug-bounty-edeb6af5640b"
authors: ["Ph.Hitachi"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken Access Control"]
publication_date: "2022-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2758
scraped_via: "browseros"
---

# View Friends List of any users using “View as” | Facebook Bug bounty

View Friends List of any users using “View as” | Facebook Bug bounty
Ph.Hitachi
Follow
2 min read
·
Apr 2, 2022

43

2

Hello guys,

to today i want to share how i find my 1st bug bounty of this year (2022) with Facebook BBP.

Get Ph.Hitachi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so let’s start… on Feb 28, 2022 facebook takedown my main account on facebook due to violations, so on that day i also create new account then after 2 weeks when im changing the privacy of my facebook account after i set all to “only me” then i decided to view my account using “view as” then when i click na the friends tab my facebook friends appear on in the list which is should not happened.

Press enter or click to view image in full size

Then i try to view my profile with another account if its already set then after i checked it’s all normal i can’t see my friend list’s using another account.

Press enter or click to view image in full size

After that i tried to view my profile on the browser then when i goto my profile using “view as” i tried to replace my username on url bar to another username then i see their friend list

Press enter or click to view image in full size
Press enter or click to view image in full size

so i reported it on faceboook.

Timeline Review
- Mar 13, 2022 (Initial report)
- Mar 14, 2022 (Triaged)
- Mar 18, 2022 (Fixed)
- Apr 02, 2022 (Bounty awarded)

Contact:
Email: ph-hitachi@wearehackerone.com
Twitter: https://x.com/PhHitachi
LinkedIn: www.linkedin.com/in/phhitachi
