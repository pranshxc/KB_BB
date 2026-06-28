---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-28_clickjacking-to-account-takeover.md
original_filename: 2020-05-28_clickjacking-to-account-takeover.md
title: Clickjacking to Account Takeover
category: documents
detected_topics:
- command-injection
- sqli
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- command-injection
- sqli
- otp
- csrf
- clickjacking
language: en
raw_sha256: b9822c8a0530ed354c79ef72ff97fe7a10e730aa72fc5f42c6ad68d784d3fcc2
text_sha256: b812f537abf17ef6d92ce862023c0778e8cf4358606d7fefea459c441eaee122
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Clickjacking to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-28_clickjacking-to-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `b9822c8a0530ed354c79ef72ff97fe7a10e730aa72fc5f42c6ad68d784d3fcc2`
- Text SHA256: `b812f537abf17ef6d92ce862023c0778e8cf4358606d7fefea459c441eaee122`


## Content

---
title: "Clickjacking to Account Takeover"
url: "https://medium.com/@abhishake100/clickjacking-to-account-takeover-97e286f26b95"
authors: ["Abhishek Yadav (@abhishake100)"]
bugs: ["Clickjacking"]
publication_date: "2020-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4556
scraped_via: "browseros"
---

# Clickjacking to Account Takeover

Clickjacking to Account Takeover
Abhishek
Follow
3 min read
·
May 28, 2020

193

2

Curated list of Bug bounty programs — https://bugbountydirectory.com

Clickjacking is an attack in which a user is tricked to click on something that he didn’t intend to, meaning an attacker could possibly make any actions that a user can do on the webapp just like CSRF. But clickjacking requires user interaction to do a following task whereas CSRF requires no interaction as it can be triggered automatically using javascript.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Its considered low finding tbh but if you find a url which has some critical actions like deleting or adding an user, or changing users email then some companies might consider it as a medium/high finding like Google.

Clickjackings in Google worth 14981.7$
Instead of going for Cross Site Scripting, Remote Code Execution, SQL Injection, etc. I decided to find clickjacking in…

medium.com

So i was looking for bugs on a website and reported a CSRF issue which led to account takeover. After a few weeks they fixed it by adding a CSRF Token/Key on the request like so.

Press enter or click to view image in full size

Tried bypassing it with various ways but had no luck, until i discovered that the page is vulnerable to clickjacking. I use a website which helps me know if a url can be clickjacked or not.

Clickjacking / framing test
Edit description

www.lookout.net

Since the url is vulnerable to clickjacking it bypasses all CSRF protection. This page lets me change the name and email of the user which looked like this.

Press enter or click to view image in full size

To exploit this i created a page in which the user has to drag something to a box and then a click a button. But what was really happening at the back was that the user was dragging text and putting it in the Email box and then clicking Save Changes which led to account takeover.

Press enter or click to view image in full size

The code of the HTML can be found here https://pastebin.com/av71Mmf9 You can position the finish button and the red blob as your requirement and also change the text in the “DRAG ME TO THE RED BOX” text.

I thought this was enough for POC and the impact was also high, so i sent the report and it got accepted. They fixed and rewarded me pretty quickly. Hope you learned something.

Follow me on twitter — https://twitter.com/abhishekY495

Thank You.😁
