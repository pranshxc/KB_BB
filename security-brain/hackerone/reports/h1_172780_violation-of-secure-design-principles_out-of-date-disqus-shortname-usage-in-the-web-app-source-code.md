---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172780'
original_report_id: '172780'
title: out of date disqus shortname usage in the web app source code
weakness: Violation of Secure Design Principles
team_handle: starbucks
created_at: '2016-09-29T01:06:46.364Z'
disclosed_at: '2017-08-12T01:40:57.248Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- violation-of-secure-design-principles
---

# out of date disqus shortname usage in the web app source code

## Metadata

- HackerOne Report ID: 172780
- Weakness: Violation of Secure Design Principles
- Program: starbucks
- Disclosed At: 2017-08-12T01:40:57.248Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Short definition of bug**: Misusage of an third-party web service in http://www.starbucks.com/

Hi Starbucks Bug Bounty Team, I found a vulnerability on your global website. I think you migrate your blog from http://www.starbucks.com/blog/archive/starbucks to https://1912pike.com/ and the blog path is also active and in-service still. Also the old blog posts are listed from the search in the main page of your website.

If we inspect the page source of any blog post page under the path http://www.starbucks.com/blog/ , we will see the disqus embedding codes still active.  

i.e. checkout the page source of this page:
http://www.starbucks.com/blog/starbucks-digital-network-content-highlights/612

```html
<script>
		
	var	disqus_params = {	shortname :'████', 
							developerMode : false, 
							hash :'██████████', 
							publicKey :'█████',
							identifier : 'TEST/blog/starbucks-digital-network-content-highlights/612',
							url :'http://www.starbucks.com/blog/starbucks-digital-network-content-highlights/612',
							ssoName : 'Starbucks',
							signinUrl : '/account/signin?skin=sdn&returnURL=/Disqus/CloseWindow',
							mobileSignInURL : '/account/signin?skin=sdn&returnURL=http://www.starbucks.com/blog/starbucks-digital-network-content-highlights/612',
							signoutURL : '/account/signout?skin=sdn&returnURL=/blog/starbucks-digital-network-content-highlights/612',
							signInButton : 'http://www.starbucks.com/static/images/signin.png', 
							signInIcon :'http://www.starbucks.com/static/images/sb-logo-16.gif'
						};
						
			
						/*TODO: Temp Hack*/

if( navigator.userAgent.match(/Android/i)
 || navigator.userAgent.match(/webOS/i)
 || navigator.userAgent.match(/iPhone/i)
 || navigator.userAgent.match(/iPad/i)
 || navigator.userAgent.match(/iPod/i)
 ){
	disqus_params.signinUrl="/account/signin?skin=sdn&returnURL=" + window.location.href;
}
	
</script>
```

and also at the end of source code

```html
<script src="/static/resource/disqus_js/1315595364_en-US"></script>
```

http://www.starbucks.com/static/resource/disqus_js/1315595364_en-US 
the js code is still in the server and in-service.

as you see in the page source code, the disqus shortname is ████ which is deprecated. I wonder and check from the disqus the “████████” shortname is not under usage. And i take that shortname as a regular user of disqus.  

Consequently whole the administration of “█████████” discussion board belongs to me. This is the best case. For a company -which is focused on customer pleasure and has total stores: 22,519* (as of June 28, 2015)- this fault can cause lots of impression such as;

- unconfirmed comments on your website
- unpleasant images as a default avatar in comments section
- undesired comments imported with older date can be shown as by name Starbucks etc.

I recommendation to solve this issue immediately;

remove the js code in blog post template code
let me know the time to transfer the ownership of “██████” disqus shortname

I am very pleased to report this issue instantly.

Have a nice work and thank you so much.

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
