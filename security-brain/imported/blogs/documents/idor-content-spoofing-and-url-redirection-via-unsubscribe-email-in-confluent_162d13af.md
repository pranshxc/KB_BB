---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-28_idor-content-spoofing-and-url-redirection-via-unsubscribe-email-in-confluent.md
original_filename: 2018-09-28_idor-content-spoofing-and-url-redirection-via-unsubscribe-email-in-confluent.md
title: IDOR, Content Spoofing and Url Redirection via unsubscribe email in Confluent
category: documents
detected_topics:
- idor
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- idor
- access-control
- command-injection
- business-logic
language: en
raw_sha256: 162d13af1618e638ac9607f44188aeeadae7b484061c600dafa79908848de9ca
text_sha256: 54c80d1036d6fd0bb5a56c189df608d0f590bf06b3c9cc28831c605fada5c0da
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR, Content Spoofing and Url Redirection via unsubscribe email in Confluent

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-28_idor-content-spoofing-and-url-redirection-via-unsubscribe-email-in-confluent.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `162d13af1618e638ac9607f44188aeeadae7b484061c600dafa79908848de9ca`
- Text SHA256: `54c80d1036d6fd0bb5a56c189df608d0f590bf06b3c9cc28831c605fada5c0da`


## Content

---
title: "IDOR, Content Spoofing and Url Redirection via unsubscribe email in Confluent"
url: "https://medium.com/@justmorpheus/idor-content-spoofing-and-url-redirection-via-unsubscribe-email-in-confluent-1fa7398cfe7a"
authors: ["Divyanshu Shukla (@justm0rph3u5)"]
programs: ["Confluent"]
bugs: ["IDOR", "Content spoofing", "Open redirect"]
publication_date: "2018-09-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5675
scraped_via: "browseros"
---

# IDOR, Content Spoofing and Url Redirection via unsubscribe email in Confluent

IDOR, Content Spoofing and Url Redirection via unsubscribe email in Confluent
Divyanshu
Follow
2 min read
·
Sep 28, 2018

137

Summary

While I was looking into my emails to unsubscribe from them, then there was mail from confluent. On copying the link, I found a subdomain https://sdr.confluent.io. Changing the id parameter allowed any user to be unsubscribed from confluent mails along with that it allowed content spoofing and after submitting on unsubscribing it redirected to the homepage. So after changing URL from the homepage to any website.

Background

Content spoofing, also referred to as content injection, “arbitrary text injection” or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application

Open Redirects are invalidated redirects and forwards are possible when a web application accepts untrusted input that could cause the web application to redirect the request to a URL contained within untrusted input.

Insecure Direct Object Reference refers to when a reference to an internal implementation object is exposed to users without any proper access control setting.

Unsubscribe Link

Link:
https://sdr.confluent.io/api/mailings/1xxxx7/unsubscribe_html?id=1xxxx7&message=ALERT:%20THERE%20HAD%20BEEN%20A%20MASSIVE%20BREACH%20AT%20OUR%20DATA%20CENTER.%20KINDLY%20UNSUBSCRIBE%20AND%20RE-REGISTER%20AT%20https://xxx.org&org=03cc2586-0cbc-479a-a28c-25882d14226f&sig=tzKGVFwyxtfzk1KYmkZHOHWFWd4S7Bjnt-qePZ6RlmQ%3D&unsubscribe_redirect_url=https%3A%2F%2Fwww.openbugbounty.org
It is vulnerable to Content Spoofing and URL redirect and idor.

Get Divyanshu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Parameters vulnerable:
id= xxxxxx
message= xxxxxx
unsubscribe_redirect_url= https://examplexxx.com

Press enter or click to view image in full size
Content_Spoofing
POC

1) Click on the URL.
2) Add parameter &message=ALERT &unsubscribe_redirect_url=https://xxx.org
3)Click on Unsubscribe
4) It redirects to www.xxx.org

There is the possibility that this might be leveraged for phishing attacks.

Impact

Any malicious User can Unsubscribe anyone that has subscribed to emails by simply brute-forcing id parameter and it can be used to spoof the message to click on unsubscribe which will redirect to a malicious website.

Solution

Since it was a simple business logic error. So, providing id and message field and replacing with a signature so that input cannot be provided externally.

Since this issue was a third party issue as mail is under managed services and didn’t come directly under confluent but organization responsible for the issue confirmed that the issue has been remediated and the fix has been implemented.

Reference

https://hackerone.com/reports/201314
https://hackerone.com/reports/230328
https://www.bugcrowd.com/how-to-find-idor-insecure-direct-object-reference-vulnerabilities-for-large-bounty-rewards/

Timeline

06/29/2018: Discovered and reported to the confluent team
06/29/2018: Bug confirmed
08/17/2018: Bug fixed by the third party and confirmed by theconfluent team
08/30/2018: Confirmed for public disclosure
28/09/2018: Published POC

#justmorpheus
