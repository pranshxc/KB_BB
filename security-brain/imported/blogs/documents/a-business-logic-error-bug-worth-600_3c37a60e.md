---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-23_a-business-logic-error-bug-worth-600.md
original_filename: 2021-11-23_a-business-logic-error-bug-worth-600.md
title: A business logic error bug worth 600$
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 3c37a60eb135654c88fb861fa7347a65ad1c70893a6332ee4b69f0aff1c1e711
text_sha256: bf28125bef032476f957e5782c592962c2f5517fbc585bd1e43e34ea67180d76
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# A business logic error bug worth 600$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-23_a-business-logic-error-bug-worth-600.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `3c37a60eb135654c88fb861fa7347a65ad1c70893a6332ee4b69f0aff1c1e711`
- Text SHA256: `bf28125bef032476f957e5782c592962c2f5517fbc585bd1e43e34ea67180d76`


## Content

---
title: "A business logic error bug worth 600$"
url: "https://itsdeepceh.medium.com/a-business-logic-error-bug-worth-600-a0050720bfee"
authors: ["Deep Patidar (@itsdeepceh)"]
bugs: ["Payment tampering"]
bounty: "600"
publication_date: "2021-11-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3148
scraped_via: "browseros"
---

# A business logic error bug worth 600$

A business logic error bug worth 600$
Deep Patidar
Follow
2 min read
·
Nov 23, 2021

573

5

Hey all,

Deep Patidar here, i hope all are doing good with good health. I am sharing my recent finding on hackerone private program, as terms and conditions i can not disclose the name of the program so call as target.com

lets say target.com has a functionality of refer a friend and if user will sign up and will activate paid plan, i will get 30$ as gift which referral code used by any other user while signup.

i was thinking like how can i use this functionality and abuse it. i thought lets check every request and try to manipulate price but there was server side validation so i didn’t get anything and like i can’t find

Press enter or click to view image in full size
Photo by Jason Strull on Unsplash

After sometime i thought that let me use referral code with new signup

Step to reproduce:

logged in my account and went to billing tab there was option for refer a friend
I used this URL for new signup with referral link but nothing got as if user will activate their paid plan then only i will receive 30$ for each new registration
I used this referral link for signup with new account and i activated paid plan as i had to pay 15$ for a month.

Now i logged in again in my account and checked wallet balance there was 30$ as i received because i shared my referral link to user for new signup.

Get Deep Patidar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now its time to ask for refund so logged in new signed up account and submit a request for refund on cancel the subscription and in few hour i have a response on my ticket “we have canceled your subscription and refund already generated ”

Again i logged in with my account as checked that 30$ what i received for referral signup is there or not and i was like

Press enter or click to view image in full size
Photo by bruce mars on Unsplash

Repeated this steps 3 times and now i have 90$ in wallet without getting paid anything, On the program if i will manage to get 300$ using same techniques i can make for 12 month premium subscription

Thank you for reading and have a great day ahead

Report Submitted — 13 Nov 2021

Triaged — 16 Nov 2021

Bounty paid — 600$ (17 Nov 2021)

Follow me on X — https://x.com/itsdeepceh

Follow me on LinkedIn — https://www.linkedin.com/in/deeppatidar/
