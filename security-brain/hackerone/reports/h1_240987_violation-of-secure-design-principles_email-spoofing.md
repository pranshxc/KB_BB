---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '240987'
original_report_id: '240987'
title: Email Spoofing
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-06-17T11:50:28.299Z'
disclosed_at: '2017-06-17T12:02:48.480Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email Spoofing

## Metadata

- HackerOne Report ID: 240987
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-06-17T12:02:48.480Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hey **Gratipay**,
It appears that spoofed email can be sent from 1 of your emails.

###The following email is vulnerable:

support@gratipay.com

###Information

>Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

###Steps to Reproduce

Go to https://emkei.cz/.
Write down support@gratipay.com or any emails stated above to From Email field.
Write down the test address(where you want to check the spoofed email) to To field.
An email will be send to your test address from support@gratipay.com.
Proof of Concept

###Screenshot 
Email from: support@gratipay.com. {F195062}

**PS:** As you can see, I used my Yahoo account as victim account and this is terrible to your clients who still using Yahoo (still a lot of them) as their email provider. It's because the email was sent directly to my inbox which is a trusted folder unlike spam so they will think that this spoofed email is legitimate.

Thank you for time and consideration you spent for reading my report.

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
