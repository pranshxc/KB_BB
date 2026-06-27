---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '90862'
original_report_id: '90862'
title: Passwords Returned in Later Responses.
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2015-09-29T06:12:14.989Z'
disclosed_at: '2015-09-30T16:46:10.182Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Passwords Returned in Later Responses.

## Metadata

- HackerOne Report ID: 90862
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2015-09-30T16:46:10.182Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Passwords submitted to the application are returned in clear form in later responses from the application. This behavior increases the risk that users' passwords will be captured by an attacker. Many types of vulnerability, such as weaknesses in session handling, broken access controls, and cross-site scripting, would enable an attacker to leverage this behavior to retrieve the passwords of other application users. This possibility typically exacerbates the impact of those other vulnerabilities, and in some situations can enable an attacker to quickly compromise the entire application.

Proof Of Concept:
1. Login into your online shop.
2. Add any staff member.
3. An invitation mail is send towards the person to whom you wanted to added.
4. When you click on the confirmation mail. A new link is generated who sends you to some another page.
5. Fill the complete form there.
6. Submit the Form.
7. You'll see the complete password are submitted in clear test in later responses.

PFA, the attached Video PoC for the same and the screenshot

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
