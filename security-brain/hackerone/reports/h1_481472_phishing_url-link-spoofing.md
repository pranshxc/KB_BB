---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '481472'
original_report_id: '481472'
title: URL link spoofing
weakness: Phishing
team_handle: slack
created_at: '2019-01-17T14:26:13.026Z'
disclosed_at: '2020-04-26T03:53:43.641Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 356
asset_identifier: slack.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- phishing
---

# URL link spoofing

## Metadata

- HackerOne Report ID: 481472
- Weakness: Phishing
- Program: slack
- Disclosed At: 2020-04-26T03:53:43.641Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Words such as `http://example.com` and `example.com` included in the message are displayed by URL link. This URL link naturally links to `example.com`. However, we can spoof the link destination by changing the message post request.

```diff
 POST /api/chat.postMessage HTTP/1.1
 Host: example.slack.com
 ...

 ...
 -----------------------------87462859699239992111770463
 Content-Disposition: form-data; name="text"

-http://example.com
+<http://evil.com|http://example.com>
 -----------------------------87462859699239992111770463
 ...
```

The URL link `http://example.com` is displayed in the message, but in fact it is linked to `evil.com`. For example, like [http://example.com](http://evil.com).

{F408013}

I took a screenshot of Slack on Chrome, so the link destination is displayed in the status bar. However, desktop apps and mobile apps do not have a status bar.

## Impact

It is used for phishing attack. For example, an attacker posts a message like the following. Victims click on this URL link will lead to a fake login page.

{F408014}

In addition, [It is already known](https://twitter.com/buritica/status/970721576034455552) that we can create Slack accounts with the same name. Therefore, an attacker can increase the success rate of phishing by spoofing an influential person.

{F408015}

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
