---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '473950'
original_report_id: '473950'
title: XSS on Desktop Client
weakness: Cross-site Scripting (XSS) - DOM
team_handle: keybase
created_at: '2019-01-02T10:50:30.183Z'
disclosed_at: '2019-10-16T12:47:58.726Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 173
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS on Desktop Client

## Metadata

- HackerOne Report ID: 473950
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: keybase
- Disclosed At: 2019-10-16T12:47:58.726Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Steps to reproduce

1. Create a file named as `')*alert(1)*v.SS('.mp4` in the keybase public/private folder.
2. On the desktop client open the file as a preview.
3. An alert box pops up.

gif poc:
{F399836}

# The Problem

The [client/shared/fs/filepreview/av-view.desktop.js](https://github.com/keybase/client/blob/master/shared/fs/filepreview/av-view.desktop.js#L46-L54) file contains a template literal with the expression `${url}`.
```go
const webviewJavaScript = url => `
const v = document.createElement("video")
v.setAttribute('loop', true)
v.setAttribute('controls', true)
v.setAttribute('controlsList', 'nodownload nofullscreen')
v.setAttribute('src', '${url}')
document.getElementsByTagName('body')[0].appendChild(v)
v.play()
```
The url format is: `http://127.0.0.1:16723/files/public/u3mur4/vid.mp4?token=28d4356e6d3348d5b3cde2618df13324`. We can manipulate the filename part of the url, therefore the javascript code.

## Impact

limited loss of confidentiality and integrity

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
