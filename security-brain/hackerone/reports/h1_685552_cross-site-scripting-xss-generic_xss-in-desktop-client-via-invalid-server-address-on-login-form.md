---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '685552'
original_report_id: '685552'
title: XSS in desktop client via invalid server address on login form
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2019-08-31T15:16:17.398Z'
disclosed_at: '2020-08-17T00:50:32.231Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in desktop client via invalid server address on login form

## Metadata

- HackerOne Report ID: 685552
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2020-08-17T00:50:32.231Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Team!

I have found this vulnerability that in my time would be called "cross zone" but at the moment I don't know.

The problem is found in the latest version of "nextcloud.exe" for your windows version.

The problem occurs with the initial screen where you ask to connect to a website.

Apparently when you put an invalid URI that generates some type of response code like 403, it is reported in a small window, as if it were an alert box, not in the main.

This "alert box" visualizes the response and to my impression (that's why I said the cross zone) has a little more permissions than the internet explorer.

For example, if the response code has an <S> test</S> it will interpret it as IE does.

That's fine, it would only be an html injection.

The problem, for example, is that it allows you to run a file like the calculator locally without any confirmation.

This vector works : <A HREF="file:///C:/WINDOWS/system32/calc.exe">CALC.EXE</A>

In my opinion, response code errors are a problem and must be controlled by the application.

For the demonstration use the burp.

But basically any personal site where the response code building could be controlled could exploit it.

I attach a video to make everything clearer.

## Impact

The impact is that you can run local files without authorization (of the application) in a context where you should warn.

It should be filtered so as not to disturb that it is a vector.

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
