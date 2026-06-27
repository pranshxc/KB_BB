---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '306414'
original_report_id: '306414'
title: Window.opener protection  Bypass
team_handle: phabricator
created_at: '2018-01-18T19:32:10.878Z'
disclosed_at: '2018-02-17T20:25:25.864Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
---

# Window.opener protection  Bypass

## Metadata

- HackerOne Report ID: 306414
- Weakness: 
- Program: phabricator
- Disclosed At: 2018-02-17T20:25:25.864Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

SUMMURY
========
If you create a post/comment with a link  like http://x.com in fabricator then server add ```rel="norefferrer"``` to anchor tag . So child window dont have access to parent window.
But it can be bypassed with url like ```/\x.com/index.php``` and child window can change the location property of parent window.

STEP TO REPRODUCE
========================
1. goto http://domain/w/  and create new document.

2. Now paste  this code in content
```
[[ /\jackluru02.000webhostapp.com/tabnabbing.html | click_me ]]
```

code of this my url is
 ```
<script>
window.opener.location.replace('http://example.com');
</script>
```

3. now save it and share this document to other user.

4. When user click this click , malicious link opened in new window and parent window location will be changed.

{F255328}

## Impact

attacker can perform malicious activity to other user using this attack.

```
mongoose
```

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
