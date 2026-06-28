---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-13_users-private-watched-videossaved-videos-exposed-through-a-messenger-call-from-a.md
original_filename: 2020-11-13_users-private-watched-videossaved-videos-exposed-through-a-messenger-call-from-a.md
title: User’s private watched videos/saved videos exposed through a messenger call
  from a locked smartphone.
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
- api-security
- mobile-security
language: en
raw_sha256: 9cd28047d765c23a5de59fc927e828889d2ed4e43f72794a4ad714d98d875655
text_sha256: 2e1473b6e90221185dbddb9b69ae44051a4b80ae98d937d59848f8073d1f5d33
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# User’s private watched videos/saved videos exposed through a messenger call from a locked smartphone.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-13_users-private-watched-videossaved-videos-exposed-through-a-messenger-call-from-a.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `9cd28047d765c23a5de59fc927e828889d2ed4e43f72794a4ad714d98d875655`
- Text SHA256: `2e1473b6e90221185dbddb9b69ae44051a4b80ae98d937d59848f8073d1f5d33`


## Content

---
title: "User’s private watched videos/saved videos exposed through a messenger call from a locked smartphone."
page_title: "User’s private watch history/saved videos exposed through a call in Locked Android Device | by Samip Aryal | InfoSec Write-ups"
url: "https://medium.com/@aryalsamipofficial59/users-private-watched-videos-list-saved-videos-etc-30faa8610b33"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Broken authorization"]
bounty: "500"
publication_date: "2020-11-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4141
scraped_via: "browseros"
---

# User’s private watched videos/saved videos exposed through a messenger call from a locked smartphone.

User’s private watch history/saved videos exposed through a call in Locked Android Device
Samip Aryal
Follow
2 min read
·
Nov 13, 2020

280

1

This writeup is about a vulnerability exposing user’s private watched videos list, saved videos, shared videos, etc. from the ‘WATCH TOGETHER’ feature in a locked phone.

A month back, I read an article from a researcher about the messenger calls exposing the user’s private friends’ list from a locked phone. So, I retested it the same day to check again if some other information were leaking out without unlocking a phone or not. That day I got none, Facebook fixed the bug by adding an extra security layer, simply afterthat; no one was able to access the feature without unlocking the phone.

Now, recently Facebook launched the ‘Watch Together’ feature in Messenger. So, I made some looks over there as well as tested the section using Burp after I got to use the feature. I found nothing intriguing that day.

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But then, the next day; I just remembered that valid bug from the researcher. Thus, I did some tests. Interestingly, I found a similar type of vulnerability in the Watch Together section, where any person with physical reach to the victim’s device could access the User’s Private Watched Videos List, Saved Videos List as well as the videos shared in the chat thread without unlocking the phone. I quickly reported it to Facebook with a short POC video. Facebook fixed it after some weeks. Now, you have to unlock the phone to use the watch together feature.

Reproduction Steps
==
1. User A’s smartphone is in a locked state.
2. User B calls User A.
3. Intruder picks up the call.
4. Intruder goes to the ‘Watch Together’ option.
5. Intruder sees User A’s entire private lists of Watched videos, Saved videos, videos shared in the chat thread, etc. without unlocking the phone.

…

Impact
===
This vulnerability could let anyone with physcial access to victim’s device view/access the user’s private saved videos, user’s entire watched videos, and also the videos shared in the chat thread without unlocking the phone. This would have affected the privacy/security of the user heavily.

…

Timeline

Reported — Saturday, 17 October 2020

Pre-Triaged — Thursday, 22 October 2020

Triaged — Thursday, 22 October 2020

Fixed — Monday, 9 November 2020

Fixed confirmed — Thursday, 12 November 2020

Bounty Rewarded — Thursday, 12 November 2020

Bounty Reward Message From Facebook

Thank you for reading this write-up about a simple vulnerability. If you have any suggestions/queries, I’m available on Facebook/ Instagram.

Try reading more bug writeups and keep yourself updated :)
