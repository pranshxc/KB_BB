---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6547'
original_report_id: '6547'
title: (lack of) smtp transport layer security
weakness: Cryptographic Issues - Generic
team_handle: security
created_at: '2014-04-08T17:09:55.612Z'
disclosed_at: '2015-05-05T21:29:27.366Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# (lack of) smtp transport layer security

## Metadata

- HackerOne Report ID: 6547
- Weakness: Cryptographic Issues - Generic
- Program: security
- Disclosed At: 2015-05-05T21:29:27.366Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

It appears that email messages from the platform are sent via plain SMTP even though the receiving MX supports ESMTPS (the use of ESMTP when STARTTLS is also successfully negotiated to provide a strong transport encryption layer).

This allows for eavesdropping along the path between the originating system (such as o1.email.hackerone.com) and the receiving MX.

To reproduce:
- Have the platform deliver a message to a recipient whose MX supports STARTTLS
- Inspect the email headers, in most cases the first 'Received:' header is relevant
- Observe the transaction id and look for 'SMTP id' (versus 'ESMTPS id')
- Observe lack of version/cipher/bits information that would be shown if TLS was used


Fictional example headers provided below;

- current
Received: from o1.email.hackerone.com (o1.email.hackerone.com. [167.89.13.71])
        by mx.receiving.tld with SMTP id e3si1568039obp.178.2014.04.08.05.59.10
        for <recipient@domain.tld>;
        Tue, 08 Apr 2014 05:59:11 -0700 (PDT)

- suggested
Received: from o1.email.hackerone.com (o1.email.hackerone.com. [167.89.13.71])
        by mx.receiving.tld with ESMTPS id e3si1568039obp.178.2014.04.08.05.59.10
        for <recipient@domain.tld>
        (version=TLSv1 cipher=ECDHE-RSA-RC4-SHA bits=128/128);
        Tue, 08 Apr 2014 05:59:11 -0700 (PDT)

The perhaps slightly obvious fix seems to be to support ESMTPS by allowing STARTTLS to be negotiated by the sending system(s). Note that blunt enforcement will cause delivery problems as it depends on EMSTPS being supported on (any) receiving MX.

HTH.

-leander

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
