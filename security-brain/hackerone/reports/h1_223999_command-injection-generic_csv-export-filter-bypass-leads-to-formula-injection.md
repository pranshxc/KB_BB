---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223999'
original_report_id: '223999'
title: CSV export filter bypass leads to formula injection.
weakness: Command Injection - Generic
team_handle: weblate
created_at: '2017-04-26T09:00:34.649Z'
disclosed_at: '2017-05-17T15:19:18.397Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- command-injection-generic
---

# CSV export filter bypass leads to formula injection.

## Metadata

- HackerOne Report ID: 223999
- Weakness: Command Injection - Generic
- Program: weblate
- Disclosed At: 2017-05-17T15:19:18.397Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear Weblate bug bounty team,

# Summary
---

The [new filter](https://github.com/WeblateOrg/weblate/commit/1216f65655ca4b3f32b9d59605eb4446d503bdbf) can be bypassed using: `%0A-3+3+cmd|' /C calc'!D2`.

~~~python
text = "%0A-3+3+cmd|' /C calc'!D2"
def csv_filter_bypass():
    if text and text[0] in ('=', '+', '-', '@'):
        return "'" + text
return text
~~~

# How can this be fixed?
---

You need to escape and detect more characters as follows:

~~~python
text = "%0A-3+3+cmd|' /C calc'!D2"
def csv_filter_fix():
    if text and text[0] in ('=', '+', '-', '@', '|', '%'):
        text = text.replace("|", "\|")
        return "'" + text + "'"
return text
~~~

You can compare your results with the following demonstration:

~~~python
text = "%0A-3+3+cmd|' /C calc'!D2"

def csv_filter_bypass():
    if text and text[0] in ('=', '+', '-', '@'):
        return "'" + text
    return text

def csv_filter_fix():
    if text and text[0] in ('=', '+', '-', '@', '|', '%'):
        text = text.replace("|", "\|")
        return "'" + text + "'"
    return text

csv_filter_bypass()
csv_filter_fix()
~~~

Best regards,
Ed

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
