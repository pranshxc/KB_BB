---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '311449'
original_report_id: '311449'
title: Reputation gain split by company can be used to track the existence of otherwise
  undisclosed reports
weakness: Information Disclosure
team_handle: security
created_at: '2018-02-01T18:19:55.254Z'
disclosed_at: '2018-02-02T17:15:04.459Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Reputation gain split by company can be used to track the existence of otherwise undisclosed reports

## Metadata

- HackerOne Report ID: 311449
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-02-02T17:15:04.459Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

**Summary:**
A researcher who shares an anonymised description of a vulnerability prior to disclosure may inadvertently be also sharing the company to whom the issue affects if a bounty/thanks has been issued.

You may ask: "Where would someone get the idea to share partial information about unfixed bugs?" Well... F259492

**Description:**
Prior to public disclosure of a vulnerability, and also prior to a resolution status, it is possible to determine information about who a particular researcher has reported issues to if a bounty/thanks has been issued.

For example, a researcher after receiving the bounty email may tweet something like: "I just got $xxxx for reporting SQLi on HackerOne!". Unbeknownst to them it is currently possible to translate this into: "I just got $xxxx for reporting SQLi *in MegaCorp* on HackerOne!", a motivated individual simply need look at a certain area in the researcher's public profile.

### Steps To Reproduce
For example,
1.  I have reported an issue Ubiquiti Networks
2. They have not yet fixed the issue, however they have awarded a bounty
3. On my main profile page this is not listed as disclosable activity F259487
4. On the thanks page for Ubiquiti Networks I am not listed F259488, F259489
5. However, on the thanks page on my profile Ubiquiti Networks **is** listed F259491
I reported three issues to them (note even though it says the total is two, the existence of a valid third can be implied by the reputation column – since no reputation would be gained for an invalid report). If a motivated individual tracked these statistics they could infer the same kind of information by looking at diffs, say at regular site crawl intervals.

---

Proposed mitigation: only update the publicly visible reputation gain split by company when a report has been resolved/closed (similar to when things are announced on the "Hacktivity" tab today).

## Impact

Prior to public disclosure of a vulnerability, and also prior to a resolution status, it is possible to determine information about who a particular researcher has reported issues to if a bounty/thanks has been issued that generates a reputation gain.
This may be used, in addition to anonymised information that the researcher may have been encouraged to share (by yourselves), in order to gain a head start on discovering the vector before a fix has been issued.

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
