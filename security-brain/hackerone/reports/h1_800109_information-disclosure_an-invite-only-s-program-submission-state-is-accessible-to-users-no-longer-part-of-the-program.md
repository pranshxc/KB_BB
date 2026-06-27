---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '800109'
original_report_id: '800109'
title: An invite-only's program submission state is accessible to users no longer
  part of the program
weakness: Information Disclosure
team_handle: security
created_at: '2020-02-19T22:56:57.036Z'
disclosed_at: '2020-04-21T23:15:04.850Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 186
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# An invite-only's program submission state is accessible to users no longer part of the program

## Metadata

- HackerOne Report ID: 800109
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2020-04-21T23:15:04.850Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

####Related This Report: #645299

###Steps To Reproduce:

####██████ Private Program:

1. I was invited by █████: `https://hackerone.com/███`
2. Submitted a report/vulnerabilty. `https://hackerone.com/reports/519502`
3. Accepted by ████ and mark as resolved.
4. Try to leave the program.
5. The █████████ Program is not accessible anymore.
5. Back to your previous report and capture the request:

####REQUEST:

          GET /reports/519502.json HTTP/1.1
          Host: hackerone.com
          User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
          Accept: application/json, text/javascript, */*; q=0.01
          Accept-Language: en-US,en;q=0.5
          Accept-Encoding: gzip, deflate
          Referer: https://hackerone.com/reports/519502
          X-Requested-With: XMLHttpRequest
          Cookie: __cfduid=████████; _cfuid=█████; _ga=█████████; _mkto_trk=███████; _biz_uid=███████; _biz_nA=14; _biz_pendingA=%5B%5D; _biz_flagsA=████████; __Host-session=█████████████; _gid=GA1.2.1121101145.1582021374
          Connection: close
          Cache-Control: max-age=0

####RESPONSE:

          "team":{"id":██████,"url":"https://hackerone.com/███","handle":"██████████","profile_picture_urls":{"small":"█████████","medium":"████},"permissions":[],"submission_state":"open"

#####The `submission_state:open` which means the submission still open even the █████ not accessible anymore.



####█████ Private Program:

1. I was invited by ██████: `https://hackerone.com/█████████`
2. Submitted a report/vulnerabilty. `https://hackerone.com/reports/668433`
3. Accepted by ███ and mark as resolved.
4. Try to leave the program. After I leave the program the program still accepting the report ans the submission still open.
5. The █████████ Program is not accessible anymore.
6. Few months later, Back to your previous report and capture the request:

####REQUEST:

          GET /reports/668433.json HTTP/1.1
          Host: hackerone.com
          User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
          Accept: application/json, text/javascript, */*; q=0.01
          Accept-Language: en-US,en;q=0.5
          Accept-Encoding: gzip, deflate
          Referer: https://hackerone.com/reports/668433
    ███████
          X-Requested-With: XMLHttpRequest
    ██████████
          Connection: close

####RESPONSE:

          "team":{"id":████████,"url":"https://hackerone.com/███████","handle":"███","profile_picture_urls":███,"permissions":[],"submission_state":"disabled",

#####The `submission_state:disabled` which means the submission was disable even the ██████████ not accessible anymore.

## Impact

The user can define whether the submission still `OPEN` or `DISABLE` on Private Programs after leaving which not accessible anymore.

Regards,

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
