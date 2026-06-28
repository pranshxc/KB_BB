---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-06_insufficient-redirect-uri-validation-the-risk-of-allowing-to-dynamically-add-arb.md
original_filename: 2021-11-06_insufficient-redirect-uri-validation-the-risk-of-allowing-to-dynamically-add-arb.md
title: 'Insufficient Redirect URI validation: The risk of allowing to dynamically
  add arbitrary query parameters and fragments to the redirect_uri'
category: documents
detected_topics:
- oauth
- sso
- access-control
- ssrf
- command-injection
- mfa
tags:
- imported
- documents
- oauth
- sso
- access-control
- ssrf
- command-injection
- mfa
language: en
raw_sha256: e7fbc8006e853e4339bdd163b8a9832aeace6d0f91daae6c18cac545e5464d3a
text_sha256: 0f560f29ddda5bddffdff0535fde266c39cd74f2b1902f3e8b1d2cc46963685f
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Insufficient Redirect URI validation: The risk of allowing to dynamically add arbitrary query parameters and fragments to the redirect_uri

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-06_insufficient-redirect-uri-validation-the-risk-of-allowing-to-dynamically-add-arb.md
- Source Type: markdown
- Detected Topics: oauth, sso, access-control, ssrf, command-injection, mfa
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `e7fbc8006e853e4339bdd163b8a9832aeace6d0f91daae6c18cac545e5464d3a`
- Text SHA256: `0f560f29ddda5bddffdff0535fde266c39cd74f2b1902f3e8b1d2cc46963685f`


## Content

---
title: "Insufficient Redirect URI validation: The risk of allowing to dynamically add arbitrary query parameters and fragments to the redirect_uri"
page_title: "(Web-)Insecurity Blog | Insufficient Redirect URI validation: The risk of allowing to dynamically add arbitrary query parameters and fragments to the redirect_uri"
url: "https://security.lauritz-holtmann.de/post/sso-security-redirect-uri-ii/"
final_url: "https://security.lauritz-holtmann.de/post/sso-security-redirect-uri-ii/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
programs: ["GitHub", "Microsoft", "StackExchange"]
bugs: ["OAuth", "Prototype pollution"]
publication_date: "2021-11-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3190
---

POSTS November 6, 2021 7 min read 1323 words

