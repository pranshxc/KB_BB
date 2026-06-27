---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1874260'
original_report_id: '1874260'
title: HTML injection that may lead to XSS on HackerOne.com through H1 Triage Wizard
  Chrome Extension
weakness: Cross-site Scripting (XSS) - Stored
team_handle: security
created_at: '2023-02-14T18:53:24.813Z'
disclosed_at: '2023-02-14T20:17:48.764Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# HTML injection that may lead to XSS on HackerOne.com through H1 Triage Wizard Chrome Extension

## Metadata

- HackerOne Report ID: 1874260
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: security
- Disclosed At: 2023-02-14T20:17:48.764Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

To reproduce:

* ensure you have the H1 Triage Wizard Chrome extension enabled
* visit https://hackerone.com/reports/1622449?subject=security&/bugs=1
* right-click the report, select "View Triage Questionnaire (Beta)"
* observe an HTML payload being injected

{F2173699}

The payload is stored in █████████. The contents of this file are dynamically loaded through the Chrome extension.

The vulnerability is caused by the following code in the `triage-extension-private` repository:

```js
buildTriageQuestionnaireModal = (
  modalElement,
  triageQuestionnaireModalOptions
) => {
  let questionnaireResponses =
    triageQuestionnaireModalOptions.questionnaireResponses;
  if (questionnaireResponses) {
    modalElement.innerHTML = triageQuestionnaireHTML
      .replace("{{handle}}", triageQuestionnaireModalOptions.handle) // <-- the handle here is taken from the subject parameter (i.e. "security")
      .replace("{{1}}", questionnaireResponses[1]) // <-- the response to the questionnaire is interpolated without sanitizing it
      .replace("{{2}}", questionnaireResponses[2]) // <-- this applies to all of these
      .replace("{{3}}", questionnaireResponses[3])
// ...
```

## Impact

This vulnerability may lead to compromising confidential information or impact its integrity.

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
