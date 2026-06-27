---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1186926'
original_report_id: '1186926'
title: Flaws In Social media Icon on error page which can lead to financial loss to
  a company.
weakness: Business Logic Errors
team_handle: sifchain
created_at: '2021-05-06T17:23:33.337Z'
disclosed_at: '2021-06-12T16:55:52.214Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Flaws In Social media Icon on error page which can lead to financial loss to a company.

## Metadata

- HackerOne Report ID: 1186926
- Weakness: Business Logic Errors
- Program: sifchain
- Disclosed At: 2021-06-12T16:55:52.214Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Here, i found an issue on sifchain.finance that will direct impact to the customer of sifchain company which can be great loss in business as well as there will be problem regarding to communication with the genuine customer of a company. 
I know that sifchain.finance is not in scope but i saw this report : https://hackerone.com/reports/1147449 and reproting this issue.

During my testing on sifchain.finance i found an issues which make a genuine customer difficult to find a way to communicate with the team member of sifchain.finance through social media.

Lets directly go to reproduction step of issue: 
1) Navigate to sifchain.finance 
2) We can see at the bottom there are 4 social media icon with their valid link.
3) Here if a genuine user get a 404 not found page accidentally. For example : https://sifchain.finance/templates/rhuk_milkyway/ in this error page at the bottom we can see 6 different icon with their prospective link but all the icon does not work for which they are mean to be.
A user can accidentally or an due to different circumstance can reach to a 404 not found page and want to contact with team , but due to mis-configuration o of a social media link user will unable to contact which can be a loss to a company.
I found that an error page contain a social media button which is not working. This kind of error can be a loss of customer as well as loss in business of a company.

## Impact

This issue can directly impact on the business of a company and can create a sufficient loss to a company. 


Thank you sifchain.finance team,
Keep secure.

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
