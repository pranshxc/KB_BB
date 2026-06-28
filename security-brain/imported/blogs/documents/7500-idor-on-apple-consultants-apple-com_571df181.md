---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-20_7500-idor-on-apple-consultantsapplecom.md
original_filename: 2022-09-20_7500-idor-on-apple-consultantsapplecom.md
title: 7,500$ – IDOR on Apple [consultants.apple.com]
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 571df1815f19364c512d6bf33770b243d2dcdb2b53c42208375e421dee56a4e4
text_sha256: 126e7006e96459d8a498793ba080b38384d8208ccdd98531afbc5089d9d15526
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# 7,500$ – IDOR on Apple [consultants.apple.com]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-20_7500-idor-on-apple-consultantsapplecom.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `571df1815f19364c512d6bf33770b243d2dcdb2b53c42208375e421dee56a4e4`
- Text SHA256: `126e7006e96459d8a498793ba080b38384d8208ccdd98531afbc5089d9d15526`


## Content

---
title: "7,500$ – IDOR on Apple [consultants.apple.com]"
page_title: "7,500$ – IDOR on Apple [consultants.apple.com] – Apapedulimu"
url: "https://apapedulimu.click/idor-on-apple/"
final_url: "https://apapedulimu.click/idor-on-apple/"
authors: ["apapedulimu / Nosa Shandy (@LocalHost31337)"]
programs: ["Apple"]
bugs: ["IDOR"]
bounty: "7,500"
publication_date: "2022-09-20"
added_date: "2022-09-22"
source: "pentester.land/writeups.json"
original_index: 2147
---

![](https://apapedulimu.click/wp-content/uploads/2022/09/ciobulletin-apple-bug-bounty-program-825x499.jpeg)

# 7,500$ – IDOR on Apple [consultants.apple.com]

# **﷽**

**In the name of Allah, the Most Gracious, the Most Merciful.**

I’m lazy to write this actually, **because this issue is like another IDOR. Nothing special, you just need to change the ID, and you will get an IDOR as simple as that**. However, I need to write this because sometimes I question myself, that do I am worth it as Security Enthusiast? Hopefully, this post will keep me motivated me to keep it up! Let’s get started it!

## Start Hunting

I chose Apple on my Bug Bounty Journey at that time, because I was inspired by my friends who got a nice bounty from Apple. However, at that time I don’t have any fancy recon tools like Rengine. So, my simple recon is just dorking with keywords like this: **“site:*.apple.com”**

Long story short, I got the target and it’s from **consultants. apple.com. **Just like a normal bug bounty hunter, I started to poke around, register and log in and do the basic thing with the feels. I’ve found some endpoint that include some numeric ID. So, I think “**Hmmmmmmmmmm, lets try some IDOR on this thing** ”

## IDOR is (Usually) Simple

Quickly I create a new account for the second test account to check the IDOR, can’t believe that the endpoint is actually a vuln of IDOR, after that I check on another endpoint and it’s also vuln of IDOR!

**Vuln URL :**

– [https://consultants.apple.com/publicLocator/deleteApplication](https://consultants.apple.com/publicLocator/deleteApplication)

– [https://consultants.apple.com/publicLocator/submitJoinForm](https://consultants.apple.com/publicLocator/submitJoinForm)

**Step To Reproduce :**

  1. Go to [https://consultants.apple.com/publicLocator/applicationAcnForm?lang=us](https://consultants.apple.com/publicLocator/applicationAcnForm?lang=us)
  2. Use 2 Accounts ( A and B ) , Save the ID of account B
  3. Change data Account A / Delete the Data
  4. Change The ID to account B
  5. Will receive if data is saved
  6. Reload Account B
  7. Data Account B is changed.

## Simple Reporting

Not good enough to write an [awesome report](http://firstsight.me/) like other’s bug bounty hunters. I quickly report with simple words and describe where the vuln come from and attached the video to reproduce the issue. **Simple** , right?

## Wait is Pain

  * **Dec 17, 2020** – Report
  * **Dec 17, 2020** – First Respond
  * **Mar 4, 2021** – “Any Update?”
  * **Mar 4, 2021** – “Your report is duplicate!” -Apple
  * **Mar 4, 2021** – “Are you sure?”
  * **Mar 4, 2021** – “Sorry, no! My mistake” -Apple
  * **Mar 4, 2021** – “You got me a heart attack for a second.”
  * **Mar 11, 2021** – “7,500$ Bounty is coming!” – Apple

## Acknowledge Link:

  * https://support.apple.com/en-ug/HT212711
  * https://support.apple.com/en-ug/HT201536

## Published by

![](https://secure.gravatar.com/avatar/4a2c0028ce53c37ad1d454a4dd5fb9ef9b89570464cdfbbc14e7e4914a284f17?s=56&d=mm&r=g)

### apapedulimu

Urip Kui Urup [ View all posts by apapedulimu ](https://apapedulimu.click/author/apapedulimu/)

Posted on [September 20, 2022September 28, 2022](https://apapedulimu.click/idor-on-apple/)Author [apapedulimu](https://apapedulimu.click/author/apapedulimu/)Tags [Apple Bug Bounty](https://apapedulimu.click/tag/apple-bug-bounty/), [IDOR](https://apapedulimu.click/tag/idor/)
