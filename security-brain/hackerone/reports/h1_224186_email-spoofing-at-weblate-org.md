---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224186'
original_report_id: '224186'
title: Email spoofing at weblate.org
team_handle: weblate
created_at: '2017-04-26T23:53:23.210Z'
disclosed_at: '2017-06-16T14:13:09.528Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# Email spoofing at weblate.org

## Metadata

- HackerOne Report ID: 224186
- Weakness: 
- Program: weblate
- Disclosed At: 2017-06-16T14:13:09.528Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Good day.

I found security bug at weblate.org. Now anybody may send email from weblate.org domain.

Now you have SPF policy and DMARC policy, that does not protect anything (because exists insecure domain policy: "p=none" and "sp=none"). Anybody may send email from weblate.org (or subdomain), that are not protected (because SPF does not mean, that email service will do something with spoofed email (for example, Yahoo will add it to inbox)). 

You may use https://emkei.cz/ to test this bug. For example, I sent email from admin@weblate.org (or test@mail.weblate.org) to my email and got this message.

Why it is dangerous?

Attacker may send fake email from your domain and ask user to do somethig. For example, go to site and insert password. User may trust, because email send from normal domain.

If you try send email from Facebook main site, Google domain, you will not get message. You may use DMARC Policy (with "p=reject") to prevent sending emails form your domain.

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
