---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38232'
original_report_id: '38232'
title: Breaking Bugs as team member
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2014-12-04T17:18:07.896Z'
disclosed_at: '2014-12-09T19:03:12.619Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Breaking Bugs as team member

## Metadata

- HackerOne Report ID: 38232
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2014-12-09T19:03:12.619Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It is possible to break a bug page (front-end) as a team member. This is how it's done:

1. Go to a bug.
2. Select "Change State" -> "Triaged".
3. Enter a random comment.
4. Intercept the `POST` request, change `"message"` to `"message[]"`.

The status change will be saved but the `message` will be `null` (and not `""`). This breaks the front-end JavaScript causing the bug page to 'crash' for every participant. In some occasions this broke the entire Bugs page for me.

```
[Error] TypeError: null is not an object (evaluating 'this.props.raw_message.length')
	(anonymous function) (application-60308a88d636b65f18a684a058b87853.js, line 16)
[Error] TypeError: null is not an object (evaluating 'this.props.raw_message.length')
	perform (application-60308a88d636b65f18a684a058b87853.js, line 14)
	batchedUpdates (application-60308a88d636b65f18a684a058b87853.js, line 12)
	s (application-60308a88d636b65f18a684a058b87853.js, line 13)
	forceUpdate (application-60308a88d636b65f18a684a058b87853.js, line 11)
	(anonymous function) (application-60308a88d636b65f18a684a058b87853.js, line 14)
	c (application-60308a88d636b65f18a684a058b87853.js, line 4)
```

There is some weird behaviour. In Safari it always fails to load the page, but in Chrome it sometimes works for some reason. Using the steps above, with Safari, you should be able to reproduce the bug.

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
