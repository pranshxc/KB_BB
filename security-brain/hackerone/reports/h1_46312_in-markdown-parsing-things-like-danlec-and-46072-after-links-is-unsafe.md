---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46312'
original_report_id: '46312'
title: 'In markdown, parsing things like @danlec and #46072 after links is unsafe'
team_handle: security
created_at: '2015-02-03T15:18:26.640Z'
disclosed_at: '2015-07-04T19:12:43.228Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# In markdown, parsing things like @danlec and #46072 after links is unsafe

## Metadata

- HackerOne Report ID: 46312
- Weakness: 
- Program: security
- Disclosed At: 2015-07-04T19:12:43.228Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

(Let me preface this by saying that I haven't worked out an actual exploit for this, and there may not be one, but when #46072 is disclosed, folks will probably be taking a closer look at HackerOne's markdown parsing and may find a way to turn this bug into something)

It looks like the links for things like @danlec and #46072 are being added to the HTML after the initial markdown is processed; this leads to situations where links end up malformed because link markup is being added in an unexpected place (inside the attribute values of existing links)

For example:

```
[text](http://danlec.com " @danlec ")
```

renders as

[text](http://danlec.com " @danlec ")

i.e.

```
<p><a title=" <a href=" danlec"="">@danlec</a> " href="http://danlec.com"&gt;text</p>
```

As you can see, there's an unexpected `danlec"` attribute on the link tag.

The same kind of issue exists for references to other submissions, e.g.

```
[text](http://danlec.com " #46072 ")
```

renders as 

[text](http://danlec.com " #46072 ")

```
<p><a title=" <a href=" reports="" 46072"="">#46072</a> " href="http://danlec.com"&gt;text</p>
```

… with an  unexpected `reports` and `46072"` attribute

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
