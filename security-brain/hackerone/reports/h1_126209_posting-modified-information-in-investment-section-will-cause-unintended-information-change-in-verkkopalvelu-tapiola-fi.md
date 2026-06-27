---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126209'
original_report_id: '126209'
title: Posting modified information in 'Investment section' will cause unintended
  information change in verkkopalvelu.tapiola.fi
team_handle: localtapiola
created_at: '2016-03-26T18:36:14.297Z'
disclosed_at: '2016-05-14T21:18:10.895Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# Posting modified information in 'Investment section' will cause unintended information change in verkkopalvelu.tapiola.fi

## Metadata

- HackerOne Report ID: 126209
- Weakness: 
- Program: localtapiola
- Disclosed At: 2016-05-14T21:18:10.895Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Some strange account information modification is ongoing when intercepting and making small modifications to requests in 'investment section'.

Login to portal and go to buy shares

https://verkkopalvelu.tapiola.fi/jb2/ltvr/purchases or similar 

and pic 2025 A shares, intercept requests and edit response from
https://verkkopalvelu.tapiola.fi/jb2/ltvr/rest/fund?fundRef=-1&fundKey=&accountKey=&accountRef=&opener=

find and edit params
***"firstName":"dipadu","lastName":"something"***

forward request. Purchase shares but do not buy / use banks payment. 

go to normal localtapiola customer portal (name is still normal?). 

(does not require this but confirms that you do have managed to purchase shares
Goto
https://verkkopalvelu.tapiola.fi/jb2/ltvr/custodialaccounts
and purchase should be visible...)

Goto https://verkkopalvelu.tapiola.fi/a2/AskoWeb/ProfileServlet?resource=asko_frontpage and your name involved to ANY previously named contacts is changed to "dipadu something". Also your username /name. ("PIC ATTACHED")

First, i do not know if you are supposed to buy shares with imagination name (i used Topi Sorsakoski with fake social security number)? It is also possible to fake social security number here.

Second, this one "buy" procedure make changes to customer portal names (in this case Topi Sorsakoski). What the ****? :) When portal user data is modified thru this request, i could test to change somebody elses account information. These forms (when buying shares) asks address and other thing which is then moved / will replace REAL account fields? By changing account ID (maybe social security number?) could damage be done to other account holders? Did not tested this one but should be taken in to account when tested in-house.

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
