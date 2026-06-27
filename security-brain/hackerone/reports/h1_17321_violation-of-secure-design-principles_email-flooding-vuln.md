---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17321'
original_report_id: '17321'
title: Email Flooding Vuln
weakness: Violation of Secure Design Principles
team_handle: uzbey
created_at: '2014-06-23T12:13:53.842Z'
disclosed_at: '2014-08-07T18:44:30.503Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email Flooding Vuln

## Metadata

- HackerOne Report ID: 17321
- Weakness: Violation of Secure Design Principles
- Program: uzbey
- Disclosed At: 2014-08-07T18:44:30.503Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Your contact us form has no captcha implementation. NOW THIS IS NOT DOS VULNERABILITY. it is called as logical flaw in your website.

By using your contact us form I can flood anyone's email id on the planet.

Because once contact us form has been filled your application gives back reply to the email id given to the server. Ideally it should not be happen else anyone in the world can give my email id with 1000 request and I will be flooded by your server 1000 times.

That is why either you should stop giving message to client that "WE HAVE RECEIVED YOUR REQUEST AND REQ NO IS 'XYZ' OUR REVIEW TEAM " or you should implement captcha system on your form..

There is a huge difference in DOS issue and this issue.
IN dos issue I try to send so many req so its upto your server that to respond me or not.
In this issue I use your server to flood someone...that is why it has higher impact. and I am reporting this.

Detailed Video is attached here IN LINK...Kindly see. Its nt DOS vuln..its called logical flaw .email flooding.

VIDEO TUTORIAL LINK - DONWLOAD AND SEE FOR HIGH QUALITY OR SEE ONLINE WITH LESS QUALITY. - https://www.dropbox.com/s/3f5vdn1q6xxza66/Email%20flooding%20UZbey.mp4?m=

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
