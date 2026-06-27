---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1939272'
original_report_id: '1939272'
title: AEM misconfiguration leads to Information disclosure
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2023-04-08T02:40:16.993Z'
disclosed_at: '2023-05-15T15:05:48.523Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# AEM misconfiguration leads to Information disclosure

## Metadata

- HackerOne Report ID: 1939272
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2023-05-15T15:05:48.523Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I was able to access sensitive information by appending `/.1.json` to certain URLs on ████Specifically, by visiting the following URL, I was able to obtain a JSON response that contained all the templates and files present in the web root due to AEM misconfiguration:

█████████
██████████

 We can see it disclose system username and templates used by the system. This presents a serious security risk, as an attacker could use this information to gain access to sensitive files or directories that should not be publicly available.

## Impact

* Loss of confidentiality: The disclosure of internal username and webroot directories can result in a loss of confidentiality of sensitive information. This can lead to unauthorized access, manipulation, or exploitation of the disclosed information.

* Social engineering attacks: Internal username can be used in social engineering attacks such as phishing, spear-phishing, or pretexting. Attackers can use this information to craft targeted emails or other communications that appear to come from a trusted source and attempt to deceive the recipient into divulging sensitive information or clicking on malicious links.

* Reputation damage: The disclosure of sensitive information can damage an organization's reputation and erode trust among customers, partners, and stakeholders.

https://www.linkedin.com/feed/update/urn:li:activity:7049404669814530048/

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Visit : ███, █████

## Suggested Mitigation/Remediation Actions
https://www.linkedin.com/feed/update/urn:li:activity:7049404669814530048/

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
