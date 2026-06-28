---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-16_broken-access-control.md
original_filename: 2021-12-16_broken-access-control.md
title: Broken Access Control
category: documents
detected_topics:
- access-control
- idor
- xss
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- idor
- xss
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 30e1cde505fcdcb0fdffa147f80efe72975821262159b87256657e025934f978
text_sha256: 735abe114ae456358a48be17ec033c8523778af2079509715d4506faafc4d876
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Access Control

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-16_broken-access-control.md
- Source Type: markdown
- Detected Topics: access-control, idor, xss, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `30e1cde505fcdcb0fdffa147f80efe72975821262159b87256657e025934f978`
- Text SHA256: `735abe114ae456358a48be17ec033c8523778af2079509715d4506faafc4d876`


## Content

---
title: "Broken Access Control"
url: "https://mearegtu.medium.com/broken-access-control-cc6cfd793b15"
authors: ["Meareg"]
programs: ["Microsoft"]
bugs: ["IDOR"]
publication_date: "2021-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3083
scraped_via: "browseros"
---

# Broken Access Control

Broken Access Control
Part 0x01 | Improper Authorization could allow access to more than 100,000 Microsoft Dynamics 365 for Partner Users
Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣
Follow
3 min read
·
Dec 16, 2021

30

Introduction

As a part of Microsoft coordinated vulnerability disclosures, I would like to share a critical vulnerability within the dynamics portal which could allow an attacker to access personally identifiable information (first name, last name, email address, MPN ID etc.) of users of the Microsoft Dynamics for 365 Partner website.

Technical Details:

Step 0x01: Login to ‘Dynamics 365 for Partners’ portal using my valid partner account:

https://dynamicspartners.xxxxx.microsoft.com/

Press enter or click to view image in full size

Step 0x02: The above application invokes different API calls in the background. Let’s closely analyze the following interesting API call, which fetches details of currently logged in user.

Request

Endpoint: /api/Users/email?emailId=maotg@???.onmicrosoft.com
Host: landingapi-prod.azurewebsites.net
Authorization: Bearer eyJ....

The ‘emailId’ parameter by default takes currently logged in user email address:

Press enter or click to view image in full size

Response

The application returns first & last name, email address, MPNID, AAD Profile ID, role name etc. of currently logged in user.

Step 0x03: [Vulnerability/Unexpected behavior] One important test case here trying to access other users on the dynamics portal system details using their email address.

The following is unauthorized reading of other users of the system information by using their email address. The application discloses the details of the user without checking for an additional authorization on the API call. For this example, I use email address of my second testing account.

Get Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Request

Endpoint: /api/Users/email?emailId=moxxx@???.onmicrosoft.com
Host: landingapi-prod.azurewebsites.net
Authorization: Bearer eyJ....
Press enter or click to view image in full size

Response

The application discloses first & last name, email address, MPNID, AAD Profile ID, role name etc. of another application user without authorization. However, in order to exploit this vulnerability, the attacker should know in advanced the email address of other site user of the dynamics portal.

Step 0x04: The following a way to disclose all user data (~112MB) without secondary authorization.

For this test case instead of /api/Users/email?emailId=<email address> I directly invoke the API to /api/Users:

Request

Endpoint: /api/Users
Host: landingapi-prod.azurewebsites.net
Authorization: Bearer eyJ....
Press enter or click to view image in full size

Response:

112 megabytes of website users’ detail which is likely over 100,000 users.

Disclaimer

The following blog is for informational and educational purpose only. I am not responsible for the misuse of the information in this blog.

Timeline:

Aug 04, 2021 — Reported to Microsoft

Aug 05, 2021 — Case Manger assigns a case to the defect

Aug 12, 2021 — A fix was completed and communicated to the finder.

Sept 27, 2021 — Finder notification of intent to go public.

Dec 16, 2021 — Approval for write-up

Final Note:

I would like to thank MSRC team who assist and help me throughout this responsible vulnerability disclosure process. Special thanks to Jim & Kriti.
