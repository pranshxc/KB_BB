---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-06_how-i-could-have-accessed-all-your-private-videosphotos-saved-inside-your-device.md
original_filename: 2021-06-06_how-i-could-have-accessed-all-your-private-videosphotos-saved-inside-your-device.md
title: How I could have accessed all your private videos/photos saved inside your
  device without even unlocking it?
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- mobile-security
language: en
raw_sha256: aa9489f3e2a4587f208532c969e9cab4b4993bfe9681fe6b191946c8a0fc396d
text_sha256: 28ace33345ed12d97627abaf3adda41902851d26d055461c787ca57635ec20d8
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I could have accessed all your private videos/photos saved inside your device without even unlocking it?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-06_how-i-could-have-accessed-all-your-private-videosphotos-saved-inside-your-device.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `aa9489f3e2a4587f208532c969e9cab4b4993bfe9681fe6b191946c8a0fc396d`
- Text SHA256: `28ace33345ed12d97627abaf3adda41902851d26d055461c787ca57635ec20d8`


## Content

---
title: "How I could have accessed all your private videos/photos saved inside your device without even unlocking it?"
url: "https://samiparyal.medium.com/how-i-could-have-accessed-all-your-private-videos-photos-saved-inside-your-device-without-even-1a7e455ddcc8"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "3,150"
publication_date: "2021-06-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3594
scraped_via: "browseros"
---

# How I could have accessed all your private videos/photos saved inside your device without even unlocking it?

How I could have accessed all your private videos/photos saved inside your device without even unlocking it?
Samip Aryal
Follow
4 min read
·
Jun 6, 2021

843

2

…

Press enter or click to view image in full size

This writeup is about how a user’s Sensitive Private Data like photos/videos saved inside his/her device could have been leaked out through a Facebook Room Call even from a locked Android device.

…

In October 2020; I submitted a valid vulnerability report in Facebook Whitehat Program where users’ private saved videos/watch history could have been exposed from the watch together feature in a Messenger call from a locked Android device.

User’s private watched videos’ List, saved videos, etc.
This writeup is about a vulnerability exposing user’s private watched videos list, saved videos, shared videos, etc…

infosecwriteups.com

Shortly Summarizing, there; users could have made a messenger call to the victim’s account and then receive the call from the victim’s locked Android phone to use the ‘Watch Together’ feature from the call screen without unlocking the phone thus allowing the intruder to get access to all of the saved videos & Watch History of the Facebook user. So, basically; the vulnerability here was that Facebook was allowing users to use such a sensitive feature like Watch Together even from a locked state of the device. Facebook patched this one along with similar such vulnerabilities by asking first to unlock the phone before using such sensitive features from a locked Android phone.

So, one day; some thoughts triggered in my mind when I suddenly remembered that report:

1) What if, instead of a normal Messenger Call; it was a Room Call?

,

2) Is there similar such sensitive feature available in a room call which can be accessed from outside the lock screen without unlocking the phone?

So, `without any delay`,

I made two test Facebook accounts; one logged into my Android Phone (Let, UserA-Victim) and another logged into my PC(Let, UserB-Attacker).
Here, UserA’s Android Phone was in a Locked state.
Then, from UserB, I hosted a Messenger Room and invited UserA to the room & joined the room myself too.
Then, from UserB; I called UserA from the ‘invited users’ section.
After some seconds, the call rung up in UserA’s Locked Android Phone.
I then picked up the call and tried all previously known sensitive features like ‘watch together’, ‘add people’, etc. but all of them needed to first unlock the phone before using them.
Then, Suddenly, I saw something like this at the top right corner of the call:
“Noticed That?”

There’s a chat option for the group formed between the room attendees.

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, getting excited I clicked it immediately.

Then, as soon as I clicked, a beautiful view popped out like this:

Press enter or click to view image in full size

I was like:

Not only because I just knew that I could message the group without even unlocking the phone but because of that gallery option present there at the side of the text box.

So, immediately; I clicked on that option at the fastest possible velocity.

After seeing that scenery, I was like:

I found that I could access all private photos/videos on that device without even unlocking the phone. Moreover; I could post stories to the victim_user’s Logged-In Facebook from the same locked state by clicking on the ‘edit’ option for any media.

So, wrapping up all the information, I quickly made a report to Facebook. Facebook Security Team made a quick-hot fix of the vulnerability at the client-side as well as they did some tweaks at server-side to patch it in previous vulnerable versions, in just less than a day after triage and rewarded me with an awesome bounty that I didn’t even expect for an attack scenario requiring physical reach to the victim’s device. Though, I appreciate their decision for the bounty based on the scope of what impact this vulnerability would have brought among the Android FB users.

Final Reward Message

If you would like to check the POC video of this vulnerability that I sent with the report, you can find it here.

…

Thank you for reading this write-up about the simple scenario of a highly impacting vulnerability. If you have any queries/suggestions, I’m available on Facebook/ Instagram.

…

Android screen lock protection thwarted by Facebook Messenger Rooms exploit
Adam Bannister 14 June 2021 at 12:40 UTC Updated: 14 June 2021 at 13:27 UTC Researcher earns $3,000 bug bounty after…

portswigger.net
