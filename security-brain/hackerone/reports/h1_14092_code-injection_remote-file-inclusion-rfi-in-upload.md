---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14092'
original_report_id: '14092'
title: Remote file Inclusion - RFI in upload
weakness: Code Injection
team_handle: slack
created_at: '2014-05-30T08:20:37.757Z'
disclosed_at: '2014-07-08T10:00:25.403Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- code-injection
---

# Remote file Inclusion - RFI in upload

## Metadata

- HackerOne Report ID: 14092
- Weakness: Code Injection
- Program: slack
- Disclosed At: 2014-07-08T10:00:25.403Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,

Everysite has a RFI vulnerability.
Everysite i.e *.slack.com is having this vulnerability.

Proof of concept / Steps to Reproduce :
=================================

1. Sign in to your account on slack eg. I signed in https://pran3hiva.slack.com
2. Now, go to 'Change photo'. i.e https://pran3hiva.slack.com/account/photo
3. Now, select file to upload.
4. Click on upload image.
5. You will be redirected to 'Crop Photo'.
6. Note the url 
eg.
https://pran3hiva.slack.com/account/photo?url=https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fslack-files2%2Favatar-temp%2F2014-05-30%2F2364428212.jpg

Note the 'url' parameter.

7. Change it to desired.
8. I changed it to --> https://pran3hiva.slack.com/account/photo?url=https://www.google.co.in/images/srpr/logo11w.png

Now, image from site will be loaded.

Hence, RFI :D
I have attached 2 screen-shots. POC.
Hope, you patch this one. :)

If you have any questions you may ask me.

Thank You,
Pranav

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
