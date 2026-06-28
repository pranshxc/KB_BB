---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-15_securitybreach-how-i-was-able-to-book-hotel-room-for-150.md
original_filename: 2018-04-15_securitybreach-how-i-was-able-to-book-hotel-room-for-150.md
title: '#SecurityBreach — ''How I was able to book hotel room for 1.50₹!'''
category: documents
detected_topics:
- command-injection
- automation-abuse
- cors
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- cors
- api-security
language: en
raw_sha256: 7befc3d41a0d260c6f7a5b83fd21539f75a80a51a087d9e3fd1f40bf686575f2
text_sha256: f71c5ac77c9d638f5a1b476c60ecefa2546b4bdac6545aebcc1adf25ae176045
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #SecurityBreach — 'How I was able to book hotel room for 1.50₹!'

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-15_securitybreach-how-i-was-able-to-book-hotel-room-for-150.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cors, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `7befc3d41a0d260c6f7a5b83fd21539f75a80a51a087d9e3fd1f40bf686575f2`
- Text SHA256: `f71c5ac77c9d638f5a1b476c60ecefa2546b4bdac6545aebcc1adf25ae176045`


## Content

---
title: "#SecurityBreach — 'How I was able to book hotel room for 1.50₹!'"
page_title: "#SecurityBreach — “How I was able to book hotel room for 1.50₹!” | by Hariom Vashisth | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/securitybreach-how-i-was-able-to-book-hotel-room-for-1-50-9b35f18e49e8"
authors: ["Hariom Vashisth"]
bugs: ["CORS misconfiguration"]
publication_date: "2018-04-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5918
scraped_via: "browseros"
---

# #SecurityBreach — "How I was able to book hotel room for 1.50₹!"

Hariom Vashisth
 highlighted

#SecurityBreach — “How I was able to book hotel room for 1.50₹!”
Hariom Vashisth
Follow
3 min read
·
Apr 15, 2018

87

3

Let’s do it…

Press enter or click to view image in full size
Invoice
Understanding The Prospect::

Hotel booking website based in India for both married and unmarried couples. The site is responsible for booking hotel rooms in more than 40 Indian cities.

Prospect Identification:
I always search for custom made web-applications — ✔
API driven methodology — ✔
CORS Misconfiguration- ✔
Tools (worth mentioning)
Postman — chrome app — ✔
Postman Interceptor — ✔
Google Chrome browser — ✔
Let’s do it
Prerequisite:
Nothing more than you (Real You)

Remember! The gap between your bar and your ground level is the space where you suffer, because you do not experience reality as it is. Your body is here, and your thoughts are above. Ground level is where acceptance lives and we can experience peace and harmony with what is. — Unknown

We all are connected — How

Discover yourself with me — DreamAlarm

Aristotle: “Knowing yourself is the beginning of all wisdom.”

pretty much inspired! let’s understand how can we do this
open their wonderful dream website(example.com), Go to the Network Tab and Monitor XHR traffic
Press enter or click to view image in full size
chrome console -> Network Tab

2. Choose your favourite Hotel.

Press enter or click to view image in full size
Hotel Page — Before

Once you start monitoring network tab, you’ll get to know the way they process input data through API. Thanks to CORS -> * , you can do whole lot of experiment through postman. Capture their API call with postman interceptor and change the booking amount. Pay minimal amount and enjoy your day!

Get Hariom Vashisth’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Although I cancelled my booking as it was just a POC.

Press enter or click to view image in full size
Reporting Vulnerability through Email

