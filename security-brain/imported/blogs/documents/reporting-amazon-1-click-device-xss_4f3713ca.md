---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-12_reporting-amazon-1-click-device-xss.md
original_filename: 2019-08-12_reporting-amazon-1-click-device-xss.md
title: Reporting - Amazon 1 click device XSS
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
raw_sha256: 4f3713caf8f3a88e46067c79b8b696050e4d7761d9a127d5ac4d73cff2b55c40
text_sha256: 2eb22cb7bf94573c6fb90295f805a97b9c22a05afa5ace265436bf787742a922
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Reporting - Amazon 1 click device XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-12_reporting-amazon-1-click-device-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `4f3713caf8f3a88e46067c79b8b696050e4d7761d9a127d5ac4d73cff2b55c40`
- Text SHA256: `2eb22cb7bf94573c6fb90295f805a97b9c22a05afa5ace265436bf787742a922`


## Content

---
title: "Reporting - Amazon 1 click device XSS"
page_title: "Posts/posts/Amazon_1_click_device_XSS.md at 2454456529ddeedb17237b4e9678f7d58d0ffdca · sneakerhax/Posts · GitHub"
url: "https://github.com/sneakerhax/Posts/blob/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/Amazon_1_click_device_XSS.md"
final_url: "https://github.com/sneakerhax/Posts/blob/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/Amazon_1_click_device_XSS.md"
authors: ["Sneakerhax (@sneakerhax)"]
programs: ["Amazon"]
bugs: ["XSS"]
publication_date: "2019-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5086
---

# Reporting - Amazon 1 click device XSS

I wanted to share a bug that is far from complicated but drives home the point that all data that is controlled by a user should be sanitized & output encoded if it will return back to the client. Sometimes because of the nature of the data developers assume that certain types of input can’t exist there. This is a trick I have used to find multiple bugs in the past couple of years.

All of my personal devices such as iPhone and iPad have names that can trigger XSS. I achieve this by naming the device some XSS payload such as the simple one found below:

[![alt text](/sneakerhax/Posts/raw/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20iphone%20payload.png)](/sneakerhax/Posts/blob/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20iphone%20payload.png)

This has triggered XSS on many different softwares including notification software, routers, and in this case Amazon. It does this because many of these softwares have a page that lists devices and is viewed by other users. In the case of Amazon the XSS was triggered when accessing the one click devices. The bug was reported through email as seen in the next section.

## Reporting the bug to Amazon

Report date: July 19th 2017

Issue fix confirmed: November 13th 2017

Reported to: Amazon Security [[security@amazon.com](mailto:security@amazon.com)]

Bug Type: XSS(Stored)

Description: Under the account settings for 1 click purchasing which can be found here: Your Account > Manage Default Address and 1-Click Settings The device names listed under 1-Click Status are not sanitized

POC: My phone name is <script>alert(1)</script> and once this is loaded into the 1-Click Status an alert window appears with the number 1

[![alt text](/sneakerhax/Posts/raw/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20POC.png)](/sneakerhax/Posts/blob/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20POC.png)

[![alt text](/sneakerhax/Posts/raw/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20browser%20console.png)](/sneakerhax/Posts/blob/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20browser%20console.png)

If you need additional information please let me know.

Thanks,

Justin

## Discovery of mobile compatibility and reporting (Update)

Additionally later I found that this could be triggered from a mobile phone as seen in the example below. This update was reported to Amazon on August 19th 2017:

[![alt text](/sneakerhax/Posts/raw/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20mobile%20POC.png)](/sneakerhax/Posts/blob/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20mobile%20POC.png)

## Fix implemantation

This issue was fixed by adding output encoding to the device listing. Additionally they have moved 1-click device listing to it’s own page under Your Account -> 1-Click settings -> Manager 1-Click for your devices:

[![alt text](/sneakerhax/Posts/raw/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20-%20fix.png)](/sneakerhax/Posts/blob/2454456529ddeedb17237b4e9678f7d58d0ffdca/posts/.img/Amazon%20-%201%20click%20XSS%20-%20fix.png)

## Conclusion

In this case the 1 click device list is only something that the user would view and the attack vector is through the name of their device. This means the only valid attack vector as I specified to them in a later email is to attack reps who assist me with my account and have to view my 1 click devices for troubleshooting. This however is not always the case in all bugs I have discovered. In other bugs I have discovered other users would be affected by my XSS payload.
