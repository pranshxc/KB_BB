---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-17_mobile-oauth-attacks-ios-url-scheme-hijacking-revamped.md
original_filename: 2024-06-17_mobile-oauth-attacks-ios-url-scheme-hijacking-revamped.md
title: Mobile OAuth Attacks - iOS URL Scheme Hijacking Revamped
category: documents
detected_topics:
- oauth
- mfa
- mobile-security
- sso
- access-control
- command-injection
tags:
- imported
- documents
- oauth
- mfa
- mobile-security
- sso
- access-control
- command-injection
language: en
raw_sha256: 2163cf8fc25e1986acfb6f67a6897f84e145d026332403a8fa6203a944090b10
text_sha256: 1ea0b0d9e52c64b28f16f29148753e4e86ffedd9b73d8a663ab335b1baa9e363
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Mobile OAuth Attacks - iOS URL Scheme Hijacking Revamped

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-17_mobile-oauth-attacks-ios-url-scheme-hijacking-revamped.md
- Source Type: markdown
- Detected Topics: oauth, mfa, mobile-security, sso, access-control, command-injection
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `2163cf8fc25e1986acfb6f67a6897f84e145d026332403a8fa6203a944090b10`
- Text SHA256: `1ea0b0d9e52c64b28f16f29148753e4e86ffedd9b73d8a663ab335b1baa9e363`


## Content

---
title: "Mobile OAuth Attacks - iOS URL Scheme Hijacking Revamped"
page_title: "Mobile OAuth Attacks - iOS URL Scheme Hijacking Revamped | Evan Connelly"
url: "https://evanconnelly.github.io/post/ios-oauth/"
final_url: "https://evanconnelly.github.io/post/ios-oauth/"
authors: ["Evan Connelly (@Evan_Connelly)", "Julien Ahrens (@MrTuxracer)"]
bugs: ["OAuth", "iOS", "URL scheme hijacking", "Account takeover"]
publication_date: "2024-06-17"
added_date: "2024-07-01"
source: "pentester.land/writeups.json"
original_index: 245
---

# Mobile OAuth Attacks - iOS URL Scheme Hijacking Revamped

June 18, 2024

## Summary#

