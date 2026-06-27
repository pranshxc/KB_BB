---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2213366'
original_report_id: '2213366'
title: captcha bypass leads to register multiple user with one valid captcha
weakness: Business Logic Errors
team_handle: tennessee-valley-authority
created_at: '2023-10-17T17:08:07.272Z'
disclosed_at: '2023-11-30T15:45:56.295Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 43
asset_identifier: '*.tva.gov'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# captcha bypass leads to register multiple user with one valid captcha

## Metadata

- HackerOne Report ID: 2213366
- Weakness: Business Logic Errors
- Program: tennessee-valley-authority
- Disclosed At: 2023-11-30T15:45:56.295Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hi team,
when we register in valley connect, captcha now expire and we can use single valid captcha for register and call to many user.

## Steps To Reproduce:
1. go to login form : https://valleyconnect.tva.gov/registration
2. complete form and click on submit registration, then intercept request with burp
3. use intruder for call multiple request, we should replace email in every request.

```
POST /registration HTTP/2
Host: valleyconnect.tva.gov

UserName=admin&Password=jgn%25%5EThgf%23rfvHRESdy56tef&ConfirmPassword=jgn%25%5EThgf%23rfvHRESdy56tef&EmailAddress=E%40jetamooz.com&EmailAddressVerify=E%40jetamooz.com&FirstName=alex&LastName=jane&Initials=&Suffix=&JobTitle=it&OrganizationType=Business+Partner&OrganizationName=sarv&Country=792&StreetAddress=sary&City=katy&Province=titi&State=AL&ZipCode=&PhoneNumber=%28934%29+734-4364&MobilePhoneNumber=%28957%29+363-4655&TimeZone=America%2FLos_Angeles&CapAnswer=U4YIQ&CapKey=XXTxVOUWZrCz6buVtsgF2cFaPHLSCKVSRQc4z4My13Bee8JiTYVZXmiPd8zLSbMc&BeCheck=
```


## Supporting Material/References:

{F2781078}
{F2781077}
{F2781085}
{F2781080}

## Impact

we can bypass captcha and register too many user with one valid captcha

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
