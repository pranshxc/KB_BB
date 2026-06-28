---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-18_insecure-direct-object-reference-exposes-all-users-of-microsoft-azure-independen.md
original_filename: 2022-03-18_insecure-direct-object-reference-exposes-all-users-of-microsoft-azure-independen.md
title: Insecure Direct Object Reference Exposes all users of Microsoft Azure Independent
  Software Vendors
category: documents
detected_topics:
- idor
- access-control
- rate-limit
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- access-control
- rate-limit
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 3ca99b4072ed861057c0d248b9b923ffcf14033a75a1f2dc9b47be49e468d520
text_sha256: 6f599ff904076e50117f342d52dad0be5e24c69e2370663eef111eed4bfaeafc
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Insecure Direct Object Reference Exposes all users of Microsoft Azure Independent Software Vendors

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-18_insecure-direct-object-reference-exposes-all-users-of-microsoft-azure-independen.md
- Source Type: markdown
- Detected Topics: idor, access-control, rate-limit, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `3ca99b4072ed861057c0d248b9b923ffcf14033a75a1f2dc9b47be49e468d520`
- Text SHA256: `6f599ff904076e50117f342d52dad0be5e24c69e2370663eef111eed4bfaeafc`


## Content

---
title: "Insecure Direct Object Reference Exposes all users of Microsoft Azure Independent Software Vendors"
url: "https://mearegtu.medium.com/insecure-direct-object-reference-exposes-all-users-of-microsoft-azure-independent-software-vendors-bed3b45e509"
authors: ["Meareg"]
programs: ["Microsoft"]
bugs: ["IDOR"]
publication_date: "2022-03-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2803
scraped_via: "browseros"
---

# Insecure Direct Object Reference Exposes all users of Microsoft Azure Independent Software Vendors

Insecure Direct Object Reference Exposes all users of Microsoft Azure Independent Software Vendors
Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣
Follow
5 min read
·
Mar 19, 2022

10

1

Hi Everyone,

This is my continued responsible disclosure blog on Microsoft products. If you didn’t read my previous blog, you can get it from here.

Today, I will share how I discover IDOR vulnerability in Microsoft Partner application which exposes all Microsoft Azure Independent Software Vendors.

Introduction

What is Insecure Direct Object Reference / IDOR?

Insecure direct object reference (IDOR) is a type of access control vulnerability that arises when an application uses a user supplied input to access an objects directly without properly checking permission of a user. The application solely relies on the presence of a valid session.

Example:

Suppose, a fictional user ‘Negus’ is fetching his detail information from our vulnerable ‘mynotsecureapp.com’ application. Keep in mind his userId is 1055.

https://mynotsecureapp.com/users?userId=1055

Result: Personal identifiable information of the user retrieved from the backend database:

{
 "UserId": 1055,
 "First Name": "Negus",
 "Last Name": "Ezana",
 "DoB": "1970–01–01",
 "Place of Birth": "Bahir Dar",
 "email": "ng@mynotsecureapp.com",
 "mobile": "0918xxxxxx"
}

From the above example, userId parameter is interesting - from attacker or curious user perspective. Let’s say ‘Negus’ is a curious user & he wants to see the details of next user in sequence i.e. userId 1056.

https://mynotsecureapp.com/users?userId=1056

Result: Negus was able to disclose personal identifiable information of ‘Mahelete’.

{
 "UserId": 1056,
 "First Name": "Mahelete",
 "Last Name": "Solomon",
 "DoB": "1980–04–10",
 "Place of Birth": "Addis Ababa",
 "email": "ms@mynotsecureapp.com",
 "mobile": "0911xxxxxx"
}

Based on the above example, our curious user was able to read other users’ personal identifier information by circumventing the authorization mechanism. Hence, we can safely say the application is vulnerable to IDOR.

An attacker can exploit the above security vulnerability to extract all user detail information and use it for many nefarious purpose. In a simple term, it leads to a huge financial and reputational damage to owner of the application.