We (Julien Ahrens [@MrTuxracer](https://x.com/MrTuxracer) and myself [@Evan_Connelly](https://x.com/Evan_Connelly)) identified nearly 30 popular apps, as well as a feature within iOS itself, vulnerable to an attack in which any installed iOS app from the Apple App Store could perform an account takeover of victim users.

This vulnerability exploits the nuances of the OAuth protocol and iOS’s handling of Custom URL Schemes and Safari browser sessions to steal OAuth Authentication Codes from vulnerable OAuth implementations, thereby allowing an attacker to gain access to a victim’s account.

While we’ve identified this vulnerability in quite a few apps, it’s all but certain that it exists in apps we were not able to test as well.

## Overview#

If you see this prompt on an iOS app, the app could be asking to hijack an account from any other app.

![Example](oauthy.jpeg)

This is because:

  * Many apps use an auth endpoint that, when opened with an existing session, can return an authentication code as part of an automatic redirect to a URI, which uses a custom URL scheme.

  * In iOS, it is possible to open a URL using an in-app browser via an ASWebAuthenticationSession instance, which:

  * Has access to session cookies from the Safari App

  * Can receive redirects to any custom URL scheme you specify

## The Technical Details#

### OAuth Client Apps for Mobile App Auth#

In a typical mobile OAuth flow, a redirect occurs from the Authorization Server (AS) back to the mobile application. On mobile, this almost always happens via a redirect to a custom URL scheme to get the redirect to reach the app.

### Custom URL Schemes#

Custom URL schemes allow you to define a URL scheme for your app, such as `exampleapp://`

As [Apple’s documentation explains](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Overview):

> Custom URL schemes provide a way to reference resources inside your app. Users tapping a custom URL in an email, for example, launch your app in a specified context. Other apps can also trigger your app to launch with specific context data; for example, a photo library app might display a specified image.

In theory, this means that once an app is installed, other apps would not be able to claim or use this scheme. However, in reality, it’s a bit wonky. Apple explains this in their [Developer documentation:](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app)

> Although using a reverse DNS string is a best practice, it doesn’t prevent other apps from registering the same scheme and handling the associated links. Use universal links instead of custom URL schemes to define links that are uniquely associated with your website.

and

> **Note**

> If multiple apps register the same scheme, the app the system targets is undefined. There’s no mechanism to change the app, or the order apps appear in a Share sheet.

In fact, URL schemes have some very interesting behavior. Of note, iOS does not prompt a user to redirect to a custom URL scheme if the redirect happens within an in-app browser and the app has registered that URL scheme. Furthermore, iOS will send the URL to the app that has opened the in-app browser, even if another app already has registered the URL scheme.

### URL Scheme Hijacking#

So, it would seem an attacker app could register any URL scheme, such as `fb` used by Facebook, and steal data sent via a redirect, right? While that is not the case anymore, it was once the case.

This previously made headlines: <https://thehackernews.com/2019/07/ios-custom-url-scheme.html?m=1>

Based on the research here: <https://web.archive.org/web/20191030235352/https://blog.trendmicro.com/trendlabs-security-intelligence/ios-url-scheme-susceptible-to-hijacking/>

This is largely mitigated now, as iOS seems to have a first-come-first-serve principle in routing URL schemes to apps. So, if you’ve already installed Facebook, another app can’t steal the URL scheme.

There is also a significant mitigating factor here. In the attack scenario of this behavior being used for an account takeover in an OAuth flow, the attacker would need to get the victim user to open the auth endpoint of the victim app in the Safari app. The victim user would then need to click through the iOS TCC prompt to allow the redirect with the auth code to go to the attacker app. This is quite complex and represents a fairly unlikely attack scenario.

We were able to create a far more feasible and concerning attack scenario due to the behavior of and use of the below components:

### ASWebAuthenticationSession#

In iOS, [ASWebAuthenticationSession](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/2990952-init#parameters) offers an in-app browser with access to data, including cookies from the Safari App. This is meant to help make SSO easier and faster. So, if you’re logged in inside Safari, the `ASWebAuthenticationSession` in-app browser has you logged in, too. To mitigate the inherent risk, a confirmation prompt shows the domain you’re opening.

But that is imperfect as the URL being opened could potentially be redirected to obscure the actual destination.

### Silent Authentication#

A big part of pulling this off was discovering that you can set a `prompt=none` parameter in many OAuth flows, which removes all user interaction in the OAuth flow. As Auth0 explains:

<https://auth0.com/docs/authenticate/login/configure-silent-authentication>

> The [OpenID Connect protocol](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol) supports a `prompt=none` parameter on the authentication request that allows applications to indicate that the authorization server must not display any user interaction (such as authentication, consent, or MFA). Auth0 will either return the requested response back to the application, or return an error if the user is not already authenticated or if some type of consent or prompt is required before proceeding.

### Connecting the Dots#

To demonstrate this issue, we built PoC apps for each vulnerable target we identified. The PoC app would use `ASWebAuthenticationSession` to open an endpoint on one of our websites, such as evanconnelly.com, that was configured to redirect to the OAuth client app of the victim app. This meant iOS would ask for permission to open `evanconnelly.com` rather than `victim.com`.

Behind the scenes, if a user of the app were to allow the app to open our website, they were immediately redirected to the OAuth client app of the victim application.

Thanks to the `prompt=none` parameter, the auth flow would be completed silently without user interaction.

If they had an active session on the victim domain, an authentication code would be sent to our app via the victim app’s custom URL scheme, which can be registered within the ASWebAuthenticationSession instance.

Once the code was received, our app was configured to trade it for an access token in the same way the vulnerable application itself would.

Of note here is that common OAuth protections such as PKCE do not mitigate this attack scenario. With PKCE, for example, because our PoC app was opening the client app and receiving the redirect, we could specify our own `code_challenge` value and our own `code_verifier` later in the code exchange.

A bit of what this looks like in Swift:
  
  
  import AuthenticationServices
  
  
  
  @State private var asWebAuthURL: String = "https://evanconnelly.com/redirect?to=https%3A%2F%2Fexample.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dexample%26redirect_uri%3Dexampleapp%3A%2F%2Foauth%2Fcallback%26scope%3Dopenid%2520profile%2520email%26prompt%3Dnone"
  
  @State private var asWebAuthScheme: String = "exampleapp"
  
  ...  
  
  private func startASWebAuthenticationSession() {
  guard let authURL = URL(string: asWebAuthURL) else { return }
  let session = ASWebAuthenticationSession(url: authURL, callbackURLScheme: asWebAuthScheme) { callbackURL, error in
  if let callbackURL = callbackURL {
  self.openedURL = callbackURL
  if let code = self.extractCode(from: callbackURL) {
  self.obtainAccessToken(using: code)
  }
  }
  }
  session.presentationContextProvider = asWebAuthContextProvider
  session.start()
  }
  

## Mitigation#

App Store review is not a mitigation here. Apple’s review process does not look at the app’s source code, and even if it did, because this attack utilizes a redirect, it could easily be hidden during the review process. Unless Apple changes the behavior of ASWebAuthenticationSession, the onus is on developers to mitigate this.

This attack scenario could be mitigated by using universal links rather than custom URL schemes in the OAuth flow or by requiring a consent step (not automatically authorizing this OAuth client and redirecting to the redirect URL without user interaction).

As mentioned earlier, Apple offers Universal Links that are not hijackable, meaning an attacker would not be able to receive the redirect with the authentication code.

Additionally, per [RFC 6819](https://datatracker.ietf.org/doc/html/rfc6819#section-5.2.4.1), the authorization server should not perform automatic re-authorizations for clients it is unable to authenticate or validate reliably

> **Section 5.2.4.1**

> Authorization servers should NOT automatically process repeat authorizations where the client is not authenticated through a client secret or some other authentication mechanism, such as a signed authentication assertion certificate (Section 5.2.3.7) or validation of a pre-registered redirect URI (Section 5.2.3.5).

## Closing Shoutout#

Thanks to Joseph Thacker [(@rez0__)](https://x.com/rez0__?) for connecting Julien and I and for encouraging us throughout the course of our research, as well as creating some amazing AI generated art for the app icon app of our PoC app.
