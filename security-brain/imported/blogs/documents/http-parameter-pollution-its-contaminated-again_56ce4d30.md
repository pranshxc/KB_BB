---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-26_http-parameter-pollution-its-contaminated-again_2.md
original_filename: 2022-07-26_http-parameter-pollution-its-contaminated-again_2.md
title: HTTP Parameter Pollution - It’s Contaminated Again
category: documents
detected_topics:
- rate-limit
- command-injection
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- api-security
language: en
raw_sha256: 56ce4d30236842affb191eee782e97929285bf2f3bbe25db64ed86f2cf806308
text_sha256: 04e1c1a257d686cccdba8cf32d2d468d17aed8cdffc2a6ddc564d99f8a2b7cfa
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# HTTP Parameter Pollution - It’s Contaminated Again

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-26_http-parameter-pollution-its-contaminated-again_2.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `56ce4d30236842affb191eee782e97929285bf2f3bbe25db64ed86f2cf806308`
- Text SHA256: `04e1c1a257d686cccdba8cf32d2d468d17aed8cdffc2a6ddc564d99f8a2b7cfa`


## Content

---
title: "HTTP Parameter Pollution - It’s Contaminated Again"
url: "https://shahjerry33.medium.com/http-parameter-pollution-its-contaminated-again-95c75b0295e1"
authors: ["Jerry Shah (@Jerry)", "ethicalbughunter (@ethicalbughuntr)", "droppyy33"]
bugs: ["HTTP parameter pollution", "Rate limiting bypass"]
bounty: "50"
publication_date: "2022-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2393
scraped_via: "browseros"
---

# HTTP Parameter Pollution - It’s Contaminated Again

HTTP Parameter Pollution - It’s Contaminated Again
Jerry Shah (Jerry)
Follow
4 min read
·
Jul 26, 2022

496

3

Summary :

HTTP Parameter Pollution (HPP) means to pollute the HTTP parameters of a web application for achieving a specific malicious task. It refers to manipulating how a website treats parameters it receives during HTTP requests. It changes a website’s behaviour from its intended one. HTTP
parameter pollution is a simple kind of attack but it is an effective one.

When you pollute any parameter the code runs only on the server-side which is invisible to us, but we can see the results on our screen. The process in between is a black box.

The term Query String is commonly used to refer to the part between the “?” and the end of the URI as defined in the RFC 3986, it is a series of field-
value pairs. Pairs are separated by “&” or “;” and the usage of semicolon is a W3C recommendation in order to avoid escaping. RFC 2396 defines two classes of characters:

Unreserved: a-z, A-Z, 0–9 and _ . ! ~ * ‘ ( )
Reserved: ; / ? : @ & = + $ ,

Description :

We found this vulnerability on a private program on one of the bug bounty platform and it was a collaboration between me, ethicalbughuntr and droppyy33. We found this parameter pollution on invite member functionality where we were able to send multiple emails to a single user and flooding his/her inbox, just like no rate limit.

The impact and the severity of this bug is as same as no rate limit but the only difference is the attack medium. You can also consider it as a bypass to rate limits on email flooding. We reported this issue and it was triaged in low severity (P4) and we were awarded with a bounty of 50 USD.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How we found this vulnerability ?

We added the email in invite member functionality
Invite Member

2. Then we tried to add same email another time but it gave an error

Invite Member
Invite Member - Error

3. After intercepting the request we found that the parameter is an array

Press enter or click to view image in full size
Intercepted Request - Invite Member

4. So we polluted the parameter by passing the same email 3 times

Press enter or click to view image in full size
Polluting the parameter

5. Then we checked the response and it showed “success”: true. However the other parameter “failed_invitee_emails”:[“”], had the email value we passed but it was not performing the duplication check (small misconfiguration here).

Press enter or click to view image in full size
Response - Success

6. After that we checked the inbox and found that there were 3 emails

Press enter or click to view image in full size
Inbox - 3 Emails

7. Then we thought of flooding the inbox with 200 emails so we passed same email 200 times in the “invitee_emails”:[] parameter and it was successful

Press enter or click to view image in full size
Intercepted Request - Invite email
Press enter or click to view image in full size
200 Emails

8. Then again we checked the inbox and it was flooded with 200 emails

Press enter or click to view image in full size
Inbox Flooded - 200 Emails

Why it happened ?

In my opinion,

It happened because the server side check for the “invitee_emails”:[] array parameter was not being performed. However the check was performed on the client side only which was the reason for this vulnerability.

A small observation from this vulnerability was that, we came to know the size of an array of “invitee_emails”:[] parameter because in the inbox you can see that after 100 emails the remaining emails came as a new message of another 100 emails.

Press enter or click to view image in full size
Improper Validation Flow

Impact :

The impact of this vulnerability is as same as no rate limit on email flooding. The severity for this bug is low as an attacker can only flood the victim’s inbox with n number of emails.

Calculated CVSS :

Vector String - CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L

Score - 3.7 (Low)

Mitigation :

In my case the security check for the parameters should be performed on the client side as well as server side. Apart from that if the website is restricting for entering same email another time then a duplication check should be performed on the client as well as server side.

Press enter or click to view image in full size