D̶e̶s̶p̶i̶t̶e̶ ̶o̶f̶ ̶i̶n̶f̶o̶r̶m̶i̶n̶g̶ ̶t̶h̶e̶i̶r̶ ̶t̶e̶c̶h̶ ̶t̶e̶a̶m̶,̶ ̶t̶h̶e̶y̶ ̶d̶i̶d̶n̶’̶t̶ ̶p̶a̶y̶ ̶a̶t̶t̶e̶n̶t̶i̶o̶n̶ ̶t̶o̶ ̶t̶h̶e̶ ̶i̶d̶e̶n̶t̶i̶f̶i̶e̶d̶ ̶v̶u̶l̶n̶e̶r̶a̶b̶i̶l̶i̶t̶y̶.̶ ̶T̶h̶e̶ ̶d̶a̶y̶s̶ ̶a̶r̶e̶ ̶p̶a̶s̶s̶i̶n̶g̶ ̶a̶n̶d̶ ̶t̶h̶e̶ ̶s̶i̶t̶e̶ ̶i̶s̶ ̶g̶r̶o̶w̶i̶n̶g̶ ̶w̶e̶l̶l̶ ̶i̶n̶ ̶p̶r̶o̶f̶i̶t̶s̶ ̶b̶u̶t̶ ̶a̶l̶o̶n̶g̶ ̶w̶i̶t̶h̶ ̶t̶h̶i̶s̶ ̶i̶s̶s̶u̶e̶.̶ ̶I̶n̶ ̶t̶h̶e̶ ̶c̶o̶m̶i̶n̶g̶ ̶f̶u̶t̶u̶r̶e̶,̶ ̶t̶h̶e̶ ̶r̶e̶l̶a̶t̶i̶v̶e̶ ̶c̶o̶n̶s̶e̶q̶u̶e̶n̶c̶e̶ ̶a̶n̶d̶ ̶b̶o̶o̶m̶i̶n̶g̶ ̶p̶o̶s̶s̶i̶b̶i̶l̶i̶t̶y̶ ̶w̶i̶l̶l̶ ̶b̶e̶ ̶t̶h̶a̶t̶ ̶a̶n̶y̶ ̶h̶a̶c̶k̶e̶r̶ ̶o̶r̶ ̶s̶o̶f̶t̶w̶a̶r̶e̶ ̶p̶r̶o̶f̶e̶s̶s̶i̶o̶n̶a̶l̶ ̶c̶a̶n̶ ̶d̶u̶m̶p̶ ̶t̶h̶e̶i̶r̶ ̶e̶n̶t̶i̶r̶e̶ ̶d̶a̶t̶a̶b̶a̶s̶e̶ ̶a̶n̶d̶ ̶c̶a̶n̶ ̶m̶a̶k̶e̶ ̶i̶t̶ ̶p̶u̶b̶l̶i̶c̶.̶ ̶A̶s̶ ̶a̶ ̶r̶e̶s̶u̶l̶t̶,̶ ̶i̶t̶s̶ ̶r̶e̶p̶u̶t̶a̶t̶i̶o̶n̶ ̶a̶n̶d̶ ̶r̶e̶l̶e̶v̶a̶n̶c̶e̶ ̶w̶i̶l̶l̶ ̶g̶o̶ ̶o̶n̶ ̶d̶e̶c̶r̶e̶a̶s̶i̶n̶g̶ ̶b̶e̶c̶a̶u̶s̶e̶ ̶i̶t̶ ̶w̶i̶l̶l̶ ̶c̶r̶e̶a̶t̶e̶ ̶a̶ ̶m̶e̶n̶t̶a̶l̶i̶t̶y̶ ̶i̶n̶ ̶t̶h̶e̶ ̶m̶i̶n̶d̶s̶ ̶o̶f̶ ̶p̶e̶o̶p̶l̶e̶ ̶t̶h̶a̶t̶ ̶t̶h̶e̶ ̶f̶o̶l̶l̶o̶w̶i̶n̶g̶ ̶h̶o̶t̶e̶l̶ ̶b̶o̶o̶k̶i̶n̶g̶ ̶w̶e̶b̶s̶i̶t̶e̶ ̶f̶a̶i̶l̶e̶d̶ ̶t̶o̶ ̶k̶e̶e̶p̶ ̶t̶h̶e̶ ̶d̶e̶t̶a̶i̶l̶s̶ ̶c̶o̶n̶f̶i̶d̶e̶n̶t̶i̶a̶l̶ ̶a̶n̶d̶ ̶r̶u̶i̶n̶e̶d̶ ̶t̶h̶e̶i̶r̶ ̶f̶a̶i̶t̶h̶ ̶a̶n̶d̶ ̶t̶r̶u̶s̶t̶ ̶o̶n̶ ̶s̶u̶c̶h̶ ̶w̶e̶b̶s̶i̶t̶e̶s̶.̶

I am obsessed about security vulnerabilities and thought of contacting them again, not for reward or recognition, not for me, not for them… for those people who used their platform for booking hotel(s). So, without any single thought, I opened my gmail and wrote an email with some philosophical statements.

I successfully negotiate on emotions and as a programmer it is very difficult for me to convey my things in words. Finally, they understood my good intentions and started working on my report. After few days I received one email from “cyber vulnerability investigation” Manager about the investigation report and for my time he decided to give me some reward and also a security audit proposal.

Timeline:

Vulnerability Found: Mar 25

POC: Mar 27

Reported: Mar 28

Investigation Report: Apr 24

Bounty Rewarded: May 08

Happy Coding!

Thanks for reading!
This is all about this interesting finding. ☺
