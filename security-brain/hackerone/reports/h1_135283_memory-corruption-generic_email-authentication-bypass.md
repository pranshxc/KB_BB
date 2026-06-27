---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135283'
original_report_id: '135283'
title: Email Authentication Bypass
weakness: Memory Corruption - Generic
team_handle: paragonie
created_at: '2016-04-29T00:49:05.985Z'
disclosed_at: '2016-05-16T17:45:47.784Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- memory-corruption-generic
---

# Email Authentication Bypass

## Metadata

- HackerOne Report ID: 135283
- Weakness: Memory Corruption - Generic
- Program: paragonie
- Disclosed At: 2016-05-16T17:45:47.784Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi,

I was able to bypass you email authentication. You have not published "DMARC [Domain-based Message Authentication, Reporting, and Conformance]" for the domain paragonie.com more information :-

http://dmarc.org/
---------------------------------------------------------------------->
what is DMARC ?

DMARC, which stands for “Domain-based Message Authentication, Reporting & Conformance”, is a technical specification created by a group of organizations that want to help reduce the potential for email-based abuse by solving a couple of long-standing operational, deployment, and reporting issues 
related to email authentication protocols.DMARC standardizes how email receivers perform
email authentication using the well-known SPF and DKIM mechanisms. This means that senders will experience consistent authentication results for their messages at AOL, Gmail, Hotmail, Yahoo! and any 
other email receiver implementing DMARC. We hope this will encourage senders to more broadly authenticate their outbound email which can make email a more reliable way to communicate.

DMARC was aimed at:

Reducing false negatives
Provide authentication reporting
Apply sender policies at the receiving end
Reduce phishing
Be scalable
In order to get started with DMARC, the sending domain needs to have an SPF and DKIM record published. Once the SPF and DKIM records are in place, you can ure DMARC by adding policies to your domain's TXT records (the same way in which you published your SPF and DKIM records). Your TXT record name should read something similar to "dmarc.your_domain.com." Please replace the "yourdomain.com" with your own domain.

As DMARC policies are published as TXT records, it defines what an email receiver should do with non-aligned mail it receives.

You can read more about creating DMARC records and their uses here:https://support.sendgrid.com/hc/en-us/articles/200182958-Everything-about-DMARC-

Why should you implement this

When I try to send a spoofed email from your domain to anyone like from

scott@paragonie.com or security@paragonie.com
to abcd@example.com`

when a domain has DMARC record then they get this

http://i.gyazo.com/59c6acf761ff010bb16aa93d19c6fc39.png

The main point here is that DMARC prevents spoofing by adding this line:
It has a from address in mailjet.com but has failed mailjet.com's required tests for authentication.

Now, thats how DMARC comes to rescue

The following site https://dmarcian.com/dmarc-inspector/paragonie.com

Give the follwong detail:
No DMARC record published.

Which shows that you are missing this security feature.

You should publish a valid DMARC record for your domain to prevent any misunderstanding and to prevent hackers from using your email.

Thank you!

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
