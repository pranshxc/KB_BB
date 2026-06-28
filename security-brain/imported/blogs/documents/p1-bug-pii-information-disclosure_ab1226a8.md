---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-08_p1-bug-pii-information-disclosure.md
original_filename: 2022-05-08_p1-bug-pii-information-disclosure.md
title: P1 Bug — PII information disclosure
category: documents
detected_topics:
- idor
- command-injection
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: ab1226a8dc9af2462ec5b2bc3a61438fb89d7fbd33be977b2b67ab790d63df14
text_sha256: 168d00905e68777e68c918af07f157d0b37797742f9ab90b4013e39c33ddb814
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# P1 Bug — PII information disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-08_p1-bug-pii-information-disclosure.md
- Source Type: markdown
- Detected Topics: idor, command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `ab1226a8dc9af2462ec5b2bc3a61438fb89d7fbd33be977b2b67ab790d63df14`
- Text SHA256: `168d00905e68777e68c918af07f157d0b37797742f9ab90b4013e39c33ddb814`


## Content

---
title: "P1 Bug — PII information disclosure"
url: "https://medium.com/@huntersherlock11/p1-bug-pii-information-disclosure-7669ebbb91a8"
authors: ["Huntersherlock"]
bugs: ["Information disclosure", "IDOR"]
publication_date: "2022-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2655
scraped_via: "browseros"
---

# P1 Bug — PII information disclosure

P1 Bug — PII information disclosure
Mariam
Follow
2 min read
·
May 9, 2022

225

3

Press enter or click to view image in full size

Hello amazing penetration testers and bug bounty hunters, I hope you all are fine ❤ In this blog I will be explaining the bug that I recently found on private program through which I was able to fetch the sensitive information. Let us call the program as example.com. There were many functionalities in it. one of them was that a person can give gifts to the another person. As I was testing this feature, I gave a gift to the a random person and after presenting gift I was redirected to final page. That was normal flow of the application.

Press enter or click to view image in full size

But then I noticed the URL which was something like that “https://example.com/gift-sent/?id=NzYwNDU%3D”

Id parameter

The id parameter was quite interesting to me. I understood the whole flow of application and got to know that the this was my id which was assigned to me after giving gift.

Get Mariam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Decoding Id parameter value

The Id was something like that NzYwNDU%3D. To decode that i first URL decoded the string. After that the id was like this “NzYwNDU=” which is base64 encode. Then I quickly base64 decoded this string which gave me a plain id “76045”.I changed the value of ID parameter “76045” to “76044” and BOOM!! the request was successful. I was able to see the name of person to whom someone gave a gift. That was kinda low impact bug. I don’t gave up. I looked at the source code and to my surprise I was able to see the sensitive information of any person who presented a gift to any person. Sensitive information included email, bank details, first name , last name. That was quite interesting.

Python Exploit

I made small script which helped me in automating my task. The script looked something like that

Press enter or click to view image in full size

Thanks ! I hope you enjoyed reading.
