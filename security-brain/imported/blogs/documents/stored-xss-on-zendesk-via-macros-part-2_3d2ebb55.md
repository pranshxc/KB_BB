---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-20_stored-xss-on-zendesk-via-macros-part-2.md
original_filename: 2019-09-20_stored-xss-on-zendesk-via-macros-part-2.md
title: Stored XSS on Zendesk via Macro’s PART 2
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 3d2ebb5519ad3a85f3b34ea10847216c509beeb5af3f6adfb072c5b9fb18afc5
text_sha256: 83cf308a1b37b45aa02171a14b412c32356b6288c7356cb4653d4df794ae4bcd
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Zendesk via Macro’s PART 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-20_stored-xss-on-zendesk-via-macros-part-2.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `3d2ebb5519ad3a85f3b34ea10847216c509beeb5af3f6adfb072c5b9fb18afc5`
- Text SHA256: `83cf308a1b37b45aa02171a14b412c32356b6288c7356cb4653d4df794ae4bcd`


## Content

---
title: "Stored XSS on Zendesk via Macro’s PART 2"
url: "https://medium.com/@hariharan21/stored-xss-on-zendesk-via-macros-part-2-676cefee4616"
authors: ["Hariharan.s (@DJHARIZ1)"]
programs: ["Zendesk"]
bugs: ["Stored XSS"]
publication_date: "2019-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5018
scraped_via: "browseros"
---

# Stored XSS on Zendesk via Macro’s PART 2

Stored XSS on Zendesk via Macro’s PART 2
Hariharan S
Follow
2 min read
·
Sep 20, 2019

92

1

Hi Guys,

This is the continuation of my first write of Stored XSS Via Alternate Text At Zendesk Support.

So let's get back to business..As i was investing the XSS issue on the platform i noticed that the XSS Popup was triggered TWO times on the homepage. So i searched for the endpoint where the XSS payload got executed.

But no luck, So i removed my payload from the first vulnerable endpoint that is the Alternate Url Text and checked the homepage. To my suprise the XSS pop triggered as usual but this time it pop’d up only ONCE.

So i look up the macro if i had entered the payload anywhere else and of course i had entered a payload on the macro description field. So i found an another vulnerable endpoint. Time for POC.

For POC purposes i created a fresh macro and entered the payload on the macro description field and click on save…A Web Application Firewall(WAF) came smiling upon me Saying “YOU HAVE BEEN BLOCKED”.

WAF BYPASS TIME!!!!!!!!!!!!!!!

After learning about the working of the WAF i found out a “Not so Complicated” Method to bypass It.

Don't Enter the payload in beginning itself while creating the macro. Instead while creating the macro just enter random things in the description and after creating the macro edit the description and enter the payload.

Get Hariharan S’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Shorter version : WAF only scans the content that is entered the first time and does not care what you enter afterwards.

Press enter or click to view image in full size

After this BYE BYE WAF. The payload got saved successfully and also got triggered on the homepage.

Report Timeline :

Aug 10th- Report Submitted
Aug 11th- Closed as duplicate of my first report
Aug 17th- Report reopened after providing info that the two xss issues are different
Aug 23rd- Bounty Time $$$
Aug 26th- Resolved and Got listed on their HOF

Few Things to Say..

Check the number of XSS triggers ( Number of XSS triggers = Number of Vulnerable endpoints)
Try to Bypass the WAF by not only changing the payload.

3. The payload that i used is <img src=x onerror=alert(document.cookie)>

MAY THE BUGS BE WITH YOU,

P5YCH0(@Neo_X37)
