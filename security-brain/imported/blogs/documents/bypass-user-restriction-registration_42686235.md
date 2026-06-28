---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-18_bypass-user-restriction-registration.md
original_filename: 2020-07-18_bypass-user-restriction-registration.md
title: bypass user-restriction registration
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 426862351378b1149a10416e9707a8a9567ed73064e1c2bd571a33fc7499bee1
text_sha256: a1183b36367cb86b5de22759aec4007990cefdd5e213b6ff685ee576939bed56
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# bypass user-restriction registration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-18_bypass-user-restriction-registration.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `426862351378b1149a10416e9707a8a9567ed73064e1c2bd571a33fc7499bee1`
- Text SHA256: `a1183b36367cb86b5de22759aec4007990cefdd5e213b6ff685ee576939bed56`


## Content

---
title: "bypass user-restriction registration"
url: "https://medium.com/@mohamedayad_72488/bypass-user-restriction-registration-cbfc4eb855"
authors: ["Mohamed Ayad"]
bugs: ["Logic flaw", "Payment tampering"]
publication_date: "2020-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4398
scraped_via: "browseros"
---

# bypass user-restriction registration

bypass user-restriction registration
Mohamed Ayad
Follow
2 min read
·
Jul 18, 2020

105

1

peace upon you guys..

today i will came across another interesting bug that i found in the same last target u can reach it from here block user from resetting his password

Press enter or click to view image in full size

so let’s begin, while moving around and investigating site features i found a function that allowd you to add multiple users to the same account so i added some users and left the site..

Press enter or click to view image in full size
add users

after some weeks i found that my free trial has ended, i got to a subscription page and it was we can say like that:

subscription page

primary email = 1500$

every additional user = 600$

so if you have added another 2 users for your account, total subscription price will be 1500+ 2(600) = 2700$

there also some (+) and (-) buttons to add more users but (-) one was disabled untill you have pressed (+) one

meaning if u have added 2 users the (-) will be disabled else u decided to add more user (-) will be enabled again untill u reach your 2 users again

Get Mohamed Ayad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so what i did was that i opened subscription page, (-) was disabled now i have inspected element and found disable attribute in the (-) button input

so i just removed it and hit the (-) button and removed the 2 added users

and when pushing subscription button i only was asked to pay for my pimary user 1500$

steps to reproduce:

1- enter your account and add another 2 users

2- in the payment page, hit F12 on keyboard and remove the “disabled” attribute from (-) button

3- remove additional users and hit subscripe

And bingooo !! you have bypassed additional users taxes

thank you for reading ! hope you enjoyed it…

you can find me on twitter @0xMohamed_Ayad

also linkedin @0xmh3yad
