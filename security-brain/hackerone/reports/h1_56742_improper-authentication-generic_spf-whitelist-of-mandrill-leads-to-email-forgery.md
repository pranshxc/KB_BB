---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56742'
original_report_id: '56742'
title: SPF whitelist of mandrill leads to email forgery
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2015-04-16T18:15:09.759Z'
disclosed_at: '2015-06-08T00:26:08.156Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# SPF whitelist of mandrill leads to email forgery

## Metadata

- HackerOne Report ID: 56742
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2015-06-08T00:26:08.156Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I just sent a forged email to support@hackerone.com that appears to originate from mike.brooks@hackerone.com.   I was able to do this because of the following  SPF record:

dig txt hackerone.com
hackerone.com.		299	IN	TXT	"v=spf1 include:_spf.google.com include:sendgrid.net include:mail.zendesk.com include:spf.mandrillapp.com ~all"

Using my own mandrill account I can send email which appears to originate from hackerone.  This is useful in phishing,  and this type of vulnerability is news worthy (http://bits.blogs.nytimes.com/2015/04/09/sendgrid-email-breach-was-used-to-attack-coinbase-a-bitcoin-exchange/).

The patch is pretty simple.  Complete your mandril registration process.  This will lock out other mandrill users from sending email that originates from *@hackerone.com.

Let me know if you need me to send another forged email,  or if  have any other questions.

Thanks,
Mike Brooks from Bishop Fox.

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
