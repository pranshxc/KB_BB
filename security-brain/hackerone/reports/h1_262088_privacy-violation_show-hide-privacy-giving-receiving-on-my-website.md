---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '262088'
original_report_id: '262088'
title: Show hide privacy giving receiving on my website
weakness: Privacy Violation
team_handle: gratipay
created_at: '2017-08-21T22:49:34.266Z'
disclosed_at: '2017-09-09T17:23:33.680Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: https://gratipay.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Show hide privacy giving receiving on my website

## Metadata

- HackerOne Report ID: 262088
- Weakness: Privacy Violation
- Program: gratipay
- Disclosed At: 2017-09-09T17:23:33.680Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team ..
I found show hide privacy settings on website ... nobody can see  on my profile but i put code on my website anybode can see my total giving .. 

Step reprodence ..

1- go to https://gratipay.com/~demo/settings/ click turn on (  hide total to giving other) and (hide my self from search result ) this way nobody can see my profile it .
2- go to https://gratipay.com/~demo/widgets/
3- copy code to your website then preview your test site look show all your privacy before now you hide it

* GIVING & TAKING WIDGETS

Use this code to add a Gratipay "receiving" widget on your website:

<script data-gratipay-username="demo"
        src="//grtp.co/v1.js"></script>

Or, if you'd like to include a "giving" widget, you can add the

data-gratipay-widget="giving"
attribute:
<script data-gratipay-username="demo"
        data-gratipay-widget="giving"
        src="//grtp.co/v1.js"></script>


##Poc
 Screenshot

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
