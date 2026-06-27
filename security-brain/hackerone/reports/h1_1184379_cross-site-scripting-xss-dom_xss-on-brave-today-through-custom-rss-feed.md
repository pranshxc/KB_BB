---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1184379'
original_report_id: '1184379'
title: XSS on Brave Today through custom RSS feed
weakness: Cross-site Scripting (XSS) - DOM
team_handle: brave
created_at: '2021-05-04T23:26:23.415Z'
disclosed_at: '2023-06-22T05:51:53.264Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS on Brave Today through custom RSS feed

## Metadata

- HackerOne Report ID: 1184379
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: brave
- Disclosed At: 2023-06-22T05:51:53.264Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Two months ago, the [custom RSS feed feature](https://github.com/brave/brave-ios/pull/3317) was introduced to Brave Today on Brave iOS.

This feature allows to add any RSS feed to Brave Today, and the registered feed entries are shown in a tab with a hyperlink to the original article URL.
Then, Brave iOS doesn't restrict the URL scheme of the original article link, which can cause XSS weakness through `javascript:` URL.

Here is a demonstration RSS feed of this attack.
https://csrf.jp/brave/rss.php

This RSS feed contains `javascript:alert(document.domain)` in an entry tag like this.
```
<entry>
  <title>XSS</title>
  <link rel="alternate" type="text/html" href="javascript:alert(document.domain)" />
  <content type="html"><![CDATA[<img src="https://csrf.jp/test.png">]]></content>
</entry>
```
When user taps the entry on Brave Today, an alert dialog is shown on `http://localhost:65XX`.

## Products affected: 

 * Brave iOS current Nightly build

## Steps To Reproduce:

 * Open "Settings"
 * Tap "Brave Today" in Settings menu
 * Tap "Add Source"
 * Type "https://csrf.jp/brave/rss.php" and tap "Search"
 * RSS feed, that name is PoC, is found, then tap "Add"
 * Enable PoC feed
 * Close the Settings menu and open a new tab
 * Enable Brave Today, then you can find an article entry that name is "XSS"
 * Tap the article, then an alert dialog is shown

## Supporting Material/References:

  * See attached movie file for the demonstration

## Impact

As written in summary, XSS is possible on `http://localhost:65XX`.
Note that `http://localhost:65XX` should be considered as a privileged domain that hosts Brave's internal features such as reader-view, error-pages and so on.

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
