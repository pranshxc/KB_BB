---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-07-20_bypassing-google-authentication-on-periscopes-administration-panel.md
original_filename: 2015-07-20_bypassing-google-authentication-on-periscopes-administration-panel.md
title: Bypassing Google Authentication on Periscope's Administration Panel
category: documents
detected_topics:
- oauth
- mobile-security
- xss
- command-injection
- mfa
- otp
tags:
- imported
- documents
- oauth
- mobile-security
- xss
- command-injection
- mfa
- otp
language: en
raw_sha256: 919c71d2762acdb2655752b261e96168ab581e25706e99557beb6b94a767048b
text_sha256: 3d84bd927bcacc0fb60e61f4321e23d0ad46d384e5688255196db859d5874589
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Google Authentication on Periscope's Administration Panel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-07-20_bypassing-google-authentication-on-periscopes-administration-panel.md
- Source Type: markdown
- Detected Topics: oauth, mobile-security, xss, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `919c71d2762acdb2655752b261e96168ab581e25706e99557beb6b94a767048b`
- Text SHA256: `3d84bd927bcacc0fb60e61f4321e23d0ad46d384e5688255196db859d5874589`


## Content

---
title: "Bypassing Google Authentication on Periscope's Administration Panel"
page_title: "Bypassing Google Authentication on Periscope's Administration Panel – Jack"
url: "https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/"
final_url: "https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Google"]
bugs: ["Authentication bypass"]
publication_date: "2015-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6338
---

# [Bypassing Google Authentication on Periscope's Administration Panel](https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/ "Bypassing Google Authentication on Periscope's Administration Panel")

## July 20, 2015

__Reading time ~2 minutes

I haven’t blogged for quite some time, so I thought it was worth re-launching with an interesting, albeit simple, high-impact bug.

[Periscope](https://www.periscope.tv/) is an iOS/Android app, owned by Twitter, used for live streaming. To manage the millions of users, a web-based administation panel is used, accessible at [admin.periscope.tv](https://admin.periscope.tv).

When you browse to the site, all requests are redirected to `/auth?redirect=/` (since we don’t have a valid session), which in turn redirects to [Google for authentication](https://developers.google.com/identity/protocols/OpenIDConnect).

[ ![](/images/periscope/periscope-admin-panel-1.png) ](/images/periscope/periscope-admin-panel-1.png)

The redirected URL, shown below, contains various parameters, but the most interesting one is `hd`. This is used to [restrict logins to a specific domain](https://developers.google.com/identity/protocols/OpenIDConnect#hd-param), in this case `bountyapp.co`.
  
  
  https://accounts.google.com/o/oauth2/auth?access_type=
  &approval_prompt=
  &client_id=57569323683-c0hvkac6m15h3u3l53u89vpquvjiu8sb.apps.googleusercontent.com
  **& hd=bountyapp.co**
  &redirect_uri=https%3A%2F%2Fadmin.periscope.tv%2Fauth%2Fcallback
  &response_type=code
  &scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fplus.login+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile
  &state=%2FStreams
  

If we try and login with an account such as `[[email protected]](/cdn-cgi/l/email-protection)`, we’re redirected back to the account selection page, and if we try again we get redirected back to the same place, and so on.

[ ![](/images/periscope/periscope-admin-panel-2.png) ](/images/periscope/periscope-admin-panel-2.png)

However, we can simply remove this parameter. There’s no signature in the URL to prevent us from making modifications, and as indicated in the documentation, the onus is on the application to validate the returned token.

This gives us the following login URL (you may also notice I’ve removed the Google+ scope, this is purely because my test account isn’t signed up for it):
  
  
  https://accounts.google.com/o/oauth2/auth?access_type=
  &approval_prompt=
  &client_id=57569323683-c0hvkac6m15h3u3l53u89vpquvjiu8sb.apps.googleusercontent.com
  &redirect_uri=https%3A%2F%2Fadmin.periscope.tv%2Fauth%2Fcallback
  &response_type=code
  &scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile
  &state=%2FStreams
  

Browsing to this new URL prompts us to authorise the application.

[ ![](/images/periscope/periscope-admin-panel-3.png) ](/images/periscope/periscope-admin-panel-3.png)

After clicking “Accept”, a redirect is issused back to the administation panel, with our code as a parameter.

[ ![](/images/periscope/periscope-admin-panel-4.png) ](/images/periscope/periscope-admin-panel-4.png)

This is where the application should then exchange the code for an access token, and validate the returned user ID against either a whitelist, or at the very least verify that the domain is `bountyapp.co`.

But, in this case, the assumption is made that if you managed to login, you are an employee with an `@bountyapp.co` email.

The requested `[userinfo.profile](https://developers.google.com/+/web/api/rest/oauth#userinfo.profile)` permission doesn’t contain the user’s email address, so the application can’t validate it if it tried.

This then presents us with the admin panel.

[ ![](/images/periscope/periscope-admin-panel-5.png) ](/images/periscope/periscope-admin-panel-5.png)

From here we can now manage various aspects of Periscope, including users and streams.

#### Fix

Twitter fixed this by making two changes. The first is to request an additional permission:
  
  
  https://www.googleapis.com/auth/userinfo.email
  

The second is to correctly validate the user on callback.

Now, the application returns a 401 when trying to authenticate with an invalid user:
  
  
  HTTP/1.1 401 Unauthorized
  Content-Type: text/html; charset=utf-8
  Location: /Login
  Strict-Transport-Security: max-age=31536000; preload
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  X-Xss-Protection: 1; mode=block
  Content-Length: 36
  
  <href="/Login">Unauthorized</a>.
  

[websec](https://whitton.io/tags/#websec "Pages tagged websec")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[authentication](https://whitton.io/tags/#authentication "Pages tagged authentication")[periscope](https://whitton.io/tags/#periscope "Pages tagged periscope")[twitter](https://whitton.io/tags/#twitter "Pages tagged twitter") Updated on July 20, 2015 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/ "Share on Google Plus")

[Read More](https://whitton.io/articles/bug-bounties-101-getting-started/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
