---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '188972'
original_report_id: '188972'
title: Persistent XSS in www.starbucks.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2016-12-06T23:19:45.660Z'
disclosed_at: '2017-01-17T21:57:52.926Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Persistent XSS in www.starbucks.com

## Metadata

- HackerOne Report ID: 188972
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2017-01-17T21:57:52.926Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is a persistent XSS in 

```
https://www.starbucks.com/coffee/espresso/latte-macchiato
```

It is caused by loading scripts from: 

```
//starbucksmacchiato-prod.elasticbeanstalk.com/scripts/bn-v1.0.0-Release-min.js
```

Note that ```starbucksmacchiato-prod.elasticbeanstalk.com``` is not registered on elastic beanstalk. You can verify this by looking up the IP address for this subdomain and noting that it does not resolve. Through registering that domain on elastic beanstalk and deploying a webserver that responds to that request with javascript, an attacker could get a persistent XSS on Starbuck's website. 

I have not registered that domain with Elastic Beanstalk since it would give me a large amount of information about the user's of Starbuck's website (and it would incur a large amount of traffic-more than I'd like to pay for on AWS!). If you would like me to do so, let me know but I do not want to go past the bounds of acceptable testing. 

Thanks,
David Dworken

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