In this post, I will discuss an OAuth 2.0 and OpenID Connect 1.0 implementation flaw pattern that was or is present even in well-known implementations from [Github](https://developer.github.com/v3/oauth/), [Stackoverflow](https://api.stackexchange.com/docs/authentication) and [Microsoft](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols).

It has been observed in the wild that some Identity Provider (_Authorization Server_) implementations allow to dynamically add query parameters to the _Authorization Request_ and forward these parameters within the _Authorization Response_. As a result, depending on the Relying Party (_Client_) implementation, this pattern may enable [HTTP parameter pollution](https://en.wikipedia.org/wiki/HTTP_parameter_pollution) attacks.

### Background

The [OAuth 2.0 RFC](https://datatracker.ietf.org/doc/html/rfc6749) outlines how the `redirect_uri` parameter should be handled if present within the _Authorization Request_ :

> When a redirection URI is included in an authorization request, the authorization server MUST compare and match the value received against at least one of the registered redirection URIs (or URI components) as defined in [RFC3986] Section 6, if any redirection URIs were registered. If the client registration included the full redirection URI, the authorization server MUST compare the two URIs using simple string comparison as defined in [RFC3986] Section 6.2.1.
> 
> <https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2.3>

The `redirect_uri` is allowed to include query parameters:

> The redirection endpoint URI MUST be an absolute URI as defined by [RFC3986] Section 4.3. The endpoint URI MAY include an “application/x-www-form-urlencoded” formatted (per Appendix B) query component ([RFC3986] Section 3.4), which MUST be retained when adding additional query parameters. The endpoint URI MUST NOT include a fragment component.
> 
> <https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2>

Notably, these query parameters need to be **pre-registered** , so that the Authorization Server can apply the required simple string comparison to the entire provided `redirect_uri`.

Furthermore, apparently there is no clear definition how an implementation is supposed to handle multiple occurrences of the same query parameter. The original [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986#section-3.4) does not comment on this at all. Thus, different implementations and libraries handle this incident quite different, see [this talk](https://owasp.org/www-pdf-archive/AppsecEU09_CarettoniDiPaola_v0.8.pdf) (slide 9).

Recently Youssef Sammouda ([@samm0uda](https://twitter.com/samm0uda)) published a [blog post](https://ysamm.com/?p=708) with multiple bugs in Facebook’s OAuth implementation. The root cause of the very first vulnerability was also a parameter pollution issue.

### Implementation Inconsistencies

Even though the specification is quite strict regarding the `redirect_uri` validation, even popular implementations handle this crucial verification step lax.

A relatively harmless behaviour that was observed in the wild is to allow slight differences between the registered and provided redirect URI value but to stick to the registered value. For instance, Facebook was observed to accept additional query parameters on _Authorization Request_ , but for the _Authorization Response_ only the registered `redirect_uri` was used.

In contrast, Github as an example actually accepts not-registered query parameters and uses these parameters within the _Authorization Response._

### Impact

At worst, the aforementioned behaviour could enable a malicious actor to inject a controlled `code` into an OAuth 2.0 flow that is performed in a user’s browser and session. As a result, the end-user would be authenticated within the attacker-controlled account (see [Login CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#login-csrf)).

Apparently there is no up-to-date research on how implementations handle multiple occurrences of the same parameter. To my knowledge, the most recent research that was published dates back to 2009 ([OWASP EU09 Poland: HTTP Parameter Pollution](https://owasp.org/www-pdf-archive/AppsecEU09_CarettoniDiPaola_v0.8.pdf)), slide 9). Notably, according to this resource, some Java-based frameworks use the very first occurring parameter.

As an in-the-wild and up-to-date example, Keycloak can be configured as Service Provider and is written in Java. Some Java libraries handle query parameters with a “ _first come first serve_ ” approach. If Keycloak encounters multiple `code` values within the _Authorization Response_ , only the very first occurrence is processed.

### Limitations

If a `state` or `PKCE` is used, the aforementioned flaw most likely can not be directly exploited, as to craft a malicious _Authorization Request,_ a malicious actor would already be in possession of sensitive OAuth 2.0 parameters that would enable them to directly spoof the _Authorization Response_ , for instance a CSRF attack against a user.

### Example: Github

The following steps require a close look to the actual traffic and requests that are sent between the participating parties. Therefore, I recommend to use an intercepting proxy to observe the actual traffic. But at first we will use the shortcut without thoroughly analysing what is going on:

  1. Click the following link or open it in any browser: [https://github.com/login/oauth/authorize?client_id=01b478c0264a1fbd7183&scope=user:email&redirect_uri=https%3a%2f%2fstackauth.com%2fauth%2foauth2%2fgithub%3fcode%3dlauritz&state=aaaaaa&response_type=code](https://github.com/login/oauth/authorize?client_id=01b478c0264a1fbd7183&scope=user:email&redirect_uri=https%3a%2f%2fstackauth.com%2fauth%2foauth2%2fgithub%3fcode%3dlauritz&state=aaaaaa&response_type=code)
  2. Login at Github.
  3. Observe that you are redirected to [https://stackauth.com/auth/oauth2/github?code=lauritz&code=[REDACTED]&state=aaaaaa](https://stackauth.com/auth/oauth2/github?code=lauritz&code=%5BREDACTED%5D&state=aaaaaa)

Now let’s have a closer look at the outcomes of the login request: The value of the first `code` parameter in this request is `lauritz`, the latter `code` parameter holds the benign value issued from Github. The `code` parameter is crucial in OAuth 2.0 and would be used by the application in the following to retrieve a valid `access_token`.

_But how could this happen?_

Github does not sufficiently validate the `redirect_uri` parameter within the Authorization Request. The requests that are performed are as follows:

  1. With clicking the link, we launch a login flow (Authorization Request):

  
  
  GET /login/oauth/authorize?client_id=01b478c0264a1fbd7183&scope=user:email&redirect_uri=https%3a%2f%2fstackauth.com%2fauth%2foauth2%2fgithub%3fcode%3dlauritz&state=aaaaaa&response_type=code HTTP/2
  Host: github.com
  [...]
  

After authentication, Github responds with the Authorization Response whose destination is _stackauth.com_ :
  
  
  GET /auth/oauth2/github?code=lauritz&code=aaaaaaaaaaaaaaaaa&state=aaaaaa HTTP/1.1
  Host: stackauth.com
  

As you can see, Github embeds both, the real code value and the injected attacker-controlled “fake” code. The following steps then may be implementation specific to the Service Provider.

#### Responsible Disclosure Timeline

  * **2021-08-12** : Report via <https://hackerone.com/github>
  * **2021-08-12** : Report is closed as informative.
  * **2021-08-13** : Github gives permissions to disclose post.

* * *

### Example: Stackoverflow

The Stackoverflow OAuth 2.0 implementation (<https://api.stackexchange.com/docs/authentication>) implements a Single-Sign On flow using OAuth 2.0. An insufficient validation of the `redirect_uri` parameter within the Authorization Request allows to inject arbitrary parameters into the Authorization Response. _Strikingly, the implementation does only include each parameter once, allowing a malicious actor to overwrite response parameters_.

#### Steps to reproduce

The following application (client_id = 20816) with “OAuth Domain” `security.lauritz-holtmann.de` was registered at Stackoverflow.

An exemplary _Authorization Request_ looks as follows: [https://stackoverflow.com/oauth?client_id=20816&redirect_uri=https%3a%2f%2fsecurity.lauritz-holtmann.de%2f%3fcode%3dlauritz&response_type=code&state=a](https://stackoverflow.com/oauth?client_id=20816&redirect_uri=https%3a%2f%2fsecurity.lauritz-holtmann.de%2f%3fcode%3dlauritz&response_type=code&state=a)

The application responds as follows:
  
  
  HTTP/2 302 Found
  Cache-Control: private
  Location: https://security.lauritz-holtmann.de/?code=lauritz&state=a
  [...]
  

As one can see, the `code` parameter reflects the value that was previously injected with the Authorization Request (`redirect_uri`). Depending on the Service Provider implementation, this `code` would be directly used by the configured Service Provider.

In contrast, for a benign request ([https://stackoverflow.com/oauth?client_id=20816&redirect_uri=https%3a%2f%2fsecurity.lauritz-holtmann.de%2f&response_type=code&state=a)](https://stackoverflow.com/oauth?client_id=20816&redirect_uri=https%3a%2f%2fsecurity.lauritz-holtmann.de%2f&response_type=code&state=a\)), the response looks as follows:
  
  
  HTTP/2 302 Found
  Cache-Control: private
  Location: https://security.lauritz-holtmann.de/?code=r2iRH[...]&state=a
  [...]
  

#### Responsible Disclosure Timeline

  * **2021-08-23** : Initial report via <https://stackexchange.com/about/security>.
  * **2021-09-09** : Stackoverflow notifies about fix and agrees to disclose this post.

### Example: Microsoft

Microsoft’s _[login.live.com](https://login.live.com)_ as OAuth 2.0 Authorization Server allows to append arbitrary query parameters (`?`) and fragments (`#`) to registered `redirect_uri` values. This enables the injection of malicious `code` or `access_token` values, resulting in multiple `code` or `access_token` parameters being forwarded by the MS service.

An exemplary _Authorization Request_ is given in the following:
  
  
  GET /oauth20_authorize.srf?client_id=0000000000047086&response_type=token&redirect_uri=https%3a%2f%2fwww.office.com%2fhtml%2fMsaToken.html%23access_token%3dtest&response_mode=fragment&scope=onedrive_implicit.access&state=iframe%7Caaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaa&prompt=none HTTP/1.1
  Host: login.live.com
  [...]
  

After authentication, the Authorization Server responds with the _Authorization Response_ whose destination is _[www.office.com](https://www.office.com)_ :
  
  
  HTTP/1.1 302 Found
  Content-Type: text/html; charset=utf-8
  Location: https://www.office.com/html/MsaToken.html#access_token=test#access_token=[REDACTED]&token_type=bearer&expires_in=3600&scope=onedrive_implicit.access&state=iframe%7aaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaa
  [...]
  

As the above HTTP response illustrates, this _Authorization Response_ includes multiple `access_token` values within the fragment of the URL. The very first `access_token` was injected within the _Authorization Request_ and then reflected within the _Authorization Response_.

#### Responsible Disclosure Timeline

  * **2021-11-03** : Initial report via Microsoft Security Response Center (MSRC, <https://msrc.microsoft.com/)>.
  * **2021-11-03** : _MSRC_ informs that they do not consider this a vulnerability.

* * *

## References

  * [OAuth 2.0 RFC](https://datatracker.ietf.org/doc/html/rfc6749)
  * [OWASP: Login CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#login-csrf)
  * [OWASP EU09 Poland: HTTP Parameter Pollution, Luca Carettoni and Stefano di Paola](https://owasp.org/www-pdf-archive/AppsecEU09_CarettoniDiPaola_v0.8.pdf)
  * [YOUSSEF SAMMOUDA: More secure Facebook Canvas : Tale of $126k worth of bugs that lead to Facebook Account Takeovers](https://ysamm.com/?p=708)

* * *

* * *

Thank you for reading this post! If you have any feedback, feel free to reach out via [Mastodon](https://ruhr.social/@lauritz), [Twitter](https://twitter.com/_lauritz_) or [LinkedIn](https://linkedin.com/in/lauritz-holtmann). 👨‍💻

You can directly tweet about this post using [this link](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsecurity.lauritz-holtmann.de%2Fpost%2Fsso-redirect-uri%2F&via=_lauritz_). 🤓

If you are interested in _Single Sign-On Security_ , the following series of blog posts might be interesting for you:

  1. [[Overview] Common Issue Patterns and Derived Security Considerations](/post/sso-security-overview/)
  2. [[Implementation] Login Confusion](/post/sso-security-login-confusion/)
  3. [[Implementation] Injection of CRLF sequences](/post/sso-security-crlf-injection/)
  4. [[Implementation] SSRF issues in real-life OIDC implementations](/post/sso-security-ssrf/)
  5. [[Specification] Redirect URI Schemes](/post/sso-security-redirect-uri/)
  6. [[Specification] Reusable State parameter](/post/sso-security-state/)
  7. [[Responsible Disclosure] Lessons learned during Responsible Disclosure of OIDC/OAuth related issues](/post/sso-security-responsible-disclosure/)

Special thanks to the security teams of Github and Stackoverflow for the permission to disclose this blog post.

  * [OAuth](/tags/oauth)
  * [OIDC](/tags/oidc)
  * [Github](/tags/github)
  * [Stackoverflow](/tags/stackoverflow)
