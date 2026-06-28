---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-20_unlimited-report-user-in-instagram-facebook-leads-to-abuse-risk.md
original_filename: 2021-09-20_unlimited-report-user-in-instagram-facebook-leads-to-abuse-risk.md
title: Unlimited report user in Instagram (Facebook) leads to abuse risk.
category: documents
detected_topics:
- rate-limit
- command-injection
tags:
- imported
- documents
- rate-limit
- command-injection
language: en
raw_sha256: 33898217dcbfdf88d82838b81c30c2247415e66920de86eeead95ed075c4e3aa
text_sha256: 49d5c454f961c527147954e44de840dbb206dc60120a3a8951d64b7d91471ae3
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Unlimited report user in Instagram (Facebook) leads to abuse risk.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-20_unlimited-report-user-in-instagram-facebook-leads-to-abuse-risk.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `33898217dcbfdf88d82838b81c30c2247415e66920de86eeead95ed075c4e3aa`
- Text SHA256: `49d5c454f961c527147954e44de840dbb206dc60120a3a8951d64b7d91471ae3`


## Content

---
title: "Unlimited report user in Instagram (Facebook) leads to abuse risk."
url: "https://infosecwriteups.com/unlimited-report-user-in-instagram-facebook-leads-to-abuse-risk-efcca325aada"
authors: ["Mano Prasanth"]
programs: ["Meta / Facebook"]
bugs: ["Lack of rate limiting"]
publication_date: "2021-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3301
scraped_via: "browseros"
---

# Unlimited report user in Instagram (Facebook) leads to abuse risk.

Unlimited report user in Instagram (Facebook) leads to abuse risk.
Mano Prasanth
Follow
3 min read
·
Sep 20, 2021

25

Hello, it’s Mano Prasanth here,

Press enter or click to view image in full size
Photo by Alexander Shatov on Unsplash

This write-up is about a simple Rate-limiting bug which I found on Instagram.

This is my first bug report at Instagram. As a noob bug hunter, I tried various hunting methods to find a bug in Facebook. First, I started with Authentication and moved further into other types. But it seemed everything was secure with authentication, to my knowledge :/ (Anyway nothing is completely secure).

Before this report, I was hunting in the Bugcrowd, but unfortunately my previous reports were duplicated. Then I started to hunt private programs and got some valid bugs. Then thought of finding bugs in GAFAM and decided to hunt for Facebook’s acquisitions.

This isn’t a severe bug but rather a low-level bug that has the potential to get rid of your enemies in Instagram Lol.

Get Mano Prasanth’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This bug allowed anyone on Instagram to report a user unlimited number of times (Abuse risk). If you try to do it manually, you might end up frustrated or wasting a day. Generally, most of the tech giants limit these types of bugs by rate limiting in their POST requests or by using WAF, Captcha, etc. But Instagram haven’t implemented any rate limit in the report user feature. To start the attack, I used Burpsuite to manipulate the Request-Reponse cycle. In Instagram before submitting the report, I have intercepted that particular POST request and forwarded it to the intruder to make it easier. Then, I have selected a position for payload. Choosing the position for payload should not have any effect on the response. Instead of NULL Payload I have chosen a position in the Header - Accept-Language: en-US,en;q=0.$5$. Then I started the attack with 100 payloads. I got HTTP 200 OK Status Code & all reports submitted in the response like “text”:”Thank you, we received your report”. Generally, you will get Rate limit exceeded response after four to five POST request. But…….

Below is the impact of the attack which I submitted to Facebook.

Impact:
It seems that there is no rate limiting in the user account report feature which leads to a large number of report submission. It will stack up in your reports causing inconvenience to work with the report feature. You may not know whether the reports are true or not unless you check it individually, and it may lead to spam with this feature.

I know rate-limit-related bugs usually don’t qualify for bounties. But I tried to report my close friend from four Instagram demo accounts each with 100 reports and everything worked perfectly. I didn’t complete these attacks and immediately terminated the attack to report this issue to Facebook. So, this may definitely gain some attention from Facebook. There are two chances here. They may either filter the reports arising from same accounts or they might not inspect every report and only just look at the number of counts. If the latter is true then there are some chances that your account might be considered for deletion. You don’t know unless you are an employee at Facebook managing this report feature. Facebook admitted that they won’t look into each report but if an account reaches enough reports, then we will examine some reports and take action against it. Though Facebook has internal protocols to deal with before deleting a user, this bug could have allowed anyone to spam Instagram users and Facebook’s internal infrastructure.

Press enter or click to view image in full size
Acknowledgment from Facebook

Though rate-limiting bugs don’t get me bounties, it’s quite amusing to spam friends. I once sent 179 invitation messages (better than SMS bomber) within a span of 5 minutes with the help of a misconfigured rate limit in the landing page of Glance.

Thanks for reading:)

Happy Hunting!!

LinkedIn: https://www.linkedin.com/in/mano-prasanth-m-908b061b8/
