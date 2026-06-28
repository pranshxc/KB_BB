---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-17_plan-change-logic-in-google-fiber-webpass.md
original_filename: 2020-02-17_plan-change-logic-in-google-fiber-webpass.md
title: Plan Change Logic in Google Fiber (Webpass)
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
raw_sha256: ef7d9e404940697d053d0cb9c5c94400e4a33a784bc591be25ffd860d8449576
text_sha256: 851f72d7a3d627ac9d008130eb10a8efa3bdc2139ab27f145c1a562d3d9ed0d3
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Plan Change Logic in Google Fiber (Webpass)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-17_plan-change-logic-in-google-fiber-webpass.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `ef7d9e404940697d053d0cb9c5c94400e4a33a784bc591be25ffd860d8449576`
- Text SHA256: `851f72d7a3d627ac9d008130eb10a8efa3bdc2139ab27f145c1a562d3d9ed0d3`


## Content

---
title: "Plan Change Logic in Google Fiber (Webpass)"
url: "https://s1gnalcha0s.github.io/logic/2020/02/17/Google-Fiber.html"
final_url: "https://s1gnalcha0s.github.io/logic/2020/02/17/Google-Fiber.html"
authors: ["Craig Arendt (@signalchaos)"]
programs: ["Google"]
bugs: ["Logic flaw", "Payment tampering"]
publication_date: "2020-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4767
---

> “Distracted from Distraction by Distraction” - T.S. Eliot

TLDR; Found a simple logic bug when paying my annual Google Fiber bill (Webpass).

I initially added a $50 payment to my Google Fiber (WebPass) annual subscription, and then switched from annual to monthly billing, and saw that $550 (the annual amount) was credited to the account, and $60 was billed to the account for the new subscription.
  
  
  POST /api/plan_changes HTTP/1.1
  Host: webpass.net
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  
  from_subscription_id=12345&cashier=

I then replayed the same API operation that was initially called to change the subscription about six more times and saw that each time I called it $550 was credited to the account, and $60 was billed to the account.

![Image](/assets/webpass/1.png)

At this point there was $2,450 credited to the account, and it showed that the previously invoiced amount had been paid. It would have been fun to call that API operation 100+ more times to see what would happen 😅, but I just reported it instead.

![Image](/assets/webpass/2.png)

It was covered under the Google VRP because Webpass is a 2016 Google Fiber acquisition. A few days later someone took the credits out of my account which reset my account balance back to $0.

Thanks to the Google VRP team. 👋

[@signalchaos](https://twitter.com/signalchaos)

Disclosure timeline stuff:

  * Nov 2019: Reported the plan_changes bug to the Google VRP
  * Jan 2020: Reported an authorization bug in some API operations that allowed customer subscriptions to be changed.
