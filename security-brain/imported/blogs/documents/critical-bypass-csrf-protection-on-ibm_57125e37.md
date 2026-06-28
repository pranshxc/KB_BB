---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-09_critical-bypass-csrf-protection-on-ibm.md
original_filename: 2018-10-09_critical-bypass-csrf-protection-on-ibm.md
title: '[Critical] Bypass CSRF protection on IBM'
category: documents
detected_topics:
- command-injection
- otp
- csrf
tags:
- imported
- documents
- command-injection
- otp
- csrf
language: en
raw_sha256: 57125e3746ae3dace64a53015209cfe97cdb1a56550a108e1bcbdd189b6f4137
text_sha256: 6e5853f53f5acec30ff813110263adff7ee88375571e7c4c133671952607bf0f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# [Critical] Bypass CSRF protection on IBM

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-09_critical-bypass-csrf-protection-on-ibm.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `57125e3746ae3dace64a53015209cfe97cdb1a56550a108e1bcbdd189b6f4137`
- Text SHA256: `6e5853f53f5acec30ff813110263adff7ee88375571e7c4c133671952607bf0f`


## Content

---
title: "[Critical] Bypass CSRF protection on IBM"
url: "https://medium.com/bugbountywriteup/critical-bypass-csrf-protection-on-ibm-313ffb68dd0c"
authors: ["Mohamed Sayed (@FlEx0Geek)"]
programs: ["IBM"]
bugs: ["CSRF"]
publication_date: "2018-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5656
scraped_via: "browseros"
---

# [Critical] Bypass CSRF protection on IBM

[Critical] Bypass CSRF protection on IBM
Mohamed Sayed
Follow
2 min read
·
Oct 9, 2018

200

1

IBM

What is CSRF attack?
CSRF is an attack that tricks the victim to send a malicious request this request can change the victim information like Email, Username, Passwords and etc…

What did I found on IBM?
when trying to change my email on my test account I notice that the website change it by using a GET request
( https://www.ibm.com/ibmweb/myibm/account/sendmail?locale=us-en&email=NEW_EMAIL )
this link used to change the email so I didn’t notice any CSRF token to protect the website from the CSRF attack I try to exploit it but it’s not worked because of the website check the Referer Header :( I was like:

but I tried more and after a few hours I found a Bypass to this protection when I change the Referer Header value it returned an error but when I use this value it returned true
( https://www.ibm.com/ibmweb/myibm/profile/profile-edit.jsp )
so I tried to spoof this protection and I found a bypass by using this URL
( http://my_website/www.ibm.com/ibmweb/myibm/profile/profile-edit.jsp.php )
what I did is make the valid URL as a path on my website so now the request will be sent from ( profile-edit.jsp.php )to the IBM website to change the email when I try this method it worked I was like:

So now I can steal the accounts of IBM users by just visit my website :P.

Get Mohamed Sayed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

POC Video:

Report Sent: Sep 14th
Triaged on: Sep 28th
Solved on: Oct 8th

I hope that this topic helped someone and I want to thank @zseano for helping me.
