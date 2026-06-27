---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1675674'
original_report_id: '1675674'
title: 'An Attacker Can Flag Draft Job Posts And Can Disclose The Draft Job Posts
  Details [ Similar to #1581528 Resolved Report]'
weakness: Business Logic Errors
team_handle: linkedin
created_at: '2022-08-21T05:58:50.731Z'
disclosed_at: '2023-08-24T03:10:19.734Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: www.linkedin.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# An Attacker Can Flag Draft Job Posts And Can Disclose The Draft Job Posts Details [ Similar to #1581528 Resolved Report]

## Metadata

- HackerOne Report ID: 1675674
- Weakness: Business Logic Errors
- Program: linkedin
- Disclosed At: 2023-08-24T03:10:19.734Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

During the security assessment, It has been observed that the Job posts ID is numerical, while testing I came across an endpoint where a user can report the job posts of other users. The business logic error is present where an attacker can report the draft job posts of other users. After reporting the draft posts, the attacker receives a notification from LinkedIn about the reported job posts disclosing some details of the draft job posts ( which are not even published yet) .

Also, Report: #1581528 is similar, and it is resolved, but in my case, I was still able to report the draft jobs. 


##Steps:
1) Login into the account and go to job posts like ``` https://www.linkedin.com/jobs/view/██████/```.
2) Open any draft job  ``` https://www.linkedin.com/jobs/view/██████████/``` It will give the error ``` something went wrong```.
3) Report the posted job and intercept the vulnerable request.
██████████
4) Forward the job using the draft jobid- █████. The report will get submitted without any error 
███
5) After some time, the attacker receives the notification from Trust and Safety Team ( We’ve reviewed your report) . Disclosing the job details of the job posts.
█████████

## Vulnerable Request:
```
POST /lite/flag-content?contentUrn=urn:li:jobPosting:██████████&reason=SPAM_CONTENT&contentSource=JOBS_PREMIUM_OFFLINE&authorProfileId=0&trk=report-content HTTP/2
Host: www.linkedin.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Csrf-Token: ajax:███
X-Isajaxform: 1
Origin: https://www.linkedin.com
Referer: https://www.linkedin.com/jobs/search/?currentJobId=████████
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Content-Length: 0
Te: trailers
```

## Impact

An attacker can report any draft job and can access the details of the job, like : job name of the company, etc details.

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
