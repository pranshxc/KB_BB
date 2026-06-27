---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '209821'
original_report_id: '209821'
title: URL Given leading to end users ending up in malicious sites
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-03-01T10:10:32.598Z'
disclosed_at: '2017-03-01T22:15:49.827Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# URL Given leading to end users ending up in malicious sites

## Metadata

- HackerOne Report ID: 209821
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-03-01T22:15:49.827Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

I found a design issue in the profile statement for the registered user. This is dependant on the end user however.

In the profile statement, one can write something as well giving links is allowed. This, I think is by design. However, let us suppose the authenticated user creates a website of his own which is basically a phishing page. Or he gives links to malicious websites.

Next he sends the link of his page to the victim. Try out this page.
https://gratipay.com/~www.google.com/.

Here the first link is to www.google.com. However, the next link is unknown and can be malicious.

Yes, this depends on the end user completely but I still think this is an issue.

Mitigation: Allow only alphabets or display the entire thing as text. The end user can copy paste the link in the browser if it is that relevant.

Thanks & Regards,
Dipmalya Pyne

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
