---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152416'
original_report_id: '152416'
title: Lazy Load stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2016-07-20T05:14:23.703Z'
disclosed_at: '2017-12-01T13:34:44.899Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Lazy Load stored XSS

## Metadata

- HackerOne Report ID: 152416
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2017-12-01T13:34:44.899Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I noticed a problem with the Lazy Load WordPress plugin. It could be exploited by a lower-level user to gain administrator-level access or server compromise.

I've discussed this by email with Mohammad Jangda who confirmed the issue.

According to my tests, this kind of post content leads to JavaScript execution:
~~~~ html
<img src="/foo onerror=alert(/xss/) // " />
~~~~

The problem seems to be this regular expression:
~~~~ php
               // This is a pretty simple regex, but it works
                $content = preg_replace( '#<img([^>]+?)src=[\'"]?([^\'"\s>]+)[\'"]?([^>]*)>#', sprintf( '<img${1}src="%s" data-lazy-src="${2}"${3}><noscript><img${1}src="${2}"${3}></noscript>', $placeholder_image ), $content );
~~~~

It doesn't work as intended if there are spaces or mixed single and double quotes inside the image tag. A maliciously formed src attribute can be used to inject any other HTML attributes, like onerror.

Why this is a problem: normally users without the administrator privilege can't embed JavaScript in posts/pages. A malicious user can inject JS which, when the post is viewed by an administrator, executes administrative functions such as changing passwords, adding users, or editing plugin PHP.

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
