---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1031644'
original_report_id: '1031644'
title: DOM XSS on http://talks.lystit.com
weakness: Cross-site Scripting (XSS) - DOM
team_handle: lyst
created_at: '2020-11-11T15:09:33.360Z'
disclosed_at: '2021-02-09T11:38:16.383Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.lystit.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS on http://talks.lystit.com

## Metadata

- HackerOne Report ID: 1031644
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: lyst
- Disclosed At: 2021-02-09T11:38:16.383Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Description
DOM XSS can be achieved via a postMessage due to an insecure postMessage handler being registered.

#POC
1. Visit https://gamer7112.com/lyst_1.html
2. Click the link
3. View alert

#Vulnerable Code
Located at http://talks.lystit.com/data-saloon-presentation/plugin/notes/notes.html
```javascript
window.addEventListener('message', function(event) {
    var data = JSON.parse(event.data);

    // No need for updating the notes in case of fragment changes
    if (data.notes !== undefined) {
        if (data.markdown) {
            notes.innerHTML = marked(data.notes);
        } else {
            notes.innerHTML = data.notes;
        }
    }

    silenced = true;

    // Update the note slides
    currentSlide.contentWindow.Reveal.slide(data.indexh, data.indexv, data.indexf);
    nextSlide.contentWindow.Reveal.slide(data.nextindexh, data.nextindexv);

    silenced = false;

}, false);
```

## Impact

XSS allows for an attacker to execute arbitrary javascript on another user.

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