It sounds unrealistic right? Unfortunately, it is a very common security vulnerability. An attacker needs one vulnerable endpoint to exploit, while the defender needs to protect all endpoints (attacker-defender dilemma).

We covered basics of IDOR. In the next section, we will deep-dive into the main topic — exploiting IDOR in Microsoft Partner.

Exploiting IDOR in Microsoft Partner application

Microsoft provides a platform for their independent software vendors to centrally build, manage and sell their solution. Partners can use Microsoft Partner portal for managing publishers, users, commercial market place etc.

In this blog, I will share IDOR vulnerability which exposes all Microsoft Partner users.

Detection

Once registered to Microsoft Partner application you can access the Partner portal by directly browsing to its URL — https://partner.microsoft.com

Press enter or click to view image in full size

You can fetch the details of sellers under your ‘Organization Profile’. Each seller in your account identified by 8 digit ID. For example, 76xxxx10 is one of my sellerId.

Press enter or click to view image in full size
List of Sellers

Here is the underlying API request and response used to fetch publisher/seller details. Please note, the sellerId of the currently logged in user is 76????10.

Request:

GET /en-us/dashboard/account/<reduct>/<reduct>/<reduct>/<reduct>/76????10/users HTTP/2
Host: partner.microsoft.com
Press enter or click to view image in full size
Details of users belongs to publisher 76????10

Response: The application returns the details of publishers.

Close analysis reveals ‘sellerId’ parameter value seems sequential in nature. Hence, I attempt to read other customer data before and after my sellerId.

My seller id is 76????10 to disclose another user next to my sellerId is just adding 10:

Get Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

76????10 + 10 = 76????20

Request:

GET /en-us/dashboard/account/<reduct>/<reduct>/<reduct>/<reduct>/76????20/users HTTP/2
Host: partner.microsoft.com
Press enter or click to view image in full size
Details of users belongs to publisher 76????20

Response: The application discloses other customers detail without verifying users’ authorization. It is unexpected behavior or security vulnerability.

Another example of user — 76????10-10 = 76????00

Request:

GET /en-us/dashboard/account/<reduct>/<reduct>/<reduct>/<reduct>/76????00/users HTTP/2
Host: partner.microsoft.com
Press enter or click to view image in full size
Details of users belongs to publisher 76????00

The application is clearly vulnerable to IDOR. An attacker can fetch randomly any publisher’s detail.

Randomly accessing other Microsoft Partner Information

GET /en-us/dashboard/account/<reduct>/<reduct>/<reduct>/<reduct>/3?????30/users HTTP/2
Host: partner.microsoft.com
Press enter or click to view image in full size
Details of users belongs to publisher 3?????30

another example:

GET /en-us/dashboard/account/<reduct>/<reduct>/<reduct>/<reduct>/2?????50/users HTTP/2
Host: partner.microsoft.com
Press enter or click to view image in full size
Details of users belongs to publisher 2?????50

Automating the Exploit

Since the application doesn’t have rate limiting and the sellerId is sequential, the entire process can be automated to extract thousands of customers detail:

Press enter or click to view image in full size
python script to extract thousands of users

Conclusion

During security review, it was possible to fetch numerous companies publisher information including Microsoft’s different team (blockchain team, AKS Engine team etc.) and other important Microsoft Partners.

Recommendation

Implement rate-limiting (why we let a user to send thousands of request to a single endpoint within short period time?)
Utilize a randomized strings to identify objects (user, account, customer etc.)
Detect and respond anomalies in realtime
S-SDLC is a key
Security Code Review ( manual & automated)
Perform penetration testing in any product before release it to prod
Logging and monitoring

Report Timeline

Aug 21, 2021 — Reported to Microsoft
Aug 21, 2021 — Case Manager assigns a case to the defect
Sep 07, 2021 — Triage
Sep 10, 2021 — Vulnerability was fixed
Dec 10, 2021 — Writeup Request
