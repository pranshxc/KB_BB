---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92111'
original_report_id: '92111'
title: Self-XSS in mails sent by hello@owncloud.com
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2015-10-02T22:26:06.101Z'
disclosed_at: '2016-02-06T21:38:56.388Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Self-XSS in mails sent by hello@owncloud.com

## Metadata

- HackerOne Report ID: 92111
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2016-02-06T21:38:56.388Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello 
i create account with username have a payload code "><img src="c" onerror=alert(1)><script>alert(1)</script>,
and i always when i  get mail from hello@owncloud.com i get mail win inject the code payload (html code inject)
From: ownCloud <hello@owncloud.com>
Reply-To: hello@owncloud.com
To: s-dz@hotmail.fr
Message-ID: <1443803020209.163f96fc-108e-42bf-8c10-86406627607e@smtp.hubapi.com>
Subject: ownCloud Security & Encryption 2.0; A Technical Overview
MIME-Version: 1.0
Content-Type: multipart/alternative;
	boundary="----=_Part_2297473_416570165.1443803059574"
List-Unsubscribe: <mailto:MCQyw6Wdcg_W8ys71T8040lgVzv76n4tcsZ_W4fKWHX3ZskbF0@m.hsms06.com>, <http://t.hsms06.com/e1t/c/*W4Zt7h03lnvKlW7vlbtK3d_CYy0/*W48wfbt6qPs7GW8WTnbw5F30_R0/
------=_Part_2297473_416570165.1443803059574
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

Hi "><img src=3D"c" onerror=3Dalert(1)><script>alert(1)</script>,

PoC image 


Thanks 

Hadji Samir

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
