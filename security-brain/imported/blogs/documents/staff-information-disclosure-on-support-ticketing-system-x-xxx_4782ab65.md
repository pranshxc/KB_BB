---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-22_staff-information-disclosure-on-support-ticketing-system-xxxx.md
original_filename: 2021-01-22_staff-information-disclosure-on-support-ticketing-system-xxxx.md
title: Staff Information Disclosure on Support Ticketing System ($x,xxx)
category: documents
detected_topics:
- command-injection
- mfa
- information-disclosure
tags:
- imported
- documents
- command-injection
- mfa
- information-disclosure
language: en
raw_sha256: 4782ab65d0960bb2c0bba79dec6f66cbcc815633827463c02e4ffa9bfac576a0
text_sha256: 1d8c964e095c2625d2d00f9b0d1e9ac0ea01109a48bbcd44ee965cabeb996f59
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Staff Information Disclosure on Support Ticketing System ($x,xxx)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-22_staff-information-disclosure-on-support-ticketing-system-xxxx.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4782ab65d0960bb2c0bba79dec6f66cbcc815633827463c02e4ffa9bfac576a0`
- Text SHA256: `1d8c964e095c2625d2d00f9b0d1e9ac0ea01109a48bbcd44ee965cabeb996f59`


## Content

---
title: "Staff Information Disclosure on Support Ticketing System ($x,xxx)"
url: "https://ph-hitachi.medium.com/staff-information-disclosure-on-support-ticketing-system-p2-x-xxx-a08960aea7b1"
authors: ["Ph.Hitachi"]
bugs: ["Information disclosure"]
publication_date: "2021-01-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3977
scraped_via: "browseros"
---

# Staff Information Disclosure on Support Ticketing System ($x,xxx)

Staff Information Disclosure on Support Ticketing System ($x,xxx)
Ph.Hitachi
Follow
3 min read
·
Jan 22, 2021

154

Hi Guys,

So now i want to share my writes up how i got P2 and rewarded $x,xxx on private program so lets start.

What is Support Ticketing System?
Tickets can come from a variety of channels, such as social media, live chat or messaging, email, or the customer support portal that you have set up on your company’s website.

An omnichannel approach to customer service enables companies to streamline their ticket workflows by organizing requests from all your channels and bringing them to one comprehensive dashboard. Omnichannel ticketing systems allow queries from any channel, and support ticket systems give visibility into customer conversations across the organization, allowing the support team to collaborate to solve queries or pull relevant insights from tickets.

How i found this bug?
so first i im looking for information disclosure since i like hunting vulnerability on api and i see the “support ticket” in the side bar navigation and i try to open and issue.

i open issue with no description so i only wait to reply one of the their staff

but i view to the response my private info was return in api so means they can see my personal info but in my mind thats ok since they part of organization.

Get Ph.Hitachi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

after i day when im trying to find bug again the “burp suite” detect email address disclosed.

Press enter or click to view image in full size
in the issues burp suite dected “email address disclosed”

in the issues of email address disclosed in path “/api/***/tickets” burp suite get 2 emails 1 is my email and the second email is the staff email’s

me:

so i look in the response but not only emails that has been disclosed.

reply of their staff
Press enter or click to view image in full size

in the response we can see the date of account created, email,cellphone number,2FA pin,IPaddress, etc…

Press enter or click to view image in full size

Timeline Review
- Dec 18, 2020 (initials report)
- Dec 20, 2020 (Triaged)
- Dec 20, 2020 (Fixed)
- Jan 22, 2021 (Bounty Awarded)

Contact:
Email: ph-hitachi@wearehackerone.com
Twitter: https://x.com/PhHitachi
LinkedIn: www.linkedin.com/in/phhitachi
