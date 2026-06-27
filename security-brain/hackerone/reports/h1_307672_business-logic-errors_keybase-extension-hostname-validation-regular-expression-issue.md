---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '307672'
original_report_id: '307672'
title: Keybase extension hostname-validation regular expression issue.
weakness: Business Logic Errors
team_handle: keybase
created_at: '2018-01-21T16:31:07.679Z'
disclosed_at: '2018-01-26T14:58:19.407Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
tags:
- hackerone
- business-logic-errors
---

# Keybase extension hostname-validation regular expression issue.

## Metadata

- HackerOne Report ID: 307672
- Weakness: Business Logic Errors
- Program: keybase
- Disclosed At: 2018-01-26T14:58:19.407Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description

The following snippet in `js/identities.js` allows all hostnames ending in `twitter.com`, `facebook.com`, [etc.](https://github.com/keybase/client/blob/master/browser/js/identities.js#L24-L66) to display the Keybase message window. The issue stems from the fact that you use `\.` instead of `\\.` in your regular expression.

```js
{
    service: "twitter",
    getUsername: function(loc) { return loc.pathname.split('/')[1]; },
    locationMatches: new RegExp('\.twitter\.com/([\\w]+)[/]?$'),
    originAndPathMatches: '\.twitter\.com/[\\w]+[/]?$',
    css: ['body.ProfilePage']
  },
```

# PoC

```
$ cat /etc/hosts
IP_HERE totallynottwitter.com
```

Start up a little server and navigate to IP_HERE/edoverflow. Click on the Keybase extension's icon and the message window will pop up, tying @EdOverflow Twitter's identity to totallynottwitter.com.

{F256084}

# Mitigation

Make sure to use `\\.` in your regular expression.

## Impact

An attacker can create a fake page with any of the white-listed hostnames, and the extension's messaging window will open on the page.

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
