---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-25_waze-how-i-tracked-your-mother.md
original_filename: 2020-08-25_waze-how-i-tracked-your-mother.md
title: 'Waze: How I Tracked Your Mother'
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: c6526c3fb5e210a8303091aacf38b3474e3f45fc38e89fa66b7c6b23182392b2
text_sha256: 2bc1b0fcffa727af0b3cf81a4978ba31add187e4b9aa2119e9f27b035feb47e3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Waze: How I Tracked Your Mother

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-25_waze-how-i-tracked-your-mother.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c6526c3fb5e210a8303091aacf38b3474e3f45fc38e89fa66b7c6b23182392b2`
- Text SHA256: `2bc1b0fcffa727af0b3cf81a4978ba31add187e4b9aa2119e9f27b035feb47e3`


## Content

---
title: "Waze: How I Tracked Your Mother"
page_title: "Waze: How I Tracked Your Mother · malgregator"
url: "https://www.malgregator.com/post/waze-how-i-tracked-your-mother/"
final_url: "https://www.malgregator.com/post/waze-how-i-tracked-your-mother/"
authors: ["Peter Gasper (@malgregator)"]
programs: ["Google (Waze)"]
bugs: ["Logic flaw", "Information disclosure"]
bounty: "1,337"
publication_date: "2020-08-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4295
---

# Waze: How I Tracked Your Mother

Posted Aug 25, 2020

![](https://malgregator.com/post/waze-how-i-tracked-your-mother/waze_hu_70b19d7b27f9360.png)

_Update - this post received lots of attention worldwide:_  
_[Bruce Schneier: Tracking Users on Waze](https://www.schneier.com/blog/archives/2020/10/tracking-users-on-waze.html)_  
_[Threatpost: Google’s Waze Can Allow Hackers to Identify and Track Users](https://threatpost.com/googles-waze-track-users/160332/)_  
_[The Hindu: Google’s navigation software let hackers track and identify users](https://www.thehindu.com/sci-tech/technology/googles-navigation-software-let-hackers-track-and-identify-users/article32916640.ece)_  
_[Živé.sk: Slovák objavil chybu vo Waze. Umožňovala sledovať konkrétnych používateľov](https://zive.aktuality.sk/clanok/149267/slovak-objavil-chybu-vo-waze-umoznovala-sledovat-konkretnych-pouzivatelov/)_

I am a daily user of the Waze traffic navigation as it provides me with the vision of the near future when I am driving. It’s especially useful when you are driving a little bit faster and are afraid of fine. As a part of the interface Waze shows you random icons of other drivers who are nearby, what always interested me as a security engineer. Maybe there is a way to find out who are those people? As it turned out in many cases, it’s possible and it’s also possible to track them.

## Tracking random drivers

I found out that I can visit Waze from any web browser at [waze.com/livemap](https://www.waze.com/livemap) so I decided to check how are those driver icons implemented. What I found is that I can ask Waze API for data on a location by sending my latitude and longitude coordinates. Except the essential traffic information, Waze also sends me coordinates of other drivers who are nearby. What caught my eyes was that identification numbers (ID) associated with the icons were not changing over time. I decided to track one driver and after some time she really appeared in a different place on the same road.

I have spawned code editor and built Chromium extension leveraging `chrome.devtools` component to capture JSON responses from the API. I was able to visualize how users broadly traveled between the city districts or even cities themselves.

[![Real time tracking of a driver](https://malgregator.com/post/waze-how-i-tracked-your-mother/waze_tracking.png)](https://malgregator.com/post/waze-how-i-tracked-your-mother/waze_tracking.png)

Example data captured for a given user over time:
  
  
  "user-8<REDACTED>0": {
  "2019-12-15 14:09:00:000": {
  "x": 17.1345,
  "y": 48.1315
  },
  "2019-12-15 14:11:00:000": {
  "x": 17.1685,
  "y": 48.142
  },
  ...
  },
  

Once I was able to pair crawled location data with a unique ID, I knew that there must be a way to identify who is behind the icon.

## Finding who is behind the icon

There is a research paper [Unique in the Crowd: The privacy bounds of human mobility](https://www.nature.com/articles/srep01376) which tell us that _“four spatio-temporal points are enough to uniquely identify 95% of the individuals.”_ So I decided to find my own ID using just the Waze map. In the low-density area, I was able to track my ID by monitoring my own location. With enough time, an attacker would find out the victim ID by stalking it’s known location. This obviously does not scale for many accounts so I continued analyzing Waze API for some kind of oraculum that will translate ID to a username or vice versa.

Soon enough I had partial success. I found out that if user acknowledge any road obstacle or reported police patrol, user ID together with the username is returned by the Waze API to any Wazer driving through the place. The application usually don’t show this data unless there is an explicit comment created by the user, but the API response contains the username, ID, location of an event and even a time when it was acknowledged. Another privacy leak right there.

I quickly created a script that parsed json data and dumped them into human readable form.
  
  
  # example output of a script posted below:
  "Martin<REDACTED>": {
  "1569048403000": {
  "x": 17.140624523162845,
  "y": 48.144849615796936
  }
  },
  "Matej<REDACTED>": {
  "1569392866000": {
  "x": 17.140624523162845,
  "y": 48.144849615796936
  }
  },
  "Michael<REDACTED>": {
  "1569875132000": {
  "x": 17.140624523162845,
  "y": 48.144849615796936
  }
  

In order to leverage this leak, an attacker can pick multiple locations with high traffic and existing short/long running notification on the obstacle. The attacker will periodically call API and crawl the users that confirmed the existence of an obstacle. Many users are actually using their legitimate names as a username. Over time, determined attacker can build a dictionary of user names and their IDs. In parallel, an attacker can store all the icon locations and correlate them with the users.

Remediation for this leak is to show only names of people, which made comments or other social activity and are not expecting privacy.

**Advisory Timeline:**  
15.12.2019 - bug reported  
17.12.2019 - report was triaged  
19.12.2019 - accepted as a valid bug  
8.1.2020 - Vulnerability Reward Program panel has decided to issue a reward - $1337 24.1.2020 - bug bounty paid
