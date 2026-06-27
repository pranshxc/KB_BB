---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '186462'
original_report_id: '186462'
title: Stored XSS at 'Buy Button' page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-11-29T17:36:55.002Z'
disclosed_at: '2016-12-16T21:53:28.784Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS at 'Buy Button' page

## Metadata

- HackerOne Report ID: 186462
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-12-16T21:53:28.784Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello guys, would like to mention, first thing that I did when I have faced with Stored XSS at this page - I checked 'Known issues or previously reported vulnerabilities' section in order to ensure that issue is not out-of-scope, but didn't find this place in a list.

**_Description:_**
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted web sites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

**_Vulnerable place:_**
'Buy Button' page - Title name (div[@class='cart-permalink__preview-variant-title')

**_Payload:_**
"><img src=x onerror=alert(1)>

**_Steps to reproduce:_**
- Create a new product with [Buy button = ON] visibility;
- Fill out all required fields;
- Add new 'Variants';
- Put [payload] into Option name / value;
- Add another option;
- Leave defined name, and put 2 different options into value field (e.g. 1,2);
- Save all changes;
- Navigate to 'Buy Button' page -> 'Embed a product in email' Select product;
- Select just created product, 'Create an email Buy Button' page is opened with 'SELECT VARIANT' section where you can find 2 variant of a product.
- Switch between them - XSS triggered

**_PoC:_**
{F138287}

**_Impact:_**
Attackers can execute scripts in a victim’s browser to hijack user sessions, deface web sites, insert hostile content, redirect users, hijack the user’s browser using malware, etc.

**_Mitigation:_**
Developers should implement robust input validation and output encoding consistently across the application to defend against XSS and other input validation attacks. All of this input \ output mechanism recommended to implement: encoding \ escaping \ ‘black list’ \ filtering all special characters, e.g.: <, >, ‘, “, etc

**_Reference:_**
More you can read here.
https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29

Thanks,
Stas

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
