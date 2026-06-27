---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244474'
original_report_id: '244474'
title: Mailgun misconfiguration
weakness: Privilege Escalation
team_handle: wakatime
created_at: '2017-06-29T18:32:14.993Z'
disclosed_at: '2017-07-01T21:39:45.915Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- privilege-escalation
---

# Mailgun misconfiguration

## Metadata

- HackerOne Report ID: 244474
- Weakness: Privilege Escalation
- Program: wakatime
- Disclosed At: 2017-07-01T21:39:45.915Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

During subdomain enumeration i found the following subdomain:
```
email.mailgun.wakatime.com
```
Looking at the cname records, it is pointing to mailgun.
```
host email.mailgun.wakatime.com
email.mailgun.wakatime.com is an alias for mailgun.org.
mailgun.org has address 34.225.110.231
mailgun.org has address 34.194.118.46
mailgun.org is an alias for mailgun.org.
mailgun.org has address 34.194.118.46
mailgun.org mail is handled by 10 mxb.mailgun.org.
mailgun.org mail is handled by 10 mxa.mailgun.org.
```
I went to my mailgun account and tried to claim email.mailgun.wakatime.com.
And success!

{F198701}

And i can now also create a mailing list.

{F198702}

It seems you have not added ``` email.mailgun.wakatime.com``` to your mailgun account.

Hence, it could be possible to snoop into the emails of wakatime.

I guess we need to add the dns records to verify the domain and it may take upto 48 hours for DNS changes to propagate
Hence, i have not gone further and decided to report this.

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
