---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151149'
original_report_id: '151149'
title: Manipulating joinolx.com Job Vacancy alert subscription emails (HTML Injection
  / Script Injection)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-13T16:28:28.784Z'
disclosed_at: '2016-08-15T08:56:08.042Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Manipulating joinolx.com Job Vacancy alert subscription emails (HTML Injection / Script Injection)

## Metadata

- HackerOne Report ID: 151149
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-08-15T08:56:08.042Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
Another report here.

**Description**
I found that www.joinolx.com has an option to do subscription for vacancy alert. So I took a look at that.
I was able to include my HTML codes to manipulate emails sent to my address.
The *Name* field in the subscription form doesn't validate the name to strip html tags.

**Steps to Reproduce**
1. Go to any job link ( *eg. http://www.joinolx.com/careers/job/166318* )
2. Now from the left side Click on *Subscribe to our job alert*
3. In the Name field enter `<h1><font color="red">Subscription service Hacked by Zawad</font></h1>`
4. Enter your email, select random country and job position and click *Send*
Check your email and you will see the manipulated email.

**Risk**
An attacker can deliberately send malicious email from this service to make victim believe it was actually sent by OLX (and when it comes to Job service everyone would believe everything LOL)

The fix can be pretty simple to remove the tags or disallowing the html tags in the Name field. (it is never expected that a Name field will contain HTML tags).

Hope you resolve and reward.

Thanks.

-----
Zawad

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
