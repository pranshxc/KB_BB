---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-23_how-i-got-apple-hall-of-fame-.md
original_filename: 2022-04-23_how-i-got-apple-hall-of-fame-.md
title: How I got Apple Hall Of Fame !
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- mobile-security
language: en
raw_sha256: 0528ad5472f5f9c0d1fd7f9d1845176263742a8f7793b08cddb27c5ce499e882
text_sha256: ee57c07ba0dbc4ff1beee9603129ba8dbc0b602fa2280147248500cce2ed98e6
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How I got Apple Hall Of Fame !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-23_how-i-got-apple-hall-of-fame-.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, mobile-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `0528ad5472f5f9c0d1fd7f9d1845176263742a8f7793b08cddb27c5ce499e882`
- Text SHA256: `ee57c07ba0dbc4ff1beee9603129ba8dbc0b602fa2280147248500cce2ed98e6`


## Content

---
title: "How I got Apple Hall Of Fame !"
url: "https://shubhdeepp.medium.com/how-i-got-apple-hall-of-fame-3d86f858c05f"
authors: ["shubhdeep (@Shubhdeeppp)"]
programs: ["Apple"]
bugs: ["Content injection"]
publication_date: "2022-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2688
scraped_via: "browseros"
---

# How I got Apple Hall Of Fame !

How I got Apple Hall Of Fame !
shubhdeep
Follow
3 min read
·
Apr 23, 2022

111

2

Press enter or click to view image in full size

Introduction :

When a web application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain

How did I find this ?

Subdomain Enumeration
Probing for Live Assets
Active & Passive reconnaissance

During the third phase, while performing passive reconnaissance. A URL catches my attention.

Tool Used : https://github.com/lc/gau

Passive recon — gau

URL : https://activate.apple.com/success?deviceType=TV&appleId=donmac%40me.com

When I tried opening this URL, I got the following results. At that moment, I realized that it might be vulnerable to text injection.

Press enter or click to view image in full size
Response — activate.apple.com

When I supplied content via parameter “appleId” then it was reflected back in the response. The reflection was so beautiful & capable enough to make a victim believe that the modified page is real under the context of the trusted domain

Get shubhdeep’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

URL : https://activate.apple.com/success?deviceType=TV&appleId={Vulnerable to text injection}

Press enter or click to view image in full size
Modified Page — Text injection

Since It was more beautiful than other scenarios of text injection. I quickly made a detailed report and submitted it to apple for review. Guess what ? They accepted the report and made a fix.

Press enter or click to view image in full size
Asked for details

How they made a fix ?

Before reporting the issue, When I analyzed source code of the webpage.
I came across a JavaScript file :
https://activate.apple.com/success.4d4adb99f76951f234a1.js
After the fix, they removed the parameter “appleID”
Press enter or click to view image in full size
Before vs After

Now, Visiting the same URL gives the following result :

Press enter or click to view image in full size
Response

Hall of Fame:

Press enter or click to view image in full size
Hall of Fame

Timeline :

October 30, 2021 : Reported

November 2, 2021 : Triaged

February 22, 2022 : Resolved

April 20, 2022 : Credited
