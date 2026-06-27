---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1198439'
original_report_id: '1198439'
title: No Valid SPF Records/don't have DMARC record
weakness: Improper Access Control - Generic
team_handle: upchieve
created_at: '2021-05-15T17:09:25.104Z'
disclosed_at: '2021-05-18T18:49:59.228Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: app.upchieve.org
asset_type: URL
max_severity: none
tags:
- hackerone
- improper-access-control-generic
---

# No Valid SPF Records/don't have DMARC record

## Metadata

- HackerOne Report ID: 1198439
- Weakness: Improper Access Control - Generic
- Program: upchieve
- Disclosed At: 2021-05-18T18:49:59.228Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have already reported this isssue through email and the company has accepted my report.
Hiii,
There is any issue No valid SPF Records on 
https://app.upchieve.org
Desciprition :
There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.
I found :
SPF record lookup and validation for: https://app.upchieve.org
SPF records are published in DNS as TXT records.
The TXT records found for your domain are:
No valid SPF record found.
Use the back button on your browser to return to the SPF checking tool without clearing the form.
Remediation :
Replace ~all with -all to prevent fake email.
ss attched with this
you can check this using https://www.kitterman.com/spf/validate.html
if you had a valid spf record then you don't have DMARC record due to which any one can send the mail on behalf of comapny which cause same issues of damaging comapny reputation can be used to get user data.
for checking this visit : https://dmarcian.com/spf-survey/
and type your url and you'll find all the details i
i send you the screen shot as a proof of both the above.

## Impact

An attacker would send a Fake email. can also use to get user credential after send a psihing link through mail.The results can be more dangerous.

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
