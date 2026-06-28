---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-05_blind-xss-in-apple-school-enrollment-data-disclosure.md
original_filename: 2021-07-05_blind-xss-in-apple-school-enrollment-data-disclosure.md
title: Blind XSS in Apple School- Enrollment Data Disclosure
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
language: en
raw_sha256: d06f816c3a5a6f43d4e423ba7812259255c5083ecfa9378fc60c5c0983c2c2b1
text_sha256: a3957d9ff28b92f2978df91c1ad66003c870ce7796e3e71dce3e8d894532917d
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS in Apple School- Enrollment Data Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-05_blind-xss-in-apple-school-enrollment-data-disclosure.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `d06f816c3a5a6f43d4e423ba7812259255c5083ecfa9378fc60c5c0983c2c2b1`
- Text SHA256: `a3957d9ff28b92f2978df91c1ad66003c870ce7796e3e71dce3e8d894532917d`


## Content

---
title: "Blind XSS in Apple School- Enrollment Data Disclosure"
url: "https://hackrzvijay.medium.com/blind-xss-in-apple-school-enrollment-data-disclosure-a94c1da5bf54"
authors: ["hackrzvijay (@hackrzvijay)"]
programs: ["Apple"]
bugs: ["Blind XSS"]
bounty: "5,000"
publication_date: "2021-07-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3528
scraped_via: "browseros"
---

# Blind XSS in Apple School- Enrollment Data Disclosure

Blind XSS in Apple School- Enrollment Data Disclosure
.
hackrzvijay
Follow
2 min read
·
Jul 5, 2021

233

1

Hello!
I’am Hackrzvijay
I have found blind xss in apple school during october 2020..
Reproduction Steps:
During researching apple i have found one subdomain school.apple.com
In the enrollment form i have added my xss hunter payload multiple times which was created by iammandatory
After adding the payload the enrollment data has fired in my xss hunter within 5 to 10 seconds.
Nearly 420 records have been disclosed at the time of research but large number is possible in real time if continuously payload is added.
Press enter or click to view image in full size

Above is the data and below is the proof that my xsshunter payload has executed.

Get hackrzvijay’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Press enter or click to view image in full size
The data discloses like
Organization name
enrollee firstname and last name
country
assigned apple employee email
organziation type
Attacker if continuously adds the xsshunter payloads so he can get data in real time within 5 to 10 seconds.
Impact:
First attacker executes the vulnerable code in the back end.
Next attacker will retrieves the enrollment data in large number.
I have reported immediately to apple security and they fixed the bug immediately.
Reported: October 13th 2020
Bounty Rewarded: $5,000 on june 3rd 2021
Press enter or click to view image in full size
Thanks to apple security Team!
Follow me on twitter
