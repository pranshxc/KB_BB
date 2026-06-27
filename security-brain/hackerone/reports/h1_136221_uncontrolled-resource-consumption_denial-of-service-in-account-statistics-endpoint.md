---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '136221'
original_report_id: '136221'
title: Denial of service in account statistics endpoint
weakness: Uncontrolled Resource Consumption
team_handle: mapbox
created_at: '2016-05-04T14:35:14.691Z'
disclosed_at: '2016-05-31T21:32:00.979Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of service in account statistics endpoint

## Metadata

- HackerOne Report ID: 136221
- Weakness: Uncontrolled Resource Consumption
- Program: mapbox
- Disclosed At: 2016-05-31T21:32:00.979Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Mapbox,
I know that your guidelines explicitly say that Denial of Service coinditions are not in scope and should not be attempted, but I maintained the testing between adequate parameters so as to not to create excessive load on your backend. I also sent an email to security@mapbox.com prior to submitting this report and Alex Ulsh and he or she (Sorry, can't know which since Alex is a unisex name hahaha) told me that this could be an exception.

The vulnerability relies on the https://www.mapbox.com/core/statistics/v1/apokh11/account endpoint, it seems that by modifying the "period" parameter to an arbitrary value, the amount of data returned increases probably without any limit, furthermore, if the interval is set to "hour" instead of "day", it is possible to increase the amount of data returned even further. To avoid affecting the availability of the server, I limited my testing to a small period, which still returned around 350 kb of data.

The amount of data can also be increased if the end date of the period requested is set to a point in the future.

To reproduce:
1) Create an account or login to an existing account.
2) Access this URL: https://www.mapbox.com/core/statistics/v1/apokh11/account?interval=day&period=1461766083142%2C1462370883143&metrics=countries%2Cbrowsers%2Chosts%2Cmaps%2Cversion&services=mapview%2Ctile%2Cstatic%2Cgeocode%2Cpermanentgeocode%2Cdirections%2Csurface&_=1462370883155
3) Observe that the amount of data returned is around 2.5 Kb.
4) Modify the "interval" parameter to "hour" and the "Period" parameter to, for example "1451766083142,1462370883143" 
5) Observe that the amount of data returned increased to 372 Kb. 

Not tested: If the period is long enough, the amount of time taken to answer the request will probably be increased as well.

Implication: A malicious individual could leverage this feature by asking for extended periods to cause high loads on the backend, which in turn could affect the availiability of the service.

Recommendation: Limit the period length to an amount established by the business logic, so as to mitigate the possibility of using this functionality with malicious intent.

Let me know if you require any additional tests and/or information.
Kind Regards,
Apok.

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
