---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1444675'
original_report_id: '1444675'
title: Host Header Injection leads to Open Redirect and Content Spoofing or Text Injection.
team_handle: omise
created_at: '2022-01-09T21:01:03.658Z'
disclosed_at: '2022-04-09T06:45:59.233Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: dashboard.omise.co
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Host Header Injection leads to Open Redirect and Content Spoofing or Text Injection.

## Metadata

- HackerOne Report ID: 1444675
- Weakness: 
- Program: omise
- Disclosed At: 2022-04-09T06:45:59.233Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

1.) Open Redirection
The https://dashboard.omise.co/test/dashboard website is vulnerable to an Open Redirection flaw if the server receives a crafted X-Forwarded-Host header.

Description:
Open Redirect is a vulnerability in which the attacker manipulates a web page to redirect the users to unknown destinations (malicious/phishing destinations in most cases).

Steps To Reproduce:

1. Visit https://dashboard.omise.co/signin and sign in with your credentials and make sure you have not verified your email.
2. Once you log in, you will be on this page --  https://dashboard.omise.co/test/dashboard , send the request to Repeater and add X-Forwarded-Host: bing.com below Host: dashboard.omise.co
3. Open the request in the browser and click on "here" inside --> Please check your mailbox (***********@gmail.com) to confirm your email address.
If you did not get an email from us, please click here to request another email.
4. It will redirect to a malicious page.

POC:
Attached Video.

  2.)  Content Spoofing or Text Injection.
The https://dashboard.omise.co/test/settings website is vulnerable to a Content Spoofing or Text Injection flaw if the server receives a crafted X-Forwarded-Host header.
Description:
Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

Steps To Reproduce:

1. Visit https://dashboard.omise.co/signin and sign in with your credentials and make sure you have not verified your email.
2. Once you log in, go to Settings  https://dashboard.omise.co/test/settings , send the request to Repeater and add X-Forwarded-Host: bing.com below Host: dashboard.omise.co
3. Open the request in the browser and in the Settings option under Chains mark Enable account chaining CheckBox.
4. Once you mark the check box it will show the URL, copy that URL and paste it in the browser.
5. It will redirect.

POC:
Attached Video.

## Impact

Open Redirection Impact - 
An attacker can redirect users to malicious websites, which can lead to phishing attacks.

Content Spoofing or Text Injection Impact - 
An attacker can create a valid webpage with malicious recommendations and the user believes the recommendation as it was from the stock website.

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
